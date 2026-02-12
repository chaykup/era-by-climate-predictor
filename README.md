# Predicting MLB Pitcher ERA from Climate + Performance Data (2022–2025)

**Goal:** Test whether **game-day weather / venue climate** improves **single-game pitcher ERA prediction** beyond traditional pitching metrics.

This repo contains an end-to-end data science workflow: **power analysis → data extraction (APIs) → dataset build → EDA → feature engineering → modeling (XGBoost) → evaluation + interpretability**.

---

## Why this project matters (for data science work)

This project mirrors a real applied ML workflow:

- **Problem framing:** “Does adding climate context improve predictive signal?”
- **Data engineering:** large-scale API extraction, joining heterogeneous sources, handling missingness
- **Statistical thinking:** power analysis + Welch’s t-test to sanity-check relationships
- **Modeling:** baseline vs. augmented features, train/test split, metrics, residual analysis, learning curves
- **Communication:** clear takeaway + limitations and next steps

---

## Key results (from `analysis.ipynb`)

Two XGBoost regression models were trained to predict **per-game pitcher ERA** across **4 MLB seasons (2022–2025)**:

| Model | Features | RMSE | MAE | R² |
|------|----------|------|-----|----|
| **A: Pitching Only** | Rolling ERA, K/9, WHIP, FIP, IP | **4.2373** | **3.2329** | **-0.0121** |
| **B: Pitching + Climate** | Above + Temp, Humidity, Wind Speed, Elevation | **4.1991** | **3.1933** | **0.0060** |

**Takeaway:** Climate features provided a **modest improvement** (RMSE improved by **~0.90%**) and slightly improved R² from negative to slightly positive. Elevation contributed the most (e.g., thinner air at high altitude parks can affect pitch movement/ball carry).

> Important context: **single-game ERA is extremely noisy**, so even strong models struggle to predict it precisely.

---

## Data sources

- **MLB Stats API** (per-game pitcher stats, schedule/venue metadata)
- **Open-Meteo Archive API** (historical weather by venue + date/time)

---

## Feature set

**Pitching / performance features**
- Rolling ERA (recent form)
- K/9
- WHIP
- FIP (with approximate constant)
- IP (per appearance)

**Climate features**
- Temperature (°F)
- Humidity (%)
- Wind speed (mph)
- Elevation (ft)

---

## Repo contents

- **`analysis.ipynb`**  
  Full narrative analysis **with all outputs already rendered** (plots, tables, metrics, conclusions).  
  ✅ Best file for recruiters to review quickly.

- **`build.ipynb`**  
  Re-runs the pipeline end-to-end (API extraction → CSVs → merged dataset → modeling).

- **Generated datasets (created by the build pipeline)**
  - `pitcher_game_stats_2021_2025.csv` (per pitcher-game stats + venue metadata)
  - `weather_by_game.csv` (weather features aligned to game location/time)
  - `pitcher_climate_merged.csv` (final joined dataset used for EDA/modeling)

---

## How to run

### Option A (recommended): just open results
Open **`analysis.ipynb`** — it already contains all outputs, charts, and conclusions.

### Option B: reproduce everything locally (`build.ipynb`)
`build.ipynb` extracts data from the MLB Stats API + Open-Meteo and rebuilds all CSVs.

⚠️ **Runtime warning:** the extraction steps can take **up to ~1 hour** depending on network speed and API responsiveness because it pulls and merges multi-season pitcher-game logs and weather data.

#### 1) Create environment
```bash
python -m venv .venv
source .venv/bin/activate   # macOS/Linux
# .venv\Scripts\activate    # Windows
pip install -U pip
```

### 2) Install dependencies
```bash
pip install pandas numpy requests tqdm matplotlib seaborn scipy scikit-learn xgboost statsmodels
```

### 3) Run notebooks
```bash
jupyter lab
```