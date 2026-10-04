# CreativeBatch — Run #2 working prototype

## Hypothesis

Performance designers, media buyers and small agencies often export large batches of ad creatives and then spend repetitive manual time renaming, ordering and handing those files off.

A recent small-business discussion included a designer explicitly asking for a tool that renames sets of 50+ Figma ad creatives, orders them logically, exports them in one go and uploads them to Google Drive.

## Free wedge

CreativeBatch is a browser-only batch naming utility:

- Drop a large export batch.
- Define a token-based naming pattern.
- Preview every old/new filename.
- Detect duplicate generated names.
- Download renamed copies in one ZIP.
- Export a CSV manifest.
- Save the naming template locally.

No account, backend or file upload is required.

## Target user

- Performance designers
- Paid-social creative teams
- Freelance designers delivering campaign batches
- Small agencies
- Media buyers receiving inconsistent creative filenames

## Paid hypothesis — not built

Only after real repeated use:

- Figma plugin / frame naming before export
- Saved client/team naming conventions
- Automatic dimension/aspect-ratio tokens
- Google Drive / Dropbox destination upload
- Team QA rules and duplicate prevention

Possible pricing hypothesis: A$5–A$15/month.

## Evidence thresholds

Weak: 5 independent successful batches or meaningful feedback.

Promising: 10 repeat users or 5+ requests for Figma/Drive/team presets.

Strong: independent user asks to pay or accepts a paid pilot.

## Current status

FUNCTIONAL PROTOTYPE — staged on branch `run2-creativebatch`, not publicly deployed yet.

The GitHub connector currently cannot create a new repository, so the prototype is staged safely on a separate branch until a dedicated repository is created.
