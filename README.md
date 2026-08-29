# Energy Storage Valuation & RL Dispatch

**Status:** 🚧 Early build — Phase 1 (data pipeline) in progress.

## What this project does

Values a natural gas or battery storage asset as a real option (a swing option) using
Longstaff-Schwartz Least-Squares Monte Carlo, then trains a reinforcement learning
agent to actually operate the asset (charge/discharge decisions) against real
historical power/gas price data. The RL agent's performance is compared honestly
against the LSMC theoretical optimum and a naive rule-based baseline.

## Why this project exists

Storage is valuable specifically *because* prices are volatile and unpredictable —
that unpredictability is what creates the option value. This project:
1. Reconstructs a realistic price model from real ISO/EIA market data
2. Computes the theoretical maximum value of a storage asset via LSMC (an
   industry-standard technique for gas storage/swing option valuation)
3. Trains an RL agent that has to make decisions in real time, without knowing
   the future — and measures how much of the theoretical value it can actually capture

## Architecture

```
data/            raw and cleaned price data (not committed — see data/README.md)
src/data_pipeline/  pulls + cleans EIA/PJM data
src/models/          price model calibration (mean-reverting process), forecasting model
src/sim_engine/      C++ Monte Carlo + LSMC valuation core
src/bindings/        pybind11 glue exposing the C++ engine to Python
src/rl/              RL environment + DQN training
tests/               unit tests, mirrors src/ structure
notebooks/           exploratory analysis only — no core logic lives here
results/             generated plots and comparison tables
```

## Setup

```bash
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

C++ build (once the sim engine exists):
```bash
mkdir build && cd build
cmake ..
cmake --build .
```

## Status / Roadmap

- [x] Repo scaffold
- [ ] Phase 1: Data pipeline (EIA/PJM ingestion + cleaning)
- [ ] Phase 2: Price model calibration
- [ ] Phase 3: LSMC valuation engine (Python prototype → C++ port)
- [ ] Phase 4: Forecasting layer
- [ ] Phase 5: RL environment + agent
- [ ] Phase 6: Comparative evaluation & writeup

## Data sources

- [EIA Wholesale Electricity Market Portal](https://eia.gov/electricity/wholesalemarkets) — day-ahead/real-time LMPs, load, generation mix
- [PJM Data Miner 2](https://dataminer2.pjm.com/) — node-level historical LMPs
- EIA Henry Hub natural gas price series
