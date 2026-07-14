# NorthPeak Marketplace Growth Strategy Analysis

**Business Analyst | Consumer Insights Team**
**Reporting to: Director of Digital Commerce**

---

## Business Context

NorthPeak is a global consumer products company that designs innovative home, kitchen, and lifestyle products for modern households. The company distributes its portfolio through major retail partners and online marketplaces across North America, serving millions of customers each year.

As NorthPeak prepared its annual marketplace growth strategy, leadership faced a critical investment decision: should future marketplace resources prioritize competitive pricing or customer trust initiatives to strengthen marketplace performance?

To support this decision, the Consumer Insights team analyzed 42,675 publicly available Amazon product listings across 15 product categories. Amazon was used as a competitive intelligence source to understand how pricing and social proof influence consumer behavior on digital marketplaces.

**Business Problem:** How should NorthPeak allocate future marketplace investments to improve marketplace performance?

---

## Executive Summary

The central finding of this analysis challenges a widely held assumption in marketplace strategy: price does not drive consumer trust or ratings. Social proof does.

Across 42,675 Amazon product observations spanning 15 categories, average ratings remain virtually flat regardless of price. Only 0.15 stars separate the cheapest from the most expensive products. Yet budget products average 13,703 reviews compared to just 464 for premium products, a 30x gap in visible consumer engagement.

Products with more reviews consistently earn higher ratings. Budget products also average 3,264 monthly purchases compared to 251 for premium products, a 13x difference in current buying velocity.

The data points to a clear strategic direction: NorthPeak should not compete primarily on price. The higher-return investment is building the review volume and purchase engagement that signals marketplace credibility to future buyers.

| Metric | Finding |
|---|---|
| Total product observations analyzed | 42,675 |
| Average review gap: budget vs premium | 30x (13,703 vs 464 reviews) |
| Average rating spread across all price tiers | 0.15 stars |
| Monthly purchase gap: budget vs premium | 13x (3,264 vs 251 purchases) |
| Categories where pattern holds | 13 of 15 |ion](https://github.com/oyin-onafuye/amazon-consumer-behavior-analysis)
---

## Insights Deep Dive

### Section 1: Pricing Strategy
**Does lower price improve marketplace performance?**

Across six price tiers from $0 to $2,000+, average product ratings stay virtually flat. The $0-25 tier averages 4.53 stars. The $500-1,999 tier averages 4.38 stars. The total spread is just 0.15 stars, smaller than a single rating increment on Amazon's five-star scale.

Price is not making products look better in the eyes of consumers. A $10 product and a $1,500 product are rated nearly identically. The assumption that premium pricing signals premium quality does not hold in this data.

**Implication for NorthPeak:** Price cuts are unlikely to improve consumer perception of quality. Brands investing in discounting to signal value are solving the wrong problem.

---

### Section 2: Customer Trust
**Does social proof have a stronger relationship with marketplace performance than price?**

While rating stays flat across price tiers, review volume tells a completely different story. Products in the $0-25 tier average 13,703 total reviews. Products in the $500-1,999 tier average just 464. Every price tier has fewer reviews than the one below it without exception.

Monthly purchase data confirms this is not a historical artifact. Products under $25 average 3,264 purchases per month compared to 251 for premium products, a 13x difference in current buying velocity.

When products are grouped by review count, a consistent upward trend emerges in ratings. Products with fewer than 100 reviews average 4.34 stars. Products with over 100,000 reviews average 4.60 stars. Review volume is the real driver of marketplace performance.

**Implication for NorthPeak:** Review count is a compounding competitive asset. A product with 13,000 reviews signals credibility to every new potential buyer. A product with 464 reviews, regardless of quality, sends a much weaker signal. Investing in review volume generation is a higher-return strategy than investing in price cuts.

---

### Section 3: Category Analysis
**Do these relationships differ across product categories?**

The pattern holds across 13 of 15 product categories. Two categories break the pattern in a meaningful way: Storage and Smart Home. Storage averages 21,295 reviews, the highest of any category, despite a moderate average price. Smart Home maintains strong review volume at 9,256 average reviews.

Both are high-consideration categories where consumers do extensive research before buying. Storage products are purchased with specific technical requirements. Smart Home devices require ecosystem compatibility decisions. In both cases, consumers rely more heavily on review volume as a trust signal precisely because the purchase decision is more complex.

**Implication for NorthPeak:** In categories where consumers have more at stake, they lean harder on social proof, not price.

---

### Section 4: Marketplace Strategy
**Where should NorthPeak focus future marketplace investments?**

The data points to a two-phase marketplace positioning strategy.

**Phase 1: Seed volume.** In new or underpenetrated categories, price aggressively to drive initial purchase velocity. The goal is not to be permanently cheap. The goal is to accumulate enough reviews quickly that the product gains algorithmic visibility and social proof credibility. A product with 10,000 reviews at $19.99 is significantly harder to displace than a product with 200 reviews at $14.99, regardless of which one is objectively better.

**Phase 2: Move to margin.** Once review credibility is established, approximately 1,000+ reviews as a baseline threshold, move toward premium positioning. The review count remains visible to future buyers as the price increases, and the higher rating that correlates with higher review count supports the premium price story.
---

## Recommendations

### Pricing Team
Avoid competing solely on price in mature categories where ratings remain consistent across price tiers. Price reductions in these categories are unlikely to improve consumer perception and will erode margin without a corresponding return in marketplace credibility.

In new category launches, use introductory pricing strategically to seed purchase volume, not as a long-term positioning tool.

### Marketing Team
Increase investment in verified review generation initiatives. Post-purchase follow-up sequences, sampling programs, and loyalty-driven review campaigns will generate higher long-term marketplace returns than promotional discounting.

Focus messaging on social proof signals: review count, purchase volume badges, and community engagement, rather than price-led communications.

### Marketplace Team
Develop category-specific marketplace strategies rather than a one-size-fits-all pricing approach. Storage and Smart Home categories demonstrate that in high-consideration segments, social proof investments are even more critical than average.

Monitor review velocity as a leading performance indicator alongside traditional metrics like revenue and conversion rate.

### Consumer Insights Team
Establish a quarterly review of marketplace performance data tracking review count growth, pricing tier distribution, and rating trends by category. This will allow NorthPeak to identify early signals of competitive displacement before they show up in revenue metrics.

---

## Expected Business Impact

| Recommendation | Expected Outcome |
|---|---|
| Shift from price-led to review-led marketplace investment | More sustainable long-term marketplace performance without permanent margin sacrifice |
| Post-purchase review generation programs | Compounding improvement in marketplace credibility and algorithmic visibility |
| Category-specific pricing strategy | Higher return on marketplace investment in high-consideration categories |
| Quarterly review velocity tracking | Earlier identification of competitive threats and marketplace performance shifts |

---

## Data Overview

**Dataset:** 42,675 Amazon product observations across 15 electronics categories, collected over a 9-day scrape window.

**Deduplication:** Products identified using ASIN (Amazon's unique product identifier). 8,806 unique products used for price-tier comparison analysis.

**Tools:** SQL (SQLite) for price-tier breakdowns and review-rating correlation. Python (Pandas) for data cleaning, handling scraping artifacts, and ASIN-based deduplication. Tableau Public for dashboard visualization.

---

## Limitations

- Amazon marketplace data was used as a proxy for marketplace performance. Internal NorthPeak metrics such as conversion rate, advertising spend, and profit margins were unavailable and would strengthen the analysis.
- Dataset covers electronics categories only. Findings should be treated as directional insights for NorthPeak's home, kitchen, and lifestyle categories, where purchase dynamics may differ.
- This is a descriptive analysis. Correlation between review count and rating is identified, not causation.
- Average rather than median was used for price and review aggregations. Both distributions are right-skewed, so median would be a more robust measure in a follow-on analysis.
- Approximately 17% of rows had scraping artifacts in the purchased_last_month field and were treated as missing values.
- Snapshot data only. Does not capture price or review changes over time.

---

## Dashboard

[View Interactive Dashboard on Tableau Public](https://public.tableau.com/app/profile/oyinlayomi.onafuye/viz/AmazonPricingReviewAnalysis/Dashboard1)

---

## Files

- sql_queries/ — SQL queries used for price-tier breakdowns and review-rating correlation
- data_cleaning.py — Python cleaning and deduplication script
- amazon_FINAL.csv — Final cleaned dataset (8,806 unique products)
