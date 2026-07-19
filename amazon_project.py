"""Review the raw-to-final Amazon marketplace cleaning workflow.

This script keeps the original exploratory cleaning logic concise and runnable
from the repository root. It does not overwrite the curated final dataset.
"""

from pathlib import Path
import re

import numpy as np
import pandas as pd


PROJECT_DIR = Path(__file__).resolve().parent
RAW_PATH = PROJECT_DIR / "amazon_products_sales_data_uncleaned.csv"
FINAL_PATH = PROJECT_DIR / "amazon_FINAL.csv"


def parse_purchase_volume(value):
    """Convert Amazon purchase badges such as '6K+ bought...' to numbers."""
    if pd.isna(value):
        return np.nan
    match = re.fullmatch(
        r"\s*([\d,.]+)\s*([kKmM]?)\+?\s+bought in past month\s*",
        str(value),
    )
    if not match:
        return np.nan
    number = float(match.group(1).replace(",", ""))
    multiplier = {"": 1, "k": 1_000, "m": 1_000_000}[match.group(2).lower()]
    return number * multiplier


def parse_currency(series):
    """Convert currency-like strings to numeric values."""
    return pd.to_numeric(
        series.astype("string")
        .str.replace("$", "", regex=False)
        .str.replace(",", "", regex=False),
        errors="coerce",
    )


def extract_asin(url):
    """Extract an ASIN from a directly accessible Amazon product URL."""
    if pd.isna(url):
        return None
    match = re.search(r"/dp/([A-Z0-9]{10})", str(url), flags=re.I)
    return match.group(1).upper() if match else None


def clean_raw_data(raw):
    """Apply the core parsing rules used to evaluate the scraped dataset."""
    cleaned = raw.rename(
        columns={
            "title": "product_title",
            "rating": "product_rating",
            "number_of_reviews": "total_reviews",
            "bought_in_last_month": "purchased_last_month",
            "current/discounted_price": "discounted_price",
            "listed_price": "original_price",
            "is_couponed": "has_coupon",
            "delivery_details": "delivery_date",
            "sustainability_badges": "sustainability_tags",
            "image_url": "product_image_url",
            "product_url": "product_page_url",
            "collected_at": "data_collected_at",
        }
    ).copy()

    cleaned["product_rating"] = pd.to_numeric(
        cleaned["product_rating"].astype("string").str.extract(r"(\d+(?:\.\d+)?)")[0],
        errors="coerce",
    )
    cleaned["total_reviews"] = pd.to_numeric(
        cleaned["total_reviews"].astype("string").str.replace(",", "", regex=False),
        errors="coerce",
    )
    cleaned["purchased_last_month"] = cleaned["purchased_last_month"].apply(
        parse_purchase_volume
    )
    cleaned["discounted_price"] = parse_currency(cleaned["discounted_price"])
    cleaned["original_price"] = parse_currency(cleaned["original_price"])
    cleaned["data_collected_at"] = pd.to_datetime(
        cleaned["data_collected_at"], errors="coerce"
    )
    cleaned["asin"] = cleaned["product_page_url"].apply(extract_asin)
    return cleaned


def deduplicate_products(cleaned):
    """Keep the latest ASIN snapshot and a documented fallback for missing ASINs."""
    ordered = cleaned.sort_values("data_collected_at")

    with_asin = ordered[ordered["asin"].notna()].drop_duplicates(
        subset="asin", keep="last"
    )
    without_asin = ordered[ordered["asin"].isna()].drop_duplicates(
        subset=["product_title", "product_rating", "total_reviews"], keep="last"
    )
    combined = pd.concat([with_asin, without_asin], ignore_index=True)

    # Resolve overlap between sponsored and organic records that describe the
    # same titled product, retaining the most recent snapshot.
    return combined.sort_values("data_collected_at").drop_duplicates(
        subset="product_title", keep="last"
    )


def main():
    raw = pd.read_csv(RAW_PATH)
    final = pd.read_csv(FINAL_PATH)
    cleaned = clean_raw_data(raw)
    deduplicated = deduplicate_products(cleaned)

    malformed_purchase_values = (
        raw["bought_in_last_month"].notna()
        & cleaned["purchased_last_month"].isna()
    ).sum()

    print(f"Raw observations: {len(raw):,}")
    print(f"Collection window: {raw['collected_at'].min()} to {raw['collected_at'].max()}")
    print(f"Distinct raw titles: {raw['title'].nunique():,}")
    print(
        "Malformed non-null purchase values: "
        f"{malformed_purchase_values:,} "
        f"({malformed_purchase_values / len(raw):.1%})"
    )
    print(f"ASINs extracted from raw URLs: {cleaned['asin'].notna().sum():,}")
    print(f"Exploratory deduplicated rows: {len(deduplicated):,}")
    print(f"Curated final rows: {len(final):,}")
    print(f"Curated final unique ASINs: {final['asin'].nunique():,}")
    print("\nFinal missing values in key fields:")
    print(
        final[
            [
                "discounted_price",
                "product_rating",
                "total_reviews",
                "purchased_last_month",
            ]
        ].isna().sum()
    )


if __name__ == "__main__":
    main()
