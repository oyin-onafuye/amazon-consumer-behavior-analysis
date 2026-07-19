"""Analyze the final Amazon marketplace dataset and export portfolio visuals."""

from pathlib import Path

import pandas as pd
from PIL import Image, ImageDraw, ImageFont


PROJECT_DIR = Path(__file__).resolve().parent
DATA_PATH = PROJECT_DIR / "amazon_FINAL.csv"
CHART_DATA_DIR = PROJECT_DIR / "chart_data"

PRICE_LABELS = ["<$25", "$25–99", "$100–499", "$500–1,999", "$2,000+"]
PRICE_BINS = [float("-inf"), 25, 100, 500, 2000, float("inf")]
REVIEW_LABELS = ["1–99", "100–999", "1K–9,999", "10K–99,999", "100K+"]
REVIEW_BINS = [0, 100, 1000, 10000, 100000, float("inf")]

BURGUNDY = "#941F1F"
DARK_BURGUNDY = "#6F1515"
CHARCOAL = "#292929"
MID_GRAY = "#777777"
LIGHT_GRAY = "#E8E4E1"
PALE = "#F7F4F2"
WHITE = "#FFFFFF"

FONT_REGULAR = "/System/Library/Fonts/Supplemental/Arial.ttf"
FONT_BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
FONT_SYMBOL = "/System/Library/Fonts/Apple Symbols.ttf"


def font(size, bold=False):
    path = FONT_BOLD if bold else FONT_REGULAR
    try:
        return ImageFont.truetype(path, size)
    except OSError:
        return ImageFont.load_default()


def symbol_font(size):
    try:
        return ImageFont.truetype(FONT_SYMBOL, size)
    except OSError:
        return font(size, bold=True)


def add_price_tier(df):
    result = df.copy()
    result["price_tier"] = pd.cut(
        result["discounted_price"],
        PRICE_BINS,
        labels=PRICE_LABELS,
        right=False,
        ordered=True,
    )
    return result


def build_summaries(df):
    priced = add_price_tier(df[df["discounted_price"].notna()])
    price_summary = (
        priced.groupby("price_tier", observed=False)
        .agg(
            products=("product_title", "size"),
            avg_rating=("product_rating", "mean"),
            avg_reviews=("total_reviews", "mean"),
            avg_purchases_last_month=("purchased_last_month", "mean"),
            purchase_values=("purchased_last_month", "count"),
        )
        .reset_index()
    )

    reviewed = df[df["total_reviews"].notna()].copy()
    reviewed["review_tier"] = pd.cut(
        reviewed["total_reviews"],
        REVIEW_BINS,
        labels=REVIEW_LABELS,
        right=False,
        ordered=True,
    )
    review_summary = (
        reviewed.groupby("review_tier", observed=False)
        .agg(
            products=("product_title", "size"),
            avg_rating=("product_rating", "mean"),
            avg_price=("discounted_price", "mean"),
        )
        .reset_index()
    )

    category_summary = (
        df.groupby("product_category")
        .agg(
            products=("product_title", "size"),
            avg_price=("discounted_price", "mean"),
            avg_rating=("product_rating", "mean"),
            avg_reviews=("total_reviews", "mean"),
            avg_purchases_last_month=("purchased_last_month", "mean"),
        )
        .reset_index()
        .sort_values("avg_reviews", ascending=False)
    )
    return price_summary, review_summary, category_summary


def export_chart_data(price_summary, review_summary, category_summary):
    CHART_DATA_DIR.mkdir(exist_ok=True)
    price_summary.round(2).to_csv(
        CHART_DATA_DIR / "price_tier_summary.csv", index=False
    )
    review_summary.round(2).to_csv(
        CHART_DATA_DIR / "review_tier_summary.csv", index=False
    )
    category_summary.round(2).to_csv(
        CHART_DATA_DIR / "category_summary.csv", index=False
    )


def text(draw, xy, value, size, color=CHARCOAL, bold=False, anchor=None):
    draw.text(xy, str(value), font=font(size, bold), fill=color, anchor=anchor)


def title_block(draw, title, subtitle=None, width=1400):
    text(draw, (70, 48), title, 30, DARK_BURGUNDY, True)
    if subtitle:
        text(draw, (70, 92), subtitle, 17, MID_GRAY)
    draw.line((70, 126, width - 70, 126), fill=LIGHT_GRAY, width=2)


def draw_price_chart(price_summary):
    width, height = 1400, 820
    image = Image.new("RGB", (width, height), WHITE)
    draw = ImageDraw.Draw(image)
    title_block(
        draw,
        "Lower-Priced Products Lead in Reviews; Ratings Stay Similar",
        "Average reviews and ratings across five price tiers • 8,382 products with price data",
        width,
    )

    labels = price_summary["price_tier"].astype(str).tolist()
    reviews = price_summary["avg_reviews"].tolist()
    ratings = price_summary["avg_rating"].tolist()
    counts = price_summary["products"].tolist()

    left, right = 115, 1325
    top, split, bottom = 190, 495, 725
    gap = (right - left) / len(labels)
    bar_w = gap * 0.48
    max_review = 15000

    for tick in [0, 5000, 10000, 15000]:
        y = split - tick / max_review * (split - top)
        draw.line((left, y, right, y), fill=LIGHT_GRAY, width=1)
        text(draw, (left - 16, y), f"{tick//1000}K" if tick else "0", 14, MID_GRAY, anchor="rm")

    for i, (label, value, rating, count) in enumerate(
        zip(labels, reviews, ratings, counts)
    ):
        x = left + gap * (i + 0.5)
        y = split - value / max_review * (split - top)
        color = BURGUNDY if i == 0 else "#B9B2AE"
        draw.rounded_rectangle(
            (x - bar_w / 2, y, x + bar_w / 2, split),
            radius=4,
            fill=color,
        )
        text(draw, (x, y - 14), f"{value:,.0f}", 17, color, True, anchor="ms")
        text(draw, (x, bottom + 18), label, 16, CHARCOAL, True, anchor="ma")
        text(draw, (x, bottom + 48), f"n={count:,}", 13, MID_GRAY, anchor="ma")

    rating_min, rating_max = 4.30, 4.60
    rating_top, rating_bottom = 550, 690
    points = []
    for i, rating in enumerate(ratings):
        x = left + gap * (i + 0.5)
        y = rating_bottom - (rating - rating_min) / (rating_max - rating_min) * (
            rating_bottom - rating_top
        )
        points.append((x, y))
    draw.line(points, fill=DARK_BURGUNDY, width=4, joint="curve")
    for x, y in points:
        draw.ellipse((x - 7, y - 7, x + 7, y + 7), fill=DARK_BURGUNDY)
    for (x, y), rating in zip(points, ratings):
        text(draw, (x, y - 16), f"{rating:.2f}", 16, DARK_BURGUNDY, True, anchor="ms")

    text(draw, (70, 320), "AVG. REVIEWS", 14, MID_GRAY, True, anchor="mm")
    text(draw, (70, 620), "AVG. RATING", 14, MID_GRAY, True, anchor="mm")
    image.save(PROJECT_DIR / "Price vs Volume Quality.png")


def draw_review_chart(review_summary):
    width, height = 1200, 720
    image = Image.new("RGB", (width, height), WHITE)
    draw = ImageDraw.Draw(image)
    title_block(
        draw,
        "Higher Review Counts Align With Slightly Higher Ratings",
        "Average rating by review tier • 8,741 products with review data",
        width,
    )

    labels = review_summary["review_tier"].astype(str).tolist()
    ratings = review_summary["avg_rating"].tolist()
    counts = review_summary["products"].tolist()
    left, right, top, bottom = 120, 1120, 205, 575

    for tick in [4.30, 4.40, 4.50, 4.60]:
        y = bottom - (tick - 4.30) / 0.35 * (bottom - top)
        draw.line((left, y, right, y), fill=LIGHT_GRAY, width=1)
        text(draw, (left - 18, y), f"{tick:.2f}", 15, MID_GRAY, anchor="rm")

    gap = (right - left) / (len(labels) - 1)
    points = []
    for i, rating in enumerate(ratings):
        x = left + gap * i
        y = bottom - (rating - 4.30) / 0.35 * (bottom - top)
        points.append((x, y))
    draw.line(points, fill=BURGUNDY, width=5, joint="curve")

    for (x, y), label, rating, count in zip(points, labels, ratings, counts):
        draw.ellipse((x - 9, y - 9, x + 9, y + 9), fill=BURGUNDY)
        text(draw, (x, y - 20), f"{rating:.2f}", 17, DARK_BURGUNDY, True, anchor="ms")
        text(draw, (x, bottom + 48), label, 15, CHARCOAL, True, anchor="ma")
        text(draw, (x, bottom + 76), f"n={count:,}", 13, MID_GRAY, anchor="ma")

    image.save(PROJECT_DIR / "Review Tier vs Avg Rating.png")


def draw_category_chart(category_summary):
    width, height = 1500, 940
    image = Image.new("RGB", (width, height), WHITE)
    draw = ImageDraw.Draw(image)
    title_block(
        draw,
        "Customer Review Volume Varies Widely by Category",
        "Average reviews by category • product counts shown for context",
        width,
    )

    rows = category_summary.reset_index(drop=True)
    left, right, top, bottom = 285, 1300, 170, 875
    row_h = (bottom - top) / len(rows)
    max_value = 23000

    for tick in [0, 5000, 10000, 15000, 20000]:
        x = left + tick / max_value * (right - left)
        draw.line((x, top, x, bottom), fill=LIGHT_GRAY, width=1)
        text(draw, (x, bottom + 25), f"{tick//1000}K" if tick else "0", 13, MID_GRAY, anchor="ma")

    for i, row in rows.iterrows():
        y = top + row_h * (i + 0.5)
        value = row["avg_reviews"]
        x = left + value / max_value * (right - left)
        color = BURGUNDY if i < 3 else "#A9A3A0"
        text(draw, (left - 18, y), row["product_category"], 15, CHARCOAL, anchor="rm")
        draw.rounded_rectangle((left, y - 8, x, y + 8), radius=4, fill=color)
        text(draw, (x + 12, y), f"{value:,.0f}", 14, CHARCOAL, True, anchor="lm")
        text(draw, (1420, y), f"n={int(row['products']):,}", 12, MID_GRAY, anchor="rm")

    image.save(PROJECT_DIR / "Category.png")


def draw_dashboard(price_summary, review_summary, category_summary, raw_rows):
    width, height = 1600, 1120
    image = Image.new("RGB", (width, height), WHITE)
    draw = ImageDraw.Draw(image)

    text(draw, (70, 48), "Price Influences Customer Engagement, Not Ratings", 34, DARK_BURGUNDY, True)
    text(
        draw,
        (70, 96),
        (
            f"Analysis of {len(pd.read_csv(DATA_PATH)):,} deduplicated Amazon listings from {raw_rows:,} scrape observations • "
            "Review volume and recent-purchase activity vary far more across price tiers than customer ratings"
        ),
        18,
        MID_GRAY,
    )

    budget = price_summary.iloc[0]
    premium = price_summary.iloc[3]
    review_ratio = budget["avg_reviews"] / premium["avg_reviews"]
    rating_spread = price_summary["avg_rating"].max() - price_summary["avg_rating"].min()
    cards = [
        ("8,806", ["Marketplace Listings Analyzed"]),
        (f"{review_ratio:.1f}×", ["Higher Average Review Volume", "<$25 vs. $500–1,999"]),
        (
            f"{rating_spread:.2f}★",
            ["Maximum Difference in Average Rating", "Across Five Price Tiers"],
        ),
    ]
    card_y = 155
    card_w = 455
    for i, (value, label_lines) in enumerate(cards):
        x = 70 + i * 500
        draw.rounded_rectangle((x, card_y, x + card_w, card_y + 145), radius=10, fill=PALE)
        if i == 2:
            number = value.removesuffix("★")
            number_font = font(44, bold=True)
            draw.text((x + 24, card_y + 25), number, font=number_font, fill=CHARCOAL)
            star_x = x + 24 + draw.textlength(number, font=number_font) + 3
            draw.text(
                (star_x, card_y + 31),
                "★",
                font=symbol_font(35),
                fill=CHARCOAL,
            )
        else:
            text(draw, (x + 24, card_y + 25), value, 44, BURGUNDY if i == 1 else CHARCOAL, True)
        label_y = card_y + 99 if len(label_lines) == 1 else card_y + 88
        for line_number, label in enumerate(label_lines):
            text(draw, (x + 24, label_y + line_number * 25), label, 15, MID_GRAY)

    text(draw, (70, 355), "Customer Engagement Across Price Tiers", 22, CHARCOAL, True)
    labels = price_summary["price_tier"].astype(str).tolist()
    reviews = price_summary["avg_reviews"].tolist()
    ratings = price_summary["avg_rating"].tolist()
    chart_left, chart_right, chart_top, chart_bottom = 90, 760, 410, 680
    gap = (chart_right - chart_left) / len(labels)
    for i, (label, value, rating) in enumerate(zip(labels, reviews, ratings)):
        x = chart_left + gap * (i + 0.5)
        y = chart_bottom - value / 15000 * (chart_bottom - chart_top)
        color = BURGUNDY if i == 0 else "#B8B1AD"
        draw.rectangle((x - 35, y, x + 35, chart_bottom), fill=color)
        text(draw, (x, y - 12), f"{value/1000:.1f}K", 13, color, True, anchor="ms")
        text(draw, (x, chart_bottom + 26), label, 12, CHARCOAL, True, anchor="ma")
        text(draw, (x, chart_bottom + 52), f"rating {rating:.2f}", 12, MID_GRAY, anchor="ma")

    text(draw, (855, 355), "Ratings Across Review Tiers", 22, CHARCOAL, True)
    rlabels = review_summary["review_tier"].astype(str).tolist()
    rvalues = review_summary["avg_rating"].tolist()
    rleft, rright, rtop, rbottom = 875, 1510, 430, 660
    rgap = (rright - rleft) / (len(rlabels) - 1)
    pts = []
    for i, value in enumerate(rvalues):
        x = rleft + rgap * i
        y = rbottom - (value - 4.30) / 0.35 * (rbottom - rtop)
        pts.append((x, y))
    draw.line(pts, fill=BURGUNDY, width=4)
    for (x, y), label, value in zip(pts, rlabels, rvalues):
        draw.ellipse((x - 7, y - 7, x + 7, y + 7), fill=BURGUNDY)
        text(draw, (x, y - 15), f"{value:.2f}", 13, DARK_BURGUNDY, True, anchor="ms")
        text(draw, (x, rbottom + 28), label, 11, CHARCOAL, anchor="ma")

    text(draw, (70, 790), "Review Volume Across Product Categories", 22, CHARCOAL, True)
    top_categories = category_summary.head(8)
    max_category = top_categories["avg_reviews"].max()
    for i, row in top_categories.reset_index(drop=True).iterrows():
        y = 845 + i * 30
        x = 300 + row["avg_reviews"] / max_category * 1000
        text(draw, (280, y), row["product_category"], 14, CHARCOAL, anchor="rm")
        draw.rounded_rectangle((300, y - 7, x, y + 7), radius=3, fill=BURGUNDY if i < 3 else "#AAA4A0")
        text(draw, (x + 10, y), f"{row['avg_reviews']:,.0f}", 13, CHARCOAL, True, anchor="lm")

    text(
        draw,
        (70, 1080),
        "Ratings are observed customer scores. Reviews and recent purchases measure engagement. Trust is inferred, not directly measured.",
        14,
        MID_GRAY,
    )
    image.save(PROJECT_DIR / "Dashboard 1.png")


def print_analysis(df, price_summary, review_summary, category_summary):
    print(f"Rows: {len(df):,}")
    print(f"Median price: ${df['discounted_price'].median():,.2f}")
    print(f"Mean price: ${df['discounted_price'].mean():,.2f}")
    print(f"Median reviews: {df['total_reviews'].median():,.0f}")
    print(f"Mean reviews: {df['total_reviews'].mean():,.0f}")
    print("\nPrice tiers:")
    print(price_summary.to_string(index=False))
    print("\nReview tiers:")
    print(review_summary.to_string(index=False))
    print("\nCategories:")
    print(category_summary.to_string(index=False))

    pairs = [
        ("discounted_price", "product_rating"),
        ("discounted_price", "total_reviews"),
        ("total_reviews", "product_rating"),
        ("discounted_price", "purchased_last_month"),
    ]
    print("\nPearson correlations:")
    for first, second in pairs:
        subset = df[[first, second]].dropna()
        print(
            f"{first} vs {second}: "
            f"n={len(subset):,}, r={subset[first].corr(subset[second]):.3f}"
        )


def main():
    df = pd.read_csv(DATA_PATH)
    price_summary, review_summary, category_summary = build_summaries(df)
    export_chart_data(price_summary, review_summary, category_summary)
    draw_price_chart(price_summary)
    draw_review_chart(review_summary)
    draw_category_chart(category_summary)
    draw_dashboard(price_summary, review_summary, category_summary, raw_rows=42_675)
    print_analysis(df, price_summary, review_summary, category_summary)


if __name__ == "__main__":
    main()
