#!/usr/bin/env python
# coding: utf-8

# In[1]:


#*******************************************************************************************
 #
 #  File Name:  oil_energy_sectorx.py
 #
 #  File Description:
 #      This Python script, oil_energy_sectorx.py, contains generic Python functions 
 #      for completing common tasks for the IPython Notebook, oil_energy_sector.ipynb,
 #      Here is the list:
 #
 #      is_valid_company_start_date
 #      return_industry_statistics_summary
 #      return_top_company_by_industry
 #      convert_to_geodataframe
 #      return_shares_aligned_with_prices
 #      return_normalized_outstanding_shares_to_prices
 #
 #      return_yahoo_trading_prices
 #      return_complete_ticker_list
 #      return_who_covid_data
 #      return_formatted_address_string
 #      return_geographic_dataframe
 #      return_oil_energy_sector_companies
 #      return_oil_sector_market_indices
 #
 #
 #  Date            Description                             Programmer
 #  ----------      ------------------------------------    ------------------
 #  08/14/2023      Initial Development                     Nicholas J. George
 #  02/03/2026      Modified return_complete_ticker_list
 #                  to use csv file in lieu of yahoo_fin
 #                  module                                  Nicholas J. George
 #
 #******************************************************************************************/

import logx
import oil_energy_sectorx_constants
import pandasx

import datetime
import requests

import pandas as pd
import yfinance as yf

from io import StringIO
from oil_energy_sector_config import geoapify_key

pd.options.mode.chained_assignment = None


# In[2]:


CONSTANT_LOCAL_FILE_NAME = 'oil_energy_sectorx.py'


# In[3]:


#*******************************************************************************************
 #
 #  Function Name:  is_valid_company_start_date
 #
 #  Function Description:
 #      This function returns true if the start date for the stock's trading began
 #      at or before the analysis period.
 #
 #
 #  Return Type: boolean
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  object  yahoo_finance   The parameter is a object containing dictionaries about
 #                          a particular company.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  08/14/2023          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/ 

def is_valid_company_start_date(yahoo_finance):

    first_trading_datetime \
        = datetime.datetime.fromtimestamp(yahoo_finance.info['firstTradeDateEpochUtc'])

    analysis_start_datetime \
        = datetime.datetime.strptime \
            (oil_energy_sectorx_constants.START_DATE, '%Y-%m-%d')


    if analysis_start_datetime < first_trading_datetime:

        return False

    else:

        return True


# In[4]:


#*******************************************************************************************
 #
 #  Function Name:  return_industry_statistics_summary
 #
 #  Function Description:
 #      This function receives a market capitalization dataframe, calculates the statistics
 #      for a box plot, and returns the statistics as a dataframe.
 #
 #
 #  Return Type: dataframe
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  dataframe
 #          input_dataframe The parameter is the input dataframe.
 #  string  column_name_string
 #                          The parameter is the dataframe column with the 
 #                          input series information.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  08/14/2023          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def return_industry_statistics_summary \
        (input_dataframe,
         column_name_string):

    quantile_series \
        = input_dataframe \
            .groupby('industry')[column_name_string] \
            .quantile([0.25, 0.50, 0.75])


    industry_string_list = []

    lower_quartile_float_list = []

    upper_quartile_float_list = []

    interquartile_range_float_list = []

    lower_bound_float_list = []

    upper_bound_float_list = []

    mean_float_list = []

    median_float_list = []

    company_count_integer_list = []

    outlier_count_integer_list = []


    for index, quartile in enumerate(quantile_series):

        modulus_condition_integer = index % 3


        if modulus_condition_integer == 0:

            industry_string = quantile_series.keys()[index][0]

            lower_quartile_float = quantile_series.iloc[index]

            upper_quartile_float = quantile_series.iloc[index + 2]

            interquartile_range_float = upper_quartile_float - lower_quartile_float

            lower_bound_float = lower_quartile_float - (1.5 * interquartile_range_float)

            upper_bound_float = lower_quartile_float + (1.5 * interquartile_range_float)

            mean_float \
                = input_dataframe \
                    .loc[input_dataframe['industry'] == industry_string][column_name_string] \
                    .mean()

            median_float \
                = input_dataframe \
                    .loc[input_dataframe['industry'] == industry_string][column_name_string] \
                    .median()

            company_count_integer \
                = input_dataframe \
                    .loc[input_dataframe['industry'] == industry_string]['ticker'].count()

            outlier_count_integer \
                = len(input_dataframe \
                        .loc[(input_dataframe['industry'] == industry_string) \
                             & ((input_dataframe[column_name_string] < lower_bound_float) \
                                | (input_dataframe[column_name_string] > upper_bound_float))])


            industry_string_list.append(industry_string)

            lower_quartile_float_list.append(lower_quartile_float)

            upper_quartile_float_list.append(upper_quartile_float)

            interquartile_range_float_list.append(interquartile_range_float)

            lower_bound_float_list.append(lower_bound_float)

            upper_bound_float_list.append(upper_bound_float)

            mean_float_list.append(mean_float)

            median_float_list.append(median_float)

            company_count_integer_list.append(company_count_integer)

            outlier_count_integer_list.append(outlier_count_integer)


    temp_dataframe \
        = pd.concat({'industry': pd.Series(industry_string_list), 
                     'lower_quartile': pd.Series(lower_quartile_float_list),
                     'upper_quartile': pd.Series(upper_quartile_float_list),
                     'interquartile_range': pd.Series(interquartile_range_float_list),
                     'lower_boundary': pd.Series(lower_bound_float_list),
                     'upper_boundary': pd.Series(upper_bound_float_list),
                     'mean': pd.Series(mean_float_list),
                     'median': pd.Series(median_float_list),
                     'company_count': pd.Series(company_count_integer_list),
                     'outliers_count': pd.Series(outlier_count_integer_list)},
                    axis = 1)

    return temp_dataframe


# In[5]:


#*******************************************************************************************
 #
 #  Function Name:  return_top_company_by_industry
 #
 #  Function Description:
 #      This function receives an oil company index weight dataframe, formats it, and
 #      returns a top company dataframe.
 #
 #
 #  Return Type: dataframe
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  dataframe
 #          input_dataframe The parameter is the input dataframe.
 #  string  criterion_string
 #                          The parameter is the column name used for sorting.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  08/14/2023          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def return_top_company_by_industry \
        (input_dataframe,
         criterion_string):

    maximum_median_capitalization_by_industry_series \
        = input_dataframe.groupby('industry')[criterion_string].max()

    top_ticker_string_list = []

    top_company_string_list = []

    industry_string_list = []

    median_capitalization_float_list = []


    for index, capitalization in enumerate(maximum_median_capitalization_by_industry_series):

        top_ticker_string \
            = (input_dataframe.loc[input_dataframe[criterion_string] \
               == capitalization]['ticker']) \
                .iloc[0]

        top_company_name_string \
            = (input_dataframe.loc[input_dataframe['ticker'] \
               == top_ticker_string]['company_name']) \
                .iloc[0]

        industry_string = maximum_median_capitalization_by_industry_series.keys()[index]


        top_ticker_string_list.append(top_ticker_string)

        top_company_string_list.append(top_company_name_string)

        industry_string_list.append(industry_string)

        median_capitalization_float_list.append(capitalization)


    index_weight_float_list = []

    total_median_capitalization_float = sum(median_capitalization_float_list)


    for index, capitalization in enumerate(median_capitalization_float_list):

        index_weight_float = capitalization / total_median_capitalization_float

        index_weight_float_list.append(index_weight_float)


    final_dataframe \
        = pd.DataFrame \
            (list(zip(top_ticker_string_list, top_company_string_list, industry_string_list, 
                      median_capitalization_float_list, index_weight_float_list)),
             columns = ['ticker', 'company_name', 'industry', 
                        'median_capitalization', 'index_weight'])

    return final_dataframe


# In[6]:


#*******************************************************************************************
 #
 #  Function Name:  convert_to_geodataframe
 #
 #  Function Description:
 #      This function receives an input dataframe, and creates a geoDataFrame from it.
 #
 #
 #  Return Type: dataframe
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  dataframe
 #          input_dataframe The parameter is a input dataframe.
 #  string  size_field_string
 #                          The parameter is the column name for the marker size information.
 #  integer size_order_factor_integer
 #                          The parameter is the order of magnitude to reduce the marker
 #                          size parameter.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  08/14/2023          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def convert_to_geodataframe \
        (input_dataframe,
         size_field_string,
         size_order_factor_integer = 1):

    if size_order_factor_integer <= 0:

        size_order_factor_integer = 1


    temp_dataframe = input_dataframe.copy()

    temp_dataframe[size_field_string] \
        = temp_dataframe[size_field_string] / size_order_factor_integer

    frame_dictionary \
        = {'ticker': temp_dataframe['ticker'], 
           'company_name': temp_dataframe['company_name'], 
           'industry': temp_dataframe['industry'], 
           'address': temp_dataframe['address'],
           'longitude': temp_dataframe['longitude'],
           'latitude': temp_dataframe['latitude'],
           'marker_size': temp_dataframe[size_field_string]}


    final_dataframe = pd.DataFrame(frame_dictionary)

    return final_dataframe


# In[7]:


#*******************************************************************************************
 #
 #  Function Name:  return_shares_aligned_with_prices
 #
 #  Function Description:
 #      This function receives an inputDataFrame, and creates a geoDataFrame from it.
 #
 #
 #  Return Type: series
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  series  prices_series   The parameter is a the series with the reference indices
 #  series  shares_series   The parameter is the Series with the requisite values.
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  08/14/2023          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def return_shares_aligned_with_prices \
        (prices_series,
         shares_series):

    prices_first_index_date = prices_series.index[0]

    shares_first_index_date = shares_series.index[0]


    index_integer_list = []

    value_integer_list = []


    prices_index_integer = 0

    shares_index_integer = 0


    if prices_first_index_date < shares_first_index_date:

        while prices_series.index[prices_index_integer] < shares_first_index_date:

            index_integer_list.append(prices_series.index[prices_index_integer])

            value_integer_list.append(shares_series.iloc[shares_index_integer])

            prices_index_integer += 1


        if prices_first_index_date in shares_series.index:

            index_integer_list.append(prices_series.index[prices_index_integer])

            value_integer_list.append(shares_series.iloc[shares_index_integer])

            prices_index_integer += 1

    elif prices_first_index_date > shares_first_index_date:

        while shares_series.index[shares_index_integer] < prices_first_index_date:

            shares_index_integer += 1


        index_integer_list.append(prices_series.index[prices_index_integer])

        value_integer_list.append(shares_series.iloc[shares_index_integer])

        prices_index_integer += 1


    prices_series_size_integer = prices_series.count()

    shares_series_size_integer = shares_series.count()


    for loop_index in range(prices_index_integer, prices_series_size_integer):     

        if loop_index == prices_index_integer \
            and shares_index_integer < shares_series_size_integer:

            if prices_series.index[prices_index_integer] \
                == shares_series.index[shares_index_integer]:

                index_integer_list.append(prices_series.index[prices_index_integer])

                value_integer_list.append(shares_series.iloc[shares_index_integer])


                if prices_index_integer < prices_series_size_integer - 1:

                    prices_index_integer += 1

                if shares_index_integer < shares_series_size_integer - 1:

                    shares_index_integer += 1

            elif shares_index_integer == shares_series_size_integer - 1:

                while prices_index_integer < prices_series_size_integer:

                    index_integer_list.append(prices_series.index[prices_index_integer])

                    value_integer_list.append(shares_series.iloc[shares_index_integer])

                    prices_index_integer += 1    

            elif prices_series.index[prices_index_integer] \
                    < shares_series.index[shares_index_integer]:

                while prices_index_integer < prices_series_size_integer \
                        and prices_series.index[prices_index_integer] \
                            < shares_series.index[shares_index_integer]:

                    index_integer_list.append(prices_series.index[prices_index_integer])

                    value_integer_list.append(shares_series.iloc[shares_index_integer - 1])

                    prices_index_integer += 1

            else:

                if prices_index_integer < prices_series_size_integer \
                    and shares_index_integer < shares_series_size_integer:

                    index_integer_list.append(prices_series.index[prices_index_integer])

                    value_integer_list.append(shares_series.iloc[shares_index_integer])

                while shares_index_integer < shares_series_size_integer \
                        and shares_series.index[shares_index_integer] \
                            < prices_series.index[prices_index_integer]:

                    shares_index_integer += 1


            if shares_index_integer < shares_series_size_integer \
                and shares_series.index[shares_index_integer] not in prices_series.index:

                while shares_index_integer < shares_series_size_integer - 1 \
                        and shares_series.index[shares_index_integer] not in prices_series.index:

                    shares_index_integer += 1


    final_series = pd.Series(value_integer_list, index = index_integer_list)

    return final_series


# In[8]:


#*******************************************************************************************
 #
 #  Function Name:  return_normalized_outstanding_shares_to_prices
 #
 #  Function Description:
 #      This function receives a full shares series, extrapolates its values to fit
 #      a historical price series, and returns the new series to the caller.
 #
 #
 #  Return Type: series
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  series  prices_series   The parameter is a the series with the reference indices
 #  series  shares_series   The parameter is the Series with the requisite values.
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  08/14/2023          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def return_normalized_outstanding_shares_to_prices \
        (prices_series,
         shares_series):

    if shares_series.count() <= 0:

        logx.print_and_log_text('The shares series has no elements.')

        return None

    elif shares_series.count() == 1:

        temp_series = prices_series.copy()

        shares_series = (temp_series.astype(int) * 0) + shares_series[0]

        return shares_series


    first_prices_series = pandasx.return_unique_indices_last_values(prices_series)

    first_shares_series = pandasx.return_unique_indices_last_values(shares_series)


    prices_series = pandasx.return_date_indices(first_prices_series)

    shares_series = pandasx.return_date_indices(first_shares_series)


    final_series = return_shares_aligned_with_prices(prices_series, shares_series) 

    return final_series


# In[9]:


#*******************************************************************************************
 #
 #  Function Name:  return_yahoo_trading_prices
 #
 #  Function Description:
 #      This function receives a Yahoo Finance ticker and returns a series containing
 #      trading values for the analysis period.
 #
 #
 #  Return Type: series
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  string  ticker_string   The parameter is the Yahoo Finance ticker for the stock,
 #                          or index in question.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  08/14/2023          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/ 

def return_yahoo_trading_prices(ticker_string):

    if ticker_string == None or ticker_string == '':

        logx.print_and_log_text \
            ('The function, return_yahoo_trading_pricess, '
             + 'did not have a symbol passed to it ' 
             + f'as a parameter.  Exiting...\n')

        return None

    yahoo_finance_stock = yf.Ticker(ticker_string)

    historical_prices_series \
        = (yahoo_finance_stock.history \
            (start = oil_energy_sectorx_constants.START_DATE, 
             end = oil_energy_sectorx_constants.END_DATE)) \
                ['Close']


    return historical_prices_series


# In[10]:


#*******************************************************************************************
 #
 #  Function Name:  return_complete_ticker_list
 #
 #  Function Description:
 #      This function uses a Yahoo Finance API to transfer all tickers in its 
 #      database into a list. The script sorts the list alphabetically and 
 #      removes any redundancies before returning the list to the caller.
 #
 #
 #  Return Type: list
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  n/a     n/a             n/a
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  08/14/2023          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def return_complete_ticker_list():

    publically_traded_companies_df \
        = pd.read_csv \
            (oil_energy_sectorx_constants \
                .PUBLICALLY_TRADED_COMPANIES_CSV_FILE)


    publically_traded_companies_list \
        = publically_traded_companies_df \
            [oil_energy_sectorx_constants \
                .PUBLICALLY_TRADED_COMPANIES_TICKER_COLUMN] \
            .astype(str).tolist()

    publically_traded_companies_list \
        = [str(x) for x in publically_traded_companies_list]

    publically_traded_companies_list \
        = list(set(publically_traded_companies_list))

    publically_traded_companies_list \
        = sorted(publically_traded_companies_list)


    return publically_traded_companies_list


# In[11]:


#*******************************************************************************************
 #
 #  Function Name:  return_who_covid_data
 #
 #  Function Description:
 #      This function uses an WHO API to transfer all available COVID-19 Data
 #      for all countries into a dataframe, which the function returns to the
 #      caller.
 #
 #
 #  Return Type: list
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  n/a     n/a             n/a
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  08/14/2023          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def return_who_covid_data():

    current_response \
        = requests.get(oil_energy_sectorx_constants.WHO_COVID_19_DATA_URL)

    who_covid_file_path = StringIO(current_response.text)


    temp_dataframe = pd.read_csv(who_covid_file_path)

    temp_dataframe \
        .rename \
            (columns \
                = {'ï»¿Date_reported': 'date_reported', 
                   'Country_code': 'country_code',
                   'Country': 'country',
                   'WHO_region': 'who_region',
                   'New_cases': 'new_cases',
                   'Cumulative_cases': 'cumulative_cases',
                   'New_deaths': 'new_deaths',
                   'Cumulative_deaths': 'cumulative_deaths'},
             inplace = True)


    return temp_dataframe


# In[12]:


#*******************************************************************************************
 #
 #  Function Name:  return_formatted_address_string
 #
 #  Function Description:
 #      This function receives a Yahoo Finance API object for a company, retrieves address
 #      information, and returns the formatted address as a string.
 #
 #
 #  Return Type: string
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  object  yahoo_finance_stock
 #                          The parameter is a Yahoo Finance API object for a company.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  08/14/2023          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def return_formatted_address_string (yahoo_finance_stock):

    street_address_string = yahoo_finance_stock.info['address1']

    city_string = yahoo_finance_stock.info['city']

    country_string = yahoo_finance_stock.info['country']


    if country_string == 'United States' or country_string == 'Canada':

        state_string = yahoo_finance_stock.info['state']

        zip_code_string = yahoo_finance_stock.info['zip']

        address_string \
            = f'{street_address_string}, ' + f'{city_string}, ' + f'{state_string}, ' \
              + f'{zip_code_string}, ' + f'{country_string}'

    elif country_string == 'United Kingdom' \
            or country_string == 'Bermuda' \
            or country_string == 'Denmark':

        zip_code_string = yahoo_finance_stock.info['zip']

        address_string \
            = f'{street_address_string}, ' + f'{city_string}, ' \
              + f'{zip_code_string}, ' + f'{country_string}'

    else:

        address_string \
            = f'{street_address_string}, ' + f'{city_string}, ' + f'{country_string}'


    return address_string


# In[13]:


#*******************************************************************************************
 #
 #  Function Name:  return_geographic_dataframe
 #
 #  Function Description:
 #      This function receives a input dataframe, appends latitude and longitude onto
 #      a copy of the input dataframe, and returns the copy to the caller.
 #
 #
 #  Return Type: dataframe
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  dataframe
 #          input_dataframe The parameter is a input dataframe.
 #  string  address_field_string
 #                          The parameter is the column name for the address information.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  08/14/2023          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def return_geographic_dataframe \
        (input_dataframe,
         address_field_string):

    temp_dataframe = input_dataframe.copy()

    longitude_float_list = []

    latitude_float_list = []

    logx.print_and_log_text \
        ('\nRETRIEVING LONGITUDES AND LATITUDES FROM ADDRESSES...\n\n')


    for index, company in temp_dataframe.iterrows():

        company_address_string = company[address_field_string]

        url_string \
            = oil_energy_sectorx_constants.GEOAPIFY_QUERY_URL \
              + f'{company_address_string}&apiKey={geoapify_key}'

        try:

            current_response = requests.get(url_string)

            current_response.raise_for_status()

            information_dictionary = current_response.json()


            longitude_float = information_dictionary['features'][0]['properties']['lon']

            latitude_float = information_dictionary['features'][0]['properties']['lat']

            logx.print_and_log_text \
                (f'\nindex: {index}\n' + '\nCompany Information:\n' + f'{company}\n\n' \
                 + f'longitude:  {longitude_float}\n' \
                 + f'latitude: {latitude_float}\n')


            longitude_float_list.append(longitude_float)

            latitude_float_list.append(latitude_float)

            logx.print_and_log_text \
                ('\nRETRIEVAL OF LONGITUDES AND LATITUDES FROM ADDRESSES IS COMPLETE.\n\n')

        except:

            logx.print_and_log_text \
                ('\nThe function, return_geographic_dataframe, ' \
                 + f'in file, {LOCAL_FILE_NAME}, ' \
                 + f' for company:\n\n{company}\n\n' \
                 + 'did not find the requested address. ' \
                 + 'Skipping...\n')


    temp_dataframe \
        = pd.DataFrame \
            (list(zip(longitude_float_list, latitude_float_list)), 
             columns = ['longitude', 'latitude'])

    final_dataframe = pd.concat([input_dataframe, temp_dataframe], axis = 1)

    return final_dataframe


# In[14]:


#*******************************************************************************************
 #
 #  Function Name:  return_oil_energy_sector_companies
 #
 #  Function Description:
 #      This function receives a list of tickers and returns those for companies
 #      that belong to an oil industry and whose trading date began at or before 
 #      the analysis period.  Information concerning the process is displayed and
 #      written to a log file in the folder, resources.
 #
 #
 #  Return Type: dataframe
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  list    ticker_string_list
 #                          The parameter is the list of tickers from Yahoo Finance.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  08/14/2023          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def return_oil_energy_sector_companies(ticker_string_list):

    company_ticker_string_list = []

    company_name_string_list = []

    industry_string_list = []

    address_string_list = []

    minimum_capitalization_float_list = []

    maximum_capitalization_float_list = []

    mean_capitalization_float_list = []

    median_capitalization_float_list = []

    variance_capitalization_float_list = []

    standard_deviation_capitalization_float_list = []

    standard_error_of_mean_capitalization_float_list = []


    logx.print_and_log_text('\nBEGIN RETRIEVING OIL COMPANY INFORMATION...\n\n')


    for ticker in ticker_string_list:

        try:

            if ticker == None or ticker == '':

                continue


            yahoo_finance_stock = yf.Ticker(ticker)

            first_trading_datetime \
                = datetime.datetime.fromtimestamp \
                    (yahoo_finance_stock.info['firstTradeDateEpochUtc'])

            analysis_start_datetime \
                = datetime.datetime.strptime \
                    (oil_energy_sectorx_constants.START_DATE, '%Y-%m-%d')

            if analysis_start_datetime < first_trading_datetime:

                logx.print_and_log_text \
                    (f'\nTrading for the ticker, {ticker}, begins ' \
                     + 'after the first day of the analysis period. ' \
                     + 'Skipping...\n')

                continue


            industry_string = yahoo_finance_stock.info['industry']

            if industry_string.find('Oil') != -1 \
               and industry_string != 'Independent Oil & Gas':      

                company_name_string = yahoo_finance_stock.info['longName']

                address_string = return_formatted_address_string(yahoo_finance_stock)

                closing_stock_price_series \
                    = yahoo_finance_stock.history \
                        (start = oil_energy_sectorx_constants.START_DATE, 
                         end = oil_energy_sectorx_constants.END_DATE) \
                            ['Close']

                if closing_stock_price_series.empty == True \
                    or closing_stock_price_series.count() == 0 \
                    or (closing_stock_price_series == 0.0).all() == True:

                    logx.print_and_log_text \
                        (f'\nThis ticker, {ticker}, does not have historical share price '
                         + 'information. Skipping...\n')

                    continue


                full_shares_series \
                    = yahoo_finance_stock.get_shares_full \
                        (start = oil_energy_sectorx_constants.START_DATE, 
                         end = oil_energy_sectorx_constants.END_DATE)

                if full_shares_series.empty == True \
                    or full_shares_series.count() == 0 \
                    or (full_shares_series == 0).all() == True:

                    outstanding_shares_integer = yahoo_finance_stock.info['sharesOutstanding']

                    full_shares_series \
                        = pd.Series \
                            ([outstanding_shares_integer], 
                             index = [closing_stock_price_series.index[0]])


                updated_full_shares_series \
                    = return_normalized_outstanding_shares_to_prices \
                        (closing_stock_price_series, 
                         full_shares_series)

                capitalization_float_list \
                    = list(map(lambda x, y: x * y, 
                               closing_stock_price_series.tolist(), 
                               updated_full_shares_series.tolist()))

                capitalization_series \
                    = pd.Series \
                        (capitalization_float_list, 
                         index = updated_full_shares_series.index.tolist())


                company_ticker_string_list.append(ticker)

                company_name_string_list.append(company_name_string)

                industry_string_list.append(industry_string)

                address_string_list.append(address_string)


                minimum_capitalization_float_list.append(capitalization_series.min())

                maximum_capitalization_float_list.append(capitalization_series.max())

                mean_capitalization_float_list.append(capitalization_series.mean())

                median_capitalization_float_list.append(capitalization_series.median())

                variance_capitalization_float_list.append(capitalization_series.var())

                standard_deviation_capitalization_float_list.append(capitalization_series.std())

                standard_error_of_mean_capitalization_float_list.append(capitalization_series.sem())


                logx.print_and_log_text \
                    (f'\n\nSUCCESFULLY RETRIEVED INFORMATION FOR TICKER, {ticker}, IN THE ' \
                     + f'{industry_string} INDUSTRY.\n\n')

            else:

                logx.print_and_log_text \
                    (f'\nThis ticker, {ticker}, belongs to a company that ' \
                     + 'is not in the oil industry. Skipping...\n')

        except:

            logx.print_and_log_text \
                (f'\nThis ticker, {ticker}, does not have the required information.'
                 + '  Skipping...\n')


    logx.print_and_log_text \
        (f'\nTHE RETRIEVAL OF OIL COMPANY INFORMATION IS COMPLETE.\n\n')


    temp_dataframe \
        = pd.DataFrame \
            (list(zip(company_ticker_string_list, company_name_string_list, 
                      industry_string_list, address_string_list,
                      minimum_capitalization_float_list, maximum_capitalization_float_list, 
                      mean_capitalization_float_list, median_capitalization_float_list,
                      variance_capitalization_float_list, 
                      standard_deviation_capitalization_float_list,
                      standard_error_of_mean_capitalization_float_list)),
             columns = ['ticker', 'company_name', 'industry', 'address',
                        'min_market_cap', 'max_market_cap', 
                        'mean_market_cap', 'median_market_cap',
                        'var_market_cap', 'stdev_market_cap',
                        'sem_market_cap'])


    final_geographic_dataframe = return_geographic_dataframe(temp_dataframe, 'address')

    return final_geographic_dataframe


# In[15]:


#*******************************************************************************************
 #
 #  Function Name:  return_oil_sector_market_indices
 #
 #  Function Description:
 #      This function receives a list of tickers and index weights, calculates 
 #      an index over time, and returns the series.
 #
 #
 #  Return Type: series
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  list    ticker_string_list
 #                          The parameter is a list of tickers from Yahoo Finance.
 #  list    index_weight_float_list
 #                          The parameter is a list of index weights corresponding
 #                          to the ticker list parameter.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  08/14/2023          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def return_oil_sector_market_indices \
        (ticker_string_list,
         index_weight_float_list):

    if len(ticker_string_list) != len(index_weight_float_list):

        logx.print_and_log_text \
            ('The number of elements in the two function parameters are not equal. ' \
             + 'Exiting...\n')

        return None


    logx.print_and_log_text('BEGIN CALCULATING OIL COMPANY SHARE INDEX...\n\n')


    first_series_flag_boolean = True

    for index, ticker in enumerate(ticker_string_list):

        try:

            if ticker == None or ticker == '':

                logx.print_and_log_text('\nThere is no ticker. Skipping...\n')

                continue


            yahoo_finance_stock = yf.Ticker(ticker)

            temp_series \
                = yahoo_finance_stock.history \
                    (start = oil_energy_sectorx_constants.START_DATE, 
                     end = oil_energy_sectorx_constants.END_DATE) \
                        ['Close']

            if temp_series.empty == True \
                or temp_series.count() == 0 \
                or (temp_series == 0).all() == True:

                logx.print_and_log_text \
                    (f'This ticker, {ticker}, does not have historical share '
                     + 'price information.  Skipping...\n')

                continue


            if first_series_flag_boolean == True:

                market_index_series = temp_series * index_weight_float_list[index]

                first_series_flag_boolean = False

            else:

                market_index_series += temp_series * index_weight_float_list[index]


            logx.print_and_log_text \
                (f"\nSUCCESSFULLY PROCESSED TICKER'S, {ticker}, " \
                 + 'CONTRIBUTION TO THE SHARE INDEX...\n')


        except:

            logx.print_and_log_text \
                (f'\nThis ticker, {ticker}, did not have historical stock prices. ' \
                 + 'Skipping...\n')


    logx.print_and_log_text \
        ('\nTHE CALCULATION OF THE OIL COMPANY SHARE INDEX IS COMPLETE.\n')


    return market_index_series


# In[ ]:




