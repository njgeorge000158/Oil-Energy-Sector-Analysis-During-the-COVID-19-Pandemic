#!/usr/bin/env python
# coding: utf-8

# In[1]:


#*******************************************************************************************
 #
 #  File Name:  mapx.py
 #
 #  File Description:
 #      This Python script, pandasx.py, contains Python functions for displaying 
 #      dataframe information on a map.
 #
 #  get_folium_dict
 #  get_hvplot_dict
 #  get_folium_circle_limit
 #  get_folium_name
 #  get_folium_marker_size
 #  get_tooltip_display
 #  get_tooltip_cols
 #
 #  set_folium_dict
 #  set_hvplot_dict
 #  set_folium_circle_limit
 #  set_folium_name
 #  set_folium_marker_size
 #  set_tooltip_display
 #  set_tooltip_cols
 #
 #  clean_folium_df
 #
 #  random_css4_color_name
 #  rtn_title_html
 #  rtn_coords
 #  rtn_radius
 #  rtn_fill_color
 #  rtn_tooltip
 #
 #  add_circle_markers
 #
 #  disp_folium_circles_df
 #  disp_hvplot_circles_df
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  03/18/2024          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

import dtypesx
import logx

import branca
import copy
import folium
import hvplot.pandas
import random

import matplotlib.colors as mcolors
import numpy             as np
import pandas            as pd

from folium.plugins import MarkerCluster

pd.options.mode.chained_assignment = None


# In[2]:


CONSTANT_LOCAL_FILE_NAME = 'mapx.py'


# In[3]:


folium_dict \
    = {'params': {'name':    'city',
                  'lat':     'latitude',
                  'lng':     'longitude',
                  'size':    'humidity',
                  'country': 'country'},
       'map':    {'tiles':         'https://tile.openstreetmap.org/{z}/{x}/{y}.png',
                  'attr':          '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
                  'location':      np.array([20.0, 0.0], dtype = float),
                  'zoom_start':    2,
                  'detect_retina': True,
                  'prefer_canvas': True,
                  'ctrl_scale':    True,
                  'circle_lim':    1000},
       'circle': {'radius_scale': 0.12,
                  'edge_color':  'black',
                  'edge_weight':  1.0,
                  'fill':         True,
                  'fill_opacity': 0.7,
                  'fill_color':   None},
       'tooltip': {'display':    True,
                   'cols':       np.asarray(['city', 'country', 'latitude', 'longitude']),
                   'max_width':  100,
                   'max_height': 100},
       'title': {'align':       'left',
                 'font_size':   20.0,
                 'color':       'black',
                 'font_style':  'bold',
                 'font_family': 'Arial'}}

hvplot_dict \
    = {'lng_col':    'longitude',
       'lat_col':    'latitude',
       'color_col':  'city',
       'size_col':   'humidity',
       'x_lbl':      '',
       'y_lbl':      '',
       'geo':        True,
       'x_lmt':      (-180, 180),
       'y_lmt':      (-55, 75),
       'alpha':      0.7,
       'tiles':      'OSM',
       'hover_cols': []}


# In[4]:


#*******************************************************************************************
 #
 #  Function Name:  get_folium_dict
 #                  get_hvplot_dict
 #                  get_folium_circle_limit
 #                  get_folium_name
 #                  get_folium_marker_size
 #                  get_tooltip_display
 #                  get_tooltip_cols
 #
 #  Function Description:
 #      The function retrieves the dictionary.
 #
 #
 #  Return Type: varies
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  dictionary     upd_dict         The parameter is the updated dictionary
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_folium_dict() -> dict:         return copy.deepcopy(folium_dict)
def get_hvplot_dict() -> dict:         return copy.deepcopy(hvplot_dict)
def get_folium_circle_limit() -> int:  return folium_dict['map']['circle_lim']
def get_folium_name() -> str:          return folium_dict['params']['name']
def get_folium_marker_size() -> float: return folium_dict['params']['size']
def get_tooltip_display() -> bool:     return folium_dict['tooltip']['display']
def get_tooltip_cols():                return folium_dict['tooltip']['cols']


# In[5]:


#*******************************************************************************************
 #
 #  Function Name:  set_folium_dict
 #
 #  Function Description:
 #      The function sets the folium dictionary.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  dictionary     upd_dict         The parameter is the updated dictionary
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_folium_dict(upd_dict: dict):

    global folium_dict

    folium_dict = copy.deepcopy(upd_dict)


# In[6]:


#*******************************************************************************************
 #
 #  Function Name:  set_hvplot_dict
 #
 #  Function Description:
 #      The function sets the hvplot dictionary.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  dictionary     upd_dict         The parameter is the updated dictionary.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_hvplot_dict(upd_dict: dict):

    global hvplot_dict

    hvplot_dict = copy.deepcopy(upd_dict)


# In[7]:


#*******************************************************************************************
 #
 #  Function Name:  set_folium_circle_limit
 #
 #  Function Description:
 #      The function sets the folium dictionary's circle limit.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  integer        upd_int          The parameter is the updated circle limit.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_folium_circle_limit(upd_int: int):

    global folium_dict

    folium_dict['map']['circle_lim'] = upd_int


# In[8]:


#*******************************************************************************************
 #
 #  Function Name:  set_folium_name
 #
 #  Function Description:
 #      The function sets the folium dictionary's name column.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  string         upd              The parameter is the updated name column.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_folium_name(upd: str):

    global folium_dict

    folium_dict['params']['name'] = upd


# In[9]:


#*******************************************************************************************
 #
 #  Function Name:  set_folium_marker_size
 #
 #  Function Description:
 #      The function sets the folium dictionary's marker size column.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  float          upd_flt          The parameter is the updated marker size column.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_folium_marker_size(upd_flt: float):

    global folium_dict

    folium_dict['params']['size'] = upd_flt


# In[10]:


#*******************************************************************************************
 #
 #  Function Name:  set_tooltip_display
 #
 #  Function Description:
 #      The function sets the folium dictionary's circle tooltip display.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  bool           upd_bool         The parameter is the updated circle tooltip display.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_tooltip_display(upd_bool: bool):

    global folium_dict

    folium_dict['tooltip']['display'] = upd_bool


# In[11]:


#*******************************************************************************************
 #
 #  Function Name:  set_tooltip_cols
 #
 #  Function Description:
 #      The function sets the folium dictionary's dataframe columns array for a tooltip.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  object         upd_obj          The parameter is the updated circle tooltip columns.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_tooltip_cols(upd_obj: object):

    global folium_dict

    folium_dict['tooltip']['cols'] = dtypesx.cnv_data_to_array(upd_obj)


# In[12]:


#******************************************************************************************
 #
 #  Function Name:  clean_folium_df
 #
 #  Function Description:
 #      This function returns a cleaned dataframe for a folium map.
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
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def clean_folium_df(input_df: pd.DataFrame) -> pd.DataFrame:

    clean_df \
        = input_df.dropna \
            (subset = [folium_dict['params']['name'], 
                       folium_dict['params']['lat'], 
                       folium_dict['params']['lng'], 
                       folium_dict['params']['size']]) \
            .copy()

    clean_df[folium_dict['params']['lat']] \
        = pd.to_numeric(clean_df[folium_dict['params']['lat']])

    clean_df[folium_dict['params']['lng']] \
        = pd.to_numeric(clean_df[folium_dict['params']['lng']])

    clean_df[folium_dict['params']['size']] \
        = pd.to_numeric(clean_df[folium_dict['params']['size']])

    if len(clean_df) > folium_dict['map']['circle_lim']: 

        clean_df = clean_df[0:folium_dict['map']['circle_lim']]


    return clean_df


# In[13]:


#******************************************************************************************
 #
 #  Function Name:  random_css4_color_name
 #
 #  Function Description:
 #      This function returns a random css4 color.
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
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def random_css4_color_name() -> str:

    return random.choice(np.array(list(mcolors.CSS4_COLORS.keys()), dtype = str))


# In[14]:


#******************************************************************************************
 #
 #  Function Name:  rtn_title_html
 #
 #  Function Description:
 #      This function returns the formatted title for a folium map.
 #
 #
 #  Return Type: string
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  string         title            The parameter is the map title.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def rtn_title_html(title: str) -> str:

    return \
        f"""
            <h3 align='{folium_dict['title']['align']}' style='
                font-size:{folium_dict['title']['font_size']}px; 
                color:{folium_dict['title']['color']}; 
                font-style:{folium_dict['title']['font_style']}; 
                font-family:{folium_dict['title']['font_family']};'>
                <b>{title}</b>
            </h3>
         """


# In[15]:


#******************************************************************************************
 #
 #  Function Name:  rtn_coords
 #
 #  Function Description:
 #      This function returns the latitude and logitude array for a folium circle.
 #
 #
 #  Return Type: array
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  series         row              The parameter is the dataframe row.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def rtn_coords(row: object) -> np.ndarray:

    return \
        np.asarray \
            ([row[folium_dict['params']['lat']], 
              row[folium_dict['params']['lng']]], 
             dtype = float)


# In[16]:


#******************************************************************************************
 #
 #  Function Name:  rtn_radius
 #
 #  Function Description:
 #      This function returns the folium circle radius for a dataframe row.
 #
 #
 #  Return Type: float
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  series         row              The parameter is the dataframe row.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def rtn_radius(row: object) -> float: 

    return row[folium_dict['params']['size']] * folium_dict['circle']['radius_scale']


# In[17]:


#******************************************************************************************
 #
 #  Function Name:  rtn_fill_color
 #
 #  Function Description:
 #      This function returns the fill color for a foilium map circle.
 #
 #
 #  Return Type: string
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  int            idx              The parameter is the index for the color array.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def rtn_fill_color(idx: int) -> str:

    if folium_dict['circle']['fill_color'] is None: return random_css4_color_name()

    else: return folium_dict['circle']['fill_color'][idx]


# In[18]:


#******************************************************************************************
 #
 #  Function Name:  rtn_tooltip
 #
 #  Function Description:
 #      This function returns the folium circle tooltip for a dataframe row.
 #
 #
 #  Return Type: string
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  series         row              The parameter is the dataframe row.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def rtn_tooltip(row) -> str:

    cols_array = dtypesx.cnv_data_to_array(folium_dict['tooltip']['cols'])

    final_idx = len(cols_array) - 1

    tooltip = ''


    for idx, col in enumerate(cols_array):

        tooltip += f"{col.title()}: {row[col]}"

        if idx != final_idx: tooltip += '<br>'


    return tooltip


# In[19]:


#******************************************************************************************
 #
 #  Function Name:  add_circle_markers
 #
 #  Function Description:
 #      This function adds circle markers to a folium map.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  dataframe      clean_df         The parameter is the cleaned input dataframe.
 #  object         folium_map       The parameter is the folium map object.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def add_circle_markers \
        (clean_df:   pd.DataFrame, 
         folium_map: object):

    if folium_dict['tooltip']['display']:

        for idx, row in clean_df.iterrows():

            folium.CircleMarker(
                location = rtn_coords(row),
                radius = rtn_radius(row),
                color = folium_dict['circle']['edge_color'],
                weight = folium_dict['circle']['edge_weight'],
                fill = folium_dict['circle']['fill'],
                fill_opacity = folium_dict['circle']['fill_opacity'],
                fill_color = rtn_fill_color(idx),
                tooltip = rtn_tooltip(row)) \
                    .add_to(folium_map)

    else:

        for idx, row in clean_df.iterrows():

            popup \
                = folium.Popup \
                    (rtn_tooltip(row),
                     max_width = folium_dict['tooltip']['max_width'],
                     max_height = folium_dict['tooltip']['max_height'])

            folium.CircleMarker(
                location = rtn_coords(row),
                radius = rtn_radius(row),
                color = folium_dict['circle']['edge_color'],
                weight = folium_dict['circle']['edge_weight'],
                fill = folium_dict['circle']['fill'],
                fill_opacity = folium_dict['circle']['fill_opacity'],
                fill_color = rtn_fill_color(idx),
                popup = popup) \
                    .add_to(folium_map)


# In[20]:


#******************************************************************************************
 #
 #  Function Name:  disp_folium_circles_df
 #
 #  Function Description:
 #      This function receives a dataframe and displays a formatted map with proportional 
 #      circles for locations. This function uses the global dictionary folium_dict for 
 #      its remaining parameters.
 #
 #
 #  Return Type: folium overlay
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  dataframe      input_df         The parameter is the input dataframe.
 #  string         title            The parameter is the plot's title.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def disp_folium_circles_df \
        (input_df: pd.DataFrame, 
         title:    str) \
-> object:

    folium_map \
        = folium.Map \
            (location = folium_dict['map']['location'], 
             zoom_start = folium_dict['map']['zoom_start'], 
             detect_retina = folium_dict['map']['detect_retina'], 
             tiles = folium_dict['map']['tiles'],
             attr = folium_dict['map']['attr'],
             control_scale = folium_dict['map']['ctrl_scale'],
             prefer_canvas = folium_dict['map']['prefer_canvas'])


    title_html = rtn_title_html(title)

    folium_map.get_root().html.add_child(folium.Element(title_html))


    clean_df = clean_folium_df(input_df)

    add_circle_markers(clean_df, folium_map)


    logx.save_map_image(folium_map, title)

    return folium_map


# In[21]:


#******************************************************************************************
 #
 #  Function Name:  disp_hvplot_circles_df
 #
 #  Function Description:
 #      This function receives a dataframe and displays a formatted map with proportional 
 #      circles for locations. This function uses the global dictionary hvplot_dict for 
 #      its remaining parameters.
 #
 #
 #  Return Type: hvplot overlay
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  dataframe      input_df         The parameter is the input dataframe.
 #  string         title            The parameter is the plot's title.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def disp_hvplot_circles_df \
        (input_df: pd.DataFrame, 
         title:    str) \
-> object:

    hvplot_overlay \
        = input_df \
            .hvplot \
            .points \
                (hvplot_dict['lng_col'],
                 hvplot_dict['lat_col'],
                 xlabel = hvplot_dict['x_lbl'],
                 ylabel = hvplot_dict['y_lbl'],
                 geo = hvplot_dict['geo'],
                 color = hvplot_dict['color_col'],
                 size = hvplot_dict['size_col'],
                 xlim = hvplot_dict['x_lmt'],
                 ylim = hvplot_dict['y_lmt'],
                 alpha = hvplot_dict['alpha'],
                 tiles = hvplot_dict['tiles'],
                 title = title,
                 hover_cols = hvplot_dict['hover_cols'])


    logx.save_map_image(hvplot_overlay, title, 'hvplot')

    return hvplot_overlay


# In[ ]:




