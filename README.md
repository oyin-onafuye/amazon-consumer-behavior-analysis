# Amazon Consumer Behavior Analysis
### What Actually Drives Consumer Choice in 2026 — Price or Social Proof?

---

## Executive Summary

In 2026, brands like PepsiCo, Walmart, and E.l.f. are cutting prices to win back consumers who traded down during inflation. This analysis asks: is that actually the right lever?

Across 42,675 Amazon product observations spanning 15 electronics categories, the data shows that price does not signal quality to consumers. The crowd does. Budget products average 13,703 reviews compared to 464 for premium products, a 30x gap that represents the real competitive moat. Brands cutting prices are solving the wrong problem.

**Stop competing on price. Start competing on proof.**

---

## Dashboard

<img width="1011" height="776" alt="Image" src="https://github.com/user-attachments/assets/a7e43c6b-848a-4b79-989b-1e792d392558" />

[View Interactive Dashboard on Tableau Public](https://public.tableau.com/app/profile/oyinlayomi.onafuye/viz/AmazonPricingReviewAnalysis/Dashboard1)

---

## Business Context

The consumer goods industry is at an inflection point. After years of inflation-driven price hikes, brands are now facing a loyalty crisis. Consumers traded down to private label and cheaper alternatives, and they have not come back. The instinctive response from brand managers and category leaders has been to cut prices. PepsiCo did it. General Mills did it. E.l.f. Cosmetics cut the price of its Halo Glow Skin Tint from $18 to $14 and saw a 36% unit lift. Walmart has rolled back prices on over 7,200 products.

But is price actually what drove consumers away, and is it what will bring them back?

This analysis examines 42,675 Amazon product observations across 15 electronics categories to answer a more precise version of that question: when consumers choose one product over another on a major retail marketplace, what signal are they actually responding to? Price, rating, or something else entirely?

---

## Key Findings

### Finding 1: Price Has Almost No Effect on Rating

The most counterintuitive finding in this dataset is also the most important one. Across six price tiers spanning products from $0 to $2,000+, average product ratings stay virtually flat. The $0-25 tier averages 4.53 stars. The $500-1,999 tier averages 4.38 stars. The total spread across the entire price range is just 0.15 stars, smaller than a single rating increment on Amazon's five-star scale.

This means that on Amazon, a $10 phone charger and a $1,500 laptop are rated nearly identically by the people who bought them. Price is not making products better in the eyes of consumers. It is not even making them look better. The assumption that premium pricing signals premium quality, a cornerstone of traditional brand strategy, simply does not hold in this data.

For brand managers considering whether to cut prices to improve perceived value: the data suggests price cuts will not move the quality perception needle. Consumers are not rating cheaper products higher because they are cheaper. Something else is driving that perception.

### Finding 2: Budget Products Get 30x More Reviews Than Premium Products

While rating stays flat across price tiers, review volume tells a completely different story. Products in the $0-25 tier average 13,703 total reviews. Products in the $500-1,999 tier average just 464. That is a 30x difference in visible consumer engagement, and it is not random noise. It is a clean, consistent decline: every price tier has fewer reviews than the one below it, without exception.

Monthly purchase data confirms this is not just a historical artifact of older cheap products accumulating reviews over time. Products under $25 average 3,264 purchases per month. Products in the $500-1,999 range average 251 per month, a 13x difference in current buying velocity. Cheaper products are being chosen more often right now, and that ongoing volume is continuously building the review count that cheaper products hold.

The implication is significant: review count is not just a vanity metric. It is a compounding competitive asset. A product with 13,000 reviews signals to every new potential buyer that 13,000 people made this decision before them and most of them did not regret it. A product with 464 reviews sends a much weaker signal, regardless of how good it actually is.

### Finding 3: Review Count Correlates Directly With Rating

The third finding connects findings one and two into a single mechanism. When products are grouped by review count rather than price, a clear upward trend emerges. Products with fewer than 100 reviews average 4.34 stars. Products with 1,000 to 10,000 reviews average 4.47 stars. Products with over 100,000 reviews average 4.60 stars.

The relationship is not perfectly linear. There is a slight dip in the 11-100 review bucket before the consistent climb begins. But the directional finding is clear and consistent: products with more reviews tend to have higher ratings.

This could reflect several mechanisms: better products may naturally attract more buyers and therefore more reviews; Amazon's algorithm may promote highly reviewed products to more buyers, who then review them; or the social validation of seeing thousands of reviews may make buyers more satisfied with their purchase and therefore more likely to rate it positively. The data cannot distinguish between these explanations, but the correlation is real and the business implication is the same regardless of the mechanism.

If review volume drives rating, and rating is what consumers use to evaluate quality, then the path to a better perceived product is not a better price. It is a larger review base.

### Finding 4: The Pattern Holds Across 13 of 15 Categories, With Two Meaningful Exceptions

The findings above were tested across all 15 product categories in the dataset. The pattern holds in 13 of them: higher-priced categories have lower average review counts, and the relationship between review volume and rating is consistent.

Two categories break the pattern in a meaningful way: Storage and Smart Home. Both maintain high review counts despite not being the cheapest categories in the dataset. Storage averages 21,295 reviews, the highest of any category, despite a moderate average price. Smart Home similarly maintains strong review volume at 9,256 average reviews.

Both are high-consideration categories where consumers do extensive research before buying. Storage products are purchased with specific technical requirements in mind. Smart Home devices require ecosystem compatibility decisions. In both cases, consumers may be relying more heavily on review volume as a trust signal precisely because the decision is more complex, making these categories where review-driven social proof matters even more than average.

The exceptions do not undermine the core finding. They reinforce it: in categories where consumers have more at stake, they lean harder on the crowd signal, not the price signal.

---

## Business Recommendation

For CPG and retail brands entering or defending market position in price-sensitive categories, the data suggests a two-phase positioning strategy rather than a permanent price cut.

**Phase 1: Seed volume.** Price aggressively in new or underpenetrated categories to drive initial purchase velocity. The goal is not to be the cheapest product permanently. The goal is to accumulate enough reviews quickly that the product gains algorithmic visibility and social proof credibility. A product with 10,000 reviews at $19.99 is significantly harder to displace than a product with 200 reviews at $14.99, regardless of which one is objectively better. The review base is the moat.

**Phase 2: Move to margin.** Once review credibility is established, roughly 1,000+ reviews as a baseline threshold, brands can move toward premium positioning without losing the trust signal they have built. The review count remains visible to future buyers even as price increases, and the higher rating that correlates with higher review count now supports the premium price story.

This reframes the entire price-cut debate. Brands should not be asking "how low can we go?" They should be asking "how quickly can we build the review volume that makes our price irrelevant?"

---

## Methodology and Limitations

**Data:** 42,675 Amazon product observations across 15 electronics categories, collected over a 9-day scrape window in August 2026. Products deduplicated to 8,806 unique products using ASIN matching for the price-tier comparison analysis.

**Analysis approach:** SQL (SQLite) for price-tier breakdowns, review-rating correlation, and category comparisons. Python (Pandas) for data cleaning, handling scraping artifacts, and ASIN-based deduplication. Tableau Public for dashboard visualization.

**Limitations:**
- This is a descriptive analysis. Correlation is identified, not causation. The relationship between review count and rating could reflect product quality, algorithmic promotion, or buyer psychology. The data does not distinguish between these.
- Dataset covers electronics categories only. Findings may differ in fashion, food, beauty, or other consumer goods verticals where purchase frequency and review behavior differ.
- Approximately 17% of rows had non-numeric scraping artifacts in the purchased_last_month field and were treated as missing values.
- Average rather than median was used for price and review aggregations. Both distributions are right-skewed, so median would be a more robust measure, a refinement worth incorporating in a follow-on analysis.
- Snapshot data. Does not capture price or review changes over time, limiting causal inference about what drives review accumulation.

---

## Files

- `sql_queries/` — All SQL queries used for analysis
- `data_cleaning.py` — Python cleaning and deduplication script
- `amazon_FINAL.csv` — Final cleaned dataset (8,806 unique products)

[View Code and Technical Documentation](https://github.com/oyin-onafuye/amazon-consumer-behavior-analysis)
