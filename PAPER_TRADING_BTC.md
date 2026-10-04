# Paper Trading Lab — BTC/USD Spot

Started: 2026-10-05 (Australia/Brisbane)

## Purpose

Test whether a simple, explicit BTC trend-following system has a repeatable edge **before any real money is used**.

This is an experiment, not a prediction service.

## Market

- Instrument: BTC/USD spot
- Direction: Long only
- Leverage: None
- Primary decision timeframe: 4-hour candle
- Regime timeframe: Daily
- Monitoring: every 4 hours
- Starting paper capital: **US$50.00**
- Risk per trade: **1.0% of current paper equity**
- Max simultaneous positions: 1
- Assumed execution friction: **0.25% entry + 0.25% exit** until calibrated to an actual exchange
- Shorts, futures, options and leverage: prohibited in v1

Why BTC first:
- 24/7 market
- highly liquid relative to most crypto assets
- fractional position sizing
- broad public price/technical-data availability
- no need to introduce leverage to test a trading hypothesis

## Strategy v1 — 4H Trend Breakout

A long entry is valid only after a completed 4-hour candle when ALL are true:

1. **Daily regime:** daily close is above the daily 200 EMA.
2. **Daily trend:** daily 50 EMA is above daily 200 EMA.
3. **4H trend:** 4H EMA20 is above EMA50.
4. **Breakout:** the completed 4H close is above the highest high of the previous 20 completed 4H candles.
5. **Momentum:** 4H RSI(14) is between 55 and 72 inclusive.
6. **Risk sanity:** the planned stop distance is at least 1.0% and no more than 8.0% from entry.
7. No existing position is open.

No discretionary override. If one rule fails: **NO TRADE**.

## Position sizing

Initial risk budget:
US$50 × 1% = **US$0.50 maximum planned loss before execution friction**.

Stop:
- 2 × 4H ATR(14) below entry.

Position size:
- risk dollars / (entry price - stop price)
- capped at available paper cash
- include estimated transaction friction in reported trade economics.

If the required size exceeds available cash, use available cash only. Never simulate borrowing.

## Exit rules

1. Initial stop = entry - 2 × ATR(14).
2. At +2R:
   - exit 50% of the position;
   - move the remaining stop to entry plus enough buffer to approximately cover entry/exit friction.
3. Remaining 50%:
   - trail using the higher of:
     - 4H EMA20 minus 0.5 ATR, or
     - the previous stop.
4. Full exit if a completed 4H candle closes below 4H EMA50.
5. No manual profit-taking because of fear/FOMO.

## No-trade rules

- Never enter intrabar.
- Never chase because price is rising quickly.
- Never average down.
- Never add leverage.
- Never change the rules while a position is open.
- Major data disagreement across reputable sources = no trade.
- Missing indicator data = no trade.

## Experiment thresholds

Minimum sample before judging the strategy:
**30 closed paper trades.**

Track:
- win rate
- average winner in R
- average loser in R
- expectancy in R
- maximum drawdown
- profit factor
- net return after simulated friction
- average holding time
- rule violations

Promising:
- positive net expectancy after 30 trades;
- profit factor > 1.2;
- max drawdown remains tolerable for the intended tiny-capital experiment;
- results are not dependent on one outlier win.

Strong enough to consider a tiny real-money experiment:
- 50+ closed trades;
- positive after simulated fees/slippage;
- positive expectancy across more than one market regime;
- no evidence that execution friction destroys the edge.

Even then, moving to real money requires a separate decision.

## Initial market snapshot

At setup, public market data placed BTC around **US$85.2k**. Current technical pages showed a broadly bullish short-term picture, with Investing.com's BTC/USD summary showing Strong Buy across hourly, 5-hour, daily and weekly views, while some fast oscillators were already overbought.

That is **not an entry signal under this system**.

Initial position:
**FLAT — NO TRADE**

Reason:
The v1 system requires a confirmed completed-4H 20-bar breakout plus the exact daily/4H EMA and RSI filters. A generic "Strong Buy" rating is insufficient.

## Trade journal

| # | Open time | Side | Entry | Stop | Size BTC | Risk $ | Close time | Exit | Net P/L $ | R | Reason | Rules followed? |
|---|---|---:|---:|---:|---:|---:|---|---:|---:|---:|---|---|
| — | — | — | — | — | — | — | — | — | 0.00 | — | No qualifying trade yet | Yes |

## Equity

Starting equity: **US$50.00**
Current equity: **US$50.00**
Open P/L: **US$0.00**
Closed P/L: **US$0.00**
Trades closed: **0**
Current position: **FLAT**

## Change control

Any rule change creates a new strategy version.
Do not retroactively alter v1 because of a losing trade.
