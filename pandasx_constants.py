#!/usr/bin/env python
# coding: utf-8

# In[1]:


#*******************************************************************************************
 #
 #  File Name:  pandasx_constants.py
 #
 #  File Description:
 #      This Python script, pandasx_constants.py, contains generic Python constants
 #      for for processing Pandas data structures
 #
 #
 #  Date            Description                             Programmer
 #  ----------      ------------------------------------    ------------------
 #  04/20/2024      Initial Development                     Nicholas J. George
 #
 #******************************************************************************************/


# In[2]:


CONSTANT_LOCAL_FILE_NAME = 'pandasx_constants.py'


# In[3]:


EQUATION_COEFFICIENT_PRECISION = 4


GENERAL_TEXT_FORMAT = '{:}'

INTEGER_FORMAT = '{:,}'

FLOAT_FORMAT = '{:,.2f}'

PERCENT_FORMAT = '{:,.2%}'

FLOAT_AS_INTEGER_FORMAT = '{:,.0f}'

CURRENCY_INTEGER_FORMAT = '$' + INTEGER_FORMAT

CURRENCY_FLOAT_FORMAT = '$' + FLOAT_FORMAT

CURRENCY_FLOAT_AS_INTEGER_FORMAT = '$' + FLOAT_AS_INTEGER_FORMAT

PERCENT_FLOAT_FORMAT = FLOAT_FORMAT + '%'

PERCENT_INTEGER_FORMAT = INTEGER_FORMAT + '%'

TEMPERATURE_FLOAT_FORMAT = FLOAT_FORMAT +'° F'


# In[ ]:




