#!/usr/bin/env python
# coding: utf-8

# In[1]:


#*******************************************************************************************
 #
 #  File Name:  assetx.py
 #
 #  File Description:
 #      This Python script, assetx.py, contains generic data structures and Python 
 #      functions for querying for and processing asset prices.
 #      Here is the list:
 #
 #  get_date_range
 #  set_date_range
 #
 #  rtn_new_date
 #
 #  rtn_prices
 #  rtn_cmdt_prices
 #  rtn_shares
 #  rtn_who_covid_data
 #  rtn_covid_cntry_df
 #  rtn_covid_cntry_file_df
 #
 #  rtn_sec_tickers
 #  rtn_all_symbols_array
 #  rtn_all_symbols_file_array
 #  rtn_sector_symbols_array
 #  rtn_sector_symbols_file_array
 #
 #  rtn_sector_cmps_df
 #  rtn_geo_coords
 #
 #  rtn_norm_shares_to_prices
 #  rtn_mrkt_cap
 #
 #  fmt_addr
 #  rtn_addr
 #
 #  rtn_cmp_name
 #  rtn_cmp_industry
 #  
 #  rtn_cmps_info_df
 #  rtn_cmps_info_file_df
 #  rtn_industry_stats_summary
 #  rtn_sctr_mrkt_idx
 #  rtn_sctr_mrkt_idx_file
 #  rtn_geo_df
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/13/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

import dtypesx
import logx

import os
import copy
import requests

import datetime as dt
import numpy    as np
import pandas   as pd
import yfinance as yf

from econ_api               import geoapify_key

from datetime               import datetime, timedelta
from dateutil.relativedelta import relativedelta
from enum                   import Enum, auto
from geopy.geocoders        import Nominatim
from openbb                 import obb
from operator               import itemgetter
from io                     import StringIO


# In[2]:


CONSTANT_LOCAL_FILE_NAME = 'assetx.py'


# In[3]:


class price_type_enum(Enum):
    def _generate_next_value_(name, start, count, last_values):
        return count

    OPEN   = auto()

    HIGH   = auto()

    LOW    = auto()

    CLOSE  = auto()

    VOLUME = auto()


# In[4]:


config_dict \
    = {'url':   {'who':              'https://storage.googleapis.com/covid19-open-data/v3/epidemiology.csv',
                 'geoapify':         'https://api.geoapify.com/v1/geocode/search?text=',
                 'sec':              'https://www.sec.gov/files/company_tickers.json'},
       'file':   {'agr1':            './resources/agr1.json',
                  'agr2':            './resources/agr2.json',
                  'exchg_rts':       './resources/exchg_rts.json',
                  'intrt_rts':       './resources/intrt_rts.json',
                  'metals':          './resources/metals.json',
                  'petrol':          './resources/petrol.json',
                  'petrol_plus':     './resources/petrol_plus.json',
                  'stk_mkt':         './resources/stk_mkt.json',
                  'covid_usa':       './resources/covid_usa.json',
                  'cmps':            './resources/cmps.json',
                  'all_stcks':       './resources/all_stcks.json',
                  'sctr_stcks':      './resources/sctr_stcks.json',
                  'all_mdn':         './resources/all_mdn_wgts.json',
                  'top_mdn':         './resources/top_mdn_wgts.json',
                  'opt_fll_prd':     './resources/opt_fll_prd.json',
                  'opt_int_shk':     './resources/opt_int_shk.json',
                  'opt_adp':         './resources/opt_adp.json',
                  'opt_rec':         './resources/opt_rec.json',
                  'opt_fll_prd_pct': './resources/opt_fll_prd_pct.json',
                  'opt_int_shk_pct': './resources/opt_int_shk_pct.json',
                  'opt_adp_pct':     './resources/opt_adp_pct.json',
                  'opt_rec_pct':     './resources/opt_rec_pct.json',
                  'opt_fnl_cnd':     './resources/opt_fnl_cnd.json',
                  'cmp_idx':         'company_id',
                  'date_idx':        'date',
                  'srch':            'oil'},
       'yahoo':  {'shr_out':         'sharesOutstanding'},
       'openbb': {'shr_out':         'shares_outstanding',
                  'tkr_prov':        'sec',
                  'provider':        'yfinance'},
       'sec':    {'tkr':             'ticker',
                  'headers':         {'User-Agent':      'MyResearchFirm research@mycompany.com',
                                      'Accept-Encoding': 'gzip, deflate'}},
       'date':   {'start':           '2020-01-22',
                  'end':             '2022-09-14',
                  'format':          '%Y-%m-%d'},
       'precision':                  2,
       'exclude_industry':           [],
       'invalid_symbols': \
           ['AACO',   'ACAA',  'ACGC',  'ADBT',  'AESI', 
            'AERGP',  'AFNX',  'AIB',   'AIST',  'ALOV', 
            'ALTUF',  'AMAN',  'AMBI',  'APC',   'APN', 
            'APUR',   'APXC',  'AUGG',  'AVAT',  'AVAX', 
            'AVEX',   'AZULQ', 'BAGZ',  'BANL',  'BAVA', 
            'BKFDF',  'BKV',   'BMOK',  'BRLL',  'BROXF', 
            'BSTT',   'BTAB',  'BUHPY', 'BVENY', 'BXDIF', 
            'BWIV',   'CAEA',  'CEHCF', 'CLBR',  'CLSO', 
            'CMCAW',  'CNVEF', 'CPPBY', 'CRCE',  'CTAA', 
            'CTPUF',  'CTTRF', 'CYAB',  'DBCA',  'DETX', 
            'DGAC',   'DLXY',  'ENBHF', 'ENBMF', 'ENBNF', 
            'ENBRF',  'EOHC',  'ETHB',  'ETHB',  'ETSS', 
            'EUEV',   'EYUBY', 'EXYN',  'FGHFF', 'FGO', 
            'FGXC',   'FHLD',  'FLOC',  'FRVO',  'FTW', 
            'FXAC',   'GACW',  'GADA',  'GBNB',  'GCGJ', 
            'GEHDF',  'GFSAY', 'GLED',  'GLND',  'GHYP', 
            'HACQ',   'HBAR',  'HCIIP', 'HCYC',  'HHHEF', 
            'HMH',    'HONA',  'HQBB',  'IACQ',  'IDAC', 
            'INNP',   'INR',   'IPFX',  'IRAB',  'JEQ', 
            'KGS',    'KPET',  'KPHMW', 'KRAQ',  'KUKE', 
            'LB',     'LBKX',  'LPSL',  'LSE',   'LTGR', 
            'MADL',   'MCAH',  'MDCOY', 'MEON',  'METRY', 
            'MEVO',   'MLAA',  'MNR',   'MPLXP', 'MSBT', 
            'MSMU',   'MTAL',  'MTVE',  'MZYX',  'NAFS', 
            'NBBI',   'NCLA',  'NESR',  'NEUE',  'NHIV', 
            'NINE',   'NZEOY', 'OHAC',  'OKMN',  'OMSE', 
            'OPTH',   'OTAI',  'OXYWS', 'PAEXY', 'PALO', 
            'PAXG',   'PGIM',  'PHD',   'PHDWY', 'PLUN',  
            'PMVC',   'PRAG',  'PSUS',  'PTIXW', 'PTNT', 
            'PTOR',   'PTXAF', 'PWRL',  'PWRU',  'QADR', 
            'QLEP',   'QMLS',  'QRED',  'RACC',  'RADB', 
            'RBNE',   'RFAM',  'RGGG',  'RNBW',  'RNGOF', 
            'RREV',   'RVI',   'SAAQ',  'SDRL',  'SECZ', 
            'SERPY',  'SHMLF', 'SKAI',  'SKYQ',  'SOBO', 
            'SORN',   'SSAC',  'STAK',  'STHRF', 'SUMA', 
            'SUNC',   'SVIV',  'TBN',   'TBNRL', 'TCEYF', 
            'TDSPRU', 'TIXT',  'TMDE',  'TMRD',  'TORO', 
            'TPET',   'TRAX',  'TRBG',  'TREO',  'TRGS', 
            'TRLEF',  'TRMOY', 'TRPEF', 'TVIV',  'TXO', 
            'UNID',   'UNIU',  'UNTC',  'UNXP',  'VAII', 
            'VARRY',  'VEST',  'VG',    'VGNT',  'VIRX', 
            'VTS',    'WBI',   'WENC',  'WINTW', 'WLII', 
            'WNS',    'WPAC',  'WRPT',  'XCBE',  'XFLH', 
            'XSLL',   'XXAAU', 'YIFE',  'YSWY',  'ZEFIF'],
       'mrkt_cap_cols': \
           ['symbol',          'company_name',
            'industry',        'address',
            'longitude',       'latitude',
            'min_market_cap',  'max_market_cap',
            'mean_market_cap', 'median_market_cap',
            'std_market_cap',  'sem_market_cap'],
       'price_type': \
           ['open', 'high', 'low', 'close', 'volume']}

symbols_dict \
    = {'agriculture': {'cocoa':           'CC=F',
                       'coffee':          'KC=F',
                       'corn':            'ZC=F',
                       'oats':            'ZO=F',
                       'orange_juice':    'OJ=F',
                       'rice':            'ZR=F',
                       'soybeans':        'ZS=F',
                       'sugar':           'SB=F',
                       'wheat':           'KE=F',
                       'live_cattle':     'LE=F'},
       'currencies':  {'eur':             'EURUSD=X',
                       'gpb':             'GBPUSD=X',
                       'chf':             'CHFUSD=X',
                       'aud':             'AUDUSD=X',
                       'cad':             'CADUSD=X',
                       'sgd':             'SGDUSD=X',
                       'bitcoin':         'BTC-USD'},
       'indices':     {'sp500':           '^GSPC',
                       'djia':            '^DJI',
                       'nasdaq':          '^IXIC',
                       'nyse':            '^NYA',
                       'russell':         '^RUT'},
       'metals':      {'gold':            'GC=F',
                       'silver':          'SI=F',
                       'platinum':        'PL=F',
                       'palladium':       'PA=F',
                       'copper':          'SI=F'},
       'petroleum':   {'brent_crude_oil': 'BZ=F',
                       'crude_oil_wti':   'CL=F',
                       'rbob_gasoline':   'RB=F',
                       'heating_oil':     'HO=F',
                       'natural_gas':     'NG=F'},
       'yields':      {'treas_bond':      'ZB=F',
                       'treas_5_year':    '^FVX',
                       'treas_10_year':   'ZN=F',
                       'treas_30_year':   '^TYX',
                       'cboe':            '^TNX'}}

covid_rename_cols_dict \
    = {'new_confirmed':        'covid_cases',
       'new_deceased':         'covid_deaths',
       'new_combined':         'covid_c&d',
       'cumulative_confirmed': 'cml_covid_cases',
       'cumulative_deceased':  'cml_covid_deaths',
       'cumulative_combined':  'cml_covid_c&d'}


# In[5]:


#*******************************************************************************************
 #
 #  Function Name:  get_date_range
 #
 #  Function Description:
 #      This function returns the global values for the start and end dates 
 #      for the analysis.
 #
 #
 #  Return Type: string, string
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
 #  02/13/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/ 

def get_date_range() -> tuple[str, str]:

    return config_dict['date']['start'], config_dict['date']['end']


# In[6]:


#*******************************************************************************************
 #
 #  Function Name:  set_date_range
 #
 #  Function Description:
 #      This function sets the global values for the start and end dates 
 #      for the analysis.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  string         start            The parameter is the start date with the format, 
 #                                  yyyy-mm-dd.
 #  string         end              The parameter is the start date with the format, 
 #                                  yyyy-mm-dd.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/13/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/ 

def set_date_range(start: str, end: str):

    global config_dict

    config_dict['date']['start'] = start

    config_dict['date']['end']   = end


# In[7]:


#*******************************************************************************************
 #
 #  Function Name:  rtn_new_date
 #
 #  Function Description:
 #      This function returns the global values for the start and end dates for the 
 #      analysis.
 #
 #
 #  Return Type: string
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  string         date             The parameter is the input date.
 #  string         fmt              The parameter is the date format.
 #  integer        months           The parameter is the offset in months.
 #  integer        years            The parameter is the offset in years.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/13/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def rtn_new_date \
        (date:   str, 
         fmt:    str, 
         days:   int = 0, 
         months: int = 0, 
         years:  int = 0) \
-> str:

    date_obj = datetime.strptime(date, fmt)


    days_int = int(days)

    mths_int = int(months)

    yrs_int  = int(years)


    new_date_obj = date_obj


    if days_int != 0:   new_date_obj += relativedelta(days   = days_int)

    if months_int != 0: new_date_obj += relativedelta(months = mths_int)

    if years_int != 0:  new_date_obj += relativedelta(years  = yrs_int) 


    new_date = new_date_obj.strftime(fmt)


    return new_date


# In[8]:


#*******************************************************************************************
 #
 #  Function Name:  rtn_prices
 #
 #  Function Description:
 #      This function receives symbol parameters and returns prices.
 #
 #
 #  Return Type: series
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  string         symbol           The parameter is the asset symbol.
 #  string         price_type       The parameter is the price type (high, low, etc.)
 #  object         stock_obj        The parameter is the yahoo stock object.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/13/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/ 

def rtn_prices \
        (symbol:     str,
         price_type: str = config_dict['price_type'][price_type_enum.CLOSE.value],
         stock_obj:  object = None) \
-> pd.Series:

    if stock_obj is None: 

        try: 

            pr_series \
                = obb.equity.price.historical \
                    (symbol     = symbol,
                     start_date = config_dict['date']['start'],
                     end_date   = config_dict['date']['end'],
                     provider   = config_dict['openbb']['provider']) \
                        .to_df()[price_type]

        except: 

            try:

                stock_obj = yf.Ticker(symbol)

                adj_end_date \
                    = rtn_new_date \
                        (config_dict['date']['end'], 
                         config_dict['date']['format'], 
                         days_int = 1)

                pr_series \
                    = stock_obj.history \
                        (start = config_dict['date']['start'], 
                         end   = adj_end_date) \
                            [price_type.title()]

            except: pr_series = None

    else:

        try:

            adj_end_date \
                = rtn_new_date \
                    (config_dict['date']['end'], 
                     config_dict['date']['format'], 
                     days_int = 1)

            pr_series \
                = stock_obj.history \
                    (start = config_dict['date']['start'], 
                     end   = adj_end_date) \
                        [price_type.title()]

        except:

            try:

                pr_series \
                    = obb.equity.price.historical \
                        (symbol     = symbol,
                         start_date = config_dict['date']['start'],
                         end_date   = config_dict['date']['end'],
                         provider   = config_dict['openbb']['provider']) \
                            .to_df()[price_type]

            except: pr_series = None


    try:

        if pr_series is not None and len(pr_series) > 0:

            pr_series = dtypesx.rtn_date_idxs(pr_series)

            pr_series = dtypesx.rtn_series_with_unq_idxs(pr_series)

            pr_series = pr_series.astype(float).round(config_dict['precision'])

        else: pr_series = None

    except: pr_series = None


    if pr_series is not None:

        pr_start_date \
            = datetime.strptime \
                (config_dict['date']['start'], 
                 config_dict['date']['format']) \
                    .date()

        pr_end_date \
            = datetime.strptime \
                (config_dict['date']['end'], 
                 config_dict['date']['format']) \
                    .date()


        if pr_series.index[0] == pr_start_date \
            and pr_series.index[len(pr_series.index) - 1] == pr_end_date:

            return pr_series

        else: return None


    return pr_series


# In[9]:


#*******************************************************************************************
 #
 #  Function Name:  rtn_cmdt_prices
 #
 #  Function Description:
 #      This function receives commodity parameters and returns historical prices.
 #
 #
 #  Return Type: series
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  string         asset_type       The parameter is the asset type and key for symbol 
 #                                  dictionary.
 #  string         commodity        The parameter is the commodity name.
 #  string         price_type       The parameter is the price type (high, low, etc.)
 #  object         stock_obj        The parameter is the yahoo stock object.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/13/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/ 

def rtn_cmdt_prices \
        (asset_type: str,
         commodity:  str,
         price_type: str = config_dict['price_type'][price_type_enum.CLOSE.value],
         stock_obj:  object = None) \
-> pd.Series:

    if symbols_dict.get(asset_type) is not None \
        and symbols_dict[asset_type].get(commodity) is not None:

        symbol = symbols_dict[asset_type][commodity]


        pr_series = rtn_prices(symbol, price_type, stock_obj)

        if pr_series is not None:

            pr_series = pr_series.rename(commodity.lower())

            return pr_series


    return None


# In[10]:


#*******************************************************************************************
 #
 #  Function Name:  rtn_shares
 #
 #  Function Description:
 #      This function receives symbol parameters and returns historical outstanding shares.
 #
 #
 #  Return Type: series
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  string         symbol           The parameter is the asset symbol.
 #  object         stock_obj        The parameter is the yahoo stock object.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/13/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/ 

def rtn_shares \
        (symbol:    str,
         stock_obj: object = None) \
-> pd.Series:

    if stock_obj is None:

        try: stock_obj = yf.Ticker(symbol)

        except: stock_obj = None


    if stock_obj is not None:

        try: 

            sh_series \
                = stock_obj.get_shares_full \
                    (start = config_dict['date']['start'], 
                     end = config_dict['date']['end'])

        except: 

            try:

                sh_int = stock_obj.info[config_dict['yahoo']['shr_out']]

                pr_series = rtn_prices(symbol, stock_obj = stock_obj)

                sh_series = pd.Series([sh_int], index = [pr_series.index[0]])

            except:

                try:

                    sh_flt \
                        = obb.equity.profile \
                            (symbol = symbol, 
                             provider = config_dict['openbb']['provider']) \
                                .to_df()[config_dict['openbb']['shr_out']] \
                                .iloc[0]

                    pr_series = rtn_prices(symbol, stock_obj = stock_obj)

                    sh_series = pd.Series([sh_int], index = [pr_series.index[0]])

                except: return None

    else:

        try:

            shares_flt \
                = obb.equity.profile \
                    (symbol = symbol, 
                     provider = config_dict['openbb']['provider']) \
                        .to_df()[config_dict['openbb']['shr_out']] \
                        .iloc[0]

            pr_series = rtn_prices(symbol, stock_obj = stock_obj)

            sh_series = pd.Series([sh_int], index = [pr_series.index[0]])

        except: return None


    if sh_series is not None and len(sh_series) > 0:

        sh_series = dtypesx.rtn_date_idxs(sh_series)

        sh_series = dtypesx.rtn_series_with_unq_idxs(sh_series)

        sh_series = sh_series.astype(float).round(0)


        return sh_series

    else: return None


# In[11]:


#*******************************************************************************************
 #
 #  Function Name:  rtn_who_covid_data
 #
 #  Function Description:
 #      This function uses an WHO API to transfer all available COVID-19 Data
 #      for all countries into a dataframe, which the function returns to the
 #      caller.
 #
 #
 #  Return Type: dataframe
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
 #  02/16/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def rtn_who_covid_data() -> pd.DataFrame:

    who_covid_file_path = StringIO(requests.get(config_dict['url']['who']).text)

    who_covid_df = pd.read_csv(who_covid_file_path)

    return who_covid_df


# In[12]:


#*******************************************************************************************
 #
 #  Function Name:  rtn_covid_cntry_df
 #
 #  Function Description:
 #      This function uses an WHO API to transfer all available COVID-19 Data
 #      for all countries into a dataframe before extracting new cases and deaths
 #      for a particular country.
 #
 #
 #  Return Type: dataframe
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  series         idx_series       The parameter is the series with the target index.
 #  string         cntry            The parameter is the target country abbreviation.
 #  string         idx_col          The parameter is the index column in the output file.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/16/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def rtn_covid_cntry_df \
        (idx_series: pd.Series = None, 
         cntry:      str       = None, 
         idx_col:    str       = 'date') \
-> pd.DataFrame:

    wrld_df = rtn_who_covid_data()


    if cntry is not None:

        cntry_df = wrld_df.apply(lambda x: x[wrld_df['location_key'].isin([cntry])])

    else: cntry_df = wrld_df.copy()


    cntry_df[idx_col] \
        = cntry_df[idx_col] \
            .apply(lambda x: datetime.strptime(x, config_dict['date']['format']).date())


    if idx_series is not None:

        cntry_df \
            = cntry_df.apply \
                (lambda x: x[cntry_df[idx_col].isin(idx_series.index.to_numpy())])


    cntry_df \
        = cntry_df \
            .set_index \
                (idx_col, 
                 drop = True, 
                 append = False, 
                 verify_integrity = False)

    cntry_df \
        = cntry_df \
            [['new_confirmed', 
              'new_deceased', 
              'cumulative_confirmed', 
              'cumulative_deceased']]


    cntry_df['new_confirmed'] \
        = cntry_df.apply(lambda x: abs(x['new_confirmed']), axis = 1).astype(int)

    cntry_df['new_deceased'] \
        = cntry_df.apply(lambda x: abs(x['new_deceased']), axis = 1).astype(int)

    cntry_df['cumulative_confirmed'] \
        = cntry_df.apply(lambda x: abs(x['cumulative_confirmed']), axis = 1).astype(int)

    cntry_df['cumulative_deceased'] \
        = cntry_df.apply(lambda x: abs(x['cumulative_deceased']), axis = 1).astype(int)


    cntry_df['new_combined'] \
        = cntry_df['new_confirmed'] + cntry_df['new_deceased']

    cntry_df['cumulative_combined'] \
        = cntry_df['cumulative_confirmed'] + cntry_df['cumulative_deceased']


    cntry_df \
        = cntry_df \
            [['new_confirmed', 
              'new_deceased',
              'new_combined',
              'cumulative_confirmed',
              'cumulative_deceased',
              'cumulative_combined']]

    cntry_df = cntry_df.rename(columns = covid_rename_cols_dict)


    return cntry_df


# In[13]:


#*******************************************************************************************
 #
 #  Function Name:  rtn_covid_cntry_file_df
 #
 #  Function Description:
 #      This function uses an WHO API to transfer all available COVID-19 Data
 #      for all countries into a dataframe before extracting new cases and deaths
 #      for a particular country but attempts to extract the information from an
 #      existing file first.
 #
 #
 #  Return Type: dataframe
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  string         file_path        The parameter is the file path to the input file.
 #  string         cntry            The parameter is the target country abbreviation.
 #  series         comp_idx_series  The parameter is the series with the comparison index.
 #  string         idx_col          The parameter is the index column in the output file.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/16/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def rtn_covid_cntry_file_df \
        (file_path:       str,
         cntry:           str       = 'US',
         comp_idx_series: pd.Series = None,
         idx_col:         str       = 'date') \
-> pd.DataFrame:

    file_exists_bool   = os.path.exists(file_path)

    if not file_exists_bool: 

        covid_df       = rtn_covid_cntry_df(comp_idx_series, cntry).dropna()


        idx_series     = covid_df.iloc[:, 0]

        idx_series     = dtypesx.rtn_date_idxs(idx_series)


        covid_df.index = idx_series.index.to_numpy()

        covid_df.to_json(file_path, mode = 'w')

    else:

        covid_df       = pd.read_json(file_path)


        idx_series     = covid_df.iloc[:, 0]

        idx_series     = dtypesx.rtn_date_idxs(idx_series)


        covid_df.index = idx_series.index.to_numpy()


    return covid_df


# In[14]:


#*******************************************************************************************
 #
 #  Function Name:  rtn_sec_tickers
 #
 #  Function Description:
 #      This function retrieves a list of stock tickers from the SEC.
 #
 #
 #  Return Type: list
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
 #  02/16/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def rtn_sec_tickers() -> list:

    response \
        = requests.get \
            (config_dict['url']['sec'], 
             headers = config_dict['sec']['headers'])

    response.raise_for_status() 


    data = response.text.strip()

    if data.startswith("{") and data.endswith("}"):

        cleaned_data   = "[" + data[1:-1] + "]"

    else: cleaned_data = data


    sec_series \
        = pd.read_json \
            (StringIO(cleaned_data)) \
                .transpose() \
                    [config_dict['sec']['tkr']]

    sec_list = sec_series.tolist()

    return sec_list


# In[15]:


#*******************************************************************************************
 #
 #  Function Name:  rtn_all_symbols_array
 #
 #  Function Description:
 #      This function creates a list of symbols for all publically traded companies
 #      recognized by the SEC. The function sorts the list alphabetically and removes
 #      any redundancies before returning the list to the caller.
 #
 #
 #  Return Type: array
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
 #  02/16/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def rtn_all_symbols_array() -> np.ndarray:

    try:

        symbols_list = rtn_sec_tickers()

    except:

        symbols_obj \
            = obb.equity.search \
                (query = '', 
                 provider = config_dict['openbb']['tkr_prov'])

        symbols_list = symbols_obj.to_df()['symbol'].tolist()


    symbols_list = [str(x).strip() for x in symbols_list]

    symbols_list = [x.upper() for x in symbols_list if x.isalpha()]

    symbols_list = list(set(symbols_list) - set(config_dict['invalid_symbols']))

    symbols_list = sorted(symbols_list)


    symbols_array = np.asarray(symbols_list, dtype = str)

    return symbols_array


# In[16]:


#*******************************************************************************************
 #
 #  Function Name:  rtn_all_symbols_file_array
 #
 #  Function Description:
 #      This function creates a list of symbols for all publically traded companies
 #      recognized by the SEC but attempts to extract the information from an existing 
 #      file first. The function sorts the list alphabetically and removes any redundancies 
 #      before returning the list to the caller.
 #
 #
 #  Return Type: array
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  string         file_path        The parameter is the file path to the input file.
 #  string         idx_col          The parameter is the index column in the output file.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/16/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def rtn_all_symbols_file_array \
        (file_path: str, 
         idx_col:   str = 'index') \
-> np.ndarray:

    file_exists_bool = os.path.exists(file_path)


    if not file_exists_bool: 

        data_array   = rtn_all_symbols_array()

        pd.Series(data_array).to_json(file_path, mode = 'w')

    else: data_array = pd.read_json(file_path, typ = 'series').to_numpy()


    return data_array


# In[17]:


#*******************************************************************************************
 #
 #  Function Name:  rtn_sector_symbols_array
 #
 #  Function Description:
 #      This function returns only those stock symbols for the industry related to the
 #      search industry.
 #
 #
 #  Return Type: array
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  object         input_obj        The parameter is the list of symbols for publically 
 #                                  traded companies.
 #  string         search_sector    The parameter is the name of the search industry in 
 #                                  lowercase.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/17/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/ 

def rtn_sector_symbols_array \
        (input_obj:     object, 
         search_sector: str) \
-> np.ndarray:

    stock_array  = dtypesx.cnv_data_to_array(input_obj)

    srch_sctr    = search_sector.lower()

    sector_array = np.asarray([], dtype = str)


    for symbol in stock_array:

        try:

            industry \
                = obb.equity.profile \
                    (symbol = symbol) \
                        .to_df()['industry_category'] \
                            .iloc[0] \
                            .lower()

        except:

            try:

                stock_obj = yf.Ticker(symbol)

                industry = stock_obj.info['industry'].lower()

            except: continue


        if industry not in config_dict['exclude_industry'] \
            and industry.find(srch_sctr) >= 0:

            try:

                pr_prices = rtn_prices(symbol)

                sh_prices = rtn_shares(symbol)


                if pr_prices is not None \
                    and sh_prices is not None:

                    sector_array = np.append(sector_array, symbol)

                    logx.print_and_log_text \
                        (f'\nStock symbol, {symbol}, is in industry: {industry}\n')

            except: continue


    return sector_array


# In[18]:


#*******************************************************************************************
 #
 #  Function Name:  rtn_sector_symbols_file_array
 #
 #  Function Description:
 #      This function returns only those stock symbols for the industry related to the
 #      search industry but attempts to extract the information from an existing file
 #      first.
 #
 #
 #  Return Type: array
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  string         symbol_array     The parameter is an array of stock symbols.
 #  string         search_sector    The parameter is the name of the search industry in 
 #                                  lowercase.
 #  string         file_path        The parameter is the file path to the input file.
 #  string         idx_col          The parameter is the index column in the output file.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/17/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/ 

def rtn_sector_symbols_file_array \
        (symbol_array:  np.ndarray,
         search_sector: str,
         file_path:     str, 
         idx_col:       str = 'index') \
-> np.ndarray:

    file_exists_bool = os.path.exists(file_path)


    if not file_exists_bool:

        data_array = rtn_sector_symbols_array(symbol_array, search_sector)

        pd.Series(data_array).to_json(file_path, mode = 'w')

    else: data_array = pd.read_json(file_path, typ = 'series').to_numpy()


    return data_array


# In[19]:


#*******************************************************************************************
 #
 #  Function Name:  rtn_geo_coords
 #
 #  Function Description:
 #      This function returns the longitude and latitude based on an address.
 #
 #
 #  Return Type: float, float
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  string         address          The parameter is the address.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/17/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/ 

def rtn_geo_coords(address: str) -> tuple[float, float]:

    url = config_dict['url']['geoapify'] + f'{address}&apiKey={geoapify_key}'

    try:

        response       = requests.get(url)

        info_dict      = response.json()


        lng_flt        = info_dict['features'][0]['properties']['lon']

        lat_flt        = info_dict['features'][0]['properties']['lat']

    except:

        try:

            geolocator = Nominatim(user_agent = 'openbb_app')

            location   = geolocator.geocode(address)


            lng_flt    = location.longitude

            lat_flt    = location.latitude

        except:

            lng_flt    = None

            lat_flt    = None


    return lng_flt, lat_flt


# In[20]:


#*******************************************************************************************
 #
 #  Function Name:  rtn_norm_shares_to_prices
 #
 #  Function Description:
 #      This function normalizes a series of shares to match a series of prices
 #      through alignment and interpolation.
 #
 #
 #  Return Type: series
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  series         pr_series        The parameter is the prices series.
 #  series         sh_series        The parameter is the shares series.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/17/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/ 

def rtn_norm_shares_to_prices \
        (pr_series: pd.Series, 
         sh_series: pd.Series) \
-> pd.Series:

    sh1_series       = sh_series.dropna()

    if sh1_series.count() == 0: return None


    if sh1_series.count() == 1: 

        sh2_series   = (pr_series * 0.0) + sh1_series.iloc[0]

        sh2_series   = dtypesx.rtn_series_aligned_with_target(sh2_series, pr_series)

    else: sh2_series = dtypesx.rtn_series_aligned_with_target(sh1_series, pr_series)


    return sh2_series


# In[21]:


#*******************************************************************************************
 #
 #  Function Name:  rtn_mrkt_cap
 #
 #  Function Description:
 #      This function returns a company's market capitalization.
 #
 #
 #  Return Type: series
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  string         symbol           The parameter is the company's trading symbol.
 #  object         stock_obj        The parameter is the yahoo information object.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/17/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/ 

def rtn_mrkt_cap \
        (symbol:    str, 
         stock_obj: object = None) \
-> pd.Series:

    try:

        pr_series  = rtn_prices(symbol, stock_obj = stock_obj)

        sh1_series = rtn_shares(symbol, stock_obj = stock_obj)

    except: return None


    try:

        sh_series  = rtn_norm_shares_to_prices(pr_series, sh1_series)

    except: 

        logx.print_and_log_text \
            (f'\nThe shares for symbol {symbol} could not be normalized...\n')

        return None


    if pr_series.count() == sh_series.count():

        if list(pr_series.index) == list(sh_series.index):

            mrkt_cap_list \
                = list \
                    (map \
                        (lambda x, y: x * y, pr_series.to_numpy(), sh_series.to_numpy()))

        else: sh_series.index = pr_series.index

    else:

        logx.print_and_log_text \
            (f'\nThe prices and shares for symbol {symbol} are misaligned...\n')

        return None


    mrkt_cap_series \
        = pd.Series(mrkt_cap_list, index = sh_series.index.to_numpy()).dropna()

    return mrkt_cap_series


# In[22]:


#*******************************************************************************************
 #
 #  Function Name:  fmt_addr
 #
 #  Function Description:
 #      This function formats an address.
 #
 #
 #  Return Type: string
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  string         street           The parameter is the street address.
 #  string         city             The parameter is the city.
 #  string         state            The parameter is the state.
 #  string         postal_code      The parameter is the postal code.
 #  string         country          The parameter is the country.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/17/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/ 

def fmt_addr \
        (street:      str, 
         city:        str, 
         state:       str, 
         postal_code: str, 
         country:     str) \
-> str:

    if len(street) > 0:      street += ', '

    if len(city) > 0:        city += ', ' 

    if len(state) > 0:       state += ' ' 

    if len(postal_code) > 0: postal_code += ', ' 


    addr = street + city + state + postal_code + country

    addr = addr.lower()

    return addr


# In[23]:


#*******************************************************************************************
 #
 #  Function Name:  rtn_addr
 #
 #  Function Description:
 #      This function returns a formatted address.
 #
 #
 #  Return Type: string
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  string         symbol           The parameter is the asset symbol.          
 #  object         stock_obj        The parameter is the yahoo information object.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/17/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/ 

def rtn_addr \
        (symbol:    str,
         stock_obj: object = None) \
-> str:

    if stock_obj is None:

        try:     stock_obj = yf.Ticker()

        except:  stock_obj = None


    try:

        profile_df \
            = obb.equity.profile \
                (symbol = symbol,
                 provider = config_dict['openbb']['provider']) \
                    .to_df()

    except:     profile_df    = None


    try: street = stock_obj.info['address1'].lower().strip()

    except:

        try:    street = profile_df['hq_address1'].iloc[0].lower().strip()

        except: street = ''


    try: city = stock_obj.info['city'].lower().strip()

    except:

        try:    city = profile_df['hq_address_city'].iloc[0].lower().strip()

        except: city = ''


    try: state = stock_obj.info['state'].lower().strip()

    except:

        try:    state = profile_df['hq_state'].iloc[0].lower().strip()

        except: state = ''


    try: postal_code = stock_obj.info['zip'].lower().strip()

    except:

        try:    postal_code = profile_df['hq_address_postal_code'].iloc[0].lower().strip()

        except: postal_code = ''


    try: country = stock_obj.info['country'].lower()

    except:

        try:    country = profile_df['hq_country'].iloc[0].lower().strip()

        except: country = ''


    addr = fmt_addr(street, city, state, postal_code, country)

    return addr


# In[24]:


#*******************************************************************************************
 #
 #  Function Name:  rtn_cmp_name
 #
 #  Function Description:
 #      This function returns the company name.
 #
 #
 #  Return Type: string
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  string         symbol           The parameter is the asset symbol.          
 #  object         stock_obj        The parameter is the yahoo information object.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/17/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/ 

def rtn_cmp_name \
        (symbol:    str, 
         stock_obj: object = None) \
-> str:

    if stock_obj is None:

        try: stock_obj    = yf.Ticker(symbol)

        except: stock_obj = None


    if stock_obj is not None:

        try: company = stock_obj.info['longName'].lower()

        except:

            try:

                company \
                    = obb.equity.profile \
                        (symbol = symbol, 
                         provider = config_dict['openbb']['provider']) \
                            .to_df()['name'] \
                                .iloc[0] \
                                .lower()

            except: company = None

    else:

        try:

            company \
                = obb.equity.profile \
                    (symbol = symbol, 
                     provider = config_dict['openbb']['provider']) \
                        .to_df()['name'] \
                            .iloc[0] \
                            .lower()

        except: company = None


    return company


# In[25]:


#*******************************************************************************************
 #
 #  Function Name:  rtn_cmp_industry
 #
 #  Function Description:
 #      This function returns the industry name.
 #
 #
 #  Return Type: string
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  string         symbol           The parameter is the asset symbol.          
 #  object         stock_obj        The parameter is the yahoo information object.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/17/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/ 

def rtn_cmp_industry \
        (symbol:    str, 
         stock_obj: object = None) \
-> str:

    if stock_obj is None:

        try:    stock_obj = yf.Ticker(symbol)

        except: stock_obj = None


    if stock_obj is not None:

        try: industry = stock_obj.info['industry'].lower()

        except:

            try:

                industry \
                    = obb.equity.profile \
                        (symbol = symbol, 
                         provider = config_dict['openbb']['provider']) \
                            .to_df()['industry_category'] \
                                .iloc[0] \
                                .lower()

            except: industry = None

    else:

        try:

            industry \
                = obb.equity.profile \
                    (symbol = symbol, 
                     provider = config_dict['openbb']['provider']) \
                        .to_df()['industry_category'] \
                            .iloc[0] \
                            .lower()

        except: industry = None


    return industry


# In[26]:


#*******************************************************************************************
 #
 #  Function Name:  rtn_cmps_info_df
 #
 #  Function Description:
 #      This function returns a company information dataframe.
 #
 #
 #  Return Type: dataframe
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  object         input_obj        The parameter is the array of company symbols.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/17/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/ 

def rtn_cmps_info_df(input_obj: object) -> pd.DataFrame:

    input_array = dtypesx.cnv_data_to_array(input_obj)

    symbol_array = company_array \
        = industry_array = address_array \
        = np.asarray([], dtype = str)

    lng_array = lat_array \
        = min_capital_array = max_capital_array = mean_capital_array \
        = median_capital_array = std_capital_array = sem_capital_array \
        = np.asarray([], dtype = float)


    logx.print_and_log_text('\nBEGIN RETRIEVING COMPANY INFORMATION...\n')


    for symbol in input_array:

        try: stock_obj       = yf.Ticker(symbol)

        except: stock_obj    = None


        company              = rtn_cmp_name(symbol, stock_obj)

        industry             = rtn_cmp_industry(symbol, stock_obj)


        address              = rtn_addr(symbol, stock_obj)

        lng_flt, lat_flt     = rtn_geo_coords(address)


        mrkt_cap_series      = rtn_mrkt_cap(symbol, stock_obj)


        if  company is None \
            or industry is None \
            or address == '' \
            or lng_flt is None \
            or lat_flt is None \
            or mrkt_cap_series is None:

            logx.print_and_log_text \
                (f'\nThe symbol, {symbol}, does not have the required information. '
                 + 'Skipping...\n')     


            continue


        min_capital_array    = np.append(min_capital_array, mrkt_cap_series.min())

        max_capital_array    = np.append(max_capital_array, mrkt_cap_series.max())

        mean_capital_array   = np.append(mean_capital_array, mrkt_cap_series.mean())

        median_capital_array = np.append(median_capital_array, mrkt_cap_series.median())

        std_capital_array    = np.append(std_capital_array, mrkt_cap_series.std())

        sem_capital_array    = np.append(sem_capital_array, mrkt_cap_series.sem())

        symbol_array         = np.append(symbol_array, symbol)

        company_array        = np.append(company_array, company)

        industry_array       = np.append(industry_array, industry)

        address_array        = np.append(address_array, address)

        lng_array            = np.append(lng_array, lng_flt)

        lat_array            = np.append(lat_array, lat_flt)


        logx.print_and_log_text \
            (f'\nSUCCESSFULLY RETRIEVED INFORMATION FOR SYMBOL, {symbol}.\n')


    mrkt_cap_df \
        = pd.DataFrame \
            (list \
                 (zip \
                      (symbol_array, company_array, 
                       industry_array, address_array, lng_array, 
                       lat_array, min_capital_array, max_capital_array, 
                       mean_capital_array, median_capital_array,
                       std_capital_array, sem_capital_array)),
             columns = config_dict['mrkt_cap_cols'])

    return mrkt_cap_df


# In[27]:


#*******************************************************************************************
 #
 #  Function Name:  rtn_cmps_info_file_df
 #
 #  Function Description:
 #      This function returns a company information dataframe but attempts to extract 
 #      the information from an existing file first.
 #
 #
 #  Return Type: dataframe
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  object         input_obj        The parameter is the array of company symbols.
 #  string         file_path        The parameter is the file path to the input file.
 #  string         idx_col          The parameter is the index column in the output file.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/17/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/ 

def rtn_cmps_info_file_df \
        (input_obj: object,
         file_path: str,
         idx_col:   str = config_dict['file']['cmp_idx']) \
-> pd.DataFrame:

    file_exists_bool = os.path.exists(file_path)


    if not file_exists_bool:

        data_df = rtn_cmps_info_df(input_obj)

        data_df = data_df.dropna()

        data_df = data_df.reset_index(drop = True)

        data_df.to_json(file_path, mode = 'w')

    else: data_df = pd.read_json(file_path, typ = 'frame')


    return data_df


# In[28]:


#*******************************************************************************************
 #
 #  Function Name:  rtn_industry_stats_summary
 #
 #  Function Description:
 #      This function takes a dataframe and column name of industry data and returns a
 #      summary statistics dataframe.
 #
 #
 #  Return Type: dataframe
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  dataframe      input_df         The parameter is the input dataframe.
 #  string         col              The parameter is the dataframe column for analysis.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/17/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/ 

def rtn_industry_stats_summary \
        (input_df: pd.DataFrame, 
         col:      str) \
-> pd.DataFrame:

    quantile_series = input_df.groupby('industry')[col].quantile([0.25, 0.50, 0.75])


    industry_array = np.asarray([], dtype = str)

    lwr_quartile_array = upr_quartile_array = iqr_rng_array \
        = lwr_bnd_array = upr_bnd_array = mean_array = median_array \
        = np.asarray([], dtype = float)

    cmp_cnt_array = outlier_cnt_array = np.asarray([], dtype = int)


    for idx, quartile in enumerate(quantile_series):

        mod_cond_int = idx % 3


        if mod_cond_int == 0:

            industry = quantile_series.keys()[idx][0]


            lwr_quartile_flt = quantile_series.iloc[idx]

            upr_quartile_flt = quantile_series.iloc[idx + 2]


            iqr_rng_flt = upr_quartile_flt - lwr_quartile_flt


            lwr_bnd_flt = lwr_quartile_flt - (1.5 * iqr_rng_flt)

            upr_bnd_flt = lwr_quartile_flt + (1.5 * iqr_rng_flt)


            mean_flt = input_df.loc[input_df['industry'] == industry][col].mean()

            median_flt = input_df.loc[input_df['industry'] == industry][col].median()


            cmp_cnt_int = input_df.loc[input_df['industry'] == industry]['symbol'].count()

            outlier_cnt_int \
                = len(input_df \
                        .loc[(input_df['industry'] == industry) \
                             & ((input_df[col] < lwr_bnd_flt) \
                                | (input_df[col] > upr_bnd_flt))])


            industry_array = np.append(industry_array, industry)

            lwr_quartile_array = np.append(lwr_quartile_array, lwr_quartile_flt)

            upr_quartile_array = np.append(upr_quartile_array, upr_quartile_flt)

            iqr_rng_array = np.append(iqr_rng_array, iqr_rng_flt)

            lwr_bnd_array = np.append(lwr_bnd_array, lwr_bnd_flt)

            upr_bnd_array = np.append(upr_bnd_array, upr_bnd_flt)

            mean_array = np.append(mean_array, mean_flt)

            median_array = np.append(median_array, median_flt)

            cmp_cnt_array = np.append(cmp_cnt_array, cmp_cnt_int)

            outlier_cnt_array = np.append(outlier_cnt_array, outlier_cnt_int)


    data_df \
        = pd.concat \
            ({'industry': pd.Series(industry_array), 
              'lower_quartile': pd.Series(lwr_quartile_array),
              'upper_quartile': pd.Series(upr_quartile_array),
              'iqr_range': pd.Series(iqr_rng_array),
              'lower_boundary': pd.Series(lwr_bnd_array),
              'upper_boundary': pd.Series(upr_bnd_array),
              'mean': pd.Series(mean_array),
              'median': pd.Series(median_array),
              'company_count': pd.Series(cmp_cnt_array),
              'outliers_count': pd.Series(outlier_cnt_array)},
             axis = 1)

    return data_df


# In[29]:


#*******************************************************************************************
 #
 #  Function Name:  rtn_sctr_mrkt_idx
 #
 #  Function Description:
 #      This function takes an array of stock symbols from an industry along with the
 #      criteria series and calculates a market industry price index over a period of
 #      time.
 #
 #
 #  Return Type: series
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  object         symbol_obj       The parameter is the symbol object.
 #  object         idx_wgts_obj     The parameter is the index weights object.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/17/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/ 

def rtn_sctr_mrkt_idx \
        (symbol_obj:   object, 
         idx_wgts_obj: object) \
-> pd.Series:

    symbol_array   = dtypesx.cnv_data_to_array(symbol_obj)

    idx_wgts_array = dtypesx.cnv_data_to_array(idx_wgts_obj)


    logx.print_and_log_text('BEGIN CALCULATING MARKET INDEX...\n')


    mrkt_series = None

    for idx, symbol in enumerate(symbol_array):

        try:

            prices_series    = rtn_prices(symbol)

            curr_mrkt_series = prices_series * idx_wgts_array[idx]


            if mrkt_series is not None:

                    mrkt_series += curr_mrkt_series

            else:   mrkt_series = copy.deepcopy(curr_mrkt_series)


            logx.print_and_log_text \
                (f"\nSUCCESSFULLY PROCESSED SYMBOL {symbol} FOR THE SHARE INDEX...\n")

        except:

            logx.print_and_log_text \
                (f'\nThe symbol, {symbol}, was not successfully processed. ' \
                 + 'Skipping...\n')


    logx.print_and_log_text \
        ('\nTHE CALCULATION OF THE MARKET INDEX IS COMPLETE.\n')


    mrkt_series = mrkt_series.rename('yields')

    mrkt_series = dtypesx.rtn_date_idxs(mrkt_series)

    return mrkt_series


# In[30]:


#*******************************************************************************************
 #
 #  Function Name:  rtn_sctr_mrkt_idx_file
 #
 #  Function Description:
 #      This function takes an array of stock symbols from an industry along with the
 #      criteria series and calculates a market industry price index over a period of
 #      time but attempts to extract the information from an existing file first.
 #
 #
 #  Return Type: series
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  series         symbol_series    The parameter is the symbol object.
 #  series         idx_wgts_series  The parameter is the index weights series.
 #  string         file_path        The parameter is the file path to the input file.
 #  string         series_name      The parameter is the output series name.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/17/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/ 

def rtn_sctr_mrkt_idx_file \
        (symbol_series:           pd.Series,
         cmp_idx_wgts_all_series: pd.Series,
         file_path:               str,
         series_name:             str = 'prices') \
-> pd.Series:

    file_exists_bool = os.path.exists(file_path)


    if not file_exists_bool:

        data_series = rtn_sctr_mrkt_idx(symbol_series, cmp_idx_wgts_all_series)

        data_series = dtypesx.rtn_date_idxs(data_series)

        data_series = data_series.rename(series_name)

        data_series.to_json(file_path, mode = 'w')

    else:

        data_series = pd.read_json(file_path, typ = 'series')

        data_series = dtypesx.rtn_date_idxs(data_series)

        data_series = data_series.rename(series_name)


    return data_series


# In[31]:


#*******************************************************************************************
 #
 #  Function Name:  rtn_geo_df
 #
 #  Function Description:
 #      This function returns a geographic dataframe for display.
 #
 #
 #  Return Type: dataframe
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  dataframe      input_df         The parameter is the input dataframe.
 #  string         size_col         The parameter is the marker size column name.
 #  integer        size_factor      The parameter is the marker size reduction factor.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/17/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/ 

def rtn_geo_df \
        (input_df:    pd.DataFrame, 
         size_col:    str, 
         size_factor: int = 1) \
-> pd.DataFrame:

    if size_factor == 0:  sz_fctr_int = 1

    elif size_factor < 0: sz_fctr_int = abs(size_factor)

    else:                 sz_fctr_int = size_factor


    data_df = input_df.copy()

    data_df[size_col] = data_df[size_col] / sz_fctr_int


    geo_dict \
        = {'symbol':       data_df['symbol'], 
           'company_name': data_df['company_name'], 
           'industry':     data_df['industry'], 
           'address':      data_df['address'],
           'longitude':    data_df['longitude'],
           'latitude':     data_df['latitude'],
           'marker_size':  data_df[size_col]}

    geo_df = pd.DataFrame(geo_dict)

    return geo_df


# In[ ]:




