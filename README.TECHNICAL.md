# **Project 1, Oil Energy Sector Analysis**

----

### **Installation:**

----

If the computer has Anaconda, Jupyter Notebook, and a recent version of Python, the IPython notebook already has the following dependencies installed: datetime, io, json, matplotlib, numpy, pandas, pathlib, os, pandas, requests, requests_html, scipy.

In addition to those modules, the IPython notebook needs the following to execute: yfinance, yahoo_fin, holoviews, hvplot, geoviews, geopy, aspose-words, dataframe-image.

Here are the requisite Terminal commands for the installation of these peripheral modules:

pip3 install -U yfinance

pip3 install -U yahoo_fin

pip3 install -U holoviews

pip3 install -U hvplot

pip3 install -U geoviews

pip3 install -U geopy

pip3 install -U aspose-words

pip3 install -U dataframe-image

----

### **Usage:**

----

The IPython notebook, oil_energy_sector.ipynb, requires the following Python scripts with it in the same folder:

logx.py

mathx.py

matplotlibx.py

oil_energy_sector_config.py

oil_energy_sectorx_constants.py

oil_energy_sectorx.py

pandasx.py

timex.py

If the folders, logs and images, are not present, the IPython notebook will create them.  If the CSV file, oil_companies.csv, is not present in the folder, resources, the program will use APIs to generate the CSV file.  Without the CSV file, execution time is an hour; with it, execution time is approximately 1.5 minutes.

To place the IPython notebook in Log Mode or Image Mode set the parameter for the appropriate subroutine in coding cell #2 to True. In Log Mode, it writes that information to the log file in the folder, logs. If the program is in Image Mode, the notebook writes all dataframes, hvplot maps, and matplotlib plots to PNG files in the folder, images.

----

### **Resource Summary:**

----

#### Source code

oil_energy_sector.ipynb, logx.py, mathx.py, matplotlibx.py, oil_energy_sector_config.py, oil_energy_sectorx_constants.py, oil_energy_sectorx.py, pandasx.py, timex.py

#### Input files

oil_companies.csv

#### Output files

oil_companies.csv

#### SQL script

n/a

#### Software

Jupyter Notebook, Matplotlib, Numpy, Pandas, Python 3.11.5

![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

----

### **GitHub Repository Branches:**

----

#### main branch 

|&rarr; [./oil_energy_sector.ipynb](./oil_energy_sector.ipynb)

|&rarr; [./oil_energy_sectorx_constants.py](./oil_energy_sectorx_constants.py)

|&rarr; [./oil_energy_sectorx.py](./oil_energy_sectorx.py)

|&rarr; [./README.TECHNICAL.md](./README.TECHNICAL.md)

|&rarr; [./README.md](./README.md)

|&rarr; [./table-of-contents.md](./table-of-contents.md)

|&rarr; [./images/](./images/)

  &emsp; |&rarr; [./images/oil_energy_sectorFigure111EconomicIndicatorPricesvsAnalysisPeriod.png](./images/oil_energy_sectorFigure111EconomicIndicatorPricesvsAnalysisPeriod.png)
  
  &emsp; |&rarr; [./images/oil_energy_sectorFigure112EconomicIndicatorPriceChangesvsAnalysisPeriod.png](./images/oil_energy_sectorFigure112EconomicIndicatorPriceChangesvsAnalysisPeriod.png)
  
  &emsp; |&rarr; [./images/oil_energy_sectorFigure121COVID19NewCasesandNewDeathsvsAnalysisPeriodUSA.png](./images/oil_energy_sectorFigure121COVID19NewCasesandNewDeathsvsAnalysisPeriodUSA.png)
  
  &emsp; |&rarr; [./images/oil_energy_sectorFigure122COVID19NewCasesvsNewDeathsScatterPlotwRegression.png](./images/oil_energy_sectorFigure122COVID19NewCasesvsNewDeathsScatterPlotwRegression.png)
  
  &emsp; |&rarr; [./images/oil_energy_sectorFigure123COVID19NewCasesandNewDeathsChangevsAnalysisPeriodUSA.png](./images/oil_energy_sectorFigure123COVID19NewCasesandNewDeathsChangevsAnalysisPeriodUSAd.png)
  
  &emsp; |&rarr; [./images/oil_energy_sectorFigure124COVID19NewCasesvsNewDeathsScatterPlotwRegression.png](./images/oil_energy_sectorFigure124COVID19NewCasesvsNewDeathsScatterPlotwRegression.png)
  
  &emsp; |&rarr; [./images/oil_energy_sectorFigure211OilIndustrySharefromNumberofCompanies.png](./images/oil_energy_sectorFigure211OilIndustrySharefromNumberofCompanies.png)
  
  &emsp; |&rarr; [./images/oil_energy_sectorFigure212OilIndustrySharefromMarketCapitalizationMean.png](./images/oil_energy_sectorFigure212OilIndustrySharefromMarketCapitalizationMean.png)

  &emsp; |&rarr; [./images/oil_energy_sectorFigure213OilIndustrySharefromMarketCapitalizationMedian.png](./images/oil_energy_sectorFigure213OilIndustrySharefromMarketCapitalizationMedian.png)
  
  &emsp; |&rarr; [./images/oil_energy_sectorFigure214CompanyCountvsMarketCapMean.png](./images/oil_energy_sectorFigure214CompanyCountvsMarketCapMean.png)

  &emsp; |&rarr; [./images/oil_energy_sectorFigure215MarketCapMeanvsMarketCapMedian.png](./images/oil_energy_sectorFigure215MarketCapMeanvsMarketCapMedian.png)

  &emsp; |&rarr; [./images/oil_energy_sectorFigure221MarketCapitalizationMeanStatisticsbyOilIndustry.png](./images/oil_energy_sectorFigure221MarketCapitalizationMeanStatisticsbyOilIndustry.png)

  &emsp; |&rarr; [./images/oil_energy_sectorFigure231MarketCapitalizationMedianStatisticsbyOilIndustry.png](./images/oil_energy_sectorFigure231MarketCapitalizationMedianStatisticsbyOilIndustry.png)

  &emsp; |&rarr; [./images/oil_energy_sectorFigure241MarketCapitalizationStandardDeviationStatisticsbyOilIndustry.png](./images/oil_energy_sectorFigure241MarketCapitalizationStandardDeviationStatisticsbyOilIndustry.png)

  &emsp; |&rarr; [./images/oil_energy_sectorFigure242MarketCapitalizationSEMStatisticsbyOilIndustry.png](./images/oil_energy_sectorFigure242MarketCapitalizationSEMStatisticsbyOilIndustry.png)

  &emsp; |&rarr; [./images/oil_energy_sectorFigure251CompanyCountvsMarketCapitalizationHistograms.png](./images/oil_energy_sectorFigure251CompanyCountvsMarketCapitalizationHistograms.png)

  &emsp; |&rarr; [./images/oil_energy_sectorFigure311OESIndexAll.png](./images/oil_energy_sectorFigure311OESIndexAll.png)

  &emsp; |&rarr; [./images/oil_energy_sectorFigure311OESIndexAllChange.png](./images/oil_energy_sectorFigure311OESIndexAllChange.png)

  &emsp; |&rarr; [./images/oil_energy_sectorFigure331OESTopIndex.png](./images/oil_energy_sectorFigure331OESTopIndex.png)

  &emsp; |&rarr; [./images/oil_energy_sectorFigure332OESTopIndexChange.png](./images/oil_energy_sectorFigure332OESTopIndexChange.png)

  &emsp; |&rarr; [./images/oil_energy_sectorFigure341AllCompaniesWorldMap.html](./images/oil_energy_sectorFigure341AllCompaniesWorldMap.html)

  &emsp; |&rarr; [./images/oil_energy_sectorFigure342AllCompaniesAmericasandEuropeMap.html](./images/oil_energy_sectorFigure342AllCompaniesAmericasandEuropeMap.html)

  &emsp; |&rarr; [./images/oil_energy_sectorFigure343TopCompaniesWorldMap.html](./images/oil_energy_sectorFigure343TopCompaniesWorldMap.html)

  &emsp; |&rarr; [./images/oil_energy_sectorFigure344TopCompaniesAmericasandEuropeMap.html](./images/oil_energy_sectorFigure344TopCompaniesAmericasandEuropeMap.html)

  &emsp; |&rarr; [./images/oil_energy_sectorFigure345OESTopIndexandOESAllIndex.png](./images/oil_energy_sectorFigure345OESTopIndexandOESAllIndex.png)

  &emsp; |&rarr; [./images/oil_energy_sectorFigure346OESAllIndexvsOESTopIndexScatterPlotwRegression.png](./images/oil_energy_sectorFigure346OESAllIndexvsOESTopIndexScatterPlotwRegression.png)

  &emsp; |&rarr; [./images/oil_energy_sectorFigure347OESTopIndexandOESAllIndexChange.png](./images/oil_energy_sectorFigure347OESTopIndexandOESAllIndexChange.png)

  &emsp; |&rarr; [./images/oil_energy_sectorFigure348OESTopIndexandOESAllIndexChange.png](./images/oil_energy_sectorFigure348OESTopIndexandOESAllIndexChange.png)

  &emsp; |&rarr; [./images/oil_energy_sectorFigure349OESAllIndexvsOESTopIndexChangeScatterPlotwRegression.png](./images/oil_energy_sectorFigure349OESAllIndexvsOESTopIndexChangeScatterPlotwRegression.png)

  &emsp; |&rarr; [./images/oil_energy_sectorFigure411CrudeOilandOESTopIndex.png](./images/oil_energy_sectorFigure411CrudeOilandOESTopIndex.png)

  &emsp; |&rarr; [./images/oil_energy_sectorFigure412CrudeOilandOESTopIndex.png](./images/oil_energy_sectorFigure412CrudeOilandOESTopIndex.png)

  &emsp; |&rarr; [./images/oil_energy_sectorFigure413CrudeOilvsOESTopIndexScatterPlotwRegression.png](./images/oil_energy_sectorFigure413CrudeOilvsOESTopIndexScatterPlotwRegression.png)

  &emsp; |&rarr; [./images/oil_energy_sectorFigure414CrudeOilandOESTopIndexChange.png](./images/oil_energy_sectorFigure414CrudeOilandOESTopIndexChange.png)

  &emsp; |&rarr; [./images/oil_energy_sectorFigure415CrudeOilandOESTopIndexChange.png](./images/oil_energy_sectorFigure415CrudeOilandOESTopIndexChange.png)

  &emsp; |&rarr; [./images/oil_energy_sectorFigure416CrudeOilvsOESTopIndexChangeScatterPlotwRegression.png](./images/oil_energy_sectorFigure416CrudeOilvsOESTopIndexChangeScatterPlotwRegression.png)

  &emsp; |&rarr; [./images/oil_energy_sectorFigure421SP500andOESTopIndex.png](./images/oil_energy_sectorFigure421SP500andOESTopIndex.png)

  &emsp; |&rarr; [./images/oil_energy_sectorFigure422SP500andOESTopIndex.png](./images/oil_energy_sectorFigure422SP500andOESTopIndex.png)

  &emsp; |&rarr; [./images/oil_energy_sectorFigure423SP500vsOESTopIndexScatterPlotwRegression.png](./images/oil_energy_sectorFigure423SP500vsOESTopIndexScatterPlotwRegression.png)

  &emsp; |&rarr; [./images/oil_energy_sectorFigure424SP500andOESTopIndexChange.png](./images/oil_energy_sectorFigure424SP500andOESTopIndexChange.png)

  &emsp; |&rarr; [./images/oil_energy_sectorFigure425SP500andOESTopIndexChange.png](./images/oil_energy_sectorFigure425SP500andOESTopIndexChange.png)

  &emsp; |&rarr; [./images/oil_energy_sectorFigure426SP500vsOESTopIndexChangeScatterPlotwRegression.png](./images/oil_energy_sectorFigure426SP500vsOESTopIndexChangeScatterPlotwRegression.png)

  &emsp; |&rarr; [./images/oil_energy_sectorFigure431GoldandOESTopIndex.png](./images/oil_energy_sectorFigure431GoldandOESTopIndex.png)

  &emsp; |&rarr; [./images/oil_energy_sectorFigure432GoldandOESTopIndex.png](./images/oil_energy_sectorFigure432GoldandOESTopIndex.png)

  &emsp; |&rarr; [./images/oil_energy_sectorFigure433GoldvsOESTopIndexScatterPlotwRegression.png](./images/oil_energy_sectorFigure433GoldvsOESTopIndexScatterPlotwRegression.png)

  &emsp; |&rarr; [./images/oil_energy_sectorFigure434GoldandOESTopIndexChange.png](./images/oil_energy_sectorFigure434GoldandOESTopIndexChange.png)

  &emsp; |&rarr; [./images/oil_energy_sectorFigure435GoldandOESTopIndexChange.png](./images/oil_energy_sectorFigure435GoldandOESTopIndexChange.png)

  &emsp; |&rarr; [./images/oil_energy_sectorFigure436GoldvsOESTopIndexChangeScatterPlotwRegression.png](./images/oil_energy_sectorFigure436GoldvsOESTopIndexChangeScatterPlotwRegression.png)

  &emsp; |&rarr; [./images/oil_energy_sectorFigure451NewCovidCasesandOESTopIndex.png](./images/oil_energy_sectorFigure451NewCovidCasesandOESTopIndex.png)

  &emsp; |&rarr; [./images/oil_energy_sectorFigure452NewCovidCasesandOESTopIndex.png](./images/oil_energy_sectorFigure452NewCovidCasesandOESTopIndex.png)

  &emsp; |&rarr; [./images/oil_energy_sectorFigure453NewCovidCasesvsOESTopIndexScatterPlotwRegression.png](./images/oil_energy_sectorFigure453NewCovidCasesvsOESTopIndexScatterPlotwRegression.png)

  &emsp; |&rarr; [./images/oil_energy_sectorFigure454NewCovidCasesandOESTopIndexChange.png](./images/oil_energy_sectorFigure454NewCovidCasesandOESTopIndexChange.png)

  &emsp; |&rarr; [./images/oil_energy_sectorFigure455NewCovidCasesandOESTopIndexChange.png](./images/oil_energy_sectorFigure455NewCovidCasesandOESTopIndexChange.png)

  &emsp; |&rarr; [./images/oil_energy_sectorFigure456NewCovidCasesvsOESTopIndexChangeScatterPlotwRegression.png](./images/oil_energy_sectorFigure456NewCovidCasesvsOESTopIndexChangeScatterPlotwRegression.png)

  &emsp; |&rarr; [./images/oil_energy_sectorFigure461NewCovidDeathsandOESTopIndex.png](./images/oil_energy_sectorFigure461NewCovidDeathsandOESTopIndex.png)

  &emsp; |&rarr; [./images/oil_energy_sectorFigure462NewCovidDeathsandOESTopIndex.png](./images/oil_energy_sectorFigure462NewCovidDeathsandOESTopIndex.png)

  &emsp; |&rarr; [./images/oil_energy_sectorFigure463NewCovidDeathsvsOESTopIndexScatterPlotwRegression.png](./images/oil_energy_sectorFigure463NewCovidDeathsvsOESTopIndexScatterPlotwRegression.png)

  &emsp; |&rarr; [./images/oil_energy_sectorFigure464NewCovidDeathsandOESTopIndexChange.png](./images/oil_energy_sectorFigure464NewCovidDeathsandOESTopIndexChange.png)

  &emsp; |&rarr; [./images/oil_energy_sectorFigure465NewCovidDeathsandOESTopIndexChange.png](./images/oil_energy_sectorFigure465NewCovidDeathsandOESTopIndexChange.png)

  &emsp; |&rarr; [./images/oil_energy_sectorFigure466NewCovidDeathsvsOESTopIndexChangeScatterPlotwRegression.png](./images/oil_energy_sectorFigure466NewCovidDeathsvsOESTopIndexChangeScatterPlotwRegression.png)

  &emsp; |&rarr; [./images/oil_energy_sectorFigure43610YearBondYieldvsOESTopIndexChangeScatterPlotwRegression.png](./images/oil_energy_sectorFigure43610YearBondYieldvsOESTopIndexChangeScatterPlotwRegression.png)

  &emsp; |&rarr; [./images/oil_energy_sectorFigure44110YearBondYieldandOESTopIndex.png](./images/oil_energy_sectorFigure44110YearBondYieldandOESTopIndex.png)

  &emsp; |&rarr; [./images/oil_energy_sectorFigure44210YearBondYieldandOESTopIndex.png](./images/oil_energy_sectorFigure44210YearBondYieldandOESTopIndex.png)

  &emsp; |&rarr; [./images/oil_energy_sectorFigure44310YearBondYieldvsOESTopIndexScatterPlotwRegression.png](./images/oil_energy_sectorFigure44310YearBondYieldvsOESTopIndexScatterPlotwRegression.png)

  &emsp; |&rarr; [./images/oil_energy_sectorFigure44410YearBondYieldandOESTopIndexChange.png](./images/oil_energy_sectorFigure44410YearBondYieldandOESTopIndexChange.png)

  &emsp; |&rarr; [./images/oil_energy_sectorFigure44510YearBondYieldandOESTopIndexChange.png](./images/oil_energy_sectorFigure44510YearBondYieldandOESTopIndexChange.png)

  &emsp; |&rarr; [./images/oil_energy_sectorTable13USOilEnergySectorCompanies.png](./images/oil_energy_sectorTable13USOilEnergySectorCompanies.png)

  &emsp; |&rarr; [./images/oil_energy_sectorTable32TopCompanyinEachOilIndustryfromMarketCapitalizationMedian.png](./images/oil_energy_sectorTable32TopCompanyinEachOilIndustryfromMarketCapitalizationMedian.png)

  &emsp; |&rarr; [./images/oil_energy_sectorTable111EconomicIndicatorPrices.png](./images/oil_energy_sectorTable111EconomicIndicatorPrices.png)

  &emsp; |&rarr; [./images/oil_energy_sectorTable113EconomicIndicatorPricesChange.png](./images/oil_energy_sectorTable113EconomicIndicatorPricesChange.png)

  &emsp; |&rarr; [./images/oil_energy_sectorTable121COVID19CasesandDeathsDuringAnalysisPeriodUSA.png](./images/oil_energy_sectorTable121COVID19CasesandDeathsDuringAnalysisPeriodUSA.png)

  &emsp; |&rarr; [./images/oil_energy_sectorTable122COVID19NewCasesandNewDeathsChangeUSA.png](./images/oil_energy_sectorTable122COVID19NewCasesandNewDeathsChangeUSA.png)

  &emsp; |&rarr; [./images/oil_energy_sectorTable221OilCompanyMarketCapitalizationMetrics.png](./images/oil_energy_sectorTable221OilCompanyMarketCapitalizationMetrics.png)

  &emsp; |&rarr; [./images/oil_energy_sectorTable221OilIndustryMarketCapitalizationMeanStatistics.png](./images/oil_energy_sectorTable221OilIndustryMarketCapitalizationMeanStatistics.png)

  &emsp; |&rarr; [./images/oil_energy_sectorTable231OilIndustryMarketCapitalizationMedianStatistics.png](./images/oil_energy_sectorTable231OilIndustryMarketCapitalizationMedianStatistics.png)

  &emsp; |&rarr; [./images/oil_energy_sectorTable241OilIndustryMarketCapitalizationStandardDeviationStatistics.png](./images/oil_energy_sectorTable241OilIndustryMarketCapitalizationStandardDeviationStatistics.png)

  &emsp; |&rarr; [./images/oil_energy_sectorTable242OilIndustryMarketCapitalizationSEMStatistics.png](./images/oil_energy_sectorTable242OilIndustryMarketCapitalizationSEMStatistics.png)

  &emsp; |&rarr; [./images/oil_energy_sectorTable341OilEnergySectorIndices.png](./images/oil_energy_sectorTable341OilEnergySectorIndices.png)

  &emsp; |&rarr; [./images/oil_energy_sectorTable471AllMetricsCorrelationMatrix.png](./images/oil_energy_sectorTable471AllMetricsCorrelationMatrix.png)

  &emsp; |&rarr; [./images/oil_energy_sectorTable472AllMetricsChangeCorrelationMatrix.png](./images/oil_energy_sectorTable472AllMetricsChangeCorrelationMatrix.png)

  &emsp; |&rarr; [./images/README.md](./images/README.md)

|&rarr; [./logs/](./logs/)

  &emsp; |&rarr; [./logs/20240424oil_energy_sector_log.txt](./logs/20240424oil_energy_sector_log.txt)

  &emsp; |&rarr; [./logs/README.md](./logs/README.md)

|&rarr; [./resources/](./resources/)

  &emsp; |&rarr; [./resources/oil_companies.csv](./resources/oil_companies.csv)

  &emsp; |&rarr; [./resources/README.md](./resources/README.md)

----

### **References:**

----

[Jupyter Notebook Documentation](https://jupyter-notebook.readthedocs.io/en/stable/)

[Matplotlib Documentation](https://matplotlib.org/stable/index.html)

[Numpy documentation](https://numpy.org/doc/1.26/)

[Pandas User Guide](https://pandas.pydata.org/docs/user_guide/index.html)

[Python Documentation](https://docs.python.org/3/contents.html)

----

### **Authors and Acknowledgment:**

----

### Copyright

Nicholas J. George © 2023. All Rights Reserved.
