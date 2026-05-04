#!/usr/bin/env python
# coding: utf-8

# In[1]:


 #*******************************************************************************************
 #
 #  File Name:  econ_anlys_vrb.ipynb
 #
 #  File Description:
 #      This interactive Python notebook, econ_anlys_vrb.ipynb, contains functions that 
 #      create and manage the input variables for the generic Jupyter Notebook template 
 #      econ_anlys_gnc.ipynb. Here is the list:
 #
 #  covid_cases_static_xsetup
 #  covid_cases_cumulative_xsetup
 #  covid_deaths_static_xsetup
 #  covid_deaths_cumulative_xsetup
 #  covid_cd_static_xsetup
 #  covid_cd_cumulative_xsetup
 #  xsetup
 #
 #  agr1_ysetup
 #  agr2_ysetup
 #  exchg_rts_ysetup
 #  intrt_rts_ysetup
 #  metals_ysetup
 #  petrol_plus_ysetup
 #  stk_mkt_ysetup
 #  ysetup
 #     
 #  upd_xroll_day
 #  setup_time_prd
 #  setup_dsg
 #  setup
 #
 #  get_dsg
 #  get_xattr
 #  get_yattr
 #  get_prd_attr
 #  get_y_enum
 #
 #  x_time_series
 #  y_time_series_dict
 #  dropna_transform_time_series_dict
 #  find_optimal_candidates
 #  top_candidates_by_time_period_df
 #  set_coords
 #
 #
 #  Date            Description                             Programmer
 #  ----------      ------------------------------------    ------------------
 #  04/10/2026      Initial Development                     Nicholas J. George
 #
 #******************************************************************************************/

import assetx
import dtypesx
import logx
import mathx
import matplotlibx

import pandas as pd
import numpy as np

from IPython.display import clear_output
from enum import Enum, auto


# In[2]:


CONSTANT_LOCAL_FILE_NAME = 'econ_anlys_vrb.py'


# In[3]:


class covid_enum(Enum):
    def _generate_next_value_(name, start, count, last_values):
        return count

    CSS       = auto()

    ROLL_CSS  = auto()

    DTH       = auto()

    ROLL_DTH  = auto()

    CD        = auto()

    ROLL_CD   = auto()

    CCSS      = auto()

    ROLL_CCSS = auto()

    CDTH      = auto()

    ROLL_CDTH = auto()

    CCD       = auto()

    ROLL_CCD  = auto()

class y_enum(Enum):
    def _generate_next_value_(name, start, count, last_values):
        return count

    Y1 = auto()

    Y2 = auto()

    Y3 = auto()

    Y4 = auto()

    Y5 = auto()


# In[4]:


x_typ_list  = ['static', 'cumulative']

x_list      = ['covid_cases', 'covid_deaths', 'covid_c&d']

y_list      = ['agr1', 'agr2', 'exchg_rts', 'intrt_rts', 'metals', 'petrol_plus', 'stk_mkt']

tm_prd_list = ['full_period', 'initial_shock', 'adaptation', 'recovery']


y_vrb_array = np.asarray(y_list, dtype = str)

x_vrb_array = np.asarray(x_list, dtype = str)

bool_vrb_array = np.asarray([True, False], dtype = bool)


# In[5]:


crn_dict \
    = {'dsg':  '',
       'file': {'x': '',
                'y': ''},
       'x':    {'roll': False,
                'day':  7,
                'cml':  False,
                'pct':  False,
                'col':  '',
                'subj': '',
                'cat':  '',
                'lbl':  '',
                'ttl':  ''},
       'y':    {'pct':  False,
                'col':  '',
                'subj': '', 
                'cat': [],
                'lbl': [],
                'ttl': []}}


# In[6]:


x_cat_dict \
    = {'covid':  ['covid_cases',              'roll_covid_cases',
                  'covid_deaths',             'roll_covid_deaths',
                  'covid_c&d',                'roll_covid_c&d',
                  'cml_covid_cases',          'roll_cml_covid_cases',
                  'cml_covid_deaths',         'roll_cml_covid_deaths',
                  'cml_covid_c&d',            'roll_cml_covid_c&d'],
       'covid%': ['covid_cases%',             'roll_covid_cases%',
                  'covid_deaths%',            'roll_covid_deaths%',
                  'covid_c&d%',               'roll_covid_c&d%',
                  'cml_covid_cases%',         'roll_cml_covid_cases%',
                  'cml_covid_deaths%',        'roll_cml_covid_deaths%',
                  'cml_covid_c&d%',           'roll_cml_covid_c&d%']}

x_lbl_dict \
    = {'covid':  ['covid cases',              'roll. covid cases',
                  'covid deaths',             'roll. covid deaths',
                  'covid c&d',                'roll. covid c&d',
                  'cml covid cases',          'roll. cml covid cases',
                  'cml covid deaths',         'roll. cml covid deaths',
                  'cml covid c&d',            'roll. cml covid c&d'],
       'covid%': ['covid cases (%)',          'roll. covid cases (%)',
                  'covid deaths (%)',         'roll. covid deaths (%)',
                  'covid c&d (%)',            'roll. covid c&d (%)',
                  'cml covid cases (%)',      'roll. cml covid cases (%)',
                  'cml covid deaths (%)',     'roll. cml covid deaths (%)',
                  'cml covid c&d (%)',        'roll. cml covid c&d (%)']}

x_ttl_dict \
    = {'covid':  ['Covid-19 Cases',            f"Covid-19 Cases ({crn_dict['x']['day']}-day Roll. Avg.)",
                  'Covid-19 Deaths',           f"Covid-19 Deaths ({crn_dict['x']['day']}-day Roll. Avg.)",
                  'Covid-19 C&D',              f"Covid-19 C&D ({crn_dict['x']['day']}-day Roll. Avg.)",
                  'Cuml. Covid-19 Cases',      f"Cuml. Covid-19 Cases ({crn_dict['x']['day']}-day Roll. Avg.)",
                  'Cuml. Covid-19 Deaths',     f"Cuml. Covid-19 Deaths ({crn_dict['x']['day']}-day Roll. Avg.)",
                  'Cuml. Covid-19 C&D',        f"Cuml. Covid-19 C&D ({crn_dict['x']['day']}-day Roll. Avg.)"],
       'covid%': ['Covid-19 Cases (%)',        f"Covid-19 Cases ({crn_dict['x']['day']}-day Roll. Avg.) (%)",
                  'Covid-19 Deaths (%)',       f"Covid-19 Deaths ({crn_dict['x']['day']}-day Roll. Avg.) (%)",
                  'Covid-19 C&D (%)',          f"Covid-19 C&D ({crn_dict['x']['day']}-day Roll. Avg.) (%)",
                  'Cuml. Covid-19 Cases (%)',  f"Cuml. Covid-19 Cases ({crn_dict['x']['day']}-day Roll. Avg.) (%)",
                  'Cuml. Covid-19 Deaths (%)', f"Cuml. Covid-19 Deaths ({crn_dict['x']['day']}-day Roll. Avg.) (%)",
                  'Cuml. Covid-19 C&D (%)',    f"Cuml. Covid-19 C&D ({crn_dict['x']['day']}-day Roll. Avg.) (%)"]}


# In[7]:


y_cat_dict \
    = {'agr1':         ['cocoa',             'coffee',             'corn',
                        'oats',              'orange_juice'],
       'agr2':         ['rice',              'soybeans',           'sugar',
                        'wheat',             'live_cattle'],
       'exchg_rts':    ['eur',               'aud',                'cad',
                        'sgd',               'bitcoin'],
       'intrt_rts':    ['t_bond_fut',        'treas_yld_5',        't_note',
                        'treas_yld_30',      'cboe_t_note'],
       'metals':       ['gold',              'silver',             'platinum',
                        'palladium',         'copper'],
       'petrol_plus':  ['crude_oil_wti',     'rbob_gasoline',      'heating_oil',
                        'natural_gas',       'oil_top_idx'],
       'stk_mkt':      ['sp500',             'djia',               'nasdaq',
                        'nyse',              'russell'],
       'agr1%':        ['cocoa',             'coffee',             'corn',
                        'oats',              'orange_juice'],
       'agr2%':        ['rice',              'soybeans',           'sugar',
                        'wheat',             'live_cattle'],
       'exchg_rts%':   ['eur',               'aud',                'cad',
                        'sgd',               'bitcoin'],
       'intrt_rts%':   ['treas_bond',        'treas_5_year',       'treas_10_year',
                        'treas_30_year',     'cboe'],
       'metals%':      ['gold',              'silver',             'platinum',
                        'palladium',         'copper'],
       'petrol_plus%': ['crude_oil_wti',     'rbob_gasoline',      'heating_oil',
                        'natural_gas',       'oil_top_idx'],
       'stk_mkt%':     ['sp500',             'djia',               'nasdaq',
                        'nyse',              'russell']}


y_lbl_dict \
    = {'agr1':         ['cocoa',               'coffee',             'corn',
                        'oats',                'orange juice'],
       'agr2':         ['rice',                'soybeans',           'sugar',
                        'wheat',               'live cattle'],
       'exchg_rts':    ['euro',                'aud',                'cad',
                        'sgd',                 'bitcoin'],
       'intrt_rts':    ['t-bnd fut.',          'treas. yld (5)',     't-note',
                        'treas. yld (30)',     'cboe t-note'],
       'metals':       ['gold',                'silver',             'platinum',
                        'palladium',           'copper'],
       'petrol_plus':  ['crude oil wti',       'rbob gasoline',      'heating oil',
                        'natural gas',         'oil idx'],
       'stk_mkt':      ['s&p 500',             'djia',               'nasdaq',
                        'nyse',                'russell'],
       'agr1%':        ['cocoa (%)',           'coffee (%)',         'corn (%)',
                        'oats (%)',            'orange juice (%)'],
       'agr2%':        ['rice (%)',            'soybeans (%)',       'sugar (%)',
                        'wheat (%)',           'live cattle (%)'],
       'exchg_rts%':   ['euro (%)',            'aud (%)',            'cad (%)',
                        'sgd (%)',             'bitcoin (%)'],
       'intrt_rts%':   ['t-bnd fut. (%)',      'treas. yld (5) (%)', 't-note (%)',  
                        'treas. yld (30) (%)', 'cboe t-note (%)'],
       'metals%':      ['gold (%)',            'silver (%)',         'platinum (%)',
                        'palladium (%)',       'copper (%)'],
       'petrol_plus%': ['crude oil wti (%)',   'rbob gasoline (%)',  'heating oil (%)',
                        'natural gas (%)',     'oil idx (%)'],
       'stk_mkt%':     ['s&p 500 (%)',         'djia (%)',           'nasdaq (%)',
                        'nyse (%)',            'russell (%)']}


y_ttl_dict \
    = {'agr1':         ['Cocoa Prices',                   'Coffee Prices',             'Corn Prices',      
                        'Oat Prices',                     'Orange Juice Prices'],
       'agr2':         ['Rice Prices',                    'Soybean Prices',             'Sugar Prices',     
                        'Wheat Prices',                   'Live Cattle'],
       'exchg_rts':    ['Euro',                           'Australian Dollar',          'Canadian Dollar',  
                        'Singapore Dollar',               'Bitcoin'],
       'intrt_rts':    ['U.S. Treasury Bond Futures',     'Treasury Yield (5-Yr.)',     'T-Note Futures (10-Yr.)',  
                        'Treasury Yield (30-Yr.)',        'CBOE T-Note (10-Yr.)'],
       'metals':       ['Gold Prices',                    'Silver Prices',              'Platinum Prices',  
                        'Palladium Prices',               'Copper Prices'],
       'petrol_plus':  ['Crude Oil Prices (WTI)',         'RBOB Gasoline Prices',       'Heating Oil Prices', 
                        'Natural Gas Prices',             'Oil Energy Sector Index'],
       'stk_mkt':      ['S&P 500',                        'DJIA',                       'Nasdaq Composite', 
                        'NYSE Composite',                 'Russell 2000'],
       'agr1%':        ['Cocoa Prices (%)',               'Coffee Prices (%)',          'Corn Prices (%)',  
                        'Oat Prices (%)',                 'Orange Juice Prices (%)'],
       'agr2%':        ['Rice Prices (%)',                'Soybean Prices (%)',         'Sugar Prices (%)', 
                        'Wheat Prices (%)',               'Live Cattle (%)'],
       'exchg_rts%':   ['Euro (%)',                       'Australian Dollar (%)',      'Canadian Dollar (%)', 
                        'Singapore Dollar (%)',           'Bitcoin (%)'],
       'intrt_rts%':   ['U.S. Treasury Bond Futures (%)', 'Treasury Yield (5-Yr.) (%)', 'T-Note Futures (10-Yr.) (%)',  
                        'Treasury Yield (30-Yr.) (%)',    'CBOE T-Note (10-Yr.) (%)'],
       'metals%':      ['Gold Prices (%)',                'Silver Prices (%)',          'Platinum Prices (%)',  
                        'Palladium Prices (%)',           'Copper Prices (%)'],
       'petrol_plus%': ['Crude Oil Prices (WTI)',         'RBOB Gasoline Prices',       'Heating Oil Prices', 
                        'Natural Gas Prices',             'Oil Energy Sector Index (%)'],
       'stk_mkt%':     ['S&P 500 (%)',                    'DJIA (%)',                   'Nasdaq Composite (%)', 
                        'NYSE Composite (%)',             'Russell 2000 (%)']}


# In[8]:


x_abbr_dict \
    = {'covid_cases':   'css',
       'covid_deaths':  'dth',
       'covid_c&d':     'cnd'}

y_abbr_dict \
    = {'agr1':          'agr1',
       'agr2':          'agr2',
       'exchg_rts':     'exr',
       'intrt_rts':     'itr',
       'metals':        'mts',
       'petrol':        'oil',
       'petrol_plus':   'oilp',
       'stk_mkt':       'mkt'}

tm_abbr_dict \
    = {'full_period':   'fll',
       'initial_shock': 'shk',
       'adaptation':    'adp',
       'recovery':      'rec'}


# In[9]:


tm_prd_dict = None

full_prd_dict \
    = {'text':  '(Full Period)',
       'start': '2020-01-22',
       'end':   '2022-09-14'}

init_shk_prd_dict \
    = {'text':  '(Initial Shock)',
       'start': '2020-01-22',
       'end':   '2020-06-07'}

adpt_prd_dict \
    = {'text':  '(Adaptation)',
       'start': '2020-06-08',
       'end':   '2021-11-25'}

rcvry_prd_dict \
    = {'text':  '(Recovery)',
       'start': '2021-11-26',
       'end':   '2022-09-14'}   


# In[10]:


#*******************************************************************************************
 #
 #  Function Name:  covid_cases_static_xsetup
 #
 #  Function Description:
 #      This function assigns values to the variables for a static covid cases x-value 
 #      time series.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  boolean        x_roll           The parameter is the indicator that the x-value time 
 #                                  series has had a rolling average applied to it.
 #  boolean        pct              The parameter is the indicator that the x-value time 
 #                                  series has had a pecent change applied to it.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  04/27/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def covid_cases_static_xsetup \
        (x_roll: bool, 
         pct:    bool):

    global crn_dict

    crn_dict['x']['col'] = 'covid_cases'

    crn_dict['x']['cml'] = False

    if x_roll:

        if pct:

            crn_dict['x']['cat'] = x_cat_dict['covid%'][covid_enum.ROLL_CSS.value]

            crn_dict['x']['lbl'] = x_lbl_dict['covid%'][covid_enum.ROLL_CSS.value]

            crn_dict['x']['ttl'] = x_ttl_dict['covid%'][covid_enum.ROLL_CSS.value]

        else:

            crn_dict['x']['cat'] = x_cat_dict['covid'][covid_enum.ROLL_CSS.value]

            crn_dict['x']['lbl'] = x_lbl_dict['covid'][covid_enum.ROLL_CSS.value]

            crn_dict['x']['ttl'] = x_ttl_dict['covid'][covid_enum.ROLL_CSS.value]

    else:

        if pct:

            crn_dict['x']['cat'] = x_cat_dict['covid%'][covid_enum.CSS.value]

            crn_dict['x']['lbl'] = x_lbl_dict['covid%'][covid_enum.CSS.value]

            crn_dict['x']['ttl'] = x_ttl_dict['covid%'][covid_enum.CSS.value]

        else:

            crn_dict['x']['cat'] = x_cat_dict['covid'][covid_enum.CSS.value]

            crn_dict['x']['lbl'] = x_lbl_dict['covid'][covid_enum.CSS.value]

            crn_dict['x']['ttl'] = x_ttl_dict['covid'][covid_enum.CSS.value]


# In[11]:


#*******************************************************************************************
 #
 #  Function Name:  covid_cases_cumulative_xsetup
 #
 #  Function Description:
 #      This function assigns values to the variables for a cumulative covid cases 
 #      x-value time series.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  boolean        x_roll           The parameter is the indicator that the x-value time 
 #                                  series has had a rolling average applied to it.
 #  boolean        pct              The parameter is the indicator that the x-value time 
 #                                  series has had a pecent change applied to it.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  04/27/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def covid_cases_cumulative_xsetup \
        (x_roll: bool, 
         pct:    bool):

    global crn_dict

    crn_dict['x']['col'] = 'cml_covid_cases'

    crn_dict['x']['cml'] = True

    if x_roll:

        if pct:

            crn_dict['x']['cat'] = x_cat_dict['covid%'][covid_enum.ROLL_CCSS.value]

            crn_dict['x']['lbl'] = x_lbl_dict['covid%'][covid_enum.ROLL_CCSS.value]

            crn_dict['x']['ttl'] = x_ttl_dict['covid%'][covid_enum.ROLL_CCSS.value]

        else:

            crn_dict['x']['cat'] = x_cat_dict['covid'][covid_enum.ROLL_CCSS.value]

            crn_dict['x']['lbl'] = x_lbl_dict['covid'][covid_enum.ROLL_CCSS.value]

            crn_dict['x']['ttl'] = x_ttl_dict['covid'][covid_enum.ROLL_CCSS.value]

    else:

        if pct:

            crn_dict['x']['cat'] = x_cat_dict['covid%'][covid_enum.CCSS.value]

            crn_dict['x']['lbl'] = x_lbl_dict['covid%'][covid_enum.CCSS.value]

            crn_dict['x']['ttl'] = x_ttl_dict['covid%'][covid_enum.CCSS.value]

        else:

            crn_dict['x']['cat'] = x_cat_dict['covid'][covid_enum.CCSS.value]

            crn_dict['x']['lbl'] = x_lbl_dict['covid'][covid_enum.CCSS.value]

            crn_dict['x']['ttl'] = x_ttl_dict['covid'][covid_enum.CCSS.value]


# In[12]:


#*******************************************************************************************
 #
 #  Function Name:  covid_deaths_static_xsetup
 #
 #  Function Description:
 #      This function assigns values to the variables for a static covid deaths x-value 
 #      time series.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  boolean        x_roll           The parameter is the indicator that the x-value time 
 #                                  series has had a rolling average applied to it.
 #  boolean        pct              The parameter is the indicator that the x-value time 
 #                                  series has had a pecent change applied to it.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  04/27/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def covid_deaths_static_xsetup \
        (x_roll: bool, 
         pct:    bool):

    global crn_dict

    crn_dict['x']['col'] = 'covid_deaths'

    crn_dict['x']['cml'] = False

    if x_roll:

        if pct:

            crn_dict['x']['cat'] = x_cat_dict['covid%'][covid_enum.ROLL_DTH.value]

            crn_dict['x']['lbl'] = x_lbl_dict['covid%'][covid_enum.ROLL_DTH.value]

            crn_dict['x']['ttl'] = x_ttl_dict['covid%'][covid_enum.ROLL_DTH.value]

        else:

            crn_dict['x']['cat'] = x_cat_dict['covid'][covid_enum.ROLL_DTH.value]

            crn_dict['x']['lbl'] = x_lbl_dict['covid'][covid_enum.ROLL_DTH.value]

            crn_dict['x']['ttl'] = x_ttl_dict['covid'][covid_enum.ROLL_DTH.value]

    else:

        if pct:

            crn_dict['x']['cat'] = x_cat_dict['covid%'][covid_enum.DTH.value]

            crn_dict['x']['lbl'] = x_lbl_dict['covid%'][covid_enum.DTH.value]

            crn_dict['x']['ttl'] = x_ttl_dict['covid%'][covid_enum.DTH.value]

        else:

            crn_dict['x']['cat'] = x_cat_dict['covid'][covid_enum.DTH.value]

            crn_dict['x']['lbl'] = x_lbl_dict['covid'][covid_enum.DTH.value]

            crn_dict['x']['ttl'] = x_ttl_dict['covid'][covid_enum.DTH.value]  


# In[13]:


#*******************************************************************************************
 #
 #  Function Name:  covid_deaths_cumulative_xsetup
 #
 #  Function Description:
 #      This function assigns values to the variables for a cumulative covid deaths 
 #      x-value time series.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  boolean        x_roll           The parameter is the indicator that the x-value time 
 #                                  series has had a rolling average applied to it.
 #  boolean        pct              The parameter is the indicator that the x-value time 
 #                                  series has had a pecent change applied to it.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  04/27/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def covid_deaths_cumulative_xsetup \
        (x_roll: bool, 
         pct:    bool):

    global crn_dict

    crn_dict['x']['col'] = 'cml_covid_deaths'

    crn_dict['x']['cml'] = True

    if x_roll:

        if pct:

            crn_dict['x']['cat'] = x_cat_dict['covid%'][covid_enum.ROLL_CDTH.value]

            crn_dict['x']['lbl'] = x_lbl_dict['covid%'][covid_enum.ROLL_CDTH.value]

            crn_dict['x']['ttl'] = x_ttl_dict['covid%'][covid_enum.ROLL_CDTH.value]

        else:

            crn_dict['x']['cat'] = x_cat_dict['covid'][covid_enum.ROLL_CDTH.value]

            crn_dict['x']['lbl'] = x_lbl_dict['covid'][covid_enum.ROLL_CDTH.value]

            crn_dict['x']['ttl'] = x_ttl_dict['covid'][covid_enum.ROLL_CDTH.value]

    else:

        if pct:

            crn_dict['x']['cat'] = x_cat_dict['covid%'][covid_enum.CDTH.value]

            crn_dict['x']['lbl'] = x_lbl_dict['covid%'][covid_enum.CDTH.value]

            crn_dict['x']['ttl'] = x_ttl_dict['covid%'][covid_enum.CDTH.value]

        else:

            crn_dict['x']['cat'] = x_cat_dict['covid'][covid_enum.CDTH.value]

            crn_dict['x']['lbl'] = x_lbl_dict['covid'][covid_enum.CDTH.value]

            crn_dict['x']['ttl'] = x_ttl_dict['covid'][covid_enum.CDTH.value]    


# In[14]:


#*******************************************************************************************
 #
 #  Function Name:  covid_cd_static_xsetup
 #
 #  Function Description:
 #      This function assigns values to the variables for a static covid cases and 
 #      deaths x-value time series.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  boolean        x_roll           The parameter is the indicator that the x-value time 
 #                                  series has had a rolling average applied to it.
 #  boolean        pct              The parameter is the indicator that the x-value time 
 #                                  series has had a pecent change applied to it.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  04/27/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def covid_cd_static_xsetup \
        (x_roll: bool, 
         pct:    bool):

    global crn_dict

    crn_dict['x']['col'] = 'covid_c&d'

    crn_dict['x']['cml'] = False

    if x_roll:

        if pct:

            crn_dict['x']['cat'] = x_cat_dict['covid%'][covid_enum.ROLL_CD.value]

            crn_dict['x']['lbl'] = x_lbl_dict['covid%'][covid_enum.ROLL_CD.value]

            crn_dict['x']['ttl'] = x_ttl_dict['covid%'][covid_enum.ROLL_CD.value]

        else:

            crn_dict['x']['cat'] = x_cat_dict['covid'][covid_enum.ROLL_CD.value]

            crn_dict['x']['lbl'] = x_lbl_dict['covid'][covid_enum.ROLL_CD.value]

            crn_dict['x']['ttl'] = x_ttl_dict['covid'][covid_enum.ROLL_CD.value]

    else:

        if pct:

            crn_dict['x']['cat'] = x_cat_dict['covid%'][covid_enum.CD.value]

            crn_dict['x']['lbl'] = x_lbl_dict['covid%'][covid_enum.CD.value]

            crn_dict['x']['ttl'] = x_ttl_dict['covid%'][covid_enum.CD.value]

        else:

            crn_dict['x']['cat'] = x_cat_dict['covid'][covid_enum.CD.value]

            crn_dict['x']['lbl'] = x_lbl_dict['covid'][covid_enum.CD.value]

            crn_dict['x']['ttl'] = x_ttl_dict['covid'][covid_enum.CD.value]


# In[15]:


#*******************************************************************************************
 #
 #  Function Name:  covid_cd_cumulative_xsetup
 #
 #  Function Description:
 #      This function assigns values to the variables for a cumulative covid cases 
 #      and deaths x-value time series.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  boolean        x_roll           The parameter is the indicator that the x-value time 
 #                                  series has had a rolling average applied to it.
 #  boolean        pct              The parameter is the indicator that the x-value time 
 #                                  series has had a pecent change applied to it.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  04/27/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def covid_cd_cumulative_xsetup \
        (x_roll: bool, 
         pct:    bool):

    global crn_dict

    crn_dict['x']['col'] = 'cml_covid_c&d'

    crn_dict['x']['cml'] = True

    if x_roll:

        if pct:

            crn_dict['x']['cat'] = x_cat_dict['covid%'][covid_enum.ROLL_CCD.value]

            crn_dict['x']['lbl'] = x_lbl_dict['covid%'][covid_enum.ROLL_CCD.value]

            crn_dict['x']['ttl'] = x_ttl_dict['covid%'][covid_enum.ROLL_CCD.value]

        else:

            crn_dict['x']['cat'] = x_cat_dict['covid'][covid_enum.ROLL_CCD.value]

            crn_dict['x']['lbl'] = x_lbl_dict['covid'][covid_enum.ROLL_CCD.value]

            crn_dict['x']['ttl'] = x_ttl_dict['covid'][covid_enum.ROLL_CCD.value]

    else:

        if pct:

            crn_dict['x']['cat'] = x_cat_dict['covid%'][covid_enum.CCD.value]

            crn_dict['x']['lbl'] = x_lbl_dict['covid%'][covid_enum.CCD.value]

            crn_dict['x']['ttl'] = x_ttl_dict['covid%'][covid_enum.CCD.value]

        else:

            crn_dict['x']['cat'] = x_cat_dict['covid'][covid_enum.CCD.value]

            crn_dict['x']['lbl'] = x_lbl_dict['covid'][covid_enum.CCD.value]

            crn_dict['x']['ttl'] = x_ttl_dict['covid'][covid_enum.CCD.value]


# In[16]:


#*******************************************************************************************
 #
 #  Function Name:  xsetup
 #
 #  Function Description:
 #      This function assigns values to the variables for the x-variable time series.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  boolean        xcml             The parameter is the indicator that the x-value time 
 #                                  series is cumulative
 #  string         x                The parameter is the name of the x-variable.
 #  boolean        x_roll           The parameter is the indicator that the x-value time 
 #                                  series has had a rolling average applied to it.
 #  boolean        pct              The parameter is the indicator that the x-value time 
 #                                  series has had a pecent change applied to it.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  04/27/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def xsetup \
        (xcml:   bool, 
         x:      str, 
         x_roll: bool = True, 
         pct:    bool = False):

    global crn_dict      


    crn_dict['x']['roll']     = x_roll


    if x == 'covid_cases' or x == 'covid_deaths' or x == 'covid_c&d':

        crn_dict['file']['x'] = './resources/covid_usa.json'

        crn_dict['x']['subj'] = 'COVID-19 Pandemic'


    if x == 'covid_cases':

        if xcml: covid_cases_cumulative_xsetup(x_roll, pct)

        else:    covid_cases_static_xsetup(x_roll, pct)

    elif x == 'covid_deaths':

        if xcml: covid_deaths_cumulative_xsetup(x_roll, pct)

        else:    covid_deaths_static_xsetup(x_roll, pct)

    elif x == 'covid_c&d':

        if xcml: covid_cd_cumulative_xsetup(x_roll, pct)

        else:    covid_cd_static_xsetup(x_roll, pct)


# In[17]:


#*******************************************************************************************
 #
 #  Function Name:  agr1_ysetup
 #
 #  Function Description:
 #      This function assigns values to the variables for the y1-variable agriculture
 #      prices.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  boolean        pct              The parameter is the indicator that the y-value time 
 #                                  series has had a pecent change applied to it.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  04/27/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def agr1_ysetup(pct: bool):

    global crn_dict


    crn_dict['y']['col']  = 'agr1'

    crn_dict['file']['y'] = './resources/agr1.json'        


    crn_dict['y']['subj'] = 'Agricultural Prices (Part 1)'


    if pct:

        crn_dict['y']['cat']  = y_cat_dict['agr1%']

        crn_dict['y']['lbl']  = y_lbl_dict['agr1%']

        crn_dict['y']['ttl']  = y_ttl_dict['agr1%']

    else:

        crn_dict['y']['cat']  = y_cat_dict['agr1']

        crn_dict['y']['lbl']  = y_lbl_dict['agr1']

        crn_dict['y']['ttl']  = y_ttl_dict['agr1'] 


# In[18]:


#*******************************************************************************************
 #
 #  Function Name:  agr2_ysetup
 #
 #  Function Description:
 #      This function assigns values to the variables for the y2-variable agriculture
 #      prices.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  boolean        pct              The parameter is the indicator that the y-value time 
 #                                  series has had a pecent change applied to it.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  04/27/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def agr2_ysetup(pct: bool):

    global crn_dict


    crn_dict['y']['col']  = 'agr2'

    crn_dict['file']['y'] = './resources/agr2.json'        


    crn_dict['y']['subj'] = 'Agricultural Prices (Part 2)'


    if pct:

        crn_dict['y']['cat']  = y_cat_dict['agr2%']

        crn_dict['y']['lbl']  = y_lbl_dict['agr2%']

        crn_dict['y']['ttl']  = y_ttl_dict['agr2%']

    else:

        crn_dict['y']['cat']  = y_cat_dict['agr2']

        crn_dict['y']['lbl']  = y_lbl_dict['agr2']

        crn_dict['y']['ttl']  = y_ttl_dict['agr2'] 


# In[19]:


#*******************************************************************************************
 #
 #  Function Name:  exchg_rts_ysetup
 #
 #  Function Description:
 #      This function assigns values to the variables for the y-variable exchange rates.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  boolean        pct              The parameter is the indicator that the y-value time 
 #                                  series has had a pecent change applied to it.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  04/27/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def exchg_rts_ysetup(pct: bool):

    global crn_dict


    crn_dict['y']['col']  = 'exchg_rts'

    crn_dict['file']['y'] = './resources/exchg_rts.json'        


    crn_dict['y']['subj'] = 'Exchange Rates (USD)'


    if pct:

        crn_dict['y']['cat']  = y_cat_dict['exchg_rts%']

        crn_dict['y']['lbl']  = y_lbl_dict['exchg_rts%']

        crn_dict['y']['ttl']  = y_ttl_dict['exchg_rts%']

    else:

        crn_dict['y']['cat']  = y_cat_dict['exchg_rts']

        crn_dict['y']['lbl']  = y_lbl_dict['exchg_rts']

        crn_dict['y']['ttl']  = y_ttl_dict['exchg_rts'] 


# In[20]:


#*******************************************************************************************
 #
 #  Function Name:  intrt_rts_ysetup
 #
 #  Function Description:
 #      This function assigns values to the variables for the y-variable interest rates.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  boolean        pct              The parameter is the indicator that the y-value time 
 #                                  series has had a pecent change applied to it.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  04/27/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def intrt_rts_ysetup(pct: bool):

    global crn_dict


    crn_dict['y']['col']  = 'intrt_rts'

    crn_dict['file']['y'] = './resources/intrt_rts.json'        


    crn_dict['y']['subj'] = 'U.S. Interest Rate Futures & Yields'


    if pct:

        crn_dict['y']['cat']  = y_cat_dict['intrt_rts%']

        crn_dict['y']['lbl']  = y_lbl_dict['intrt_rts%']

        crn_dict['y']['ttl']  = y_ttl_dict['intrt_rts%']

    else:

        crn_dict['y']['cat']  = y_cat_dict['intrt_rts']

        crn_dict['y']['lbl']  = y_lbl_dict['intrt_rts']

        crn_dict['y']['ttl']  = y_ttl_dict['intrt_rts']


# In[21]:


#*******************************************************************************************
 #
 #  Function Name:  metals_ysetup
 #
 #  Function Description:
 #      This function assigns values to the variables for the y-variable metals prices.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  boolean        pct              The parameter is the indicator that the y-value time 
 #                                  series has had a pecent change applied to it.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  04/27/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def metals_ysetup(pct: bool):

    global crn_dict


    crn_dict['y']['col']  = 'metals'

    crn_dict['file']['y'] = './resources/metals.json'        


    crn_dict['y']['subj'] = 'Metals Prices (USD)'


    if pct:

        crn_dict['y']['cat']  = y_cat_dict['metals%']

        crn_dict['y']['lbl']  = y_lbl_dict['metals%']

        crn_dict['y']['ttl']  = y_ttl_dict['metals%']

    else:

        crn_dict['y']['cat']  = y_cat_dict['metals']

        crn_dict['y']['lbl']  = y_lbl_dict['metals']

        crn_dict['y']['ttl']  = y_ttl_dict['metals'] 


# In[22]:


#*******************************************************************************************
 #
 #  Function Name:  petrol_plus_ysetup
 #
 #  Function Description:
 #      This function assigns values to the variables for the y-variable petroleum prices.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  boolean        pct              The parameter is the indicator that the y-value time 
 #                                  series has had a pecent change applied to it.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  04/27/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def petrol_plus_ysetup(pct: bool):

    global crn_dict


    crn_dict['y']['col']  = 'petrol_plus'

    crn_dict['file']['y'] = './resources/petrol_plus.json'        


    crn_dict['y']['subj'] = 'Oil Energy Sector'


    if pct:

        crn_dict['y']['cat']  = y_cat_dict['petrol_plus%']

        crn_dict['y']['lbl']  = y_lbl_dict['petrol_plus%']

        crn_dict['y']['ttl']  = y_ttl_dict['petrol_plus%']

    else:

        crn_dict['y']['cat']  = y_cat_dict['petrol_plus']

        crn_dict['y']['lbl']  = y_lbl_dict['petrol_plus']

        crn_dict['y']['ttl']  = y_ttl_dict['petrol_plus']


# In[23]:


#*******************************************************************************************
 #
 #  Function Name:  stk_mkt_ysetup
 #
 #  Function Description:
 #      This function assigns values to the variables for the y-variable stock market 
 #      indices prices.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  boolean        pct              The parameter is the indicator that the y-value time 
 #                                  series has had a pecent change applied to it.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  04/27/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def stk_mkt_ysetup(pct: bool):

    global crn_dict


    crn_dict['y']['col']  = 'stk_mkt'

    crn_dict['file']['y'] = './resources/stk_mkt.json'        


    crn_dict['y']['subj'] = 'Stock Market Indices'


    if pct:

        crn_dict['y']['cat']  = y_cat_dict['stk_mkt%']

        crn_dict['y']['lbl']  = y_lbl_dict['stk_mkt%']

        crn_dict['y']['ttl']  = y_ttl_dict['stk_mkt%']

    else:

        crn_dict['y']['cat']  = y_cat_dict['stk_mkt']

        crn_dict['y']['lbl']  = y_lbl_dict['stk_mkt']

        crn_dict['y']['ttl']  = y_ttl_dict['stk_mkt']


# In[24]:


#*******************************************************************************************
 #
 #  Function Name:  xsetup
 #
 #  Function Description:
 #      This function assigns values to the variables for the x-variable time series.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  string         y                The parameter is the name of the y-variable.
 #  boolean        pct              The parameter is the indicator that the y-value time 
 #                                  series has had a pecent change applied to it.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  04/27/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def ysetup(y: str, pct: bool):

    if y == 'agr1':          agr1_ysetup(pct)

    elif y == 'agr2':        agr2_ysetup(pct)

    elif y == 'exchg_rts':   exchg_rts_ysetup(pct)

    elif y == 'intrt_rts':   intrt_rts_ysetup(pct)

    elif y == 'metals':      metals_ysetup(pct)

    elif y == 'petrol_plus': petrol_plus_ysetup(pct)

    elif y == 'stk_mkt':     stk_mkt_ysetup(pct)


# In[25]:


#*******************************************************************************************
 #
 #  Function Name:  upd_xroll_day
 #
 #  Function Description:
 #      This function updates the day value for the rolling average of the x-variable.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  integer        day              The parameter is the updated rolling average day 
 #                                  value.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  04/27/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def upd_xroll_day(day: int):

    global crn_dict

    global x_ttl_dict


    crn_dict['x']['day'] = day


    x_ttl_dict['covid'][covid_enum.ROLL_CSS.value]   = f"Covid-19 Cases ({day}-day Roll. Avg.)"

    x_ttl_dict['covid%'][covid_enum.ROLL_CSS.value]  = f"Covid-19 Cases ({day}-day Roll. Avg.) (%)"


    x_ttl_dict['covid'][covid_enum.ROLL_DTH.value]   = f"Covid-19 Deaths ({crn_dict['x']['day']}-day Roll. Avg.)"

    x_ttl_dict['covid%'][covid_enum.ROLL_DTH.value]  = f"Covid-19 Deaths ({crn_dict['x']['day']}-day Roll. Avg.) (%)"


    x_ttl_dict['covid'][covid_enum.ROLL_CD.value]    = f"Covid-19 C&D ({crn_dict['x']['day']}-day Roll. Avg.)"

    x_ttl_dict['covid%'][covid_enum.ROLL_CD.value]   = f"Covid-19 C&D ({crn_dict['x']['day']}-day Roll. Avg.) (%)"


    x_ttl_dict['covid'][covid_enum.ROLL_CCSS.value]  = f"Cuml. Covid-19 Cases ({day}-day Roll. Avg.)"

    x_ttl_dict['covid%'][covid_enum.ROLL_CCSS.value] = f"Cuml. Covid-19 Cases ({day}-day Roll. Avg.) (%)"


    x_ttl_dict['covid'][covid_enum.ROLL_CDTH.value]  = f"Cuml. Covid-19 Deaths ({crn_dict['x']['day']}-day Roll. Avg.)"

    x_ttl_dict['covid%'][covid_enum.ROLL_CDTH.value] = f"Cuml. Covid-19 Deaths ({crn_dict['x']['day']}-day Roll. Avg.) (%)"


    x_ttl_dict['covid'][covid_enum.ROLL_CCD.value]   = f"Cuml. Covid-19 C&D ({crn_dict['x']['day']}-day Roll. Avg.)"

    x_ttl_dict['covid%'][covid_enum.ROLL_CCD.value]  = f"Cuml. Covid-19 C&D ({crn_dict['x']['day']}-day Roll. Avg.) (%)"


# In[26]:


#*******************************************************************************************
 #
 #  Function Name:  setup_time_prd
 #
 #  Function Description:
 #      This function setups the time period information for analysis.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  string         tm_prd           The parameter is the name of the time period.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  04/27/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def setup_time_prd(tm_prd: str):

    global tm_prd_dict


    if   tm_prd == 'full_period':   tm_prd_dict = full_prd_dict.copy()

    elif tm_prd == 'initial_shock': tm_prd_dict = init_shk_prd_dict.copy()

    elif tm_prd == 'adaptation':    tm_prd_dict = adpt_prd_dict.copy()

    elif tm_prd == 'recovery':      tm_prd_dict = rcvry_prd_dict.copy()


# In[27]:


#*******************************************************************************************
 #
 #  Function Name:  setup_dsg
 #
 #  Function Description:
 #      This function setups the analysis designation name.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  boolean        xcml             The parameter is the indicator that the x-value time 
 #                                  series is cumulative
 #  string         x                The parameter is the name of the x-variable.
 #  string         y                The parameter is the name of the y-variable.
 #  string         tm_prd           The parameter is the name of the time period.
 #  boolean        x_roll           The parameter is the indicator that the x-value time 
 #                                  series has had a rolling average applied to it.
 #  integer        x_roll_days      The parameter is the updated rolling average day 
 #                                  value.
 #  boolean        pct              The parameter is the indicator that the x-value time 
 #                                  series has had a pecent change applied to it.
 #  string         bse              The parameter is the base designation name.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  04/27/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def setup_dsg \
        (xcml:        bool,
         x:           str, 
         y:           str,  
         tm_prd:      str,
         x_roll:      bool,
         x_roll_days: int,
         pct:         bool,
         bse:         str): 

    global crn_dict


    crn_dict['dsg'] = bse + '_' + tm_abbr_dict[tm_prd]


    if pct:    crn_dict['dsg'] += '_pct'

    if x_roll: crn_dict['dsg'] += '_rll' + str(x_roll_days)

    if xcml:   crn_dict['dsg'] += '_cml'


    crn_dict['dsg'] += '_' + x_abbr_dict[x] + '_' + y_abbr_dict[y]


# In[28]:


#*******************************************************************************************
 #
 #  Function Name:  setup
 #
 #  Function Description:
 #      This function setups the variables for analysis.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  boolean        xcml             The parameter is the indicator that the x-value time 
 #                                  series is cumulative
 #  string         x                The parameter is the name of the x-variable.
 #  string         y                The parameter is the name of the y-variable.
 #  string         tm_prd           The parameter is the name of the time period.
 #  boolean        x_roll           The parameter is the indicator that the x-value time 
 #                                  series has had a rolling average applied to it.
 #  integer        x_roll_days      The parameter is the updated rolling average day 
 #                                  value.
 #  boolean        xpct             The parameter is the indicator that the x-value time 
 #                                  series has had a pecent change applied to it.
 #  boolean        ypct             The parameter is the indicator that the y-value time 
 #                                  series has had a pecent change applied to it.
 #  string         bse              The parameter is the base designation name.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  04/27/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def setup \
        (xcml:        bool, 
         x:           str,
         y:           str, 
         tm_prd:      str,
         x_roll:      bool = True,
         x_roll_days: int = 7,
         xpct:        bool = False,
         ypct:        bool = False,
         bse:         str = 'econ_anlys'):

    global crn_dict


    crn_dict['x']['pct'] = xpct

    crn_dict['y']['pct'] = ypct            


    x               = x.strip().lower()

    y               = y.strip().lower()


    tm_prd          = tm_prd.strip().lower()

    bse             = bse.strip().lower()


    upd_xroll_day(x_roll_days)

    xsetup(xcml, x, x_roll, xpct)


    ysetup(y, ypct)


    setup_time_prd(tm_prd)

    setup_dsg(xcml, x, y, tm_prd, x_roll, x_roll_days, xpct, bse)


# In[29]:


#*******************************************************************************************
 #
 #  Function Name:  get_dsg
 #
 #  Function Description:
 #      This function retrieves the analysis designation.
 #
 #
 #  Return Type: string
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  n/a            n/a              n/a
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  04/27/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_dsg() -> str: return crn_dict['dsg']


# In[30]:


#*******************************************************************************************
 #
 #  Function Name:  get_xattr
 #
 #  Function Description:
 #      This function retrieves the x-variable attributes.
 #
 #
 #  Return Type: string, string, string, string, string, boolean, integer
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  n/a            n/a              n/a
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  04/27/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_xattr() -> tuple[str, str, str, str, str, bool, int]:

    return \
        crn_dict['x']['col'], \
        crn_dict['x']['subj'], \
        crn_dict['x']['cat'], \
        crn_dict['x']['lbl'], \
        crn_dict['x']['ttl'], \
        crn_dict['x']['roll'], \
        crn_dict['x']['day'], \
        crn_dict['x']['pct']


# In[31]:


#*******************************************************************************************
 #
 #  Function Name:  get_yattr
 #
 #  Function Description:
 #      This function retrieves the y-variable attributes.
 #
 #
 #  Return Type: string, string, string, string, string
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  n/a            n/a              n/a
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  04/27/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_yattr() -> tuple[str, str, str, str, str]: \

    return \
        crn_dict['y']['col'], \
        crn_dict['y']['subj'], \
        crn_dict['y']['cat'], \
        crn_dict['y']['lbl'], \
        crn_dict['y']['ttl'], \
        crn_dict['y']['pct']


# In[32]:


#*******************************************************************************************
 #
 #  Function Name:  get_prd_attr
 #
 #  Function Description:
 #      This function retrieves the time period attributes.
 #
 #
 #  Return Type: string, string, string
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  n/a            n/a              n/a
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  04/27/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_prd_attr() -> tuple[str, str, str]:

    return \
        tm_prd_dict['text'], \
        tm_prd_dict['start'], \
        tm_prd_dict['end']


# In[33]:


#*******************************************************************************************
 #
 #  Function Name:  get_y_enum
 #
 #  Function Description:
 #      This function retrieves y-variable enumeration data structure.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  n/a            n/a              n/a
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  04/27/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_y_enum(): return y_enum


# In[34]:


#*******************************************************************************************
 #
 #  Function Name:  x_time_series
 #
 #  Function Description:
 #      This function retreives and processes the x-variable time series.
 #
 #
 #  Return Type: series
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  string         file             The parameter is the x-variable file path.
 #  string         x                The parameter is the name of the x-variable.
 #  boolean        xcml             The parameter is the indicator that the x-value time 
 #                                  series is cumulative
 #  boolean        x_roll           The parameter is the indicator that the x-value time 
 #                                  series has had a rolling average applied to it.
 #  string         start            The parameter is the start date for the analysis.
 #  string         end              The parameter is the end date for the analysis.
 #  integer        x_roll_days      The parameter is the updated rolling average day 
 #                                  value.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  04/27/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def x_time_series \
        (file:       str,
         x:          str,
         xcml:       bool,
         xroll:      bool,
         start:      str,
         end:        str,
         xroll_days: int  = 7) \
-> pd.Series:

    x_df = pd.read_json(file, typ = 'frame')


    if xcml: xcol = 'cml_' + x.strip().lower()

    else:    xcol = x.strip().lower()


    x_series = x_df[xcol][start:end]

    x_series = dtypesx.rtn_date_idxs(x_series)


    if xroll: x_series = x_series.rolling(window = xroll_days).mean()

    return x_series


# In[35]:


#*******************************************************************************************
 #
 #  Function Name:  y_time_series_dict
 #
 #  Function Description:
 #      This function retreives and processes the y-variable time series dictionary.
 #
 #
 #  Return Type: dict
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  string         y                The parameter is the name of the y-variable.
 #  string         start            The parameter is the start date for the analysis.
 #  string         end              The parameter is the end date for the analysis.
 #  string         path             The parameter is the folder path for the y-variable 
 #                                  file.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  04/27/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def y_time_series_dict \
        (y:     str,
         start: str,
         end:   str,
         path: str = './resources/') \
-> dict:

    file_path     = path + y + '.json'

    y_tmp_df      = pd.read_json(file_path, typ = 'frame')

    y_df          = pd.DataFrame()

    for col in y_tmp_df.columns:

        y_df[col] = y_tmp_df[col][start:end]

        y_df[col] = dtypesx.rtn_date_idxs(y_df[col])


    y_dict        = y_df.to_dict(orient = 'series')

    return y_dict


# In[36]:


#*******************************************************************************************
 #
 #  Function Name:  dropna_transform_time_series_dict
 #
 #  Function Description:
 #      This function drops all nan from the time series and transforms them into 
 #      stationary time series.
 #
 #
 #  Return Type: series, dict
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  series         y                The parameter is the name of the y-variable.
 #  string         start            The parameter is the start date for the analysis.
 #  string         end              The parameter is the end date for the analysis.
 #  string         path             The parameter is the folder path for the y-variable 
 #                                  file.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  04/27/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def dropna_transform_time_series_dict \
        (x_series: pd.Series,
         y_dict:   dict,
         pct:      bool,
         vrb_bool: bool = False) \
-> tuple[pd.Series, dict]:

    comp_dict                = y_dict.copy()

    comp_dict[x_series.name] = x_series


    comp_df                  = pd.DataFrame(comp_dict).dropna()

    if pct: comp_df          = dtypesx.cnv_df_to_pct_chg(comp_df)


    trns_df                  = mathx.crct_stnry_df(comp_df.to_dict(orient = 'series'), vrb_bool = False)


    x_fnl_series             = trns_df[x_series.name]

    trns_df                  = trns_df.drop(columns = [x_series.name])

    y_fnl_dict               = trns_df.to_dict(orient = 'series')


    return x_fnl_series, y_fnl_dict


# In[37]:


#*******************************************************************************************
 #
 #  Function Name:  find_optimal_candidates
 #
 #  Function Description:
 #      This function scores x-series and a dictionary of y_series in terms of causality 
 #      and association then sorts the list in descending order as a dataframe.
 #
 #
 #  Return Type: series, dict
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  string         xfile            The parameter is the x-variable file.
 #  string         start            The parameter is the start date for the analysis.
 #  string         end              The parameter is the end date for the analysis.
 #  array          x_array          The parameter is the x-variable name array.
 #  array          y_array          The parameter is the y-variable name array.
 #  array          bool_array       The parameter is the boolean name array.
 #  boolean        pct              The parameter is the indicator that the x-value and 
 #                                  y-values time series have had a pecent change applied 
 #                                  to it.
 #  boolean        vrb_bool         The parameter is the indicator of verbosity.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  04/27/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def find_optimal_candidates \
        (xfile:      str,
         start:      str,
         end:        str,
         x_array:    np.ndarray = x_vrb_array,
         y_array:    np.ndarray = y_vrb_array,
         bool_array: np.ndarray = bool_vrb_array,
         pct:        bool       = False,
         vrb_bool:   bool       = True) \
-> pd.DataFrame:

    ttl_int \
        = len(y_array)    * \
          len(x_array)    * \
          len(bool_array) * \
          len(bool_array)

    cnt_int = 1


    results_list = []

    for y in y_array:

        for x in x_array:

            for xcml in bool_array:

                for xroll in bool_array:

                    X_series \
                        = x_time_series \
                            (file  = xfile,
                             x     = x,
                             xcml  = xcml,
                             xroll = xroll,
                             start = start,
                             end   = end)

                    y_dict \
                        = y_time_series_dict \
                            (y     = y,
                             start = start,
                             end   = end)


                    X_series, y_dict \
                        = dropna_transform_time_series_dict(X_series, y_dict, pct)

                    score, _ \
                        = mathx.score_x_vs_y_dict \
                            (X_series, y_dict, scr_pct_bool = True, vrb_bool = False)


                    result_dict \
                        = {'cuml. x':  xcml,
                           'roll. x':  xroll,
                           'pct. x':   pct,
                           'x':        x,
                           'pct. y':   pct,
                           'y':        y,
                           'score':    score}

                    results_list.append(result_dict)


                    if vrb_bool:            

                        x_tmp = x

                        if xcml:  x_tmp = 'cml_' + x_tmp

                        if xroll: x_tmp = 'roll_' + x_tmp


                        msg = f'THE SCORE FOR {x_tmp} AND {y} IS ' \
                            + f'{round(score, 2)} ({cnt_int}/{ttl_int}).\n\n'

                        logx.print_and_log_text('\033[1m' + msg + '\033[0m')


                        cnt_int += 1


    clear_output()


    scores_df       = pd.DataFrame(results_list)

    scores_df       = scores_df.sort_values(by = 'score', ascending = False)


    scores_df       = scores_df.reset_index(drop = True)

    scores_df.index = scores_df.index + 1


    return scores_df


# In[38]:


#*******************************************************************************************
 #
 #  Function Name:  find_optimal_candidates
 #
 #  Function Description:
 #      This function produces the top candidates by time period from scores.
 #
 #
 #  Return Type: dataframe
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  dataframe      scores11_df      The parameter is the full period scores dataframe.
 #  dataframe      scores12_df      The parameter is the initial shock scores dataframe.
 #  dataframe      scores13_df      The parameter is the adaptation scores dataframe.
 #  dataframe      scores14_df      The parameter is the recovery scores dataframe.
 #  dataframe      scores21_df      The parameter is the full period (%) scores dataframe.
 #  dataframe      scores22_df      The parameter is the initial shock (%) scores dataframe.
 #  dataframe      scores23_df      The parameter is the adaptation (%) scores dataframe.
 #  dataframe      scores24_df      The parameter is the recovery (%) scores dataframe.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  04/27/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def top_candidates_by_time_period_df \
        (scores11_df: pd.DataFrame,
         scores12_df: pd.DataFrame,
         scores13_df: pd.DataFrame,
         scores14_df: pd.DataFrame,
         scores21_df: pd.DataFrame,
         scores22_df: pd.DataFrame,
         scores23_df: pd.DataFrame,
         scores24_df: pd.DataFrame) \
-> pd.DataFrame:

    if scores11_df.loc[1, 'score'] >= scores21_df.loc[1, 'score']: df1 = scores11_df

    else: df1 = scores21_df

    if scores12_df.loc[1, 'score'] >= scores22_df.loc[1, 'score']: df2 = scores12_df

    else: df2 = scores22_df

    if scores13_df.loc[1, 'score'] >= scores23_df.loc[1, 'score']: df3 = scores13_df

    else: df3 = scores23_df

    if scores14_df.loc[1, 'score'] >= scores24_df.loc[1, 'score']: df4 = scores14_df

    else: df4 = scores24_df


    dfs_list  = [df1, df2, df3, df4]

    prd_list  = ['full_period', 'initial_shock', 'adaptation', 'recovery']


    top_cnd_df = pd.concat([d.iloc[[0]] for d in dfs_list], ignore_index = True)

    top_cnd_df.index = prd_list


    return top_cnd_df


# In[39]:


#*******************************************************************************************
 #
 #  Function Name:  set_coords
 #
 #  Function Description:
 #      This function sets the coordinates for matplotlib figures.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  string         code             The parameter is the figure number.
 #  string         PRD              The parameter is the analysis period.
 #  string         XCAT             The parameter is the x-axis series category.
 #  string         YCOL             The parameter is the y-axis series column name.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  04/27/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_coords(code: str, PRD: str, XCAT: str, YCOL: str):

    if code == '1.1.1':

        if PRD == '(Full Period)':

            if XCAT == 'covid_deaths%'          and YCOL == 'exchg_rts': matplotlibx.set_line_chart_legend_bbox_to_anchor(1.155, 3.48)

        elif PRD == '(Initial Shock)':

            if XCAT == 'roll_cml_covid_c&d'     and YCOL == 'stk_mkt':   matplotlibx.set_line_chart_legend_bbox_to_anchor(1.18, 3.48)

        elif PRD == '(Adaptation)':

            if XCAT == 'roll_cml_covid_deaths%' and YCOL == 'metals':    matplotlibx.set_line_chart_legend_bbox_to_anchor(1.205, 3.48)

        elif PRD == '(Recovery)':

            if XCAT == 'roll_cml_covid_c&d%'    and YCOL == 'metals':    matplotlibx.set_line_chart_legend_bbox_to_anchor(1.19, 3.48)

    elif code == '1.1.2':

        if PRD == '(Full Period)':

            if XCAT == 'covid_deaths%'          and YCOL == 'exchg_rts': matplotlibx.set_line_chart_legend_bbox_to_anchor(1.154, 3.52)

        elif PRD == '(Initial Shock)':

            if XCAT == 'roll_cml_covid_c&d'     and YCOL == 'stk_mkt':   matplotlibx.set_line_chart_legend_bbox_to_anchor(1.18, 3.52)

        elif PRD == '(Adaptation)':

            if XCAT == 'roll_cml_covid_deaths%' and YCOL == 'metals':    matplotlibx.set_line_chart_legend_bbox_to_anchor(1.205, 3.48)

        elif PRD == '(Recovery)':

            if XCAT == 'roll_cml_covid_c&d%'    and YCOL == 'metals':    matplotlibx.set_line_chart_legend_bbox_to_anchor(1.19, 3.48)

    elif code == '1.1.3.2':

        if PRD == '(Full Period)':

            if XCAT == 'covid_deaths%'          and YCOL == 'exchg_rts': matplotlibx.set_regr_eqn_coords(-2.8*(10**0), 1.6*(10**2))

        elif PRD == '(Initial Shock)':

            if XCAT == 'roll_cml_covid_c&d'     and YCOL == 'stk_mkt':   matplotlibx.set_regr_eqn_coords(-7.0*(10**2), 1.7*(10**-1))

        elif PRD == '(Adaptation)':

            if XCAT == 'roll_cml_covid_deaths%' and YCOL == 'metals':    matplotlibx.set_regr_eqn_coords(-5.2*(10**0), 1.4*(10**0))

        elif PRD == '(Recovery)':

            if XCAT == 'roll_cml_covid_c&d%'    and YCOL == 'metals':    matplotlibx.set_regr_eqn_coords(-2.5*(10**0), 1.4*(10**0))

    elif code == '1.1.3.6':

        if PRD == '(Full Period)':

            if XCAT == 'covid_deaths%'          and YCOL == 'exchg_rts': matplotlibx.set_lag_corr_annot_xyoffsets(-4.0, -0.15)

        elif PRD == '(Initial Shock)':

            if XCAT == 'roll_cml_covid_c&d'     and YCOL == 'stk_mkt':   matplotlibx.set_lag_corr_annot_xyoffsets(-4.0, 0.15)

        elif PRD == '(Adaptation)':

            if XCAT == 'roll_cml_covid_deaths%' and YCOL == 'metals':    matplotlibx.set_lag_corr_annot_xyoffsets(-5.0, 0.1)

        elif PRD == '(Recovery)':

            if XCAT == 'roll_cml_covid_c&d%'    and YCOL == 'metals':    matplotlibx.set_lag_corr_annot_xyoffsets(-2.0, 0.2)

    elif code == '1.1.4.2':

        if PRD == '(Full Period)':

            if XCAT == 'covid_deaths%'          and YCOL == 'exchg_rts': matplotlibx.set_regr_eqn_coords(-3.4*(10**0), 1.6*(10**2))

        elif PRD == '(Initial Shock)':

            if XCAT == 'roll_cml_covid_c&d'     and YCOL == 'stk_mkt':   matplotlibx.set_regr_eqn_coords(-2.95*(10**3), 1.7*(10**-1))

        elif PRD == '(Adaptation)':

            if XCAT == 'roll_cml_covid_deaths%' and YCOL == 'metals':    matplotlibx.set_regr_eqn_coords(-1.1*(10**1), 1.42*(10**0))

        elif PRD == '(Recovery)':

            if XCAT == 'roll_cml_covid_c&d%'    and YCOL == 'metals':    matplotlibx.set_regr_eqn_coords(-5.0*(10**0), 1.45*(10**0))

    elif code == '1.1.4.6':

        if PRD == '(Full Period)':

            if XCAT == 'covid_deaths%'          and YCOL == 'exchg_rts': matplotlibx.set_lag_corr_annot_xyoffsets(-4.2, 0.28)

        elif PRD == '(Initial Shock)':

            if XCAT == 'roll_cml_covid_c&d'     and YCOL == 'stk_mkt':   matplotlibx.set_lag_corr_annot_xyoffsets(-2.8, -0.18)

        elif PRD == '(Adaptation)':

            if XCAT == 'roll_cml_covid_deaths%' and YCOL == 'metals':    matplotlibx.set_lag_corr_annot_xyoffsets(-2.0, 0.25)

        elif PRD == '(Recovery)':

            if XCAT == 'roll_cml_covid_c&d%'    and YCOL == 'metals':    matplotlibx.set_lag_corr_annot_xyoffsets(-2.0, 0.25)

    elif code == '1.1.5.2':

        if PRD == '(Full Period)':

            if XCAT == 'covid_deaths%'          and YCOL == 'exchg_rts': matplotlibx.set_regr_eqn_coords(-2.5*(10**0), 2.2*(10**2))

        elif PRD == '(Initial Shock)':

            if XCAT == 'roll_cml_covid_c&d'     and YCOL == 'stk_mkt':   matplotlibx.set_regr_eqn_coords(-5.9*(10**2), 1.7*(10**-1))

        elif PRD == '(Adaptation)':

            if XCAT == 'roll_cml_covid_deaths%' and YCOL == 'metals':    matplotlibx.set_regr_eqn_coords(-7.9*(10**0), 1.42*(10**0))

        elif PRD == '(Recovery)':

            if XCAT == 'roll_cml_covid_c&d%'    and YCOL == 'metals':    matplotlibx.set_regr_eqn_coords(-6.0*(10**0), 1.9*(10**0))

    elif code == '1.1.5.6':

        if PRD == '(Full Period)':

            if XCAT == 'covid_deaths%'          and YCOL == 'exchg_rts': matplotlibx.set_lag_corr_annot_xyoffsets(-4.2, -0.28)

        elif PRD == '(Initial Shock)':

            if XCAT == 'roll_cml_covid_c&d'     and YCOL == 'stk_mkt':   matplotlibx.set_lag_corr_annot_xyoffsets(-3.0, -0.18)

        elif PRD == '(Adaptation)':

            if XCAT == 'roll_cml_covid_deaths%' and YCOL == 'metals':    matplotlibx.set_lag_corr_annot_xyoffsets(-2.0, 0.25)

        elif PRD == '(Recovery)':

            if XCAT == 'roll_cml_covid_c&d%'    and YCOL == 'metals':    matplotlibx.set_lag_corr_annot_xyoffsets(-2.0, 0.25)

    elif code == '1.1.6.2':

        if PRD == '(Full Period)':

            if XCAT == 'covid_deaths%'          and YCOL == 'exchg_rts': matplotlibx.set_regr_eqn_coords(-1.4*(10**0), 2.2*(10**2))

        elif PRD == '(Initial Shock)':

            if XCAT == 'roll_cml_covid_c&d'     and YCOL == 'stk_mkt':   matplotlibx.set_regr_eqn_coords(-1.2*(10**3), 1.7*(10**-1))

        elif PRD == '(Adaptation)':

            if XCAT == 'roll_cml_covid_deaths%' and YCOL == 'metals':    matplotlibx.set_regr_eqn_coords(-1.2*(10**1), 0.85*(10**0))

        elif PRD == '(Recovery)':

            if XCAT == 'roll_cml_covid_c&d%'    and YCOL == 'metals':    matplotlibx.set_regr_eqn_coords(-13.0*(10**0), 1.4*(10**0))

    elif code == '1.1.6.6':

        if PRD == '(Full Period)':

            if XCAT == 'covid_deaths%'          and YCOL == 'exchg_rts': matplotlibx.set_lag_corr_annot_xyoffsets(-8.0, 0.3)

        elif PRD == '(Initial Shock)':

            if XCAT == 'roll_cml_covid_c&d'     and YCOL == 'stk_mkt':   matplotlibx.set_lag_corr_annot_xyoffsets(-3.0, -0.2)

        elif PRD == '(Adaptation)':

            if XCAT == 'roll_cml_covid_deaths%' and YCOL == 'metals':    matplotlibx.set_lag_corr_annot_xyoffsets(-3.0, 0.1)

        elif PRD == '(Recovery)':

            if XCAT == 'roll_cml_covid_c&d%'    and YCOL == 'metals':    matplotlibx.set_lag_corr_annot_xyoffsets(-2.0, 0.2)

    elif code == '1.1.7.2':

        if PRD == '(Full Period)':

            if XCAT == 'covid_deaths%'          and YCOL == 'exchg_rts': matplotlibx.set_regr_eqn_coords(-3.7*(10**1), 2.2*(10**2))

        elif PRD == '(Initial Shock)':

            if XCAT == 'roll_cml_covid_c&d'     and YCOL == 'stk_mkt':   matplotlibx.set_regr_eqn_coords(-1.8*(10**2), 1.7*(10**-1))

        elif PRD == '(Adaptation)':

            if XCAT == 'roll_cml_covid_deaths%' and YCOL == 'metals':    matplotlibx.set_regr_eqn_coords(-1.1*(10**1), 1.41*(10**0))

        elif PRD == '(Recovery)':

            if XCAT == 'roll_cml_covid_c&d%'    and YCOL == 'metals':    matplotlibx.set_regr_eqn_coords(-5.0*(10**0), 1.9*(10**0))

    elif code == '1.1.7.6':

        if PRD == '(Full Period)':

            if XCAT == 'covid_deaths%'          and YCOL == 'exchg_rts': matplotlibx.set_lag_corr_annot_xyoffsets(-3.5, -0.3)

        elif PRD == '(Initial Shock)':

            if XCAT == 'roll_cml_covid_c&d'     and YCOL == 'stk_mkt':   matplotlibx.set_lag_corr_annot_xyoffsets(-3.0, -0.18)

        elif PRD == '(Adaptation)':

            if XCAT == 'roll_cml_covid_deaths%' and YCOL == 'metals':    matplotlibx.set_lag_corr_annot_xyoffsets(-2.0, 0.25)

        elif PRD == '(Recovery)':

            if XCAT == 'roll_cml_covid_c&d%'    and YCOL == 'metals':    matplotlibx.set_lag_corr_annot_xyoffsets(-2.0, 0.25)


# In[ ]:




