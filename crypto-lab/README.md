# Project Jack Crypto Lab

Point-in-time crypto strategy laboratory. Every simulated decision may use only information available at that timestamp.

## Lanes
- A: Major Swing — robust BTC/ETH/SOL benchmark.
- B: Aggressive Intraday — liquid crypto, 15m/1h execution, long/short.
- C: Extreme Leverage — leverage/risk stress-test in simulation only.
- D: Launch/Moonshot — new listings, hype acceleration, launch survival and post-hype collapse.

## Anti-hindsight rules
1. No future candles or later-revised data at decision time.
2. Signal rules are versioned before unseen test periods are revealed.
3. Fees, spread, slippage, funding and liquidity constraints are included where data permits.
4. Training, validation and locked test periods remain separate.
5. Failed/delisted coins must be included where datasets permit.
6. Moonshot results use executable exits, not theoretical peak valuations.
7. Contributions are separate from trading P&L.
8. Research/paper first. No real-money order execution.

## Data contract
CSV: timestamp,open,high,low,close,volume. UTC, strictly increasing.

## Run
python crypto-lab/replay.py --csv crypto-lab/data/BTCUSDT_1h.csv --strategy aggressive_v1 --cash 100
