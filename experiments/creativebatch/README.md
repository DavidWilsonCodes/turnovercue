# CreativeBatch — Run #2

## Current thesis

**Problem:** Figma Buzz Bulk Create can generate large asset batches from CSV data, but teams still report having to manually rename exported files or frames because the useful identifier already present in the source spreadsheet is not reliably applied as the output filename.

**Free wedge:** use the same source CSV after export to map rows back to exported files and create clean filenames automatically.

## Why this pivot happened

The first Run #2 concept was a generic browser batch-renamer for ad creatives. Research immediately found direct browser-based competitors already doing token-based ad creative renaming, dimension detection, ZIP packaging and CSV export.

Rather than ship a commodity clone, the experiment narrowed to a repeated Figma Buzz-specific complaint:

- One Figma Forum thread describes manually renaming Frame1.png through Frame175.png after Bulk Create.
- Users specifically ask to choose a CSV field such as language code, slug, ID or filename and use it for the frame/export name.
- A September 24, 2026 reply describes not wanting to rename 100+ frames manually or write scripts each time.
- Other examples include 30+ language variants, 240 team-vs-team tiles and web OpenGraph images for 100+ pages.
- Figma support confirms Buzz export still sends files to the browser/download destination; CSV-driven asset naming remains a reported workflow gap.

Evidence:
- https://forum.figma.com/suggest-a-feature-11/bulk-renaming-frames-or-exported-filenames-in-figma-buzz-bulk-create-43348
- https://forum.figma.com/suggest-a-feature-11/figma-buzz-rename-title-with-spreadsheet-42628
- https://forum.figma.com/suggest-a-feature-11/ability-to-pick-the-filename-out-of-a-data-field-when-bulk-creating-50103
- https://forum.figma.com/suggest-a-feature-11/figma-buzz-bulk-uploading-exporting-and-csv-41679

## Prototype behavior

1. Drop the exported asset files.
2. Drop the original source CSV used for Bulk Create.
3. Choose how many files correspond to each CSV row.
4. Build a filename pattern using any CSV header, plus:
   - `{original}`
   - `{n}`
   - `{date}`
   - `{part}`
5. Preview every export → CSV row → new filename mapping.
6. Block ZIP export if counts do not match or generated filenames collide.
7. Download renamed copies in one ZIP.
8. Download a CSV mapping manifest.

Everything runs locally in the browser.

## Critical assumption

The prototype assumes that the export order can be made to correspond reliably to CSV row order. That assumption must be tested with real Figma Buzz exports before public launch.

This is deliberately surfaced as the biggest technical/market risk rather than hidden.

## Target users

- Figma Buzz Bulk Create users
- Marketing production teams
- Localization teams creating many language variants
- Agencies producing campaign variants
- Web/content teams generating page-specific social/OpenGraph images

## Competitive context

This is not a generic “bulk rename files” market test.

Figma already supports bulk layer renaming in Design, and generic browser renamers/ad creative naming tools exist. The experiment only remains interesting if the **CSV row → exported filename** workflow solves a Buzz-specific gap more cleanly than existing workarounds.

## Paid hypothesis — not built

If the browser workaround earns repeat usage, the likely paid product moves upstream into Figma:

- choose CSV columns as the filename/frame-name rule
- saved mappings per template/client
- bulk frame naming before export
- separate PNG/PDF naming/export rules
- team naming standards and QA
- possibly direct destination handoff

Possible hypothesis: A$5–A$15/month, but pricing is not validated.

## Evidence thresholds

**Weak:** 5 independent users successfully map a real Buzz export or provide meaningful feedback.

**Promising:** 10 repeat users, or 5+ people request an in-Figma workflow / saved mapping.

**Strong:** an independent user explicitly asks to pay, offers to pay, or accepts a paid pilot.

## Stop / pivot rule

Stop or repurpose if:
- real Buzz exports cannot be reliably matched to CSV row order without additional metadata, or
- 100 qualified visitors produce fewer than 5 meaningful uses after one positioning correction, or
- current Figma functionality closes the exact CSV-filename gap before the test reaches users.

## Current status

**FUNCTIONAL PROTOTYPE, NOT YET PUBLICLY DEPLOYED.**

Staged on branch `run2-creativebatch`.

The one recurring infrastructure constraint is that the GitHub connector cannot create a new repository. A single generic venture-lab repository would remove this manual friction for future weekly experiments.
