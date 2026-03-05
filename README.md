![oil_sector](https://github.com/njgeorge000158/Oil-Energy-Sector-Analysis-During-the-COVID-19-Pandemic/assets/137228821/ef7762de-3193-4cfb-aa40-899e9fe069a7)

-----

# **The Oil & Gas Energy Sector and the Covid-19 Pandemic: A Multi-Variable Economic Analysis (2020–2022)**

-----

## **Introduction**

The Oil & Gas Energy Sector occupies a unique position in the global economy. As a commodity that virtually every individual, business, and nation depends upon — directly or indirectly — oil is uniquely sensitive to disruption. When unexpected shocks occur, their consequences ripple outward far beyond the energy markets themselves, touching daily life at every level. This project investigates the sector's behavior during one of the most consequential such disruptions in modern history: the Covid-19 pandemic. Specifically, we set out to answer three questions:

- How strong is the relationship between oil company share prices and the price of crude oil?
- Is there a measurable relationship between daily Covid-19 case and death counts and the prices of crude oil or oil company equities?
- If Covid-19 metrics show no significant relationship with these prices, do other economic indicators in the study?

## **Data Assembly and Sample Space**

Assembling a dataset sufficient to produce statistically valid results proved more challenging than anticipated, as the usable sample space contracted considerably through the course of data preparation. The intended analysis window — January 1, 2020, through December 31, 2022 — represented 1,095 calendar days. The New Year's Day holiday reduced this to 1,092 trading days. Excluding weekends, market holidays, and other non-trading days further reduced the count to 755 days. Finally, an inspection of World Health Organization (WHO) API data revealed that Covid-19 reporting did not begin until January 3, 2020, and transitioned from daily to weekly figures after October 16, 2022 — constraints that reduced the final sample to 702 comparable data points, spanning January 3, 2020, through October 14, 2022.

Each reduction represented a deliberate trade-off between sample size and dataset integrity. Fewer observations reduce statistical power, but incompatible datasets introduce far more damaging distortions. We made every effort to strike the most defensible balance between these competing considerations.

Data was sourced from two primary APIs. The WHO provided a comprehensive global Covid-19 dataset, which we filtered to the appropriate country, categories, and date range. Yahoo Finance supplied daily closing prices for crude oil, the S&P 500, gold, and U.S. Treasury 10-Year Bond Yields.

## **Constructing the Oil & Gas Energy Sector Index**

With the dataset assembled, we faced a methodological challenge: how best to construct a benchmark that accurately represents Oil & Gas Energy Sector equities. The guiding question became, "What most accurately reflects a company's value at any given point in time?" The answer lies in the Efficient Market Hypothesis, which holds that share prices incorporate all available information — making market capitalization, the product of share price and total shares outstanding, the most appropriate measure of a company's value.

To identify all publicly traded oil companies, we downloaded over 11,000 tickers from the Yahoo Finance API and used a Python script to isolate those belonging to oil companies whose shares were trading prior to the analysis window. For each qualifying company, we calculated minimum, maximum, mean, median, variance, standard deviation, and standard error of the mean (SEM) market capitalization values.

Side-by-side pie charts comparing the sector's industry breakdown by company count, mean market capitalization, and median market capitalization revealed a notable pattern: while industry percentages were broadly similar across mean and median measures, Oil & Gas Integrated claimed the largest share of both despite having among the fewest companies. This prompted deeper statistical scrutiny.

A more rigorous analysis of mean and median market capitalizations by industry confirmed the same pattern across all groups: substantial divergences between mean and median values, consistently small standard deviations except within Oil & Gas Integrated, a significant number of outliers, and heavily left-skewed distributions. Under normal conditions, the mean is the preferred measure of central tendency — but in the presence of skewed distributions and extreme values, it becomes an unreliable summary statistic. The median, being resistant to outlier influence, is the more appropriate and informative measure in this context, particularly given that real-world financial data tends to be dynamic and asymmetrical. Accordingly, we adopted median market capitalization as the basis for index construction.

We constructed two portfolio-based indices to represent the sector. The first incorporated all qualifying oil companies; the second included only the six companies with the highest median market capitalization within each of the six oil industry sub-sectors: ConocoPhillips (Oil & Gas Exploration & Production), Enbridge Inc. (Oil & Gas Midstream), Marathon Petroleum Corporation (Oil & Gas Refining & Marketing), Precision Drilling Corporation (Oil & Gas Drilling), Shell plc (Oil & Gas Integrated), and Schlumberger Limited (Oil & Gas Equipment & Services). For both indices, each company's index weight was calculated as its median market capitalization divided by the portfolio's total median market capitalization, and the daily index price was computed as the weighted sum of each company's closing share price.

Comparing the two indices against the S&P 500 informed our final selection. The top-company index showed a slightly lower correlation with the S&P 500 (0.598) than the all-company index (0.631), making it preferable for our purposes: lower systematic risk and correspondingly greater portfolio-specific risk produce a more differentiated and analytically useful model. Combined with the top-company index's significantly reduced computational demands and its near-perfect linear correlation with the all-company index (0.987), we selected it as our primary benchmark — designated the Oil Energy Sector (Top) Index.

## **Findings**

The analysis yielded clear and, in some respects, surprising answers to our three guiding questions.

At the level of price, the relationship between oil company equities and crude oil is very strong, evidenced by a linear correlation of 0.926. The Oil Energy Sector (Top) Index also exhibits meaningful correlations with broader economic indicators: a quadratic correlation of 0.738 with the S&P 500 and a notably stronger quadratic correlation of 0.923 with U.S. Treasury 10-Year Bond Yields. Gold, by contrast, proved the most insulated of all metrics studied, showing little meaningful relationship with any other variable in the analysis.

Perhaps the most striking finding is the complete absence of any detectable relationship between Covid-19 metrics — whether case counts or death tolls — and the price levels of crude oil, oil company equities, or any other economic indicator in the study. The pandemic's daily numbers, regardless of their magnitude, had no discernible effect on economic price levels throughout the analysis period.

What the pandemic did produce, however, was a sharp and immediate market reaction at its onset. In March 2020, prices across virtually all metrics suffered a sudden and precipitous decline. This was accompanied by a dramatic surge in volatility across all economic benchmarks — a pattern that persisted at reduced but elevated levels through the remainder of the period, with one notable exception: crude oil prices returned to normal volatility levels after the initial spike, rather than sustaining the elevated volatility observed elsewhere.

## **Conclusion**

The Covid-19 pandemic delivered an immediate and severe shock to the Oil & Gas Energy Sector and the broader economy — cratering prices and igniting volatility across markets at its onset in March 2020. Yet despite the scale of the disruption, the ongoing progression of the pandemic itself — as measured by daily case and death counts — bore no statistically meaningful relationship to economic price levels at any point in the study. The market reacted to the pandemic's arrival, not to its evolution. Prices eventually recovered, volatility gradually subsided, and the sector's strongest and most consistent driver remained what it had always been: the price of crude oil, to which oil company equities are tightly and reliably bound.

----

## Copyright

Nicholas J. George © 2023. All Rights Reserved.
