# Tableau Public Publication Checklist

Apply these copy updates to the existing Tableau workbook without changing its layout or analysis.

## Dashboard

- Title: **Price Influences Customer Engagement, Not Ratings**
- Subtitle: **Analysis of 8,806 deduplicated Amazon listings from 42,675 scrape observations • Review volume and recent-purchase activity vary far more across price tiers than customer ratings**
- KPI 1: keep **8,806**; label **Marketplace Listings Analyzed**
- KPI 2: keep **29.5×**; use **Higher Average Review Volume** with comparison line **<$25 vs. $500–1,999**
- KPI 3: keep **0.16★**; use **Maximum Difference in Average Rating** with context line **Across Five Price Tiers**
- Left chart title: **Customer Engagement Across Price Tiers**
- Right chart title: **Ratings Across Review Tiers**
- Bottom chart title: **Review Volume Across Product Categories**
- Footer: **Ratings are observed customer scores. Reviews and recent purchases measure engagement. Trust is inferred, not directly measured.**

## Worksheets

- Price worksheet title: **Lower-Priced Products Lead in Reviews; Ratings Stay Similar**
- Price worksheet subtitle: **Average reviews and ratings across five price tiers • 8,382 products with price data**
- Review-tier worksheet title: **Higher Review Counts Align With Slightly Higher Ratings**
- Review-tier worksheet subtitle: **Average rating by review tier • 8,741 products with review data**
- Category worksheet title: **Customer Review Volume Varies Widely by Category**
- Category worksheet subtitle: **Average reviews by category • product counts shown for context**

## Labels and Annotations

- Use these price tiers in this exact order:
  1. **<$25**
  2. **$25–99**
  3. **$100–499**
  4. **$500–1,999**
  5. **$2,000+**
- Use these review tiers in this exact order:
  1. **1–99**
  2. **100–999**
  3. **1K–9,999**
  4. **10K–99,999**
  5. **100K+**
- Remove any **13 of 15 categories** annotation.
- Remove any wording that calls Storage or Smart Home an exception.
- Replace **marketplace activity** with **customer engagement** where it refers to reviews or recent purchases.
- Use **tend to have slightly higher ratings**, not **consistently earn higher ratings**.
- Use **29.5×** or **approximately 30×**, not an unqualified **30×**.
- Keep legends only where they identify separate measures; use **Average Reviews** and **Average Rating**.

## Final Consistency Check

- Confirm all dashboard and worksheet filters use the five standardized price tiers.
- Confirm KPI values remain **8,806**, **29.5×**, and **0.16★**.
- Confirm titles, subtitles, annotations, tooltips, and captions contain no references to the previous six-tier system.
- Publish the refreshed workbook to the existing Tableau Public URL used in `README.md`.
