#!/usr/bin/env python
# coding: utf-8

# In[1]:


#*******************************************************************************************
 #
 #  File Name:  logx.py
 #
 #  File Description:
 #      The Python script, logx.py, contains generic Python functions for writing 
 #      information to log files.  Here is the list:
 #
 #  get_logs_config_dict
 #  get_log_mode
 #  get_image_mode
 #  get_program_designation
 #  get_logs_directory_path
 #  set_logs_config_dict
 #  get_images_directory_path
 #  get_resources_directory_path
 #  get_sql_directory_path
 #  get_visualization_directory_path
 #  get_models_directory_path
 #  get_backups_directory_path
 #  get_base_log_file_name
 #
 #  set_log_mode
 #  set_image_mode
 #  set_program_designation
 #  set_logs_directory_path
 #  set_images_directory_path
 #  set_resources_directory_path
 #  set_sql_directory_path
 #  set_visualization_directory_path
 #  set_models_directory_path
 #  set_backups_directory_path
 #  set_base_log_file_name
 #
 #  curr_img_file_path
 #  curr_analysis_file_path
 #  curr_date_as_txt
 #  curr_timestp_as_txt
 #  curr_timept_with_msg
 #
 #  sv_png_rtn_styler
 #  rtn_delta
 #
 #  begin_program
 #  end_program
 #
 #  log_write_obj
 #  create_directory
 #  open_log_file
 #  print_and_log_text
 #  write_to_folder
 #
 #  save_matplotlib_image
 #  save_hvplot_map_image
 #  save_plotly_image
 #  save_folium_map_image
 #  save_map_image
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  04/11/2024          Initial Development                         Nicholas J. George
 #  02/18/2026          Upgraded Module                             Nicholas J. George
 #
 #******************************************************************************************/

import os
import copy
import folium

import dataframe_image   as dfi
import datetime          as dt
import matplotlib.pyplot as plt

import hvplot.pandas


# In[2]:


CONSTANT_LOCAL_FILE_NAME = 'logx.py'


# In[3]:


logs_config_dict \
    = {'logs_folder': './logs',
       'images_folder': './images',
       'resources_folder': './resources',
       'analysis_folder': './analysis',
       'sql_folder': './sql',
       'visual_folder': './visualization',
       'models_folder': './models',
       'backups_folder': './backups',
       'base_log_name': '_log.txt',
       'log_folder': '',
       'log_txt_file': None,
       'prgrm_dsgn': '',
       'bbox_inches': 'tight',
       'start': None,
       'end': None,
       'ts_fmt': '%Y/%m/%d %H:%M:%S',
       'log_mode': False,
       'img_mode': False}


# In[4]:


#*******************************************************************************************
 #
 #  Function Name:  get_logs_config_dict
 #                  get_log_mode
 #                  get_image_mode
 #                  get_program_designation
 #                  get_logs_directory_path
 #                  get_images_directory_path
 #                  get_resources_directory_path
 #                  get_visualzation_directory_path
 #                  get_models_directory_path
 #                  get_backups_directory_path
 #                  get_base_log_file_name
 #
 #  Function Description:
 #      The function returns the values from the configuration dictionary.
 #
 #
 #  Return Type: varies
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

def get_logs_config_dict() -> dict:           return copy.deepcopy(logs_config_dict)
def get_log_mode() -> str:                    return logs_config_dict['log_mode']
def get_image_mode() -> str:                  return logs_config_dict['img_mode']
def get_program_designation() -> str:         return logs_config_dict['prgrm_dsgn']
def get_logs_directory_path() -> str:         return logs_config_dict['logs_folder']
def get_images_directory_path() -> str:       return logs_config_dict['images_folder']
def get_resources_directory_path() -> str:    return logs_config_dict['resources_folder']
def get_sql_directory_path() -> str:          return logs_config_dict['sql_folder']
def get_visualzation_directory_path() -> str: return logs_config_dict['visual_folder']
def get_models_directory_path() -> str:       return logs_config_dict['models_folder']
def get_backups_directory_path() -> str:      return logs_config_dict['backups_folder']
def get_base_log_file_name() -> str:          return logs_config_dict['base_log_name']


# In[5]:


#*******************************************************************************************
 #
 #  Function Name:  set_logs_config_dict
 #
 #  Function Description:
 #      The function sets the configuration dictionary.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  dictionary     config_dict      The parameter is the new configuration dictionary.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_logs_config_dict(config_dict: dict):

    global logs_config_dict

    logs_config_dict = copy.deepcopy(config_dict)


# In[6]:


#*******************************************************************************************
 #
 #  Function Name:  set_log_mode
 #
 #  Function Description:
 #      The function sets the global log mode.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  boolean        mode_bool        The parameter is the new log mode.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_log_mode(mode_bool: bool):

    global logs_config_dict

    logs_config_dict['log_mode'] = mode_bool


# In[7]:


#*******************************************************************************************
 #
 #  Function Name:  set_image_mode
 #
 #  Function Description:
 #      The function sets the global image mode.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  boolean        mode_bool        The parameter is the new image mode.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_image_mode(mode_bool: bool):

    global logs_config_dict

    logs_config_dict['img_mode'] = mode_bool


# In[8]:


#*******************************************************************************************
 #
 #  Function Name:  set_program_designation
 #
 #  Function Description:
 #      The function sets the value for the global program designation string.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  string         prgrm_desig      The parameter is the text for the global program 
 #                                  designation.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_program_designation(prgrm_desig: str = ''):

    global logs_config_dict

    logs_config_dict['prgrm_dsgn'] = prgrm_desig


# In[9]:


#*******************************************************************************************
 #
 #  Function Name:  set_logs_directory_path
 #
 #  Function Description:
 #      The function sets the logs directory path.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  string         upd_dir_path     The parameter is the updated logs directory path.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_logs_directory_path(upd_dir_path: str):

    global logs_config_dict

    logs_config_dict['logs_folder'] = upd_dir_path


# In[10]:


#*******************************************************************************************
 #
 #  Function Name:  set_images_directory_path
 #
 #  Function Description:
 #      The function sets the images directory path.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  string         upd_dir_path     The parameter is the updated images directory path.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_images_directory_path(upd_dir_path: str):

    global logs_config_dict

    logs_config_dict['images_folder'] = upd_dir_path


# In[11]:


#*******************************************************************************************
 #
 #  Function Name:  set_resources_directory_path
 #
 #  Function Description:
 #      The function sets the resources directory path.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  string         upd_dir_path     The parameter is the updated resources directory path.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_resources_directory_path(upd_dir_path: str):

    global logs_config_dict

    logs_config_dict['resources_folder'] = upd_dir_path


# In[12]:


#*******************************************************************************************
 #
 #  Function Name:  set_sql_directory_path
 #
 #  Function Description:
 #      The function sets the sql directory path.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  string         upd_dir_path     The parameter is the updated sql directory path.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_sql_directory_path(upd_dir_path: str):

    global logs_config_dict

    logs_config_dict['sql_folder'] = upd_dir_path


# In[13]:


#*******************************************************************************************
 #
 #  Function Name:  set_visualzation_directory_path
 #
 #  Function Description:
 #      The function sets the visualzation directory path.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  string         upd_dir_path     The parameter is the updated visualization directory
 #                                  path.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_visualzation_directory_path(upd_dir_path: str):

    global logs_config_dict

    logs_config_dict['visual_folder'] = upd_dir_path


# In[14]:


#*******************************************************************************************
 #
 #  Function Name:  set_models_directory_path
 #
 #  Function Description:
 #      The function sets the models directory path.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  string         upd_dir_path     The parameter is the updated models directory path.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_models_directory_path(upd_dir_path: str):

    global logs_config_dict

    logs_config_dict['models_folder'] = upd_dir_path


# In[15]:


#*******************************************************************************************
 #
 #  Function Name:  set_backups_directory_path
 #
 #  Function Description:
 #      The function sets the backups directory path.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  string         upd_dir_path     The parameter is the updated backups directory path.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_backups_directory_path(upd_dir_path: str):

    global logs_config_dict

    logs_config_dict['backups_folder'] = upd_dir_path


# In[16]:


#*******************************************************************************************
 #
 #  Function Name:  set_base_log_file_name
 #
 #  Function Description:
 #      The function sets the base log file name.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  string         base_file_path   The parameter is the updated base file name.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_base_log_file_name(upd_file_name: str):

    global logs_config_dict

    logs_config_dict['base_log_name'] = upd_file_name


# In[17]:


#*******************************************************************************************
 #
 #  Function Name:  curr_img_file_path
 #
 #  Function Description:
 #      The function uses a plot's caption to determine the image file path.
 #
 #
 #  Return Type: string
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  string         caption          The parameter is the plot title.
 #  string         img_fmt          The parameter is the image format file suffix.    
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def curr_img_file_path \
        (caption: str = 'test', 
         img_fmt: str = '') \
-> str:

    img_file_path \
        = logs_config_dict['images_folder'] \
            + '/' + logs_config_dict['prgrm_dsgn'] \
            + ''.join(filter(str.isalnum, caption))

    if img_fmt != '': img_file_path += '.' + img_fmt


    return img_file_path


# In[18]:


#*******************************************************************************************
 #
 #  Function Name:  curr_analysis_file_path
 #
 #  Function Description:
 #      The function uses the title to determine the file path.
 #
 #
 #  Return Type: string
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  string         title            The parameter is the analysis title.
 #  string         img_fmt          The parameter is the file format suffix.    
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def curr_analysis_file_path \
        (title: str, 
         fmt:   str = 'txt') \
-> str:

    file_path \
        = logs_config_dict['analysis_folder'] + '/' \
            + logs_config_dict['prgrm_dsgn'] \
            + ''.join(filter(str.isalnum, title))

    file_path += '.' + fmt


    return file_path


# In[19]:


#*******************************************************************************************
 #
 #  Function Name:  curr_date_as_txt
 #
 #  Function Description:
 #      The function returns the current date as a formatted string for the names
 #      of log files.
 #
 #
 #  Return Type: string
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  string         fmt              The parameter is optional and specifies the date 
 #                                  format.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def curr_date_as_txt(fmt: str = '%Y%m%d') -> str: 

    return dt.date.today().strftime(fmt)


# In[20]:


#*******************************************************************************************
 #
 #  Function Name:  curr_timestp_as_txt
 #
 #  Function Description:
 #      The function returns the current date and time as a formatted string
 #      for timepoint entries in log files.
 #
 #
 #  Return Type: string
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  string         fmt              The parameter is optional and specifies the datetime 
 #                                  format.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def curr_timestp_as_txt(fmt: str = logs_config_dict['ts_fmt']) -> str: 

    return dt.datetime.now().strftime(fmt)


# In[21]:


#*******************************************************************************************
 #
 #  Function Name:  curr_timept_with_msg
 #
 #  Function Description:
 #      The function takes a message, formats it with a timestamp, and returns it 
 #      to the caller.
 #
 #
 #  Return Type: string
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  string         msg              The parameter is the optional message with the 
 #                                  timepoint.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def curr_timept_with_msg(msg: str = '') -> str: 

    return f'\nTimepoint: {curr_timestp_as_txt()}\n' + msg + '\n\n'


# In[22]:


#*******************************************************************************************
 #
 #  Function Name:  sv_png_rtn_styler
 #
 #  Function Description:
 #      The function saves the styler object as a png image file then returns it.
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
 #  string         caption          The parameter is the styler caption.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def sv_png_rtn_styler(input_styler, caption: str):

    if logs_config_dict['img_mode'] == True:

        dfi.export(input_styler, curr_img_file_path(caption, 'png'))

    return input_styler


# In[23]:


#*******************************************************************************************
 #
 #  Function Name:  rtn_delta
 #
 #  Function Description:
 #      The function returns the elapsed time based on a beginning and ending timestamp 
 #      strings.
 #
 #
 #  Return Type: string
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  string         start            The parameter is the start timestamp string.
 #  string         end              The parameter is the end timestamp string.
 #  string         fmt              The parameter is the timestamp format.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def rtn_delta(start: str, end: str, fmt: str) -> str:

    start_ts = dt.datetime.strptime(start, fmt)

    end_ts = dt.datetime.strptime(end, fmt)


    delta_ts = end_ts - start_ts


    total_seconds_int = int(delta_ts.total_seconds())

    hours_int = total_seconds_int // 3600

    minutes_int = (total_seconds_int % 3600) // 60

    seconds_int = total_seconds_int % 60    


    delta = f'{hours_int:02}:{minutes_int:02}:{seconds_int:02}'

    return delta


# In[24]:


#*******************************************************************************************
 #
 #  Function Name:  begin_program
 #
 #  Function Description:
 #      The function prints an announcement for the start of program execution, creates
 #      the appropriate folders, and writes the same announcement to the log file.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  string         prgrm_desig      The parameter is the program designation.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def begin_program(prgrm_desig: str = ''):

    global logs_config_dict


    create_directory(logs_config_dict['logs_folder'])

    create_directory(logs_config_dict['images_folder'])


    set_program_designation(prgrm_desig)

    open_log_file()


    if logs_config_dict['log_mode'] == True:

        logs_config_dict['start'] = curr_timestp_as_txt()

        print_and_log_text(f"Program execution has begun...\n")


# In[25]:


#*******************************************************************************************
 #
 #  Function Name:  end_program
 #
 #  Function Description:
 #      The function prints an end of program execution announcement, creates the 
 #      appropriate folders, and writes the same announcement to the log file.
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
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def end_program():

    global logs_config_dict


    if logs_config_dict['log_mode'] == True:

        logs_config_dict['end'] = curr_timestp_as_txt()


        delta \
            = rtn_delta \
                (start = logs_config_dict['start'], 
                 end = logs_config_dict['end'], 
                 fmt = logs_config_dict['ts_fmt'])


        print_and_log_text \
            (f"Program execution begins at {logs_config_dict['start']}.")

        print_and_log_text \
            (f"Program execution ends at {logs_config_dict['end']}.\n")

        print_and_log_text \
            ('Program execution ran for ' + delta + '.\n')


        logs_config_dict['log_txt_file'].close() 


# In[26]:


#*******************************************************************************************
 #
 #  Function Name:  log_write_obj
 #
 #  Function Description:
 #      The function takes an object as a parameter, and, if the global debug flag is true, 
 #      writes it to a debug file.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  object         input_obj        The parameter is the object to be written to the 
 #                                  log file.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def log_write_obj(input_obj: object):

    if logs_config_dict['log_mode'] == True:

        logs_config_dict['log_txt_file'].write(f'\n\n' + str(input_obj) + f'\n\n')


# In[27]:


#*******************************************************************************************
 #
 #  Function Name:  create_directory
 #
 #  Function Description:
 #      The function creates a folder if it does not exist.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  string         dir_path         The parameter is the directory name.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def create_directory(dir_path: str):

    exist_bool = os.path.exists(dir_path)

    if exist_bool == False:

        os.makedirs(dir_path)

        print(f'The script created directory, {dir_path}.\n')


# In[28]:


#*******************************************************************************************
 #
 #  Function Name:  open_log_file
 #
 #  Function Description:
 #      The function opens the log file for appending.  If it does not exist, the 
 #      function creates it.
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
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def open_log_file():

    global logs_config_dict

    logs_config_dict['log_folder'] \
        = logs_config_dict['logs_folder'] \
            + '/' + curr_date_as_txt() \
            + logs_config_dict['prgrm_dsgn'] \
            + logs_config_dict['base_log_name']

    if logs_config_dict['log_mode'] == True:

        logs_config_dict['log_txt_file'] = open(logs_config_dict['log_folder'], 'a')


# In[29]:


#*******************************************************************************************
 #
 #  Function Name:  print_and_log_text
 #
 #  Function Description:
 #      The function prints the received message then writes the message to the log file.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  string         msg              The parameter is the input message text.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def print_and_log_text(msg: str = ''):

    print(msg)

    if logs_config_dict['log_mode'] == True:

        logs_config_dict['log_txt_file'].write(curr_timept_with_msg(msg))    


# In[30]:


#*******************************************************************************************
 #
 #  Function Name:  write_to_folder
 #
 #  Function Description:
 #      The function writes the message to the analysis file.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  string         msg              The parameter is the input message text.
 #  string         title            The parameter is the analysis title.
 #  string         mode             The parameter is the file mode ('w' or 'a').
 #  
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def write_to_folder(msg: str, title: str, mode: str = 'w'):

    if not os.path.isdir(logs_config_dict['analysis_folder']):

        try:

            os.mkdir(logs_config_dict['analysis_folder'])

        except FileExistsError: 

            print_and_log_text \
                (f"\n\nThe script failed to create folder {logs_config_dict['analysis_folder']}.\n\n")


    file_path = curr_analysis_file_path(title)

    with open(file_path, mode) as file: file.write(msg)


    if logs_config_dict['log_mode'] == True:

        logs_config_dict['log_txt_file'].write(curr_timept_with_msg(msg))    


# In[31]:


#*******************************************************************************************
 #
 #  Function Name:  save_matplotlib_image
 #
 #  Function Description:
 #      The function saves the image of a matplotlib plot to a file.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  string         caption         The parameter is the plot title.
 #  integer        dpi             The parameter is the dots per square inch for the image.
 #  float          pad_inch        The parameter is the buffer around the plot in inches.
 #  string         img_fmt         The parameter is the image format (png, html, etc.).
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def save_matplotlib_image \
        (caption:  str   = '',
         dpi:      int   = 300,
         pad_inch: float = 0.5,
         img_fmt:  str   = 'png'):

    if logs_config_dict['img_mode'] == True:

        plt.savefig \
            (curr_img_file_path(caption, img_fmt), 
             dpi = dpi, 
             bbox_inches = logs_config_dict['bbox_inches'], 
             pad_inches = pad_inch)


# In[32]:


#*******************************************************************************************
 #
 #  Function Name:  save_plotly_image
 #
 #  Function Description:
 #      The function saves a Plotly image to the images folder.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  object         plotly_fig       The parameter is the plotly figure object.
 #  string         title            The parameter is the figure title.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def save_plotly_image(plotly_fig, title: str):

    if logs_config_dict['img_mode'] == True: 

        plotly_fig.write_image(curr_img_file_path(title, 'png'))


# In[33]:


#*******************************************************************************************
 #
 #  Function Name:  save_folium_map_image
 #
 #  Function Description:
 #      The function saves a folium map to an html file.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  object         folium_map       The parameter is the input folium map object.
 #  string         title            The parameter is the plot title.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def save_folium_map_image(folium_map: object, title: str):

    if logs_config_dict['img_mode'] == True: 

        folium_map.save(curr_img_file_path(title, 'html'))


# In[34]:


#*******************************************************************************************
 #
 #  Function Name:  save_hvplot_map_image
 #
 #  Function Description:
 #      The function saves an hvplot to an html file.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  object         hvplot_ovl       The parameter is the input hvplot overlay object.
 #  string         title            The parameter is the plot title.
 #  integer        height           The parameter is the plot's height.
 #  integer        width            The parameter is the plot's width.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def save_hvplot_map_image \
        (hvplot_ovl: object,
         title:      str,
         height:     int,
         width:      int):

    if logs_config_dict['img_mode'] == True:

        tmp_ovl = copy.deepcopy(hvplot_ovl)

        tmp_ovl.opts(width = width, height = height)


        hvplot.save(tmp_ovl, curr_img_file_path(title, 'html'))


# In[35]:


#*******************************************************************************************
 #
 #  Function Name:  save_map_image
 #
 #  Function Description:
 #      The function saves a map image to an html file.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  object         input_obj        The parameter is the input map object.
 #  string         title            The parameter is the plot title.
 #  integer        height           The parameter is the plot's height.
 #  integer        width            The parameter is the plot's width.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def save_map_image \
        (input_obj:  object,
         title:      str = '',
         input_type: str = 'folium',
         height:     int = 550,
         width:      int = 1100):

    if logs_config_dict['img_mode'] == True:

        if  input_type == 'folium': save_folium_map_image(input_obj, title)

        elif input_type == 'hvplot': save_hvplot_map_image(input_obj, title, height, width)


# In[ ]:




