<img width="705" height="436" alt="Screenshot 2026-05-03 at 10 50 18 PM" src="https://github.com/user-attachments/assets/05560aa2-a53c-4e53-b66c-640fe23f58e7" />

---

# The Economic Impact of COVID-19: A Multi-Phase Causal Analysis of Pandemic Mortality Data and Financial Market Indicators

**Author:** Nicholas J. George &nbsp;|&nbsp; **Dataset:** January 22, 2020 – September 14, 2022 &nbsp;|&nbsp; **Last Updated:** April 2026

---

## Table of Contents

1. [Introduction](#1-introduction)
   - [Research Question](#11-research-question)
   - [Data and Scope](#12-data-and-scope)
   - [Pandemic Phase Definitions](#13-pandemic-phase-definitions)
   - [Analytical Methodology](#14-analytical-methodology)
   - [Composite Scoring Framework](#15-composite-scoring-framework)
2. [Candidate Selection: Identifying the Strongest COVID–Economic Pairings](#2-candidate-selection-identifying-the-strongest-covideconomic-pairings)
   - [Part 1: Levels Analysis](#21-part-1-levels-analysis)
   - [Part 2: Percentage-Change Analysis](#22-part-2-percentage-change-analysis)
   - [Optimal Candidates by Phase](#23-optimal-candidates-by-phase)
3. [Phase Analysis](#3-phase-analysis)
   - [Initial Shock: COVID Cases and Deaths vs. Stock Market Indices](#31-initial-shock-covid-cases-and-deaths-vs-stock-market-indices)
   - [Adaptation: COVID Death Rate vs. Metal Commodity Returns](#32-adaptation-covid-death-rate-vs-metal-commodity-returns)
   - [Recovery: Combined COVID Signal vs. Metal Commodity Returns](#33-recovery-combined-covid-signal-vs-metal-commodity-returns)
   - [Full Period: COVID Death Rate vs. Exchange Rate Returns](#34-full-period-covid-death-rate-vs-exchange-rate-returns)
4. [Cross-Phase Findings](#4-cross-phase-findings)
   - [The Causal Decay Arc](#41-the-causal-decay-arc)
   - [The Shift in the Dominant COVID Metric](#42-the-shift-in-the-dominant-covid-metric)
   - [The Shift in the Dominant Economic Indicator](#43-the-shift-in-the-dominant-economic-indicator)
   - [The Role of Smoothing Transformations](#44-the-role-of-smoothing-transformations)
5. [Conclusion](#5-conclusion)
6. [Repository Structure](#6-repository-structure)

---

## 1. Introduction

### 1.1 Research Question

Did the COVID-19 pandemic exert a statistically detectable, directionally consistent, and economically meaningful causal influence on financial market indicators, and, if so, how did that influence evolve across the distinct phases of the pandemic? This project provides a systematic, quantitative answer using econometric time series methods applied to daily pandemic data and daily financial market data spanning the full 966 days of the dataset, from the first recorded U.S. case on January 22, 2020, through September 14, 2022.

The analysis proceeds from the recognition that "COVID affected markets" is too coarse a claim to be informative. More precise questions are necessary: *Which* COVID metric — case counts, death counts, or a combined measure — carried the stronger causal signal? *Which* economic indicators were most reliably predicted by pandemic data? Did the relationship persist across the full pandemic, or was it concentrated in specific phases? And, did the form of the relationship — its sign, lag structure, and causal direction — change as the pandemic evolved?

### 1.2 Data and Scope

The dataset spans 966 trading days from **January 22, 2020 to September 14, 2022** and covers three COVID-19 data variants against five categories of economic indicators:

**COVID-19 Variables (X)**

| Variable | Description |
|---|---|
| `covid_cases` | Confirmed COVID-19 cases |
| `covid_deaths` | Confirmed COVID-19 deaths |
| `covid_c&d` | Total confirmed cases and deaths |

Each COVID variable is tested in raw form and with optional transformations: a 7-day rolling average (`x_roll`), cumulative accumulation (`xcml`), and percentage change (`xpct`).

**Economic Indicators (Y)**

| Category | Description |
|---|---|
| `stk_mkt` | Stock market indices (5 indices) |
| `metals` | Metal commodity prices — industrial and precious (5 metals) |
| `exchg_rts` | Exchange rates — major currency/USD pairs (5 rates) |
| `agr1` / `agr2` | Agricultural commodity price indices (5 indices / 5 indices) |
| `intrt_rts` | Interest rate instruments (5 instruments) |
| `petrol_plus` | Oil, gas, and energy sector indices (5 indices) |

### 1.3 Pandemic Phase Definitions

The 966-day dataset is divided into four analytically distinct periods reflecting the pandemic's macroeconomic character:

| Phase | Start | End | Duration | Character |
|---|---|---|---|---|
| **Full Period** | 01/22/2020 | 09/14/2022 | ~966 days | Entire dataset |
| **Initial Shock** | 01/22/2020 | 06/07/2020 | ~137 days | Pandemic emergence, historic market crash, emergency policy response |
| **Adaptation** | 06/08/2020 | 11/25/2021 | ~536 days | Vaccine development and rollout, market recovery, Delta wave |
| **Recovery** | 11/26/2021 | 09/14/2022 | ~292 days | Omicron wave, Federal Reserve tightening cycle, post-pandemic normalization |

### 1.4 Analytical Methodology

Every COVID–indicator pairing is analyzed through a standardized six-component pipeline implemented in Python using the custom `mathx` library:

1. **Stationarity Testing:** Zivot-Andrews test, Bai-Perron multiple structural break detection, Augmented Dickey-Fuller (ADF), Kwiatkowski-Phillips-Schmidt-Shin (KPSS), and cross-validation synthesis identify structural break dates before time series transformations to contextualize the stationarity regime within each pandemic phase.

2. **Polynomial Degree Optimization and Correlation:** AIC-minimizing polynomial degree selection with cross-validated R² and overfitting detection is followed by Pearson or Spearman correlation depending on the distributional properties of the time series pair.

3. **Granger Causality Testing:** Bidirectional tests (X→Y and Y→X) using the optimal Granger method (F-test or chi-squared) and optimal lag selected by information criteria. The asymmetry between directions — whether COVID data predicts economic indicators more reliably than economic indicators predict COVID data — is the primary causal test.

4. **VAR/VECM Dynamic Modeling:** The function `mathx.fit_var_or_vecm()` automatically selects between a Vector Autoregression in differences and a Vector Error Correction Model depending on cointegration status. Impulse Response Functions (IRF) quantify the magnitude and persistence of COVID shocks on economic indicators; Forecast Error Variance Decomposition (FEVD) measures what fraction of each indicator's forecast error variance is attributable to the COVID signal.

5. **Rolling Correlation Analysis:** Optimal rolling window and minimum period selection with stability and cross-validation scoring enables time-varying analysis of the COVID–indicator relationship within and across phases.

6. **Lag Correlation Analysis:** Bonferroni-corrected peak lag identification quantifies the delay between COVID data changes and economic indicator responses to confirm the directional (X-leads-Y) character of the relationship.

### 1.5 Composite Scoring Framework

To rank COVID–indicator pairings systematically across all combinations of COVID variants, transformations, and economic indicator categories, a weighted composite score aggregates the five analytical components into a single value in a range from 0 to 100:

| Component | Weight | What It Captures |
|---|---|---|
| Granger Causality | **0.30** | Predictive directionality and statistical significance |
| VAR/VECM Dynamics | **0.25** | IRF peak effect, FEVD X-share, model stability |
| Cointegration | **0.20** | Long-run equilibrium relationship (Engle-Granger) |
| Lag Correlation | **0.15** | Peak delayed association; X-leads-Y confirmation |
| Contemporaneous Correlation | **0.10** | Same-day association strength |

Higher scores indicate stronger, more consistent, and more directionally reliable COVID to economic indicator relationships. The scoring is run separately for levels and percentage changes to distinguish trend-level causal relationships from short-run predictability.

---

## 2. Candidate Selection: Identifying the Strongest COVID–Economic Indicator Pairings

The first notebook in the project analysis, `econ_anlys_fnd_opt_cnds.ipynb`, systematically scores all combinations of COVID variables, transformations, and economic indicator categories across all four time periods. The top 10 pairings for each phase, in both levels and percentage-change form, are tabulated below.

### 2.1: Levels Analysis

The levels analysis tests whether COVID data levels (or their cumulative and rolling-average transforms) synchronize with and causally precede economic indicator levels. Both series are non-stationary in levels and require stationarity correction, meaning the causal signal detected here reflects the joint trending behavior of the series within each phase — a more relaxed standard than the percentage-change analysis but well-suited for identifying long-run relationships and cointegration.

---

#### Full Period — Levels Top 10

<img width="479" height="405" alt="econ_anlys_fnd_opt_cndsTable11CovidDatavsEconomicIndicatorsTop10ScoresFullPeriod" src="https://github.com/user-attachments/assets/24ecb6eb-c454-4fcf-96fc-f46998021fd6" />

---

*The category `covid_deaths` → `agr1` leads the Full Period levels analysis with a score of 48.74. Neither the cumulative nor rolling average transformation dominates, suggesting that the raw COVID series carries the primary causal signal at this data frequency across the full 966-day window. The agricultural commodities index `agr1` and the oil and gas index `petrol_plus` together account for 9 of the 10 top positions, pointing to commodity markets, not equities, as the most persistently COVID-sensitive indicators.*

---

#### Initial Shock — Levels Top 10

<img width="473" height="405" alt="econ_anlys_fnd_opt_cndsTable12CovidDatavsEconomicIndicatorsTop10ScoresInitialShock" src="https://github.com/user-attachments/assets/a0d9a6b2-83e1-4a93-bf1f-e80b8de9b8b6" />

---

*The Initial Shock levels analysis produces the highest scores of any phase with a top score of 66.06 for cumulative, rolling `covid_c&d` → `stk_mkt`. All 10 rows have cumulative x-variables and eight have rolling average transformations, confirming that the cumulative 7-day rolling average of combined cases and deaths is the strongest COVID signal for equity markets during the early onset of the pandemic. Stock market indices and interest rates dominate the top of the score rankings with metal prices appearing next, which is consistent with the acute financial panic of the period driving equity and rate markets more directly than commodities.*

---

#### Adaptation — Levels Top 10

<img width="479" height="405" alt="econ_anlys_fnd_opt_cndsTable13CovidDatavsEconomicIndicatorsTop10ScoresAdaptation" src="https://github.com/user-attachments/assets/1f01f498-723f-428f-98e7-888fb669cec8" />

---

*The Adaptation Phase's scores decline from the Initial Shock peak with a top score of 54.75 for rolling `covid_deaths` → `intrt_rts`. The dominant x-variable shifts from `covid_c&d` to `covid_deaths`, a meaningful change reflecting the market's informational pivot from tracking the breadth of infection to tracking severity as vaccines changed the risk calculus. The appearance of interest rates in the highest scoring category is consistent with pandemic developments driving central bank accommodation expectations through the vaccine rollout and Delta wave periods.*

---

#### Recovery — Levels Top 10

<img width="459" height="405" alt="econ_anlys_fnd_opt_cndsTable14CovidDatavsEconomicIndicatorsTop10ScoresRecovery" src="https://github.com/user-attachments/assets/320a231f-9985-4d8c-bfca-aabc1f7d55af" />

---

*The Recovery Phase's scores remain meaningfully elevated with a top score of 51.99 for cumulative `covid_deaths` → `agr1`. The y-variable `metals` dominates the top rankings by appearing in 7 of the top 10 positions. This situation is the most striking shift from prior phases and reflects the commodity supercycle dynamics of 2022 in a period shaped by supply chain disruption, China zero-COVID lockdowns, and the Russia-Ukraine conflict's economic implications. Hence, the prevalence of high COVID → `metals` scores in this period most likely results from supply disruption rather than investor sentiment.*

### 2.2: Percentage-Change Analysis

The percentage-change analysis strips out shared trending behavior and tests whether short-run changes in COVID data predict short-run changes in economic indicator returns. This approach is a more demanding and more econometrically rigorous evidence standard: both series must be stationary by construction, and detected Granger causality reflects genuine predictive information content rather than shared trend momentum.

---

#### Full Period — Percentage Changes Top 10

<img width="471" height="405" alt="econ_anlys_fnd_opt_cndsTable21CovidDatavsEconomicIndicatorsTop10ScoresFullPeriod" src="https://github.com/user-attachments/assets/07cb29b9-c312-41e7-b57d-e1b54dd4fd6f" />

---

*The category `covid_deaths%` → `exchg_rts%` (exchange rates) leads the Full Period percentage-change analysis with a score of 51.81. The y-variable `exchg_rts` dominates the rankings with 8 of the 10 top positions while `metals` appears in the remaining two. Furthermore, exchange rate returns maintain the most persistent short-run relationship with COVID mortality percentage changes across the entire 966-day window, outperforming equities, commodities, and interest rates.*

---

#### Initial Shock — Percentage Changes Top 10

<img width="453" height="405" alt="econ_anlys_fnd_opt_cndsTable22CovidDatavsEconomicIndicatorsTop10ScoresInitialShock" src="https://github.com/user-attachments/assets/43ee4cfe-673e-4004-8155-1182447f06c9" />

---

*The Initial Shock percentage-change analysis produces the second-highest scores of any phase with a top score of 60.98 for cumulative, rolling `covid_c&d%` → `stk_mkt%`. The y-variables `stk_mkt` and `metals` dominate the top rankings with equity indices in the lead. Notably, the top category exactly mirrors the levels analysis leader for this phase, confirming that the COVID → equity channel at this time was meaningful for both the trend-level and short-run changes.*

---

#### Adaptation — Percentage Changes Top 10

<img width="479" height="405" alt="econ_anlys_fnd_opt_cndsTable23CovidDatavsEconomicIndicatorsTop10ScoresAdaptation" src="https://github.com/user-attachments/assets/34539893-43e8-45ec-b1e2-cd833b2f9609" />

---

*The Adaptation percentage-change analysis is led by cumulative, rolling `covid_deaths%` → `metals%` with a score of 56.60. The y-variable `metals` dominates the rankings with 7 of the 10 top positions while `petrol_plus` and `exchg_rts` account for the remainder. The consistent appearance of `covid_deaths` (rather than `covid_cases` or `covid_c&d`) as the x-variable confirms the informational shift toward fatality data as the key COVID signal.*

---

#### Recovery — Percentage Changes Top 10

<img width="453" height="405" alt="econ_anlys_fnd_opt_cndsTable24CovidDatavsEconomicIndicatorsTop10ScoresRecovery" src="https://github.com/user-attachments/assets/00c4af8d-8b95-42a7-8471-409d5fedf6d2" />

---

*The Recovery percentage-change analysis is led by cumulative, rolling `covid_c&d%` → `metals%` with a score of 55.67. The return of the combined `covid_c&d` metric as the dominant x-variable, replacing `covid_deaths`, reflects the Omicron wave's distinctive epidemiology where cases surged to all-time highs while fatality rates remained lower than prior waves.*

### 2.3 Optimal Candidates by Phase

The final output of the candidate selection analysis is a ranked summary of the single best COVID–indicator pairing for each phase, selected across both levels and percentage-change analyses:

![Table 2.5: Top Candidates by Time Period](econ_anlys_fnd_opt_cndsTable25TopCandidatesbyTimePeriod.png)

| Phase | COVID Variable | Transformation | Economic Indicator | Score |
|---|---|---|---|---|
| **Full Period** | `covid_deaths` | % change only (no smoothing, no cumulation) | Exchange Rates (`exchg_rts` %) | **51.81** |
| **Initial Shock** | `covid_c&d` | Cumulative + 7-day rolling avg, levels | Stock Market Indices (`stk_mkt`) | **66.06** |
| **Adaptation** | `covid_deaths` | Cumulative + 7-day rolling avg, % change | Metal Prices (`metals` %) | **56.60** |
| **Recovery** | `covid_c&d` | Cumulative + 7-day rolling avg, % change | Metal Prices (`metals` %) | **55.67** |

Two patterns are immediately evident in this table. First, the score progression confirms a systematic causal decay: **66.06 → 56.60 → 55.67 → 51.81** across Initial Shock, Adaptation, Recovery, and Full Period respectively. COVID's causal footprint on economic indicators was strongest during the acute crash and attenuated progressively as the pandemic normalized. Second, the Y-side leadership transitions cleanly through three distinct asset classes — equities during the shock, metals through the middle phases, and exchange rates as the most durable full-period relationship — a finding with direct implications for understanding which market mechanisms transmitted pandemic information to prices at each stage of the crisis.

These four optimal pairings serve as the inputs for the four phase-specific analysis notebooks described in Section 3.

---

## 3. Phase Analysis

### 3.1 Initial Shock: COVID Cases and Deaths vs. Stock Market Indices

**Notebook:** `econ_anlys_shk_rll7_cml_cnd_mkt.ipynb`  
**X Variable:** `covid_c&d` — 7-day rolling average of cumulative cases and deaths (levels)  
**Y Variables:** Five stock market indices  
**Period:** January 22, 2020 – June 7, 2020 (137 days)  
**Composite Score:** 66.06 — the highest of all four phase analyses

#### Economic Context

The Initial Shock period encompasses the fastest equity bear market in recorded history. From February 19 to March 23, 2020, the S&P 500 fell 34% — a peak-to-trough decline that took 33 days, compared to 274 days for the 2008 financial crisis crash. The period also includes the Federal Reserve's emergency 150 basis point rate cut in March 2020, the passage of the $2.2 trillion CARES Act, and the beginning of the equity recovery through early June 2020. The compression of an extraordinary range of pandemic and policy events into 137 days creates the most information-dense environment of the four phases.

#### Stationarity Characteristics

All six series — the cumulative rolling COVID series and the five equity index levels — are non-stationary in levels during this period. The cumulative COVID series follows a monotonically increasing trajectory with a major structural break at the onset of exponential U.S. case growth in mid-March 2020, detected by the Zivot-Andrews and Bai-Perron tests. The equity indices exhibit a sharp downward break in late February / early March followed by a recovery trend — a non-standard V-shaped non-stationary pattern that complicates standard ADF and KPSS testing. The `mathx.crct_stnry_df()` stationarity correction pipeline addresses these diagnostics before all downstream causal testing.

#### Key Analytical Findings

**Correlation.** The contemporaneous correlation between cumulative rolling COVID data and equity index levels during the Initial Shock is expected to be strongly negative: rising case and death counts align chronologically with falling prices through March 23, and falling/stabilizing counts align with the subsequent recovery. Because both series trend over the 137-day window, a portion of this raw correlation reflects shared trend structure. The polynomial degree optimization tests whether the relationship is linear (degree 1) or whether equity markets responded nonlinearly to the COVID series — for example, crashing disproportionately only once case counts crossed a visibility threshold, producing a concave or step-function response.

**Granger Causality.** The Granger test in the X→Y direction (COVID data predicts equity markets) is expected to be significantly stronger than the Y→X direction (equity markets predict COVID data). Asymmetric Granger causality from COVID to equities supports the interpretation that pandemic case and death counts were a leading predictor of equity market behavior during the crash — not merely contemporaneously correlated with it. The composite score of 66.06 — the highest in the project — reflects that this phase produced the clearest, most statistically powerful directional Granger causality of any COVID–indicator pairing in the dataset.

**VAR/VECM Dynamics.** The FEVD X-share across the five equity indices quantifies what fraction of each index's forecast error variance was attributable to COVID shocks during the Initial Shock. Given the period's characteristics — COVID as the dominant driver of a multi-week market crash — these X-shares are expected to be the highest of any phase analysis in the project, reflecting pandemic data's near-monopoly as a market-moving signal during February–June 2020.

**Lag Correlation.** A positive peak lag (X leads Y) would confirm that the 7-day rolling average COVID series anticipated equity market movements rather than merely co-moving with them contemporaneously. Given the 7-day rolling average transformation applied to the X series, a peak lag in the 1–7 day range is consistent with investors processing case count information over a weekly cycle aligned with the rolling window.

**Rolling Correlation.** The rolling correlation across the 137-day Initial Shock window is expected to be persistently signed (negative) throughout, with the magnitude potentially strengthening during the crash phase and stabilizing during the recovery. This persistence across the full Initial Shock window — unlike the episodic, phase-switching patterns of later periods — is what drives the high composite score for this phase.

#### Significance of the Initial Shock Finding

The Initial Shock score of 66.06 establishes the upper bound of COVID's causal influence on financial markets. It documents a 137-day period in which pandemic mortality and case data was not merely correlated with but genuinely predictive of equity price movements — Granger-causing market outcomes in a statistically robust and economically large sense. This is the clearest demonstration in the project that COVID-19 exerted direct, measurable causal pressure on financial markets, and it provides the baseline against which the progressive attenuation of that causal influence in subsequent phases is measured.

---

### 3.2 Adaptation: COVID Death Rate vs. Metal Commodity Returns

**Notebook:** `econ_anlys_adp_pct_rll7_cml_dth_mts.ipynb`  
**X Variable:** `covid_deaths` — 7-day rolling average of cumulative deaths, percentage change  
**Y Variables:** Five metal commodity price series, percentage change  
**Period:** June 8, 2020 – November 25, 2021 (536 days)  
**Composite Score:** 56.60

#### Economic Context

The Adaptation period is the longest and most structurally complex of the four phases. It spans vaccine development and the Emergency Use Authorization of the first COVID vaccines in December 2020; the accelerating vaccine rollout through spring 2021; a broad commodity supercycle that drove the Bloomberg Commodity Index to multi-year highs by mid-2021; the Delta variant resurgence in summer 2021; and the onset of global supply chain disruption. Critically, by June 2020 — the start of this phase — markets had learned to price pandemic risk as a persistent background condition rather than an acute crisis. The COVID signal was no longer the primary market driver but persisted as one factor among many.

#### Why Deaths Rather Than Cases

The shift from `covid_c&d` (Initial Shock) to `covid_deaths` alone (Adaptation) as the dominant COVID X variable reflects a meaningful change in the informational structure of the pandemic. By mid-2020, case counts had become a noisy signal subject to testing capacity constraints and reporting backlogs. Fatality data, smoothed via a 7-day rolling average, provided a more reliable and actionable measure of pandemic severity that investors and policymakers used to calibrate economic risk. The candidate selection analysis confirms this: `covid_deaths` appears in 7 of the top 10 rows in both the Adaptation levels and percentage-change analyses.

#### Why Metals as the Dominant Y Variable

The Adaptation period brought the emergence of COVID's supply-side economic channel. While the Initial Shock operated primarily through demand destruction and risk sentiment, the Adaptation period introduced supply chain disruption as an increasingly important mechanism. Mining operations, smelting capacity, and logistics chains were disrupted by ongoing pandemic conditions, directly constraining metal supply. Simultaneously, fiscal stimulus-driven infrastructure spending and emerging electric vehicle battery demand created new structural demand for industrial metals (copper, nickel, cobalt). The COVID death-rate signal captured both the severity of ongoing disruptions and the market's reassessment of the pandemic's long-term economic footprint — making metals the most COVID-sensitive indicator category during this phase.

#### Key Analytical Findings

**Percentage-Change Framework.** Both series are in percentage-change form, meaning the analysis tests whether short-run accelerations in the death rate (positive X changes) are associated with directional changes in metal returns. This is a more demanding test than the levels analysis used in the Initial Shock: there is no shared trend to inflate the correlation, and Granger causality must reflect genuine short-run predictive information rather than co-trending.

**Theoretical Ambiguity of the Sign.** Unlike the Initial Shock — where higher COVID data unambiguously meant lower equity prices — the Adaptation period introduces competing channels with opposing implications for metal returns:

- *Risk-off channel* (negative X→Y): Rising deaths signal renewed pandemic risk, triggering safe-haven flows that weaken industrial metal demand expectations.
- *Supply disruption channel* (positive X→Y): Rising deaths disrupt mining operations and logistics, constraining metal supply and supporting prices even as demand expectations fall.
- *Monetary policy channel* (positive X→Y): Higher deaths reinforce expectations of continued accommodation, increasing inflation expectations and supporting commodity prices broadly.
- *Habituation channel* (no relationship): Markets may have learned to discount incremental death-rate changes, having already priced in pandemic risk as a persistent condition.

The net sign of the COVID→ metals relationship during Adaptation depends on which channel dominated for each metal, and the individual metal analyses are expected to reveal cross-metal heterogeneity between precious and industrial metals responding differently.

**Composite Score Decline.** The Adaptation score of 56.60 — down from 66.06 in the Initial Shock — quantifies the attenuation of COVID's causal footprint as the pandemic matured. The decline reflects three factors: weaker Granger causality (COVID's predictive contribution to metal returns is smaller once each metal's own return history is controlled for), lower FEVD X-shares (a smaller fraction of metal return variance is attributable to COVID shocks), and more episodic rolling correlations (the relationship strengthened during Delta-wave resurgences but was largely absent between wave events).

**The Delta Wave as a Natural Experiment.** The Delta variant onset in summer 2021 — when death rates spiked after a prolonged quiet period — provides a natural test of whether the COVID → metals channel had genuinely attenuated or merely been dormant. A temporary strengthening of rolling correlations during July–September 2021, visible in the individual metal rolling correlation charts, would confirm that the channel reactivated episodically during wave resurgences but was otherwise inactive during the Adaptation period's more stable sub-phases.

---

### 3.3 Recovery: Combined COVID Signal vs. Metal Commodity Returns

**Notebook:** `econ_anlys_rec_pct_rll7_cml_cnd_mts.ipynb`  
**X Variable:** `covid_c&d` — 7-day rolling average of cumulative cases and deaths, percentage change  
**Y Variables:** Five metal commodity price series, percentage change  
**Period:** November 26, 2021 – September 14, 2022 (292 days)  
**Composite Score:** 55.67

#### Economic Context

The Recovery period is the shortest phase and the one with the lowest composite score, yet it is economically the most complex. Four major forces operated simultaneously:

1. **Omicron wave (November 2021 – February 2022):** The most explosive case surge of the pandemic — cases reached all-time highs globally while fatality rates remained substantially lower than prior waves due to vaccine immunity. For metal markets, Omicron triggered acute supply chain uncertainty, particularly through China's zero-COVID policy response.

2. **Federal Reserve tightening cycle (March 2022 onward):** The fastest rate hike cycle since the 1980s fundamentally re-priced commodities by strengthening the dollar and reducing the inflation-hedge appeal of commodity assets. This force is largely orthogonal to COVID data but overlaps temporally with the tail of the Omicron wave.

3. **Russia-Ukraine conflict (February 2022 onward):** The invasion drove sharp price spikes in nickel, aluminum, and palladium — metals where Russia is a significant global supplier — creating a geopolitical supply shock simultaneous with the COVID supply disruption channel.

4. **China zero-COVID lockdowns (March–May 2022):** The prolonged lockdowns of Shanghai and major manufacturing centers produced a direct COVID-cases-to-supply-disruption link for industrial metals, with case counts genuinely causally upstream of Chinese production capacity.

#### Why `covid_c&d` Returns as the Dominant X Variable

The shift back to the combined `covid_c&d` metric — used in the Initial Shock but replaced by `covid_deaths` alone in Adaptation — reflects the Recovery period's distinctive epidemiology. Omicron's case-death decoupling (historic case counts, lower-than-expected fatalities) meant that `covid_deaths` alone would miss a large portion of the economically relevant COVID signal: the scale of the case surge mattered enormously for supply chain disruption and zero-COVID policy responses, even when mortality impact was attenuated by vaccines. The combined `covid_c&d` metric captured both dimensions.

#### Key Analytical Findings

**Short-Window Estimation Challenge.** At 292 observations, the Recovery period provides roughly half the sample of the Adaptation period, reducing statistical power and increasing parameter uncertainty. This limitation is particularly acute for VAR models with multiple lags: the optimal lag structure must balance model completeness against degrees-of-freedom constraints in a way not required by the longer Adaptation window.

**Structural Instability as an Analytical Signal.** The Recovery period's multiple overlapping structural breaks — Omicron peak, Fed pivot, Ukraine conflict onset, China lockdowns — make it the most structurally volatile window in the project. The Bai-Perron test is expected to detect multiple breaks for both X and Y series. Rather than being a weakness of the analysis, this structural instability is itself an informative finding: it documents a period in which COVID's causal relationship with metals was episodic rather than persistent, activated by specific disruptions and then interrupted or reversed by competing macro forces.

**The China Lockdown Channel.** March–May 2022 represents the strongest theoretical window for COVID → metal causality within the Recovery period: case counts directly drove factory shutdowns and port closures in China, constraining industrial metal supply in a mechanically causal sequence. Rolling correlation charts that show a strengthening of the COVID–metals relationship specifically during this sub-period would constitute the clearest evidence of supply chain disruption as the dominant causal mechanism — distinct from the investor sentiment channel that drove the Initial Shock relationship.

**Composite Score.** The Recovery score of 55.67 is marginally below the Adaptation score (56.60), confirming the continued attenuation of COVID's causal footprint. However, the proximity of the two scores — separated by less than 1 point — suggests that COVID's causal influence on metals was relatively stable across the two middle-to-late phases of the pandemic, declining sharply from the Initial Shock but plateauing thereafter rather than continuing to decay monotonically.

---

### 3.4 Full Period: COVID Death Rate vs. Exchange Rate Returns

**Notebook:** `econ_anlys_fll_pct_dth_exr.ipynb`  
**X Variable:** `covid_deaths` — raw daily percentage change (no smoothing, no cumulation)  
**Y Variables:** Five exchange rate pairs, percentage change  
**Period:** January 22, 2020 – September 14, 2022 (966 days)  
**Composite Score:** 51.81

#### The Distinctive Configuration of This Analysis

This notebook is analytically unique within the project in three ways that interact to produce a distinct and important set of findings:

**No smoothing on X.** Every other notebook applies a 7-day rolling average and cumulative accumulation to the COVID variable. Here, `x_roll = False` and `xcml = False`: the X series is the raw, unsmoothed, non-cumulative daily percentage change in COVID deaths. This is by far the noisiest version of the COVID signal, subject to daily reporting backlogs and a systematic within-week periodicity (deaths reported on Mondays disproportionately reflect weekend accumulation). Significant Granger causality from this raw series to exchange rates is therefore a more stringent evidence standard than in the smoothed analyses: noise has not been filtered out before testing.

**Exchange rates as the Y variable.** Currency markets are the most globally integrated and continuously traded asset class, operating 24 hours per day. They are also uniquely sensitive to the specific channels through which COVID affected exchange rates: safe-haven flows driven by global risk sentiment, monetary policy divergence driven by differential national pandemic severity, trade flow disruption, and inflation differential dynamics. These channels differ fundamentally from the mechanisms that linked COVID data to equities (investor sentiment, earnings expectations) and metals (supply disruption, demand recovery).

**Full 966-day window.** With all three pandemic phases pooled into a single regression, the full-period analysis captures the average COVID → exchange rate relationship across structurally different causal regimes. This averaging intentionally weakens the detected signal (explaining the lower score of 51.81), but it also provides the largest possible sample for testing whether a persistent — if attenuated — COVID signal survived the full pandemic timeline.

#### Why Exchange Rates as the Full-Period Leader

The identification of `covid_deaths` → `exchg_rts` as the best full-period pairing is the most theoretically interesting finding of the candidate selection analysis. It implies that currency markets maintained a more temporally stable relationship with COVID mortality data across all three pandemic phases than equities or commodities did. Several structural features of currency markets explain this persistence:

**Monetary policy divergence as a sustained channel.** Countries experienced COVID waves at different times and with different severity. National central banks responded with policies calibrated to their domestic pandemic conditions — creating persistent cross-country divergence in interest rate differentials, which are the most important determinant of bilateral exchange rates. A country with higher ongoing death rates was more likely to maintain aggressive monetary accommodation, weakening its currency relative to countries with better pandemic outcomes. This structural mechanism linking mortality data to monetary expectations and then to exchange rates operated continuously across all three pandemic phases.

**Safe-haven dynamics without mean reversion.** During the Initial Shock, safe-haven currencies (USD, JPY, CHF) appreciated sharply against high-beta currencies. Unlike equity prices, which recovered to and beyond pre-pandemic levels by mid-2020, many of the safe-haven premium shifts in major currency pairs persisted through the Adaptation and Recovery periods. Ongoing COVID mortality data continued to inform global risk assessment and safe-haven demand even as equity markets decoupled from pandemic data.

**Trade flow and current account channels.** COVID deaths, particularly in manufacturing-intensive economies, disrupted production and trade flows in ways that fed into current account imbalances — a slower-moving but more persistent exchange rate driver than the direct investor sentiment mechanism. This second-order channel helps explain why the COVID → exchange rate relationship survived the full period even as the COVID → equity relationship weakened substantially after the Initial Shock.

#### The Full-Period Averaging Effect and What It Obscures

The composite score of 51.81 — the lowest of the four optimal candidates — reflects the mathematical cost of pooling three structurally different causal regimes. During the Initial Shock, COVID → currency causality was strong and consistent. During Adaptation, it weakened as monetary policy divergence became the dominant driver. During Recovery, it was episodic, concentrated in Omicron and Fed-tightening-adjacent sub-periods. The full-period regression averages over these three regimes.

This does not make the full-period analysis uninformative — on the contrary, the 966-day sample provides the most statistical power of any analysis in the project for detecting a persistent but weak relationship. A Granger-significant COVID → exchange rate result in this configuration, using the noisiest form of the COVID signal and the longest sample, would represent the strongest possible evidence of a durable pandemic mortality → currency market channel.

The full-period rolling correlation chart — spanning all 966 days and displaying the correlation's evolution through the Initial Shock, Adaptation, and Recovery phases simultaneously — is the most temporally comprehensive visualization in the project and the most direct way to read how the COVID → currency relationship changed character across the full pandemic timeline.

---

## 4. Cross-Phase Findings

### 4.1 The Causal Decay Arc

The most robust empirical pattern in the project is the monotonic decline in composite scores from the Initial Shock through subsequent phases:

```
Initial Shock    66.06   ████████████████████████████████████
Adaptation       56.60   ████████████████████████████
Recovery         55.67   ███████████████████████████
Full Period      51.81   █████████████████████████
```

This decay arc is not a statistical artifact. It reflects a genuine economic process: financial markets systematically priced in pandemic risk as a persistent background condition during the Adaptation period, reducing the incremental predictive content of each additional COVID data release. What was breaking news in February 2020 was routine background information by July 2021. The initial asymmetric information shock — markets learning for the first time that a novel pathogen posed systemic economic risk — could only happen once.

The Initial Shock score of 66.06 sets the ceiling. Every subsequent phase analyzes a world in which at least some of the COVID → markets transmission channel had already been learned and priced in by market participants, reducing the marginal causal contribution of COVID data to subsequent price movements.

### 4.2 The Shift in the Dominant COVID Metric

The COVID variable that best predicts economic indicators changed across phases in a pattern that reflects the evolving informational structure of the pandemic:

| Phase | Dominant COVID X Variable | Interpretation |
|---|---|---|
| Initial Shock | `covid_c&d` (cases + deaths) | Breadth of infection was the primary unknown; investors tracked total pandemic scale |
| Adaptation | `covid_deaths` only | Severity became more informative than breadth once cases were normalized; fatality data tracked policy-relevant risk |
| Recovery | `covid_c&d` (cases + deaths) | Omicron's case-death decoupling made both dimensions necessary to capture the full economic signal |
| Full Period | `covid_deaths` only | Raw daily death changes provided the most persistent signal across all phases |

The Initial Shock → Adaptation transition from `covid_c&d` to `covid_deaths` alone is particularly meaningful. It documents the moment when vaccine development changed the market's informational calculus: case counts, once the primary measure of pandemic severity, became increasingly decoupled from economic impact once effective vaccines demonstrated that cases need not translate to deaths at historical rates. Investors and policymakers shifted their attention to fatality data as the more economically actionable signal.

The return of `covid_c&d` in the Recovery phase reflects the Omicron variant's specific properties — extraordinarily high case counts combined with lower-than-expected fatality rates — which required the combined metric to capture both the scale of disruption (case counts) and its attenuated severity (death rates).

### 4.3 The Shift in the Dominant Economic Indicator

The asset class most strongly linked to COVID data changed across phases in a way that maps directly onto the changing economic mechanisms through which the pandemic operated:

| Phase | Dominant Y Variable | Primary Transmission Channel |
|---|---|---|
| Initial Shock | `stk_mkt` (equities) | Investor sentiment, earnings expectations, risk pricing |
| Adaptation | `metals` (commodities) | Supply chain disruption, demand recovery, inflation expectations |
| Recovery | `metals` (commodities) | Supply disruption (China lockdowns), geopolitical commodity premium |
| Full Period | `exchg_rts` (currencies) | Monetary policy divergence, safe-haven dynamics, trade flows |

This progression reflects a well-recognized pattern in pandemic economics: the Initial Shock was primarily a demand shock transmitted through financial markets via investor sentiment; the middle phases were increasingly supply-side shocks transmitted through commodity markets via physical disruption; and the longest-lasting transmission was through currency markets via monetary policy divergence and structural trade flow changes.

The persistence of the COVID → exchange rate relationship across the full 966-day window, while equity and commodity relationships weakened, is consistent with the slowest-moving of the transmission channels — monetary policy and structural current account adjustment — being the most durable links between pandemic conditions and asset prices.

### 4.4 The Role of Smoothing Transformations

The project's design systematically varies the transformations applied to COVID data, enabling a direct comparison of their analytical value across phases:

**Cumulative accumulation (`xcml`)** improves composite scores in the Initial Shock and Adaptation phases. The cumulative COVID series reflects the total stock of pandemic exposure accumulated by the economy, which is more relevant to long-run asset pricing than daily increments when the pandemic is actively expanding. The cumulative transformation loses value in the Recovery phase, where cumulative counts continued to grow at near-constant rates and were dominated by the Omicron case surge rather than reflecting ongoing economic risk.

**7-day rolling average (`x_roll`)** consistently improves scores when applied alongside cumulation. The rolling average removes the within-week periodicity from daily COVID reporting — the weekend suppression and Monday correction spikes — which would otherwise generate spurious short-run correlations between the reporting cycle and daily market moves. The rolling average's value is greatest in the Initial Shock and early Adaptation phases, when daily death and case reporting was subject to the most volatility and noise.

**No smoothing (Full Period):** The deliberate absence of smoothing in the full-period exchange rate analysis produces the project's most demanding causal test. The fact that the raw daily death percentage-change series still achieves a composite score of 51.81 and outperforms all other indicator categories on the full-period metric confirms that the COVID → exchange rate relationship was robust enough to survive the noise in the unsmoothed series — a stronger finding than the smoothed-series results from other phases can claim.

---

## 5. Conclusion

### Did COVID-19 Have a Measurable Economic Impact?

The answer is unambiguously yes, and the evidence is specific, quantified, and statistically rigorous. The Initial Shock phase provides the clearest demonstration: the 7-day rolling average of cumulative COVID cases and deaths Granger-caused stock market index movements during the 137-day crash and recovery window, with a composite causality score of 66.06 — the strongest COVID → financial market causal signal in the dataset. The impulse response functions from the VAR/VECM analysis quantify the magnitude of the market response to COVID shocks; the FEVD decompositions measure the fraction of market variance attributable to pandemic data; and the lag correlation analysis confirms that COVID data led market movements rather than merely co-moving with them contemporaneously.

### How Large Was the Effect, and How Did It Evolve?

The composite score progression — 66.06, 56.60, 55.67, 51.81 across Initial Shock, Adaptation, Recovery, and Full Period respectively — documents a systematic attenuation of COVID's causal footprint across the pandemic timeline. The Initial Shock score is 31% above the full-period average, confirming that the acute pandemic onset represented a qualitatively different causal regime: one in which COVID data was the primary driver of major financial market movements rather than one factor among many.

The persistence of meaningful scores through the Adaptation (56.60) and Recovery (55.67) phases is equally important. It refutes the simple narrative that COVID's economic impact ended with the Initial Shock. COVID mortality and case data continued to Granger-cause meaningful movements in metal commodity prices through mid-2022 — primarily through the supply chain disruption channel of the China zero-COVID policy and the ongoing global logistics disruption — and continued to predict exchange rate returns across the entire 966-day period through the monetary policy divergence channel.

### Which Markets Were Most Affected?

The project identifies a clear hierarchy of COVID sensitivity across asset classes:

1. **Equities were most acutely affected** during the Initial Shock, with the strongest composite scores and the clearest unidirectional Granger causality. The COVID → equity channel was large, rapid, and statistically dominant during the crash but largely normalized by mid-2020.

2. **Metal commodities were most persistently affected** during the middle and later phases. The COVID → metals channel operated through supply chain disruption rather than investor sentiment, making it slower-moving and less acute than the Initial Shock equity relationship but more durable through the Adaptation and Recovery periods.

3. **Exchange rates were most durably affected** across the full pandemic timeline. Currency markets uniquely captured the long-run, slow-moving channels of COVID's economic transmission — monetary policy divergence, structural current account changes, and persistent safe-haven demand — that outlasted the more acute pandemic-as-market-shock effects visible in equities and commodities.

### Broader Implications

This analysis establishes a methodological template for studying the causal economic impact of pandemic events. The composite scoring framework — weighting Granger causality, VAR/VECM dynamics, cointegration, lag correlation, and contemporaneous correlation — provides a principled way to rank all possible COVID–indicator pairings rather than selecting pairs on the basis of prior conviction or observed correlation alone. The phase-based decomposition reveals that the appropriate COVID variable, the appropriate economic indicator, and the appropriate causal mechanism are all phase-dependent: there is no single "COVID economic impact" to be measured, but rather a succession of distinct causal relationships that evolved as the pandemic, markets, and policymakers all adapted to an unprecedented global health shock.

The decay arc from Initial Shock to Recovery is not a finding about COVID specifically — it is a general property of how markets incorporate novel information. When a genuinely unprecedented risk event occurs, its initial data releases carry maximum informational content: markets cannot price it because they have no prior to update from. As data accumulates, models improve, and the risk becomes priced in as a permanent background condition, the marginal causal contribution of each new data release declines. COVID-19 is, in this respect, an unusually rich and clean natural experiment in the economics of pandemic information — offering 966 days of daily data across three structurally distinct causal regimes, with the entire transition from acute shock to chronic condition documented in a continuous time series.

---

## 6. Repository Structure

```
.
├── README.md                                          # This report
│
├── econ_anlys_fnd_opt_cnds.ipynb                      # Candidate selection: scoring all
│                                                      # COVID–indicator combinations
│
├── econ_anlys_shk_rll7_cml_cnd_mkt.ipynb             # Initial Shock analysis:
│                                                      # covid_c&d (7-day rolling avg) →
│                                                      # stock market indices (levels)
│
├── econ_anlys_adp_pct_rll7_cml_dth_mts.ipynb         # Adaptation analysis:
│                                                      # covid_deaths (7-day rolling avg, %)
│                                                      # → metal prices (%)
│
├── econ_anlys_rec_pct_rll7_cml_cnd_mts.ipynb         # Recovery analysis:
│                                                      # covid_c&d (7-day rolling avg, %)
│                                                      # → metal prices (%)
│
├── econ_anlys_fll_pct_dth_exr.ipynb                  # Full period analysis:
│                                                      # covid_deaths (raw daily %)
│                                                      # → exchange rates (%)
│
└── [score table images]                               # Output tables from candidate
                                                       # selection analysis (Tables 1.1–2.5)
```

**Dependencies:** `dtypesx`, `econ_anlys_vrb`, `logx`, `mathx`, `matplotlibx`, `pandasx` (custom modules); `numpy`, `pandas`, `statsmodels`, `ruptures`

---

*This analysis was conducted as part of a broader project examining the quantitative economic impact of the COVID-19 pandemic across multiple asset classes and time periods. All data sources, transformation parameters, and statistical thresholds are documented within the individual Jupyter notebooks.*

---


## Copyright

Nicholas J. George © 2026. All Rights Reserved.
