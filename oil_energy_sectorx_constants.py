#!/usr/bin/env python
# coding: utf-8

# In[1]:


#*******************************************************************************************
 #
 #  File Name:  oil_energy_sectorx_constants.py
 #
 #  File Description:
 #      This Python script, oil_energy_sectorx_constants.py, contains constants 
 #      for completing common tasks for the IPython Notebook, oil_energy_sector.ipynb.
 #
 #
 #  Date            Description                             Programmer
 #  ----------      ------------------------------------    ------------------
 #  08/22/2023      Initial Development                     Nicholas J. George
 #
 #******************************************************************************************/

from enum import Enum


# In[2]:


CONSTANT_LOCAL_FILE_NAME = 'oil_energy_sectorx_constants.py'


# In[3]:


SP_500_YAHOO_TICKER = '^GSPC'

CRUDE_OIL_YAHOO_TICKER = 'CL=F'

GOLD_YAHOO_TICKER = 'GC=F'

TEN_YEAR_BOND_YIELD_YAHOO_TICKER = '^TNX'

BITCOIN_YAHOO_TICKER = 'BTC-USD'


GEOAPIFY_QUERY_URL = 'https://api.geoapify.com/v1/geocode/search?text='

# WHO_COVID_19_DATA_URL = 'https://covid19.who.int/WHO-COVID-19-global-data.csv'

WHO_COVID_19_DATA_URL = 'https://storage.googleapis.com/covid19-open-data/v3/epidemiology.csv'

ALL_OIL_COMPANIES_FILE_PATH = './resources/oil_companies.csv'


START_DATE = '2020-01-03'

END_DATE = '2022-9-14'


# In[4]:


stacked_line_colors_string_list = ['maroon', 'teal', 'darkorange', 'darkmagenta']

covid_colors_string_list = ['firebrick', 'darkblue']

pie_chart_colors_string_list \
    = ['red', 'orange', 'yellow', 'lightgreen', 'lightskyblue', 'violet']

histogram_colors_string_list = ['darkgreen', 'darkorange', 'darkblue', 'firebrick']

geo_hover_columns_string_list \
    = ['longitude', 'latitude', 'company_name', 'ticker', 'industry', 'address']

indices_colors_string_list = ['blue', 'red']

comparison_colors1_string_list = ['teal', 'blue']

comparison_colors2_string_list = ['maroon', 'blue']

comparison_colors3_string_list = ['darkorange', 'blue']

comparison_colors4_string_list = ['darkmagenta', 'blue']

comparison_colors5_string_list = ['darkblue', 'blue']

comparison_colors6_string_list = ['firebrick', 'blue']


# In[5]:


industry_explode_float_tuple = (0.01, 0.01, 0.01, 0.01, 0.01, 0.01)


# In[ ]:




