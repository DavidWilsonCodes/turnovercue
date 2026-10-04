# One-Person Venture Studio — Experiment Ledger

Goal: build and expose a large portfolio of cheap owned assets, then allocate attention based on real market signal rather than attachment or forecasts.

## Studio rules

1. Build an owned asset, not a disguised job.
2. Prefer zero-cash or near-zero-cash tests.
3. Define the market test before polishing.
4. Real usage beats hypothetical demand.
5. Do not add recurring infrastructure before recurring value is proven.
6. Preserve dormant assets cheaply instead of deleting optionality.
7. Explicitly record the biggest assumption and stop rule.
8. Follow strong signal aggressively; do not give equal attention to every experiment.
9. Human-only boundaries stay human: identity, financial approval, tax/bank, legal agreements, public posting under owner identity.
10. Each project should leave reusable code, distribution knowledge or infrastructure even if commercial demand is weak.

## Status ladder

- NO-BUILD
- BUILDING
- FUNCTIONAL
- CUSTOMER-READY
- MARKET-READY
- EXPOSED TO QUALIFIED MARKET
- WEAK SIGNAL
- PROMISING SIGNAL
- STRONG SIGNAL
- REVENUE SIGNAL
- GROWTH SIGNAL
- FROZEN / DORMANT

---

## Run #1 — TurnoverCue

**Status:** MARKET-READY + INSTRUMENTED — awaiting first qualified external distribution submission

**Asset:** free browser utility for short-term-rental hosts.

**Target:** self-managing Airbnb/VRBO/vacation-rental hosts who coordinate cleaners manually.

**Job:** turn .ics booking calendars into cleaner-ready turnover schedules.

**Free wedge:**
- multiple calendar files
- checkout/cleaning dates
- same-day turnover flags
- cleaner message
- CSV export
- print/PDF
- local browser processing

**Possible paid wedge if earned:**
- automatic read-only calendar sync
- cancellation/change alerts
- scheduled cleaner notifications
- cleaner assignments
- completion/proof

**Cash spent:** A$0

**Infrastructure:**
- GitHub repository: DavidWilsonCodes/turnovercue
- GitHub Pages live
- Cloudflare Web Analytics installed
- search/social metadata
- sitemap/robots
- distribution pack

**Biggest commercial assumption:** enough small hosts experience this handoff pain repeatedly that removing the manual upload step becomes worth paying for.

**Biggest distribution assumption:** we can reach qualified hosts cheaply without paid advertising or prohibited community spam.

**Measurement limitation:** current Cloudflare Web Analytics does not expose UTM query reporting or custom conversion events. Use traffic/referrer plus direct feedback until a better event layer is justified.

**Weak:** 5+ independent successful uses or meaningful feedback.

**Promising:** 10 repeat users or 5+ requests for autosync/notifications.

**Strong:** independent host asks/offers to pay or accepts paid pilot.

**Stop:** two qualified exposure windows around the 100-visitor scale with minimal meaningful use after one positioning correction.

**Current next action:** submit the free Tool Directory listing using DISTRIBUTION.md.

---

## Run #2 — CreativeBatch

**Status:** LIVE LAB PROTOTYPE — publicly reachable for testing, not yet distributed to the qualified market.\n\n**Live lab:** https://davidwilsoncodes.github.io/turnovercue/lab/creativebatch/

**Initial idea:** generic batch renamer for ad creatives.

**Reality check:** direct competitors already handle generic ad-creative renaming, tokens, ZIPs and manifests.

**Pivot:** target a narrower Figma Buzz Bulk Create gap: teams already have the desired filename metadata in the source CSV but still report manually renaming large export batches.

**Target:**
- Figma Buzz Bulk Create users
- localization teams
- marketing production
- agencies
- web/content teams generating many personalised assets

**Job:** map exported files back to source CSV rows, generate filenames from spreadsheet fields, validate counts/duplicates, download a renamed ZIP and mapping manifest.

**Free wedge:**
- asset upload
- CSV upload
- arbitrary CSV-header tokens
- files-per-row mapping
- natural/drop order
- mismatch blocking
- duplicate detection
- local ZIP creation
- CSV mapping manifest
- browser-only privacy

**Possible paid wedge if earned:**
- Figma/Buzz plugin
- selected CSV field → frame/output filename
- saved mappings per template/client
- bulk frame naming before export
- export rules by file type
- team QA/naming policies

**Cash spent:** A$0

**Biggest technical assumption:** exported asset order can be matched reliably enough to CSV row order, or a lightweight matching rule can be found.

**Biggest commercial assumption:** the workflow gap is painful enough to motivate repeated use rather than a one-off workaround.

**Weak:** 5 independent successful real Buzz batches or meaningful feedback.

**Promising:** 10 repeat users or 5+ requests for an in-Figma version.

**Strong:** independent user asks/offers to pay or accepts paid pilot.

**Stop/pivot:** if real exports cannot be matched reliably, Figma closes the gap, or qualified traffic shows no meaningful use after one correction.

**Measurement markers:**\n- /turnovercue/lab/creativebatch/events/csv-loaded.html\n- /turnovercue/lab/creativebatch/events/mapping-ready.html\n- /turnovercue/lab/creativebatch/events/zip-download.html\n- /turnovercue/lab/creativebatch/events/manifest-download.html\n\n**Current next action:** run the built-in demo end-to-end, including the real ZIP export. Then test the live lab with a real Figma Buzz export + source CSV. If row/order mapping survives, move it to a neutral venture-lab host before qualified distribution.

---

## Portfolio totals

Experiments started: 2  
Public market-ready assets: 1
Live internal/lab prototypes: 1  
Qualified-market exposures completed: 0  
Revenue signals: 0  
Cash spent: A$0  
Paid subscriptions launched: 0  
Strong signals: 0  

This file should be updated from reality, not optimism.
