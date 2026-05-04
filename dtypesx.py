#!/usr/bin/env python
# coding: utf-8

# In[1]:


#*******************************************************************************************
 #
 #  File Name:  dtypesx.py
 #
 #  File Description:
 #      This Python script, dtypesx.py, contains generic Python functions 
 #      for manipulating datatypes, dates, and times.  Here is the list:
 #
 #  cnv_data_to_array
 #  drop_na
 #  strip_rmv_nmbr_space_case
 #  rtn_pos_int
 #  set_array_dtype
 #
 #  check_data_dtype_array
 #  check_data_series_dtype_array
 #  check_pos_int
 #
 #  contains_all_datetime_obj
 #  contains_all_npdatetime_obj
 #  contains_all_date_obj
 #  contains_all_strings
 #
 #  cnv_to_pct_chg
 #  cnv_df_to_pct_chg
 #  cnv_idxs_to_date
 #
 #  rtn_series_aligned_front
 #  rtn_series_aligned_back
 #  rtn_series_aligned_middle
 #  rtn_series_aligned_with_target
 #  rtn_series_align_idxs_series
 #
 #  rtn_data_obj_size
 #  rtn_series_with_unq_idxs
 #  rtn_date_idxs
 #
 #  rtn_prior_date
 #  rtn_future_date
 #
 #  rtn_norm_date_idx
 #  rtn_norm_series_list_df
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  04/11/2024          Initial Development                         Nicholas J. George
 #  02/18/2026          Upgraded Module                             Nicholas J. George
 #
 #******************************************************************************************/

import copy
import math
import re

import datetime as dt
import numpy    as np
import pandas   as pd

pd.options.mode.chained_assignment = None


# In[2]:


CONSTANT_LOCAL_FILE_NAME = 'dtypesx.py'


# In[3]:


#*******************************************************************************************
 #
 #  Function Name:  cnv_data_to_array
 #
 #  Function Description:
 #      This function takes an input object and returns it as a numpy array if it
 #      is an array, Series, list, or tuple. Otherwise, the function returns None.
 #
 #
 #  Return Type: array
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  object         input_obj        The parameter is a input obj.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def cnv_data_to_array(input_obj: object) -> np.ndarray:

    if isinstance(input_obj, np.ndarray): return input_obj

    elif isinstance(input_obj, list): return np.asarray(input_obj)

    elif isinstance(input_obj, pd.Series): return input_obj.to_numpy()

    elif isinstance(input_obj, tuple): return np.asarray(input_obj)

    elif isinstance(input_obj, pd.Index) \
            or isinstance(input_obj, pd.Index(dtype = int)) \
            or isinstance(input_obj, pd.Index(dtype = float)) \
            or isinstance(input_obj, pd.Index(dtype = str)) \
            or isinstance(input_obj, pd.Index(dtype = 'uint64')) \
            or isinstance(input_obj, pd.DatetimeIndex) \
            or isinstance(input_obj, pd.TimedeltaIndex) \
            or isinstance(input_obj, pd.PeriodIndex) \
            or isinstance(input_obj, pd.RangeIndex) \
            or isinstance(input_obj, pd.CategoricalIndex):

        return np.asarray(input_obj)

    else: return None


# In[4]:


#*******************************************************************************************
 #
 #  Function Name:  drop_inf_na
 #
 #  Function Description:
 #      This function removes na and inf values from an object.
 #
 #
 #  Return Type: object
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  object         input_obj        The parameter is a input obj.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def drop_inf_na(input_obj: object) -> object:

    if isinstance(input_obj, np.ndarray): 

        clean_obj = input_obj[np.isfinite(input_obj)]

    elif isinstance(input_obj, list):

        clean_obj = list(input_array[np.isfinite(np.asarray(input_obj))])

    elif isinstance(input_obj, pd.Series):

        clean_obj = input_obj[np.isfinite(input_obj)]

    elif isinstance(input_obj, tuple):

        clean_obj = tuple(np.asarray(input_obj)[np.isfinite(input_obj)])

    elif isinstance(input_obj, pd.Index) \
            or isinstance(input_obj, pd.Index(dtype = int)) \
            or isinstance(input_obj, pd.Index(dtype = float)) \
            or isinstance(input_obj, pd.Index(dtype = str)) \
            or isinstance(input_obj, pd.Index(dtype = 'uint64')):

        clean_obj = pd.Index(input_obj.to_series().replace([np.inf, -np.inf], np.nan).dropna())

    elif isinstance(input_obj, pd.DatetimeIndex):

        clean_obj = pd.DatetimeIndex(input_obj.to_series().replace([np.inf, -np.inf], np.nan).dropna())

    elif isinstance(input_obj, pd.TimedeltaIndex):

        clean_obj = pd.TimedeltaIndex(input_obj.to_series().replace([np.inf, -np.inf], np.nan).dropna())

    elif isinstance(input_obj, pd.PeriodIndex):

        clean_obj = pd.PeriodIndex(input_obj.to_series().replace([np.inf, -np.inf], np.nan).dropna())

    elif isinstance(input_obj, pd.RangeIndex):

        clean_obj = pd.RangeIndex(input_obj.to_series().replace([np.inf, -np.inf], np.nan).dropna())

    elif isinstance(input_obj, pd.CategoricalIndex):

        clean_obj = pd.CategoricalIndex(input_obj.to_series().replace([np.inf, -np.inf], np.nan).dropna())

    else: clean_obj = input_obj

    return clean_obj


# In[5]:


#*******************************************************************************************
 #
 #  Function Name:  strip_rmv_nmbr_space_case
 #
 #  Function Description:
 #      This function removes all non-alphabetical characters and white space from
 #      the input string and converts it to lower or upper case before returning
 #      the result.
 #
 #
 #  Return Type: string
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  string         text             The parameter is the input string.
 #  string         case             The parameter is the output case ('lower' or 'upper').
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def strip_rmv_nmbr_space_case \
        (text: str, 
         case: str = 'lower') \
-> str:

    nw_txt = re.sub(r'[^a-zA-Z]', '', text)

    nw_txt = nw_txt.replace(" ", "")

    if case == 'lower': nw_txt = nw_txt.lower()

    elif case == 'upper': nw_txt = nw_txt.upper()

    return nw_txt


# In[6]:


#*******************************************************************************************
 #
 #  Function Name:  rtn_pos_int
 #
 #  Function Description:
 #      This function attempts to return the input as a positive integer.
 #
 #
 #  Return Type: integer, boolean
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  object         input_obj        The parameter is the input object.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def rtn_pos_int(input_obj: object) -> tuple[int, bool]:

    try:

        if isinstance(input_obj, int):

            data_int = abs(input_obj)

            int_bool = True

        elif isinstance(input_obj, float):

            data_int = int(abs(input_obj))

            int_bool = True

        elif isinstance(input_obj, str):

            data_int = int(abs(float(input_obj)))

            int_bool = True

        elif isinstance(input_obj, np.int64) \
                or isinstance(input_obj, np.uint64):

            data_int = abs(int(input_obj))

            int_bool = True

        elif isinstance(input_obj, np.float64):

            data_int = abs(int(float(input_obj)))

            int_bool = True

        else: 

            data_int = input_obj

            int_bool = False

    except:

        data_int = input_obj

        int_bool = False

    return data_int, int_bool


# In[7]:


#*******************************************************************************************
 #
 #  Function Name:  set_array_dtype
 #
 #  Function Description:
 #      This function sets all the values of an array to the same data type.
 #
 #
 #  Return Type: array
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  array          data_array       The parameter is the data array.
 #  array          data_type        The parameter is the data type ('float', 'int', 
 #                                  'str', or 'bool').
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_array_dtype \
        (data_array: np.ndarray, 
         data_type:  str = 'float') \
-> np.ndarray:

    if data_type == 'float' and not all(isinstance(i, float) for i in data_array): 

        data_array = data_array.astype(float)

    elif data_type == 'int' and not all(isinstance(i, int) for i in data_array): 

        data_array = data_array.astype(int)

    elif data_type == 'str' and not all(isinstance(i, str) for i in data_array): 

        data_array = data_array.astype(str)

    elif data_type == 'bool' and not all(isinstance(i, str) for i in data_array): 

        data_array = data_array.astype(bool)


    return data_array


# In[8]:


#*******************************************************************************************
 #
 #  Function Name:  check_data_dtype_array
 #
 #  Function Description:
 #      This function returns a float array without na and inf and a success indicator.
 #
 #
 #  Return Type: object, boolean
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  object         input_obj        The parameter is the input object.
 #  object         rtn_val          The parameter is the return value upon failure
 #  string         data_type        The parameter is the array data type.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def check_data_dtype_array \
        (input_obj: object, 
         rtn_val:   object = None,
         data_type: str = 'float') \
-> tuple[object, bool]:

    if input_obj is not None:

        try:

            data_obj = drop_inf_na(input_obj)

            data_array = cnv_data_to_array(data_obj)


            if data_array is None: return rtn_val, False

            else:

                data_array = set_array_dtype(data_array, data_type)  

                return data_array, True


        except: return rtn_val, False

    else: return input_obj, False


# In[9]:


#*******************************************************************************************
 #
 #  Function Name:  check_data_series_dtype_array
 #
 #  Function Description:
 #      This function returns a dtype array and data series both without na.
 #
 #
 #  Return Type: object, object, boolean
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  object         data_obj         The parameter is the input object.
 #  object         rtn_val          The parameter is the return value upon failure
 #  string         data_type        The parameter is the array data type.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def check_data_series_dtype_array \
        (input_obj: object, 
         rtn_val:   object = None,
         data_type: str    = 'float') \
-> tuple[object, object, bool]:

    if input_obj is not None:

        try: 

            data_series = drop_inf_na(input_obj)

            data_array, data_bool = check_data_dtype_array(data_series, rtn_val = rtn_val)


            if data_bool == False: return rtn_val, rtn_val, False

            else: 

                data_array = set_array_dtype(data_array, data_type)

                return data_series, data_array, True

        except: return rtn_val, rtn_val, False

    else: return input_obj, input_obj, False


# In[10]:


#*******************************************************************************************
 #
 #  Function Name:  check_pos_int
 #
 #  Function Description:
 #      This function returns a positive integer.
 #
 #
 #  Return Type: object, boolean
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  object         int_obj          The parameter is the input object.
 #  object         rtn_val          The parameter is the return value upon failure
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def check_pos_int \
        (int_obj: object, 
         rtn_val: object = None) \
-> tuple[object, bool]:

    if int_obj is not None:

        try:

            pos_int, int_bool = rtn_pos_int(int_obj)

            if int_bool == False: return rtn_val, False

            else: return pos_int, int_bool

        except: return rtn_val, False

    else: return int_obj, False


# In[11]:


#*******************************************************************************************
 #
 #  Function Name:  contains_all_date_obj
 #
 #  Function Description:
 #      This function takes an input array, list, or Series and indicates whether all
 #      the elements are date objects.
 #
 #
 #  Return Type: boolean
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  object         data_obj         The parameter is a input obj.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def contains_all_date_obj(data_obj: object) -> bool:

    data_array = cnv_data_to_array(data_obj)

    return all(isinstance(item, dt.date) for item in data_array)


# In[12]:


#*******************************************************************************************
 #
 #  Function Name:  contains_all_datetime_obj
 #
 #  Function Description:
 #      This function takes an input array, list, or Series and indicates whether all
 #      the elements are datetime objects.
 #
 #
 #  Return Type: boolean
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  object         data_obj         The parameter is a input obj.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def contains_all_datetime_obj(data_obj: object) -> bool:

    data_array = cnv_data_to_array(data_obj)

    return all(isinstance(item, dt.datetime) for item in data_array)


# In[13]:


#*******************************************************************************************
 #
 #  Function Name:  contains_all_npdatetime_obj
 #
 #  Function Description:
 #      This function takes an input array, list, or Series and indicates whether all
 #      the elements are numpy.datetime objects.
 #
 #
 #  Return Type: boolean
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  object         data_obj         The parameter is a input obj.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def contains_all_npdatetime_obj(data_obj: object) -> bool:

    data_array = cnv_data_to_array(data_obj)

    return all(isinstance(item, np.datetime64) for item in data_array)


# In[14]:


#*******************************************************************************************
 #
 #  Function Name:  contains_all_strings
 #
 #  Function Description:
 #      This function takes an input array, list, or Series and indicates whether all
 #      the elements are strings.
 #
 #
 #  Return Type: boolean
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  object         data_obj         The parameter is a input obj.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def contains_all_strings(data_obj: object) -> bool:

    data_array = cnv_data_to_array(data_obj)

    return all(isinstance(item, str) for item in data_array)


# In[15]:


#*******************************************************************************************
 #
 #  Function Name:  cnv_to_pct_chg
 #
 #  Function Description:
 #      This function receives a series of numbers, converts its values to percent
 #      change values, and returns the new series to the caller.
 #
 #
 #  Return Type: series
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  series         input_series     The parameter is input series.
 #  integer        rnd              The parameter is the decimal place to round the 
 #                                  results.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George           
 #
 #******************************************************************************************/

def cnv_to_pct_chg \
        (input_series: pd.Series,
         rnd:          int = 2) \
-> pd.Series:

    input_array = input_series.to_numpy()

    temp_array = input_array * 0.0


    for i, ele in enumerate(input_array):

        if i > 0 and input_array[i - 1] != 0.0:

            temp_array[i] = ((ele - input_array[i - 1]) / input_array[i - 1]) * 100


    final_series      = pd.Series(temp_array, index = input_series.index)

    final_series      = final_series.drop(final_series.index[0])

    final_series.name = input_series.name


    if rnd >= 0: final_series = final_series.round(rnd)


    return final_series


# In[16]:


#*******************************************************************************************
 #
 #  Function Name:  cnv_df_to_pct_chg
 #
 #  Function Description:
 #      This function receives a dataframe, converts its values to percent change values, 
 #      and returns the new dataframe.
 #
 #
 #  Return Type: dataframe
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  series         input_df         The parameter is input dataframe.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George           
 #
 #******************************************************************************************/

def cnv_df_to_pct_chg(input_df: pd.DataFrame) -> pd.DataFrame:

    results_dict = {}

    for col in input_df.columns:

        tmp_series = input_df.loc[:, col]

        results_dict[col] = cnv_to_pct_chg(tmp_series)

    results_df = pd.DataFrame(results_dict).dropna()

    return results_df


# In[17]:


#*******************************************************************************************
 #
 #  Function Name:  rtn_series_aligned_front
 #
 #  Function Description:
 #      This function receives two series where the series's sequential index extends 
 #      before the target series sequential index or vice versa. The function returns
 #      the series aligned with the target.
 #
 #
 #  Return Type: series
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  series         sh_series        The parameter is the input series.
 #  series         trgt_series      The parameter is the target series.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George           
 #
 #******************************************************************************************/

def rtn_series_aligned_front \
        (sh_series:   pd.Series, 
         trgt_series: pd.Series) \
-> pd.Series:

    trgt_idx_array = np.asarray(trgt_series.index)

    sh_idx_array = np.asarray(sh_series.index)


    trgt_idx_int = sh_idx_int = 0


    trgt_first_idx_date = trgt_idx_array[0]

    sh_first_idx_date = sh_idx_array[0]


    trgt_val_array = trgt_series.to_numpy()

    sh_val_array = sh_series.to_numpy()


    idx_array = val_array = np.asarray([])


    if trgt_first_idx_date == sh_first_idx_date: 

        return sh_series

    elif trgt_first_idx_date < sh_first_idx_date: 

        while trgt_idx_array[trgt_idx_int] < sh_first_idx_date:

            idx_array = np.append(idx_array, trgt_idx_array[trgt_idx_int])

            val_array = np.append(val_array, sh_val_array[sh_idx_int])

            trgt_idx_int += 1


        idx_array = np.append(idx_array, sh_idx_array)

        val_array = np.append(val_array, sh_val_array)


    elif trgt_first_idx_date > sh_first_idx_date:

        while sh_idx_array[sh_idx_int] < trgt_first_idx_date:

            sh_idx_int += 1


        if trgt_first_idx_date not in sh_idx_array:

            idx_array = np.append(idx_array, trgt_first_idx_date)

            val_array = np.append(val_array, sh_val_array[sh_idx_int])

            sh_idx_int += 1


        idx_array = np.append(idx_array, sh_idx_array[sh_idx_int:])

        val_array = np.append(val_array, sh_val_array[sh_idx_int:])


    sh1_series = pd.Series(val_array, index = idx_array, name = sh_series.name)

    return sh1_series


# In[18]:


#*******************************************************************************************
 #
 #  Function Name:  rtn_series_aligned_back
 #
 #  Function Description:
 #      This function receives two series where the series's sequential index extends 
 #      past the target series sequential index or vice versa. The function returns the
 #      series aligned with the target.
 #
 #
 #  Return Type: series
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  series         sh_series        The parameter is the input series.
 #  series         trgt_series      The parameter is the target series.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George           
 #
 #******************************************************************************************/

def rtn_series_aligned_back \
        (sh_series:   pd.Series, 
         trgt_series: pd.Series) \
-> pd.Series:

    trgt_idx_array = np.asarray(trgt_series.index)

    sh_idx_array = np.asarray(sh_series.index)


    trgt_val_array = trgt_series.to_numpy()

    sh_val_array = sh_series.to_numpy()


    trgt_last_idx_date = trgt_idx_array[len(trgt_idx_array) - 1]

    sh_last_idx_date = sh_idx_array[len(sh_idx_array) - 1]


    idx_array = val_array = np.asarray([])


    if trgt_last_idx_date == sh_last_idx_date: 

        return sh_series

    elif trgt_last_idx_date > sh_last_idx_date:

        trgt_idx_int = 0

        while trgt_idx_array[trgt_idx_int] < sh_last_idx_date:

            trgt_idx_int += 1


        idx_array = copy.deepcopy(sh_idx_array)

        val_array = copy.deepcopy(sh_val_array)


        if sh_last_idx_date not in trgt_idx_array:

            idx_array = idx_array[:-1]

            val_array = val_array[:-1]

        else: trgt_idx_int += 1


        val_add_int = len(trgt_idx_array) - len(trgt_idx_array[:trgt_idx_int])

        val_add_array = np.asarray([sh_val_array[len(sh_val_array) - 1]] * val_add_int)


        idx_array = np.append(idx_array, trgt_idx_array[trgt_idx_int:])

        val_array = np.append(val_array, val_add_array)

    elif trgt_last_idx_date < sh_last_idx_date:

        sh_idx_int = 0

        while sh_idx_array[sh_idx_int] < trgt_last_idx_date:

            sh_idx_int += 1


        if trgt_last_idx_date in sh_idx_array:

            sh_idx_int += 1


        idx_array = copy.deepcopy(sh_idx_array[:sh_idx_int])

        val_array = copy.deepcopy(sh_val_array[:sh_idx_int])


        if trgt_last_idx_date not in sh_idx_array:

            idx_array = np.append(idx_array, trgt_last_idx_date)

            val_array = np.append(val_array, sh_val_array[sh_idx_int])


    sh1_series = pd.Series(val_array, index = idx_array, name = sh_series.name)

    return sh1_series


# In[19]:


#*******************************************************************************************
 #
 #  Function Name:  rtn_series_aligned_middle
 #
 #  Function Description:
 #      This function aligns two series through interpolation. The function assumes that 
 #      the two series have the same beginning and ending indices.
 #
 #
 #  Return Type: series
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  series         sh_series        The parameter is the input series.
 #  series         trgt_series      The parameter is the target series.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George           
 #
 #******************************************************************************************/

def rtn_series_aligned_middle \
        (sh_series:   pd.Series, 
         trgt_series: pd.Series) \
-> pd.Series:

    if  sh_series.index[0] != trgt_series.index[0]:

        logx.print_and_log_text \
            (f'\nThe two series must have the same starting index for alignment to proceed...\n')

        return sh_series

    elif sh_series.index[len(sh_series.index) - 1] \
            != trgt_series.index[len(trgt_series.index) - 1]:

        logx.print_and_log_text \
            (f'\nThe two series must have the same ending index for alignment to proceed...\n')

        return sh_series


    idx_array = val_array = np.asarray([])


    sh_idx_array = np.asarray(sh_series.index)

    sh_val_array = sh_series.to_numpy()


    sh_idx_int = 0


    for idx, ele in trgt_series.items():

        idx_array = np.append(idx_array, idx)

        val_array = np.append(val_array, sh_val_array[sh_idx_int])


        if idx == sh_idx_array[sh_idx_int]: 

            sh_idx_int += 1

        elif idx > sh_idx_array[sh_idx_int]:

            if sh_idx_array[sh_idx_int] in trgt_series.index \
                or idx in sh_series.index:

                while idx != sh_idx_array[sh_idx_int]: sh_idx_int += 1

                sh_idx_int += 1

            else:

                while idx > sh_idx_array[sh_idx_int]: sh_idx_int += 1


    sh1_series = pd.Series(val_array, index = idx_array, name = sh_series.name)

    return sh1_series              


# In[20]:


#*******************************************************************************************
 #
 #  Function Name:  rtn_series_aligned_with_target
 #
 #  Function Description:
 #      This function aligns an input series with the target series through alignment 
 #      and interpolation.
 #
 #
 #  Return Type: series
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  series         sh_series        The parameter is the input series.
 #  series         trgt_series      The parameter is the target series.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George           
 #
 #******************************************************************************************/

def rtn_series_aligned_with_target \
        (sh_series:   pd.Series, 
         trgt_series: pd.Series) \
-> pd.Series:

    sh1_series = rtn_series_aligned_front(sh_series, trgt_series)

    sh2_series = rtn_series_aligned_back(sh1_series, trgt_series)

    sh3_series = rtn_series_aligned_middle(sh2_series, trgt_series)

    return sh3_series


# In[21]:


#*******************************************************************************************
 #
 #  Function Name:  rtn_series_align_idxs_series
 #
 #  Function Description:
 #      This function aligns two series based on common index values and returns both
 #      series.
 #
 #
 #  Return Type: series, series
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  series         frt_series      The parameter is the first series.
 #  series         scd_series      The parameter is the second series.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George           
 #
 #******************************************************************************************/

def rtn_series_align_idxs_series \
        (frt_series: pd.Series, 
         scd_series: pd.Series) \
-> tuple[pd.Series, pd.Series]:

    merged_df \
        = pd.merge \
            (frt_series.to_frame(), 
             scd_series.to_frame(), 
             left_index = True, 
             right_index = True, 
             how = 'inner')

    return merged_df[frt_series.name], merged_df[scd_series.name]


# In[22]:


#******************************************************************************************
 #
 #  Function Name:  cnv_idxs_to_date
 #
 #  Function Description:
 #      This function receives a list with timestamp or date string indices, 
 #      converts them into dates, and returns them as an array.
 #
 #
 #  Return Type: array
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  object         input_obj        The parameter is the input object with date values.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def cnv_idxs_to_date(input_obj: object) -> np.ndarray:

    datetime_array = cnv_data_to_array(input_obj)


    if contains_all_datetime_obj(datetime_array):

        date_array = np.asarray([obj.date() for obj in datetime_array])

    elif contains_all_npdatetime_obj(datetime_array):

        date_array = np.asarray([pd.Timestamp(obj).date() for obj in datetime_array])

    elif contains_all_strings(datetime_array):

        date_array = np.asarray([pd.Timestamp(ts).date() for ts in datetime_array])

    elif contains_all_date_obj(datetime_array):

        date_array = copy.deepcopy(datetime_array)

    else: date_array = None


    return date_array


# In[23]:


#******************************************************************************************
 #
 #  Function Name:  rtn_data_obj_size
 #
 #  Function Description:
 #      This function receives a list or dataframe and returns its length.
 #
 #
 #  Return Type: integer or none
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  object         input_obj        The parameter is the input object.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def rtn_data_obj_size(input_obj: object) -> int:

    if isinstance(input_obj, list) \
        or isinstance(input_obj, np.ndarray):

        return len(input_obj[0])

    elif isinstance(input_obj, dict):

        return len(next(iter(input_obj.values())))

    elif isinstance(input_obj, pd.DataFrame):

        return len(input_obj.columns)

    else: return None


# In[24]:


#******************************************************************************************
 #
 #  Function Name:  rtn_series_with_unq_idxs
 #
 #  Function Description:
 #      This function receives a series and removes all redundant rows with the same index
 #      but leaves the row with the last instance of an index.
 #
 #
 #  Return Type: series
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  series         input_series     The parameter is the input series.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def rtn_series_with_unq_idxs(input_series: pd.Series) -> pd.Series:

    data_series = input_series.copy().dropna()

    if len(data_series) <= 1: return data_series


    last_idx_int = len(data_series) - 1

    idx_array = vals_array = np.asarray([])


    for idx, ele in enumerate(data_series):

        if idx < last_idx_int:

            if (data_series.index[idx]) != (data_series.index[idx + 1]):

                idx_array = np.append(idx_array, data_series.index[idx])

                vals_array = np.append(vals_array, data_series.iloc[idx])

        elif idx == last_idx_int:

            if (data_series.index[idx]) != (data_series.index[idx - 1]):

                idx_array = np.append(idx_array, data_series.index[idx])

                vals_array = np.append(vals_array, data_series.iloc[idx])


    rtn_series = pd.Series(vals_array, index = idx_array)

    return rtn_series


# In[25]:


#******************************************************************************************
 #
 #  Function Name:  rtn_date_idxs
 #
 #  Function Description:
 #      This function receives a series with timestamps for indices, converts those
 #      timestamps to dates, and returns the new series.
 #
 #
 #  Return Type: series
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  series         input_series     The parameter is the input series.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def rtn_date_idxs(input_series: pd.Series) -> pd.Series:

    data_series = input_series.dropna()


    idx_array = cnv_idxs_to_date(data_series.index)

    if idx_array is None: return None


    values_array = data_series.to_numpy()


    upd_series = pd.Series(values_array, index = idx_array, name = data_series.name)

    return upd_series


# In[26]:


#*******************************************************************************************
 #
 #  Function Name:  rtn_prior_date
 #
 #  Function Description:
 #      This function returns the prior date based on the number of days.
 #
 #
 #  Return Type: string
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  string         date             The parameter is the date.
 #  integer        days_int         The parameter is the number of days
 #  string         date_fmt         The parameter is the date format.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def rtn_prior_date \
        (date:     str, 
         days:     int = 365, 
         date_fmt: str = '%Y-%m-%d') \
-> str:

    curr_date_obj = dt.datetime.strptime(date, date_fmt)

    tmp_date_obj  = curr_date_obj.date() - dt.timedelta(days = days)

    prior_date    = dt.datetime.strftime(tmp_date_obj, date_fmt)

    return prior_date


# In[27]:


#*******************************************************************************************
 #
 #  Function Name:  rtn_future_date
 #
 #  Function Description:
 #      This function returns the future date based on the number of days.
 #
 #
 #  Return Type: string
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  string         date             The parameter is the date.
 #  integer        days             The parameter is the number of days
 #  string         date_fmt         The parameter is the date format.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def rtn_future_date \
        (date:     str, 
         days:     int = 365, 
         date_fmt: str = '%Y-%m-%d') \
-> str:

    curr_date_obj = dt.datetime.strptime(date, date_fmt)

    tmp_date_obj = curr_date_obj.date() + dt.timedelta(days = days)

    future_date = dt.datetime.strftime(tmp_date_obj, date_fmt)

    return future_date


# In[28]:


#*******************************************************************************************
 #
 #  Function Name:  rtn_norm_date_idx
 #
 #  Function Description:
 #      This function returns a series list where the all the series possess 
 #      a common index.
 #
 #
 #  Return Type: list
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  list           input_list       The parameter is the unsorted input series list 
 #                                  of date strings with the format, yyyy-mm-dd.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def rtn_norm_date_idx(input_list: list) -> list:

    sorted_list = sorted(input_list, key = len)


    for idx, series in enumerate(sorted_list):

        curr_list = series.index.tolist()

        new_list  = [ele[5:] for ele in curr_list]


        if idx >= 1: tmp_list = [ele for ele in tmp_list if ele in new_list]

        else:        tmp_list = new_list.copy()


    return tmp_list


# In[29]:


#*******************************************************************************************
 #
 #  Function Name:  rtn_norm_series_list_df
 #
 #  Function Description:
 #      This function returns a dataframe from a series list normalized 
 #      from a common index with a date string format, yyyy-mm-dd.
 #
 #
 #  Return Type: dataframe
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  list           input_list       The parameter is a input series list.
 #  list           omit_list        The parameter is the omitted series indices list.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def rtn_norm_series_list_df \
        (input_list: list,
         omit_list:  list = None) \
-> pd.DataFrame:

    curr_list = input_list.copy()


    if omit_list is not None: 

        curr_list = [x for i, x in enumerate(curr_list) if i not in omit_list]


    norm_idx_list = rtn_norm_date_idx(curr_list)

    norm_list = []


    for idx, series in enumerate(curr_list):

        idx_list = [x[5:] for x in curr_list[idx].index.tolist()]

        curr_list[idx] = curr_list[idx].set_axis(idx_list)


        temp_list = []

        for j, x in enumerate(curr_list[idx]):

            if str(curr_list[idx].index[j]) in norm_idx_list: temp_list.append(x)


        norm_series = pd.Series(temp_list, index = norm_idx_list)

        norm_series.name = curr_list[idx].name


        norm_list.append(norm_series)


    data_df = pd.DataFrame(norm_list).transpose()

    return data_df


# In[ ]:




