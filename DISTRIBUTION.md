# TurnoverCue — Distribution & Market-Test Pack

Status: MARKET-READY  
Public URL: https://davidwilsoncodes.github.io/turnovercue/  
Cash spent: A$0  
Paid promotion: none

## Primary launch hypothesis

Self-managing short-term-rental hosts who manually translate booking calendars into cleaner instructions will use a free, private browser tool that turns .ics booking calendars into a cleaner-ready schedule.

## Measurement reality

Cloudflare Web Analytics is installed.

It can measure visitors, page views, paths, referrers and performance, but as of October 2026 Cloudflare Web Analytics does **not** support:
- UTM parameter reporting
- custom conversion events

Therefore:
- Use the path `/turnovercue/` when reviewing top-level traffic.
- Use the **Referrer** dimension to identify traffic from directory/community placements.
- Do not rely on UTM query strings in Cloudflare.

### Anonymous pageview-based conversion markers

Because Cloudflare Web Analytics does not support custom events, TurnoverCue now creates a hidden, noindex internal pageview the first time each meaningful action happens in a browser session.

Filter Cloudflare by these paths:

- `/turnovercue/events/calendar-loaded.html` = at least one real uploaded calendar produced usable reservation events
- `/turnovercue/events/copy-cleaner-message.html` = cleaner message copied
- `/turnovercue/events/export-csv.html` = CSV export triggered
- `/turnovercue/events/print-schedule.html` = print/save-PDF action triggered

These markers send **no booking details, filenames, property names or calendar content**. They are coarse anonymous action counters implemented as ordinary pageviews because custom events are unavailable.

This method is intentionally experimental until it is confirmed in the Cloudflare dashboard. Direct feedback and repeat traffic remain stronger commercial evidence than a button click.

Cloudflare docs:
https://developers.cloudflare.com/web-analytics/faq/

## First verified qualified channel: The Tool Directory

Submission page:
https://thetooldirectory.com/submit-a-tool/

Why it qualifies:
- standard listing is free
- focused web utilities are allowed
- every submission is reviewed
- no payment is required for a standard listing
- public profile can include audience, pricing, alternatives and use cases

### Exact form copy

**Tool or product name**  
TurnoverCue

**Product website URL**  
https://davidwilsoncodes.github.io/turnovercue/

**One-line description**  
Free private browser tool that turns Airbnb, VRBO and other iCal booking calendars into cleaner-ready turnover schedules.

**Pricing**  
Free

**Category**  
Utilities  
If Utilities is unavailable, use Productivity or the closest Business/Operations category.

**Platforms**  
Web

**Who is it for?**  
Self-managing Airbnb, VRBO and vacation-rental hosts; small STR operators who coordinate cleaners manually.

**What do people use it for?**  
Turning iCal booking calendars into cleaning dates, flagging same-day turnovers, combining multiple properties, generating cleaner messages, and exporting turnover schedules.

**Alternatives to**  
Turno, Breezeway, manual spreadsheets, cleaner group messages

**Logo URL**  
Leave blank for the first submission unless we later add a stable public logo asset.

**Screenshots**  
Optional. Leave blank for the first submission unless the reviewer requires them.

**Tell us what the tool does and what makes it useful**  
TurnoverCue is a lightweight browser utility for self-managing short-term-rental hosts who do not need a full property-management platform just to coordinate cleaners. Upload one or more .ics booking calendar files and TurnoverCue identifies checkout days, highlights same-day turnover risk, combines multiple properties into one schedule, generates a cleaner-ready message, and exports CSV or printable schedules.

The current free version runs locally in the browser. It does not require an account, does not connect to the host's Airbnb or VRBO account, does not require access to prices or payouts, and does not upload the booking calendar to a TurnoverCue server.

It is designed for the awkward gap between a host's booking calendar and the cleaner who only needs to know where and when a turnover is required.

**Paid featured placement checkbox**  
Leave unchecked.

**Your email**  
Human owner step: enter the email David wants associated with the submission.

### Submission boundary

Submitting the form publicly under the owner's identity is a human boundary. No payment or featured placement should be accepted during this experiment.

## Secondary discovery channels

These are broader than the STR niche, so they are secondary rather than substitutes for qualified host traffic.

### Directree
https://www.directree.io/

- free to submit
- no pay-to-rank positioning
- useful for another indexed software profile
- use the same core positioning as The Tool Directory

### Ignlab Launch
https://launch.ignlab.net/

- free
- no account required to submit
- reviewed before publication
- no paid ranking or featured upsell according to its current FAQ

### Channels deliberately rejected for this test

**r/airbnb_hosts**  
Recent promotional/developer posts are repeatedly removed with explicit “No self promotion” moderator/bot responses. Do not post TurnoverCue there as promotion.

**STR Specialist directory**  
Current vendor listing flow leads to a US$149 one-off editorial review after fit check. That violates the A$0 experiment rule, so skip it unless later evidence justifies paid distribution.

**Airbnb Host Recommendations Directory**  
This directory is for host-recommended service providers, not software self-promotion. Do not try to force TurnoverCue into it.

Only use communities where product/tool promotion is explicitly allowed. Useful discussion and support can be separate from promotion; do not disguise advertising as advice.

## Signal thresholds

### Weak signal
- 5+ independent people report successfully using the tool, or
- useful unsolicited host feedback

### Promising signal
- 10 repeat users, or
- 5+ independent requests for automatic calendar sync / notifications / cleaner assignment

### Strong signal
- an independent host explicitly asks to pay
- an independent host offers to pay
- a host accepts a paid pilot

## Traffic checkpoint

At 100 qualified visitors, evaluate:
- Were people from the intended STR audience?
- Did we receive any direct evidence of successful use?
- Did anyone return or ask for more automation?
- Did anyone ask to pay?

If traffic arrives but there is no usage evidence, make one positioning/onboarding correction and run a second comparable exposure window.

If the second window is also dead, stop development and preserve the asset cheaply.

## No-spend rule

Do not purchase:
- directory placement
- sponsored posts
- ads
- editorial reviews
- paid backlinks

without explicit owner approval.

## Current build status

- Product works
- Public GitHub Pages URL works
- Cloudflare Web Analytics installed
- Audience positioning explicit above the fold
- How-it-works section live
- FAQ live
- privacy explanation live
- search/social metadata live
- sitemap and robots.txt live
- product development frozen unless real user evidence justifies changes
