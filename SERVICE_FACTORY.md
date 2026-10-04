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



# Marketplace universe

This is the practical platform map for the Service Factory. Do **not** open every account at once. Start with the highest-fit channels, copy the same standardized service engines across them, and add more only when the first profiles/listings are live.

## Tier 1 — launch first

### Upwork
Best for:
- fresh posted jobs
- Project Catalog fixed-scope services
- research, spreadsheet, data, admin, automation, content operations

Current notes:
- freelancer fee varies by contract
- Project Catalog provides predefined service listings
- strongest combination of outbound proposals + inbound catalog discovery

Priority: **VERY HIGH**

### Fiverr
Best for:
- fixed-scope productized services
- search-driven inbound orders
- design, research, spreadsheets, document conversion, content operations

Current notes:
- new freelancers can run up to 4 Gigs
- Level 1/2 up to 10; Top Rated up to 30
- seller receives 80% of order value

Priority: **VERY HIGH**

### Freelancer.com
Best for:
- large global pool of posted projects
- fixed-price and hourly work
- data entry, Excel, research, automation, design, coding

Current notes:
- heavy competition
- useful mainly for targeted bidding on narrow jobs, not broad generic offers

Priority: **HIGH**

### PeoplePerHour
Best for:
- UK/EU-heavy small-business demand
- fixed Offers plus project proposals
- research, admin, design, marketing, writing

Current notes:
- no sign-up fee
- freelancer commission is highest on the first low-value billing with each buyer, then falls as lifetime buyer billing increases

Priority: **HIGH**

### Contra
Best for:
- polished fixed projects
- payment links
- one-off invoices
- digital products
- creative/strategy/tech services

Current notes:
- useful as both a talent marketplace and our own lightweight sales/payment surface
- supports guest checkout payment links
- digital products are supported
- especially attractive when we eventually want direct clients without building our own checkout

Priority: **HIGH**

### Airtasker
Best for:
- Australian buyers
- fast-turn local and remote digital tasks
- spreadsheet help, admin, research, design, web/content tasks

Current notes:
- tasker fee in Australia currently ranges by tier
- high local recognition
- good for one-off quick jobs and building early reviews

Priority: **HIGH in Australia**

---

## Tier 2 — worthwhile second-wave channels

### Guru
Best for:
- business/admin/data/programming/writing
- recurring client relationships
- quote-based jobs

Priority: MEDIUM-HIGH

### Workana
Best for:
- international remote projects, especially Latin America
- fixed-price and hourly projects
- tech, admin, design, marketing

Current notes:
- freelancer commission falls as lifetime billing with a client grows

Priority: MEDIUM-HIGH

### Kwork
Best for:
- Fiverr-like fixed service listings
- SEO, marketing, design, writing, data/admin

Current notes:
- seller fee starts high and falls with cumulative revenue from the same buyer

Priority: MEDIUM

### Legiit
Best for:
- SEO, marketing, web, content, business services
- fixed service listings

Current notes:
- free marketplace account available
- marketplace fee applies per sale

Priority: MEDIUM

### Bark
Best for:
- lead generation for services
- web design, marketing, bookkeeping/admin, consulting, local services

Current notes:
- not commission-based in the normal marketplace sense; professionals buy credits to contact leads
- therefore test cautiously because cash can be spent before winning work

Priority: MEDIUM — only after free/low-cost channels

---

## Tier 3 — specialist/high-value networks

These are not ideal for US$15 microservices, but they can become important once the profile has proof and the service factory develops higher-value offers.

### Braintrust
Best for:
- remote professional contract roles
- product, engineering, design, AI/data
- AI gig work

Current notes:
- currently markets zero platform fees to talent
- more role/network oriented than fixed microservices

Priority: MEDIUM-LATER

### Toptal
Best for:
- higher-value development, design, product/project management, consulting
- longer engagements

Current notes:
- heavily vetted
- poor fit for low-price microjobs
- potentially valuable once we have a strong specialist profile

Priority: LATER

### Arc
Best for:
- developer/technical freelance and contract work
- higher hourly rates

Priority: LATER / TECH-SPECIFIC

### Catalant
Best for:
- strategy, operations, market research, finance, transformation, AI consulting
- enterprise and private-equity clients

Current notes:
- verified consultant model
- projects are generally weeks/months rather than tiny gigs

Priority: LATER / HIGH-VALUE CONSULTING

### Malt
Best for:
- EU/UK professional freelance consulting
- technology, design, marketing, strategy

Priority: LATER unless Australian onboarding/market access proves useful

### Mayple
Best for:
- experienced performance marketers
- e-commerce marketing retainers

Current notes:
- strongly vetted and requires real performance track record

Priority: LOW FOR NOW

### Codeable
Best for:
- WordPress experts

Current notes:
- strong rates and vetted network
- applications are currently closed / waitlist only

Priority: WATCHLIST

### Kolabtree
Best for:
- scientific research
- statistics/data science
- academic/technical expert work

Priority: SPECIALIST

### Clarity.fm
Best for:
- paid expert calls
- business, startup, marketing or domain expertise

Priority: SPECIALIST / FUTURE ADVISORY

---

## Creative/design-specific channels

### 99designs
Best for:
- logos, branding, web/landing page design and design contests

Current notes:
- curated designer network
- platform fees vary by designer level
- less suitable for spreadsheet/research services

Priority: ONLY FOR DESIGN OFFERS

### DesignCrowd
Best for:
- design contests and direct design work

Current notes:
- free designer registration
- platform retains commission on designer payments

Priority: ONLY FOR DESIGN OFFERS

---

## AI/data-task income channels — separate lane

These are not our main “productized service catalog” model, but they belong in the broader 50-money-method universe because they can monetize spare capacity and specialist knowledge.

Candidates to evaluate separately:
- Braintrust AI Gig Work
- Outlier
- DataAnnotation
- Clickworker
- CrowdGen / Appen
- OneForma
- TELUS Digital AI/community work
- Prolific research participation
- UserTesting / User Interviews / Respondent for paid research/testing

These should be judged by **effective hourly return**, availability in Australia, payout reliability and whether the work improves our reusable skills/data.

---

## Direct discovery surfaces — no built-in marketplace checkout

These are useful for client acquisition, but require a separate payment/invoicing channel:

- LinkedIn Services / posts
- Facebook small-business and niche groups where promotion is allowed
- relevant Reddit hiring/subreddit threads
- Discord/Slack professional communities
- local business directories
- industry forums
- cold email to businesses with a concrete micro-offer
- direct outreach from public job/problem posts
- personal website / SEO pages
- GitHub profile/repositories for technical services

Contra invoices/payment links can become the lightweight payment rail for direct clients if we do not want Stripe.

---

## Platforms deliberately deprioritized / retired

### Oneflare
Closed on 30 June 2026 and now redirects users toward Airtasker.

Do not spend setup time there.

---

## Rollout sequence

### Wave 1
1. Upwork
2. Fiverr
3. Airtasker
4. Contra

### Wave 2
5. Freelancer.com
6. PeoplePerHour
7. Guru
8. Workana
9. Kwork
10. Legiit

### Wave 3
11. Bark
12. Braintrust
13. specialist networks relevant to whatever service has proven demand

Do not build separate fulfillment processes for each platform. One service engine should be syndicated across multiple marketplaces with platform-specific titles, images and pricing.

## Core rule

A platform only earns ongoing attention if it produces one of:
- impressions from qualified buyers;
- messages;
- orders;
- paid contracts.

No signal after a defined test window = stop spending owner time there.
