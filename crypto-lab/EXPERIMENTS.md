# Experiment Registry

## A — swing_v1
Benchmark. Long only. Price > EMA20 > EMA50 > EMA200 plus prior 20-bar breakout. Risk 2% equity, 1.5 ATR stop, 2.5R target, EMA50 exit.

## B — aggressive_v1
High-risk liquid crypto. Long/short EMA-stack plus 20-bar breakout/breakdown. Risk 8%, 1.5 ATR stop, 2.5R target. Stress-test leverage separately.

## C — extreme_v1
Same signal family as B to isolate risk/leverage effects. Risk 20%. Test 1x/2x/5x/10x in simulation only.

## D — launch_hunter_v0
Must include winners and failed/rugged/delisted launches. Point-in-time features: liquidity, holder growth/concentration, unique buyers/sellers, volume acceleration, drawdown/recovery, social/news velocity, listing events, contract/rug flags. Score executable 2x/5x/10x/100x and -80%/-95%/illiquid outcomes.

## Testing
Chronological development -> validation -> locked holdout. Never random-shuffle time series. Stress: double fees/slippage, one-bar delay, remove best trade, perturb parameters +/-20%, cross-asset testing, buy-and-hold and random-entry controls.
