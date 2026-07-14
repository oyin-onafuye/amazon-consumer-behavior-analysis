# Amazon Consumer Behavior Analysis
### What Actually Drives Consumer Choice in 2026 — Price or Social Proof?

## Overview
In 2026, brands like PepsiCo, Walmart, and E.l.f. are cutting prices to win back consumers who traded down during inflation. This analysis asks: is that actually the right lever?

Across 42,675 Amazon product observations spanning 15 categories, the data shows that price doesn't signal quality to consumers. The crowd does. Review volume and purchase velocity are the real drivers of market position, not price or star rating.

## Key Findings
- **Rating is virtually flat across all price tiers** — a $10 product and a $500 product average the same 4.4 stars (0.15 star total spread)
- **Budget products get 30x more reviews** than premium products ($0-25 tier averages 13,703 reviews vs 464 for $500-1,999 tier)
- **More reviews correlates with higher rating** — products with 100K+ reviews average 4.60 stars vs 4.34 for products with under 100 reviews
- **Pattern holds across 13 of 15 categories** — Storage and Smart Home are the exception

## The So What
Brands cutting prices are solving the wrong problem. Consumers are not choosing cheaper products because they are cheaper. They are choosing products that feel proven. Price cuts drive volume. But volume is just the mechanism. What brands are actually buying with that volume is the review count and purchase engagement that signals credibility to the next buyer.

Stop competing on price. Start competing on proof.

## Tools Used
- Python (Pandas) for data cleaning and validation
- SQL (SQLite) for exploratory analysis and price tier breakdowns
- Tableau Public for dashboard and data visualization

## Dataset
- 42,675 Amazon product observations across 15 electronics categories
- 9-day scrape window (August 2026)
- Deduplicated to 8,806 unique products using ASIN matching for comparison analysis

## Dashboard
(https://public.tableau.com/app/profile/oyinlayomi.onafuye/viz/AmazonPricingReviewAnalysis/Dashboard1)
<img width="1011" height="776" alt="Image" src="https://github.com/user-attachments/assets/0d6fb1ca-8ee1-4082-9232-18e5101f2fa2" />
[View the interactive Tableau dashboard here]

## Limitations
- Descriptive analysis only, no formal statistical significance testing
- Dataset covers electronics categories only, findings may differ in other consumer goods verticals
- Approximately 17% of rows had scraping artifacts in the purchased_last_month field, treated as missing values
- Snapshot data, does not capture price or review changes over time
