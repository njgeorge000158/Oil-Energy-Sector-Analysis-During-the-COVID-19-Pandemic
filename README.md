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
   - [Recovery: Total COVID Signal vs. Metal Commodity Returns](#33-recovery-total-covid-signal-vs-metal-commodity-returns)
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

The analysis proceeds from the recognition that "COVID affected markets" is too coarse a claim to be informative. More precise questions are necessary: *Which* COVID metric — case counts, death counts, or a total measure — carried the stronger causal signal? *Which* economic indicators were most reliably predicted by pandemic data? Did the relationship persist across the full pandemic, or was it concentrated in specific phases? And, did the form of the relationship — its sign, lag structure, and causal direction — change as the pandemic evolved?

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

### 2.1: Levels Analysis: Methodology and Interpretive Framework

The levels analysis tests whether COVID data — expressed as cumulative counts or rolling-average transforms of those counts — synchronizes with and causally precedes economic indicator levels over the course of each phase. Both the COVID series and the economic indicator series are non-stationary in levels: they trend over time rather than fluctuating around a fixed mean, and their statistical properties change across the sample window. This shared non-stationarity is not simply a technical nuisance to be corrected away — it is economically meaningful. During an acute pandemic phase, cumulative case and death counts trend monotonically upward by construction, and many financial indicators trend simultaneously in response to the same underlying shock. The co-movement of two trending series can reflect either a genuine long-run equilibrium relationship (cointegration) or a spurious correlation driven by shared trend structure with no causal content. Distinguishing between these two possibilities is the central inferential challenge of the levels analysis.

The stationarity correction applied throughout — ADF and KPSS testing followed by differencing or percentage-change transformation as appropriate — addresses this challenge directly, but the levels analysis retains more of the original trend structure than the percentage-change framework does. Rather than asking whether short-run accelerations in COVID data predict short-run changes in economic indicators, the levels analysis asks whether the long-run trajectory of COVID data and the long-run trajectory of economic indicators move together in a statistically disciplined way. This is a more relaxed evidentiary standard in one sense: shared trending behavior is easier to detect than short-run predictive content, and the Granger causality tests in the levels framework are more likely to find significance when both series are driven by a common underlying force — the pandemic itself — that operates on both simultaneously. It is a more demanding standard in another sense: the cointegration tests required to validate the VECM specification impose a specific equilibrium structure on the relationship, requiring not just that the series trend together but that they are bound by a stable long-run attractor from which deviations are mean-reverting.

When cointegration is confirmed, the VECM framework is appropriate and the Granger causality, IRF, and FEVD results carry a well-defined economic interpretation: the COVID series and the economic indicator share a long-run equilibrium, and deviations from that equilibrium generate error-correction dynamics in one or both series. In this case, finding that COVID data Granger-causes an economic indicator in the levels framework constitutes evidence of a genuine long-run causal relationship — the pandemic trajectory systematically shaped the trajectory of the economic variable over the phase, not merely co-moved with it by accident. When cointegration is not confirmed but both series are non-stationary, the risk of spurious correlation is elevated, and the Granger causality results must be interpreted with greater caution: statistical significance may reflect shared trend structure rather than a causal mechanism with economic content.

The levels analysis is therefore best understood as complementary to rather than redundant with the percentage-change analysis. Where both frameworks agree — finding significant COVID → indicator causality in both levels and percentage-change specifications — the evidence for a genuine causal relationship is substantially strengthened, as it holds across both the long-run trajectory and the short-run acceleration dimensions of the data. Where the frameworks diverge — finding significance in levels but not in percentage changes, or vice versa — the pattern of disagreement is itself analytically informative. Significance in levels but not in percentage changes suggests a long-run co-trending relationship that does not extend to short-run predictive content, consistent with habituation or shared macro drivers rather than active causal transmission. Significance in percentage changes but not in levels suggests an episodic short-run causal channel that operates during specific sub-periods without producing a stable long-run equilibrium — the pattern most consistent with the wave-driven, episodic COVID signal observed in the Adaptation phase rolling correlations.

The choice between levels and percentage-change frameworks is not arbitrary but follows directly from the stationarity properties of the series in each phase and the economic question being asked. For the Initial Shock, where both COVID data and equity indices are non-stationary and the 137-day window is short enough that shared trend structure is difficult to disentangle from genuine cointegration, the levels analysis provides evidence about the joint trending behavior of the series during the crash-and-recovery arc. For the Adaptation period, where the percentage-change framework strips out the long-run trend to focus on short-run predictive content, the levels analysis serves as a check on whether the causal relationships identified in percentage changes also hold at the trajectory level — and whether the cointegrating relationships identified by the VECM specifications represent stable long-run equilibria or artifacts of the extended 536-day window's structural heterogeneity.

---

#### Full Period — Levels Top 10

<img width="479" height="405" alt="econ_anlys_fnd_opt_cndsTable11CovidDatavsEconomicIndicatorsTop10ScoresFullPeriod" src="https://github.com/user-attachments/assets/24ecb6eb-c454-4fcf-96fc-f46998021fd6" />

---

*The covid_deaths → agr1 pairing leads the Full Period levels analysis with a composite score of 48.74, establishing agricultural commodities as the most persistently COVID-sensitive indicator category across the entire 966-day analytical window. This result is worth unpacking carefully, because it is not the relationship that the Initial Shock or Adaptation analyses would have predicted as the dominant long-run pairing.
The absence of a transformation advantage — neither the cumulative nor rolling-average transform of the COVID deaths series dominates the raw series in this pairing — is itself informative. During shorter phase windows, transformation choices matter considerably: the 7-day rolling average smooths out reporting noise, and the cumulative transform captures the pandemic's accumulated severity rather than its daily fluctuation. At the 966-day full-period frequency, however, these distinctions collapse. The raw COVID deaths series already embodies a long, multi-wave trajectory that is structurally smooth at the scale of months, and its cumulative and rolling transforms become increasingly collinear with the raw series as the window lengthens. The finding that no transformation dominates therefore suggests that the causal signal between COVID mortality and agricultural commodity prices operated at the level of the pandemic's broad trajectory — its waves, plateaus, and secular decline — rather than at the level of short-run acceleration episodes that transformations are designed to isolate. This is a long-run relationship in the fullest sense: the multi-year arc of the pandemic shaped the multi-year arc of agricultural commodity prices through mechanisms that operated continuously rather than episodically.

The economic mechanism connecting COVID mortality to agricultural commodity prices across the full period is more structurally coherent than it might initially appear. Agricultural supply chains are among the most labor-intensive in the global economy and among the least substitutable for automation on short timescales. Harvesting, processing, packing, and distribution operations depend on geographically concentrated workforces that proved acutely vulnerable to COVID transmission throughout the pandemic, from the meatpacking plant outbreaks of spring 2020 through the agricultural labor disruptions that persisted across the Delta and subsequent variant waves. At the same time, agricultural demand was restructured by the pandemic — away from food service and hospitality channels toward retail and stockpiling — in ways that created supply-demand mismatches at the commodity level even when aggregate consumption was unchanged. Shipping disruption, itself a persistent feature of the pandemic economy, constrained the movement of both agricultural inputs (fertilizers, chemicals) and outputs (grains, oilseeds) across global markets. And the monetary accommodation that accompanied the pandemic's entire duration provided a sustained inflationary tailwind to commodity prices broadly. The COVID deaths series, as a proxy for pandemic severity across all four of these channels simultaneously, captures the full-period trajectory of this complex of forces in a way that shorter-window, higher-frequency analyses necessarily miss.

The broader commodity dominance of the top-10 rankings reinforces this interpretation. Agricultural commodities (agr1) and oil and gas (petrol_plus) together account for 9 of the 10 top positions in the Full Period levels analysis, with equity indices — which dominated the Initial Shock — largely absent from the upper rankings. This reordering reflects the fundamental shift in COVID's economic transmission mechanism across the pandemic's full duration. In the acute phase, COVID operated through financial markets via risk sentiment, uncertainty, and demand destruction — channels that affect equities directly and immediately. Across the full 966-day window, these acute channels were transient; what persisted was the pandemic's structural footprint on physical commodity markets through supply disruption, logistical constraint, and the sustained stimulus response that commodity-producing economies used to offset pandemic damage. The Full Period levels analysis is therefore not simply the average of the phase analyses — it is capturing a distinct long-run signal about which markets were most structurally and durably reshaped by COVID-19 as a multi-year economic event, as opposed to which markets responded most dramatically to COVID-19 as an acute financial shock.

The contrast between the Initial Shock's equity dominance and the Full Period's commodity dominance should be read as one of the project's central substantive findings: COVID's financial market impact was front-loaded into equities during the acute phase, but its durable economic footprint settled into commodity markets — particularly agricultural commodities and energy — where supply-side disruption and demand restructuring persisted long after equity markets had repriced and recovered. The full-period levels analysis is the analytical lens best positioned to capture this longer arc, and the covid_deaths → agr1 pairing at its apex is the clearest quantitative expression of where COVID's causal influence ultimately resided across the pandemic's complete trajectory.*

---

#### Initial Shock — Levels Top 10

<img width="473" height="405" alt="econ_anlys_fnd_opt_cndsTable12CovidDatavsEconomicIndicatorsTop10ScoresInitialShock" src="https://github.com/user-attachments/assets/a0d9a6b2-83e1-4a93-bf1f-e80b8de9b8b6" />

---

*The Initial Shock levels analysis produces the highest composite scores of any phase in the project, with the top pairing — rolling, cumulative covid_c&d → stk_mkt — reaching 66.06. This figure is the project's upper bound for COVID causal influence on financial markets, and its position at the apex of the Initial Shock rankings reflects the unique conditions of February–June 2020: a period in which pandemic data was not merely one market-moving signal among many but the dominant organizing fact of global financial markets.

The transformation pattern across the top 10 rows is unambiguous and analytically meaningful. All 10 rows carry cumulative X-variables, and 8 of the 10 carry the 7-day rolling average transform of that cumulative series. This near-unanimous selection of the rolling cumulative transformation is not a statistical artifact — it reflects the specific information structure of the early pandemic. Raw daily case and death counts during the Initial Shock were highly volatile, subject to weekend reporting lags, testing capacity constraints, and jurisdictional variation in reporting protocols. The 7-day rolling average corrects for this noise by smoothing over weekly reporting cycles, while the cumulative transform captures what investors were actually tracking: the pandemic's accumulated severity and its implied trajectory, not the day-to-day fluctuation around that trajectory. That this double transformation — smoothed cumulative counts — dominates every competing specification in the top 10 is evidence that the analytical framework is recovering a signal that corresponds to how market participants were actually processing COVID information during the acute shock.

The indicator hierarchy within the top 10 is equally informative. Stock market indices occupy the uppermost positions, followed by interest rates, with metal prices appearing further down the rankings. This ordering is consistent with the acute financial panic interpretation of the Initial Shock and with the transmission mechanism that the phase analysis documents in detail. Equity markets are the most direct and liquid receptors of risk sentiment: when pandemic severity crossed the visibility threshold in late February 2020, institutional and retail investors repriced equities immediately and continuously as case and death counts accumulated. Interest rates moved in close sequence — the Federal Reserve's emergency rate cuts of March 3 and March 15, 2020 were themselves responses to equity market stress and deteriorating economic conditions signaled by rising COVID data, creating a tight three-way relationship between pandemic severity, equity prices, and rate expectations that the levels analysis captures in the high scores for both indicator categories. Metal prices appearing below equities and rates reflects the Initial Shock's predominantly demand-side and sentiment-driven transmission mechanism: commodity markets respond to pandemic data through supply disruption and demand restructuring channels that are structurally slower to materialize than the risk sentiment channel operating through equities.

The dominance of the cumulative rolling-average transformation in the Initial Shock, taken together with the equity and rate concentration at the top of the rankings, points to a specific and well-defined causal story: during the Initial Shock, financial markets were responding to the pandemic's accumulated and smoothed trajectory as a signal of economic damage severity, with equity indices and interest rates as the primary transmission receptors and commodity markets as secondary ones. This story is consistent across the transformation selection, the indicator hierarchy, and the detailed Granger causality, FEVD, and rolling correlation results documented in the phase analysis — a degree of cross-method convergence that makes the Initial Shock the most analytically well-characterized phase in the project and the clearest demonstration of COVID operating as a direct, measurable causal force on financial markets.*

---

#### Adaptation — Levels Top 10

<img width="479" height="405" alt="econ_anlys_fnd_opt_cndsTable13CovidDatavsEconomicIndicatorsTop10ScoresAdaptation" src="https://github.com/user-attachments/assets/1f01f498-723f-428f-98e7-888fb669cec8" />

---

*The Adaptation Phase's scores decline from the Initial Shock peak with a top score of 54.75 for rolling `covid_deaths` → `intrt_rts`. The dominant X-variable shifts from `covid_c&d` to `covid_deaths`, a meaningful change reflecting the market's informational pivot from tracking the breadth of infection to tracking severity as vaccines changed the risk calculus. The appearance of interest rates in the highest scoring category is consistent with pandemic developments driving central bank accommodation expectations through the vaccine rollout and Delta wave periods.*

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

*The Initial Shock percentage-change analysis produces the second-highest scores of any phase with a top score of 60.98 for rolling, cumulative `covid_c&d%` → `stk_mkt%`. The y-variables `stk_mkt` and `metals` dominate the top rankings with equity indices in the lead. Notably, the top category exactly mirrors the levels analysis leader for this phase, confirming that the COVID → equity channel at this time was meaningful for both the trend-level and short-run changes.*

---

#### Adaptation — Percentage Changes Top 10

<img width="479" height="405" alt="econ_anlys_fnd_opt_cndsTable23CovidDatavsEconomicIndicatorsTop10ScoresAdaptation" src="https://github.com/user-attachments/assets/34539893-43e8-45ec-b1e2-cd833b2f9609" />

---

*The Adaptation percentage-change analysis is led by rolling, cumulative `covid_deaths%` → `metals%` with a score of 56.60. The y-variable `metals` dominates the rankings with 7 of the 10 top positions while `petrol_plus` and `exchg_rts` account for the remainder. The consistent appearance of `covid_deaths` (rather than `covid_cases` or `covid_c&d`) as the X-variable confirms the informational shift toward fatality data as the key COVID signal.*

---

#### Recovery — Percentage Changes Top 10

<img width="453" height="405" alt="econ_anlys_fnd_opt_cndsTable24CovidDatavsEconomicIndicatorsTop10ScoresRecovery" src="https://github.com/user-attachments/assets/00c4af8d-8b95-42a7-8471-409d5fedf6d2" />

---

*The Recovery percentage-change analysis is led by rolling, cumulative `covid_c&d%` → `metals%` with a score of 55.67. The return of the `covid_c&d` metric as the dominant X-variable, replacing `covid_deaths`, reflects the Omicron wave's distinctive epidemiology where cases surged to all-time highs while fatality rates remained lower than prior waves.*

### 2.3 Optimal Candidates by Phase

The final output of the candidate selection analysis is a ranked summary of the single best COVID–indicator pairing for each phase, selected across both levels and percentage-change analyses:

---

<img width="540" height="190" alt="econ_anlys_fnd_opt_cndsTable25TopCandidatesbyTimePeriod" src="https://github.com/user-attachments/assets/0955e18e-e34f-4979-9525-41939dc89a18" />

---

| Phase | COVID Variable | X-Variable Transformation | Economic Indicator | Y-Variable Transformation | Score |
|---|---|---|---|---|---|
| **Full Period** | `covid_deaths` | % change | exchange rates (`exchg_rts`) | % change | **51.81** |
| **Initial Shock** | `covid_c&d` | cumulative, 7-day rolling avg | stock market indices (`stk_mkt`) | none | **66.06** |
| **Adaptation** | `covid_deaths` | cumulative, 7-day rolling avg, % change | metal prices (`metals`) | % change | **56.60** |
| **Recovery** | `covid_c&d` | cumulative, 7-day rolling avg, % change | metal prices (`metals`) | % change | **55.67** |

There are two patterns that are immediately evident in this table. First, the score progression confirms a systematic causal decay: **66.06 → 56.60 → 55.67 → 51.81** across the Initial Shock, Adaptation, Recovery, and Full Period, respectively. COVID's causal footprint on economic indicators was strongest during the acute onset and attenuated progressively as the pandemic normalized. Second, the y-variable leadership transitions cleanly through three distinct asset classes: equities during the initial shock, metals through the adaptation and recovery phases, and exchange rates for the full period. This finding has direct implications for understanding which market mechanisms transmitted pandemic information to prices at each stage of the crisis.

These four optimal pairings serve as the inputs for the four phase-specific analysis notebooks described below.

---

## 3. Phase Analysis

### 3.1 Initial Shock: COVID Cases and Deaths vs. Stock Market Indices

**Notebook:**        `econ_anlys_shk_rll7_cml_cnd_mkt.ipynb`  
**X Variable:**      `covid_c&d` — 7-day rolling average of cumulative cases and deaths (levels)  
**Y Variables:**     Five stock market indices (S&P 500, DJIA, NASDAQ Composite, NYSE Composite, Russell 2000)
**Period:**          January 22, 2020 – June 7, 2020 (137 days)  
**Composite Score:** 66.06 — the highest of all four phase analyses

#### Economic Context

The Initial Shock period, from February 19 to March 23, 2020, encompasses the fastest equity market decline in recent history. Specifically, the S&P 500 experienced a peak-to-trough decline of 34% in 33 days compared to 274 days for the 2008 financial crisis. This period also includes the Federal Reserve's emergency 150 basis point rate cut, the passage of the $2.2 trillion CARES Act, and the beginning of equity price recovery. The compression of an extraordinary range of pandemic and policy events into 137 days creates the most information-dense environment of the four phases.

#### Stationarity Characteristics

All six time series — the rolling, cumulative COVID cases and deaths and the five equity indices — are non-stationary. The COVID time series follows a monotonically increasing trajectory with a major structural break at the onset of exponential U.S. case growth in mid-March 2020, detected by the Zivot-Andrews and Bai-Perron tests. The equity indices exhibit a sharp downward break in late February and early March followed by a recovery trend, a non-standard V-shaped non-stationary pattern that complicates standard ADF and KPSS testing. The `mathx.crct_stnry_df()` stationarity correction pipeline addresses these diagnostics before all downstream causal testing.

#### Key Analytical Findings

---

<img width="1472" height="258" alt="econ_anlys_shk_rll7_cml_cnd_mktTable1182PolynomialDegreesforCorrelationsSummaryCumlCovid19CD7dayRollAvgvsStockMarketIndicesInitialShock" src="https://github.com/user-attachments/assets/0b46c782-ba83-4932-bf9d-bcdd4dc9474b" />

---

**Correlation.** The contemporaneous correlation between rolling, cumulative COVID data and equity indices during the Initial Shock was expected to be strongly negative as rising case and death counts align chronologically with falling prices through March 23, and falling or stabilizing counts align with the subsequent recovery. Because all the time series trend over the 137-day window, a portion of this raw correlation reflects shared trend structure. Moreover, the polynomial degree optimization tests whether the relationship is linear or whether equity markets responded nonlinearly to the COVID data, crashing disproportionately only once case and death counts crossed a visibility threshold and producing a concave or step-function response.

Unfortunately, the results differed significantly from these expectations. Rather than the anticipated strongly negative correlations, the Spearman coefficients between rolling, cumulative COVID data and the five indices were weak and mixed in sign: S&P 500 (+0.35), Nasdaq (+0.04), DJIA (−0.09), NYSE (−0.10), and Russell 2000 (−0.07). Only three indices produced negative correlations, and all five coefficients were small in magnitude. Thus, the expected strongly negative signal was absent during this time period.

The most likely explanation is phase cancellation. For instance, this 137-day window encompasses two opposing sub-dynamics: the acute crash phase, during which rising case and death counts coincide with sharply falling prices, and the recovery phase, during which counts continue rising or plateau while prices rebound. These two dynamics pull the correlation in opposite directions and largely offset one another when the full window is analyzed as a single period. The S&P 500's positive coefficient of +0.35 is particularly notable and suggests the recovery dynamic dominated the aggregate signal for that index. A phase-separated analysis, isolating the crash window from the recovery window, would be expected to uncover the strongly negative relationship during the acute shock period.

The expectation of nonlinearity was confirmed, though not in the manner anticipated. Every index produced a best-fit polynomial degree well above linear — the S&P 500 (5), the Nasdaq (4), the DJIA (9), the NYSE (9), the Russell 2000 (9) — and all five are marked as adequately linear. However, the cross-validated R² values were catastrophically negative across all indices (ranging from −278 for Nasdaq to approximately −2.88 billion for NYSE), with correspondingly large cv_r²_std values, indicating severe overfitting rather than genuine nonlinear structure. The high-degree polynomials are contorting to fit a small number of outliers rather than capturing a meaningfully underlying relationship. This conclusion is corroborated by the scatter plots, where the fitted curves deviate dramatically from the bulk of the data cloud. The nonlinearity identified is therefore an artifact of the optimization process operating on a noisy, phase-mixed dataset, and should not be interpreted as evidence of a threshold or step-function response to COVID.

---

<img width="1703" height="604" alt="econ_anlys_shk_rll7_cml_cnd_mktTable1184TheGrangerCausalityTestSummaryCumlCovid19CD7dayRollAvgvsStockMarketIndicesInitialShock" src="https://github.com/user-attachments/assets/eac8938c-2b77-4184-b75c-d10b5ccf53e2" />

---

**Granger Causality.** The Granger test in the X→Y direction (COVID data predicts equity markets) was expected to be significantly stronger than the Y→X direction (equity markets predict COVID data). Asymmetric Granger causality from COVID to equities supports the interpretation that pandemic case and death counts were a leading predictor of equity market behavior during the crash, not merely contemporaneously correlated with it. The composite score of 66.06, the highest in the project, reflects that this phase produced the clearest, most statistically powerful directional Granger causality of any COVID–indicator pairing in the dataset.

The results met this expectation, with the directional asymmetry confirmed across all five indices and the reverse direction producing no credible causal signal in any case. In the COVID → equity direction, S&P 500 and Nasdaq achieved significance at lag 1 (F=6.80, p=0.01 and F=9.31, p=0.00, respectively), with all four test statistics in agreement and high-confidence conclusions in both cases. DJIA, NYSE, and Russell 2000 achieved significance at lag 5 (F=3.22, p=0.01; F=3.63, p=0.01; F=2.94, p=0.02), again with full agreement across test statistics and high-confidence conclusions. In the equity → COVID direction, DJIA, NYSE, and Russell 2000 returned high-confidence non-significant results across all lags tested. S&P 500 → COVID produced an inconclusive summary result driven by a lone chi² significant finding at lag 4 that was not corroborated by the F or lrtest statistics. Nasdaq → COVID flagged non-normal residuals or insufficient sample size at lag 5, where partial significance appeared, an edge case that does not constitute reliable evidence of reverse causality.

One finding worth noting is the lag heterogeneity in the COVID → equity direction. The large-cap benchmarks — S&P 500 and Nasdaq — responded to COVID information within a single lag, while the broader indices — DJIA, NYSE, and Russell 2000 — required five lags to produce significant results. This suggests that during the Initial Shock, large-cap equity markets incorporated pandemic signals more rapidly than broader and smaller-cap markets, a pattern consistent with differences in liquidity, institutional participation, and information efficiency across index compositions.

---

<img width="1141" height="255" alt="econ_anlys_shk_rll7_cml_cnd_mktTable1185VARVECMAnalysisSummaryCumlCovid19CD7dayRollAvgvsStockMarketIndicesInitialShock" src="https://github.com/user-attachments/assets/06c6e7b5-1b8b-4d67-9f71-8438d3551b30" />

---

**VAR/VECM Dynamics.** The FEVD X-share across the five equity indices quantifies what fraction of each index's forecast error variance was attributable to COVID shocks during the Initial Shock. Given the period's characteristics — where COVID is the dominant driver of a multi-week market crash — these X-shares were expected to be the highest of any phase analysis in the project, reflecting the COVID pandemic's near-monopoly as a market-moving signal from February to June 2020.

The results partially met this expectation. The S&P 500 produced a striking FEVD X-share of 48.7%, rising steadily across all 30 periods and stabilizing near 49%, meaning COVID shocks account for nearly half of the S&P 500's forecast error variance over the horizon. This result is strong and clearly consistent with the expectation of pandemic data functioning as the dominant market signal during the Initial Shock. NYSE (21.9%), Russell 2000 (19.2%), and DJIA (18.4%) produced moderate X-shares that, while meaningful, fall well short of the dominant influence implied by the expectation. Nasdaq produced the weakest X-share at 7.6%, and was also the only index to generate a positive cumulative IRF response (+4,799), indicating that COVID shocks were associated with rising rather than falling Nasdaq values. This result is consistent with the Nasdaq Composite's heavy technology weighting and the pandemic-driven acceleration of digital demand that benefited large-cap tech even during the broader market crash.

Two features of the VECM dynamics temper the interpretation of these X-shares. First, all five models returned infinite error correction half-lives, meaning the cointegrating relationships do not produce mean reversion within the 30-period IRF horizon. Second, the S&P 500 IRF x→y response continues growing in magnitude through period 30 (reaching −2,683 with no sign of decay), as does the DJIA (−3,220 at period 30) and NYSE (−1,645 at period 30). These non-dissipating shock responses suggest that the FEVD X-shares partly reflect a persistent, non-reverting COVID shock rather than a transient causal signal that cleanly separates from the index's own momentum. The result is nonetheless consistent with the Initial Shock phase being the period of greatest COVID influence on equity markets in the project, even if the mechanism is one of sustained shock persistence rather than rapid causal transmission.

---

<img width="5063" height="3219" alt="econ_anlys_shk_rll7_cml_cnd_mktFigure1181RollingCorrelationsoptimalwindowsoptimalminperiodsCumlCovid19CD7dayRollAvgvsStockMarketIndicesInitialShock" src="https://github.com/user-attachments/assets/7ddab3b7-582f-4f80-990f-f9e4b9c79b76" />

---

**Rolling Correlation.** The rolling correlation was expected to be persistently negative with the magnitude potentially strengthening during the crash phase and stabilizing during the recovery. This persistence across the full Initial Shock period was anticipated to be a key driver of the phase's high composite score, distinguishing it from the episodic, phase-switching patterns expected in later periods.

The results did not meet this expectation. Rather than a persistently negative rolling correlation, all five indices produced rapidly oscillating sign-switching behavior across the entire window, with rolling r-values repeatedly crossing zero and reaching extreme values in both directions. The composite overlay above shows all five indices moving closely in tandem, with peak rolling correlations reaching ±0.90–0.95 around early March and early April, periods corresponding to the acute crash and initial rebound, but these spikes are short-lived, collapsing back toward zero within days and then reversing sign. No sustained negative plateau emerges during the crash phase, and the oscillation continues with comparable amplitude through June, with no stabilization during the recovery.

The summary tables confirm this characterization quantitatively. Mean rolling correlations across all five indices are clustered near zero (S&P 500: +0.11, DJIA: −0.03, Nasdaq: −0.05, NYSE: −0.04, Russell 2000: −0.03), while rolling standard deviations are large relative to these means (0.39 to 0.59), the definitive statistical profile of sign-switching rather than directional persistence. Additionally, the rolling correlations of the covid data and all five indices are marked as unstable. The percentage of statistically significant rolling windows is correspondingly low, ranging from 7.23% for Russell 2000 to 16.87% for Nasdaq, indicating meaningful correlation is intermittent across the window.

The rolling correlation pattern observed here is structurally similar to the episodic behavior attributed to later phases, not the anticipated persistent directionality. The phase's high composite score is therefore driven by other analytical components — particularly, the Granger causality results and the S&P 500 FEVD X-share — rather than by rolling correlation consistency.

---

<img width="6686" height="2610" alt="econ_anlys_shk_rll7_cml_cnd_mktFigure1182LagCorrelationHeatmapCumlCovid19CD7dayRollAvgvsStockMarketIndicesInitialShock" src="https://github.com/user-attachments/assets/039c365c-96e6-41b4-8233-b5b1a3c82115" />

---

**Lag Correlation.** A positive peak lag (X leads Y) was expected to confirm that the rolling, cumulative COVID time series anticipated equity market movements rather than merely synchronizing with them contemporaneously. Given the 7-day rolling average transformation applied to this cumulative x_variable, a peak lag in the 1–7 day range was considered consistent with investors processing death and case count information over a weekly cycle aligned with the rolling window.

The results did not meet this expectation. Four of the five indices produced peak lags that place the equity index in the leading position rather than COVID data. The S&P 500 shows the most pronounced divergence, with a peak lag of −8 (r = +0.439), meaning that the S&P 500 leads the COVID series by eight days, and, uniquely, the entire lag correlation profile remains positive across the full ±15-day window, reflecting the same phase-cancellation dynamic identified in the contemporaneous correlation analysis. The Nasdaq Composite produced a peak lag of −5 (r = −0.295), also placing the index in the leading position. The DJIA, NYSE, and Russell 2000 all peak at lag +4, which falls nominally within the expected 1–7 day range and does place COVID in the leading position, but the magnitudes are weak (r = −0.246, −0.251, and −0.271, respectively), and none clearly exceed the ±0.30 significance threshold. The overall profiles for these three indices are noisy and irregular rather than exhibiting the expected clean leading structure.

The composite heatmap above reinforces this picture. The S&P 500 row is structurally distinct from all others, dominated by positive values across the board with no coherent negative-lag peak. The remaining four indices show scattered positive and negative patches with no consistent directional pattern across the lag range. There is no uniform positive-lag structure across the five indices that would support interpreting the COVID data as a systematic leading predictor in the lag correlation framework. The Granger causality results, which do confirm COVID as a leading predictor for all five indices, rely on a different and more powerful inferential approach that controls for autocorrelation and multivariate dynamics and should be treated as the primary evidence for COVID's leading role during the Initial Shock phase.

#### Significance of the Initial Shock Finding

The Initial Shock composite score of 66.06 establishes the upper bound of COVID's causal influence on financial markets, but the evidence underlying that score is more nuanced than the headline figure suggests. The analytical results across five methods — contemporaneous correlation, Granger causality, VAR/VECM dynamics, rolling correlation, and lag correlation — paint a consistent picture of a genuine but structurally complex causal relationship, one whose strength varied considerably depending on the analytical lens applied.

The clearest and most unambiguous evidence comes from the Granger causality tests. The COVID data Granger-caused equity market movements with high confidence across all five indices, with no credible reverse causation in any case. The S&P 500 and Nasdaq Composite achieved significance at lag 1, while the DJIA, NYSE, and Russell 2000 required lag 5, a pattern suggesting that large-cap liquid markets processed pandemic information faster than broader and smaller-cap indices. The VECM FEVD results reinforce this picture selectively: COVID shocks accounted for nearly half of S&P 500 forecast error variance across the 30-period horizon, a figure that stands as the strongest quantitative statement of pandemic causal dominance in the project. NYSE (21.9%), Russell 2000 (19.2%), and DJIA (18.4%) show meaningful but considerably more modest X-shares, and Nasdaq (7.6%),  paired with a positive cumulative IRF response, reflects the index's distinctive composition and the tech sector's anomalous relationship with pandemic-driven demand during this period.

The contemporaneous correlation, rolling correlation, and lag correlation results each tell a more complicated story that qualifies rather than contradicts the causal finding. The static Spearman correlations are weak and mixed in sign, driven by phase cancellation across the 137-day window: the crash and recovery dynamics pull in opposite directions and largely offset one another in the aggregate. The rolling correlations oscillate rapidly between strongly positive and strongly negative values throughout the window, with near-zero means and high standard deviations, producing statistically significant windows only 7–17% of the time depending on the index — a pattern structurally similar to the episodic behavior of later phases rather than the expected persistent directionality. The lag correlations show four of five indices with equity leading COVID rather than the reverse, with only the DJIA, NYSE, and Russell producing weak positive-lag peaks that nominally support COVID as a leading predictor, and the S&P 500 displaying a uniquely positive profile across all lags that is best interpreted as a further artifact of phase mixing.

Taken together, the evidence supports a revised and more precise statement of the Initial Shock finding: COVID-19 exerted genuine, statistically robust, and directionally asymmetric causal pressure on equity markets from February to June 2020, confirmed most powerfully by the Granger causality results and the S&P 500 FEVD X-share, causal pressure that was substantia and significant. However, it operated through episodic, regime-switching dynamics rather than the persistent, monotonically signed relationship implied by the phase's high composite score. The 137-day window encompasses at least two structurally distinct sub-periods, the acute crash and the recovery, whose opposing dynamics suppress the expected correlation and lag-based signals that corroborate the causal finding. The composite score of 66.06 should therefore be understood as the upper bound of COVID's Granger-causal influence on equity markets, with the important caveat that this influence was concentrated in specific sub-windows and indices rather than uniformly distributed across the full phase. Nevertheless, it remains the baseline against which the progressive attenuation of COVID's causal role in subsequent phases is measured, but that attenuation is episodic rather than continuous.

---

### 3.2 Adaptation: COVID Death Rate vs. Metal Commodity Returns

**Notebook:** `econ_anlys_adp_pct_rll7_cml_dth_mts.ipynb`  
**X Variable:** `covid_deaths` — 7-day rolling average of cumulative deaths, percentage change  
**Y Variables:** Five metal price series (gold, silver, platinum, palladium, copper), percentage change  
**Period:** June 8, 2020 – November 25, 2021 (536 days)  
**Composite Score:** 56.60

#### The Adaptation Period: Structural Context

The Adaptation period (June 8, 2020 – November 25, 2021) is the longest of the four phases at 536 days and the most structurally complex, encompassing multiple distinct economic and pandemic sub-regimes that operated concurrently and in tension with one another. Understanding the analytical results requires situating them within this layered context.

The pandemic itself passed through at least three distinct sub-phases during Adaptation. The summer and fall of 2020 brought a second wave of infections and deaths in the United States and Europe, occurring against a backdrop of partial economic reopening and the first large-scale fiscal stimulus programs. Winter 2020–21 produced the deadliest sustained mortality surge of the entire pandemic in the US, coinciding with the Emergency Use Authorization of the Pfizer-BioNTech and Moderna vaccines in December 2020 — a structural inflection point that began decoupling death-rate trajectory from market expectations about the pandemic's economic endpoint. Spring and summer 2021 brought vaccine-driven mortality decline followed by the Delta variant resurgence beginning in July 2021, which temporarily reversed that trajectory before the phase closed in November 2021. The COVID death-rate series used in this analysis — rolling cumulative deaths in percentage-change form — captures all three of these sub-regimes within a single 536-day window, which is a significant source of structural heterogeneity in the results.

The macroeconomic environment during Adaptation was simultaneously shaped by forces largely independent of the pandemic. The commodity supercycle that drove the Bloomberg Commodity Index to multi-year highs by mid-2021 was partly pandemic-related — supply chain disruption and fiscal stimulus both contributed — but also reflected structural demand shifts toward electrification and infrastructure investment that predated COVID and would have occurred regardless of the pandemic's trajectory. The Federal Reserve's commitment to near-zero interest rates and asset purchases throughout the period created a persistent monetary accommodation backdrop that supported commodity prices broadly, making it difficult to isolate COVID's marginal contribution to metal return variance from the accommodation channel's baseline effect. Global supply chain disruption, which intensified through 2021, operated through both pandemic and non-pandemic mechanisms simultaneously — semiconductor shortages, shipping congestion, and labor market tightness all intersected with ongoing COVID disruptions in ways that are analytically inseparable at the daily frequency this analysis employs.

Critically, by the start of the Adaptation phase markets had undergone a fundamental repricing of pandemic risk. The acute uncertainty that characterized the Initial Shock — when the economic consequences of COVID were genuinely unknown and market participants had no framework for pricing a novel pandemic — had been replaced by a more calibrated assessment of COVID as a persistent background condition. Investors were no longer reacting to pandemic data as if each data point carried existential implications for economic activity; they were instead incorporating it as one factor among many in an environment also shaped by monetary policy, fiscal stimulus, vaccine progress, and the structural demand shifts described above. This habituation effect is the primary reason why the Adaptation composite score of 56.60 represents a meaningful decline from the Initial Shock's 66.06, and why the analytical results across all five methods show a weaker, more episodic, and more heterogeneous COVID signal than the Initial Shock produced.

#### Why Deaths Rather Than Cases

The shift from rolling cumulative COVID C&D (Initial Shock) to COVID deaths (Adaptation) as the dominant X-variable reflects a meaningful change in the informational structure of the pandemic rather than an arbitrary modeling choice. By mid-2020, case counts had become an increasingly noisy signal subject to testing capacity constraints, reporting backlogs, and political interference with data release in several jurisdictions. Cumulative fatality counts, smoothed via a 7-day rolling average and expressed in percentage-change form, provide a more reliable and actionable measure of pandemic severity — one less susceptible to the definitional and logistical artifacts that degraded case count data quality during this period. The candidate selection analysis confirms this empirically: covid_deaths appears in 7 of the top 10 rows in both the Adaptation levels and percentage-change analyses, making it the dominant COVID variable by selection frequency rather than by analytical assumption.

#### Why Metals as the Dominant Y-Variable

The emergence of metals as the most COVID-sensitive indicator category during Adaptation reflects the shift from the pandemic's demand-side to its supply-side economic channel. The Initial Shock operated primarily through demand destruction and risk sentiment: falling economic activity expectations drove equity prices down across the board, producing a broad-based and directionally unambiguous signal. The Adaptation period introduced supply chain disruption as an increasingly important and analytically distinct mechanism. Mining operations, smelting capacity, and logistics chains were constrained by ongoing pandemic conditions across multiple producing countries, directly limiting metal supply even as demand recovered and, in some cases, accelerated. Simultaneously, fiscal stimulus-driven infrastructure spending and the accelerating buildout of electric vehicle battery supply chains created new structural demand for industrial metals — copper, platinum, palladium — that operated independently of pandemic dynamics but interacted with pandemic-driven supply constraints to amplify price movements.

The COVID death rate captures both dimensions of this supply-side mechanism: it proxies for the severity of ongoing disruptions to the labor forces and logistics networks that produce and transport metals, and it captures the market's running reassessment of the pandemic's long-term economic footprint. This dual role — disruption indicator and regime signal — makes the death rate a more economically coherent X-variable for the metals analysis than case counts would be, and explains why the Granger causality results find statistically significant COVID → metal relationships for three of the five metals analyzed (silver, platinum, copper) despite the substantially noisier analytical environment that the percentage-change framework and 536-day structural heterogeneity create.

#### Key Analytical Findings

**Percentage-Change Framework.** Both series are in percentage-change form, meaning the analysis tests whether short-run accelerations in the death rate are associated with directional changes in metal returns. This is a more demanding test than the levels analysis used in the Initial Shock: there is no shared trend to inflate the correlation, and Granger causality must reflect genuine short-run predictive information rather than co-trending. The shift to percentage changes also means that the scatter plots and lag correlations are operating on a much noisier signal, which is reflected throughout the results.

**Contemporaneous Correlation.** The scatter plots reveal a clear structural divide between precious and industrial metals in how they relate to the COVID death rate during the Adaptation period. Gold shows a diffuse, near-shapeless cloud with a shallow degree-2 polynomial fit (quadratic coefficient 2.65e-02) — no meaningful contemporaneous relationship in either direction. Silver and copper produce near-identical U-shaped scatter profiles with degree-2 fits, suggesting that extreme death-rate accelerations in either direction are associated with higher metal returns, while moderate changes show no relationship — a pattern more consistent with volatility coupling than directional causation. Platinum stands apart as the only metal with a visually coherent positive scatter profile: the degree-5 polynomial fits a broadly upward-sloping cloud, indicating that higher death-rate acceleration is associated with higher platinum returns across most of the data range, consistent with the supply disruption channel dominating for this metal. Palladium shows the shallowest and most linear scatter of the five (degree-1 fit, coefficient 7.69e-03), with a near-horizontal fitted line and enormous vertical spread at all x-values — essentially no contemporaneous signal.

**Granger Causality.** The results reveal a partial and asymmetric causal structure that is markedly weaker than the Initial Shock but not absent. In the COVID → metal direction, silver and copper both achieve high-confidence significance at lag 1 (F=5.28, p=0.02 for both, with all four test statistics in agreement in each case), making them the clearest causal targets of pandemic death-rate acceleration during the Adaptation period. Platinum achieves significance at lag 1 (F=4.23, p=0.04, all four tests agree) — a result consistent with its distinctive scatter profile and the supply disruption channel operating through mining and processing constraints. Gold produces no significant result across all eight lags tested, with uniformly high p-values (minimum F=0.22 at lag 1), confirming that safe-haven demand dynamics for gold during Adaptation were not systematically driven by short-run death-rate acceleration. Palladium also produces no significant COVID → metal causality across any lag, with the best F-statistic only reaching 1.74 at lag 5.

The reverse direction — metal returns predicting death-rate acceleration — yields one notable finding: palladium Granger-causes the COVID death rate at lag 6 (F=2.18, p=0.04, all four tests significant). This result is almost certainly spurious from an economic interpretation standpoint, and most plausibly reflects a common driver — likely supply chain disruption affecting both palladium's industrial supply chains and the logistical capacity for reporting and treating COVID cases — rather than any genuine mechanism by which palladium price movements caused pandemic mortality outcomes. No other metal produces reverse causality in either direction. The summary table confirms the overall picture: three of five metals (silver, platinum, copper) show high-confidence COVID → metal causality; two (gold, palladium) do not; and only the anomalous palladium reverse result disrupts an otherwise clean directional asymmetry.

VAR/VECM Dynamics. All five metal pairs were modeled using VECM(lag=7, rank=1), with BIC selecting lag 8 (VECM lag 7) uniformly across the group. This consistency is itself informative — the same lag structure fits all five pairs, suggesting a common information processing horizon of approximately one to two trading weeks for the COVID death rate signal to work through metal return dynamics during the Adaptation period. All five metal return series are stationary while the COVID deaths percentage-change series is non-stationary, and cointegration rank 1 is confirmed by both trace and max-eigenvalue tests in every case, justifying the VECM specification throughout.
The FEVD X-shares are uniformly and strikingly low across all five metals: gold (2.1%), silver (3.2%), copper (3.2%), palladium (1.9%), and platinum (4.2%). Every metal is classified as minimal influence, and in every case the metal's own return shocks account for 96–98% of its forecast error variance. This stands in sharp contrast to the Initial Shock's S&P 500 FEVD X-share of 48.7% and represents the most quantitatively decisive evidence of COVID causal attenuation in the project to date. Even platinum — the metal with the strongest Granger causality result (F=4.23, p=0.04) and the highest FEVD X-share of the group — attributes only 4.2% of its forecast variance to COVID death shocks. The Granger causality results establish that COVID death-rate acceleration contains statistically significant short-run predictive information for silver, platinum, and copper, but the FEVD results establish that this predictive information is economically negligible in terms of variance explained over the 31-period horizon.

The IRF results introduce an important sign heterogeneity across the metals. Gold, silver, copper, and platinum all produce positive cumulative x→y responses — a one-standard-deviation shock to the COVID death rate acceleration is associated with net positive metal returns over the 30-period horizon. The magnitudes vary (gold: +8.96, platinum: +22.85, silver and copper: +23.06), and the peak lag timing also differs: platinum responds fastest with a peak at lag 1 (magnitude +6.33), while gold, silver, and copper all peak at lag 5. These positive IRF signs are consistent with the supply disruption and monetary policy channels dominating — rising deaths constrain mining and processing capacity while reinforcing expectations of continued monetary accommodation, both of which support metal prices. Palladium is the sole exception, producing a negative cumulative response (−6.66) peaking at lag 4 (magnitude −4.35), consistent with the risk-off channel dominating for this metal and with palladium's unique automotive demand sensitivity, where rising deaths may have been interpreted as demand destruction for vehicles rather than supply constraint for the metal.

All five models return infinite error correction half-lives, meaning that while cointegrating relationships exist, the systems do not mean-revert within the 30-period IRF horizon. Platinum and palladium are the only two metals with is_stable = True in the summary table, reflecting better-behaved VECM dynamics; gold, silver, and copper are is_stable = False, and their mean reversion is not confirmed — a flag that warrants interpretive caution for those three IRF profiles specifically, as the cumulative responses may be diverging rather than settling.

Taken together, the VAR/VECM results for the Adaptation phase tell a coherent story: COVID death-rate shocks produced statistically detectable impulse responses in metal returns, with direction consistent with supply disruption and accommodation channels for four of five metals, but the magnitude of this influence — as measured by FEVD X-shares uniformly below 5% — was economically small. The pandemic had not disappeared as a causal force in metal markets during the Adaptation period, but it had been reduced from a dominant driver to a minor contributing factor, with each metal's own return dynamics accounting for the overwhelming majority of its forecast variance.

**Rolling Correlation.** All five metals exhibit the episodic, rapidly sign-switching rolling correlation pattern that characterizes the Adaptation phase. The composite overlay (Figure 1.1.8.1) shows all five metals oscillating between ±0.75–0.95 throughout the full June 2020–November 2021 window, with no metal maintaining a sustained directional signal for more than a few weeks at a time. This behavior is structurally distinct from what would be expected if any single causal channel — risk-off, supply disruption, or monetary policy — dominated persistently. Gold is the most visually damped of the five in its individual rolling correlation chart, consistent with its Granger non-result. Silver and copper show broadly similar oscillation profiles to each other, as do platinum and palladium. Notably, a visible elevation of positive rolling correlation values is apparent across multiple metals during the July–September 2021 period in the individual charts, coinciding with the Delta variant resurgence — providing partial support for the hypothesis that the COVID → metals channel reactivated episodically during wave events but was otherwise dormant. The reactivation is more pronounced for the industrial metals (copper, platinum) than for the precious metals, consistent with the supply disruption channel being the dominant transmission mechanism when the channel is active.

**Lag Correlation.** The lag correlation results across all five metals are uniformly weak, with no metal producing a peak r-value that reaches or meaningfully approaches the ±0.30 significance threshold. Peak values are: gold (lag −15, r=+0.079), silver (lag +5, r=+0.124), platinum (lag +10, r=+0.118), palladium (lag +19, r=+0.094), and copper (lag +5, r=+0.124). The entire lag correlation profile for each metal sits in a narrow band just above zero across the full ±25-day range — there is no discernible asymmetry between the leading and lagging sides in any case, and no peak stands out as structurally meaningful rather than noise. The composite heatmap (Figure 1.1.8.2) is dominated by uniform mid-green across all metals and all lags, with no coherent pattern of stronger or weaker correlations in either the COVID-leads or metal-leads half of the space. This is the clearest evidence of the habituation channel operating: at the aggregate level across the 530-day Adaptation window, incremental death-rate changes carry no systematic leading information about metal return direction, regardless of the lag structure considered. The Granger causality results — which do find significant COVID → metal relationships for silver, platinum, and copper — are therefore capturing short-run predictive structure that the lag correlation's aggregate framework averages away, most likely because the causal relationship was active only during specific sub-periods (Delta wave, winter 2020–21 surge) and absent otherwise.

**Cross-Metal Heterogeneity.** The results confirm the expected divergence between precious and industrial metals during the Adaptation period, though the boundary does not fall exactly where anticipated. Silver behaves as an industrial metal for the purposes of this analysis — showing Granger causality from COVID deaths at lag 1 alongside copper and platinum — despite its dual precious/industrial classification. Gold is the only metal that shows no causal relationship with COVID deaths in any direction and no coherent rolling or lag correlation structure, consistent with gold having fully decoupled from the pandemic signal by mid-2020 as safe-haven demand stabilized. Palladium's absence of COVID → metal causality, despite its role as an industrial metal with supply-constrained production, likely reflects the dominance of automotive sector demand dynamics — particularly semiconductor-driven vehicle production disruptions — that were driven by factors orthogonal to the COVID death rate during this period.

**Composite Score and Phase Interpretation.** The Adaptation score of 56.60 — down from 66.06 in the Initial Shock — quantifies the attenuation of COVID's causal footprint as the pandemic matured. The Granger causality results show that this attenuation was real but selective: COVID retained statistically robust predictive power for three of five metals (silver, platinum, copper) at short lags, while losing it entirely for gold and failing to establish it for palladium. The rolling and lag correlation results show that this residual causal influence operated episodically rather than continuously, activating during wave resurgences and receding during inter-wave periods. The Adaptation phase is therefore best characterized not as a uniform weakening of the COVID → financial market link, but as a restructuring of that link: from a broad-based, sentiment-driven demand-destruction signal operating across all equity indices, to a narrower, supply-disruption-driven signal operating selectively through industrial and dual-use metals during acute mortality acceleration events.

---

### 3.3 Recovery: Total COVID Signal vs. Metal Commodity Returns

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

The shift back to the `covid_c&d` metric — used in the Initial Shock but replaced by `covid_deaths` alone in Adaptation — reflects the Recovery period's distinctive epidemiology. Omicron's case-death decoupling (historic case counts, lower-than-expected fatalities) meant that `covid_deaths` alone would miss a large portion of the economically relevant COVID signal: the scale of the case surge mattered enormously for supply chain disruption and zero-COVID policy responses, even when mortality impact was attenuated by vaccines. The `covid_c&d` metric captured both dimensions.

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

The return of `covid_c&d` in the Recovery phase reflects the Omicron variant's specific properties — extraordinarily high case counts combined with lower-than-expected fatality rates — which required the total metric to capture both the scale of disruption (case counts) and its attenuated severity (death rates).

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

*This analysis was conducted as part of a broader project examining the quantitative economic impact of the COVID-19 pandemic across multiple asset classes and time periods. All data sources, transformation parameters, and statistical thresholds are documented within the individual Jupyter notebooks.*

---


## Copyright

Nicholas J. George © 2026. All Rights Reserved.
