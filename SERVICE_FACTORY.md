# Service Factory v1

Goal: create a portfolio of narrow, fixed-scope services where fulfillment can be heavily automated and human time stays low.

## Platform reality

Upwork Project Catalog currently allows up to **20 active projects** (and up to 20 more under review). Prices may start at US$5. Freelancer service fees vary by contract, currently 0–15%.

Fiverr is not a 1,000-gig surface: a new freelancer currently gets **4 active Gigs**, Level 1/2 get 10, Top Rated gets 30. Fiverr's standard freelancer commission is 20%.

Therefore the strategy is not spam volume. It is:
**20 high-specificity Upwork projects + 4 high-conversion Fiverr gigs + rotate losers quickly + reuse the same fulfillment engines across custom jobs.**

## Economics rule

Avoid building the business around US$3–10 orders unless fulfillment is genuinely near-zero-touch.

Target:
- Starter: US$15–25
- Standard: US$35–60
- Advanced: US$75–150
- human time: ideally 5–20 minutes after the intake is complete
- one revision maximum
- no meetings by default
- client supplies source material
- ambiguous cases are flagged rather than guessed

## First 12 service products

### 1. 5-competitor pricing snapshot
**Client sends:** business URL + market/category.
**Deliver:** sourced table of 5 competitors, prices, plans, headline positioning, key differentiators, 5 observations.
**Starter:** US$19.
**Human QA target:** 10–15 min.
**Why:** live Upwork demand exists for fast B2B SaaS competitor reports.

### 2. Recent customer-review pain map
**Client sends:** product URLs/review exports.
**Deliver:** top complaints, desired features, recurring praise, buyer language, severity/frequency table, 5 opportunities.
**Starter:** US$25 for up to 100 reviews.
**Human QA:** 10–15 min.
**Wedge:** outcome-focused product insight, not generic sentiment analysis.

### 3. PDF table → validated Excel
**Client sends:** machine-readable PDF(s).
**Deliver:** clean XLSX/CSV + row-count/total validation + flagged extraction exceptions.
**Starter:** US$15 for one simple PDF/table.
**Human QA:** 5–15 min.
**Why:** fresh Upwork jobs are paying US$10–30 for exactly this.

### 4. Two-file reconciliation / mismatch report
**Client sends:** two CSV/XLSX exports with common key.
**Deliver:** matched rows, only-in-A, only-in-B, changed fields, summary counts.
**Starter:** US$25.
**Human QA:** 5–10 min.
**Wedge:** reconciliation outcome rather than commodity "spreadsheet cleanup."

### 5. Supplier price-list change detector
**Client sends:** old and new supplier files.
**Deliver:** price increases/decreases, discontinued/new SKUs, percentage change, largest movers.
**Starter:** US$25.
**Human QA:** 5–10 min.
**Repeat potential:** monthly/weekly.

### 6. Marketplace competitor gap sheet
**Client sends:** category/query + marketplace (Amazon/Etsy/etc.).
**Deliver:** 10 listings with price, review count, positioning, images/topics, complaints and gap hypotheses.
**Starter:** US$35.
**Human QA:** 15–20 min.
**Why:** current Upwork jobs pay materially more for expanded versions.

### 7. Messy SOP → one-page operator checklist
**Client sends:** notes, transcript, email thread or existing procedure.
**Deliver:** concise SOP, checklist, exception/escalation section, printable version.
**Starter:** US$25.
**Human QA:** 10–15 min.
**Wedge:** "make this usable by the next person," not generic writing.

### 8. Folder/file naming convention + batch rename plan
**Client sends:** sample filenames + desired rules.
**Deliver:** naming schema, collision rules, preview mapping CSV and optional rename script.
**Starter:** US$20.
**Human QA:** 10 min.
**Wedge:** company-specific rule design + preview, not a generic renamer.

### 9. CSV import readiness audit
**Client sends:** export destined for Shopify/CRM/accounting/import system.
**Deliver:** delimiter/header/duplicate/blank/type problems, corrected copy, exception report.
**Starter:** US$25.
**Human QA:** 5–15 min.
**No domain judgment:** structural validation only.

### 10. Website pricing-page comparison
**Client sends:** own URL + up to 5 competitors.
**Deliver:** side-by-side plans, billing periods, limits, free trial, CTA, positioning, pricing gaps.
**Starter:** US$25.
**Human QA:** 10–15 min.
**Repeat potential:** quarterly monitoring.

### 11. 20-page web content inventory
**Client sends:** site/domain + page list/sitemap.
**Deliver:** page title, H1, meta description presence, status, duplicate titles, content-type label, obvious gaps.
**Starter:** US$29.
**Human QA:** 10–15 min.
**Wedge:** inventory, not SEO consulting.

### 12. Survey/open-text response synthesis
**Client sends:** CSV/XLSX of responses.
**Deliver:** coded themes, frequency table, representative excerpts (within client data), top requests, action summary.
**Starter:** US$35 up to agreed row cap.
**Human QA:** 10–20 min.
**Wedge:** decision-ready synthesis.

## What we do NOT list initially

- generic "data entry"
- generic "virtual assistant"
- generic "AI content writer"
- full website builds
- bookkeeping/accounting judgments
- legal/medical advice
- unrestricted scraping
- anything requiring live meetings for a US$10 order
- open-ended "unlimited revisions"

## Fulfillment architecture

Every service gets:
1. fixed intake questions;
2. source-file limit;
3. automated transformation/research pass;
4. validation checklist;
5. client-ready delivery template;
6. one defined revision;
7. logged actual owner minutes.

If a job takes >30 owner minutes twice, either raise price, narrow scope or kill the listing.

## Rotation rule

Upwork only gives us 20 active Project Catalog slots. Treat them as portfolio slots.

Every 30 days:
- keep listings with purchases/messages/saves;
- rewrite listings with impressions but weak conversion once;
- replace dead listings with services derived from fresh job posts;
- do not preserve listings merely because they took time to create.

## Scale target

Do not aim for 100 orders/week at US$5 first.

Stage 1:
5 orders/week × US$20 average = US$100 gross while measuring fulfillment time.

Stage 2:
15 orders/week × US$30 average = US$450 gross.

Stage 3:
25 orders/week × US$40 average = US$1,000 gross.

Only scale volume if average human handling time is under ~15 minutes/order.

The objective is **net revenue per owner minute**, not order count.
