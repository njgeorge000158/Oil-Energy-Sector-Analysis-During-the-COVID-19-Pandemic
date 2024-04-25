# **Project 1, Oil Energy Sector Analysis**

----

### **Installation:**

----

If the computer has Anaconda, Jupyter Notebook, and a recent version of Python, the IPython notebook already has the following dependencies installed: datetime, io, json, matplotlib, numpy, pandas, pathlib, os, pandas, requests, requests_html, scipy.

In addition to those modules, the IPython notebook needs the following to execute: yfinance, yahoo_fin, holoviews, hvplot, geoviews, geopy, aspose-words, dataframe-image.

Here are the requisite Terminal commands for the installation of these peripheral modules:

python3 -m pip install yfinance

python3 -m pip install yahoo_fin

python3 -m pip install holoviews

python3 -m pip install hvplot

python3 -m pip install geoviews

python3 -m pip install geopy

python3 -m pip install aspose-words

python3 -m pip install dataframe-image

----

### **Usage:**

----

The IPython notebook, oil_energy_sector.ipynb, requires the following Python scripts with it in the same folder:

logx_constants.py

logx.py

mathx.py

matplotlibx.py

oil_energy_sector_config.py

oil_energy_sectorx_constants.py

oil_energy_sectorx.py

pandasx_constants.py

pandasx.py

If the folders, logs and images, are not present, the IPython notebook will create them.  If the CSV file, oil_companies.csv, is not present in the folder, resources, the program will use APIs to generate the CSV file.  Without the CSV file, execution time is an hour; with it, execution time is approximately 1.5 minutes.

To place the IPython notebook in Log Mode or Image Mode set the parameter for the appropriate subroutine in coding cell #2 to True. If the program is in Log Mode, it writes that information to the log file. If the program is in Image Mode, it writes all dataframes, hvplot maps, and matplotlib plots to PNG files in the folder, images.

----

### **Resource Summary:**

----

#### Source code

oil_energy_sector.ipynb, logx_constants.py, logx.py, mathx.py, matplotlibx.py, oil_energy_sector_config.py, oil_energy_sectorx_constants.py, oil_energy_sectorx.py, pandasx_constants.py, pandasx.py

#### Input files

oil_companies.csv

#### Output files

oil_companies.csv

#### SQL script

n/a

#### Software

Jupyter Notebook, Matplotlib, Numpy, Pandas, Python 3.11.4

![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

----

### **GitHub Repository Branches:**

----

#### main branch 

|&rarr; [./logx_constants.py](./logx_constants.py)

|&rarr; [./logx.py](./logx.py)

|&rarr; [./mathx.py](./mathx.py)

|&rarr; [./matplotlibx.py](./matplotlibx.py)

|&rarr; [./oil_energy_sector_config.py](./oil_energy_sector_config.py)

|&rarr; [./oil_energy_sector.ipynb](./oil_energy_sector.ipynb)

|&rarr; [./oil_energy_sectorx_constants.py](./oil_energy_sectorx_constants.py)

|&rarr; [./oil_energy_sectorx.py](./oil_energy_sectorx.py)

|&rarr; [./pandasx_constants.py](./pandasx_constants.py)

|&rarr; [./pandasx.py](./pandasx.py)

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
  
  &emsp; |&rarr; [./images/oil_energy_sectorTable111EconomicIndicatorPrices.png](./images/oil_energy_sectorTable111EconomicIndicatorPrices.png)
  
  &emsp; |&rarr; [./images/oil_energy_sectorTable113EconomicIndicatorPricesChange.png](./images/oil_energy_sectorTable113EconomicIndicatorPricesChange.png)

  &emsp; |&rarr; [./images/oil_energy_sectorTable121COVID19CasesandDeathsDuringAnalysisPeriodUSA.png](./images/oil_energy_sectorTable121COVID19CasesandDeathsDuringAnalysisPeriodUSA.png)
  
  &emsp; |&rarr; [./images/oil_energy_sectorTable122COVID19NewCasesandNewDeathsChangeUSA.png](./images/oil_energy_sectorTable122COVID19NewCasesandNewDeathsChangeUSA.png)

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
