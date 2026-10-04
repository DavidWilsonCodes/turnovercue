# TurnoverCue

**Turn booking calendars into a cleaner-ready turnover schedule.**

TurnoverCue is a free, browser-only utility for short-term-rental hosts. Drop in one or more `.ics` booking-calendar files and it creates a cleaning schedule, flags same-day turns, generates a cleaner message, exports CSV, and prints cleanly to PDF.

## Why it exists

Small hosts often do not need another property-management platform just to translate booking dates into cleaner instructions. TurnoverCue is deliberately tiny: no account, no cleaner onboarding, and no server-side calendar upload.

## Privacy

- Calendar files are processed locally in the browser.
- No booking data is uploaded to a TurnoverCue server.
- Event descriptions are not displayed or exported.
- This first release contains no analytics.

## Try it

Open the hosted site and click **Load demo**, or upload your own `.ics` calendar.

A sample calendar is included at `sample-calendar.ics`.

## Current behaviour

- Supports one or more iCalendar files.
- Uses the filename as the property name.
- Treats all-day `DTEND` as the checkout / turnover date.
- Finds the next booking for the property.
- Flags same-day and next-day turns.
- Filters cancelled events.
- For Airbnb feeds, filters events identified as blocked / not available.
- Creates cleaner-ready text, CSV and printable output.

## Important limitation

Generic iCal feeds differ between platforms and may not distinguish owner blocks from reservations. Calendar feeds can also refresh slowly. Always verify critical same-day turnovers against the booking platform.

## Status

This is the free market-test build. The paid hypothesis — **not yet built** — is automatic read-only calendar sync, change/cancellation alerts and scheduled cleaner notifications. Those features will only be developed if real usage earns the additional infrastructure.

TurnoverCue is independent and is not affiliated with Airbnb, Vrbo, or other booking platforms.

## Licence

Copyright © 2026 David Wilson. All rights reserved. No open-source licence has been granted for this repository at this stage.
