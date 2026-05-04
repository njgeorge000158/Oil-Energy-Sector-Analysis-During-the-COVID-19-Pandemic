#!/usr/bin/env python
# coding: utf-8

# In[1]:


#*******************************************************************************************
 #
 #  File Name:  pandasx.py
 #
 #  File Description:
 #      This Python script, pandasx.py, contains Python functions for processing
 #      Pandas data structures. Here is the list:
 #
 #  get_google_colab
 #  get_table_conversion
 #  get_format_dict
 #  get_style_dict
 #
 #  set_google_colab
 #  set_table_conversion
 #  set_format_dict
 #  set_style_dict
 #
 #  highlight_high_low_rows
 #  highlight_val_row
 #  highlight_median_row
 #  highlight_median_col
 #  highlight_bool_col
 #  highlight_true_row
 #  highlight_best_degree
 #  highlight_top_two
 #
 #  fmt_df_from_dict
 #  sv_img_rtn_styler
 #
 #  rtn_std_fmt_styler
 #  rtn_fmt_tbl
 #  rtn_fmt_rows
 #  rtn_df_desc
 #  rtn_fmt_desc
 #
 #  disp_df_col_cnts
 #  disp_df_col_unq_val
 #  disp_series_unq_val_cnts
 #  disp_series_list_stats
 #
 #  rtn_stats_list
 #  rtn_smry_stats_as_df
 #  rtn_stats_styler_from_series
 #  rtn_stats_styler_from_series_list
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  04/11/2024          Initial Development                         Nicholas J. George
 #  02/18/2026          Upgraded Module                             Nicholas J. George
 #
 #******************************************************************************************/

import dtypesx
import logx

import copy

import dataframe_image as dfi
import numpy           as np
import pandas          as pd

pd.options.mode.chained_assignment = None


# In[2]:


CONSTANT_LOCAL_FILE_NAME = 'pandasx.py'


# In[3]:


config_dict \
    = {'google_colab':     False,
       'table_conversion': 'selenium'}

fmt_dict \
    = {'text':         '{:}',
       'int':          '{:,}',
       'flt':          '{:,.2f}',
       'flt_int':      '{:,.0f}',
       'regr_flt':     '{:,.4f}',
       'pct':          '{:,.2%}',
       'pct_flt':      '{:,.2f}%',
       'pct_int':      '{:,}%',
       'curr_int':     '${:,}',
       'curr_flt':     '${:,.2f}',
       'curr_flt_int': '${:,.0f}',
       'tmpf_int':     '{:,}° F',
       'tmpc_int':     '{:,}° C',
       'tmpf_flt':     '{:,.2f}° F',
       'tmpc_flt':     '{:,.2f}° C',
       'eqn_coeff_prec': 4}

style_dict \
    = {'table_styles': [{'selector': 'caption',
                         'props':    [('color', 'black'),
                                      ('font-size', '20px'),
                                      ('font-style', 'bold'),
                                      ('text-align', 'center')]}],
       'properties':   {'text-align': 'center',
                        'border':     '1.3px solid red',
                        'color':      'blue'},
       'format': {'precision': 2,
                  'thousands': ',',
                  'decimal':   '.'},
       'caption': {'selector': 'caption',
                   'props':    [('font-size',   '16px'),
                                ('font-weight', 'bold'),
                                ('text-align',  'center'),
                                ('caption-side', 'top')]}}

stats_dict \
    = {'idx': np.array(['mean', 'median', 'mode', 'variance', 'std_dev', 'sem',
                        'minimum', '25%', '50%', '75%', 'maximum', 'count']),
       'format': {'mean':     lambda x: f'{x:.4f}',
                  'median':   lambda x: f'{x:.4f}',
                  'mode':     lambda x: f'{x:.4f}',
                  'variance': lambda x: f'{x:.4f}',
                  'std_dev':  lambda x: f'{x:.4f}',
                  'sem':      lambda x: f'{x:.4f}',
                  'minimum':  lambda x: f'{x:.2f}',
                  '25%':      lambda x: f'{x:.2f}',
                  '50%':      lambda x: f'{x:.2f}',
                  '75%':      lambda x: f'{x:.2f}',
                  'maximum':  lambda x: f'{x:.2f}',
                  'count':    lambda x: f'{x:.0f}'},
       'desc': {'count': lambda x: f'{x:,.0f}',
                'mean':  lambda x: f'{x:,.2f}',
                'std':   lambda x: f'{x:,.2f}',
                'min':   lambda x: f'{x:,.0f}',
                '25%':   lambda x: f'{x:,.2f}',
                '50%':   lambda x: f'{x:,.2f}',
                '75%':   lambda x: f'{x:,.2f}',
                'max':   lambda x: f'{x:,.0f}'}}


# In[4]:


#*******************************************************************************************
 #
 #  Function Name:  get_google_colab
 #
 #  Function Description:
 #      This function returns the configuration dictionary value.
 #
 #
 #  Return Type: bool
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
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_google_colab() -> bool:    return config_dict['google_colab']
def get_table_conversion() -> str: return config_dict['table_conversion']
def get_format_dict()-> dict:      return copy.deepcopy(fmt_dict)
def get_style_dict()-> dict:       return copy.deepcopy(style_dict)
def get_stats_dict()-> dict:       return copy.deepcopy(stats_dict)


# In[5]:


#*******************************************************************************************
 #
 #  Function Name:  set_google_colab
 #
 #  Function Description:
 #      This function sets the global boolean for google colaboratory.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  boolean        input_bool       The parameter is the input boolean value.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_google_colab(input_bool: bool):

  global config_dict

  config_dict['google_colab'] = input_bool


# In[6]:


#*******************************************************************************************
 #
 #  Function Name:  set_table_conversion
 #
 #  Function Description:
 #      This function sets the global table conversion specifier.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  string         tbl_conv         The parameter is the new table conversion specifier.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_table_conversion(tbl_conv: str):

  global config_dict

  config_dict['table_conversion'] = tbl_conv


# In[7]:


#*******************************************************************************************
 #
 #  Function Name:  set_format_dict
 #
 #  Function Description:
 #      This function sets the global format dictionary for objects.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  dictionary     upd_dict         The parameter is the updated format dictionary.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_format_dict(upd_dict: dict):

  global fmt_dict

  fmt_dict = copy.deepcopy(upd_dict)


# In[8]:


#*******************************************************************************************
 #
 #  Function Name:  set_style_dict
 #
 #  Function Description:
 #      This function sets the global style dictionary for pandas dataframes and stylers.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  dict           upd_dict         The parameter is the updated style dictionary.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_style_dict(upd_dict:dict):

  global style_dict

  style_dict = copy.deepcopy(upd_dict)


# In[9]:


#*******************************************************************************************
 #
 #  Function Name:  set_stats_dict
 #
 #  Function Description:
 #      This function sets the global statistics format dictionary for dataframes 
 #      and stylers.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  dictionary     upd_dict         The parameter is the updated statistics dictionary.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_stats_dict(upd_dict: dict):

  global stats_dict

  stats_dict = copy.deepcopy(upd_stats_dict)


# In[10]:


#*******************************************************************************************
 #
 #  Function Name:  highlight_high_low_rows
 #
 #  Function Description:
 #      This function highlights rows with the highest and lowest values in a column.
 #
 #
 #  Return Type: list[str]
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  series         row              The parameter is the dataframe row.
 #  string         col              The parameter is the dataframe column name.
 #  dataframe      df               The parameter is the input dataframe.
 #  string         h_clr            The parameter is the high value background color.
 #  string         l_clr            The parameter is the low value background color.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def highlight_high_low_rows \
    (row:   pd.Series,
     col:   str,
     df:    pd.DataFrame,
     h_clr: str = 'mistyrose',
     l_clr: str = 'greenyellow') \
-> list[str]:

    min_val = df[col].min()

    max_val = df[col].max()


    if row[col]   == min_val: style = f'background-color: {l_clr}'

    elif row[col] == max_val: style = f'background-color: {h_clr}'

    else: style = ''


    return [style for _ in row]


# In[11]:


#*******************************************************************************************
 #
 #  Function Name:  highlight_val_row
 #
 #  Function Description:
 #      This function highlights a row where its value is equal to the value in a column.
 #
 #
 #  Return Type: string
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  series         row              The parameter is the dataframe row
 #  string         col              The parameter is the column name.
 #  object         val              The parameter is the dataframe cell value.
 #  string         clr              The parameter is the highlight color.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def highlight_val_row \
        (row: pd.Series,
         col: str,
         val: object,
         clr: str = 'greenyellow') \
-> str:

    if row[col] == val: style = f'background-color: {clr}'

    else: style = ''

    return [style for _ in row]


# In[12]:


#*******************************************************************************************
 #
 #  Function Name:  highlight_median_row
 #
 #  Function Description:
 #      This function highlights all cells in a row if that row's value in col is equal 
 #      to or closest to the column median. For even-length columns where the median 
 #      falls between two values, highlights the row whose value is nearest to that 
 #      median. The function is designed for use with df.style.apply(..., axis=1).
 #
 #
 #  Return Type: list[str]
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  series         row              The parameter is the single row passed by .apply.
 #  string         col              The parameter is the column used to identify the 
 #                                  median row.
 #  dataframe      df               The parameter is the source dataframe, which is used 
 #                                  to compute the median and find the nearest value.
 #  string         clr              The parameter is the CSS color name or hex string.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def highlight_median_row \
    (row:    pd.Series,
     col:    str,
     df:     pd.DataFrame,
     clr:    str = 'lemonchiffon') \
-> list[str]:

    median_val  = df[col].median()

    nearest_val = df[col].iloc[(df[col] - median_val).abs().argsort().iloc[0]]

    style = f'background-color: {clr}' if row[col] == nearest_val else ''

    return [style for _ in row]


# In[13]:


#*******************************************************************************************
 #
 #  Function Name:  highlight_median_col
 #
 #  Function Description:
 #      This function highlights cells in a column whose value equals the column median,
 #      or for even-length columns where the median falls between two values, highlights 
 #      the two middle values whose average produces the median.
 #
 #
 #  Return Type: list[str]
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  series         col              The parameter is the single column passed by .apply.
 #  string         clr              The parameter is the CSS color name or hex string.
 #  float          tol              The parameter is absolute tolerance for float equality.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def highlight_median_col \
    (col: pd.Series,
     clr: str   = 'lemonchiffon',
     tol: float = 1e-9) \
-> list[str]:

    median_val = col.median()

    h_clr  = f'background-color: {clr}'


    if (col - median_val).abs().min() <= tol:

        return [h_clr if abs(v - median_val) <= tol else '' for v in col]


    sort_col_series = col.dropna().sort_values()

    mid_pt_int      = len(sort_col_series) // 2

    lwr_mid_val_flt = sort_col_series.iloc[mid_pt_int - 1]

    upr_mid_val_flt = sort_col_series.iloc[mid_pt_int]


    return \
        [h_clr \
         if (abs(v - lwr_mid_val_flt) <= tol or abs(v - upr_mid_val_flt) <= tol) \
         else '' \
         for v in col]


# In[14]:


#*******************************************************************************************
 #
 #  Function Name:  highlight_bool_col
 #
 #  Function Description:
 #      This function colors the true and false vaues in a dataframe styler column.
 #
 #
 #  Return Type: string
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  boolean        val              The parameter is the dataframe cell value.
 #  string         tr_clr           The parameter is the color for true values
 #  string         fs_clr           The parameter is the color for true values
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def highlight_bool_col \
        (val:    bool, 
         tr_clr: str = 'mistyrose', 
         fs_clr: str = 'lemonchiffon') \
-> str:

    if val == True: color = 'mistyrose' 

    else: color = 'lemonchiffon'

    return f'background-color: {color}'


# In[15]:


#*******************************************************************************************
 #
 #  Function Name:  highlight_true_row
 #
 #  Function Description:
 #      This function colors a dataframe styler row lime if the specified column has 
 #      a true value.
 #
 #
 #  Return Type: list
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  boolean        val              The parameter is the dataframe cell value.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def highlight_true_row(row: object, col: str) -> list:

    if row[col] == True: return ['background-color: lime'] * len(row)

    else: return [''] * len(row)


# In[16]:


#*******************************************************************************************
 #
 #  Function Name:  highlight_row_val
 #
 #  Function Description:
 #      This function colors the row with the highest column value.
 #
 #
 #  Return Type: list
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  series         row              The parameter is the dataframe row.
 #  string         col              The parameter is the column name.
 #  object         h_val            The parameter is the high value.
 #  string         h_clr            The parameter is the highlight color.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def highlight_row_val \
        (row:    pd.Series,
         col:    str,
         h_val:  object,
         h_clr:  str = 'greenyellow') -> str:

    if row[col] == h_val: style = f'background-color: {h_clr}'

    else: style = ''

    return [style for _ in row]


# In[17]:


#*******************************************************************************************
 #
 #  Function Name:  highlight_top_two
 #
 #  Function Description:
 #      This function finds and colors the top two values in a series.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  series         series           The parameter is the input series.
 #  string         props_max        The parameter is the css color for the top value.
 #  string         props_second     The parameter is the css color for the second largest 
 #                                  value.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def highlight_top_two \
        (series:       pd.Series,
         props_max:    str = '', 
         props_second: str = ''):

    top_two_array = series.nlargest(2).unique()

    if len(top_two_array) < 2:

        is_max = series == series.max()

        return [props_max if v else '' for v in is_max]


    max_val = top_two_array[0]

    second_max_val = top_two_array[1]


    return \
        [props_max \
         if v == max_val \
         else (props_second if v == second_max_val else '') \
         for v in series]


# In[18]:


#*******************************************************************************************
 #
 #  Function Name:  fmt_df_from_dict
 #
 #  Function Description:
 #      This function formats a dataframe based on a format dictionary 
 #      and returns a styler.
 #
 #
 #  Return Type: styler
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  dataframe      input_df         The parameter is the input dataframe.
 #  dictionary     input_dict       The parameter is the format dictionary.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def fmt_df_from_dict \
        (input_df:   pd.DataFrame, 
         input_dict: dict) \
-> object:

    input_styler = input_df.style

    nmbr_cols = len(input_styler.columns)


    for idx, fmt in input_dict.items():

        row = input_styler.index.get_loc(idx)

        for col in range(nmbr_cols):

            input_styler._display_funcs[(row, col)] = fmt


    return input_styler


# In[19]:


#*******************************************************************************************
 #
 #  Function Name:  sv_img_rtn_styler
 #
 #  Function Description:
 #      This function saves the styler object as a png image then returns the object.
 #
 #
 #  Return Type: styler
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  styler         input_styler     The parameter is the input styler object.
 #  string         title            The parameter is the table title.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def sv_img_rtn_styler \
        (input_styler: object, 
         title:        str) \
-> object:

    if logx.logs_config_dict['img_mode'] == True:

        dfi.export \
            (input_styler,
             logx.curr_img_file_path(title, 'png'),
             table_conversion = config_dict['table_conversion'],
             max_rows = -1, max_cols = -1)

    return input_styler


# In[20]:


#*******************************************************************************************
 #
 #  Function Name:  rtn_std_fmt_styler
 #
 #  Function Description:
 #      This function returns a styler object in standard format from a dataframe.
 #
 #
 #  Return Type: styler
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  dataframe      input_df         The parameter is the input dataframe.
 #  string         title            The parameter is the table title.
 #  boolean        hide_idx_bool    The optional parameter indicates whether the index
 #                                  column is hidden or not.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def rtn_std_fmt_styler \
        (input_df:      pd.DataFrame,
         title:         str,
         hide_idx_bool: bool = True) \
-> object:

    fmt_styler \
        = input_df \
            .style \
            .set_caption(title) \
            .set_table_styles(style_dict['table_styles']) \
            .set_properties(**style_dict['properties']) \
            .format \
                (precision = style_dict['format']['precision'],
                 thousands = style_dict['format']['thousands'],
                 decimal = style_dict['format']['decimal']) \
            .set_table_styles([style_dict['caption']])


    if hide_idx_bool == True: return fmt_styler.hide()

    else: return fmt_styler


# In[21]:


#*******************************************************************************************
 #
 #  Function Name:  rtn_fmt_tbl
 #
 #  Function Description:
 #      This function returns a formatted table from a dataframe.
 #
 #
 #  Return Type: styler
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  dataframe      input_df         The parameter is the input dataframe.
 #  string         title            The parameter is the table title.
 #  integer        line_cnt_int     The parameter is the number of displayed records.
 #  boolean        hide_idx_bool    The parameter indicates whether the index is present.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def rtn_fmt_tbl \
        (input_df:      pd.DataFrame,
         title:         str,
         line_cnt_int:  int = 10,
         hide_idx_bool: bool = True) \
-> object:

    curr_styler = rtn_std_fmt_styler(input_df.head(line_cnt_int), title, hide_idx_bool)

    return sv_img_rtn_styler(curr_styler, title)


# In[22]:


#*******************************************************************************************
 #
 #  Function Name:  rtn_fmt_rows
 #
 #  Function Description:
 #      This function formats the rows in a pandas styler and returns it.
 #
 #
 #  Return Type: styler
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  styler         input_styler     The parameter is the input styler.
 #  dictionary     input_dict       The parameter is the dicitionary with the format 
 #                                  specifications.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def rtn_fmt_rows \
        (input_styler: object,
         input_dict:   dict) \
-> object:

    for k, v in input_dict.items():

        row = input_styler.index.get_loc(k)

        for col in range(len(input_styler.columns)):

            input_styler._display_funcs[(row, col)] = v

    return input_styler


# In[23]:


#*******************************************************************************************
 #
 #  Function Name:  rtn_df_desc
 #
 #  Function Description:
 #      This function takes a dataframe and returns the its formatted data statistics.
 #
 #
 #  Return Type: styler
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  dataframe      input_df         The parameter is the input dataframe.
 #  string         title            The parameter is the description title.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def rtn_df_desc \
        (input_df: pd.DataFrame, 
         title:    str) \
-> object:

    desc_df = input_df.describe()

    desc_styler \
        = rtn_fmt_rows(desc_df.style, stats_dict['desc']) \
            .set_caption(title) \
            .set_table_styles(style_dict['table_styles']) \
            .set_properties(**style_dict['properties'])

    return desc_styler


# In[24]:


#*******************************************************************************************
 #
 #  Function Name:  rtn_fmt_desc
 #
 #  Function Description:
 #      This function returns a formatted dataframe description.
 #
 #
 #  Return Type: styler
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  dataframe      input_df         The parameter is the input dataframe.
 #  string         title            The parameter is the description title.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def rtn_fmt_desc \
        (input_df: pd.DataFrame,
         title:    str) \
-> object:

    df_styler = sv_img_rtn_styler(rtn_df_desc(input_df, title), title)

    return df_styler


# In[25]:


#*******************************************************************************************
 #
 #  Function Name:  disp_df_col_cnts
 #
 #  Function Description:
 #      This function displays a dataframe's column counts.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  dataframe      input_df         The parameter is the input dataframe.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def disp_df_col_cnts(input_df: pd.DataFrame):

    for i, col in enumerate(input_df.columns):

        msg = '\033[1m' + f'{col}: ' + '{:,}\n'.format(input_df[col].nunique()) + '\033[0m'

        logx.print_and_log_text(msg)


# In[26]:


#*******************************************************************************************
 #
 #  Function Name:  disp_df_col_unq_val
 #
 #  Function Description:
 #      This function displays the dataframe column unique values.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  dataframe      input_df         The parameter is the input dataframe.
 #  boolean        rvs_bool         The parameter indicates whether the script sorts 
 #                                  the list in reverse order or not.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def disp_df_col_unq_val \
        (input_df: pd.DataFrame,
         rvs_bool: bool = False):

    for i, col in enumerate(input_df.columns):

        logx.print_and_log_text \
            ('\033[1m' + f'{col}:\n'
             + f'{sorted(input_df[col].unique().tolist(), reverse = rvs_bool)}\n\n'
             + '\033[0m')


# In[27]:


#*******************************************************************************************
 #
 #  Function Name:  disp_series_unq_val_cnts
 #
 #  Function Description:
 #      This function displays the sorted unique value count of a series then returns
 #      the sorted series.
 #
 #
 #  Return Type: series
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  series         input_series    The parameter is the input series.
 #  string         series_name     The parameter is the sorted series name.
 #  boolean        asc_bool        The parameter indicates wheher the script sorts the
 #                                 series in ascending order or not.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def disp_series_unq_val_cnts \
        (input_series: pd.Series,
         series_name:  str = 'output_series',
         asc_bool:     bool = False) \
-> pd.Series:

    srtd_series = input_series.value_cnts().sort_values(ascending = asc_bool)

    srtd_series.name = series_name


    for k, v in srtd_series.items():

        logx.print_and_log_text('\033[1m' + str(k) + '\t' + str(v) + '\n' + '\033[0m')


    return srtd_series


# In[28]:


#*******************************************************************************************
 #
 #  Function Name:  disp_series_list_stats
 #
 #  Function Description:
 #      This subroutine calculates and displays summary statistics for each drug
 #      in the series list.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  list           input_list       The parameter is the input series list.
 #  array          title_array      The parameter is the list of drug regimen names.
 #  string         section_name     The parameter is the section name.
 #  string         stats_type       The parameter is the statistics type.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def disp_series_list_stats \
        (input_list:   list,
         title_array:  np.ndarray,
         section_name: str,
         stats_type:   str):

    for idx, title in enumerate(title_array):

        stats_df = rtn_smry_stats_as_df(input_list[idx])

        caption \
            = 'Table ' \
              + section_name \
              + f'.{idx + 1}: ' \
              + stats_type \
              + f' Statistics for {title}'


        curr_styler = rtn_std_fmt_styler(stats_df, caption)

        curr_styler = sv_img_rtn_styler(curr_styler, caption)


        display(curr_styler)


# In[29]:


#*******************************************************************************************
 #
 #  Function Name:  rtn_stats_list
 #
 #  Function Description:
 #      This function returns the statistics for a series as a list.
 #
 #
 #  Return Type: list
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

def rtn_stats_list(input_series: pd.Series) -> list:

    stats_list \
        = [input_series.mean(),
           input_series.median(),
           input_series.mode()[0],
           input_series.var(),
           input_series.std(),
           input_series.sem(),
           input_series.min(),
           input_series.describe().loc['25%'],
           input_series.describe().loc['50%'],
           input_series.describe().loc['75%'],
           input_series.max(),
           input_series.count()]

    return stats_list


# In[30]:


#*******************************************************************************************
 #
 #  Function Name:  rtn_smry_stats_as_df
 #
 #  Function Description:
 #      This function converts a data series into summary statistics, assigns
 #      the statistics to a dataframe, and returns it.
 #
 #
 #  Return Type: dataframe
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

def rtn_smry_stats_as_df(input_series: pd.Series) -> pd.DataFrame:

    quartiles_series = input_series.quantile([0.25, 0.50, 0.75])


    lower_quartile_flt = quartiles_series[0.25]

    upper_quartile_flt = quartiles_series[0.75]


    interquartile_range_flt = upper_quartile_flt - lower_quartile_flt


    lower_bound_flt = lower_quartile_flt - (1.5 * interquartile_range_flt)

    upper_bound_flt = upper_quartile_flt + (1.5 * interquartile_range_flt)


    outliers_series \
        = input_series.loc \
            [(input_series < lower_bound_flt) | (input_series > upper_bound_flt)]


    outlier_count_int = len(outliers_series)


    stats_dict_list \
        = [{'lower_quartile': lower_quartile_flt,
            'upper_quartile': upper_quartile_flt,
            'interquartile_range': interquartile_range_flt,
            'median': quartiles_series[0.5],
            'lower_boundary': lower_bound_flt,
            'upper_boundary': upper_bound_flt,
            'outlier_count': outlier_count_int}]


    stats_df = pd.DataFrame(stats_dict_list)

    return stats_df


# In[31]:


#*******************************************************************************************
 #
 #  Function Name:  rtn_stats_styler_from_series
 #
 #  Function Description:
 #      This function receives a series, calculates its statistical values, places them
 #      in a dataframe, formats the dataframe as a syler and returns it to the caller.
 #
 #
 #  Return Type: styler
 #
 #
 #  Function Parameters:
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  series         input_series     The parameter is the input series.
 #  string         title            The parameter is the title of the styler.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def rtn_stats_styler_from_series \
        (input_series: pd.Series,
         title:        str) \
-> object:

    stats_list = rtn_stats_list(input_series)

    stats_df \
        = pd.DataFrame \
            (stats_list,
             columns = [input_series.name],
             index = stats_dict['idx'])

    stats_styler \
        = fmt_df_from_dict(stats_df, stats_dict['format']) \
            .set_caption(title) \
            .set_table_styles(style_dict['table_styles']) \
            .set_properties(**style_dict['properties'])

    stats_styler = sv_img_rtn_styler(stats_styler, title)

    return stats_styler


# In[32]:


#*******************************************************************************************
 #
 #  Function Name:  rtn_stats_styler_from_series_list
 #
 #  Function Description:
 #      This function receives a series list, calculates the statistical values 
 #      of each series, places them in a dataframe, and returns the styler to 
 #      the caller.
 #
 #
 #  Return Type: styler
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  list           input_list       The parameter is the input series list.
 #  string         title            The parameter is the title for the styler.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def rtn_stats_styler_from_series_list \
        (input_list: list,
         title:      str) \
-> object:

    for idx, series in enumerate(input_list):

        stats_flt_array = rtn_stats_as_array(series)

        temp_df \
            = pd.DataFrame \
                (stats_flt_array,
                 columns = [series.name],
                 index = stats_dict['idx'])


        if idx != 0: stats_df = pd.concat([stats_df, temp_df], axis = 1)

        else: stats_df = temp_df.copy()


    stats_styler \
        = fmt_df_from_dict(stats_df, stats_dict['format']) \
            .set_caption(title) \
            .set_table_styles(style_dict['table_styles']) \
            .set_properties(**style_dict['properties'])


    return stats_styler


# In[ ]:




