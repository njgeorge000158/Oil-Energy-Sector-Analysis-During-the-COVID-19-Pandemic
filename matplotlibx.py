#!/usr/bin/env python
# coding: utf-8

# In[1]:


#*******************************************************************************************
 #
 #  File Name:  matplotlibx.py
 #
 #  File Description:
 #      The Python script, matplotlibx.py, contains generic Python functions
 #      for matplotlib charts and processing.  Here is the list:
 #
 #  calc_rows_and_cols
 #  proc_rvalues
 #  stacked_bar_chart_setup
 #  rtn_fmt_regr_tbl
 #
 #  get_chart_dict
 #  get_chart_def_dict
 #  get_title
 #  get_title_display
 #  get_title_fontsize
 #  get_title_pad
 #  get_xylabels
 #  get_xylabels_display
 #  get_xylabels_fontsize
 #  get_xylabels_pad
 #  get_xyticks_fontsize
 #  get_xyticks_rotation
 #  get_chart_colors
 #  get_legend_display
 #  get_legend_fontsize
 #  get_legend_bbox_to_anchor
 #
 #  get_multichart_fig_dims
 #  get_multichart_fig_spaces
 #  get_multichart_stacked
 #  get_multichart_suptitle_xycoords
 #  get_multichart_supxlabel_xycoords
 #  get_multichart_supylabel_xycoords
 #  get_multichart_suptitle_fontsize
 #  get_multichart_supxlabel_fontsize
 #  get_multichart_supylabel_fontsize
 #  get_multichart_xysuplabels
 #
 #  set_chart_dict
 #  set_chart_def_dict
 #  set_title
 #  set_title_display
 #  set_title_fontsize
 #  set_title_pad
 #  set_xylabels
 #  set_xylabels_display
 #  set_xylabels_fontsize
 #  set_xylabels_pad
 #  set_xyticks_fontsize
 #  set_xyticks_rotation
 #  set_chart_colors
 #  set_legend_display
 #  set_legend_fontsize
 #  set_legend_bbox_to_anchor
 #
 #  set_multichart_fig_dims
 #  set_multichart_fig_spaces
 #  set_multichart_stacked
 #  set_multichart_suptitle_xycoords
 #  set_multichart_supxlabel_xycoords
 #  set_multichart_supylabel_xycoords
 #  set_multichart_suptitle_fontsize
 #  set_multichart_supxlabel_fontsize
 #  set_multichart_supylabel_fontsize
 #  set_multichart_xysuplabels
 #
 #  get_bar_chart_dict
 #  get_boxplot_chart_dict
 #  get_histogram_chart_dict
 #  get_line_chart_dict
 #  get_pie_chart_dict
 #  get_plot_chart_dict
 #  get_scatterplot_chart_dict
 #
 #  get_regr_line_dict
 #  get_corr_cv_dict
 #  get_window_cv_dict
 #  get_roll_corr_dict
 #  get_roll_all_corr_dict
 #  get_lag_corr_dict
 #  get_lag_heat_dict
 #
 #  get_bar_multichart_dict
 #  get_boxplot_multichart_dict
 #  get_histogram_multichart_dict
 #  get_line_multichart_dict
 #  get_pie_multichart_dict
 #  get_plot_multichart_dict
 #  get_scatterplot_multichart_dict
 #
 #  set_bar_chart_dict
 #  set_boxplot_chart_dict
 #  set_histogram_chart_dict
 #  set_line_chart_dict
 #  set_pie_chart_dict
 #  set_plot_chart_dict
 #  set_scatterplot_chart_dict
 #
 #  set_regr_line_dict
 #  set_corr_cv_dict
 #  set_window_cv_dict
 #  set_roll_corr_dict
 #  set_roll_corr_all_dict
 #  set_lag_corr_dict
 #  set_lag_heat_dict
 #
 #  set_bar_multichart_dict
 #  set_boxplot_multichart_dict
 #  set_histogram_multichart_dict
 #  set_line_multichart_dict
 #  set_pie_multichart_dict
 #  set_plot_multichart_dict
 #  set_scatterplot_multichart_dict
 #
 #  get_bar_chart_def_dict
 #  get_boxplot_chart_def_dict
 #  get_histogram_chart_def_dict
 #  get_line_chart_def_dict
 #  get_pie_chart_def_dict
 #  get_plot_chart_def_dict
 #  get_scatterplot_chart_def_dict
 #
 #  get_regr_line_def_dict
 #  get_corr_cv_def_dict
 #  get_window_cv_def_dict
 #  get_roll_corr_def_dict
 #  get_roll_corr_all_def_dict
 #  get_lag_corr_def_dict
 #  get_lag_heat_def_dict
 #
 #  get_bar_multichart_def_dict
 #  get_boxplot_multichart_def_dict
 #  get_histogram_multichart_def_dict
 #  get_line_multichart_def_dict
 #  get_pie_multichart_def_dict
 #  get_plot_multichart_def_dict
 #  get_scatterplot_multichart_def_dict
 #
 #  set_bar_chart_def_dict
 #  set_boxplot_chart_def_dict
 #  set_histogram_chart_def_dict
 #  set_line_chart_def_dict
 #  set_pie_chart_def_dict
 #  set_plot_chart_def_dict
 #  set_scatterplot_chart_def_dict
 #
 #  set_regr_line_def_dict
 #  set_corr_cv_def_dict
 #  set_window_cv_def_dict
 #  set_roll_corr_def_dict
 #  set_roll_corr_all_def_dict
 #  set_lag_corr_def_dict
 #  set_lag_heat_def_dict
 #
 #  set_bar_multichart_def_dict
 #  set_boxplot_multichart_def_dict
 #  set_histogram_multichart_def_dict
 #  set_line_multichart_def_dict
 #  set_pie_multichart_def_dict
 #  set_plot_multichart_def_dict
 #  set_scatterplot_multichart_def_dict
 #
 #  get_bar_chart_title
 #  get_boxplot_chart_title
 #  get_histogram_chart_title
 #  get_line_chart_title
 #  get_pie_chart_title
 #  get_plot_chart_title
 #  get_scatterplot_chart_title
 #
 #  get_corr_cv_title
 #  get_window_cv_title
 #  get_roll_corr_title
 #  get_roll_corr_all_title
 #  get_lag_corr_title
 #  get_lag_heat_title
 #
 #  set_bar_chart_title
 #  set_boxplot_chart_title
 #  set_histogram_chart_title
 #  set_line_chart_title
 #  set_pie_chart_title
 #  set_plot_chart_title
 #  set_scatterplot_chart_title
 #
 #  set_corr_cv_title
 #  set_window_cv_title
 #  set_roll_corr_title
 #  set_roll_corr_all_title
 #  set_lag_corr_title
 #  set_lag_heat_title
 #
 #  get_bar_chart_title_display
 #  get_boxplot_chart_title_display
 #  get_histogram_chart_title_display
 #  get_line_chart_title_display
 #  get_pie_chart_title_display
 #  get_plot_chart_title_display
 #  get_scatterplot_chart_title_display
 #
 #  get_corr_cv_title_display
 #  get_window_cv_title_display
 #  get_roll_corr_title_display
 #  get_roll_corr_all_title_display
 #  get_lag_corr_title_display
 #  get_lag_heat_title_display
 #
 #  set_bar_chart_title_display
 #  set_boxplot_chart_title_display
 #  set_histogram_chart_title_display
 #  set_line_chart_title_display
 #  set_pie_chart_title_display
 #  set_plot_chart_title_display
 #  set_scatterplot_chart_title_display
 #
 #  set_corr_cv_title_display
 #  set_window_cv_title_display
 #  set_roll_corr_title_display
 #  set_roll_corr_all_title_display
 #  set_lag_corr_title_display
 #  set_lag_heat_title_display
 #
 #  get_bar_chart_title_fontsize
 #  get_boxplot_chart_title_fontsize
 #  get_histogram_chart_title_fontsize
 #  get_line_chart_title_fontsize
 #  get_pie_chart_title_fontsize
 #  get_plot_chart_title_fontsize
 #  get_scatterplot_chart_title_fontsize
 #
 #  get_corr_cv_title_fontsize
 #  get_window_cv_title_fontsize
 #  get_roll_corr_title_fontsize
 #  get_roll_corr_all_title_fontsize
 #  get_lag_corr_title_fontsize
 #  get_lag_heat_title_fontsize
 #
 #  set_bar_chart_title_fontsize
 #  set_boxplot_chart_title_fontsize
 #  set_histogram_chart_title_fontsize
 #  set_line_chart_title_fontsize
 #  set_pie_chart_title_fontsize
 #  set_plot_chart_title_fontsize
 #  set_scatterplot_chart_title_fontsize
 #
 #  set_corr_cv_title_fontsize
 #  set_window_cv_title_fontsize
 #  set_roll_corr_title_fontsize
 #  set_roll_corr_all_title_fontsize
 #  set_lag_corr_title_fontsize
 #  set_lag_heat_title_fontsize
 #
 #  get_bar_chart_title_pad
 #  get_boxplot_chart_title_pad
 #  get_histogram_chart_title_pad
 #  get_line_chart_title_pad
 #  get_pie_chart_title_pad
 #  get_plot_chart_title_pad
 #  get_scatterplot_chart_title_pad
 #
 #  get_corr_cv_title_pad
 #  get_window_cv_title_pad
 #  get_roll_corr_title_pad
 #  get_roll_corr_all_title_pad
 #  get_lag_corr_title_pad
 #  get_lag_heat_title_pad
 #
 #  set_bar_chart_title_pad
 #  set_boxplot_chart_title_pad
 #  set_histogram_chart_title_pad
 #  set_line_chart_title_pad
 #  set_pie_chart_title_pad
 #  set_plot_chart_title_pad
 #  set_scatterplot_chart_title_pad
 #
 #  set_corr_cv_title_pad
 #  set_window_cv_title_pad
 #  set_roll_corr_title_pad
 #  set_roll_corr_all_title_pad
 #  set_lag_corr_title_pad
 #  set_lag_heat_title_pad
 #
 #  get_bar_chart_xylabels
 #  get_boxplot_chart_xylabels
 #  get_histogram_multichart_xylabels
 #  get_line_chart_xylabels
 #  get_pie_chart_xylabels
 #  get_plot_chart_xylabels
 #  get_scatterplot_chart_xylabels
 #
 #  get_corr_cv_xylabels
 #  get_window_cv_xylabels
 #  get_roll_corr_xylabels
 #  get_roll_corr_all_xylabels
 #  get_lag_corr_xylabels
 #  get_lag_heat_xylabels
 #
 #  set_bar_chart_xylabels
 #  set_boxplot_chart_xylabels
 #  set_histogram_chart_xylabels
 #  set_line_chart_xylabels
 #  set_pie_chart_xylabels
 #  set_plot_chart_xylabels
 #  set_scatterplot_chart_xylabels
 #
 #  set_corr_cv_xylabels
 #  set_window_cv_xylabels
 #  set_roll_corr_xylabels
 #  set_roll_corr_all_xylabels
 #  set_lag_corr_xylabels
 #  set_lag_heat_xylabels
 #
 #  get_bar_chart_xylabels_display
 #  get_boxplot_chart_xylabels_display
 #  get_histogram_multichart_xylabels_display
 #  get_line_chart_xylabels_display
 #  get_pie_chart_xylabels_display
 #  get_plot_chart_xylabels_display
 #  get_scatterplot_chart_xylabels_display
 #
 #  get_corr_cv_xylabels_display
 #  get_window_cv_xylabels_display
 #  get_roll_corr_xylabels_display
 #  get_roll_corr_all_xylabels_display
 #  get_lag_corr_xylabels_display
 #  get_lag_heat_xylabels_display
 #
 #  set_bar_chart_xylabels_display
 #  set_boxplot_chart_xylabels_display
 #  set_histogram_chart_xylabels_display
 #  set_line_chart_xylabels_display
 #  set_pie_chart_xylabels_display
 #  set_plot_chart_xylabels_display
 #  set_scatterplot_chart_xylabels_display
 #
 #  set_corr_cv_xylabels_display
 #  set_window_cv_xylabels_display
 #  set_roll_corr_xylabels_display
 #  set_roll_corr_all_xylabels_display
 #  set_lag_corr_xylabels_display
 #  set_lag_heat_xylabels_display
 #
 #  get_bar_chart_xylabels_fontsize
 #  get_boxplot_chart_xylabels_fontsize
 #  get_histogram_multichart_xylabels_fontsize
 #  get_line_chart_xylabels_fontsize
 #  get_pie_chart_xylabels_fontsize
 #  get_plot_chart_xylabels_fontsize
 #  get_scatterplot_chart_xylabels_fontsize
 #
 #  get_corr_cv_xylabels_fontsize
 #  get_window_cv_xylabels_fontsize
 #  get_roll_corr_xylabels_fontsize
 #  get_roll_corr_all_xylabels_fontsize
 #  get_lag_corr_xylabels_fontsize
 #  get_lag_heat_xylabels_fontsize
 #
 #  set_bar_chart_xylabels_fontsize
 #  set_boxplot_chart_xylabels_fontsize
 #  set_histogram_chart_xylabels_fontsize
 #  set_line_chart_xylabels_fontsize
 #  set_pie_chart_xylabels_fontsize
 #  set_plot_chart_xylabels_fontsize
 #  set_scatterplot_chart_xylabels_fontsize
 #
 #  set_corr_cv_xylabels_fontsize
 #  set_window_cv_xylabels_fontsize
 #  set_roll_corr_xylabels_fontsize
 #  set_roll_corr_all_xylabels_fontsize
 #  set_lag_corr_xylabels_fontsize
 #  set_lag_heat_xylabels_fontsize
 #
 #  get_bar_chart_xylabels_pad
 #  get_boxplot_chart_xylabels_pad
 #  get_histogram_multichart_xylabels_pad
 #  get_line_chart_xylabels_pad
 #  get_pie_chart_xylabels_pad
 #  get_plot_chart_xylabels_pad
 #  get_scatterplot_chart_xylabels_pad
 #
 #  get_corr_cv_xylabels_pad
 #  get_window_cv_xylabels_pad
 #  get_roll_corr_xylabels_pad
 #  get_roll_corr_all_xylabels_pad
 #  get_lag_corr_xylabels_pad
 #  get_lag_heat_xylabels_pad
 #
 #  set_bar_chart_xylabels_pad
 #  set_boxplot_chart_xylabels_pad
 #  set_histogram_chart_xylabels_pad
 #  set_line_chart_xylabels_pad
 #  set_pie_chart_xylabels_pad
 #  set_plot_chart_xylabels_pad
 #  set_scatterplot_chart_xylabels_pad
 #
 #  set_corr_cv_xylabels_pad
 #  set_window_cv_xylabels_pad
 #  set_roll_corr_xylabels_pad
 #  set_roll_corr_all_xylabels_pad
 #  set_lag_corr_xylabels_pad
 #  set_lag_heat_xylabels_pad
 #
 #  get_bar_chart_xyticks_fontsize
 #  get_boxplot_chart_xyticks_fontsize
 #  get_histogram_multichart_xyticks_fontsize
 #  get_line_chart_xyticks_fontsize
 #  get_pie_chart_xyticks_fontsize
 #  get_plot_chart_xyticks_fontsize
 #  get_scatterplot_chart_xyticks_fontsize
 #
 #  get_corr_cv_xylabels_fontsize
 #  get_window_cv_xylabels_fontsize
 #  get_roll_corr_xylabels_fontsize
 #  get_roll_corr_all_xylabels_fontsize
 #  get_lag_corr_xylabels_fontsize
 #  get_lag_heat_xylabels_fontsize
 #
 #  set_bar_chart_xyticks_fontsize
 #  set_boxplot_chart_xyticks_fontsize
 #  set_histogram_multichart_xyticks_fontsize
 #  set_line_chart_xyticks_fontsize
 #  set_pie_chart_xyticks_fontsize
 #  set_plot_chart_xyticks_fontsize
 #  set_scatterplot_chart_xyticks_fontsize
 #
 #  set_corr_cv_xyticks_fontsize
 #  set_window_cv_xyticks_fontsize
 #  set_roll_corr_xyticks_fontsize
 #  set_roll_corr_all_xyticks_fontsize
 #  set_lag_corr_xyticks_fontsize
 #  set_lag_heat_xyticks_fontsize
 #
 #  get_bar_chart_xyticks_rotation
 #  get_boxplot_chart_xyticks_rotation
 #  get_histogram_multichart_xyticks_rotation
 #  get_line_chart_xyticks_rotation
 #  get_pie_chart_xyticks_rotation
 #  get_plot_chart_xyticks_rotation
 #  get_scatterplot_chart_xyticks_rotation
 #
 #  get_corr_cv_xyticks_rotation
 #  get_window_cv_xyticks_rotation
 #  get_roll_corr_xyticks_rotation
 #  get_roll_corr_all_xyticks_rotation
 #  get_lag_corr_xyticks_rotation
 #  get_lag_heat_xyticks_rotation
 #
 #  set_bar_chart_xyticks_rotation
 #  set_boxplot_chart_xyticks_rotation
 #  set_histogram_multichart_xyticks_rotation
 #  set_line_chart_xyticks_rotation
 #  set_pie_chart_xyticks_rotation
 #  set_plot_chart_xyticks_rotation
 #  set_scatterplot_chart_xyticks_rotation
 #
 #  set_corr_cv_xyticks_rotation
 #  set_window_cv_xyticks_rotation
 #  set_roll_corr_xyticks_rotation
 #  set_roll_corr_all_xyticks_rotation
 #  set_lag_corr_xyticks_rotation
 #  set_lag_heat_xyticks_rotation
 #
 #  get_bar_chart_legend_display
 #  get_histogram_chart_legend_display
 #  get_line_chart_legend_display
 #  get_pie_chart_legend_display
 #  get_plot_chart_legend_display
 #
 #  get_corr_cv_legend_display
 #  get_window_cv_legend_display
 #  get_roll_corr_legend_display
 #  get_roll_corr_all_legend_display
 #  get_lag_corr_legend_display
 #  get_lag_heat_legend_display
 #
 #  set_bar_chart_legend_display
 #  set_histogram_chart_legend_display
 #  set_line_chart_legend_display
 #  set_pie_chart_legend_display
 #  set_plot_chart_legend_display
 #
 #  set_corr_cv_legend_display
 #  set_window_cv_legend_display
 #  set_roll_corr_legend_display
 #  set_roll_corr_all_legend_display
 #  set_lag_corr_legend_display
 #  set_lag_heat_legend_display
 #
 #  get_bar_chart_legend_fontsize
 #  get_histogram_chart_legend_fontsize
 #  get_line_chart_legend_fontsize
 #  get_pie_chart_legend_fontsize
 #  get_plot_chart_legend_fontsize
 #
 #  get_corr_cv_legend_fontsize
 #  get_window_cv_legend_fontsize
 #  get_roll_corr_legend_fontsize
 #  get_roll_corr_all_legend_fontsize
 #  get_lag_corr_legend_fontsize
 #  get_lag_heat_legend_fontsize
 #
 #  set_bar_chart_legend_fontsize
 #  set_histogram_chart_legend_fontsize
 #  set_line_chart_legend_fontsize
 #  set_pie_chart_legend_fontsize
 #  set_plot_chart_legend_fontsize
 #
 #  set_corr_cv_legend_fontsize
 #  set_window_cv_legend_fontsize
 #  set_roll_corr_legend_fontsize
 #  set_roll_corr_all_legend_fontsize
 #  set_lag_corr_legend_fontsize
 #  set_lag_heat_legend_fontsize
 #
 #  get_bar_chart_legend_bbox_to_anchor
 #  get_histogram_chart_legend_bbox_to_anchor
 #  get_line_chart_legend_bbox_to_anchor
 #  get_pie_chart_legend_bbox_to_anchor
 #  get_plot_chart_legend_bbox_to_anchor
 #
 #  get_corr_cv_legend_bbox_to_anchor
 #  get_window_cv_legend_bbox_to_anchor
 #  get_roll_corr_legend_bbox_to_anchor
 #  get_roll_corr_all_legend_bbox_to_anchor
 #  get_lag_corr_legend_bbox_to_anchor
 #  get_lag_heat_legend_bbox_to_anchor
 #
 #  set_bar_chart_legend_bbox_to_anchor
 #  set_histogram_chart_legend_bbox_to_anchor
 #  set_line_chart_legend_bbox_to_anchor
 #  set_pie_chart_legend_bbox_to_anchor
 #  set_plot_chart_legend_bbox_to_anchor
 #
 #  set_corr_cv_legend_bbox_to_anchor
 #  set_window_cv_legend_bbox_to_anchor
 #  set_roll_corr_legend_bbox_to_anchor
 #  set_roll_corr_all_legend_bbox_to_anchor
 #  set_lag_corr_legend_bbox_to_anchor
 #  set_lag_heat_legend_bbox_to_anchor
 #
 #  get_regr_degree
 #  get_regr_eqn_coords
 #  get_rvalues_display
 #
 #  set_regr_degree
 #  set_regr_eqn_coords
 #  set_rvalues_display
 #
 #  get_bar_chart_colors
 #  get_histogram_chart_colors
 #  get_line_chart_colors
 #  get_pie_chart_colors
 #  get_plot_chart_colors
 #
 #  get_corr_cv_chart_colors
 #  get_window_cv_chart_colors
 #  get_roll_corr_chart_colors
 #  get_roll_corr_all_chart_colors
 #  get_lag_corr_chart_colors
 #  get_lag_heat_chart_colors
 #
 #  set_bar_chart_colors
 #  set_histogram_chart_colors
 #  set_line_chart_colors
 #  set_pie_chart_colors
 #  set_plot_chart_colors
 #
 #  set_corr_cv_chart_colors
 #  set_window_cv_chart_colors
 #  set_roll_corr_chart_colors
 #  set_roll_corr_all_chart_colors
 #  set_lag_corr_chart_colors
 #  set_lag_heat_chart_colors
 #
 #  get_boxplot_chart_xycols
 #  set_boxplot_chart_xycols
 #
 #  get_line_chart_marker_size
 #  get_line_chart_linewidth
 #  set_line_chart_marker_size
 #  set_line_chart_linewidth
 #
 #  get_pie_chart_explode
 #  get_pie_textprops_fontsize
 #  set_pie_chart_explode
 #  set_pie_textprops_fontsize
 #
 #  get_roll_corr_w_mp
 #  set_roll_corr_w_mp
 #
 #  get_lag_corr_max_lag
 #  get_lag_corr_annot_xyoffsets
 #  get_lag_corr_method
 #  set_lag_corr_max_lag
 #  set_lag_corr_annot_xyoffsets
 #  set_lag_corr_method
 #
 #  get_lag_scores_marker_size
 #  set_lag_scores_marker_size
 #
 #  get_lag_heat_max_lag
 #  get_lag_heat_corr_method
 #  set_lag_heat_max_lag
 #  set_lag_heat_corr_method
 #
 #  get_bar_multichart_fig_dims
 #  get_boxplot_multichart_fig_dims
 #  get_histogram_multichart_fig_dims
 #  get_line_multichart_fig_dims
 #  get_pie_multichart_fig_dims
 #  get_plot_multichart_fig_dims
 #  get_scatterplot_multichart_fig_dims
 #
 #  set_bar_multichart_fig_dims
 #  set_boxplot_multichart_fig_dims
 #  set_histogram_multichart_fig_dims
 #  set_line_multichart_fig_dims
 #  set_pie_multichart_fig_dims
 #  set_plot_multichart_fig_dims
 #  set_scatterplot_multichart_fig_dims
 #
 #  get_bar_multichart_fig_spaces
 #  get_boxplot_multichart_fig_spaces
 #  get_histogram_multichart_fig_spaces
 #  get_line_multichart_fig_spaces
 #  get_pie_multichart_fig_spaces
 #  get_plot_multichart_fig_spaces
 #  get_scatterplot_multichart_fig_spaces
 #
 #  set_bar_multichart_fig_spaces
 #  set_boxplot_multichart_fig_spaces
 #  set_histogram_multichart_fig_spaces
 #  set_line_multichart_fig_spaces
 #  set_pie_multichart_fig_spaces
 #  set_plot_multichart_fig_spaces
 #  set_scatterplot_multichart_fig_spaces
 #
 #  get_bar_multichart_stacked
 #  get_boxplot_multichart_stacked
 #  get_histogram_multichart_stacked
 #  get_line_multichart_stacked
 #  get_pie_multichart_stacked
 #  get_plot_multichart_stacked
 #  get_scatterplot_multichart_stacked
 #
 #  set_bar_multichart_stacked
 #  set_boxplot_multichart_stacked
 #  set_histogram_multichart_stacked
 #  set_line_multichart_stacked
 #  set_pie_multichart_stacked
 #  set_plot_multichart_stacked
 #  set_scatterplot_multichart_stacked
 #
 #  get_bar_multichart_suptitle_xycoords
 #  get_boxplot_multichart_suptitle_xycoords
 #  get_histogram_multichart_suptitle_xycoords
 #  get_line_multichart_suptitle_xycoords
 #  get_pie_multichart_suptitle_xycoords
 #  get_plot_multichart_suptitle_xycoords
 #  get_scatterplot_multichart_suptitle_xycoords
 #
 #  set_bar_multichart_suptitle_xycoords
 #  set_boxplot_multichart_suptitle_xycoords
 #  set_histogram_multichart_suptitle_xycoords
 #  set_line_multichart_suptitle_xycoords
 #  set_pie_multichart_suptitle_xycoords
 #  set_plot_multichart_suptitle_xycoords
 #  set_scatterplot_multichart_suptitle_xycoords
 #
 #  get_bar_multichart_supxlabel_xycoords
 #  get_boxplot_multichart_supxlabel_xycoords
 #  get_histogram_multichart_supxlabel_xycoords
 #  get_line_multichart_supxlabel_xycoords
 #  get_pie_multichart_supxlabel_xycoords
 #  get_plot_multichart_supxlabel_xycoords
 #  get_scatterplot_multichart_supxlabel_xycoords
 #
 #  set_bar_multichart_supxlabel_xycoords
 #  set_boxplot_multichart_supxlabel_xycoords
 #  set_histogram_multichart_supxlabel_xycoords
 #  set_line_multichart_supxlabel_xycoords
 #  set_pie_multichart_supxlabel_xycoords
 #  set_plot_multichart_supxlabel_xycoords
 #  set_scatterplot_multichart_supxlabel_xycoords
 #
 #  get_bar_multichart_supylabel_xycoords
 #  get_boxplot_multichart_supylabel_xycoords
 #  get_histogram_multichart_supylabel_xycoords
 #  get_line_multichart_supylabel_xycoords
 #  get_pie_multichart_supylabel_xycoords
 #  get_plot_multichart_supylabel_xycoords
 #  get_scatterplot_multichart_supylabel_xycoords
 #
 #  set_bar_multichart_supylabel_xycoords
 #  set_boxplot_multichart_supylabel_xycoords
 #  set_histogram_multichart_supylabel_xycoords
 #  set_line_multichart_supylabel_xycoords
 #  set_pie_multichart_supylabel_xycoords
 #  set_plot_multichart_supylabel_xycoords
 #  set_scatterplot_multichart_supylabel_xycoords
 #
 #  get_bar_multichart_suptitle_fontsize
 #  get_boxplot_multichart_suptitle_fontsize
 #  get_histogram_multichart_suptitle_fontsize
 #  get_line_multichart_suptitle_fontsize
 #  get_pie_multichart_suptitle_fontsize
 #  get_plot_multichart_suptitle_fontsize
 #  get_scatterplot_multichart_suptitle_fontsize
 #
 #  set_bar_multichart_suptitle_fontsize
 #  set_boxplot_multichart_suptitle_fontsize
 #  set_histogram_multichart_suptitle_fontsize
 #  set_line_multichart_suptitle_fontsize
 #  set_pie_multichart_suptitle_fontsize
 #  set_plot_multichart_suptitle_fontsize
 #  set_scatterplot_multichart_suptitle_fontsize
 #
 #  get_bar_multichart_supxlabel_fontsize
 #  get_boxplot_multichart_supxlabel_fontsize
 #  get_histogram_multichart_supxlabel_fontsize
 #  get_line_multichart_supxlabel_fontsize
 #  get_pie_multichart_supxlabel_fontsize
 #  get_plot_multichart_supxlabel_fontsize
 #  get_scatterplot_multichart_supxlabel_fontsize
 #
 #  set_bar_multichart_supxlabel_fontsize
 #  set_boxplot_multichart_supxlabel_fontsize
 #  set_histogram_multichart_supxlabel_fontsize
 #  set_line_multichart_supxlabel_fontsize
 #  set_pie_multichart_supxlabel_fontsize
 #  set_plot_multichart_supxlabel_fontsize
 #  set_scatterplot_multichart_supxlabel_fontsize
 #
 #  get_bar_multichart_supylabel_fontsize
 #  get_boxplot_multichart_supylabel_fontsize
 #  get_histogram_multichart_supylabel_fontsize
 #  get_line_multichart_supylabel_fontsize
 #  get_pie_multichart_supylabel_fontsize
 #  get_plot_multichart_supylabel_fontsize
 #  get_scatterplot_multichart_supylabel_fontsize
 #
 #  set_bar_multichart_supylabel_fontsize
 #  set_boxplot_multichart_supylabel_fontsize
 #  set_histogram_multichart_supylabel_fontsize
 #  set_line_multichart_supylabel_fontsize
 #  set_pie_multichart_supylabel_fontsize
 #  set_plot_multichart_supylabel_fontsize
 #  set_scatterplot_multichart_supylabel_fontsize
 #
 #  get_bar_multichart_xysuplabels
 #  get_boxplot_multichart_xysuplabels
 #  get_histogram_multichart_xysuplabels
 #  get_line_multichart_xysuplabels
 #  get_pie_multichart_xysuplabels
 #  get_plot_multichart_xysuplabels
 #  get_scatterplot_multichart_xysuplabels
 #
 #  set_bar_multichart_xysuplabels
 #  set_boxplot_multichart_xysuplabels
 #  set_histogram_multichart_xysuplabels
 #  set_line_multichart_xysuplabels
 #  set_pie_multichart_xysuplabels
 #  set_plot_multichart_xysuplabels
 #  set_scatterplot_multichart_xysuplabels
 #
 #  setup_stacked_line_charts
 #
 #  proc_boxplot_chart_input
 #  proc_bar_chart_input
 #  proc_line_chart_input
 #  proc_pie_chart_input
 #  proc_plot_chart_input
 #  proc_scatterplot_chart_input
 #  proc_pie_multichart_input
 #  proc_scatterplot_multichart_input
 #  proc_multichart_input
 #  proc_chart_input
 #
 #  linear_regr_line
 #  regr_line
 #
 #  plot_subplots
 #  plot_subplot
 #
 #  plot_figsize
 #  plot_title_axes_stacked
 #  plot_title_axes
 #  plot_limits_stacked
 #  plot_limits
 #  plot_ticks_stacked
 #  plot_ticks
 #  plot_legend_stacked
 #  plot_legend
 #  plot_regr_line
 #  plot_peaks
 #  plot_suptitle_axes
 #  plot_tight_layout
 #  plot_subplots_adjust
 #
 #  plot_bar_chart_series
 #  plot_bar_chart_df
 #  plot_bar_chart
 #  plot_boxplot_chart
 #  plot_histogram_chart
 #  plot_line_chart
 #  plot_pie_chart
 #  plot_plot_chart
 #  plot_scatterplot_chart
 #
 #  plot_line_multichart_stacked
 #  plot_line_multichart
 #  plot_pie_multichart
 #  plot_scatterplot_multichart
 #
 #  plot_rolling_corr_lines
 #  plot_all_rolling_corrs_lines
 #  plot_corr_cv_errors
 #  plot_corr_scores
 #  plot_window_cv_errors
 #  plot_lag_corr_line_chart
 #  plot_lag_corr_bar_chart
 #  plot_lag_heatmap
 #
 #  boxplot_chart
 #  bar_chart
 #  histogram_chart
 #  line_chart
 #  pie_chart
 #  plot_chart
 #  scatterplot_chart
 #
 #  line_multichart
 #  pie_multichart
 #  scatterplot_multichart
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  08/18/2023          Initial Development                         Nicholas J. George
 #  02/24/2026          Upgraded Module                             Nicholas J. George
 #
 #******************************************************************************************/

import logx
import dtypesx
import mathx
import pandasx

import copy
import math
import operator

import matplotlib.pyplot as plt
import numpy             as np
import pandas            as pd

from enum  import Enum, auto
from scipy import stats

pd.options.mode.chained_assignment = None


# In[2]:


CONSTANT_LOCAL_FILE_NAME = 'matplotlibx.py'


# In[3]:


class chart_enum(Enum):

    BAR = auto()

    BOXPLOT = auto()

    HISTOGRAM = auto()

    LINE = auto()

    PIE = auto()

    PLOT = auto()

    SCATTER = auto()

    REGR_LINE = auto()

    CORR_CV = auto()

    CORR_SCORES = auto()

    WINDOW_CV = auto()

    ROLL_CORR = auto()

    ROLL_CORR_ALL = auto()

    LAG_HEAT = auto()

    LAG_CORR = auto()

    MULTIBAR = auto()

    MULTIBOXPLOT = auto()

    MULTIHISTOGRAM = auto()

    MULTILINE = auto()

    MULTIPIE = auto()

    MULTIPLOT = auto()

    MULTISCATTER = auto()


stacked_line_chart_colors \
    = ['steelblue', 'tomato', 'mediumseagreen', 'darkorange', 'mediumpurple', 
       'darkturquoise', 'goldenrod', 'crimson', 'slateblue', 'mediumspringgreen'] * 5 

pie_chart_colors \
    = ['steelblue', 'firebrick', 'mediumseagreen', 'goldenrod', 'mediumpurple', 
       'coral', 'cadetblue', 'darkorange', 'mediumvioletred', 'magenta', 'darkkhaki'] * 5


# In[4]:


bar_chart_dict \
    = {'params': {'horizontal': False,
                  'stacked': False,
                  'align': 'center',
                  'color': None,
                  'edgecolor': 'black',
                  'linewidth': 1.5,
                  'tick_label': None,
                  'log': False,
                  'alpha': 1.0},
       'vertical': {'width': 0.5,
                    'bottom': 0},
       'horizontal': {'height': 0.5,
                      'left': 0},
       'title': {'text': [None],
                 'display': True,
                 'fontsize': 20.0,
                 'fontstyle': 'normal',
                 'fontweight': 'bold',
                 'loc': 'center',
                 'pad': 20.0},
       'xlabel': {'text': [None],
                  'display': True,
                  'fontsize': 16.0,
                  'fontstyle': 'normal',
                  'fontweight': 'normal',
                  'labelpad': 4.0,
                  'loc': 'center',
                  'pad': 10.0},
       'ylabel': {'text': [None],
                  'display': True,
                  'fontsize': 16.0,
                  'fontstyle': 'normal',
                  'fontweight': 'normal',
                  'labelpad': 4.0,
                  'loc': 'center',
                  'pad': 10.0},
       'xlim': {'display': False,
                'emit': True,
                'auto': False,
                'mode': 'set',
                'set': {'min': 0,
                        'max': 0},
                'adjust': {'left': 0,
                           'right': 0}},
       'ylim': {'display': False,
                'emit': True,
                'auto': False,
                'mode': 'set',
                'set': {'min': 0,
                        'max': 0},
                'adjust': {'left': 0,
                           'right': 0}},
       'xticks': {'display': True,
                  'fontsize': 14.0,
                  'rotation': 90.0},
       'yticks': {'display': True,
                  'fontsize': 14.0,
                  'rotation': 0.0},
       'grid': {'display': True,
                'visible': None,
                'which': 'major',
                'axis': 'y'},
       'legend': {'display': False,
                  'loc': 'center right',
                  'fontsize': 14.0,
                  'bbox_to_anchor': (1.5, 0.5)},
       'figure': {'width': 9.708,
                  'length': 6.0}}


# In[5]:


boxplot_chart_dict \
    = {'params': {'x_col': None,
                  'y_col': None,
                  'notch': False, 
                  'vert': True, 
                  'orientation': 'vertical', 
                  'whis': 1.5, 
                  'widths': 0.45, 
                  'patch_artist': False, 
                  'autorange': False, 
                  'meanline': True,
                  'showmeans': True},
       'title': {'text': [None],
                 'display': True,
                 'fontsize': 20.0,
                 'fontstyle': 'normal',
                 'fontweight': 'bold',
                 'loc': 'center',
                 'pad': 20.0},
       'xlabel': {'text': [None],
                  'display': True,
                  'fontsize': 16.0,
                  'fontstyle': 'normal',
                  'fontweight': 'normal',
                  'labelpad': 4.0,
                  'loc': 'center',
                  'pad': 10.0},
       'ylabel': {'text': [None],
                  'display': True,
                  'fontsize': 16.0,
                  'fontstyle': 'normal',
                  'fontweight': 'normal',
                  'labelpad': 4.0,
                  'loc': 'center',
                  'pad': 10.0},
       'xlim': {'display': False,
                'emit': True,
                'auto': False,
                'mode': 'set',
                'set': {'min': 0,
                        'max': 0},
                'adjust': {'left': 0,
                           'right': 0}},
       'ylim': {'display': False,
                'emit': True,
                'auto': False,
                'mode': 'set',
                'set': {'min': 0,
                        'max': 0},
                'adjust': {'left': 0,
                           'right': 0}},
       'xticks': {'display': True,
                  'fontsize': 14.0,
                  'rotation': 90.0},
       'yticks': {'display': False,
                  'fontsize': 14.0,
                  'rotation': 0.0},
       'grid': {'display': True,
                'visible': None,
                'which': 'major',
                'axis': 'y'},
       'figure': {'width': 9.708,
                  'length': 6.0}}


# In[6]:


histogram_chart_dict \
    = {'params': {'bins': 10,
                  'range': None,
                  'density': False,
                  'weights': None,
                  'cumulative': False,
                  'bottom': 0,
                  'histtype': 'bar',
                  'align': 'mid',
                  'orientation': 'vertical',
                  'rwidth': None,
                  'log': False,
                  'color': None,
                  'label': None,
                  'stacked': False,
                  'edgecolor': 'black',
                  'color': 'white',
                  'linewidth': 1.5,
                  'alpha': 1.0},
       'title': {'text': [None],
                 'display': True,
                 'fontsize': 20.0,
                 'fontstyle': 'normal',
                 'fontweight': 'bold',
                 'loc': 'center',
                 'pad': 20.0},
       'xlabel': {'text': [None],
                  'display': True,
                  'fontsize': 16.0,
                  'fontstyle': 'normal',
                  'fontweight': 'normal',
                  'labelpad': 4.0,
                  'loc': 'center',
                  'pad': 10.0},
       'ylabel': {'text': [None],
                  'display': True,
                  'fontsize': 16.0,
                  'fontstyle': 'normal',
                  'fontweight': 'normal',
                  'labelpad': 4.0,
                  'loc': 'center',
                  'pad': 10.0},
       'xlim': {'display': False,
                'emit': True,
                'auto': False,
                'mode': 'set',
                'set': {'min': 0,
                        'max': 0},
                'adjust': {'left': 0,
                           'right': 0}},
       'ylim': {'display': False,
                'emit': True,
                'auto': False,
                'mode': 'set',
                'set': {'min': 0,
                        'max': 0},
                'adjust': {'left': 0,
                           'right': 0}},
       'xticks': {'display': True,
                  'fontsize': 14.0,
                  'rotation': 90.0},
       'yticks': {'display': True,
                  'fontsize': 14.0,
                  'rotation': 0.0},
       'grid': {'display': False,
                'visible': None,
                'which': 'major',
                'axis': 'both'},
       'legend': {'display': False,
                  'loc': 'center right',
                  'fontsize': 14.0,
                  'bbox_to_anchor': (1.5, 0.5)},
       'figure': {'width': 9.708,
                  'length': 6.0}}


# In[7]:


line_chart_dict \
    = {'line': {'color': 'darkslategray',
                'linestyle': 'solid',
                'fillstyle': 'full',
                'linewidth': 3.0,
                'alpha': 1.0},
       'marker': {'shape': 'o',
                  'color': 'red',
                  'edgecolor': 'black',
                  'size': 10.0,
                  'edgewidth': 1.0},
       'params': {'logx': False,
                  'logy': False,
                  'loglog': False,
                  'stacked': False,
                  'use_index': True},
       'title': {'text': [None],
                 'display': True,
                 'fontsize': 20.0,
                 'fontstyle': 'normal',
                 'fontweight': 'bold',
                 'loc': 'center',
                 'pad': 20.0},
       'xlabel': {'text': [None],
                  'display': True,
                  'fontsize': 16.0,
                  'fontstyle': 'normal',
                  'fontweight': 'normal',
                  'labelpad': 4.0,
                  'loc': 'center',
                  'pad': 10.0},
       'ylabel': {'text': [None],
                  'display': True,
                  'fontsize': 16.0,
                  'fontstyle': 'normal',
                  'fontweight': 'normal',
                  'labelpad': 4.0,
                  'loc': 'center',
                  'pad': 10.0},
       'xlim': {'display': False,
                'emit': True,
                'auto': False,
                'mode': 'set',
                'set': {'min': 0,
                        'max': 0},
                'adjust': {'left': 0,
                           'right': 0}},
       'ylim': {'display': False,
                'emit': True,
                'auto': False,
                'mode': 'set',
                'set': {'min': 0,
                        'max': 0},
                'adjust': {'left': 0,
                           'right': 0}},
       'xticks': {'display': True,
                  'fontsize': 14.0,
                  'rotation': 0.0},
       'yticks': {'display': True,
                  'fontsize': 14.0,
                  'rotation': 0.0},
       'grid': {'display': True,
                'visible': None,
                'which': 'major',
                'axis': 'both'},
       'legend': {'display': False,
                  'loc': 'center right',
                  'fontsize': 14.0,
                  'bbox_to_anchor': (1.5, 0.5)},
       'figure': {'width': 9.708,
                  'length': 6.0}}


# In[8]:


pie_chart_dict \
    = {'params': {'explode': None,
                  'colors': None,
                  'hatch': None,
                  'autopct': '%1.1f%%',
                  'pctdistance': 0.6,
                  'labeldistance': 1.1,
                  'shadow': True,
                  'startangle': 45.0,
                  'radius': 1.0,
                  'counterclock': True,
                  'wedgeprops': None,
                  'textprops': {'fontsize': 14.0,
                                'fontstyle': 'normal'},
                  'center': (0, 0),
                  'frame': False,
                  'rotatelabels': False,
                  'normalize': True},
       'title': {'text': [None],
                 'display': True,
                 'fontsize': 20.0,
                 'fontstyle': 'normal',
                 'fontweight': 'bold',
                 'loc': 'center',
                 'pad': 20.0},
       'xlabel': {'text': [None],
                  'display': True,
                  'fontsize': 16.0,
                  'fontstyle': 'normal',
                  'fontweight': 'normal',
                  'labelpad': 4.0,
                  'loc': 'center',
                  'pad': 10.0},
       'ylabel': {'text': [None],
                  'display': True,
                  'fontsize': 16.0,
                  'fontstyle': 'normal',
                  'fontweight': 'normal',
                  'labelpad': 4.0,
                  'loc': 'center',
                  'pad': 10.0},
       'legend': {'display': False,
                  'loc': 'center right',
                  'fontsize': 14.0,
                  'bbox_to_anchor': (1.5, 0.5)},
       'figure': {'width': 9.708,
                  'length': 6.0}}


# In[9]:


plot_chart_dict \
    = {'params': {'scalex': True, 
                  'scaley': True,
                  'color': None,
                  'alpha': 1.0},
       'peaks': {'display': False,
                 'array': [],
                 'markersize': 15.0,
                 'fontsize': 12.0,
                 'y_offset': 5.0,
                 'color': np.array(['red', 'blue'])},
       'title': {'text': [None],
                 'display': True,
                 'fontsize': 20.0,
                 'fontstyle': 'normal',
                 'fontweight': 'bold',
                 'loc': 'center',
                 'pad': 20.0},
       'xlabel': {'text': [None],
                  'display': True,
                  'fontsize': 16.0,
                  'fontstyle': 'normal',
                  'fontweight': 'normal',
                  'labelpad': 4.0,
                  'loc': 'center',
                  'pad': 10.0},
       'ylabel': {'text': [None],
                  'display': True,
                  'fontsize': 16.0,
                  'fontstyle': 'normal',
                  'fontweight': 'normal',
                  'labelpad': 4.0,
                  'loc': 'center',
                  'pad': 10.0},
       'xlim': {'display': False,
                'emit': True,
                'auto': False,
                'mode': 'set',
                'set': {'min': 0,
                        'max': 0},
                'adjust': {'left': 0,
                           'right': 0}},
       'ylim': {'display': False,
                'emit': True,
                'auto': False,
                'mode': 'set',
                'set': {'min': 0,
                        'max': 0},
                'adjust': {'left': 0,
                           'right': 0}},
       'xticks': {'display': True,
                  'fontsize': 14.0,
                  'rotation': 90.0},
       'yticks': {'display': True,
                  'fontsize': 14.0,
                  'rotation': 0.0},
       'grid': {'display': False,
                'visible': None,
                'which': 'major',
                'axis': 'both'},
       'legend': {'display': False,
                  'loc': 'center right',
                  'fontsize': 14.0,
                  'bbox_to_anchor': (1.5, 0.5)},
       'figure': {'width': 9.708,
                  'length': 6.0}}


# In[10]:


scatterplot_chart_dict \
    = {'marker': {'shape': 'o',
                  'size': 80.0,
                  'color': 'lime',
                  'linewidth': 1.5,
                  'edgecolors': 'black',
                  'alpha': 0.8},
       'title': {'text': [None],
                 'display': True,
                 'fontsize': 20.0,
                 'fontstyle': 'normal',
                 'fontweight': 'bold',
                 'loc': 'center',
                 'pad': 20.0},
       'xlabel': {'text': [None],
                  'display': True,
                  'fontsize': 16.0,
                  'fontstyle': 'normal',
                  'fontweight': 'normal',
                  'labelpad': 4.0,
                  'loc': 'center',
                  'pad': 10.0},
       'ylabel': {'text': [None],
                  'display': True,
                  'fontsize': 16.0,
                  'fontstyle': 'normal',
                  'fontweight': 'normal',
                  'labelpad': 4.0,
                  'loc': 'center',
                  'pad': 10.0},
       'xlim': {'display': False,
                'emit': True,
                'auto': False,
                'mode': 'set',
                'set': {'min': 0,
                        'max': 0},
                'adjust': {'left': 0,
                           'right': 0}},
       'ylim': {'display': False,
                'emit': True,
                'auto': False,
                'mode': 'set',
                'set': {'min': 0,
                        'max': 0},
                'adjust': {'left': 0,
                           'right': 0}},
       'xticks': {'display': True,
                  'fontsize': 14.0,
                  'rotation': 90.0},
       'yticks': {'display': True,
                  'fontsize': 14.0,
                  'rotation': 0.0},
       'grid': {'display': True,
                'visible': None,
                'which': 'major',
                'axis': 'both'},
       'figure': {'width': 9.708,
                  'length': 6.0}}


# In[11]:


regr_line_dict \
    = {'degree': [0],
       'eqn_x_coord': 0.0,
       'eqn_y_coord': 0.0,
       'linecolor': 'red',
       'linewidth': 3.0,
       'alpha': 1.0,
       'coef_prec': 2,
       'fontsize': 16.0,
       'fontweight': 'bold',
       'fontcolor': 'blue',
       'r_disp': True,
       'stats': {}}


# In[12]:


corr_cv_dict \
    = {'line': {'color': 'royalblue',
                'linestyle': 'solid',
                'fillstyle': 'full',
                'linewidth': 3.0,
                'alpha': 1.0},
       'axv': {'color': 'red',
               'linestyle': '--',
               'fillstyle': 'full',
               'linewidth': 1.5,
               'alpha': 0.8},
       'marker': {'shape': 'o',
                  'color': 'lime',
                  'edgecolor': 'black',
                  'size': 8.0,
                  'edgewidth': 1.0},
       'title': {'text': [None],
                 'display': True,
                 'fontsize': 16.0,
                 'fontstyle': 'normal',
                 'fontweight': 'bold',
                 'loc': 'center',
                 'pad': 20.0},
       'xlabel': {'text': ['polynomial degree'],
                  'display': True,
                  'fontsize': 12.0,
                  'fontstyle': 'normal',
                  'fontweight': 'bold',
                  'labelpad': 4.0,
                  'loc': 'center',
                  'pad': 15.0},
       'ylabel': {'text': ['mean cv mse'],
                  'display': True,
                  'fontsize': 12.0,
                  'fontstyle': 'normal',
                  'fontweight': 'bold',
                  'labelpad': 4.0,
                  'loc': 'center',
                  'pad': 10.0},
       'xticks': {'display': True,
                  'fontsize': 10.0,
                  'rotation': 0.0},
       'yticks': {'display': True,
                  'fontsize': 10.0,
                  'rotation': 0.0},
       'xlim': {'display': False,
                'emit': True,
                'auto': False,
                'mode': 'set',
                'set': {'min': 0,
                        'max': 0},
                'adjust': {'left': 0,
                           'right': 0}},
       'ylim': {'display': False,
                'emit': True,
                'auto': False,
                'mode': 'set',
                'set': {'min': 0,
                        'max': 0},
                'adjust': {'left': 0,
                           'right': 0}},
       'grid': {'display': True,
                'visible': None,
                'which': 'major',
                'axis': 'both'},
       'legend': {'display': True,
                  'loc': 'best',
                  'fontsize': 10.0,
                  'bbox_to_anchor': None},
       'figure': {'width': 9.708,
                  'length': 6.0}}


# In[13]:


corr_scores_dict \
    = {'line': {'color': 'royalblue',
                'linestyle': 'solid',
                'fillstyle': 'full',
                'linewidth': 3.0,
                'alpha': 1.0},
       'axv': {'color': 'red',
               'linestyle': '--',
               'fillstyle': 'full',
               'linewidth': 1.5,
               'alpha': 0.8},
       'marker': {'shape': 'o',
                  'color': 'lime',
                  'edgecolor': 'black',
                  'size': 8.0,
                  'edgewidth': 1.0},
       'title': {'text': [None],
                 'display': True,
                 'fontsize': 16.0,
                 'fontstyle': 'normal',
                 'fontweight': 'bold',
                 'loc': 'center',
                 'pad': 20.0},
       'xlabel': {'text': ['polynomial degree'],
                  'display': True,
                  'fontsize': 12.0,
                  'fontstyle': 'normal',
                  'fontweight': 'bold',
                  'labelpad': 4.0,
                  'loc': 'center',
                  'pad': 15.0},
       'ylabel': {'text': ['score'],
                  'display': True,
                  'fontsize': 12.0,
                  'fontstyle': 'normal',
                  'fontweight': 'bold',
                  'labelpad': 4.0,
                  'loc': 'center',
                  'pad': 10.0},
       'xticks': {'display': True,
                  'fontsize': 10.0,
                  'rotation': 0.0},
       'yticks': {'display': True,
                  'fontsize': 10.0,
                  'rotation': 0.0},
       'xlim': {'display': False,
                'emit': True,
                'auto': False,
                'mode': 'set',
                'set': {'min': 0,
                        'max': 0},
                'adjust': {'left': 0,
                           'right': 0}},
       'ylim': {'display': False,
                'emit': True,
                'auto': False,
                'mode': 'set',
                'set': {'min': 0,
                        'max': 0},
                'adjust': {'left': 0,
                           'right': 0}},
       'grid': {'display': True,
                'visible': None,
                'which': 'major',
                'axis': 'both'},
       'legend': {'display': True,
                  'loc': 'best',
                  'fontsize': 10.0,
                  'bbox_to_anchor': None},
       'figure': {'width': 9.708,
                  'length': 6.0}}


# In[14]:


window_cv_dict \
    = {'line': {'color': 'royalblue',
                'linestyle': 'solid',
                'fillstyle': 'full',
                'linewidth': 3.0,
                'alpha': 1.0},
       'axfill': {'color': 'royalblue',
                  'alpha': 0.2},
       'axv': {'color': 'red',
               'linestyle': '--',
               'fillstyle': 'full',
               'linewidth': 1.5,
               'alpha': 0.8},
       'marker': {'shape': 'o',
                  'color': 'lime',
                  'edgecolor': 'black',
                  'size': 8.0,
                  'edgewidth': 1.0},
       'title': {'text': [None],
                 'display': True,
                 'fontsize': 16.0,
                 'fontstyle': 'normal',
                 'fontweight': 'bold',
                 'loc': 'center',
                 'pad': 20.0},
       'xlabel': {'text': ['window size (days)'],
                  'display': True,
                  'fontsize': 12.0,
                  'fontstyle': 'normal',
                  'fontweight': 'bold',
                  'labelpad': 4.0,
                  'loc': 'center',
                  'pad': 15.0},
       'ylabel': {'text': ['mean cv mse'],
                  'display': True,
                  'fontsize': 12.0,
                  'fontstyle': 'normal',
                  'fontweight': 'bold',
                  'labelpad': 4.0,
                  'loc': 'center',
                  'pad': 10.0},
       'xticks': {'display': True,
                  'fontsize': 10.0,
                  'rotation': 0.0},
       'yticks': {'display': True,
                  'fontsize': 10.0,
                  'rotation': 0.0},
       'xlim': {'display': False,
                'emit': True,
                'auto': False,
                'mode': 'set',
                'set': {'min': 0,
                        'max': 0},
                'adjust': {'left': 0,
                           'right': 0}},
       'ylim': {'display': False,
                'emit': True,
                'auto': False,
                'mode': 'set',
                'set': {'min': 0,
                        'max': 0},
                'adjust': {'left': 0,
                           'right': 0}},
       'grid': {'display': True,
                'visible': None,
                'which': 'major',
                'axis': 'both'},
       'legend': {'display': True,
                  'loc': 'best',
                  'fontsize': 10.0,
                  'bbox_to_anchor': None},
       'figure': {'width': 9.708,
                  'length': 6.0}}


# In[15]:


roll_corr_dict \
    = {'line': {'color': ['crimson', 'steelblue', 'darkorange'],
                'linestyle': 'solid',
                'fillstyle': 'full',
                'linewidth': 2.0,
                'alpha': 1.0},
       'params': {'window': 30,
                  'min_periods': 20},
       'axfill_upr': {'color': 'darkgreen',
                      'alpha': 0.1},
       'axfill_lwr': {'color': 'darkred',
                      'alpha': 0.1},
       'axh_ctr': {'color': 'black',
                   'linestyle': '--',
                   'fillstyle': 'full',
                   'linewidth': 1.5,
                   'alpha': 0.8},
       'axh_out': {'y': 0.3,
                   'color': 'green',
                   'linestyle': '--',
                   'fillstyle': 'full',
                   'linewidth': 1.5,
                   'alpha': 0.8},
       'marker': {'shape': 'o',
                  'color': 'lime',
                  'edgecolor': 'black',
                  'size': 0.0,
                  'edgewidth': 1.0},
       'title': {'text': [None],
                 'display': True,
                 'fontsize': 16.0,
                 'fontstyle': 'normal',
                 'fontweight': 'bold',
                 'loc': 'center',
                 'pad': 20.0},
       'xlabel': {'text': [''],
                  'display': True,
                  'fontsize': 13.0,
                  'fontstyle': 'normal',
                  'fontweight': 'bold',
                  'labelpad': 4.0,
                  'loc': 'center',
                  'pad': 15.0},
       'ylabel': {'text': [''],
                  'display': True,
                  'fontsize': 13.0,
                  'fontstyle': 'normal',
                  'fontweight': 'bold',
                  'labelpad': 4.0,
                  'loc': 'center',
                  'pad': 10.0},
       'xticks': {'display': True,
                  'fontsize': 11.0,
                  'rotation': 0.0},
       'yticks': {'display': True,
                  'fontsize': 11.0,
                  'rotation': 0.0},
       'xlim': {'display': False,
                'emit': True,
                'auto': False,
                'mode': 'set',
                'set': {'min': 0,
                        'max': 0},
                'adjust': {'left': 0,
                           'right': 0}},
       'ylim': {'display': False,
                'emit': True,
                'auto': False,
                'mode': 'set',
                'set': {'min': 0,
                        'max': 0},
                'adjust': {'left': 0,
                           'right': 0}},
       'grid': {'display': True,
                'visible': None,
                'which': 'major',
                'axis': 'both'},
       'legend': {'display': True,
                  'loc': 'best',
                  'fontsize': 11.0,
                  'bbox_to_anchor': None},
       'figure': {'width': 16.18033988749,
                  'length': 10.0,
                  'nplots': 3,
                  'nrows': 3,
                  'ncols': 1,
                  'sharex': True,
                  'sharey': False,
                  'stacked': False,
                  'wspace': None,
                  'hspace': None}}


# In[16]:


roll_corr_all_dict \
    = {'line': {'color': stacked_line_chart_colors,
                'linestyle': 'solid',
                'fillstyle': 'full',
                'linewidth': 2.0,
                'alpha': 1.0},
       'params': {'window': 30,
                  'min_periods': 20},
       'axh_ctr': {'color': 'black',
                   'linestyle': '--',
                   'fillstyle': 'full',
                   'linewidth': 1.5,
                   'alpha': 0.8},
       'axh_out': {'y': 0.3,
                   'color': 'green',
                   'linestyle': '--',
                   'fillstyle': 'full',
                   'linewidth': 1.5,
                   'alpha': 0.8},
       'marker': {'shape': 'o',
                  'color': 'lime',
                  'edgecolor': 'black',
                  'size': 0.0,
                  'edgewidth': 1.0},
       'title': {'text': [None],
                 'display': True,
                 'fontsize': 16.0,
                 'fontstyle': 'normal',
                 'fontweight': 'bold',
                 'loc': 'center',
                 'pad': 20.0},
       'xlabel': {'text': [''],
                  'display': True,
                  'fontsize': 13.0,
                  'fontstyle': 'normal',
                  'fontweight': 'bold',
                  'labelpad': 4.0,
                  'loc': 'center',
                  'pad': 15.0},
       'ylabel': {'text': [''],
                  'display': True,
                  'fontsize': 13.0,
                  'fontstyle': 'normal',
                  'fontweight': 'bold',
                  'labelpad': 4.0,
                  'loc': 'center',
                  'pad': 10.0},
       'xticks': {'display': True,
                  'fontsize': 11.0,
                  'rotation': 0.0},
       'yticks': {'display': True,
                  'fontsize': 11.0,
                  'rotation': 0.0},
       'xlim': {'display': False,
                'emit': True,
                'auto': False,
                'mode': 'set',
                'set': {'min': 0,
                        'max': 0},
                'adjust': {'left': 0,
                           'right': 0}},
       'ylim': {'display': True,
                'emit': True,
                'auto': False,
                'mode': 'set',
                'set': {'min': -1.0,
                        'max': 1.0},
                'adjust': {'left': 0,
                           'right': 0}},
       'grid': {'display': True,
                'visible': None,
                'which': 'major',
                'axis': 'both'},
       'legend': {'display': True,
                  'loc': 'best',
                  'fontsize': 11.0,
                  'bbox_to_anchor': None},
       'figure': {'width': 16.18033988749,
                  'length': 10.0,
                  'nplots': 3,
                  'nrows': 3,
                  'ncols': 1,
                  'sharex': True,
                  'sharey': False,
                  'stacked': False,
                  'wspace': None,
                  'hspace': None}}


# In[17]:


lag_corr_dict \
    = {'line': {'color': 'darkorange',
                'linestyle': 'solid',
                'fillstyle': 'full',
                'linewidth': 2.0,
                'alpha': 1.0},
       'params': {'horizontal': False,
                  'stacked': False,
                  'align': 'center',
                  'upr_clr': 'green',
                  'lwr_clr': 'red',
                  'edgecolor': 'black',
                  'linewidth': 1.5,
                  'tick_label': None,
                  'log': False,
                  'alpha': 1.0,
                  'max_lag': 60,
                  'method': 'pearson'},
       'axfill_upr': {'color': 'darkgreen',
                      'alpha': 0.1},
       'axfill_lwr': {'color': 'darkred',
                      'alpha': 0.1},
       'axh_ctr': {'color': 'black',
                   'linestyle': '--',
                   'fillstyle': 'full',
                   'linewidth': 1.5,
                   'alpha': 0.8},
       'axh_out': {'y': 0.3,
                   'color': 'green',
                   'linestyle': '--',
                   'fillstyle': 'full',
                   'linewidth': 1.5,
                   'alpha': 0.8},
       'axv': {'color': 'red',
               'linestyle': '--',
               'fillstyle': 'full',
               'linewidth': 1.5,
               'alpha': 0.8},
       'annotation':{'arrw_stl': '->',
                     'arrw_clr': 'black',
                     'fontsize': 11.0,
                     'xoffset': 3.0,
                     'yoffset': -0.35},
       'vertical': {'width': 0.5,
                    'bottom': 0},
       'horizontal': {'height': 0.5,
                      'left': 0},
       'marker': {'shape': 'o',
                  'color': 'lime',
                  'edgecolor': 'black',
                  'size': 0.0,
                  'edgewidth': 1.0},
       'title': {'text': [None],
                 'display': True,
                 'fontsize': 16.0,
                 'fontstyle': 'normal',
                 'fontweight': 'bold',
                 'loc': 'center',
                 'pad': 20.0},
       'xlabel': {'text': [None],
                  'display': True,
                  'fontsize': 13.0,
                  'fontstyle': 'normal',
                  'fontweight': 'normal',
                  'labelpad': 4.0,
                  'loc': 'center',
                  'pad': 10.0},
       'ylabel': {'text': [None],
                  'display': True,
                  'fontsize': 13.0,
                  'fontstyle': 'normal',
                  'fontweight': 'normal',
                  'labelpad': 4.0,
                  'loc': 'center',
                  'pad': 10.0},
       'xlim': {'display': False,
                'emit': True,
                'auto': False,
                'mode': 'set',
                'set': {'min': 0,
                        'max': 0},
                'adjust': {'left': 0,
                           'right': 0}},
       'ylim': {'display': True,
                'emit': True,
                'auto': False,
                'mode': 'set',
                'set': {'min': -1.0,
                        'max': 1.0},
                'adjust': {'left': 0,
                           'right': 0}},
       'xticks': {'display': True,
                  'fontsize': 11.0,
                  'rotation': 90.0},
       'yticks': {'display': True,
                  'fontsize': 11.0,
                  'rotation': 0.0},
       'grid': {'display': True,
                'visible': None,
                'which': 'major',
                'axis': 'y'},
       'legend': {'display': True,
                  'loc': 'best',
                  'fontsize': 11.0,
                  'bbox_to_anchor': None},
       'figure': {'width': 15.0,
                  'length': 7.5}}


# In[18]:


lag_heat_dict \
    = {'params': {'max_lag': 60,
                  'method': 'spearman',
                  'aspect': 'auto',
                  'cmap': 'tab20c',
                  'vmin': -1.0,
                  'vmax': 1.0},
       'axv': {'color': 'red',
               'linestyle': '--',
               'fillstyle': 'full',
               'linewidth': 1.5,
               'alpha': 0.8},
       'title': {'text': [None],
                 'display': True,
                 'fontsize': 16.0,
                 'fontstyle': 'normal',
                 'fontweight': 'bold',
                 'loc': 'center',
                 'pad': 15.0},
       'xlabel': {'text': [None],
                  'display': True,
                  'fontsize': 13.0,
                  'fontstyle': 'normal',
                  'fontweight': 'bold',
                  'labelpad': 4.0,
                  'loc': 'center',
                  'pad': 10.0},
       'ylabel': {'text': [None],
                  'display': True,
                  'fontsize': 13.0,
                  'fontstyle': 'normal',
                  'fontweight': 'normal',
                  'labelpad': 4.0,
                  'loc': 'center',
                  'pad': 10.0},
       'xlim': {'display': False,
                'emit': True,
                'auto': False,
                'mode': 'set',
                'set': {'min': 0,
                        'max': 0},
                'adjust': {'left': 0,
                           'right': 0}},
       'ylim': {'display': False,
                'emit': True,
                'auto': False,
                'mode': 'set',
                'set': {'min': -1.0,
                        'max': 1.0},
                'adjust': {'left': 0,
                           'right': 0}},
       'xticks': {'display': True,
                  'fontsize': 11.0,
                  'rotation': 90.0},
       'yticks': {'display': True,
                  'fontsize': 11.0,
                  'rotation': 0.0},
       'grid': {'display': True,
                'visible': None,
                'which': 'major',
                'axis': 'y'},
       'legend': {'display': True,
                  'loc': 'best',
                  'fontsize': 11.0,
                  'bbox_to_anchor': None},
       'figure': {'width': 24.0,
                  'length': 8.0}}


# In[19]:


bar_multichart_dict \
    = {'figure': {'width': 15.0,
                  'length': 5.5181,
                  'nplots': 0,
                  'nrows': 0,
                  'ncols': 0,
                  'sharex': False,
                  'sharey': False,
                  'stacked': False,
                  'wspace': None,
                  'hspace': None},
       'suptitle': {'text': None,
                    'x': 0.5,
                    'y': 0.98,
                    'horizontalalignment': 'center',
                    'verticalalignment': 'top',
                    'fontproperties': {'family': 'sans-serif',
                                       'style': 'normal',
                                       'variant': 'normal',
                                       'stretch': 'normal',
                                       'weight': 'bold',
                                       'size': 28.0,
                                       'math_fontfamily': 'dejavusans'}},
       'supxlabel': {'text': None,
                     'x': 0.5,
                     'y': 0.04,
                     'horizontalalignment': 'center',
                     'verticalalignment': 'bottom',
                     'fontproperties': {'family': 'sans-serif',
                                        'style': 'normal',
                                        'variant': 'normal',
                                        'stretch': 'normal',
                                        'weight': 'bold',
                                        'size': 22.0,
                                        'math_fontfamily': 'dejavusans'}},
       'supylabel': {'text': None,
                     'x': 0.02,
                     'y': 0.5,
                     'horizontalalignment': 'left',
                     'verticalalignment': 'center',
                     'fontproperties': {'family': 'sans-serif',
                                        'style': 'normal',
                                        'variant': 'normal',
                                        'stretch': 'normal',
                                        'weight': 'bold',
                                        'size': 22.0,
                                        'math_fontfamily': 'dejavusans'}},
       'tight_layout': {'display': True,
                        'pad': 3.0,
                        'h_pad': None,
                        'w_pad': None,
                        'rect': None}}


# In[20]:


boxplot_multichart_dict \
    = {'figure': {'width': 15.0,
                  'length': 5.5181,
                  'nplots': 0,
                  'nrows': 0,
                  'ncols': 0,
                  'sharex': False,
                  'sharey': False,
                  'stacked': False},
       'suptitle': {'text': None,
                    'x': 0.5,
                    'y': 0.98,
                    'horizontalalignment': 'center',
                    'verticalalignment': 'top',
                    'fontproperties': {'family': 'sans-serif',
                                       'style': 'normal',
                                       'variant': 'normal',
                                       'stretch': 'normal',
                                       'weight': 'bold',
                                       'size': 28.0,
                                       'math_fontfamily': 'dejavusans'}},
       'supxlabel': {'text': None,
                     'x': 0.5,
                     'y': 0.04,
                     'horizontalalignment': 'center',
                     'verticalalignment': 'bottom',
                     'fontproperties': {'family': 'sans-serif',
                                        'style': 'normal',
                                        'variant': 'normal',
                                        'stretch': 'normal',
                                        'weight': 'bold',
                                        'size': 22.0,
                                        'math_fontfamily': 'dejavusans'}},
       'supylabel': {'text': None,
                     'x': 0.5,
                     'y': 0.01,
                     'horizontalalignment': 'left',
                     'verticalalignment': 'center',
                     'fontproperties': {'family': 'sans-serif',
                                        'style': 'normal',
                                        'variant': 'normal',
                                        'stretch': 'normal',
                                        'weight': 'bold',
                                        'size': 22.0,
                                        'math_fontfamily': 'dejavusans'}},
       'tight_layout': {'display': True,
                        'pad': 3.0,
                        'h_pad': None,
                        'w_pad': None,
                        'rect': None}}


# In[21]:


histogram_multichart_dict \
    = {'figure': {'width': 15.0,
                  'length': 5.5181,
                  'nplots': 0,
                  'nrows': 0,
                  'ncols': 0,
                  'sharex': False,
                  'sharey': False,
                  'stacked': False,
                  'wspace': None,
                  'hspace': None},
       'suptitle': {'text': None,
                    'x': 0.5,
                    'y': 0.98,
                    'horizontalalignment': 'center',
                    'verticalalignment': 'top',
                    'fontproperties': {'family': 'sans-serif',
                                       'style': 'normal',
                                       'variant': 'normal',
                                       'stretch': 'normal',
                                       'weight': 'bold',
                                       'size': 28.0,
                                       'math_fontfamily': 'dejavusans'}},
       'supxlabel': {'text': None,
                     'x': 0.5,
                     'y': 0.04,
                     'horizontalalignment': 'center',
                     'verticalalignment': 'bottom',
                     'fontproperties': {'family': 'sans-serif',
                                        'style': 'normal',
                                        'variant': 'normal',
                                        'stretch': 'normal',
                                        'weight': 'bold',
                                        'size': 22.0,
                                        'math_fontfamily': 'dejavusans'}},
       'supylabel': {'text': None,
                     'x': 0.02,
                     'y': 0.5,
                     'horizontalalignment': 'left',
                     'verticalalignment': 'center',
                     'fontproperties': {'family': 'sans-serif',
                                        'style': 'normal',
                                        'variant': 'normal',
                                        'stretch': 'normal',
                                        'weight': 'bold',
                                        'size': 22.0,
                                        'math_fontfamily': 'dejavusans'}},
       'tight_layout': {'display': True,
                        'pad': 3.0,
                        'h_pad': None,
                        'w_pad': None,
                        'rect': None}}


# In[22]:


line_multichart_dict \
    = {'figure': {'width': 15.0,
                  'length': 5.5181,
                  'nplots': 0,
                  'nrows': 0,
                  'ncols': 0,
                  'sharex': False,
                  'sharey': False,
                  'stacked': False,
                  'wspace': None,
                  'hspace': None},
       'suptitle': {'text': None,
                    'x': 0.5,
                    'y': 0.98,
                    'horizontalalignment': 'center',
                    'verticalalignment': 'top',
                    'fontproperties': {'family': 'sans-serif',
                                       'style': 'normal',
                                       'variant': 'normal',
                                       'stretch': 'normal',
                                       'weight': 'bold',
                                       'size': 28.0,
                                       'math_fontfamily': 'dejavusans'}},
       'supxlabel': {'text': None,
                     'x': 0.5,
                     'y': 0.04,
                     'horizontalalignment': 'center',
                     'verticalalignment': 'bottom',
                     'fontproperties': {'family': 'sans-serif',
                                        'style': 'normal',
                                        'variant': 'normal',
                                        'stretch': 'normal',
                                        'weight': 'bold',
                                        'size': 22.0,
                                        'math_fontfamily': 'dejavusans'}},
       'supylabel': {'text': None,
                     'x': 0.02,
                     'y': 0.5,
                     'horizontalalignment': 'left',
                     'verticalalignment': 'center',
                     'fontproperties': {'family': 'sans-serif',
                                        'style': 'normal',
                                        'variant': 'normal',
                                        'stretch': 'normal',
                                        'weight': 'bold',
                                        'size': 22.0,
                                        'math_fontfamily': 'dejavusans'}},
       'tight_layout': {'display': True,
                        'pad': 3.0,
                        'h_pad': None,
                        'w_pad': None,
                        'rect': None}}


# In[23]:


pie_multichart_dict \
    = {'figure': {'width': 15.0,
                  'length': 5.5181,
                  'nplots': 0,
                  'nrows': 0,
                  'ncols': 0,
                  'sharex': False,
                  'sharey': False,
                  'stacked': False,
                  'wspace': None,
                  'hspace': None},
       'suptitle': {'text': None,
                    'x': 0.5,
                    'y': 0.98,
                    'horizontalalignment': 'center',
                    'verticalalignment': 'top',
                    'fontproperties': {'family': 'sans-serif',
                                       'style': 'normal',
                                       'variant': 'normal',
                                       'stretch': 'normal',
                                       'weight': 'bold',
                                       'size': 28.0,
                                       'math_fontfamily': 'dejavusans'}},
       'supxlabel': {'text': None,
                     'x': 0.5,
                     'y': 0.04,
                     'horizontalalignment': 'center',
                     'verticalalignment': 'bottom',
                     'fontproperties': {'family': 'sans-serif',
                                        'style': 'normal',
                                        'variant': 'normal',
                                        'stretch': 'normal',
                                        'weight': 'bold',
                                        'size': 22.0,
                                        'math_fontfamily': 'dejavusans'}},
       'supylabel': {'text': None,
                     'x': 0.02,
                     'y': 0.5,
                     'horizontalalignment': 'left',
                     'verticalalignment': 'center',
                     'fontproperties': {'family': 'sans-serif',
                                        'style': 'normal',
                                        'variant': 'normal',
                                        'stretch': 'normal',
                                        'weight': 'bold',
                                        'size': 22.0,
                                        'math_fontfamily': 'dejavusans'}},
       'tight_layout': {'display': True,
                        'pad': 3.0,
                        'h_pad': None,
                        'w_pad': None,
                        'rect': None}}


# In[24]:


plot_multichart_dict \
    = {'figure': {'width': 15.0,
                  'length': 5.5181,
                  'nplots': 0,
                  'nrows': 0,
                  'ncols': 0,
                  'sharex': False,
                  'sharey': False,
                  'stacked': False,
                  'wspace': None,
                  'hspace': None},
       'suptitle': {'text': None,
                    'x': 0.5,
                    'y': 0.98,
                    'horizontalalignment': 'center',
                    'verticalalignment': 'top',
                    'fontproperties': {'family': 'sans-serif',
                                       'style': 'normal',
                                       'variant': 'normal',
                                       'stretch': 'normal',
                                       'weight': 'bold',
                                       'size': 28.0,
                                       'math_fontfamily': 'dejavusans'}},
       'supxlabel': {'text': None,
                     'x': 0.5,
                     'y': 0.04,
                     'horizontalalignment': 'center',
                     'verticalalignment': 'bottom',
                     'fontproperties': {'family': 'sans-serif',
                                        'style': 'normal',
                                        'variant': 'normal',
                                        'stretch': 'normal',
                                        'weight': 'bold',
                                        'size': 22.0,
                                        'math_fontfamily': 'dejavusans'}},
       'supylabel': {'text': None,
                     'x': 0.02,
                     'y': 0.5,
                     'horizontalalignment': 'left',
                     'verticalalignment': 'center',
                     'fontproperties': {'family': 'sans-serif',
                                        'style': 'normal',
                                        'variant': 'normal',
                                        'stretch': 'normal',
                                        'weight': 'bold',
                                        'size': 22.0,
                                        'math_fontfamily': 'dejavusans'}},
       'tight_layout': {'display': True,
                        'pad': 3.0,
                        'h_pad': None,
                        'w_pad': None,
                        'rect': None}}


# In[25]:


scatterplot_multichart_dict \
    = {'figure': {'width': 15.0,
                  'length': 5.5181,
                  'nplots': 0,
                  'nrows': 0,
                  'ncols': 0,
                  'sharex': False,
                  'sharey': False,
                  'stacked': False,
                  'wspace': None,
                  'hspace': None},
       'suptitle': {'text': None,
                    'x': 0.5,
                    'y': 0.98,
                    'horizontalalignment': 'center',
                    'verticalalignment': 'top',
                    'fontproperties': {'family': 'sans-serif',
                                       'style': 'normal',
                                       'variant': 'normal',
                                       'stretch': 'normal',
                                       'weight': 'bold',
                                       'size': 28.0,
                                       'math_fontfamily': 'dejavusans'}},
       'supxlabel': {'text': None,
                     'x': 0.5,
                     'y': 0.04,
                     'horizontalalignment': 'center',
                     'verticalalignment': 'bottom',
                     'fontproperties': {'family': 'sans-serif',
                                        'style': 'normal',
                                        'variant': 'normal',
                                        'stretch': 'normal',
                                        'weight': 'bold',
                                        'size': 22.0,
                                        'math_fontfamily': 'dejavusans'}},
       'supylabel': {'text': None,
                     'x': 0.02,
                     'y': 0.5,
                     'horizontalalignment': 'left',
                     'verticalalignment': 'center',
                     'fontproperties': {'family': 'sans-serif',
                                        'style': 'normal',
                                        'variant': 'normal',
                                        'stretch': 'normal',
                                        'weight': 'bold',
                                        'size': 22.0,
                                        'math_fontfamily': 'dejavusans'}},
       'tight_layout': {'display': True,
                        'pad': 3.0,
                        'h_pad': None,
                        'w_pad': None,
                        'rect': None}}


# In[26]:


bar_chart_def_dict = copy.deepcopy(bar_chart_dict)

boxplot_chart_def_dict = copy.deepcopy(boxplot_chart_dict)

histogram_chart_def_dict = copy.deepcopy(histogram_chart_dict)

line_chart_def_dict = copy.deepcopy(line_chart_dict)

pie_chart_def_dict = copy.deepcopy(pie_chart_dict)

plot_chart_def_dict = copy.deepcopy(plot_chart_dict)

scatterplot_chart_def_dict = copy.deepcopy(scatterplot_chart_dict)


regr_line_def_dict = copy.deepcopy(regr_line_dict)

corr_cv_def_dict = copy.deepcopy(corr_cv_dict)

corr_scores_def_dict = copy.deepcopy(corr_scores_dict)

window_cv_def_dict = copy.deepcopy(window_cv_dict)

roll_corr_def_dict = copy.deepcopy(roll_corr_dict)

roll_corr_all_def_dict = copy.deepcopy(roll_corr_all_dict)

lag_corr_def_dict = copy.deepcopy(lag_corr_dict)

lag_heat_def_dict = copy.deepcopy(lag_heat_dict)


bar_multichart_def_dict = copy.deepcopy(bar_multichart_dict)

boxplot_multichart_def_dict = copy.deepcopy(boxplot_multichart_dict)

histogram_multichart_def_dict = copy.deepcopy(histogram_multichart_dict)

line_multichart_def_dict = copy.deepcopy(line_multichart_dict)

pie_multichart_def_dict = copy.deepcopy(pie_multichart_dict)

plot_multichart_def_dict = copy.deepcopy(plot_multichart_dict)

scatterplot_multichart_def_dict = copy.deepcopy(scatterplot_multichart_dict)


# In[27]:


#*******************************************************************************************
 #
 #  Function Name:  calc_rows_and_cols
 #
 #  Function Description:
 #      The function returns the number of rows and columns based on the number of plots.
 #
 #
 #  Return Type: int, int
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  dictionary     chart_dict       The parameter is the multichart dictionary.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def calc_rows_and_cols(chart_dict): return mathx.calc_clst_factors(chart_dict['figure']['nplots'])


# In[28]:


#*******************************************************************************************
 #
 #  Function Name:  proc_rvalues
 #
 #  Function Description:
 #      The function processes the r-value for display or storage.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  dict           rslt_dict        The parameter is the r-values and p-values.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def proc_rvalues(rslt_dict):

    global regr_line_dict


    if regr_line_dict['r_disp']:

        for k, v in rslt_dict.items():

            tabs = '\t\t' if k == 'tau (kendall)' else '\t'

            rtn = '\n' if k == 'tau (kendall)' else ''

            logx.print_and_log_text(f'{k}:{tabs}{v:.3f}{rtn}')

        logx.print_and_log_text('\n')

    else: regr_line_dict['stats'] = copy.deepcopy(rslt_dict)


# In[29]:


#*******************************************************************************************
 #
 #  Function Name:  stacked_bar_chart_setup
 #
 #  Function Description:
 #      The function sets two parmeters expected for a stacked bar chart.
 #
 #
 #  Return Type: string, string
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  bool           stacked_bool     The parameter indicates whether the bar chart is stacked.
 #  bool           lgnd_disp_bool   The parameter indicates whether the bar chart's legend 
 #                                  is visible.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def stacked_bar_chart_setup(stacked_bool = True, lgnd_disp_bool = True):

    global bar_chart_dict

    bar_chart_dict['params']['stacked'] = stacked_bool

    bar_chart_dict['legend']['display'] = lgnd_disp_bool


# In[30]:


#*******************************************************************************************
 #
 #  Function Name:  rtn_fmt_regr_tbl
 #
 #  Function Description:
 #      The function returns a formatted table of r-values for regressions.
 #
 #
 #  Return Type: styler
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  array          idx_array        The parameter is the index array.
 #  string         title            The parameter is the table title.
 #  string         first_clr        The parameter is the first highlight color.
 #  string         sec_clr          The parameter is the second highlight color.
 #  boolean        hide_idx_bool    The parameter indicates whether the index is visible.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def rtn_fmt_regr_tbl \
        (idx_array, 
         title,
         first_clr = '#50C878', 
         sec_clr = '#C2E5D3', 
         hide_idx_bool = False):

    r_sqr_flt = regr_line_dict['stats']['r_prsn'] * regr_line_dict['stats']['r_prsn']


    data_df = pd.DataFrame(zip(regr_line_dict['stats']['r_prsn'], r_sqr_flt))

    data_df.columns = ['r_values', 'r_squared']

    data_df.index = idx_array


    return \
        pandasx.rtn_fmt_tbl \
            (data_df,
             title, 
             hide_idx_bool = hide_idx_bool) \
                .format \
                    ({'r_values': pandasx.fmt_dict['regr_flt'],
                      'r_squared': pandasx.fmt_dict['regr_flt']}) \
                .apply \
                    (pandasx.highlight_top_two,
                     props_max = f'background-color: {first_clr}',
                     props_second = f'background-color: {sec_clr}',
                     subset = data_df.columns)


# In[31]:


#*******************************************************************************************
 #
 #  Function Name:  get_chart_dict
 #
 #  Function Description:
 #      The function retrieves the dictionary.
 #
 #
 #  Return Type: string, string
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  int            chart_type       The parameter is the chart type enumeration value.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_chart_dict(chart_type):

    if chart_type == chart_enum.BAR.value: return bar_chart_dict

    elif chart_type == chart_enum.BOXPLOT.value: return boxplot_chart_dict

    elif chart_type == chart_enum.HISTOGRAM.value: return histogram_chart_dict

    elif chart_type == chart_enum.LINE.value: return line_chart_dict

    elif chart_type == chart_enum.PIE.value: return pie_chart_dict

    elif chart_type == chart_enum.PLOT.value: return plot_chart_dict

    elif chart_type == chart_enum.SCATTER.value: return scatterplot_chart_dict

    elif chart_type == chart_enum.REGR_LINE.value: return regr_line_dict

    elif chart_type == chart_enum.CORR_CV.value: return corr_cv_dict

    elif chart_type == chart_enum.CORR_SCORES.value: return corr_scores_dict

    elif chart_type == chart_enum.WINDOW_CV.value: return window_cv_dict

    elif chart_type == chart_enum.ROLL_CORR.value: return roll_corr_dict

    elif chart_type == chart_enum.ROLL_CORR_ALL.value: return roll_corr_all_dict

    elif chart_type == chart_enum.LAG_CORR.value: return lag_corr_dict  

    elif chart_type == chart_enum.LAG_HEAT.value: return lag_heat_dict 

    elif chart_type == chart_enum.MULTIBAR.value: return bar_multichart_dict

    elif chart_type == chart_enum.MULTIBOXPLOT.value: return boxplot_multichart_dict

    elif chart_type == chart_enum.MULTIHISTOGRAM.value: return histogram_multichart_dict

    elif chart_type == chart_enum.MULTILINE.value: return line_multichart_dict

    elif chart_type == chart_enum.MULTIPIE.value: return pie_multichart_dict

    elif chart_type == chart_enum.MULTIPLOT.value: return plot_multichart_dict

    elif chart_type == chart_enum.MULTISCATTER.value: return scatterplot_multichart_dict

    else: return None


# In[32]:


#*******************************************************************************************
 #
 #  Function Name:  get_chart_def_dict
 #
 #  Function Description:
 #      The function retrieves the default dictionary.
 #
 #
 #  Return Type: string, string
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  int            chart_type       The parameter is the chart type enumeration value.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_chart_def_dict(chart_type):

    if chart_type == chart_enum.BAR.value: return copy.deepcopy(bar_chart_def_dict)

    elif chart_type == chart_enum.BOXPLOT.value: return copy.deepcopy(boxplot_chart_def_dict)

    elif chart_type == chart_enum.HISTOGRAM.value: return copy.deepcopy(histogram_chart_def_dict)

    elif chart_type == chart_enum.LINE.value: return copy.deepcopy(line_chart_def_dict)

    elif chart_type == chart_enum.PIE.value: return copy.deepcopy(pie_chart_def_dict)

    elif chart_type == chart_enum.PLOT.value: return copy.deepcopy(plot_chart_def_dict)

    elif chart_type == chart_enum.SCATTER.value: return copy.deepcopy(scatterplot_chart_def_dict)

    elif chart_type == chart_enum.REGR_LINE.value: return copy.deepcopy(regr_line_def_dict)

    elif chart_type == chart_enum.CORR_CV.value: return copy.deepcopy(corr_cv_def_dict)

    elif chart_type == chart_enum.CORR_SCORES.value: return copy.deepcopy(corr_scores_def_dict)

    elif chart_type == chart_enum.WINDOW_CV.value: return copy.deepcopy(window_cv_def_dict)

    elif chart_type == chart_enum.ROLL_CORR.value: return copy.deepcopy(roll_corr_def_dict)

    elif chart_type == chart_enum.ROLL_CORR_ALL.value: return copy.deepcopy(roll_corr_all_def_dict)

    elif chart_type == chart_enum.LAG_CORR.value: return copy.deepcopy(lag_corr_def_dict)

    elif chart_type == chart_enum.LAG_HEAT.value: return copy.deepcopy(lag_heat_def_dict)

    elif chart_type == chart_enum.MULTIBAR.value: return copy.deepcopy(bar_multichart_def_dict)

    elif chart_type == chart_enum.MULTIBOXPLOT.value: return copy.deepcopy(boxplot_multichart_def_dict)

    elif chart_type == chart_enum.MULTIHISTOGRAM.value: return copy.deepcopy(histogram_multichart_def_dict)

    elif chart_type == chart_enum.MULTILINE.value: return copy.deepcopy(line_multichart_def_dict)

    elif chart_type == chart_enum.MULTIPIE.value: return copy.deepcopy(pie_multichart_def_dict)

    elif chart_type == chart_enum.MULTIPLOT.value: return copy.deepcopy(plot_multichart_def_dict)

    elif chart_type == chart_enum.MULTISCATTER.value: return copy.deepcopy(scatterplot_multichart_def_dict)

    else: return None


# In[33]:


#*******************************************************************************************
 #
 #  Function Name:  get_title
 #
 #  Function Description:
 #      The function retrieves the chart's titles.
 #
 #
 #  Return Type: string, string
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  enum           chart_type       The parameter is the chart type enumeration value.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_title(chart_type):

    if chart_type == chart_enum.BAR.value: return bar_chart_dict['title']['text']

    elif chart_type == chart_enum.BOXPLOT.value: return boxplot_chart_dict['title']['text']

    elif chart_type == chart_enum.HISTOGRAM.value: return histogram_chart_dict['title']['text']

    elif chart_type == chart_enum.LINE.value: return line_chart_dict['title']['text']

    elif chart_type == chart_enum.PIE.value: return pie_chart_dict['title']['text']

    elif chart_type == chart_enum.PLOT.value: return plot_chart_dict['title']['text']

    elif chart_type == chart_enum.SCATTER.value: return scatterplot_chart_dict['title']['text']

    elif chart_type == chart_enum.CORR_CV.value: return corr_cv_dict['title']['text']

    elif chart_type == chart_enum.CORR_SCORES.value: return corr_scores_dict['title']['text']

    elif chart_type == chart_enum.WINDOW_CV.value: return window_cv_dict['title']['text']

    elif chart_type == chart_enum.ROLL_CORR.value: return roll_corr_dict['title']['text']

    elif chart_type == chart_enum.ROLL_CORR_ALL.value: return roll_corr_all_dict['title']['text']

    elif chart_type == chart_enum.LAG_CORR.value: return lag_corr_dict['title']['text']

    elif chart_type == chart_enum.LAG_HEAT.value: return lag_heat_dict['title']['text']

    else: return None


# In[34]:


#*******************************************************************************************
 #
 #  Function Name:  get_title_display
 #
 #  Function Description:
 #      The function retrieves the chart's title display indicator.
 #
 #
 #  Return Type: boolean
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  enum           chart_type       The parameter is the chart type enumeration value.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_title_display(chart_type):

    if chart_type == chart_enum.BAR.value: return bar_chart_dict['title']['display']

    elif chart_type == chart_enum.BOXPLOT.value: return boxplot_chart_dict['title']['display']

    elif chart_type == chart_enum.HISTOGRAM.value: return histogram_chart_dict['title']['display']

    elif chart_type == chart_enum.LINE.value: return line_chart_dict['title']['display']

    elif chart_type == chart_enum.PIE.value: return pie_chart_dict['title']['display']

    elif chart_type == chart_enum.PLOT.value: return plot_chart_dict['title']['display']

    elif chart_type == chart_enum.SCATTER.value: return scatterplot_chart_dict['title']['display']

    elif chart_type == chart_enum.CORR_CV.value: return corr_cv_dict['title']['display']

    elif chart_type == chart_enum.CORR_SCORES.value: return corr_scores_dict['title']['display']

    elif chart_type == chart_enum.WINDOW_CV.value: return window_cv_dict['title']['display']

    elif chart_type == chart_enum.ROLL_CORR.value: return roll_corr_dict['title']['display']

    elif chart_type == chart_enum.ROLL_CORR_ALL.value: return roll_corr_all_dict['title']['display']

    elif chart_type == chart_enum.LAG_CORR.value: return lag_corr_dict['title']['display']

    elif chart_type == chart_enum.LAG_HEAT.value: return lag_heat_dict['title']['display']

    else: return None


# In[35]:


#*******************************************************************************************
 #
 #  Function Name:  get_title_fontsize
 #
 #  Function Description:
 #      The function retrieves the chart's title font size.
 #
 #
 #  Return Type: float
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  enum           chart_type       The parameter is the chart type enumeration value.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_title_fontsize(chart_type):

    if chart_type == chart_enum.BAR.value: return bar_chart_dict['title']['fontsize']

    elif chart_type == chart_enum.BOXPLOT.value: return boxplot_chart_dict['title']['fontsize']

    elif chart_type == chart_enum.HISTOGRAM.value: return histogram_chart_dict['title']['fontsize']

    elif chart_type == chart_enum.LINE.value: return line_chart_dict['title']['fontsize']

    elif chart_type == chart_enum.PIE.value: return pie_chart_dict['title']['fontsize']

    elif chart_type == chart_enum.PLOT.value: return plot_chart_dict['title']['fontsize']

    elif chart_type == chart_enum.SCATTER.value: return scatterplot_chart_dict['title']['fontsize']

    elif chart_type == chart_enum.CORR_CV.value: return corr_cv_dict['title']['fontsize']

    elif chart_type == chart_enum.CORR_SCORES.value: return corr_scores_dict['title']['fontsize']

    elif chart_type == chart_enum.WINDOW_CV.value: return window_cv_dict['title']['fontsize']

    elif chart_type == chart_enum.ROLL_CORR.value: return roll_corr_dict['title']['fontsize']

    elif chart_type == chart_enum.LAG_CORR.value: return lag_corr_dict['title']['fontsize']

    elif chart_type == chart_enum.LAG_HEAT.value: return lag_heat_dict['title']['fontsize']

    else: return None


# In[36]:


#*******************************************************************************************
 #
 #  Function Name:  get_title_pad
 #
 #  Function Description:
 #      The function retrieves the chart's title pad.
 #
 #
 #  Return Type: float
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  enum           chart_type       The parameter is the chart type enumeration value.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_title_pad(chart_type):

    if chart_type == chart_enum.BAR.value: return bar_chart_dict['title']['pad']

    elif chart_type == chart_enum.BOXPLOT.value: return boxplot_chart_dict['title']['pad']

    elif chart_type == chart_enum.HISTOGRAM.value: return histogram_chart_dict['title']['pad']

    elif chart_type == chart_enum.LINE.value: return line_chart_dict['title']['pad']

    elif chart_type == chart_enum.PIE.value: return pie_chart_dict['title']['pad']

    elif chart_type == chart_enum.PLOT.value: return plot_chart_dict['title']['pad']

    elif chart_type == chart_enum.SCATTER.value: return scatterplot_chart_dict['title']['pad']

    elif chart_type == chart_enum.CORR_CV.value: return corr_cv_dict['title']['pad']

    elif chart_type == chart_enum.CORR_SCORES.value: return corr_scores_dict['title']['pad']

    elif chart_type == chart_enum.WINDOW_CV.value: return window_cv_dict['title']['pad']

    elif chart_type == chart_enum.ROLL_CORR.value: return roll_corr_dict['title']['pad']

    elif chart_type == chart_enum.ROLL_CORR_ALL.value: return roll_corr_all_dict['title']['pad']

    elif chart_type == chart_enum.LAG_CORR.value: return lag_corr_dict['title']['pad']

    elif chart_type == chart_enum.LAG_HEAT.value: return lag_heat_dict['title']['pad']

    else: return None


# In[37]:


#*******************************************************************************************
 #
 #  Function Name:  get_xylabels
 #
 #  Function Description:
 #      The function retrieves the chart's x-axis label and y-axis label.
 #
 #
 #  Return Type: string, string
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  enum           chart_type       The parameter is the chart type enumeration value.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_xylabels(chart_type):

    if chart_type == chart_enum.BAR.value:

        return \
            bar_chart_dict['xlabel']['text'], \
            bar_chart_dict['ylabel']['text']

    elif chart_type == chart_enum.BOXPLOT.value:

        return \
            boxplot_chart_dict['xlabel']['text'], \
            boxplot_chart_dict['ylabel']['text']

    elif chart_type == chart_enum.HISTOGRAM.value:

        return \
            histogram_chart_dict['xlabel']['text'], \
            histogram_chart_dict['ylabel']['text']

    elif chart_type == chart_enum.LINE.value:

        return \
            line_chart_dict['xlabel']['text'], \
            line_chart_dict['ylabel']['text']

    elif chart_type == chart_enum.PIE.value:

        return \
            pie_chart_dict['xlabel']['text'], \
            pie_chart_dict['ylabel']['text']

    elif chart_type == chart_enum.PLOT.value:

        return \
            plot_chart_dict['xlabel']['text'], \
            plot_chart_dict['ylabel']['text']

    elif chart_type == chart_enum.SCATTER.value:

        return \
            scatterplot_chart_dict['xlabel']['text'], \
            scatterplot_chart_dict['ylabel']['text']

    elif chart_type == chart_enum.CORR_CV.value:

        return \
            corr_cv_dict['xlabel']['text'], \
            corr_cv_dict['ylabel']['text']

    elif chart_type == chart_enum.CORR_SCORES.value:

        return \
            corr_scores_dict['xlabel']['text'], \
            corr_scores_dict['ylabel']['text']

    elif chart_type == chart_enum.WINDOW_CV.value:

        return \
            window_cv_dict['xlabel']['text'], \
            window_cv_dict['ylabel']['text']

    elif chart_type == chart_enum.ROLL_CORR.value:

        return \
            roll_corr_dict['xlabel']['text'], \
            roll_corr_dict['ylabel']['text']

    elif chart_type == chart_enum.ROLL_CORR_ALL.value:

        return \
            roll_corr_all_dict['xlabel']['text'], \
            roll_corr_all_dict['ylabel']['text']

    elif chart_type == chart_enum.LAG_CORR.value:

        return \
            lag_corr_dict['xlabel']['text'], \
            lag_corr_dict['ylabel']['text']

    elif chart_type == chart_enum.LAG_HEAT.value:

        return \
            lag_heat_dict['xlabel']['text'], \
            lag_heat_dict['ylabel']['text']

    else: return None, None


# In[38]:


#*******************************************************************************************
 #
 #  Function Name:  get_xylabels_display
 #
 #  Function Description:
 #      The function retrieves the chart's x-axis label display and y-axis label display.
 #
 #
 #  Return Type: boolean, boolean
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  enum           chart_type       The parameter is the chart type enumeration value.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_xylabels_display(chart_type):

    if chart_type == chart_enum.BAR.value:

        return \
            bar_chart_dict['xlabel']['display'], \
            bar_chart_dict['ylabel']['display']

    elif chart_type == chart_enum.BOXPLOT.value:

        return \
            boxplot_chart_dict['xlabel']['display'], \
            boxplot_chart_dict['ylabel']['display']

    elif chart_type == chart_enum.HISTOGRAM.value:

        return \
            histogram_chart_dict['xlabel']['display'], \
            histogram_chart_dict['ylabel']['display']

    elif chart_type == chart_enum.LINE.value:

        return \
            line_chart_dict['xlabel']['display'], \
            line_chart_dict['ylabel']['display']

    elif chart_type == chart_enum.PIE.value:

        return \
            pie_chart_dict['xlabel']['display'], \
            pie_chart_dict['ylabel']['display']

    elif chart_type == chart_enum.PLOT.value:

        return \
            plot_chart_dict['xlabel']['display'], \
            plot_chart_dict['ylabel']['display']

    elif chart_type == chart_enum.SCATTER.value:

        return \
            scatterplot_chart_dict['xlabel']['display'], \
            scatterplot_chart_dict['ylabel']['display']

    elif chart_type == chart_enum.CORR_CV.value:

        return \
            corr_cv_dict['xlabel']['display'], \
            corr_cv_dict['ylabel']['display']

    elif chart_type == chart_enum.CORR_SCORES.value:

        return \
            corr_scores_dict['xlabel']['display'], \
            corr_scores_dict['ylabel']['display']

    elif chart_type == chart_enum.WINDOW_CV.value:

        return \
            window_cv_dict['xlabel']['display'], \
            window_cv_dict['ylabel']['display']

    elif chart_type == chart_enum.ROLL_CORR.value:

        return \
            roll_corr_dict['xlabel']['display'], \
            roll_corr_dict['ylabel']['display']

    elif chart_type == chart_enum.ROLL_CORR_ALL.value:

        return \
            roll_corr_all_dict['xlabel']['display'], \
            roll_corr_all_dict['ylabel']['display']

    elif chart_type == chart_enum.LAG_CORR.value:

        return \
            lag_corr_dict['xlabel']['display'], \
            lag_corr_dict['ylabel']['display']

    elif chart_type == chart_enum.LAG_HEAT.value:

        return \
            lag_heat_dict['xlabel']['display'], \
            lag_heat_dict['ylabel']['display']

    else: return None, None


# In[39]:


#*******************************************************************************************
 #
 #  Function Name:  get_xylabels_fontsize
 #
 #  Function Description:
 #      The function retrieves the chart's x and y axes labels fontsizes.
 #
 #
 #  Return Type: float, float
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  enum           chart_type       The parameter is the chart type enumeration value.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_xylabels_fontsize(chart_type):

    if chart_type == chart_enum.BAR.value: 

        return \
            bar_chart_dict['xlabel']['fontsize'], \
            bar_chart_dict['ylabel']['fontsize']

    elif chart_type == chart_enum.BOXPLOT.value: 

        return \
            boxplot_chart_dict['xlabel']['fontsize'], \
            boxplot_chart_dict['ylabel']['fontsize']

    elif chart_type == chart_enum.HISTOGRAM.value: 

        return \
            histogram_chart_dict['xlabel']['fontsize'], \
            histogram_chart_dict['ylabel']['fontsize']

    elif chart_type == chart_enum.LINE.value: 

        return \
            line_chart_dict['xlabel']['fontsize'], \
            line_chart_dict['ylabel']['fontsize']

    elif chart_type == chart_enum.PIE.value: \

        return \
            pie_chart_dict['xlabel']['fontsize'], \
            pie_chart_dict['ylabel']['fontsize']

    elif chart_type == chart_enum.PLOT.value: 

        return \
            plot_chart_dict['xlabel']['fontsize'], \
            plot_chart_dict['ylabel']['fontsize']

    elif chart_type == chart_enum.SCATTER.value: 

        return \
            scatterplot_chart_dict['xlabel']['fontsize'], \
            scatterplot_chart_dict['ylabel']['fontsize']

    elif chart_type == chart_enum.CORR_CV.value: 

        return \
            corr_cv_dict['xlabel']['fontsize'], \
            corr_cv_dict['ylabel']['fontsize']

    elif chart_type == chart_enum.CORR_SCORES.value: 

        return \
            corr_scores_dict['xlabel']['fontsize'], \
            corr_scores_dict['ylabel']['fontsize']

    elif chart_type == chart_enum.WINDOW_CV.value: 

        return \
            window_cv_dict['xlabel']['fontsize'], \
            window_cv_dict['ylabel']['fontsize']

    elif chart_type == chart_enum.ROLL_CORR.value: 

        return \
            roll_corr_dict['xlabel']['fontsize'], \
            roll_corr_dict['ylabel']['fontsize']

    elif chart_type == chart_enum.ROLL_CORR_ALL.value: 

        return \
            roll_corr_all_dict['xlabel']['fontsize'], \
            roll_corr_all_dict['ylabel']['fontsize']

    elif chart_type == chart_enum.LAG_CORR.value: 

        return \
            lag_corr_dict['xlabel']['fontsize'], \
            lag_corr_dict['ylabel']['fontsize']

    elif chart_type == chart_enum.LAG_HEAT.value: 

        return \
            lag_heat_dict['xlabel']['fontsize'], \
            lag_heat_dict['ylabel']['fontsize']

    else: return None


# In[40]:


#*******************************************************************************************
 #
 #  Function Name:  get_xylabels_pad
 #
 #  Function Description:
 #      The function retrieves the chart's x and y axes labels pads.
 #
 #
 #  Return Type: float, float
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  enum           chart_type       The parameter is the chart type enumeration value.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_xylabels_pad(chart_type):

    if chart_type == chart_enum.BAR.value: 

        return \
            bar_chart_dict['xlabel']['pad'], \
            bar_chart_dict['ylabel']['pad']

    elif chart_type == chart_enum.BOXPLOT.value: 

        return \
            boxplot_chart_dict['xlabel']['pad'], \
            boxplot_chart_dict['ylabel']['pad']

    elif chart_type == chart_enum.HISTOGRAM.value: 

        return \
            histogram_chart_dict['xlabel']['pad'], \
            histogram_chart_dict['ylabel']['pad']

    elif chart_type == chart_enum.LINE.value: 

        return \
            line_chart_dict['xlabel']['pad'], \
            line_chart_dict['ylabel']['pad']

    elif chart_type == chart_enum.PIE.value: 

        return \
            pie_chart_dict['xlabel']['pad'], \
            pie_chart_dict['ylabel']['pad']

    elif chart_type == chart_enum.PLOT.value: \

        return \
            plot_chart_dict['xlabel']['pad'], \
            plot_chart_dict['ylabel']['pad']

    elif chart_type == chart_enum.SCATTER.value: 

        return \
            scatterplot_chart_dict['xlabel']['pad'], \
            scatterplot_chart_dict['ylabel']['pad']

    elif chart_type == chart_enum.CORR_CV.value: 

        return \
            corr_cv_dict['xlabel']['pad'], \
            corr_cv_dict['ylabel']['pad']

    elif chart_type == chart_enum.CORR_SCORES.value: 

        return \
            corr_scores_dict['xlabel']['pad'], \
            corr_scores_dict['ylabel']['pad']

    elif chart_type == chart_enum.WINDOW_CV.value: 

        return \
            window_cv_dict['xlabel']['pad'], \
            window_cv_dict['ylabel']['pad']

    elif chart_type == chart_enum.ROLL_CORR.value: 

        return \
            roll_corr_dict['xlabel']['pad'], \
            roll_corr_dict['ylabel']['pad']

    elif chart_type == chart_enum.ROLL_CORR_ALL.value: 

        return \
            roll_corr_all_dict['xlabel']['pad'], \
            roll_corr_all_dict['ylabel']['pad']

    elif chart_type == chart_enum.LAG_CORR.value: 

        return \
            lag_corr_dict['xlabel']['pad'], \
            lag_corr_dict['ylabel']['pad']

    elif chart_type == chart_enum.LAG_HEAT.value: 

        return \
            lag_heat_dict['xlabel']['pad'], \
            lag_heat_dict['ylabel']['pad']

    else: return None, None


# In[41]:


#*******************************************************************************************
 #
 #  Function Name:  get_xyticks_fontsize
 #
 #  Function Description:
 #      The function retrieves the chart's x and y ticks labels font size.
 #
 #
 #  Return Type: float, float
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  enum           chart_type       The parameter is the chart type enumeration value.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_xyticks_fontsize(chart_type):

    if chart_type == chart_enum.BAR.value: 

        return \
            bar_chart_dict['xticks']['fontsize'], \
            bar_chart_dict['yticks']['fontsize']

    elif chart_type == chart_enum.BOXPLOT.value: 

        return \
            boxplot_chart_dict['xticks']['fontsize'], \
            boxplot_chart_dict['yticks']['fontsize']

    elif chart_type == chart_enum.HISTOGRAM.value: 

        return \
            histogram_chart_dict['xticks']['fontsize'], \
            histogram_chart_dict['yticks']['fontsize']

    elif chart_type == chart_enum.LINE.value: 

        return \
            line_chart_dict['xticks']['fontsize'], \
            line_chart_dict['yticks']['fontsize']

    elif chart_type == chart_enum.PIE.value: 

        return \
            pie_chart_dict['xticks']['fontsize'], \
            pie_chart_dict['yticks']['fontsize']

    elif chart_type == chart_enum.PLOT.value: \

        return \
            plot_chart_dict['xticks']['fontsize'], \
            plot_chart_dict['yticks']['fontsize']

    elif chart_type == chart_enum.SCATTER.value: 

        return \
            scatterplot_chart_dict['xticks']['fontsize'], \
            scatterplot_chart_dict['yticks']['fontsize']

    elif chart_type == chart_enum.CORR_CV.value: 

        return \
            corr_cv_dict['xticks']['fontsize'], \
            corr_cv_dict['yticks']['fontsize']

    elif chart_type == chart_enum.CORR_SCORES.value: 

        return \
            corr_scores_dict['xticks']['fontsize'], \
            corr_scores_dict['yticks']['fontsize']

    elif chart_type == chart_enum.WINDOW_CV.value: 

        return \
            window_cv_dict['xticks']['fontsize'], \
            window_cv_dict['yticks']['fontsize']

    elif chart_type == chart_enum.ROLL_CORR.value: 

        return \
            roll_corr_dict['xticks']['fontsize'], \
            roll_corr_dict['yticks']['fontsize']

    elif chart_type == chart_enum.ROLL_CORR_ALL.value: 

        return \
            roll_corr_all_dict['xticks']['fontsize'], \
            roll_corr_all_dict['yticks']['fontsize']

    elif chart_type == chart_enum.LAG_CORR.value: 

        return \
            lag_corr_dict['xticks']['fontsize'], \
            lag_corr_dict['yticks']['fontsize']

    elif chart_type == chart_enum.LAG_HEAT.value: 

        return \
            lag_heat_dict['xticks']['fontsize'], \
            lag_heat_dict['yticks']['fontsize']

    else: return None, None


# In[42]:


#*******************************************************************************************
 #
 #  Function Name:  get_xyticks_rotation
 #
 #  Function Description:
 #      The function retrieves the chart's x and y ticks labels rotation angles.
 #
 #
 #  Return Type: float, float
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  enum           chart_type       The parameter is the chart type enumeration value.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_xyticks_rotation(chart_type):

    if chart_type == chart_enum.BAR.value: 

        return \
            bar_chart_dict['xticks']['rotation'], \
            bar_chart_dict['yticks']['rotation']

    elif chart_type == chart_enum.BOXPLOT.value: 

        return \
            boxplot_chart_dict['xticks']['rotation'], \
            boxplot_chart_dict['yticks']['rotation']

    elif chart_type == chart_enum.HISTOGRAM.value: 

        return \
            histogram_chart_dict['xticks']['rotation'], \
            histogram_chart_dict['yticks']['rotation']

    elif chart_type == chart_enum.LINE.value: 

        return \
            line_chart_dict['xticks']['rotation'], \
            line_chart_dict['yticks']['rotation']

    elif chart_type == chart_enum.PIE.value: 

        return \
            pie_chart_dict['xticks']['rotation'], \
            pie_chart_dict['yticks']['rotation']

    elif chart_type == chart_enum.PLOT.value: \

        return \
            plot_chart_dict['xticks']['rotation'], \
            plot_chart_dict['yticks']['rotation']

    elif chart_type == chart_enum.SCATTER.value: 

        return \
            scatterplot_chart_dict['xticks']['rotation'], \
            scatterplot_chart_dict['yticks']['rotation']

    elif chart_type == chart_enum.CORR_CV.value: 

        return \
            corr_cv_dict['xticks']['rotation'], \
            corr_cv_dict['yticks']['rotation']

    elif chart_type == chart_enum.CORR_SCORES.value: 

        return \
            corr_scores_dict['xticks']['rotation'], \
            corr_scores_dict['yticks']['rotation']

    elif chart_type == chart_enum.WINDOW_CV.value: 

        return \
            window_cv_dict['xticks']['rotation'], \
            window_cv_dict['yticks']['rotation']

    elif chart_type == chart_enum.ROLL_CORR.value: 

        return \
            roll_corr_dict['xticks']['rotation'], \
            roll_corr_dict['yticks']['rotation']

    elif chart_type == chart_enum.ROLL_CORR_ALL.value: 

        return \
            roll_corr_all_dict['xticks']['rotation'], \
            roll_corr_all_dict['yticks']['rotation']

    elif chart_type == chart_enum.LAG_CORR.value: 

        return \
            lag_corr_dict['xticks']['rotation'], \
            lag_corr_dict['yticks']['rotation']

    elif chart_type == chart_enum.LAG_HEAT.value: 

        return \
            lag_heat_dict['xticks']['fontsize'], \
            lag_heat_dict['yticks']['fontsize']

    else: return None, None


# In[43]:


#*******************************************************************************************
 #
 #  Function Name:  get_chart_colors
 #
 #  Function Description:
 #      The function retrieves the chart colors.
 #
 #
 #  Return Type: string or list
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  enum           chart_type       The parameter is the chart type enumeration value.
 #  string         cat              The parameter is the color category.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_chart_colors(chart_type, cat = ''):

    if chart_type == chart_enum.BAR.value: return bar_chart_dict['params']['color']

    elif chart_type == chart_enum.HISTOGRAM.value: return histogram_chart_dict['params']['color']

    elif chart_type == chart_enum.LINE.value: return line_chart_dict[cat]['color']

    elif chart_type == chart_enum.PIE.value: return pie_chart_dict['params']['colors']

    elif chart_type == chart_enum.PLOT.value: return plot_chart_dict[cat]['color']

    elif chart_type == chart_enum.SCATTER.value: return scatterplot_chart_dict['marker']['color']

    elif chart_type == chart_enum.CORR_CV.value: return corr_cv_dict[cat]['color']

    elif chart_type == chart_enum.CORR_SCORES.value: return corr_scores_dict[cat]['color']

    elif chart_type == chart_enum.WINDOW_CV.value: return window_cv_dict[cat]['color']

    elif chart_type == chart_enum.ROLL_CORR.value: return roll_corr_dict[cat]['color']

    elif chart_type == chart_enum.ROLL_CORR_ALL.value: return roll_corr_all_dict[cat]['color']

    elif chart_type == chart_enum.LAG_CORR.value: return [lag_corr_dict[cat]['upr_clr'], lag_corr_dict[cat]['lwr_clr']]

    elif chart_type == chart_enum.LAG_HEAT.value: return lag_heat_dict[cat]['color']

    else: return None


# In[44]:


#*******************************************************************************************
 #
 #  Function Name:  get_legend_display
 #
 #  Function Description:
 #      The function retrieves the chart legend display indicator.
 #
 #
 #  Return Type: boolean
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  enum           chart_type       The parameter is the chart type enumeration value.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_legend_display():

    if chart_type == chart_enum.BAR.value: return bar_chart_dict['legend']['display']

    elif chart_type == chart_enum.HISTOGRAM.value: return histogram_chart_dict['legend']['display']

    elif chart_type == chart_enum.LINE.value: return line_chart_dict['legend']['display']

    elif chart_type == chart_enum.PIE.value: return pie_chart_dict['legend']['display']

    elif chart_type == chart_enum.PLOT.value: return plot_chart_dict['legend']['display']

    elif chart_type == chart_enum.CORR_CV.value: return corr_cv_dict['legend']['display']

    elif chart_type == chart_enum.CORR_SCORES.value: return corr_scores_dict['legend']['display']

    elif chart_type == chart_enum.WINDOW_CV.value: return window_cv_dict['legend']['display']

    elif chart_type == chart_enum.ROLL_CORR.value: return roll_corr_dict['legend']['display']

    elif chart_type == chart_enum.ROLL_CORR_ALL.value: return roll_corr_all_dict['legend']['display']

    elif chart_type == chart_enum.LAG_CORR.value: return lag_corr_dict['legend']['display']

    elif chart_type == chart_enum.LAG_HEAT.value: return lag_heat_dict['legend']['display']

    else: return None


# In[45]:


#*******************************************************************************************
 #
 #  Function Name:  get_legend_fontsize
 #
 #  Function Description:
 #      The function retrieves the chart legend font size.
 #
 #
 #  Return Type: boolean
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  enum           chart_type       The parameter is the chart type enumeration value.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_legend_fontsize():

    if chart_type == chart_enum.BAR.value: return bar_chart_dict['legend']['fontsize']

    elif chart_type == chart_enum.HISTOGRAM.value: return histogram_chart_dict['legend']['fontsize']

    elif chart_type == chart_enum.LINE.value: return line_chart_dict['legend']['fontsize']

    elif chart_type == chart_enum.PIE.value: return pie_chart_dict['legend']['fontsize']

    elif chart_type == chart_enum.PLOT.value: return plot_chart_dict['legend']['fontsize']

    elif chart_type == chart_enum.CORR_CV.value: return corr_cv_dict['legend']['fontsize']

    elif chart_type == chart_enum.CORR_SCORES.value: return corr_scores_dict['legend']['fontsize']

    elif chart_type == chart_enum.WINDOW_CV.value: return window_cv_dict['legend']['fontsize']

    elif chart_type == chart_enum.ROLL_CORR.value: return roll_corr_dict['legend']['fontsize']

    elif chart_type == chart_enum.ROLL_CORR_ALL.value: return roll_corr_all_dict['legend']['fontsize']

    elif chart_type == chart_enum.LAG_CORR.value: return lag_corr_dict['legend']['fontsize']

    elif chart_type == chart_enum.LAG_HEAT.value: return lag_heat_dict['legend']['fontsize']

    else: return None


# In[46]:


#*******************************************************************************************
 #
 #  Function Name:  get_legend_bbox_to_anchor
 #
 #  Function Description:
 #      The function retrieves the chart legend bbox to anchor.
 #
 #
 #  Return Type: string or list
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  enum           chart_type       The parameter is the chart type enumeration value.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_legend_bbox_to_anchor(chart_type):

    if chart_type == chart_enum.BAR.value: return bar_chart_dict['legend']['bbox_to_anchor']

    elif chart_type == chart_enum.HISTOGRAM.value: return histogram_chart_dict['legend']['bbox_to_anchor']

    elif chart_type == chart_enum.LINE.value: return line_chart_dict['legend']['bbox_to_anchor']

    elif chart_type == chart_enum.PIE.value: return pie_chart_dict['legend']['bbox_to_anchor']

    elif chart_type == chart_enum.PLOT.value: return plot_chart_dict['legend']['bbox_to_anchor']

    elif chart_type == chart_enum.CORR_CV.value: return corr_cv_dict['legend']['bbox_to_anchor']

    elif chart_type == chart_enum.CORR_SCORES.value: return corr_scores_dict['legend']['bbox_to_anchor']

    elif chart_type == chart_enum.WINDOW_CV.value: return window_cv_dict['legend']['bbox_to_anchor']

    elif chart_type == chart_enum.ROLL_CORR.value: return roll_corr_dict['legend']['bbox_to_anchor']

    elif chart_type == chart_enum.ROLL_CORR_ALL.value: return roll_corr_all_dict['legend']['bbox_to_anchor']

    elif chart_type == chart_enum.LAG_CORR.value: return lag_corr_dict['legend']['bbox_to_anchor']

    elif chart_type == chart_enum.LAG_HEAT.value: return lag_heat_dict['legend']['bbox_to_anchor']

    else: return None


# In[47]:


#*******************************************************************************************
 #
 #  Function Name:  get_multichart_fig_dims
 #
 #  Function Description:
 #      The function retrieves the multichart's figure dimensions (width, length).
 #
 #
 #  Return Type: float, float
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  enum           chart_type       The parameter is the multichart type enumeration value.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_multichart_fig_dims(chart_type):

    if chart_type == chart_enum.MULTIBAR.value: 

        return \
            bar_multichart_dict['figure']['width'], \
            bar_multichart_dict['figure']['length']

    elif chart_type == chart_enum.MULTIBOXPLOT.value: 

        return \
            boxplot_multichart_dict['figure']['width'], \
            boxplot_multichart_dict['figure']['length']

    elif chart_type == chart_enum.MULTIHISTOGRAM.value: 

        return \
            histogram_multichart_dict['figure']['width'], \
            histogram_multichart_dict['figure']['length']

    elif chart_type == chart_enum.MULTILINE.value: 

        return \
            line_multichart_dict['figure']['width'], \
            line_multichart_dict['figure']['length']

    elif chart_type == chart_enum.MULTIPIE.value: 

        return \
            pie_multichart_dict['figure']['width'], \
            pie_multichart_dict['figure']['length']

    elif chart_type == chart_enum.MULTIPLOT.value: 

        return \
            plot_multichart_dict['figure']['width'], \
            plot_multichart_dict['figure']['length']

    elif chart_type == chart_enum.MULTISCATTER.value: 

        return \
            scatterplot_multichart_dict['figure']['width'], \
            scatterplot_multichart_dict['figure']['length']

    else: return None


# In[48]:


#*******************************************************************************************
 #
 #  Function Name:  get_multichart_fig_spaces
 #
 #  Function Description:
 #      The function retrieves the multichart's figure spaces (wspace, hspace).
 #
 #
 #  Return Type: float, float
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  enum           chart_type       The parameter is the multichart type enumeration value.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_multichart_fig_spaces(chart_type):

    if chart_type == chart_enum.MULTIBAR.value: 

        return \
            bar_multichart_dict['figure']['wspace'], \
            bar_multichart_dict['figure']['hspace']

    elif chart_type == chart_enum.MULTIBOXPLOT.value: 

        return \
            boxplot_multichart_dict['figure']['wspace'], \
            boxplot_multichart_dict['figure']['hspace']

    elif chart_type == chart_enum.MULTIHISTOGRAM.value: 

        return \
            histogram_multichart_dict['figure']['wspace'], \
            histogram_multichart_dict['figure']['hspace']

    elif chart_type == chart_enum.MULTILINE.value: 

        return \
            line_multichart_dict['figure']['wspace'], \
            line_multichart_dict['figure']['hspace']

    elif chart_type == chart_enum.MULTIPIE.value: 

        return \
            pie_multichart_dict['figure']['wspace'], \
            pie_multichart_dict['figure']['hspace']

    elif chart_type == chart_enum.MULTIPLOT.value: 

        return \
            plot_multichart_dict['figure']['wspace'], \
            plot_multichart_dict['figure']['hspace']

    elif chart_type == chart_enum.MULTISCATTER.value: 

        return \
            scatterplot_multichart_dict['figure']['wspace'], \
            scatterplot_multichart_dict['figure']['hspace']

    else: return None 


# In[49]:


#*******************************************************************************************
 #
 #  Function Name:  get_multichart_stacked
 #
 #  Function Description:
 #      The function retrieves the multichart's stacked boolean value.
 #
 #
 #  Return Type: boolean
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  enum           chart_type       The parameter is the multichart type enumeration value.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_multichart_stacked(chart_type):

    if chart_type == chart_enum.MULTIBAR.value: return bar_multichart_dict['figure']['stacked']

    elif chart_type == chart_enum.MULTIBOXPLOT.value: return boxplot_multichart_dict['figure']['stacked']

    elif chart_type == chart_enum.MULTIHISTOGRAM.value: return histogram_multichart_dict['figure']['stacked']

    elif chart_type == chart_enum.MULTILINE.value: return line_multichart_dict['figure']['stacked']

    elif chart_type == chart_enum.MULTIPIE.value: return pie_multichart_dict['figure']['stacked']

    elif chart_type == chart_enum.MULTIPLOT.value: return plot_multichart_dict['figure']['stacked']

    elif chart_type == chart_enum.MULTISCATTER.value: return scatterplot_multichart_dict['figure']['stacked']

    else: return None


# In[50]:


#*******************************************************************************************
 #
 #  Function Name:  get_multichart_xysuplabels
 #
 #  Function Description:
 #      The function retrieves the multichart's x-axis suplabel and y-axis suplabel.
 #
 #
 #  Return Type: string, string
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  enum           chart_type       The parameter is the multichart type enumeration value.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_multichart_xysuplabels(chart_type):

    if chart_type == chart_enum.MULTIBAR.value:

        return \
            bar_multichart_dict['supxlabel']['text'], \
            bar_multichart_dict['supylabel']['text']

    elif chart_type == chart_enum.MULTIBOXPLOT.value:

        return \
            boxplot_multichart_dict['supxlabel']['text'], \
            boxplot_multichart_dict['supylabel']['text']

    elif chart_type == chart_enum.MULTIHISTOGRAM.value:

        return \
            histogram_multichart_dict['supxlabel']['text'], \
            histogram_multichart_dict['supylabel']['text']

    elif chart_type == chart_enum.MULTILINE.value:

        return \
            line_multichart_dict['supxlabel']['text'], \
            line_multichart_dict['supylabel']['text']

    elif chart_type == chart_enum.MULTIPIE.value:

        return \
            pie_multichart_dict['supxlabel']['text'], \
            pie_multichart_dict['supylabel']['text']

    elif chart_type == chart_enum.MULTIPLOT.value:

        return \
            plot_multichart_dict['supxlabel']['text'], \
            plot_multichart_dict['supylabel']['text']

    elif chart_type == chart_enum.MULTISCATTER.value:

        return \
            scatterplot_multichart_dict['supxlabel']['text'], \
            scatterplot_multichart_dict['supylabel']['text']

    else: return None, None


# In[51]:


#*******************************************************************************************
 #
 #  Function Name:  get_multichart_suptitle_xycoords
 #
 #  Function Description:
 #      The function retrieves the multichart suptitle x and y coordinates.
 #
 #
 #  Return Type: float, float
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  enum           chart_type       The parameter is the multichart type enumeration value.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_multichart_suptitle_xycoords(chart_type):

    if chart_type == chart_enum.MULTIBAR.value:

        return \
            bar_multichart_dict['suptitle']['x'], \
            bar_multichart_dict['suptitle']['y']

    elif chart_type == chart_enum.MULTIBOXPLOT.value:

        return \
            boxplot_multichart_dict['suptitle']['x'], \
            boxplot_multichart_dict['suptitle']['y']

    elif chart_type == chart_enum.MULTIHISTOGRAM.value:

        return \
            histogram_multichart_dict['suptitle']['x'], \
            histogram_multichart_dict['suptitle']['y']

    elif chart_type == chart_enum.MULTILINE.value:

        return \
            line_multichart_dict['suptitle']['x'], \
            line_multichart_dict['suptitle']['y']

    elif chart_type == chart_enum.MULTIPIE.value:

        return \
            pie_multichart_dict['suptitle']['x'], \
            pie_multichart_dict['suptitle']['y']

    elif chart_type == chart_enum.MULTIPLOT.value:

        return \
            plot_multichart_dict['suptitle']['x'], \
            plot_multichart_dict['suptitle']['y']

    elif chart_type == chart_enum.MULTISCATTER.value:

        return \
            scatterplot_multichart_dict['suptitle']['x'], \
            scatterplot_multichart_dict['suptitle']['y']

    else: return None, None


# In[52]:


#*******************************************************************************************
 #
 #  Function Name:  get_multichart_supxlabel_xycoords
 #
 #  Function Description:
 #      The function retrieves the multichart supxlabel x and y coordinates.
 #
 #
 #  Return Type: float, float
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  enum           chart_type       The parameter is the multichart type enumeration value.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_multichart_supxlabel_xycoords(chart_type):

    if chart_type == chart_enum.MULTIBAR.value:

        return \
            bar_multichart_dict['supxlabel']['x'], \
            bar_multichart_dict['supxlabel']['y']

    elif chart_type == chart_enum.MULTIBOXPLOT.value:

        return \
            boxplot_multichart_dict['supxlabel']['x'], \
            boxplot_multichart_dict['supxlabel']['y']

    elif chart_type == chart_enum.MULTIHISTOGRAM.value:

        return \
            histogram_multichart_dict['supxlabel']['x'], \
            histogram_multichart_dict['supxlabel']['y']

    elif chart_type == chart_enum.MULTILINE.value:

        return \
            line_multichart_dict['supxlabel']['x'], \
            line_multichart_dict['supxlabel']['y']

    elif chart_type == chart_enum.MULTIPIE.value:

        return \
            pie_multichart_dict['supxlabel']['x'], \
            pie_multichart_dict['supxlabel']['y']

    elif chart_type == chart_enum.MULTIPLOT.value:

        return \
            plot_multichart_dict['supxlabel']['x'], \
            plot_multichart_dict['supxlabel']['y']

    elif chart_type == chart_enum.MULTISCATTER.value:

        return \
            scatterplot_multichart_dict['supxlabel']['x'], \
            scatterplot_multichart_dict['supxlabel']['y']

    else: return None, None


# In[53]:


#*******************************************************************************************
 #
 #  Function Name:  get_multichart_supylabel_xycoords
 #
 #  Function Description:
 #      The function retrieves the multichart supylabel x and y coordinates.
 #
 #
 #  Return Type: float, float
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  enum           chart_type       The parameter is the multichart type enumeration value.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_multichart_supylabel_xycoords(chart_type):

    if chart_type == chart_enum.MULTIBAR.value:

        return \
            bar_multichart_dict['supylabel']['x'], \
            bar_multichart_dict['supylabel']['y']

    elif chart_type == chart_enum.MULTIBOXPLOT.value:

        return \
            boxplot_multichart_dict['supylabel']['x'], \
            boxplot_multichart_dict['supylabel']['y']

    elif chart_type == chart_enum.MULTIHISTOGRAM.value:

        return \
            histogram_multichart_dict['supylabel']['x'], \
            histogram_multichart_dict['supylabel']['y']

    elif chart_type == chart_enum.MULTILINE.value:

        return \
            line_multichart_dict['supylabel']['x'], \
            line_multichart_dict['supylabel']['y']

    elif chart_type == chart_enum.MULTIPIE.value:

        return \
            pie_multichart_dict['supylabel']['x'], \
            pie_multichart_dict['supylabel']['y']

    elif chart_type == chart_enum.MULTIPLOT.value:

        return \
            plot_multichart_dict['supylabel']['x'], \
            plot_multichart_dict['supylabel']['y']

    elif chart_type == chart_enum.MULTISCATTER.value:

        return \
            scatterplot_multichart_dict['supylabel']['x'], \
            scatterplot_multichart_dict['supylabel']['y']

    else: return None, None


# In[54]:


#*******************************************************************************************
 #
 #  Function Name:  get_multichart_suptitle_fontsize
 #
 #  Function Description:
 #      The function retrieves the multichart suptitle font size.
 #
 #
 #  Return Type: float, float
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  enum           chart_type       The parameter is the multichart type enumeration value.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_multichart_suptitle_fontsize(chart_type):

    if chart_type == chart_enum.MULTIBAR.value:

        return bar_multichart_dict['suptitle']['fontproperties']['size']

    elif chart_type == chart_enum.MULTIBOXPLOT.value:

        return boxplot_multichart_dict['suptitle']['fontproperties']['size']

    elif chart_type == chart_enum.MULTIHISTOGRAM.value:

        return histogram_multichart_dict['suptitle']['fontproperties']['size']

    elif chart_type == chart_enum.MULTILINE.value:

        return line_multichart_dict['suptitle']['fontproperties']['size']

    elif chart_type == chart_enum.MULTIPIE.value:

        return pie_multichart_dict['suptitle']['fontproperties']['size']

    elif chart_type == chart_enum.MULTIPLOT.value:

        return plot_multichart_dict['suptitle']['fontproperties']['size']

    elif chart_type == chart_enum.MULTISCATTER.value:

        return scatterplot_multichart_dict['suptitle']['fontproperties']['size']

    else: return None, None


# In[55]:


#*******************************************************************************************
 #
 #  Function Name:  get_multichart_supxlabel_fontsize
 #
 #  Function Description:
 #      The function retrieves the multichart supxlabel font size.
 #
 #
 #  Return Type: float, float
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  enum           chart_type       The parameter is the multichart type enumeration value.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_multichart_supxlabel_fontsize(chart_type):

    if chart_type == chart_enum.MULTIBAR.value:

        return bar_multichart_dict['supxlabel']['fontproperties']['size']

    elif chart_type == chart_enum.MULTIBOXPLOT.value:

        return boxplot_multichart_dict['supxlabel']['fontproperties']['size']

    elif chart_type == chart_enum.MULTIHISTOGRAM.value:

        return histogram_multichart_dict['supxlabel']['fontproperties']['size']

    elif chart_type == chart_enum.MULTILINE.value:

        return line_multichart_dict['supxlabel']['fontproperties']['size']

    elif chart_type == chart_enum.MULTIPIE.value:

        return pie_multichart_dict['supxlabel']['fontproperties']['size']

    elif chart_type == chart_enum.MULTIPLOT.value:

        return plot_multichart_dict['supxlabel']['fontproperties']['size']

    elif chart_type == chart_enum.MULTISCATTER.value:

        return scatterplot_multichart_dict['supxlabel']['fontproperties']['size']

    else: return None, None


# In[56]:


#*******************************************************************************************
 #
 #  Function Name:  get_multichart_supylabel_fontsize
 #
 #  Function Description:
 #      The function retrieves the multichart supylabel font size.
 #
 #
 #  Return Type: float, float
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  enum           chart_type       The parameter is the multichart type enumeration value.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_multichart_supylabel_fontsize(chart_type):

    if chart_type == chart_enum.MULTIBAR.value:

        return bar_multichart_dict['supylabel']['fontproperties']['size']

    elif chart_type == chart_enum.MULTIBOXPLOT.value:

        return boxplot_multichart_dict['supylabel']['fontproperties']['size']

    elif chart_type == chart_enum.MULTIHISTOGRAM.value:

        return histogram_multichart_dict['supylabel']['fontproperties']['size']

    elif chart_type == chart_enum.MULTILINE.value:

        return line_multichart_dict['supylabel']['fontproperties']['size']

    elif chart_type == chart_enum.MULTIPIE.value:

        return pie_multichart_dict['supylabel']['fontproperties']['size']

    elif chart_type == chart_enum.MULTIPLOT.value:

        return plot_multichart_dict['supylabel']['fontproperties']['size']

    elif chart_type == chart_enum.MULTISCATTER.value:

        return scatterplot_multichart_dict['supylabel']['fontproperties']['size']

    else: return None, None


# In[57]:


#*******************************************************************************************
 #
 #  Function Name:  set_chart_dict
 #
 #  Function Description:
 #      The function sets the global chart dictionary.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  dictionary     upd_dict         The parameter is the updated bar chart dictionary.
 #  int            chart_type       The parameter is the chart type enumeration value.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_chart_dict(upd_dict, chart_type):

    if chart_type == chart_enum.BAR.value: 

        global bar_chart_dict

        bar_chart_dict = copy.deepcopy(upd_dict)

    elif chart_type == chart_enum.BOXPLOT.value:

        global boxplot_chart_dict

        boxplot_chart_dict = copy.deepcopy(upd_dict)

    elif chart_type == chart_enum.HISTOGRAM.value:

        global histogram_chart_dict

        histogram_chart_dict = copy.deepcopy(upd_dict)

    elif chart_type == chart_enum.LINE.value:

        global line_chart_dict

        line_chart_dict = copy.deepcopy(upd_dict)

    elif chart_type == chart_enum.PIE.value:

        global pie_chart_dict

        pie_chart_dict = copy.deepcopy(upd_dict)

    elif chart_type == chart_enum.PLOT.value: 

        global plot_chart_dict

        plot_chart_dict = copy.deepcopy(upd_dict)

    elif chart_type == chart_enum.SCATTER.value:

        global scatterplot_chart_dict

        scatterplot_chart_dict = copy.deepcopy(upd_dict)

    elif chart_type == chart_enum.REGR_LINE.value:

        global regr_line_dict

        regr_line_dict = copy.deepcopy(upd_dict)

    elif chart_type == chart_enum.CORR_CV.value: 

        global corr_cv_dict

        corr_cv_dict = copy.deepcopy(upd_dict)

    elif chart_type == chart_enum.CORR_SCORES.value: 

        global corr_scores_dict

        corr_scores_dict = copy.deepcopy(upd_dict)

    elif chart_type == chart_enum.WINDOW_CV.value:

        global window_cv_dict

        window_cv_dict = copy.deepcopy(upd_dict)

    elif chart_type == chart_enum.ROLL_CORR.value:

        global roll_corr_dict

        roll_corr_dict = copy.deepcopy(upd_dict)

    elif chart_type == chart_enum.ROLL_CORR_ALL.value:

        global roll_corr_all_dict

        roll_corr_all_dict = copy.deepcopy(upd_dict)

    elif chart_type == chart_enum.LAG_CORR.value:

        global lag_corr_dict

        lag_corr_dict = copy.deepcopy(upd_dict)

    elif chart_type == chart_enum.LAG_HEAT.value:

        global lag_heat_dict

        lag_heat_dict = copy.deepcopy(upd_dict)

    elif chart_type == chart_enum.MULTIBAR.value:

        global bar_multichart_dict

        bar_multichart_dict = copy.deepcopy(upd_dict)

    elif chart_type == chart_enum.MULTIBOXPLOT.value:

        global boxplot_multichart_dict

        boxplot_multichart_dict = copy.deepcopy(upd_dict)

    elif chart_type == chart_enum.MULTIHISTOGRAM.value:

        global histogram_multichart_dict

        histogram_multichart_dict = copy.deepcopy(upd_dict)

    elif chart_type == chart_enum.MULTILINE.value:

        global line_multichart_dict

        line_multichart_dict = copy.deepcopy(upd_dict)

    elif chart_type == chart_enum.MULTIPIE.value:

        global pie_multichart_dict

        pie_multichart_dict = copy.deepcopy(upd_dict)

    elif chart_type == chart_enum.MULTIPLOT.value:

        global plot_multichart_dict

        plot_multichart_dict = copy.deepcopy(upd_dict)

    elif chart_type == chart_enum.MULTISCATTER.value:

        global scatterplot_multichart_dict

        scatterplot_multichart_dict = copy.deepcopy(upd_dict)


# In[58]:


#*******************************************************************************************
 #
 #  Function Name:  set_chart_def_dict
 #
 #  Function Description:
 #      The function sets the global chart default dictionary.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  int            chart_type       The parameter is the chart type enumeration value.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_chart_def_dict(chart_type):

    if chart_type == chart_enum.BAR.value: 

        global bar_chart_dict

        bar_chart_dict = copy.deepcopy(bar_chart_def_dict)

    elif chart_type == chart_enum.BOXPLOT.value:

        global boxplot_chart_dict

        boxplot_chart_dict = copy.deepcopy(boxplot_chart_def_dict)

    elif chart_type == chart_enum.HISTOGRAM.value:

        global histogram_chart_dict

        histogram_chart_dict = copy.deepcopy(histogram_chart_def_dict)

    elif chart_type == chart_enum.LINE.value:

        global line_chart_dict

        line_chart_dict = copy.deepcopy(line_chart_def_dict)

    elif chart_type == chart_enum.PIE.value:

        global pie_chart_dict

        pie_chart_dict = copy.deepcopy(pie_chart_def_dict)

    elif chart_type == chart_enum.PLOT.value: 

        global plot_chart_dict

        plot_chart_dict = copy.deepcopy(plot_chart_def_dict)

    elif chart_type == chart_enum.SCATTER.value:

        global scatterplot_chart_dict

        scatterplot_chart_dict = copy.deepcopy(scatterplot_chart_def_dict)

    elif chart_type == chart_enum.REGR_LINE.value:

        global regr_line_dict

        regr_line_dict = copy.deepcopy(regr_line_def_dict)

    elif chart_type == chart_enum.CORR_CV.value:

        global corr_cv_dict

        corr_cv_dict = copy.deepcopy(corr_cv_def_dict)

    elif chart_type == chart_enum.CORR_SCORES.value:

        global corr_scores_dict

        corr_scores_dict = copy.deepcopy(corr_scores_def_dict)

    elif chart_type == chart_enum.WINDOW_CV.value:

        global window_cv_dict

        window_cv_dict = copy.deepcopy(window_cv_def_dict)

    elif chart_type == chart_enum.ROLL_CORR.value:

        global roll_corr_dict

        roll_corr_dict = copy.deepcopy(roll_corr_def_dict)

    elif chart_type == chart_enum.ROLL_CORR_ALL.value:

        global roll_corr_all_dict

        roll_corr_all_dict = copy.deepcopy(roll_corr_all_def_dict)

    elif chart_type == chart_enum.LAG_CORR.value:

        global lag_corr_dict

        lag_corr_dict = copy.deepcopy(lag_corr_def_dict)

    elif chart_type == chart_enum.LAG_HEAT.value:

        global lag_heat_dict

        lag_heat_dict = copy.deepcopy(lag_heat_def_dict)

    elif chart_type == chart_enum.MULTIBAR.value:

        global bar_multichart_dict

        bar_multichart_dict = copy.deepcopy(bar_multichart_def_dict)

    elif chart_type == chart_enum.MULTIBOXPLOT.value:

        global boxplot_multichart_dict

        boxplot_multichart_dict = copy.deepcopy(boxplot_multichart_def_dict)

    elif chart_type == chart_enum.MULTIHISTOGRAM.value:

        global histogram_multichart_dict

        histogram_multichart_dict = copy.deepcopy(histogram_multichart_def_dict)

    elif chart_type == chart_enum.MULTILINE.value:

        global line_multichart_dict

        line_multichart_dict = copy.deepcopy(line_multichart_def_dict)

    elif chart_type == chart_enum.MULTIPIE.value:

        global pie_multichart_dict

        pie_multichart_dict = copy.deepcopy(pie_multichart_def_dict)

    elif chart_type == chart_enum.MULTIPLOT.value:

        global plot_multichart_dict

        plot_multichart_dict = copy.deepcopy(plot_multichart_def_dict)

    elif chart_type == chart_enum.MULTISCATTER.value:

        global scatterplot_multichart_dict

        scatterplot_multichart_dict = copy.deepcopy(scatterplot_multichart_def_dict)


# In[59]:


#*******************************************************************************************
 #
 #  Function Name:  set_title
 #
 #  Function Description:
 #      The function sets the chart's titles.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  string         titles           The parameter is the chart's titles.
 #  enum           chart_type       The parameter is the chart type enumeration value.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_title(titles, chart_type):

    if chart_type == chart_enum.BAR.value:

        global bar_chart_dict

        if isinstance(titles, np.ndarray) \
            or isinstance(titles, list) \
            or isinstance(titles, pd.Series) \
            or isinstance(titles, pd.Index):

            bar_chart_dict['title']['text'] = dtypesx.cnv_data_to_array(titles)

        else: bar_chart_dict['title']['text'] = np.array([str(titles)], dtype = str)

    elif chart_type == chart_enum.BOXPLOT.value:

        global boxplot_chart_dict

        if isinstance(titles, np.ndarray) \
            or isinstance(titles, list) \
            or isinstance(titles, pd.Series) \
            or isinstance(titles, pd.Index):

            boxplot_chart_dict['title']['text'] = dtypesx.cnv_data_to_array(titles)

        else: boxplot_chart_dict['title']['text'] = np.array([str(titles)], dtype = str)

    elif chart_type == chart_enum.HISTOGRAM.value:

        global histogram_chart_dict

        if isinstance(titles, np.ndarray) \
            or isinstance(titles, list) \
            or isinstance(titles, pd.Series) \
            or isinstance(titles, pd.Index):

            histogram_chart_dict['title']['text'] = dtypesx.cnv_data_to_array(titles)

        else: histogram_chart_dict['title']['text'] = np.array([str(titles)], dtype = str)

    elif chart_type == chart_enum.LINE.value:

        global line_chart_dict

        if isinstance(titles, np.ndarray) \
            or isinstance(titles, list) \
            or isinstance(titles, pd.Series) \
            or isinstance(titles, pd.Index):

            line_chart_dict['title']['text'] = dtypesx.cnv_data_to_array(titles)

        else: line_chart_dict['title']['text'] = np.array([str(titles)], dtype = str)

    elif chart_type == chart_enum.PIE.value:

        global pie_chart_dict

        if isinstance(titles, np.ndarray) \
            or isinstance(titles, list) \
            or isinstance(titles, pd.Series) \
            or isinstance(titles, pd.Index):

            pie_chart_dict['title']['text'] = dtypesx.cnv_data_to_array(titles)

        else: pie_chart_dict['title']['text'] = np.array([str(titles)], dtype = str)

    elif chart_type == chart_enum.PLOT.value:

        global plot_chart_dict

        if isinstance(titles, np.ndarray) \
            or isinstance(titles, list) \
            or isinstance(titles, pd.Series) \
            or isinstance(titles, pd.Index):

            plot_chart_dict['title']['text'] = dtypesx.cnv_data_to_array(titles)

        else: plot_chart_dict['title']['text'] = np.array([str(titles)], dtype = str)

    elif chart_type == chart_enum.SCATTER.value:

        global scatterplot_chart_dict

        if isinstance(titles, np.ndarray) \
            or isinstance(titles, list) \
            or isinstance(titles, pd.Series) \
            or isinstance(titles, pd.Index):

            scatterplot_chart_dict['title']['text'] = dtypesx.cnv_data_to_array(titles)

        else: scatterplot_chart_dict['title']['text'] = np.array([str(titles)], dtype = str)

    elif chart_type == chart_enum.CORR_CV.value:

        global corr_cv_dict

        if isinstance(titles, np.ndarray) \
            or isinstance(titles, list) \
            or isinstance(titles, pd.Series) \
            or isinstance(titles, pd.Index):

            corr_cv_dict['title']['text'] = dtypesx.cnv_data_to_array(titles)

        else: corr_cv_dict['title']['text'] = np.array([str(titles)], dtype = str)

    elif chart_type == chart_enum.CORR_SCORES.value:

        global corr_scores_dict

        if isinstance(titles, np.ndarray) \
            or isinstance(titles, list) \
            or isinstance(titles, pd.Series) \
            or isinstance(titles, pd.Index):

            corr_scores_dict['title']['text'] = dtypesx.cnv_data_to_array(titles)

        else: corr_scores_dict['title']['text'] = np.array([str(titles)], dtype = str)

    elif chart_type == chart_enum.WINDOW_CV.value:

        global window_cv_dict

        if isinstance(titles, np.ndarray) \
            or isinstance(titles, list) \
            or isinstance(titles, pd.Series) \
            or isinstance(titles, pd.Index):

            window_cv_dict['title']['text'] = dtypesx.cnv_data_to_array(titles)

        else: window_cv_dict['title']['text'] = np.array([str(titles)], dtype = str)

    elif chart_type == chart_enum.ROLL_CORR.value:

        global roll_corr_dict

        if isinstance(titles, np.ndarray) \
            or isinstance(titles, list) \
            or isinstance(titles, pd.Series) \
            or isinstance(titles, pd.Index):

            roll_corr_dict['title']['text'] = dtypesx.cnv_data_to_array(titles)

        else: roll_corr_dict['title']['text'] = np.array([str(titles)], dtype = str)

    elif chart_type == chart_enum.ROLL_CORR_ALL.value:

        global roll_corr_all_dict

        if isinstance(titles, np.ndarray) \
            or isinstance(titles, list) \
            or isinstance(titles, pd.Series) \
            or isinstance(titles, pd.Index):

            roll_corr_all_dict['title']['text'] = dtypesx.cnv_data_to_array(titles)

        else: roll_corr_all_dict['title']['text'] = np.array([str(titles)], dtype = str)

    elif chart_type == chart_enum.LAG_CORR.value:

        global lag_corr_dict

        if isinstance(titles, np.ndarray) \
            or isinstance(titles, list) \
            or isinstance(titles, pd.Series) \
            or isinstance(titles, pd.Index):

            lag_corr_dict['title']['text'] = dtypesx.cnv_data_to_array(titles)

        else: lag_corr_dict['title']['text'] = np.array([str(titles)], dtype = str)

    elif chart_type == chart_enum.LAG_HEAT.value:

        global lag_heat_dict

        if isinstance(titles, np.ndarray) \
            or isinstance(titles, list) \
            or isinstance(titles, pd.Series) \
            or isinstance(titles, pd.Index):

            lag_heat_dict['title']['text'] = dtypesx.cnv_data_to_array(titles)

        else: lag_heat_dict['title']['text'] = np.array([str(titles)], dtype = str)


# In[60]:


#*******************************************************************************************
 #
 #  Function Name:  set_title_display
 #
 #  Function Description:
 #      The function sets the chart's title display indicator.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  boolean        upd_bool         The parameter is the chart's title display indicator.
 #  enum           chart_type       The parameter is the chart type enumeration value.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_title_display(upd_bool, chart_type):

    if chart_type == chart_enum.BAR.value:

        global bar_chart_dict

        bar_chart_dict['title']['display'] = upd_bool

    elif chart_type == chart_enum.BOXPLOT.value:

        global boxplot_chart_dict

        boxplot_chart_dict['title']['display'] = upd_bool

    elif chart_type == chart_enum.HISTOGRAM.value:

        global histogram_chart_dict

        histogram_chart_dict['title']['display'] = upd_bool

    elif chart_type == chart_enum.LINE.value:

        global line_chart_dict

        line_chart_dict['title']['display'] = upd_bool

    elif chart_type == chart_enum.PIE.value:

        global pie_chart_dict

        pie_chart_dict['title']['display'] = upd_bool

    elif chart_type == chart_enum.PLOT.value:

        global plot_chart_dict

        plot_chart_dict['title']['display'] = upd_bool

    elif chart_type == chart_enum.SCATTER.value:

        global scatterplot_chart_dict

        scatterplot_chart_dict['title']['display'] = upd_bool

    elif chart_type == chart_enum.CORR_CV.value:

        global corr_cv_dict

        corr_cv_dict['title']['display'] = upd_bool

    elif chart_type == chart_enum.CORR_SCORES.value:

        global corr_scores_dict

        corr_scores_dict['title']['display'] = upd_bool

    elif chart_type == chart_enum.WINDOW_CV.value:

        global window_cv_dict

        window_cv_dict['title']['display'] = upd_bool

    elif chart_type == chart_enum.ROLL_CORR.value:

        global roll_corr_dict

        roll_corr_dict['title']['display'] = upd_bool

    elif chart_type == chart_enum.ROLL_CORR_ALL.value:

        global roll_corr_all_dict

        roll_corr_all_dict['title']['display'] = upd_bool

    elif chart_type == chart_enum.LAG_CORR.value:

        global lag_corr_dict

        lag_corr_dict['title']['display'] = upd_bool

    elif chart_type == chart_enum.LAG_HEAT.value:

        global lag_heat_dict

        lag_heat_dict['title']['display'] = upd_bool


# In[61]:


#*******************************************************************************************
 #
 #  Function Name:  set_title_fontsize
 #
 #  Function Description:
 #      The function sets the chart's title sizes.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  float          size_flt         The parameter is the chart's title font sizes.
 #  enum           chart_type       The parameter is the chart type enumeration value.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_title_fontsize(size_flt, chart_type):

    if chart_type == chart_enum.BAR.value:

        global bar_chart_dict

        bar_chart_dict['title']['fontsize'] = size_flt

    elif chart_type == chart_enum.BOXPLOT.value:

        global boxplot_chart_dict

        boxplot_chart_dict['title']['fontsize'] = size_flt

    elif chart_type == chart_enum.HISTOGRAM.value:

        global histogram_chart_dict

        histogram_chart_dict['title']['fontsize'] = size_flt

    elif chart_type == chart_enum.LINE.value:

        global line_chart_dict

        line_chart_dict['title']['fontsize'] = size_flt

    elif chart_type == chart_enum.PIE.value:

        global pie_chart_dict

        pie_chart_dict['title']['fontsize'] = size_flt

    elif chart_type == chart_enum.PLOT.value:

        global plot_chart_dict

        plot_chart_dict['title']['fontsize'] = size_flt

    elif chart_type == chart_enum.SCATTER.value:

        global scatterplot_chart_dict

        scatterplot_chart_dict['title']['fontsize'] = size_flt

    elif chart_type == chart_enum.CORR_CV.value:

        global corr_cv_dict

        corr_cv_dict['title']['fontsize'] = size_flt

    elif chart_type == chart_enum.CORR_SCORES.value:

        global corr_scores_dict

        corr_scores_dict['title']['fontsize'] = size_flt

    elif chart_type == chart_enum.WINDOW_CV.value:

        global window_cv_dict

        window_cv_dict['title']['fontsize'] = size_flt

    elif chart_type == chart_enum.ROLL_CORR.value:

        global roll_corr_dict

        roll_corr_dict['title']['fontsize'] = size_flt

    elif chart_type == chart_enum.ROLL_CORR_ALL.value:

        global roll_corr_all_dict

        roll_corr_all_dict['title']['fontsize'] = size_flt

    elif chart_type == chart_enum.LAG_CORR.value:

        global lag_corr_dict

        lag_corr_dict['title']['fontsize'] = size_flt

    elif chart_type == chart_enum.LAG_HEAT.value:

        global lag_heat_dict

        lag_heat_dict['title']['fontsize'] = size_flt


# In[62]:


#*******************************************************************************************
 #
 #  Function Name:  set_title_pad
 #
 #  Function Description:
 #      The function sets the chart's title pad.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  float          pad_flt          The parameter is the chart's title font sizes.
 #  enum           chart_type       The parameter is the chart type enumeration value.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_title_pad(pad_flt, chart_type):

    if chart_type == chart_enum.BAR.value:

        global bar_chart_dict

        bar_chart_dict['title']['pad'] = pad_flt

    elif chart_type == chart_enum.BOXPLOT.value:

        global boxplot_chart_dict

        boxplot_chart_dict['title']['pad'] = pad_flt

    elif chart_type == chart_enum.HISTOGRAM.value:

        global histogram_chart_dict

        histogram_chart_dict['title']['pad'] = pad_flt

    elif chart_type == chart_enum.LINE.value:

        global line_chart_dict

        line_chart_dict['title']['pad'] = pad_flt

    elif chart_type == chart_enum.PIE.value:

        global pie_chart_dict

        pie_chart_dict['title']['pad'] = pad_flt

    elif chart_type == chart_enum.PLOT.value:

        global plot_chart_dict

        plot_chart_dict['title']['pad'] = pad_flt

    elif chart_type == chart_enum.SCATTER.value:

        global scatterplot_chart_dict

        scatterplot_chart_dict['title']['pad'] = pad_flt

    elif chart_type == chart_enum.CORR_CV.value:

        global corr_cv_dict

        corr_cv_dict['title']['pad'] = pad_flt

    elif chart_type == chart_enum.CORR_SCORES.value:

        global corr_scores_dict

        corr_scores_dict['title']['pad'] = pad_flt

    elif chart_type == chart_enum.WINDOW_CV.value:

        global window_cv_dict

        window_cv_dict['title']['pad'] = pad_flt

    elif chart_type == chart_enum.ROLL_CORR.value:

        global roll_corr_dict

        roll_corr_dict['title']['pad'] = pad_flt

    elif chart_type == chart_enum.ROLL_CORR_ALL.value:

        global roll_corr_all_dict

        roll_corr_all_dict['title']['pad'] = pad_flt

    elif chart_type == chart_enum.LAG_CORR.value:

        global lag_corr_dict

        lag_corr_dict['title']['pad'] = pad_flt

    elif chart_type == chart_enum.LAG_HEAT.value:

        global lag_heat_dict

        lag_heat_dict['title']['pad'] = pad_flt


# In[63]:


#*******************************************************************************************
 #
 #  Function Name:  set_xylabels
 #
 #  Function Description:
 #      The function sets the chart's x-axis label and y-axis label.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  string         xlabel           The parameter is the chart's x-axis label.
 #  string         ylabel           The parameter is the chart's y-axis label.
 #  enum           chart_type       The parameter is the chart type enumeration value.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_xylabels(xlabel, ylabel, chart_type):

    if chart_type == chart_enum.BAR.value:

        global bar_chart_dict

        if isinstance(xlabel, np.ndarray) \
            or isinstance(xlabel, list) \
            or isinstance(xlabel, pd.Series) \
            or isinstance(xlabel, pd.Index):

            bar_chart_dict['xlabel']['text'] = dtypesx.cnv_data_to_array(xlabel)

        else: bar_chart_dict['xlabel']['text'] = np.array([str(xlabel)], dtype = str)

        if isinstance(ylabel, np.ndarray) \
            or isinstance(ylabel, list) \
            or isinstance(ylabel, pd.Series) \
            or isinstance(ylabel, pd.Index):

            bar_chart_dict['ylabel']['text'] = dtypesx.cnv_data_to_array(ylabel)

        else: bar_chart_dict['ylabel']['text'] = np.array([str(ylabel)], dtype = str)            

    elif chart_type == chart_enum.BOXPLOT.value:

        global boxplot_chart_dict

        if isinstance(xlabel, np.ndarray) \
            or isinstance(xlabel, list) \
            or isinstance(xlabel, pd.Series) \
            or isinstance(xlabel, pd.Index):

            boxplot_chart_dict['xlabel']['text'] = dtypesx.cnv_data_to_array(xlabel)

        else: boxplot_chart_dict['xlabel']['text'] = np.array([str(xlabel)], dtype = str)

        if isinstance(ylabel, np.ndarray) \
            or isinstance(ylabel, list) \
            or isinstance(ylabel, pd.Series) \
            or isinstance(ylabel, pd.Index):

            boxplot_chart_dict['ylabel']['text'] = dtypesx.cnv_data_to_array(ylabel)

        else: boxplot_chart_dict['ylabel']['text'] = np.array([str(ylabel)], dtype = str) 

    elif chart_type == chart_enum.HISTOGRAM.value:

        global histogram_chart_dict

        if isinstance(xlabel, np.ndarray) \
            or isinstance(xlabel, list) \
            or isinstance(xlabel, pd.Series) \
            or isinstance(xlabel, pd.Index):

            histogram_chart_dict['xlabel']['text'] = dtypesx.cnv_data_to_array(xlabel)

        else: histogram_chart_dict['xlabel']['text'] = np.array([str(xlabel)], dtype = str)

        if isinstance(ylabel, np.ndarray) \
            or isinstance(ylabel, list) \
            or isinstance(ylabel, pd.Series) \
            or isinstance(ylabel, pd.Index):

            histogram_chart_dict['ylabel']['text'] = dtypesx.cnv_data_to_array(ylabel)

        else: histogram_chart_dict['ylabel']['text'] = np.array([str(ylabel)], dtype = str) 

    elif chart_type == chart_enum.LINE.value:

        global line_chart_dict

        if isinstance(xlabel, np.ndarray) \
            or isinstance(xlabel, list) \
            or isinstance(xlabel, pd.Series) \
            or isinstance(xlabel, pd.Index):

            line_chart_dict['xlabel']['text'] = dtypesx.cnv_data_to_array(xlabel)

        else: line_chart_dict['xlabel']['text'] = np.array([str(xlabel)], dtype = str)

        if isinstance(ylabel, np.ndarray) \
            or isinstance(ylabel, list) \
            or isinstance(ylabel, pd.Series) \
            or isinstance(ylabel, pd.Index):

            line_chart_dict['ylabel']['text'] = dtypesx.cnv_data_to_array(ylabel)

        else: line_chart_dict['ylabel']['text'] = np.array([str(ylabel)], dtype = str) 

    elif chart_type == chart_enum.PIE.value:

        global pie_chart_dict

        if isinstance(xlabel, np.ndarray) \
            or isinstance(xlabel, list) \
            or isinstance(xlabel, pd.Series) \
            or isinstance(xlabel, pd.Index):

            pie_chart_dict['xlabel']['text'] = dtypesx.cnv_data_to_array(xlabel)

        else: pie_chart_dict['xlabel']['text'] = np.array([str(xlabel)], dtype = str)

        if isinstance(ylabel, np.ndarray) \
            or isinstance(ylabel, list) \
            or isinstance(ylabel, pd.Series) \
            or isinstance(ylabel, pd.Index):

            pie_chart_dict['ylabel']['text'] = dtypesx.cnv_data_to_array(ylabel)

        else: pie_chart_dict['ylabel']['text'] = np.array([str(ylabel)], dtype = str) 

    elif chart_type == chart_enum.PLOT.value:

        global plot_chart_dict

        if isinstance(xlabel, np.ndarray) \
            or isinstance(xlabel, list) \
            or isinstance(xlabel, pd.Series) \
            or isinstance(xlabel, pd.Index):

            plot_chart_dict['xlabel']['text'] = dtypesx.cnv_data_to_array(xlabel)

        else: plot_chart_dict['xlabel']['text'] = np.array([str(xlabel)], dtype = str)

        if isinstance(ylabel, np.ndarray) \
            or isinstance(ylabel, list) \
            or isinstance(ylabel, pd.Series) \
            or isinstance(ylabel, pd.Index):

            plot_chart_dict['ylabel']['text'] = dtypesx.cnv_data_to_array(ylabel)

        else: plot_chart_dict['ylabel']['text'] = np.array([str(ylabel)], dtype = str) 

    elif chart_type == chart_enum.SCATTER.value:

        global scatterplot_chart_dict

        if isinstance(xlabel, np.ndarray) \
            or isinstance(xlabel, list) \
            or isinstance(xlabel, pd.Series) \
            or isinstance(xlabel, pd.Index):

            scatterplot_chart_dict['xlabel']['text'] = dtypesx.cnv_data_to_array(xlabel)

        else: scatterplot_chart_dict['xlabel']['text'] = np.array([str(xlabel)], dtype = str)

        if isinstance(ylabel, np.ndarray) \
            or isinstance(ylabel, list) \
            or isinstance(ylabel, pd.Series) \
            or isinstance(ylabel, pd.Index):

            scatterplot_chart_dict['ylabel']['text'] = dtypesx.cnv_data_to_array(ylabel)

        else: scatterplot_chart_dict['ylabel']['text'] = np.array([str(ylabel)], dtype = str)

    elif chart_type == chart_enum.CORR_CV.value:

        global corr_cv_dict

        if isinstance(xlabel, np.ndarray) \
            or isinstance(xlabel, list) \
            or isinstance(xlabel, pd.Series) \
            or isinstance(xlabel, pd.Index):

            corr_cv_dict['xlabel']['text'] = dtypesx.cnv_data_to_array(xlabel)

        else: corr_cv_dict['xlabel']['text'] = np.array([str(xlabel)], dtype = str)

        if isinstance(ylabel, np.ndarray) \
            or isinstance(ylabel, list) \
            or isinstance(ylabel, pd.Series) \
            or isinstance(ylabel, pd.Index):

            corr_cv_dict['ylabel']['text'] = dtypesx.cnv_data_to_array(ylabel)

        else: corr_cv_dict['ylabel']['text'] = np.array([str(ylabel)], dtype = str)

    elif chart_type == chart_enum.CORR_SCORES.value:

        global corr_scores_dict

        if isinstance(xlabel, np.ndarray) \
            or isinstance(xlabel, list) \
            or isinstance(xlabel, pd.Series) \
            or isinstance(xlabel, pd.Index):

            corr_scores_dict['xlabel']['text'] = dtypesx.cnv_data_to_array(xlabel)

        else: corr_scores_dict['xlabel']['text'] = np.array([str(xlabel)], dtype = str)

        if isinstance(ylabel, np.ndarray) \
            or isinstance(ylabel, list) \
            or isinstance(ylabel, pd.Series) \
            or isinstance(ylabel, pd.Index):

            corr_scores_dict['ylabel']['text'] = dtypesx.cnv_data_to_array(ylabel)

        else: corr_scores_dict['ylabel']['text'] = np.array([str(ylabel)], dtype = str)

    elif chart_type == chart_enum.WINDOW_CV.value:

        global window_cv_dict

        if isinstance(xlabel, np.ndarray) \
            or isinstance(xlabel, list) \
            or isinstance(xlabel, pd.Series) \
            or isinstance(xlabel, pd.Index):

            window_cv_dict['xlabel']['text'] = dtypesx.cnv_data_to_array(xlabel)

        else: window_cv_dict['xlabel']['text'] = np.array([str(xlabel)], dtype = str)

        if isinstance(ylabel, np.ndarray) \
            or isinstance(ylabel, list) \
            or isinstance(ylabel, pd.Series) \
            or isinstance(ylabel, pd.Index):

            window_cv_dict['ylabel']['text'] = dtypesx.cnv_data_to_array(ylabel)

        else: window_cv_dict['ylabel']['text'] = np.array([str(ylabel)], dtype = str)

    elif chart_type == chart_enum.ROLL_CORR.value:

        global roll_corr_dict

        if isinstance(xlabel, np.ndarray) \
            or isinstance(xlabel, list) \
            or isinstance(xlabel, pd.Series) \
            or isinstance(xlabel, pd.Index):

            roll_corr_dict['xlabel']['text'] = dtypesx.cnv_data_to_array(xlabel)

        else: roll_corr_dict['xlabel']['text'] = np.array([str(xlabel)], dtype = str)

        if isinstance(ylabel, np.ndarray) \
            or isinstance(ylabel, list) \
            or isinstance(ylabel, pd.Series) \
            or isinstance(ylabel, pd.Index):

            roll_corr_dict['ylabel']['text'] = dtypesx.cnv_data_to_array(ylabel)

        else: roll_corr_dict['ylabel']['text'] = np.array([str(ylabel)], dtype = str)

    elif chart_type == chart_enum.ROLL_CORR_ALL.value:

        global roll_corr_all_dict

        if isinstance(xlabel, np.ndarray) \
            or isinstance(xlabel, list) \
            or isinstance(xlabel, pd.Series) \
            or isinstance(xlabel, pd.Index):

            roll_corr_all_dict['xlabel']['text'] = dtypesx.cnv_data_to_array(xlabel)

        else: roll_corr_all_dict['xlabel']['text'] = np.array([str(xlabel)], dtype = str)

        if isinstance(ylabel, np.ndarray) \
            or isinstance(ylabel, list) \
            or isinstance(ylabel, pd.Series) \
            or isinstance(ylabel, pd.Index):

            roll_corr_all_dict['ylabel']['text'] = dtypesx.cnv_data_to_array(ylabel)

        else: roll_corr_all_dict['ylabel']['text'] = np.array([str(ylabel)], dtype = str) 

    elif chart_type == chart_enum.LAG_CORR.value:

        global lag_corr_dict       

        if isinstance(xlabel, np.ndarray) \
            or isinstance(xlabel, list) \
            or isinstance(xlabel, pd.Series) \
            or isinstance(xlabel, pd.Index):

            lag_corr_dict['xlabel']['text'] = dtypesx.cnv_data_to_array(xlabel)

        else: lag_corr_dict['xlabel']['text'] = np.array([str(xlabel)], dtype = str)

        if isinstance(ylabel, np.ndarray) \
            or isinstance(ylabel, list) \
            or isinstance(ylabel, pd.Series) \
            or isinstance(ylabel, pd.Index):

            lag_corr_dict['ylabel']['text'] = dtypesx.cnv_data_to_array(ylabel)

        else: lag_corr_dict['ylabel']['text'] = np.array([str(ylabel)], dtype = str)

    elif chart_type == chart_enum.LAG_HEAT.value:

        global lag_heat_dict

        if isinstance(xlabel, np.ndarray) \
            or isinstance(xlabel, list) \
            or isinstance(xlabel, pd.Series) \
            or isinstance(xlabel, pd.Index):

            lag_heat_dict['xlabel']['text'] = dtypesx.cnv_data_to_array(xlabel)

        else: lag_heat_dict['xlabel']['text'] = np.array([str(xlabel)], dtype = str)

        if isinstance(ylabel, np.ndarray) \
            or isinstance(ylabel, list) \
            or isinstance(ylabel, pd.Series) \
            or isinstance(ylabel, pd.Index):

            lag_heat_dict['ylabel']['text'] = dtypesx.cnv_data_to_array(ylabel)

        else: lag_heat_dict['ylabel']['text'] = np.array([str(ylabel)], dtype = str) 


# In[64]:


#*******************************************************************************************
 #
 #  Function Name:  set_xylabels_display
 #
 #  Function Description:
 #      The function sets the chart's x-axis label display and y-axis label display.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  boolean        xdisp_bool       The parameter is the chart's x-axis label display.
 #  boolean        ydisp_bool       The parameter is the chart's y-axis label display.
 #  enum           chart_type       The parameter is the chart type enumeration value.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_xylabels_display(xdisplay_bool, ydisplay_bool, chart_type):

    if chart_type == chart_enum.BAR.value:

        global bar_chart_dict

        bar_chart_dict['xlabel']['display'] = xdisplay_bool

        bar_chart_dict['ylabel']['display'] = ydisplay_bool

    elif chart_type == chart_enum.BOXPLOT.value:

        global boxplot_chart_dict

        boxplot_chart_dict['xlabel']['display'] = xdisplay_bool

        boxplot_chart_dict['ylabel']['display'] = ydisplay_bool

    elif chart_type == chart_enum.HISTOGRAM.value:

        global histogram_chart_dict

        histogram_chart_dict['xlabel']['display'] = xdisplay_bool

        histogram_chart_dict['ylabel']['display'] = ydisplay_bool

    elif chart_type == chart_enum.LINE.value:

        global line_chart_dict

        line_chart_dict['xlabel']['display'] = xdisplay_bool

        line_chart_dict['ylabel']['display'] = ydisplay_bool

    elif chart_type == chart_enum.PIE.value:

        global pie_chart_dict

        pie_chart_dict['xlabel']['display'] = xdisplay_bool

        pie_chart_dict['ylabel']['display'] = ydisplay_bool

    elif chart_type == chart_enum.PLOT.value:

        global plot_chart_dict

        plot_chart_dict['xlabel']['display'] = xdisplay_bool

        plot_chart_dict['ylabel']['display'] = ydisplay_bool

    elif chart_type == chart_enum.SCATTER.value:

        global scatterplot_chart_dict

        scatterplot_chart_dict['xlabel']['display'] = xdisplay_bool

        scatterplot_chart_dict['ylabel']['display'] = ydisplay_bool

    elif chart_type == chart_enum.CORR_CV.value:

        global corr_cv_dict

        corr_cv_dict['xlabel']['display'] = xdisplay_bool

        corr_cv_dict['ylabel']['display'] = ydisplay_bool

    elif chart_type == chart_enum.CORR_SCORES.value:

        global corr_scores_dict

        corr_scores_dict['xlabel']['display'] = xdisplay_bool

        corr_scores_dict['ylabel']['display'] = ydisplay_bool

    elif chart_type == chart_enum.WINDOW_CV.value:

        global window_cv_dict

        window_cv_dict['xlabel']['display'] = xdisplay_bool

        window_cv_dict['ylabel']['display'] = ydisplay_bool

    elif chart_type == chart_enum.ROLL_CORR.value:

        global roll_corr_dict

        roll_corr_dict['xlabel']['display'] = xdisplay_bool

        roll_corr_dict['ylabel']['display'] = ydisplay_bool

    elif chart_type == chart_enum.ROLL_CORR_ALL.value:

        global roll_corr_all_dict

        roll_corr_all_dict['xlabel']['display'] = xdisplay_bool

        roll_corr_all_dict['ylabel']['display'] = ydisplay_bool

    elif chart_type == chart_enum.LAG_CORR.value:

        global lag_corr_dict

        lag_corr_dict['xlabel']['display'] = xdisplay_bool

        lag_corr_dict['ylabel']['display'] = ydisplay_bool

    elif chart_type == chart_enum.LAG_HEAT.value:

        global lag_heat_dict

        lag_heat_dict['xlabel']['display'] = xdisplay_bool

        lag_heat_dict['ylabel']['display'] = ydisplay_bool


# In[65]:


#*******************************************************************************************
 #
 #  Function Name:  set_xylabels_fontsize
 #
 #  Function Description:
 #      The function sets the chart's x and y axes font sizes.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  float          xsize_flt        The parameter is the chart's x-axis label font size.
 #  float          ysize_flt        The parameter is the chart's y-axis label font size.
 #  enum           chart_type       The parameter is the chart type enumeration value.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_xylabels_fontsize(xsize_flt, ysize_flt, chart_type):

    if chart_type == chart_enum.BAR.value:

        global bar_chart_dict

        bar_chart_dict['xlabel']['fontsize'] = xsize_flt

        bar_chart_dict['ylabel']['fontsize'] = ysize_flt

    elif chart_type == chart_enum.BOXPLOT.value:

        global boxplot_chart_dict

        boxplot_chart_dict['xlabel']['fontsize'] = xsize_flt

        boxplot_chart_dict['ylabel']['fontsize'] = ysize_flt

    elif chart_type == chart_enum.HISTOGRAM.value:

        global histogram_chart_dict

        histogram_chart_dict['xlabel']['fontsize'] = xsize_flt

        histogram_chart_dict['ylabel']['fontsize'] = ysize_flt

    elif chart_type == chart_enum.LINE.value:

        global line_chart_dict

        line_chart_dict['xlabel']['fontsize'] = xsize_flt

        line_chart_dict['ylabel']['fontsize'] = ysize_flt

    elif chart_type == chart_enum.PIE.value:

        global pie_chart_dict

        pie_chart_dict['xlabel']['fontsize'] = xsize_flt

        pie_chart_dict['ylabel']['fontsize'] = ysize_flt

    elif chart_type == chart_enum.PLOT.value:

        global plot_chart_dict

        plot_chart_dict['xlabel']['fontsize'] = xsize_flt

        plot_chart_dict['ylabel']['fontsize'] = ysize_flt

    elif chart_type == chart_enum.SCATTER.value:

        global scatterplot_chart_dict

        scatterplot_chart_dict['xlabel']['fontsize'] = xsize_flt

        scatterplot_chart_dict['ylabel']['fontsize'] = ysize_flt

    elif chart_type == chart_enum.CORR_CV.value:

        global corr_cv_dict

        corr_cv_dict['xlabel']['fontsize'] = xsize_flt

        corr_cv_dict['ylabel']['fontsize'] = ysize_flt

    elif chart_type == chart_enum.CORR_SCORES.value:

        global corr_scores_dict

        corr_scores_dict['xlabel']['fontsize'] = xsize_flt

        corr_scores_dict['ylabel']['fontsize'] = ysize_flt

    elif chart_type == chart_enum.WINDOW_CV.value:

        global window_cv_dict

        window_cv_dict['xlabel']['fontsize'] = xsize_flt

        window_cv_dict['ylabel']['fontsize'] = ysize_flt

    elif chart_type == chart_enum.ROLL_CORR.value:

        global roll_corr_dict

        roll_corr_dict['xlabel']['fontsize'] = xsize_flt

        roll_corr_dict['ylabel']['fontsize'] = ysize_flt

    elif chart_type == chart_enum.ROLL_CORR_ALL.value:

        global roll_corr_all_dict

        roll_corr_all_dict['xlabel']['fontsize'] = xsize_flt

        roll_corr_all_dict['ylabel']['fontsize'] = ysize_flt

    elif chart_type == chart_enum.LAG_CORR.value:

        global lag_corr_dict

        lag_corr_dict['xlabel']['fontsize'] = xsize_flt

        lag_corr_dict['ylabel']['fontsize'] = ysize_flt

    elif chart_type == chart_enum.LAG_HEAT.value:

        global lag_heat_dict

        lag_heat_dict['xlabel']['fontsize'] = xsize_flt

        lag_heat_dict['ylabel']['fontsize'] = ysize_flt


# In[66]:


#*******************************************************************************************
 #
 #  Function Name:  set_xylabels_pad
 #
 #  Function Description:
 #      The function sets the chart's x and y axes pads.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  float          xpad_flt         The parameter is the chart's x-axis label pad.
 #  float          ypad_flt         The parameter is the chart's y-axis label pad.
 #  enum           chart_type       The parameter is the chart type enumeration value.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_xylabels_pad(xpad_flt, ypad_flt, chart_type):

    if chart_type == chart_enum.BAR.value:

        global bar_chart_dict

        bar_chart_dict['xlabel']['pad'] = xpad_flt

        bar_chart_dict['ylabel']['pad'] = ypad_flt

    elif chart_type == chart_enum.BOXPLOT.value:

        global boxplot_chart_dict

        boxplot_chart_dict['xlabel']['pad'] = xpad_flt

        boxplot_chart_dict['ylabel']['pad'] = ypad_flt

    elif chart_type == chart_enum.HISTOGRAM.value:

        global histogram_chart_dict

        histogram_chart_dict['xlabel']['pad'] = xpad_flt

        histogram_chart_dict['ylabel']['pad'] = ypad_flt

    elif chart_type == chart_enum.LINE.value:

        global line_chart_dict

        line_chart_dict['xlabel']['pad'] = xpad_flt

        line_chart_dict['ylabel']['pad'] = ypad_flt

    elif chart_type == chart_enum.PIE.value:

        global pie_chart_dict

        pie_chart_dict['xlabel']['pad'] = xpad_flt

        pie_chart_dict['ylabel']['pad'] = ypad_flt

    elif chart_type == chart_enum.PLOT.value:

        global plot_chart_dict

        plot_chart_dict['xlabel']['pad'] = xpad_flt

        plot_chart_dict['ylabel']['pad'] = ypad_flt

    elif chart_type == chart_enum.SCATTER.value:

        global scatterplot_chart_dict

        scatterplot_chart_dict['xlabel']['pad'] = xpad_flt

        scatterplot_chart_dict['ylabel']['pad'] = ypad_flt

    elif chart_type == chart_enum.CORR_CV.value:

        global corr_cv_dict

        corr_cv_dict['xlabel']['pad'] = xpad_flt

        corr_cv_dict['ylabel']['pad'] = ypad_flt

    elif chart_type == chart_enum.CORR_SCORES.value:

        global corr_scores_dict

        corr_scores_dict['xlabel']['pad'] = xpad_flt

        corr_scores_dict['ylabel']['pad'] = ypad_flt

    elif chart_type == chart_enum.WINDOW_CV.value:

        global window_cv_dict

        window_cv_dict['xlabel']['pad'] = xpad_flt

        window_cv_dict['ylabel']['pad'] = ypad_flt

    elif chart_type == chart_enum.ROLL_CORR.value:

        global roll_corr_dict

        roll_corr_dict['xlabel']['pad'] = xpad_flt

        roll_corr_dict['ylabel']['pad'] = ypad_flt

    elif chart_type == chart_enum.ROLL_CORR_ALL.value:

        global roll_corr_all_dict

        roll_corr_all_dict['xlabel']['pad'] = xpad_flt

        roll_corr_all_dict['ylabel']['pad'] = ypad_flt

    elif chart_type == chart_enum.LAG_CORR.value:

        global lag_corr_dict

        lag_corr_dict['xlabel']['pad'] = xpad_flt

        lag_corr_dict['ylabel']['pad'] = ypad_flt

    elif chart_type == chart_enum.LAG_HEAT.value:

        global lag_heat_dict

        lag_heat_dict['xlabel']['pad'] = xpad_flt

        lag_heat_dict['ylabel']['pad'] = ypad_flt


# In[67]:


#*******************************************************************************************
 #
 #  Function Name:  set_xyticks_fontsize
 #
 #  Function Description:
 #      The function sets the chart's x and y axes pads.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  float          xsize_flt        The parameter is the chart's x-ticks label font size.
 #  float          ysize_flt        The parameter is the chart's y-ticks label font size.
 #  enum           chart_type       The parameter is the chart type enumeration value.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_xyticks_fontsize(xsize_flt, ysize_flt, chart_type):

    if chart_type == chart_enum.BAR.value:

        global bar_chart_dict

        bar_chart_dict['xticks']['fontsize'] = xsize_flt

        bar_chart_dict['yticks']['fontsize'] = ysize_flt

    elif chart_type == chart_enum.BOXPLOT.value:

        global boxplot_chart_dict

        boxplot_chart_dict['xticks']['fontsize'] = xsize_flt

        boxplot_chart_dict['yticks']['fontsize'] = ysize_flt

    elif chart_type == chart_enum.HISTOGRAM.value:

        global histogram_chart_dict

        histogram_chart_dict['xticks']['fontsize'] = xsize_flt

        histogram_chart_dict['yticks']['fontsize'] = ysize_flt

    elif chart_type == chart_enum.LINE.value:

        global line_chart_dict

        line_chart_dict['xticks']['fontsize'] = xsize_flt

        line_chart_dict['yticks']['fontsize'] = ysize_flt

    elif chart_type == chart_enum.PIE.value:

        global pie_chart_dict

        pie_chart_dict['xticks']['fontsize'] = xsize_flt

        pie_chart_dict['yticks']['fontsize'] = ysize_flt

    elif chart_type == chart_enum.PLOT.value:

        global plot_chart_dict

        plot_chart_dict['xticks']['fontsize'] = xsize_flt

        plot_chart_dict['yticks']['fontsize'] = ysize_flt

    elif chart_type == chart_enum.SCATTER.value:

        global scatterplot_chart_dict

        scatterplot_chart_dict['xticks']['fontsize'] = xsize_flt

        scatterplot_chart_dict['yticks']['fontsize'] = ysize_flt

    elif chart_type == chart_enum.CORR_CV.value:

        global corr_cv_dict

        corr_cv_dict['xticks']['fontsize'] = xsize_flt

        corr_cv_dict['yticks']['fontsize'] = ysize_flt

    elif chart_type == chart_enum.CORR_SCORES.value:

        global corr_scores_dict

        corr_scores_dict['xticks']['fontsize'] = xsize_flt

        corr_scores_dict['yticks']['fontsize'] = ysize_flt

    elif chart_type == chart_enum.WINDOW_CV.value:

        global window_cv_dict

        window_cv_dict['xticks']['fontsize'] = xsize_flt

        window_cv_dict['yticks']['fontsize'] = ysize_flt

    elif chart_type == chart_enum.ROLL_CORR.value:

        global roll_corr_dict

        roll_corr_dict['xticks']['fontsize'] = xsize_flt

        roll_corr_dict['yticks']['fontsize'] = ysize_flt

    elif chart_type == chart_enum.ROLL_CORR_ALL.value:

        global roll_corr_all_dict

        roll_corr_all_dict['xticks']['fontsize'] = xsize_flt

        roll_corr_all_dict['yticks']['fontsize'] = ysize_flt

    elif chart_type == chart_enum.LAG_CORR.value:

        global lag_corr_dict

        lag_corr_dict['xticks']['fontsize'] = xsize_flt

        lag_corr_dict['yticks']['fontsize'] = ysize_flt

    elif chart_type == chart_enum.LAG_HEAT.value:

        global lag_heat_dict

        lag_heat_dict['xticks']['fontsize'] = xsize_flt

        lag_heat_dict['yticks']['fontsize'] = ysize_flt


# In[68]:


#*******************************************************************************************
 #
 #  Function Name:  set_xyticks_rotation
 #
 #  Function Description:
 #      The function sets the chart's x and y axes label rotation angles.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  float          xrot_flt         The parameter is the chart's x-ticks label rotation.
 #  float          yrot_flt         The parameter is the chart's y-ticks label rotation.
 #  enum           chart_type       The parameter is the chart type enumeration value.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_xyticks_rotation(xrot_flt, yrot_flt, chart_type):

    if chart_type == chart_enum.BAR.value:

        global bar_chart_dict

        bar_chart_dict['xticks']['rotation'] = xrot_flt

        bar_chart_dict['yticks']['rotation'] = yrot_flt

    elif chart_type == chart_enum.BOXPLOT.value:

        global boxplot_chart_dict

        boxplot_chart_dict['xticks']['rotation'] = xrot_flt

        boxplot_chart_dict['yticks']['rotation'] = yrot_flt

    elif chart_type == chart_enum.HISTOGRAM.value:

        global histogram_chart_dict

        histogram_chart_dict['xticks']['rotation'] = xrot_flt

        histogram_chart_dict['yticks']['rotation'] = yrot_flt

    elif chart_type == chart_enum.LINE.value:

        global line_chart_dict

        line_chart_dict['xticks']['rotation'] = xrot_flt

        line_chart_dict['yticks']['rotation'] = yrot_flt

    elif chart_type == chart_enum.PIE.value:

        global pie_chart_dict

        pie_chart_dict['xticks']['rotation'] = xrot_flt

        pie_chart_dict['yticks']['rotation'] = yrot_flt

    elif chart_type == chart_enum.PLOT.value:

        global plot_chart_dict

        plot_chart_dict['xticks']['rotation'] = xrot_flt

        plot_chart_dict['yticks']['rotation'] = yrot_flt

    elif chart_type == chart_enum.SCATTER.value:

        global scatterplot_chart_dict

        scatterplot_chart_dict['xticks']['rotation'] = xrot_flt

        scatterplot_chart_dict['yticks']['rotation'] = yrot_flt

    elif chart_type == chart_enum.CORR_CV.value:

        global corr_cv_dict

        corr_cv_dict['xticks']['rotation'] = xrot_flt

        corr_cv_dict['yticks']['rotation'] = yrot_flt

    elif chart_type == chart_enum.CORR_SCORES.value:

        global corr_scores_dict

        corr_scores_dict['xticks']['rotation'] = xrot_flt

        corr_scores_dict['yticks']['rotation'] = yrot_flt

    elif chart_type == chart_enum.WINDOW_CV.value:

        global window_cv_dict

        window_cv_dict['xticks']['rotation'] = xrot_flt

        window_cv_dict['yticks']['rotation'] = yrot_flt

    elif chart_type == chart_enum.ROLL_CORR.value:

        global roll_corr_dict

        roll_corr_dict['xticks']['rotation'] = xrot_flt

        roll_corr_dict['yticks']['rotation'] = yrot_flt

    elif chart_type == chart_enum.ROLL_CORR_ALL.value:

        global roll_corr_all_dict

        roll_corr_all_dict['xticks']['rotation'] = xrot_flt

        roll_corr_all_dict['yticks']['rotation'] = yrot_flt

    elif chart_type == chart_enum.LAG_CORR.value:

        global lag_corr_dict

        lag_corr_dict['xticks']['rotation'] = xrot_flt

        lag_corr_dict['yticks']['rotation'] = yrot_flt

    elif chart_type == chart_enum.LAG_HEAT.value:

        global lag_heat_dict

        lag_heat_dict['xticks']['rotation'] = xrot_flt

        lag_heat_dict['yticks']['rotation'] = yrot_flt


# In[69]:


#*******************************************************************************************
 #
 #  Function Name:  set_chart_colors
 #
 #  Function Description:
 #      The function sets the chart colors.
 #
 #
 #  Return Type: string or list
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  object         upd_obj          The parameter is the updated group of chart colors.
 #  enum           chart_type       The parameter is the multichart type enumeration value.
 #  string         cat              The parameter is the color category.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_chart_colors(upd_obj, chart_type, cat = ''):

    if chart_type == chart_enum.BAR.value:

        global bar_chart_dict

        if isinstance(upd_obj, str):

            bar_chart_dict['params']['color'] = np.array(upd_obj, dtype = str)

        elif isinstance(upd_obj, list) \
            or isinstance(upd_obj, np.ndarray) \
            or isinstance(upd_obj, pd.Series):

            bar_chart_dict['params']['color'] = dtypesx.cnv_data_to_array(upd_obj)

    elif chart_type == chart_enum.HISTOGRAM.value:

        global histogram_chart_dict

        if isinstance(upd_obj, str):

            histogram_chart_dict['params']['color'] = np.array(upd_obj, dtype = str)

        elif isinstance(upd_obj, list) \
            or isinstance(upd_obj, np.ndarray) \
            or isinstance(upd_obj, pd.Series):

            histogram_chart_dict['params']['color'] = dtypesx.cnv_data_to_array(upd_obj)

    elif chart_type == chart_enum.LINE.value:

        global line_chart_dict

        if isinstance(upd_obj, str):

            line_chart_dict[cat]['color'] = np.array(upd_obj, dtype = str)

        elif isinstance(upd_obj, list) \
            or isinstance(upd_obj, np.ndarray) \
            or isinstance(upd_obj, pd.Series):

            line_chart_dict[cat]['color'] = dtypesx.cnv_data_to_array(upd_obj)

    elif chart_type == chart_enum.PIE.value:

        global pie_chart_dict

        if isinstance(upd_obj, str):

            pie_chart_dict['params']['colors'] = np.array(upd_obj, dtype = str)

        elif isinstance(upd_obj, list) \
            or isinstance(upd_obj, np.ndarray) \
            or isinstance(upd_obj, pd.Series):

            pie_chart_dict['params']['colors'] = dtypesx.cnv_data_to_array(upd_obj)

    elif chart_type == chart_enum.PLOT.value:

        global plot_chart_dict

        if isinstance(upd_obj, str):

            plot_chart_dict[cat]['color'] = np.array(upd_obj, dtype = str)

        elif isinstance(upd_obj, list) \
            or isinstance(upd_obj, np.ndarray) \
            or isinstance(upd_obj, pd.Series):

            plot_chart_dict[cat]['color'] = dtypesx.cnv_data_to_array(upd_obj)

    elif chart_type == chart_enum.SCATTER.value:

        global scatterplot_chart_dict

        if isinstance(upd_obj, str):

            scatterplot_chart_dict['marker']['color'] = np.array(upd_obj, dtype = str)

        elif isinstance(upd_obj, list) \
            or isinstance(upd_obj, np.ndarray) \
            or isinstance(upd_obj, pd.Series):

            scatterplot_chart_dict['marker']['color'] = dtypesx.cnv_data_to_array(upd_obj)

    elif chart_type == chart_enum.CORR_CV.value:

        global corr_cv_dict

        if isinstance(upd_obj, str):

            corr_cv_dict[cat]['color'] = np.array(upd_obj, dtype = str)

        elif isinstance(upd_obj, list) \
            or isinstance(upd_obj, np.ndarray) \
            or isinstance(upd_obj, pd.Series):

            corr_cv_dict[cat]['color'] = dtypesx.cnv_data_to_array(upd_obj)

    elif chart_type == chart_enum.CORR_SCORES.value:

        global corr_scores_dict

        if isinstance(upd_obj, str):

            corr_scores_dict[cat]['color'] = np.array(upd_obj, dtype = str)

        elif isinstance(upd_obj, list) \
            or isinstance(upd_obj, np.ndarray) \
            or isinstance(upd_obj, pd.Series):

            corr_scores_dict[cat]['color'] = dtypesx.cnv_data_to_array(upd_obj)

    elif chart_type == chart_enum.WINDOW_CV.value:

        global window_cv_dict

        if isinstance(upd_obj, str):

            window_cv_dict[cat]['color'] = np.array(upd_obj, dtype = str)

        elif isinstance(upd_obj, list) \
            or isinstance(upd_obj, np.ndarray) \
            or isinstance(upd_obj, pd.Series):

            window_cv_dict[cat]['color'] = dtypesx.cnv_data_to_array(upd_obj)

    elif chart_type == chart_enum.ROLL_CORR.value:

        global roll_corr_dict

        if isinstance(upd_obj, str):

            roll_corr_dict[cat]['color'] = np.array(upd_obj, dtype = str)

        elif isinstance(upd_obj, list) \
            or isinstance(upd_obj, np.ndarray) \
            or isinstance(upd_obj, pd.Series):

            roll_corr_dict[cat]['color'] = dtypesx.cnv_data_to_array(upd_obj)

    elif chart_type == chart_enum.ROLL_CORR_ALL.value:

        global roll_corr_all_dict

        if isinstance(upd_obj, str):

            roll_corr_all_dict[cat]['color'] = np.array(upd_obj, dtype = str)

        elif isinstance(upd_obj, list) \
            or isinstance(upd_obj, np.ndarray) \
            or isinstance(upd_obj, pd.Series):

            roll_corr_all_dict[cat]['color'] = dtypesx.cnv_data_to_array(upd_obj)

    elif chart_type == chart_enum.LAG_CORR.value:

        global lag_corr_dict

        if isinstance(upd_obj[0], str):

            lag_corr_dict[cat]['upr_clr'] = np.array(upd_obj[0], dtype = str)

        else: lag_corr_dict[cat]['upr_clr'] = str(upd_obj[0])

        if isinstance(upd_obj[1], str):

            lag_corr_dict[cat]['lwr_clr'] = np.array(upd_obj[1], dtype = str)

        else: lag_corr_dict[cat]['lwr_clr'] = str(upd_obj[1])

    elif chart_type == chart_enum.LAG_HEAT.value:

        global lag_heat_dict

        if isinstance(upd_obj, str):

            lag_heat_dict[cat]['color'] = np.array(upd_obj, dtype = str)

        elif isinstance(upd_obj, list) \
            or isinstance(upd_obj, np.ndarray) \
            or isinstance(upd_obj, pd.Series):

            lag_heat_dict[cat]['color'] = dtypesx.cnv_data_to_array(upd_obj)


# In[70]:


#*******************************************************************************************
 #
 #  Function Name:  set_legend_display
 #
 #  Function Description:
 #      The function sets a chart's legend display indicator.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  float          x_flt            The parameter is the x-coordinate.
 #  float          y_flt            The parameter is the y-coordinate.
 #  enum           chart_type       The parameter is the multichart type enumeration value.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_legend_display(upd_bool, chart_type):

    if chart_type == chart_enum.BAR.value:

        global bar_chart_dict

        bar_chart_dict['legend']['display'] = upd_bool

    elif chart_type == chart_enum.HISTOGRAM.value:

        global histogram_chart_dict

        histogram_chart_dict['legend']['display'] = upd_bool

    elif chart_type == chart_enum.LINE.value:

        global line_chart_dict

        line_chart_dict['legend']['display'] = upd_bool

    elif chart_type == chart_enum.PIE.value:

        global pie_chart_dict

        pie_chart_dict['legend']['display'] = upd_bool

    elif chart_type == chart_enum.PLOT.value:

        global plot_chart_dict

        plot_chart_dict['legend']['display'] = upd_bool

    elif chart_type == chart_enum.CORR_CV.value:

        global corr_cv_dict

        corr_cv_dict['legend']['display'] = upd_bool

    elif chart_type == chart_enum.CORR_SCORES.value:

        global corr_scores_dict

        corr_scores_dict['legend']['display'] = upd_bool

    elif chart_type == chart_enum.WINDOW_CV.value:

        global window_cv_dict

        window_cv_dict['legend']['display'] = upd_bool

    elif chart_type == chart_enum.ROLL_CORR.value:

        global roll_corr_dict

        roll_corr_dict['legend']['display'] = upd_bool

    elif chart_type == chart_enum.ROLL_CORR_ALL.value:

        global roll_corr_all_dict

        roll_corr_all_dict['legend']['display'] = upd_bool

    elif chart_type == chart_enum.LAG_CORR.value:

        global lag_corr_dict

        lag_corr_dict['legend']['display'] = upd_bool

    elif chart_type == chart_enum.LAG_HEAT.value:

        global lag_heat_dict

        lag_heat_dict['legend']['display'] = upd_bool


# In[71]:


#*******************************************************************************************
 #
 #  Function Name:  set_legend_fontsize
 #
 #  Function Description:
 #      The function sets a chart's legend font size.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  float          upd_flt          The parameter is the updated font size.
 #  enum           chart_type       The parameter is the multichart type enumeration value.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_legend_fontsize(upd_flt, chart_type):

    if chart_type == chart_enum.BAR.value:

        global bar_chart_dict

        bar_chart_dict['legend']['fontsize'] = upd_flt

    elif chart_type == chart_enum.HISTOGRAM.value:

        global histogram_chart_dict

        histogram_chart_dict['legend']['fontsize'] = upd_flt

    elif chart_type == chart_enum.LINE.value:

        global line_chart_dict

        line_chart_dict['legend']['fontsize'] = upd_flt

    elif chart_type == chart_enum.PIE.value:

        global pie_chart_dict

        pie_chart_dict['legend']['fontsize'] = upd_flt

    elif chart_type == chart_enum.PLOT.value:

        global plot_chart_dict

        plot_chart_dict['legend']['fontsize'] = upd_flt

    elif chart_type == chart_enum.CORR_CV.value:

        global corr_cv_dict

        corr_cv_dict['legend']['fontsize'] = upd_flt

    elif chart_type == chart_enum.CORR_SCORES.value:

        global corr_scores_dict

        corr_scores_dict['legend']['fontsize'] = upd_flt

    elif chart_type == chart_enum.WINDOW_CV.value:

        global window_cv_dict

        window_cv_dict['legend']['fontsize'] = upd_flt

    elif chart_type == chart_enum.ROLL_CORR.value:

        global roll_corr_dict

        roll_corr_dict['legend']['fontsize'] = upd_flt

    elif chart_type == chart_enum.ROLL_CORR_ALL.value:

        global roll_corr_all_dict

        roll_corr_all_dict['legend']['fontsize'] = upd_flt

    elif chart_type == chart_enum.LAG_CORR.value:

        global lag_corr_dict

        lag_corr_dict['legend']['fontsize'] = upd_flt

    elif chart_type == chart_enum.LAG_HEAT.value:

        global lag_heat_dict

        lag_heat_dict['legend']['fontsize'] = upd_flt


# In[72]:


#*******************************************************************************************
 #
 #  Function Name:  set_legend_bbox_to_anchor
 #
 #  Function Description:
 #      The function sets a chart's legend bbox to anchor.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  float          x_flt            The parameter is the x-coordinate.
 #  float          y_flt            The parameter is the y-coordinate.
 #  enum           chart_type       The parameter is the multichart type enumeration value.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_legend_bbox_to_anchor(x_flt, y_flt, chart_type):

    if chart_type == chart_enum.BAR.value:

        global bar_chart_dict

        bar_chart_dict['legend']['bbox_to_anchor'] = np.array([x_flt, y_flt], dtype = float)

    elif chart_type == chart_enum.HISTOGRAM.value:

        global histogram_chart_dict

        histogram_chart_dict['legend']['bbox_to_anchor'] = np.array([x_flt, y_flt], dtype = float)

    elif chart_type == chart_enum.LINE.value:

        global line_chart_dict

        line_chart_dict['legend']['bbox_to_anchor'] = np.array([x_flt, y_flt], dtype = float)

    elif chart_type == chart_enum.PIE.value:

        global pie_chart_dict

        pie_chart_dict['legend']['bbox_to_anchor'] = np.array([x_flt, y_flt], dtype = float)

    elif chart_type == chart_enum.PLOT.value:

        global plot_chart_dict

        plot_chart_dict['legend']['bbox_to_anchor'] = np.array([x_flt, y_flt], dtype = float)

    elif chart_type == chart_enum.CORR_CV.value:

        global corr_cv_dict

        corr_cv_dict['legend']['bbox_to_anchor'] = np.array([x_flt, y_flt], dtype = float)

    elif chart_type == chart_enum.CORR_SCORES.value:

        global corr_scores_dict

        corr_scores_dict['legend']['bbox_to_anchor'] = np.array([x_flt, y_flt], dtype = float)

    elif chart_type == chart_enum.WINDOW_CV.value:

        global window_cv_dict

        window_cv_dict['legend']['bbox_to_anchor'] = np.array([x_flt, y_flt], dtype = float)

    elif chart_type == chart_enum.ROLL_CORR.value:

        global roll_corr_dict

        roll_corr_dict['legend']['bbox_to_anchor'] = np.array([x_flt, y_flt], dtype = float)

    elif chart_type == chart_enum.ROLL_CORR_ALL.value:

        global roll_corr_all_dict

        roll_corr_all_dict['legend']['bbox_to_anchor'] = np.array([x_flt, y_flt], dtype = float)

    elif chart_type == chart_enum.LAG_CORR.value:

        global lag_corr_dict

        lag_corr_dict['legend']['bbox_to_anchor'] = np.array([x_flt, y_flt], dtype = float)

    elif chart_type == chart_enum.LAG_HEAT.value:

        global lag_heat_dict

        lag_heat_dict['legend']['bbox_to_anchor'] = np.array([x_flt, y_flt], dtype = float)


# In[73]:


#*******************************************************************************************
 #
 #  Function Name:  set_multichart_fig_dims
 #
 #  Function Description:
 #      The function sets the multichart's figure dimensions (width, length).
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  float          width_flt        The parameter is the chart figure's width.
 #  float          length_flt       The parameter is the chart figure's length.
 #  enum           chart_type       The parameter is the chart type enumeration value.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_multichart_fig_dims(width_flt, length_flt, chart_type):

    if chart_type == chart_enum.MULTIBAR.value:

        global bar_multichart_dict

        bar_multichart_dict['figure']['width'] = width_flt

        bar_multichart_dict['figure']['length'] = length_flt

    elif chart_type == chart_enum.MULTIBOXPLOT.value:

        global boxplot_multichart_dict

        boxplot_multichart_dict['figure']['width'] = width_flt

        boxplot_multichart_dict['figure']['length'] = length_flt

    elif chart_type == chart_enum.MULTIHISTOGRAM.value:

        global histogram_multichart_dict

        histogram_multichart_dict['figure']['width'] = width_flt

        histogram_multichart_dict['figure']['length'] = length_flt

    elif chart_type == chart_enum.MULTILINE.value:

        global line_multichart_dict

        line_multichart_dict['figure']['width'] = width_flt

        line_multichart_dict['figure']['length'] = length_flt

    elif chart_type == chart_enum.MULTIPIE.value:

        global pie_multichart_dict

        pie_multichart_dict['figure']['width'] = width_flt

        pie_multichart_dict['figure']['length'] = length_flt

    elif chart_type == chart_enum.MULTIPLOT.value:

        global plot_multichart_dict

        plot_multichart_dict['figure']['width'] = width_flt

        plot_multichart_dict['figure']['length'] = length_flt

    elif chart_type == chart_enum.MULTISCATTER.value:

        global scatterplot_multichart_dict

        scatterplot_multichart_dict['figure']['width'] = width_flt

        scatterplot_multichart_dict['figure']['length'] = length_flt


# In[74]:


#*******************************************************************************************
 #
 #  Function Name:  set_multichart_fig_spaces
 #
 #  Function Description:
 #      The function sets the multichart's figure spaces (wspace, hspace).
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  float          wspace_flt       The parameter is the chart figure's width.
 #  float          hspace_flt       The parameter is the chart figure's length.
 #  enum           chart_type       The parameter is the chart type enumeration value.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_multichart_fig_spaces(wspace_flt, hspace_flt, chart_type):

    if chart_type == chart_enum.MULTIBAR.value:

        global bar_multichart_dict

        bar_multichart_dict['figure']['wspace'] = wspace_flt

        bar_multichart_dict['figure']['hspace'] = hspace_flt

    elif chart_type == chart_enum.MULTIBOXPLOT.value:

        global boxplot_multichart_dict

        boxplot_multichart_dict['figure']['wspace'] = wspace_flt

        boxplot_multichart_dict['figure']['hspace'] = hspace_flt

    elif chart_type == chart_enum.MULTIHISTOGRAM.value:

        global histogram_multichart_dict

        histogram_multichart_dict['figure']['wspace'] = wspace_flt

        histogram_multichart_dict['figure']['hspace'] = hspace_flt

    elif chart_type == chart_enum.MULTILINE.value:

        global line_multichart_dict

        line_multichart_dict['figure']['wspace'] = wspace_flt

        line_multichart_dict['figure']['hspace'] = hspace_flt

    elif chart_type == chart_enum.MULTIPIE.value:

        global pie_multichart_dict

        pie_multichart_dict['figure']['wspace'] = wspace_flt

        pie_multichart_dict['figure']['hspace'] = hspace_flt

    elif chart_type == chart_enum.MULTIPLOT.value:

        global plot_multichart_dict

        plot_multichart_dict['figure']['wspace'] = wspace_flt

        plot_multichart_dict['figure']['hspace'] = hspace_flt

    elif chart_type == chart_enum.MULTISCATTER.value:

        global scatterplot_multichart_dict

        scatterplot_multichart_dict['figure']['wspace'] = wspace_flt

        scatterplot_multichart_dict['figure']['hspace'] = hspace_flt


# In[75]:


#*******************************************************************************************
 #
 #  Function Name:  set_multichart_stacked
 #
 #  Function Description:
 #      The function sets the multichart's stacked boolean value.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  boolean        upd_bool         The parameter is the chart's updated stacked boolean.
 #  enum           chart_type       The parameter is the chart type enumeration value.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_multichart_stacked(upd_bool, chart_type):

    if chart_type == chart_enum.MULTIBAR.value:

        global bar_multichart_dict

        bar_multichart_dict['figure']['stacked'] = upd_bool

    elif chart_type == chart_enum.MULTIBOXPLOT.value:

        global boxplot_multichart_dict

        boxplot_multichart_dict['figure']['stacked'] = upd_bool

    elif chart_type == chart_enum.MULTIHISTOGRAM.value:

        global histogram_multichart_dict

        histogram_multichart_dict['figure']['stacked'] = upd_bool

    elif chart_type == chart_enum.MULTILINE.value:

        global line_multichart_dict

        line_multichart_dict['figure']['stacked'] = upd_bool

    elif chart_type == chart_enum.MULTIPIE.value:

        global pie_multichart_dict

        pie_multichart_dict['figure']['stacked'] = upd_bool

    elif chart_type == chart_enum.MULTIPLOT.value:

        global plot_multichart_dict

        plot_multichart_dict['figure']['stacked'] = upd_bool

    elif chart_type == chart_enum.MULTISCATTER.value:

        global scatterplot_multichart_dict

        scatterplot_multichart_dict['figure']['stacked'] = upd_bool


# In[76]:


#*******************************************************************************************
 #
 #  Function Name:  set_multichart_suptitle_xycoords
 #
 #  Function Description:
 #      The function sets the multichart suptitle's x and y coordinates.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  float          x_flt            The parameter is the suptitle's x-coordinate.
 #  float          y_flt            The parameter is the suptitle's y-coordinate.
 #  enum           chart_type       The parameter is the multichart type enumeration value.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_multichart_suptitle_xycoords(x_flt, y_flt, chart_type):

    if chart_type == chart_enum.MULTIBAR.value:

        global bar_multichart_dict

        bar_multichart_dict['suptitle']['x'] = x_flt
        bar_multichart_dict['suptitle']['y'] = y_flt

    elif chart_type == chart_enum.MULTIBOXPLOT.value:

        global boxplot_multichart_dict

        boxplot_multichart_dict['suptitle']['x'] = x_flt
        boxplot_multichart_dict['suptitle']['y'] = y_flt

    elif chart_type == chart_enum.MULTIHISTOGRAM.value:

        global histogram_multichart_dict

        histogram_multichart_dict['suptitle']['x'] = x_flt
        histogram_multichart_dict['suptitle']['y'] = y_flt

    elif chart_type == chart_enum.MULTILINE.value:

        global line_multichart_dict

        line_multichart_dict['suptitle']['x'] = x_flt
        line_multichart_dict['suptitle']['y'] = y_flt

    elif chart_type == chart_enum.MULTIPIE.value:

        global pie_multichart_dict

        pie_multichart_dict['suptitle']['x'] = x_flt
        pie_multichart_dict['suptitle']['y'] = y_flt

    elif chart_type == chart_enum.MULTIPLOT.value:

        global plot_multichart_dict

        plot_multichart_dict['suptitle']['x'] = x_flt
        plot_multichart_dict['suptitle']['y'] = y_flt

    elif chart_type == chart_enum.MULTISCATTER.value:

        global scatterplot_multichart_dict

        scatterplot_multichart_dict['suptitle']['x'] = x_flt
        scatterplot_multichart_dict['suptitle']['y'] = y_flt


# In[77]:


#*******************************************************************************************
 #
 #  Function Name:  set_multichart_supxlabel_xycoords
 #
 #  Function Description:
 #      The function sets the multichart supxlabel's x and y coordinates.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  float          x_flt            The parameter is the supxlabel's x-coordinate.
 #  float          y_flt            The parameter is the supxlabel's y-coordinate.
 #  enum           chart_type       The parameter is the multichart type enumeration value.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_multichart_supxlabel_xycoords(x_flt, y_flt, chart_type):

    if chart_type == chart_enum.MULTIBAR.value:

        global bar_multichart_dict

        bar_multichart_dict['supxlabel']['x'] = x_flt
        bar_multichart_dict['supxlabel']['y'] = y_flt

    elif chart_type == chart_enum.MULTIBOXPLOT.value:

        global boxplot_multichart_dict

        boxplot_multichart_dict['supxlabel']['x'] = x_flt
        boxplot_multichart_dict['supxlabel']['y'] = y_flt

    elif chart_type == chart_enum.MULTIHISTOGRAM.value:

        global histogram_multichart_dict

        histogram_multichart_dict['supxlabel']['x'] = x_flt
        histogram_multichart_dict['supxlabel']['y'] = y_flt

    elif chart_type == chart_enum.MULTILINE.value:

        global line_multichart_dict

        line_multichart_dict['supxlabel']['x'] = x_flt
        line_multichart_dict['supxlabel']['y'] = y_flt

    elif chart_type == chart_enum.MULTIPIE.value:

        global pie_multichart_dict

        pie_multichart_dict['supxlabel']['x'] = x_flt
        pie_multichart_dict['supxlabel']['y'] = y_flt

    elif chart_type == chart_enum.MULTIPLOT.value:

        global plot_multichart_dict

        plot_multichart_dict['supxlabel']['x'] = x_flt
        plot_multichart_dict['supxlabel']['y'] = y_flt

    elif chart_type == chart_enum.MULTISCATTER.value:

        global scatterplot_multichart_dict

        scatterplot_multichart_dict['supxlabel']['x'] = x_flt
        scatterplot_multichart_dict['supxlabel']['y'] = y_flt


# In[78]:


#*******************************************************************************************
 #
 #  Function Name:  set_multichart_supylabel_xycoords
 #
 #  Function Description:
 #      The function sets the multichart supylabel's x and y coordinates.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  float          x_flt            The parameter is the supylabel's x-coordinate.
 #  float          y_flt            The parameter is the supylabel's y-coordinate.
 #  enum           chart_type       The parameter is the multichart type enumeration value.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_multichart_supylabel_xycoords(x_flt, y_flt, chart_type):

    if chart_type == chart_enum.MULTIBAR.value:

        global bar_multichart_dict

        bar_multichart_dict['supylabel']['x'] = x_flt
        bar_multichart_dict['supylabel']['y'] = y_flt

    elif chart_type == chart_enum.MULTIBOXPLOT.value:

        global boxplot_multichart_dict

        boxplot_multichart_dict['supylabel']['x'] = x_flt
        boxplot_multichart_dict['supylabel']['y'] = y_flt

    elif chart_type == chart_enum.MULTIHISTOGRAM.value:

        global histogram_multichart_dict

        histogram_multichart_dict['supylabel']['x'] = x_flt
        histogram_multichart_dict['supylabel']['y'] = y_flt

    elif chart_type == chart_enum.MULTILINE.value:

        global line_multichart_dict

        line_multichart_dict['supylabel']['x'] = x_flt
        line_multichart_dict['supylabel']['y'] = y_flt

    elif chart_type == chart_enum.MULTIPIE.value:

        global pie_multichart_dict

        pie_multichart_dict['supylabel']['x'] = x_flt
        pie_multichart_dict['supylabel']['y'] = y_flt

    elif chart_type == chart_enum.MULTIPLOT.value:

        global plot_multichart_dict

        plot_multichart_dict['supylabel']['x'] = x_flt
        plot_multichart_dict['supylabel']['y'] = y_flt

    elif chart_type == chart_enum.MULTISCATTER.value:

        global scatterplot_multichart_dict

        scatterplot_multichart_dict['supylabel']['x'] = x_flt
        scatterplot_multichart_dict['supylabel']['y'] = y_flt


# In[79]:


#*******************************************************************************************
 #
 #  Function Name:  set_multichart_suptitle_fontsize
 #
 #  Function Description:
 #      The function sets the multichart suptitle's font size.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  float          fnt_sz_flt       The parameter is the suptitle's updated font size.
 #  enum           chart_type       The parameter is the multichart type enumeration value.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_multichart_suptitle_fontsize(fnt_sz_flt, chart_type):

    if chart_type == chart_enum.MULTIBAR.value:

        global bar_multichart_dict

        bar_multichart_dict['suptitle']['fontproperties']['size'] = fnt_sz_flt

    elif chart_type == chart_enum.MULTIBOXPLOT.value:

        global boxplot_multichart_dict

        boxplot_multichart_dict['suptitle']['fontproperties']['size'] = fnt_sz_flt

    elif chart_type == chart_enum.MULTIHISTOGRAM.value:

        global histogram_multichart_dict

        histogram_multichart_dict['suptitle']['fontproperties']['size'] = fnt_sz_flt

    elif chart_type == chart_enum.MULTILINE.value:

        global line_multichart_dict

        line_multichart_dict['suptitle']['fontproperties']['size'] = fnt_sz_flt

    elif chart_type == chart_enum.MULTIPIE.value:

        global pie_multichart_dict

        pie_multichart_dict['suptitle']['fontproperties']['size'] = fnt_sz_flt

    elif chart_type == chart_enum.MULTIPLOT.value:

        global plot_multichart_dict

        plot_multichart_dict['suptitle']['fontproperties']['size'] = fnt_sz_flt

    elif chart_type == chart_enum.MULTISCATTER.value:

        global scatterplot_multichart_dict

        scatterplot_multichart_dict['suptitle']['fontproperties']['size'] = fnt_sz_flt


# In[80]:


#*******************************************************************************************
 #
 #  Function Name:  set_multichart_supxlabel_fontsize
 #
 #  Function Description:
 #      The function sets the multichart supxlabel's font size.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  float          fnt_sz_flt       The parameter is the supxlabel's updated font size.
 #  enum           chart_type       The parameter is the multichart type enumeration value.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_multichart_supxlabel_fontsize(fnt_sz_flt, chart_type):

    if chart_type == chart_enum.MULTIBAR.value:

        global bar_multichart_dict

        bar_multichart_dict['supxlabel']['fontproperties']['size'] = fnt_sz_flt

    elif chart_type == chart_enum.MULTIBOXPLOT.value:

        global boxplot_multichart_dict

        boxplot_multichart_dict['supxlabel']['fontproperties']['size'] = fnt_sz_flt

    elif chart_type == chart_enum.MULTIHISTOGRAM.value:

        global histogram_multichart_dict

        histogram_multichart_dict['supxlabel']['fontproperties']['size'] = fnt_sz_flt

    elif chart_type == chart_enum.MULTILINE.value:

        global line_multichart_dict

        line_multichart_dict['supxlabel']['fontproperties']['size'] = fnt_sz_flt

    elif chart_type == chart_enum.MULTIPIE.value:

        global pie_multichart_dict

        pie_multichart_dict['supxlabel']['fontproperties']['size'] = fnt_sz_flt

    elif chart_type == chart_enum.MULTIPLOT.value:

        global plot_multichart_dict

        plot_multichart_dict['supxlabel']['fontproperties']['size'] = fnt_sz_flt

    elif chart_type == chart_enum.MULTISCATTER.value:

        global scatterplot_multichart_dict

        scatterplot_multichart_dict['supxlabel']['fontproperties']['size'] = fnt_sz_flt


# In[81]:


#*******************************************************************************************
 #
 #  Function Name:  set_multichart_supylabel_fontsize
 #
 #  Function Description:
 #      The function sets the multichart supylabel's font size.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  float          fnt_sz_flt       The parameter is the supylabel's updated font size.
 #  enum           chart_type       The parameter is the multichart type enumeration value.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_multichart_supylabel_fontsize(fnt_sz_flt, chart_type):

    if chart_type == chart_enum.MULTIBAR.value:

        global bar_multichart_dict

        bar_multichart_dict['supylabel']['fontproperties']['size'] = fnt_sz_flt

    elif chart_type == chart_enum.MULTIBOXPLOT.value:

        global boxplot_multichart_dict

        boxplot_multichart_dict['supylabel']['fontproperties']['size'] = fnt_sz_flt

    elif chart_type == chart_enum.MULTIHISTOGRAM.value:

        global histogram_multichart_dict

        histogram_multichart_dict['supylabel']['fontproperties']['size'] = fnt_sz_flt

    elif chart_type == chart_enum.MULTILINE.value:

        global line_multichart_dict

        line_multichart_dict['supylabel']['fontproperties']['size'] = fnt_sz_flt

    elif chart_type == chart_enum.MULTIPIE.value:

        global pie_multichart_dict

        pie_multichart_dict['supylabel']['fontproperties']['size'] = fnt_sz_flt

    elif chart_type == chart_enum.MULTIPLOT.value:

        global plot_multichart_dict

        plot_multichart_dict['supylabel']['fontproperties']['size'] = fnt_sz_flt

    elif chart_type == chart_enum.MULTISCATTER.value:

        global scatterplot_multichart_dict

        scatterplot_multichart_dict['supylabel']['fontproperties']['size'] = fnt_sz_flt


# In[82]:


#*******************************************************************************************
 #
 #  Function Name:  set_multichart_xysuplabels
 #
 #  Function Description:
 #      The function sets the multichart's x-axis suplabel and y-axis suplabel.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  string         xsuplabel        The parameter is the chart's x-axis suplabel.
 #  string         ysuplabel        The parameter is the chart's y-axis suplabel.
 #  enum           chart_type       The parameter is the multichart type enumeration value.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_multichart_xysuplabels(xsuplabel, ysuplabel, chart_type):

    if chart_type == chart_enum.MULTIBAR.value:

        global bar_multichart_dict

        bar_multichart_dict['supxlabel']['text'] = xsuplabel
        bar_multichart_dict['supylabel']['text'] = ysuplabel

    elif chart_type == chart_enum.MULTIBOXPLOT.value:

        global boxplot_multichart_dict

        boxplot_multichart_dict['supxlabel']['text'] = xsuplabel
        boxplot_multichart_dict['supylabel']['text'] = ysuplabel

    elif chart_type == chart_enum.MULTIHISTOGRAM.value:

        global histogram_multichart_dict

        histogram_multichart_dict['supxlabel']['text'] = xsuplabel
        histogram_multichart_dict['supylabel']['text'] = ysuplabel

    elif chart_type == chart_enum.MULTILINE.value:

        global line_multichart_dict

        line_multichart_dict['supxlabel']['text'] = xsuplabel
        line_multichart_dict['supylabel']['text'] = ysuplabel

    elif chart_type == chart_enum.MULTIPIE.value:

        global pie_multichart_dict

        pie_multichart_dict['supxlabel']['text'] = xsuplabel
        pie_multichart_dict['supylabel']['text'] = ysuplabel

    elif chart_type == chart_enum.MULTIPLOT.value:

        global plot_multichart_dict

        plot_multichart_dict['supxlabel']['text'] = xsuplabel
        plot_multichart_dict['supylabel']['text'] = ysuplabel

    elif chart_type == chart_enum.MULTISCATTER.value:

        global scatterplot_multichart_dict

        scatterplot_multichart_dict['supxlabel']['text'] = xsuplabel
        scatterplot_multichart_dict['supylabel']['text'] = ysuplabel


# In[83]:


#*******************************************************************************************
 #
 #  Function Name:  get_bar_chart_dict
 #                  get_boxplot_chart_dict
 #                  get_histogram_chart_dict
 #                  get_line_chart_dict
 #                  get_pie_chart_dict
 #                  get_plot_chart_dict
 #                  get_scatterplot_chart_dict
 #
 #                  get_regr_line_dict
 #                  get_corr_cv_dict
 #                  get_corr_scores_dict
 #                  get_window_cv_dict
 #                  get_roll_corr_dict
 #                  get_roll_corr_all_dict
 #                  get_lag_corr_dict
 #                  get_lag_heat_dict
 #                  
 #                  get_bar_multichart_dict
 #                  get_boxplot_multichart_dict
 #                  get_histogram_multichart_dict
 #                  get_line_multichart_dict
 #                  get_pie_multichart_dict
 #                  get_plot_multichart_dict
 #                  get_scatterplot_multichart_dict
 #
 #  Function Description:
 #      The function retrieves the global chart dictionary.
 #
 #
 #  Return Type: dictionary
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
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_bar_chart_dict(): return get_chart_dict(chart_enum.BAR.value)
def get_boxplot_chart_dict(): return get_chart_dict(chart_enum.BOXPLOT.value)
def get_histogram_chart_dict(): return get_chart_dict(chart_enum.HISTOGRAM.value)
def get_line_chart_dict(): return get_chart_dict(chart_enum.LINE.value)
def get_pie_chart_dict(): return get_chart_dict(chart_enum.PIE.value)
def get_plot_chart_dict(): return get_chart_dict(chart_enum.PLOT.value)
def get_scatterplot_chart_dict(): return get_chart_dict(chart_enum.SCATTER.value)

def get_regr_line_dict(): return get_chart_dict(chart_enum.REGR_LINE.value)
def get_corr_cv_dict(): return get_chart_dict(chart_enum.CORR_CV.value)
def get_corr_scores_dict(): return get_chart_dict(chart_enum.CORR_SCORES.value)
def get_window_cv_dict(): return get_chart_dict(chart_enum.WINDOW_CV.value)
def get_roll_corr_dict(): return get_chart_dict(chart_enum.ROLL_CORR.value)
def get_roll_corr_all_dict(): return get_chart_dict(chart_enum.ROLL_CORR_ALL.value)
def get_lag_corr_dict(): return get_chart_dict(chart_enum.LAG_CORR.value)
def get_lag_heat_dict(): return get_chart_dict(chart_enum.LAG_HEAT.value)

def get_bar_multichart_dict(): return get_chart_dict(chart_enum.MULTIBAR.value)
def get_boxplot_multichart_dict(): return get_chart_dict(chart_enum.MULTIBOXPLOT.value)
def get_histogram_multichart_dict(): return get_chart_dict(chart_enum.MULTIHISTOGRAM.value)
def get_line_multichart_dict(): return get_chart_dict(chart_enum.MULTILINE.value)
def get_pie_multichart_dict(): return get_chart_dict(chart_enum.MULTIPIE.value)
def get_plot_multichart_dict(): return get_chart_dict(chart_enum.MULTIPLOT.value)
def get_scatterplot_multichart_dict(): return get_chart_dict(chart_enum.MULTISCATTER.value)


# In[84]:


#*******************************************************************************************
 #
 #  Function Name:  set_bar_chart_dict
 #                  set_boxplot_chart_dict
 #                  set_histogram_chart_dict
 #                  set_line_chart_dict
 #                  set_pie_chart_dict
 #                  set_plot_chart_dict
 #                  set_scatterplot_chart_dict
 #
 #                  set_regr_line_dict
 #                  set_corr_cv_dict
 #                  set_corr_scores_dict
 #                  set_window_cv_dict
 #                  set_roll_corr_dict
 #                  set_roll_corr_all_dict
 #                  set_lag_corr_dict
 #                  set_lag_heat_dict
 #
 #                  set_bar_multichart_dict
 #                  set_boxplot_multichart_dict
 #                  set_histogram_multichart_dict
 #                  set_line_multichart_dict
 #                  set_pie_multichart_dict
 #                  set_plot_multichart_dict
 #                  set_scatterplot_multichart_dict
 #
 #  Function Description:
 #      The function sets the global chart dictionary.
 #
 #
 #  Return Type: dictionary
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  dictionary     upd_dict         The parameter is the updated bar chart dictionary. 
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_bar_chart_dict(upd_dict): set_chart_dict(upd_dict, chart_enum.BAR.value)
def set_boxplot_chart_dict(upd_dict): set_chart_dict(upd_dict, chart_enum.BOXPLOT.value)
def set_histogram_chart_dict(upd_dict): set_chart_dict(upd_dict, chart_enum.HISTOGRAM.value)
def set_line_chart_dict(upd_dict): set_chart_dict(upd_dict, chart_enum.LINE.value)
def set_pie_chart_dict(upd_dict): set_chart_dict(upd_dict, chart_enum.PIE.value)
def set_plot_chart_dict(upd_dict): set_chart_dict(upd_dict, chart_enum.PLOT.value)
def set_scatterplot_chart_dict(upd_dict): set_chart_dict(upd_dict, chart_enum.SCATTER.value)

def set_regr_line_dict(upd_dict): set_chart_dict(upd_dict, chart_enum.REGR_LINE.value)
def set_corr_cv_dict(upd_dict): set_chart_dict(upd_dict, chart_enum.CORR_CV.value)
def set_corr_scores_dict(upd_dict): set_chart_dict(upd_dict, chart_enum.CORR_SCORES.value)
def set_window_cv_dict(upd_dict): set_chart_dict(upd_dict, chart_enum.WINDOW_CV.value)
def set_roll_corr_dict(upd_dict): set_chart_dict(upd_dict, chart_enum.ROLL_CORR.value)
def set_roll_corr_all_dict(upd_dict): set_chart_dict(upd_dict, chart_enum.ROLL_CORR_ALL.value)
def set_lag_corr_dict(upd_dict): set_chart_dict(upd_dict, chart_enum.LAG_CORR.value)
def set_lag_heat_dict(upd_dict): set_chart_dict(upd_dict, chart_enum.LAG_HEAT.value)

def set_bar_multichart_dict(upd_dict): set_chart_dict(upd_dict, chart_enum.MULTIBAR.value)
def set_boxplot_multichart_dict(upd_dict): set_chart_dict(upd_dict, chart_enum.MULTIBOXPLOT.value)
def set_histogram_multichart_dict(upd_dict): set_chart_dict(upd_dict, chart_enum.MULTIHISTOGRAM.value)
def set_line_multichart_dict(upd_dict): set_chart_dict(upd_dict, chart_enum.MULTILINE.value)
def set_pie_multichart_dict(upd_dict): set_chart_dict(upd_dict, chart_enum.MULTIPIE.value)
def set_plot_multichart_dict(upd_dict): set_chart_dict(upd_dict, chart_enum.MULTIPLOT.value)
def set_scatterplot_multichart_dict(upd_dict): set_chart_dict(upd_dict, chart_enum.MULTISCATTER.value)


# In[85]:


#*******************************************************************************************
 #
 #  Function Name:  get_bar_chart_def_dict
 #                  get_boxplot_chart_def_dict
 #                  get_histogram_chart_def_dict
 #                  get_line_chart_def_dict
 #                  get_pie_chart_def_dict
 #                  get_plot_chart_def_dict
 #                  get_scatterplot_chart_def_dict
 #
 #                  get_regr_line_def_dict
 #                  get_corr_cv_def_dict
 #                  get_corr_scores_def_dict
 #                  get_window_cv_def_dict
 #                  get_roll_corr_def_dict
 #                  get_roll_corr_all_def_dict
 #                  get_lag_corr_def_dict
 #                  get_lag_heat_def_dict
 #
 #                  get_bar_multichart_def_dict
 #                  get_boxplot_multichart_def_dict
 #                  get_histogram_multichart_def_dict
 #                  get_line_multichart_def_dict
 #                  get_pie_multichart_def_dict
 #                  get_plot_multichart_def_dict
 #                  get_scatterplot_multichart_def_dict
 #
 #  Function Description:
 #      The function retrieves the global chart default dictionary.
 #
 #
 #  Return Type: dictionary
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
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_bar_chart_def_dict(): return get_chart_def_dict(chart_enum.BAR.value)
def get_boxplot_chart_def_dict(): return get_chart_def_dict(chart_enum.BOXPLOT.value)
def get_histogram_chart_def_dict(): return get_chart_def_dict(chart_enum.HISTOGRAM.value)
def get_line_chart_def_dict(): return get_chart_def_dict(chart_enum.LINE.value)
def get_pie_chart_def_dict(): return get_chart_def_dict(chart_enum.PIE.value)
def get_plot_chart_def_dict(): return get_chart_def_dict(chart_enum.PLOT.value)
def get_scatterplot_chart_def_dict(): return get_chart_def_dict(chart_enum.SCATTER.value)

def get_regr_line_def_dict(): return get_chart_def_dict(chart_enum.REGR_LINE.value)
def get_corr_cv_def_dict(): return get_chart_def_dict(chart_enum.CORR_CV.value)
def get_corr_scores_def_dict(): return get_chart_def_dict(chart_enum.CORR_SCORES.value)
def get_window_cv_def_dict(): return get_chart_def_dict(chart_enum.WINDOW_CV.value)
def get_roll_corr_def_dict(): return get_chart_def_dict(chart_enum.ROLL_CORR.value)
def get_roll_corr_all_def_dict(): return get_chart_def_dict(chart_enum.ROLL_CORR_ALL.value)
def get_lag_corr_def_dict(): return get_chart_def_dict(chart_enum.LAG_CORR.value)
def get_lag_heat_def_dict(): return get_chart_def_dict(chart_enum.LAG_HEAT.value)

def get_bar_multichart_def_dict(): return get_chart_def_dict(chart_enum.MULTIBAR.value)
def get_boxplot_multichart_def_dict(): return get_chart_def_dict(chart_enum.MULTIBOXPLOT.value)
def get_histogram_multichart_def_dict(): return get_chart_def_dict(chart_enum.MULTIHISTOGRAM.value)
def get_line_multichart_def_dict(): return get_chart_def_dict(chart_enum.MULTILINE.value)
def get_pie_multichart_def_dict(): return get_chart_def_dict(chart_enum.MULTIPIE.value)
def get_plot_multichart_def_dict(): return get_chart_def_dict(chart_enum.MULTIPLOT.value)
def get_scatterplot_multichart_def_dict(): return get_chart_def_dict(chart_enum.MULTISCATTER.value)


# In[86]:


#*******************************************************************************************
 #
 #  Function Name:  set_bar_chart_def_dict
 #                  set_boxplot_chart_def_dict
 #                  set_histogram_chart_def_dict
 #                  set_line_chart_def_dict
 #                  set_pie_chart_def_dict
 #                  set_plot_chart_def_dict
 #                  set_scatterplot_chart_def_dict
 #
 #                  set_regr_line_def_dict
 #                  set_corr_cv_def_dict
 #                  set_corr_scores_def_dict
 #                  set_window_cv_def_dict
 #                  set_roll_corr_def_dict
 #                  set_roll_corr_all_def_dict
 #                  set_lag_corr_def_dict
 #                  set_lag_heat_def_dict
 #
 #                  set_bar_multichart_def_dict
 #                  set_boxplot_multichart_def_dict
 #                  set_histogram_multichart_def_dict
 #                  set_line_multichart_def_dict
 #                  set_pie_multichart_def_dict
 #                  set_plot_multichart_def_dict
 #                  set_scatterplot_multichart_def_dict
 #
 #  Function Description:
 #      The function sets the global chart dictionary with default values.
 #
 #
 #  Return Type: dictionary
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  dictionary     upd_dict         The parameter is the updated bar chart dictionary. 
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_bar_chart_def_dict(upd_dict): set_chart_def_dict(upd_dict, chart_enum.BAR.value)
def set_boxplot_chart_def_dict(upd_dict): set_chart_def_dict(upd_dict, chart_enum.BOXPLOT.value)
def set_histogram_chart_def_dict(upd_dict): set_chart_def_dict(upd_dict, chart_enum.HISTOGRAM.value)
def set_line_chart_def_dict(upd_dict): set_chart_def_dict(upd_dict, chart_enum.LINE.value)
def set_pie_chart_def_dict(upd_dict): set_chart_def_dict(upd_dict, chart_enum.PIE.value)
def set_plot_chart_def_dict(upd_dict): set_chart_def_dict(upd_dict, chart_enum.PLOT.value)
def set_scatterplot_chart_def_dict(upd_dict): set_chart_def_dict(upd_dict, chart_enum.SCATTER.value)

def set_regr_line_def_dict(upd_dict): set_chart_def_dict(upd_dict, chart_enum.REGR_LINE.value)
def set_corr_cv_def_dict(upd_dict): set_chart_def_dict(upd_dict, chart_enum.CORR_CV.value)
def set_corr_scores_def_dict(upd_dict): set_chart_def_dict(upd_dict, chart_enum.CORR_SCORES.value)
def set_window_cv_def_dict(upd_dict): set_chart_def_dict(upd_dict, chart_enum.WINDOW_CV.value)
def set_roll_corr_def_dict(upd_dict): set_chart_def_dict(upd_dict, chart_enum.ROLL_CORR.value)
def set_roll_corr_all_def_dict(upd_dict): set_chart_def_dict(upd_dict, chart_enum.ROLL_CORR_ALL.value)
def set_lag_corr_def_dict(upd_dict): set_chart_def_dict(upd_dict, chart_enum.LAG_CORR.value)
def set_lag_heat_def_dict(upd_dict): set_chart_def_dict(upd_dict, chart_enum.LAG_HEAT.value)

def set_bar_multichart_def_dict(upd_dict): set_chart_def_dict(upd_dict, chart_enum.MULTIBAR.value)
def set_boxplot_multichart_def_dict(upd_dict): set_chart_def_dict(upd_dict, chart_enum.MULTIBOXPLOT.value)
def set_histogram_multichart_def_dict(upd_dict): set_chart_def_dict(upd_dict, chart_enum.MULTIHISTOGRAM.value)
def set_line_multichart_def_dict(upd_dict): set_chart_def_dict(upd_dict, chart_enum.MULTILINE.value)
def set_pie_multichart_def_dict(upd_dict): set_chart_def_dict(upd_dict, chart_enum.MULTIPIE.value)
def set_plot_multichart_def_dict(upd_dict): set_chart_def_dict(upd_dict, chart_enum.MULTIPLOT.value)
def set_scatterplot_multichart_def_dict(upd_dict): set_chart_def_dict(upd_dict, chart_enum.MULTISCATTER.value)


# In[87]:


#*******************************************************************************************
 #
 #  Function Name:  get_bar_chart_title
 #                  get_boxplot_chart_title
 #                  get_histogram_chart_title
 #                  get_line_chart_title
 #                  get_pie_chart_title
 #                  get_plot_chart_title
 #                  get_scatterplot_chart_title
 #
 #                  get_corr_cv_title
 #                  get_corr_scores_title
 #                  get_window_cv_title
 #                  get_roll_corr_title
 #                  get_roll_corr_all_title
 #                  get_lag_corr_title
 #                  get_lag_heat_title
 #
 #  Function Description:
 #      The function retrieves the chart's titles.
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
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_bar_chart_title(): return get_title(chart_enum.BAR.value)
def get_boxplot_chart_title(): return get_title(chart_enum.BOXPLOT.value)
def get_histogram_chart_title(): return get_title(chart_enum.HISTOGRAM.value)
def get_line_chart_title(): return get_title(chart_enum.LINE.value)
def get_pie_chart_title(): return get_title(chart_enum.PIE.value)
def get_plot_chart_title(): return get_title(chart_enum.PLOT.value)
def get_scatterplot_chart_title(): return get_title(chart_enum.SCATTER.value)

def get_corr_cv_title(): return get_title(chart_enum.CORR_CV.value)
def get_corr_scores_title(): return get_title(chart_enum.CORR_SCORES.value)
def get_window_cv_title(): return get_title(chart_enum.WINDOW_CV.value)
def get_roll_corr_title(): return get_title(chart_enum.ROLL_CORR.value)
def get_roll_corr_all_title(): return get_title(chart_enum.ROLL_CORR_ALL.value)
def get_lag_corr_title(): return get_title(chart_enum.LAG_CORR.value)
def get_lag_heat_title(): return get_title(chart_enum.LAG_HEAT.value)


# In[88]:


#*******************************************************************************************
 #
 #  Function Name:  set_bar_chart_title
 #                  set_boxplot_chart_title
 #                  set_histogram_chart_title
 #                  set_line_chart_title
 #                  set_pie_chart_title
 #                  set_plot_chart_title
 #                  set_scatterplot_chart_title
 #
 #                  set_corr_cv_title
 #                  set_corr_scores_title
 #                  set_window_cv_title
 #                  set_roll_corr_title
 #                  set_roll_corr_all_title
 #                  set_lag_corr_title
 #                  set_lag_heat_title
 #
 #  Function Description:
 #      The function sets the chart's titles.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  string         titles           The parameter is the chart's titles.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_bar_chart_title(titles): set_title(titles, chart_enum.BAR.value)
def set_boxplot_chart_title(titles): set_title(titles, chart_enum.BOXPLOT.value)
def set_histogram_chart_title(titles): set_title(titles, chart_enum.HISTOGRAM.value)
def set_line_chart_title(titles): set_title(titles, chart_enum.LINE.value)
def set_pie_chart_title(titles): set_title(titles, chart_enum.PIE.value)
def set_plot_chart_title(titles): set_title(titles, chart_enum.PLOT.value)
def set_scatterplot_chart_title(titles): set_title(titles, chart_enum.SCATTER.value)

def set_corr_cv_title(titles): set_title(titles, chart_enum.CORR_CV.value)
def set_corr_scores_title(titles): set_title(titles, chart_enum.CORR_SCORES.value)
def set_window_cv_title(titles): set_title(titles, chart_enum.WINDOW_CV.value)
def set_roll_corr_title(titles): set_title(titles, chart_enum.ROLL_CORR.value)
def set_roll_corr_all_title(titles): set_title(titles, chart_enum.ROLL_CORR_ALL.value)
def set_lag_corr_title(titles): set_title(titles, chart_enum.LAG_CORR.value)
def set_lag_heat_title(titles): set_title(titles, chart_enum.LAG_HEAT.value)


# In[89]:


#*******************************************************************************************
 #
 #  Function Name:  get_bar_chart_title_display
 #                  get_boxplot_chart_title_display
 #                  get_histogram_chart_title_display
 #                  get_line_chart_title_display
 #                  get_pie_chart_title_display
 #                  get_plot_chart_title_display
 #                  get_scatterplot_chart_title_display
 #
 #                  get_corr_cv_title_display
 #                  get_corr_scores_title_display
 #                  get_window_cv_title_display
 #                  get_roll_corr_title_display
 #                  get_roll_corr_all_title_display
 #                  get_lag_corr_title_display
 #                  get_lag_heat_title_display
 #
 #  Function Description:
 #      The function retrieves the chart's title display indicator.
 #
 #
 #  Return Type: boolean
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
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_bar_chart_title_display(): return get_title_display(chart_enum.BAR.value)
def get_boxplot_chart_title_display(): return get_title_display(chart_enum.BOXPLOT.value)
def get_histogram_chart_title_display(): return get_title_display(chart_enum.HISTOGRAM.value)
def get_line_chart_title_display(): return get_title_display(chart_enum.LINE.value)
def get_pie_chart_title_display(): return get_title_display(chart_enum.PIE.value)
def get_plot_chart_title_display(): return get_title_display(chart_enum.PLOT.value)
def get_scatterplot_chart_title_display(): return get_title_display(chart_enum.SCATTER.value)

def get_corr_cv_title_display(): return get_title_display(chart_enum.CORR_CV.value)
def get_corr_scores_title_display(): return get_title_display(chart_enum.CORR_SCORES.value)
def get_window_cv_title_display(): return get_title_display(chart_enum.WINDOW_CV.value)
def get_roll_corr_title_display(): return get_title_display(chart_enum.ROLL_CORR.value)
def get_roll_corr_all_title_display(): return get_title_display(chart_enum.ROLL_CORR_ALL.value)
def get_lag_corr_title_display(): return get_title_display(chart_enum.LAG_CORR.value)
def get_lag_heat_title_display(): return get_title_display(chart_enum.LAG_HEAT.value)


# In[90]:


#*******************************************************************************************
 #
 #  Function Name:  set_bar_chart_title_display
 #                  set_boxplot_chart_title_display
 #                  set_histogram_chart_title_display
 #                  set_line_chart_title_display
 #                  set_pie_chart_title_display
 #                  set_plot_chart_title_display
 #                  set_scatterplot_chart_title_display
 #
 #                  set_corr_cv_title_display
 #                  set_corr_scores_title_display
 #                  set_window_cv_title_display
 #                  set_roll_corr_title_display
 #                  set_roll_corr_all_title_display
 #                  set_lag_corr_title_display
 #                  set_lag_heat_title_display
 #
 #  Function Description:
 #      The function sets the chart's title display indicator.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  boolean        upd_bool         The parameter is the chart title's display indicator.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_bar_chart_title_display(upd_bool): set_title_display(upd_bool, chart_enum.BAR.value)
def set_boxplot_chart_title_display(upd_bool): set_title_display(upd_bool, chart_enum.BOXPLOT.value)
def set_histogram_chart_title__display(upd_bool): set_title_display(upd_bool, chart_enum.HISTOGRAM.value)
def set_line_chart_title_display(upd_bool): set_title_display(upd_bool, chart_enum.LINE.value)
def set_pie_chart_title_display(upd_bool): set_title_display(upd_bool, chart_enum.PIE.value)
def set_plot_chart_title_display(upd_bool): set_title_display(upd_bool, chart_enum.PLOT.value)
def set_scatterplot_chart_title_display(upd_bool): set_title_display(upd_bool, chart_enum.SCATTER.value)

def set_corr_cv_title_display(upd_bool): set_title_display(upd_bool, chart_enum.CORR_CV.value)
def set_corr_scores_title_display(upd_bool): set_title_display(upd_bool, chart_enum.CORR_SCORES.value)
def set_window_cv_title_display(upd_bool): set_title_display(upd_bool, chart_enum.WINDOW_CV.value)
def set_roll_corr_title_display(upd_bool): set_title_display(upd_bool, chart_enum.ROLL_CORR.value)
def set_roll_corr_all_title_display(upd_bool): set_title_display(upd_bool, chart_enum.ROLL_CORR_ALL.value)
def set_lag_corr_title_display(upd_bool): set_title_display(upd_bool, chart_enum.LAG_CORR.value)
def set_lag_heat_title_display(upd_bool): set_title_display(upd_bool, chart_enum.LAG_HEAT.value)


# In[91]:


#*******************************************************************************************
 #
 #  Function Name:  get_bar_chart_title_fontsize
 #                  get_boxplot_chart_title_fontsize
 #                  get_histogram_chart_title_fontsize
 #                  get_line_chart_title_fontsize
 #                  get_pie_chart_title_fontsize
 #                  get_plot_chart_title_fontsize
 #                  get_scatterplot_chart_title_fontsize
 #
 #                  get_corr_cv_title_fontsize
 #                  get_corr_scores_title_fontsize
 #                  get_window_cv_title_fontsize
 #                  get_roll_corr_title_fontsize
 #                  get_roll_corr_all_title_fontsize
 #                  get_lag_corr_title_fontsize
 #                  get_lag_heat_title_fontsize
 #
 #  Function Description:
 #      The function retrieves the chart's title font size.
 #
 #
 #  Return Type: float
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
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_bar_chart_title_fontsize(): return get_title_fontsize(chart_enum.BAR.value)
def get_boxplot_chart_title_fontsize(): return get_title_fontsize(chart_enum.BOXPLOT.value)
def get_histogram_chart_title_fontsize(): return get_title_fontsize(chart_enum.HISTOGRAM.value)
def get_line_chart_title_fontsize(): return get_title_fontsize(chart_enum.LINE.value)
def get_pie_chart_title_fontsize(): return get_title_fontsize(chart_enum.PIE.value)
def get_plot_chart_title_fontsize(): return get_title_fontsize(chart_enum.PLOT.value)
def get_scatterplot_chart_title_fontsize(): return get_title_fontsize(chart_enum.SCATTER.value)

def get_corr_cv_title_fontsize(): return get_title_fontsize(chart_enum.CORR_CV.value)
def get_corr_scores_title_fontsize(): return get_title_fontsize(chart_enum.CORR_SCORES.value)
def get_window_cv_title_fontsize(): return get_title_fontsize(chart_enum.WINDOW_CV.value)
def get_roll_corr_title_fontsize(): return get_title_fontsize(chart_enum.ROLL_CORR.value)
def get_roll_corr_all_title_fontsize(): return get_title_fontsize(chart_enum.ROLL_CORR_ALL.value)
def get_lag_corr_title_fontsize(): return get_title_fontsize(chart_enum.LAG_CORR.value)
def get_lag_heat_title_fontsize(): return get_title_fontsize(chart_enum.LAG_HEAT.value)


# In[92]:


#*******************************************************************************************
 #
 #  Function Name:  set_bar_chart_title_fontsize
 #                  set_boxplot_chart_title_fontsize
 #                  set_histogram_chart_title_fontsize
 #                  set_line_chart_title_fontsize
 #                  set_pie_chart_title_fontsize
 #                  set_plot_chart_title_fontsize
 #                  set_scatterplot_chart_title_fontsize
 #
 #                  set_corr_cv_title_fontsize
 #                  set_corr_scores_title_fontsize
 #                  set_window_cv_title_fontsize
 #                  set_roll_corr_title_fontsize
 #                  set_roll_corr_all_title_fontsize
 #                  set_lag_corr_title_fontsize
 #                  set_lag_heat_title_fontsize
 #
 #  Function Description:
 #      The function sets the chart's title font size.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  float          size_flt         The parameter is the chart's title font size.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_bar_chart_title_fontsize(size_flt): set_title_fontsize(size_flt, chart_enum.BAR.value)
def set_boxplot_chart_title_fontsize(size_flt): set_title_fontsize(size_flt, chart_enum.BOXPLOT.value)
def set_histogram_chart_title_fontsize(size_flt): set_title_fontsize(size_flt, chart_enum.HISTOGRAM.value)
def set_line_chart_title_fontsize(size_flt): set_title_fontsize(size_flt, chart_enum.LINE.value)
def set_pie_chart_title_fontsize(size_flt): set_title_fontsize(size_flt, chart_enum.PIE.value)
def set_plot_chart_title_fontsize(size_flt): set_title_fontsize(size_flt, chart_enum.PLOT.value)
def set_scatterplot_chart_title_fontsize(size_flt): set_title_fontsize(size_flt, chart_enum.SCATTER.value)

def set_corr_cv_title_fontsize(size_flt): set_title_fontsize(size_flt, chart_enum.CORR_CV.value)
def set_corr_scores_title_fontsize(size_flt): set_title_fontsize(size_flt, chart_enum.CORR_SCORES.value)
def set_window_cv_title_fontsize(size_flt): set_title_fontsize(size_flt, chart_enum.WINDOW_CV.value)
def set_roll_corr_title_fontsize(size_flt): set_title_fontsize(size_flt, chart_enum.ROLL_CORR.value)
def set_roll_corr_all_title_fontsize(size_flt): set_title_fontsize(size_flt, chart_enum.ROLL_CORR_ALL.value)
def set_lag_corr_title_fontsize(size_flt): set_title_fontsize(size_flt, chart_enum.LAG_CORR.value)
def set_lag_heat_title_fontsize(size_flt): set_title_fontsize(size_flt, chart_enum.LAG_HEAT.value)


# In[93]:


#*******************************************************************************************
 #
 #  Function Name:  get_bar_chart_title_pad
 #                  get_boxplot_chart_title_pad
 #                  get_histogram_chart_title_pad
 #                  get_line_chart_title_pad
 #                  get_pie_chart_title_pad
 #                  get_plot_chart_title_pad
 #                  get_scatterplot_chart_title_pad
 #
 #                  get_corr_cv_title_pad
 #                  get_corr_scores_title_pad
 #                  get_window_cv_title_pad
 #                  get_roll_corr_title_pad
 #                  get_roll_corr_all_title_pad
 #                  get_lag_corr_title_pad
 #                  get_lag_heat_title_pad
 #
 #  Function Description:
 #      The function retrieves the chart's title pad.
 #
 #
 #  Return Type: float
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
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_bar_chart_title_pad(): return get_title_pad(chart_enum.BAR.value)
def get_boxplot_chart_title_pad(): return get_title_pad(chart_enum.BOXPLOT.value)
def get_histogram_chart_title_pad(): return get_title_pad(chart_enum.HISTOGRAM.value)
def get_line_chart_title_pad(): return get_title_pad(chart_enum.LINE.value)
def get_pie_chart_title_pad(): return get_title_pad(chart_enum.PIE.value)
def get_plot_chart_title_pad(): return get_title_pad(chart_enum.PLOT.value)
def get_scatterplot_chart_title_pad(): return get_title_pad(chart_enum.SCATTER.value)

def get_corr_cv_title_pad(): return get_title_pad(chart_enum.CORR_CV.value)
def get_window_cv_title_pad(): return get_title_pad(chart_enum.WINDOW_CV.value)
def get_roll_corr_title_pad(): return get_title_pad(chart_enum.ROLL_CORR.value)
def get_roll_corr_all_title_pad(): return get_title_pad(chart_enum.ROLL_CORR_ALL.value)
def get_lag_corr_title_pad(): return get_title_pad(chart_enum.LAG_CORR.value)
def get_lag_heat_title_pad(): return get_title_pad(chart_enum.LAG_HEAT.value)


# In[94]:


#*******************************************************************************************
 #
 #  Function Name:  set_bar_chart_title_pad
 #                  set_boxplot_chart_title_pad
 #                  set_histogram_chart_title_pad
 #                  set_line_chart_title_pad
 #                  set_pie_chart_title_pad
 #                  set_plot_chart_title_pad
 #                  set_scatterplot_chart_title_pad
 #
 #                  set_corr_cv_title_pad
 #                  set_corr_scores_title_pad
 #                  set_window_cv_title_pad
 #                  set_roll_corr_title_pad
 #                  set_roll_corr_all_title_pad
 #                  set_lag_corr_title_pad
 #                  set_lag_heat_title_pad
 #
 #  Function Description:
 #      The function sets the chart's title pad.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  float          pad_flt          The parameter is the chart's title pad.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_bar_chart_title_pad(pad_flt): set_title_pad(pad_flt, chart_enum.BAR.value)
def set_boxplot_chart_title_pad(pad_flt): set_title_pad(pad_flt, chart_enum.BOXPLOT.value)
def set_histogram_chart_title_pad(pad_flt): set_title_pad(pad_flt, chart_enum.HISTOGRAM.value)
def set_line_chart_title_pad(pad_flt): set_title_pad(pad_flt, chart_enum.LINE.value)
def set_pie_chart_title_pad(pad_flt): set_title_pad(pad_flt, chart_enum.PIE.value)
def set_plot_chart_title_pad(pad_flt): set_title_pad(pad_flt, chart_enum.PLOT.value)
def set_scatterplot_chart_title_pad(pad_flt): set_title_pad(pad_flt, chart_enum.SCATTER.value)

def set_corr_cv_title_pad(pad_flt): set_title_pad(pad_flt, chart_enum.CORR_CV.value)
def set_corr_scores_title_pad(pad_flt): set_title_pad(pad_flt, chart_enum.CORR_SCORES.value)
def set_window_cv_title_pad(pad_flt): set_title_pad(pad_flt, chart_enum.WINDOW_CV.value)
def set_roll_corr_title_pad(pad_flt): set_title_pad(pad_flt, chart_enum.ROLL_CORR.value)
def set_roll_corr_all_title_pad(pad_flt): set_title_pad(pad_flt, chart_enum.ROLL_CORR_ALL.value)
def set_lag_corr_title_pad(pad_flt): set_title_pad(pad_flt, chart_enum.LAG_CORR.value)
def set_lag_heat_title_pad(pad_flt): set_title_pad(pad_flt, chart_enum.LAG_HEAT.value)


# In[95]:


#*******************************************************************************************
 #
 #  Function Name:  get_bar_chart_xylabels
 #                  get_boxplot_chart_xylabels
 #                  get_histogram_chart_xylabels
 #                  get_line_chart_xylabels
 #                  get_pie_chart_xylabels
 #                  get_plot_chart_xylabels
 #                  get_scatterplot_chart_xylabels
 #
 #                  get_corr_cv_xylabels
 #                  get_corr_scores_xylabels
 #                  get_window_cv_xylabels
 #                  get_roll_corr_xylabels
 #                  get_roll_corr_all_xylabels
 #                  get_lag_corr_xylabels
 #                  get_lag_heat_xylabels
 #
 #  Function Description:
 #      The function retrieves the chart's x-axis label and y-axis label.
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
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_bar_chart_xylabels(): return get_xylabels(chart_enum.BAR.value)
def get_boxplot_chart_xylabels(): return get_xylabels(chart_enum.BOXPLOT.value)
def get_histogram_chart_xylabels(): return get_xylabels(chart_enum.HISTOGRAM.value)
def get_line_chart_xylabels(): return get_xylabels(chart_enum.LINE.value)
def get_pie_chart_xylabels(): return get_xylabels(chart_enum.PIE.value)
def get_plot_chart_xylabels(): return get_xylabels(chart_enum.PLOT.value)
def get_scatterplot_chart_xylabels(): return get_xylabels(chart_enum.SCATTER.value)

def get_corr_cv_xylabels(): return get_xylabels(chart_enum.CORR_CV.value)
def get_corr_scores_xylabels(): return get_xylabels(chart_enum.CORR_SCORES.value)
def get_window_cv_xylabels(): return get_xylabels(chart_enum.WINDOW_CV.value)
def get_roll_corr_xylabels(): return get_xylabels(chart_enum.ROLL_CORR.value)
def get_roll_corr_all_xylabels(): return get_xylabels(chart_enum.ROLL_CORR_ALL.value)
def get_lag_corr_xylabels(): return get_xylabels(chart_enum.LAG_CORR.value)
def get_lag_heat_xylabels(): return get_xylabels(chart_enum.LAG_HEAT.value)


# In[96]:


#*******************************************************************************************
 #
 #  Function Name:  set_bar_chart_xylabels
 #                  set_boxplot_chart_xylabels
 #                  set_histogram_chart_xylabels
 #                  set_line_chart_xylabels
 #                  set_pie_chart_xylabels
 #                  set_plot_chart_xylabels
 #                  set_scatterplot_chart_xylabels
 #
 #                  set_corr_cv_xylabels
 #                  set_corr_scores_xylabels
 #                  set_window_cv_xylabels
 #                  set_roll_corr_xylabels
 #                  set_roll_corr_all_xylabels
 #                  set_lag_corr_xylabels
 #                  set_lag_heat_xylabels
 #
 #  Function Description:
 #      The function sets the chart's x-axis label and y-axis label.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  string         xlabel           The parameter is the chart's x-axis label.
 #  string         ylabel           The parameter is the chart's y-axis label.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_bar_chart_xylabels(xlabel, ylabel): set_xylabels(xlabel, ylabel, chart_enum.BAR.value)
def set_boxplot_chart_xylabels(xlabel, ylabel): set_xylabels(xlabel, ylabel, chart_enum.BOXPLOT.value)
def set_histogram_chart_xylabels(xlabel, ylabel): set_xylabels(xlabel, ylabel, chart_enum.HISTOGRAM.value)
def set_line_chart_xylabels(xlabel, ylabel): set_xylabels(xlabel, ylabel, chart_enum.LINE.value)
def set_pie_chart_xylabels(xlabel, ylabel): set_xylabels(xlabel, ylabel, chart_enum.PIE.value)
def set_plot_chart_xylabels(xlabel, ylabel): set_xylabels(xlabel, ylabel, chart_enum.PLOT.value)   
def set_scatterplot_chart_xylabels(xlabel, ylabel): set_xylabels(xlabel, ylabel, chart_enum.SCATTER.value)

def set_corr_cv_xylabels(xlabel, ylabel): set_xylabels(xlabel, ylabel, chart_enum.CORR_CV.value)
def set_corr_scores_xylabels(xlabel, ylabel): set_xylabels(xlabel, ylabel, chart_enum.CORR_SCORES.value)
def set_window_cv_xylabels(xlabel, ylabel): set_xylabels(xlabel, ylabel, chart_enum.WINDOW_CV.value)
def set_roll_corr_xylabels(xlabel, ylabel): set_xylabels(xlabel, ylabel, chart_enum.ROLL_CORR.value)
def set_roll_corr_all_xylabels(xlabel, ylabel): set_xylabels(xlabel, ylabel, chart_enum.ROLL_CORR_ALL.value)
def set_lag_corr_xylabels(xlabel, ylabel): set_xylabels(xlabel, ylabel, chart_enum.LAG_CORR.value)
def set_lag_heat_xylabels(xlabel, ylabel): set_xylabels(xlabel, ylabel, chart_enum.LAG_HEAT.value)


# In[97]:


#*******************************************************************************************
 #
 #  Function Name:  get_bar_chart_xylabels_display
 #                  get_boxplot_chart_xylabels_display
 #                  get_histogram_chart_xylabels_display
 #                  get_line_chart_xylabels_display
 #                  get_pie_chart_xylabels_display
 #                  get_plot_chart_xylabels_display
 #                  get_scatterplot_chart_xylabels_display
 #
 #                  get_corr_cv_xylabels_display
 #                  get_corr_scores_xylabels_display
 #                  get_window_cv_xylabels_display
 #                  get_roll_corr_xylabels_display
 #                  get_roll_corr_all_xylabels_display
 #                  get_lag_corr_xylabels_display
 #                  get_lag_heat_xylabels_display
 #
 #  Function Description:
 #      The function retrieves the chart's x-axis label display and y-axis label display.
 #
 #
 #  Return Type: boolean, boolean
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
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_bar_chart_xylabels_display(): return get_xylabels_display(chart_enum.BAR.value)
def get_boxplot_chart_xylabels_display(): return get_xylabels_display(chart_enum.BOXPLOT.value)
def get_histogram_chart_xylabels_display(): return get_xylabels_display(chart_enum.HISTOGRAM.value)
def get_line_chart_xylabels_display(): return get_xylabels_display(chart_enum.LINE.value)
def get_pie_chart_xylabels_display(): return get_xylabels_display(chart_enum.PIE.value)
def get_plot_chart_xylabels_display(): return get_xylabels_display(chart_enum.PLOT.value)
def get_scatterplot_chart_xylabels_display(): return get_xylabels_display(chart_enum.SCATTER.value)

def get_corr_cv_xylabels_display(): return get_xylabels_display(chart_enum.CORR_CV.value)
def get_corr_scores_xylabels_display(): return get_xylabels_display(chart_enum.CORR_SCORES.value)
def get_window_cv_xylabels_display(): return get_xylabels_displays(chart_enum.WINDOW_CV.value)
def get_roll_corr_xylabels_display(): return get_xylabels_display(chart_enum.ROLL_CORR.value)
def get_roll_corr_all_xylabels_display(): return get_xylabels_display(chart_enum.ROLL_CORR_ALL.value)
def get_lag_corr_xylabels_display(): return get_xylabels_display(chart_enum.LAG_CORR.value)
def get_lag_heat_xylabels_display(): return get_xylabels_display(chart_enum.LAG_HEAT.value)


# In[98]:


#*******************************************************************************************
 #
 #  Function Name:  set_bar_chart_xylabels_display
 #                  set_boxplot_chart_xylabels_display
 #                  set_histogram_chart_xylabels_display
 #                  set_line_chart_xylabels_display
 #                  set_pie_chart_xylabels_display
 #                  set_plot_chart_xylabels_display
 #                  set_scatterplot_chart_xylabels_display
 #
 #                  set_corr_cv_xylabels_display
 #                  set_corr_scores_xylabels_display
 #                  set_window_cv_xylabels_display
 #                  set_roll_corr_xylabels_display
 #                  set_roll_corr_all_xylabels_display
 #                  set_lag_corr_xylabels_display
 #                  set_lag_heat_xylabels_display
 #
 #  Function Description:
 #      The function sets the chart's x-axis label display and y-axis label display.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  boolean        xdisp_bool       The parameter is the chart's x-axis label display.
 #  boolean        ydisp_bool       The parameter is the chart's y-axis label display.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_bar_chart_xylabels_display(xdisp_bool, ydisp_bool): set_xylabels_display(xdisp_bool, ydisp_bool, chart_enum.BAR.value)
def set_boxplot_chart_xylabels_display(xdisp_bool, ydisp_bool): set_xylabels_display(xdisp_bool, ydisp_bool, chart_enum.BOXPLOT.value)
def set_histogram_chart_xylabels_display(xdisp_bool, ydisp_bool): set_xylabels_display(xdisp_bool, ydisp_bool, chart_enum.HISTOGRAM.value)
def set_line_chart_xylabels_display(xdisp_bool, ydisp_bool): set_xylabels_display(xdisp_bool, ydisp_bool, chart_enum.LINE.value)
def set_pie_chart_xylabels_display(xdisp_bool, ydisp_bool): set_xylabels_display(xdisp_bool, ydisp_bool, chart_enum.PIE.value)
def set_plot_chart_xylabels_display(xdisp_bool, ydisp_bool): set_xylabels_display(xdisp_bool, ydisp_bool, chart_enum.PLOT.value)
def set_scatterplot_chart_xylabels_display(xdisp_bool, ydisp_bool): set_xylabels_display(xdisp_bool, ydisp_bool, chart_enum.SCATTER.value)

def set_corr_cv_xylabels_display(xdisp_bool, ydisp_bool): set_xylabels_display(xdisp_bool, ydisp_bool, chart_enum.CORR_CV.value)
def set_corr_scores_xylabels_display(xdisp_bool, ydisp_bool): set_xylabels_display(xdisp_bool, ydisp_bool, chart_enum.CORR_SCORES.value)
def set_window_cv_xylabels_display(xdisp_bool, ydisp_bool): set_xylabels_display(xdisp_bool, ydisp_bool, chart_enum.WINDOW_CV.value)
def set_roll_corr_xylabels_display(xdisp_bool, ydisp_bool): set_xylabels_display(xdisp_bool, ydisp_bool, chart_enum.ROLL_CORR.value)
def set_roll_corr_all_xylabels_display(xdisp_bool, ydisp_bool): set_xylabels_display(xdisp_bool, ydisp_bool, chart_enum.ROLL_CORR_ALL.value)
def set_lag_corr_xylabels_display(xdisp_bool, ydisp_bool): set_xylabels_display(xdisp_bool, ydisp_bool, chart_enum.LAG_CORR.value)
def set_lag_heat_xylabels_display(xdisp_bool, ydisp_bool): set_xylabels_display(xdisp_bool, ydisp_bool, chart_enum.LAG_HEAT.value)


# In[99]:


#*******************************************************************************************
 #
 #  Function Name:  get_bar_chart_xylabels_fontsize
 #                  get_boxplot_chart_xylabels_fontsize
 #                  get_histogram_chart_xylabels_fontsize
 #                  get_line_chart_xylabels_fontsize
 #                  get_pie_chart_xylabels_fontsize
 #                  get_plot_chart_xylabels_fontsize
 #                  get_scatterplot_chart_xylabels_fontsize
 #
 #                  get_corr_cv_xylabels_fontsize
 #                  get_corr_scores_xylabels_fontsize
 #                  get_window_cv_xylabels_fontsize
 #                  get_roll_corr_xylabels_fontsize
 #                  get_roll_corr_all_xylabels_fontsize
 #                  get_lag_corr_xylabels_fontsize
 #                  get_lag_heat_xylabels_fontsize
 #
 #  Function Description:
 #      The function retrieves the chart's x and y axes labels font sizes.
 #
 #
 #  Return Type: float, float
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
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_bar_chart_xylabels_fontsize(): return get_xylabels_fontsize(chart_enum.BAR.value)
def get_boxplot_chart_xylabels_fontsize(): return get_xylabels_fontsize(chart_enum.BOXPLOT.value)
def get_histogram_chart_xylabels_fontsize(): return get_xylabels_fontsize(chart_enum.HISTOGRAM.value)
def get_line_chart_xylabels_fontsize(): return get_xylabels_fontsize(chart_enum.LINE.value)
def get_pie_chart_xylabels_fontsize(): return get_xylabels_fontsize(chart_enum.PIE.value)
def get_plot_chart_xylabels_fontsize(): return get_xylabels_fontsize(chart_enum.PLOT.value)
def get_scatterplot_chart_xylabels_fontsize(): return get_xylabels_fontsize(chart_enum.SCATTER.value)

def get_corr_cv_xylabels_fontsize(): return get_xylabels_fontsize(chart_enum.CORR_CV.value)
def get_corr_scores_xylabels_fontsize(): return get_xylabels_fontsize(chart_enum.CORR_SCORES.value)
def get_window_cv_xylabels_fontsize(): return get_xylabels_fontsize(chart_enum.WINDOW_CV.value)
def get_roll_corr_xylabels_fontsize(): return get_xylabels_fontsize(chart_enum.ROLL_CORR.value)
def get_roll_corr_all_xylabels_fontsize(): return get_xylabels_fontsize(chart_enum.ROLL_CORR_ALL.value)
def get_lag_corr_xylabels_fontsize(): return get_xylabels_fontsize(chart_enum.LAG_CORR.value)
def get_lag_heat_xylabels_fontsize(): return get_xylabels_fontsize(chart_enum.LAG_HEAT.value)


# In[100]:


#*******************************************************************************************
 #
 #  Function Name:  set_bar_chart_xylabels_fontsize
 #                  set_boxplot_chart_xylabels_fontsize
 #                  set_histogram_chart_xylabels_fontsize
 #                  set_line_chart_xylabels_fontsize
 #                  set_pie_chart_xylabels_fontsize
 #                  set_plot_chart_xylabels_fontsize
 #                  set_scatterplot_chart_xylabels_fontsize
 #
 #                  set_corr_cv_xylabels_fontsize
 #                  set_corr_scores_xylabels_fontsize
 #                  set_window_cv_xylabels_fontsize
 #                  set_roll_corr_xylabels_fontsize
 #                  set_roll_corr_all_xylabels_fontsize
 #                  set_lag_corr_xylabels_fontsize
 #                  set_lag_heat_xylabels_fontsize
 #
 #  Function Description:
 #      The function sets the chart's x and y axes labels font sizes.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  float          xsize_flt         The parameter is the chart's x-axis label font size.
 #  float          ysize_flt         The parameter is the chart's y-axis label font size.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_bar_chart_xylabels_fontsize(xsize_flt, ysize_flt): set_xylabels_fontsize(xsize_flt, ysize_flt, chart_enum.BAR.value)
def set_boxplot_chart_xylabels_fontsize(xsize_flt, ysize_flt): set_xylabels_fontsize(xsize_flt, ysize_flt, chart_enum.BOXPLOT.value)
def set_histogram_chart_xylabels_fontsize(xsize_flt, ysize_flt): set_xylabels_fontsize(xsize_flt, ysize_flt, chart_enum.HISTOGRAM.value)
def set_line_chart_xylabels_fontsize(xsize_flt, ysize_flt): set_xylabels_fontsize(xsize_flt, ysize_flt, chart_enum.LINE.value)
def set_pie_chart_xylabels_fontsize(xsize_flt, ysize_flt): set_xylabels_fontsize(xsize_flt, ysize_flt, chart_enum.PIE.value)
def set_plot_chart_xylabels_fontsize(xsize_flt, ysize_flt): set_xylabels_fontsize(xsize_flt, ysize_flt, chart_enum.PLOT.value)
def set_scatterplot_chart_xylabels_fontsize(xsize_flt, ysize_flt): set_xylabels_fontsize(xsize_flt, ysize_flt, chart_enum.SCATTER.value)

def set_corr_cv_xylabels_fontsize(xsize_flt, ysize_flt): set_xylabels_fontsize(xsize_flt, ysize_flt, chart_enum.CORR_CV.value)
def set_corr_scores_xylabels_fontsize(xsize_flt, ysize_flt): set_xylabels_fontsize(xsize_flt, ysize_flt, chart_enum.CORR_SCORES.value)
def set_window_cv_xylabels_fontsize(xsize_flt, ysize_flt): set_xylabels_fontsize(xsize_flt, ysize_flt, chart_enum.WINDOW_CV.value)
def set_roll_corr_xylabels_fontsize(xsize_flt, ysize_flt): set_xylabels_fontsize(xsize_flt, ysize_flt, chart_enum.ROLL_CORR.value)
def set_roll_corr_all_xylabels_fontsize(xsize_flt, ysize_flt): set_xylabels_fontsize(xsize_flt, ysize_flt, chart_enum.ROLL_CORR_ALL.value)
def set_lag_corr_xylabels_fontsize(xsize_flt, ysize_flt): set_xylabels_fontsize(xsize_flt, ysize_flt, chart_enum.LAG_CORR.value)
def set_lag_heat_xylabels_fontsize(xsize_flt, ysize_flt): set_xylabels_fontsize(xsize_flt, ysize_flt, chart_enum.LAG_HEAT.value)


# In[101]:


#*******************************************************************************************
 #
 #  Function Name:  get_bar_chart_xylabels_pad
 #                  get_boxplot_chart_xylabels_pad
 #                  get_histogram_chart_xylabels_pad
 #                  get_line_chart_xylabels_pad
 #                  get_pie_chart_xylabels_pad
 #                  get_plot_chart_xylabels_pad
 #                  get_scatterplot_chart_xylabels_pad
 #
 #                  get_corr_cv_xylabels_pad
 #                  get_corr_scores_xylabels_pad
 #                  get_window_cv_xylabels_pad
 #                  get_roll_corr_xylabels_pad
 #                  get_roll_corr_all_xylabels_pad
 #                  get_lag_corr_xylabels_pad
 #                  get_lag_heat_xylabels_pad
 #
 #  Function Description:
 #      The function retrieves the chart's x and y axes labels pads.
 #
 #
 #  Return Type: float, float
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
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_bar_chart_xylabels_pad(): return get_xylabels_pad(chart_enum.BAR.value)
def get_boxplot_chart_xylabels_pad(): return get_xylabels_pad(chart_enum.BOXPLOT.value)
def get_histogram_chart_xylabels_pad(): return get_xylabels_pad(chart_enum.HISTOGRAM.value)
def get_line_chart_xylabels_pad(): return get_xylabels_pad(chart_enum.LINE.value)
def get_pie_chart_xylabels_pad(): return get_xylabels_pad(chart_enum.PIE.value)
def get_plot_chart_xylabels_pad(): return get_xylabels_pad(chart_enum.PLOT.value)
def get_scatterplot_chart_xylabels_pad(): return get_xylabels_pad(chart_enum.SCATTER.value)

def get_corr_cv_xylabels_pad(): return get_xylabels_pad(chart_enum.CORR_CV.value)
def get_corr_scores_xylabels_pad(): return get_xylabels_pad(chart_enum.CORR_SCORES.value)
def get_window_cv_xylabels_pad(): return get_xylabels_pad(chart_enum.WINDOW_CV.value)
def get_roll_corr_xylabels_pad(): return get_xylabels_pad(chart_enum.ROLL_CORR.value)
def get_roll_corr_all_xylabels_pad(): return get_xylabels_pad(chart_enum.ROLL_CORR_ALL.value)
def get_lag_corr_xylabels_pad(): return get_xylabels_pad(chart_enum.LAG_CORR.value)
def get_lag_heat_xylabels_pad(): return get_xylabels_pad(chart_enum.LAG_HEAT.value)


# In[102]:


#*******************************************************************************************
 #
 #  Function Name:  set_bar_chart_xylabels_pad
 #                  set_boxplot_chart_xylabels_pad
 #                  set_histogram_chart_xylabels_pad
 #                  set_line_chart_xylabels_pad
 #                  set_pie_chart_xylabels_pad
 #                  set_plot_chart_xylabels_pad
 #                  set_scatterplot_chart_xylabels_pad
 #
 #                  set_corr_cv_xylabels_pad
 #                  set_corr_scores_xylabels_pad
 #                  set_window_cv_xylabels_pad
 #                  set_roll_corr_xylabels_pad
 #                  set_roll_corr_al_xylabels_pad
 #                  set_lag_corr_xylabels_pad
 #                  set_lag_heat_xylabels_pad
 #
 #  Function Description:
 #      The function sets the chart's x and y axes labels pads.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  float          xpad_flt         The parameter is the chart's x-axis label pad.
 #  float          ypad_flt         The parameter is the chart's y-axis label pad.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_bar_chart_xylabels_pad(xpad_flt, ypad_flt): set_xylabels_pad(xpad_flt, ypad_flt, chart_enum.BAR.value)
def set_boxplot_chart_xylabels_pad(xpad_flt, ypad_flt): set_xylabels_pad(xpad_flt, ypad_flt, chart_enum.BOXPLOT.value)
def set_histogram_chart_xylabels_pad(xpad_flt, ypad_flt): set_xylabels_pad(xpad_flt, ypad_flt, chart_enum.HISTOGRAM.value)
def set_line_chart_xylabels_pad(xpad_flt, ypad_flt): set_xylabels_pad(xpad_flt, ypad_flt, chart_enum.LINE.value)
def set_pie_chart_xylabels_pad(xpad_flt, ypad_flt): set_xylabels_pad(xpad_flt, ypad_flt, chart_enum.PIE.value)
def set_plot_chart_xylabels_pad(xpad_flt, ypad_flt): set_xylabels_pad(xpad_flt, ypad_flt, chart_enum.PLOT.value)
def set_scatterplot_chart_xylabels_pad(xpad_flt, ypad_flt): set_xylabels_pad(xpad_flt, ypad_flt, chart_enum.SCATTER.value)

def set_corr_cv_xylabels_pad(xpad_flt, ypad_flt): set_xylabels_pad(xpad_flt, ypad_flt, chart_enum.CORR_CV.value)
def set_corr_scores_xylabels_pad(xpad_flt, ypad_flt): set_xylabels_pad(xpad_flt, ypad_flt, chart_enum.CORR_SCORES.value)
def set_window_cv_xylabels_pad(xpad_flt, ypad_flt): set_xylabels_pad(xpad_flt, ypad_flt, chart_enum.WINDOW_CV.value)
def set_roll_corr_xylabels_pad(xpad_flt, ypad_flt): set_xylabels_pad(xpad_flt, ypad_flt, chart_enum.ROLL_CORR.value)
def set_roll_corr_all_xylabels_pad(xpad_flt, ypad_flt): set_xylabels_pad(xpad_flt, ypad_flt, chart_enum.ROLL_CORR_ALL.value)
def set_lag_corr_xylabels_pad(xpad_flt, ypad_flt): set_xylabels_pad(xpad_flt, ypad_flt, chart_enum.LAG_CORR.value)
def set_lag_heat_xylabels_pad(xpad_flt, ypad_flt): set_xylabels_pad(xpad_flt, ypad_flt, chart_enum.LAG_HEAT.value)


# In[103]:


#*******************************************************************************************
 #
 #  Function Name:  get_bar_chart_xyticks_fontsize
 #                  get_boxplot_chart_xyticks_fontsize
 #                  get_histogram_chart_xyticks_fontsize
 #                  get_line_chart_xyticks_fontsize
 #                  get_pie_chart_xyticks_fontsize
 #                  get_plot_chart_xyticks_fontsize
 #                  get_scatterplot_chart_xyticks_fontsize
 #
 #                  get_corr_cv_xyticks_fontsize
 #                  get_corr_scores_xyticks_fontsize
 #                  get_window_cv_xyticks_fontsize
 #                  get_roll_corr_xyticks_fontsize
 #                  get_roll_corr_all_xyticks_fontsize
 #                  get_lag_corr_xyticks_fontsize
 #                  get_lag_heat_xyticks_fontsize
 #
 #  Function Description:
 #      The function retrieves the chart's x and y ticks labels font sizes.
 #
 #
 #  Return Type: float, float
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
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_bar_chart_xyticks_fontsize(): return get_xyticks_fontsize(chart_enum.BAR.value)
def get_boxplot_chart_xyticks_fontsize(): return get_xyticks_fontsize(chart_enum.BOXPLOT.value)
def get_histogram_chart_xyticks_fontsize(): return get_xyticks_fontsize(chart_enum.HISTOGRAM.value)
def get_line_chart_xyticks_fontsize(): return get_xyticks_fontsize(chart_enum.LINE.value)
def get_pie_chart_xyticks_fontsize(): return get_xyticks_fontsize(chart_enum.PIE.value)
def get_plot_chart_xyticks_fontsize(): return get_xyticks_fontsize(chart_enum.PLOT.value)
def get_scatterplot_chart_xyticks_fontsize(): return get_xyticks_fontsize(chart_enum.SCATTER.value)

def get_corr_cv_xyticks_fontsize(): return get_xyticks_fontsize(chart_enum.CORR_CV.value)
def get_corr_scores_xyticks_fontsize(): return get_xyticks_fontsize(chart_enum.CORR_SCORES.value)
def get_window_cv_xyticks_fontsize(): return get_xyticks_fontsize(chart_enum.WINDOW_CV.value)
def get_roll_corr_xyticks_fontsize(): return get_xyticks_fontsize(chart_enum.ROLL_CORR.value)
def get_roll_corr_all_xyticks_fontsize(): return get_xyticks_fontsize(chart_enum.ROLL_CORR_ALL.value)
def get_lag_corr_xyticks_fontsize(): return get_xyticks_fontsize(chart_enum.LAG_CORR.value)
def get_lag_heat_xyticks_fontsize(): return get_xyticks_fontsize(chart_enum.LAG_HEAT.value)


# In[104]:


#*******************************************************************************************
 #
 #  Function Name:  set_bar_chart_xyticks_fontsize
 #                  set_boxplot_chart_xyticks_fontsize
 #                  set_histogram_chart_xyticks_fontsize
 #                  set_line_chart_xyticks_fontsize
 #                  set_pie_chart_xyticks_fontsize
 #                  set_plot_chart_xyticks_fontsize
 #                  set_scatterplot_chart_xyticks_fontsize
 #
 #                  set_corr_cv_xyticks_fontsize
 #                  set_corr_scores_xyticks_fontsize
 #                  set_window_cv_xyticks_fontsize
 #                  set_roll_corr_xyticks_fontsize
 #                  set_roll_heat_xyticks_fontsize
 #                  set_lag_corr_xyticks_fontsize
 #                  set_lag_heat_xyticks_fontsize
 #
 #  Function Description:
 #      The function sets the chart's x and y ticks labels font size.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  float          xsize_flt        The parameter is the chart's x-tick label font size.
 #  float          ysize_flt        The parameter is the chart's y-tick label font size.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_bar_chart_xyticks_fontsize(xsize_flt, ysize_flt): set_xyticks_fontsize(xsize_flt, ysize_flt, chart_enum.BAR.value)
def set_boxplot_chart_xyticks_fontsize(xsize_flt, ysize_flt): set_xyticks_fontsize(xsize_flt, ysize_flt, chart_enum.BOXPLOT.value)
def set_histogram_chart_xyticks_fontsize(xsize_flt, ysize_flt): set_xyticks_fontsize(xsize_flt, ysize_flt, chart_enum.HISTOGRAM.value)
def set_line_chart_xyticks_fontsize(xsize_flt, ysize_flt): set_xyticks_fontsize(xsize_flt, ysize_flt, chart_enum.LINE.value)
def set_pie_chart_xyticks_fontsize(xsize_flt, ysize_flt): set_xyticks_fontsize(xsize_flt, ysize_flt, chart_enum.PIE.value)
def set_plot_chart_xyticks_fontsize(xsize_flt, ysize_flt): set_xyticks_fontsize(xsize_flt, ysize_flt, chart_enum.PLOT.value)
def set_scatterplot_chart_xyticks_fontsize(xsize_flt, ysize_flt): set_xyticks_fontsize(xsize_flt, ysize_flt, chart_enum.SCATTER.value)

def set_corr_cv_xyticks_fontsize(xsize_flt, ysize_flt): set_xyticks_fontsize(xsize_flt, ysize_flt, chart_enum.CORR_CV.value)
def set_corr_scores_xyticks_fontsize(xsize_flt, ysize_flt): set_xyticks_fontsize(xsize_flt, ysize_flt, chart_enum.CORR_SCORES.value)
def set_window_cv_xyticks_fontsize(xsize_flt, ysize_flt): set_xyticks_fontsize(xsize_flt, ysize_flt, chart_enum.WINDOW_CV.value)
def set_roll_corr_xyticks_fontsize(xsize_flt, ysize_flt): set_xyticks_fontsize(xsize_flt, ysize_flt, chart_enum.ROLL_CORR.value)
def set_roll_corr_all_xyticks_fontsize(xsize_flt, ysize_flt): set_xyticks_fontsize(xsize_flt, ysize_flt, chart_enum.ROLL_CORR_ALL.value)
def set_lag_corr_xyticks_fontsize(xsize_flt, ysize_flt): set_xyticks_fontsize(xsize_flt, ysize_flt, chart_enum.LAG_CORR.value)
def set_lag_heat_xyticks_fontsize(xsize_flt, ysize_flt): set_xyticks_fontsize(xsize_flt, ysize_flt, chart_enum.LAG_HEAT.value)


# In[105]:


#*******************************************************************************************
 #
 #  Function Name:  get_bar_chart_xyticks_rotation
 #                  get_boxplot_chart_xyticks_rotation
 #                  get_histogram_chart_xyticks_rotation
 #                  get_line_chart_xyticks_rotation
 #                  get_pie_chart_xyticks_rotation
 #                  get_plot_chart_xyticks_rotation
 #                  get_scatterplot_chart_xyticks_rotation
 #
 #                  get_corr_cv_xyticks_rotation
 #                  get_corr_scores_xyticks_rotation
 #                  get_window_cv_xyticks_rotation
 #                  get_roll_corr_xyticks_rotation
 #                  get_roll_corr_all_xyticks_rotation
 #                  get_lag_corr_xyticks_rotation
 #                  get_lag_heat_xyticks_rotation
 #
 #  Function Description:
 #      The function retrieves the chart's x and y ticks labels rotation angles.
 #
 #
 #  Return Type: float, float
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
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_bar_chart_xyticks_rotation(): return get_xyticks_rotation(chart_enum.BAR.value)
def get_boxplot_chart_xyticks_rotation(): return get_xyticks_rotation(chart_enum.BOXPLOT.value)
def get_histogram_chart_xyticks_rotation(): return get_xyticks_rotation(chart_enum.HISTOGRAM.value)
def get_line_chart_xyticks_rotation(): return get_xyticks_rotation(chart_enum.LINE.value)
def get_pie_chart_xyticks_rotation(): return get_xyticks_rotation(chart_enum.PIE.value)
def get_plot_chart_xyticks_rotation(): return get_xyticks_rotation(chart_enum.PLOT.value)
def get_scatterplot_chart_xyticks_rotation(): return get_xyticks_rotation(chart_enum.SCATTER.value)

def get_corr_cv_xyticks_rotation(): return get_xyticks_rotation(chart_enum.CORR_CV.value)
def get_corr_scores_xyticks_rotation(): return get_xyticks_rotation(chart_enum.CORR_SCORES.value)
def get_window_cv_xyticks_rotation(): return get_xyticks_rotation(chart_enum.WINDOW_CV.value)
def get_roll_corr_xyticks_rotation(): return get_xyticks_rotation(chart_enum.ROLL_CORR.value)
def get_roll_corr_all_xyticks_rotation(): return get_xyticks_rotation(chart_enum.ROLL_CORR_ALL.value)
def get_lag_corr_xyticks_rotation(): return get_xyticks_rotation(chart_enum.LAG_CORR.value)
def get_lag_heat_xyticks_rotation(): return get_xyticks_rotation(chart_enum.LAG_HEAT.value)


# In[106]:


#*******************************************************************************************
 #
 #  Function Name:  set_bar_chart_xyticks_rotation
 #                  set_boxplot_chart_xyticks_rotation
 #                  set_histogram_chart_xyticks_rotation
 #                  set_line_chart_xyticks_rotation
 #                  set_pie_chart_xyticks_rotation
 #                  set_plot_chart_xyticks_rotation
 #                  set_scatterplot_chart_xyticks_rotation
 #
 #                  set_corr_cv_xyticks_rotation
 #                  set_corr_scores_xyticks_rotation
 #                  set_window_cv_xyticks_rotation
 #                  set_roll_corr_xyticks_rotation
 #                  set_roll_corr_all_xyticks_rotation
 #                  set_lag_corr_xyticks_rotation
 #                  set_lag_heat_xyticks_rotation
 #
 #  Function Description:
 #      The function sets the chart's x and y ticks labels rotation angles.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  float          xrot_flt         The parameter is the chart's x-tick label rotation.
 #  float          yrot_flt         The parameter is the chart's y-tick label rotation.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_bar_chart_xyticks_rotation(xrot_flt, yrot_flt): set_xyticks_rotation(xrot_flt, yrot_flt, chart_enum.BAR.value)
def set_boxplot_chart_xyticks_rotation(xrot_flt, yrot_flt): set_xyticks_rotation(xrot_flt, yrot_flt, chart_enum.BOXPLOT.value)
def set_histogram_chart_xyticks_rotation(xrot_flt, yrot_flt): set_xyticks_rotation(xrot_flt, yrot_flt, chart_enum.HISTOGRAM.value)
def set_line_chart_xyticks_rotation(xrot_flt, yrot_flt): set_xyticks_rotation(xrot_flt, yrot_flt, chart_enum.LINE.value)
def set_pie_chart_xyticks_rotation(xrot_flt, yrot_flt): set_xyticks_rotation(xrot_flt, yrot_flt, chart_enum.PIE.value)
def set_plot_chart_xyticks_rotation(xrot_flt, yrot_flt): set_xyticks_rotation(xrot_flt, yrot_flt, chart_enum.PLOT.value)
def set_scatterplot_chart_xyticks_rotation(xrot_flt, yrot_flt): set_xyticks_rotation(xrot_flt, yrot_flt, chart_enum.SCATTER.value)

def set_corr_cv_xyticks_rotation(xrot_flt, yrot_flt): set_xyticks_rotation(xrot_flt, yrot_flt, chart_enum.CORR_CV.value)
def set_corr_scores_xyticks_rotation(xrot_flt, yrot_flt): set_xyticks_rotation(xrot_flt, yrot_flt, chart_enum.CORR_SCORES.value)
def set_window_cv_xyticks_rotation(xrot_flt, yrot_flt): set_xyticks_rotation(xrot_flt, yrot_flt, chart_enum.WINDOW_CV.value)
def set_roll_corr_xyticks_rotation(xrot_flt, yrot_flt): set_xyticks_rotation(xrot_flt, yrot_flt, chart_enum.ROLL_CORR.value)
def set_roll_corr_all_xyticks_rotation(xrot_flt, yrot_flt): set_xyticks_rotation(xrot_flt, yrot_flt, chart_enum.ROLL_CORR_ALL.value)
def set_lag_corr_xyticks_rotation(xrot_flt, yrot_flt): set_xyticks_rotation(xrot_flt, yrot_flt, chart_enum.LAG_CORR.value)
def set_lag_heat_xyticks_rotation(xrot_flt, yrot_flt): set_xyticks_rotation(xrot_flt, yrot_flt, chart_enum.LAG_HEAT.value)


# In[107]:


#*******************************************************************************************
 #
 #  Function Name:  get_bar_chart_legend_display
 #                  get_histogram_chart_legend_display
 #                  get_line_chart_legend_display
 #                  get_pie_chart_legend_display
 #                  get_plot_chart_legend_display
 #
 #                  get_corr_cv_legend_display
 #                  get_corr_scores_legend_display
 #                  get_window_cv_legend_display
 #                  get_roll_corr_legend_display
 #                  get_roll_corr_all_legend_display
 #                  get_lag_corr_legend_display
 #                  get_lag_heat_legend_display
 #
 #  Function Description:
 #      The function retrieves the chart's legend display indicator.
 #
 #
 #  Return Type: boolean
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
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_bar_chart_legend_display(): return get_legend_display(chart_enum.BAR.value)
def get_histogram_chart_legend_display(): return get_legend_display(chart_enum.HISTOGRAM.value)
def get_line_chart_legend_display(): return get_legend_display(chart_enum.LINE.value)
def get_pie_chart_legend_display(): return get_legend_display(chart_enum.PIE.value)
def get_plot_chart_legend_display(): return get_legend_display(chart_enum.PLOT.value)

def get_corr_cv_legend_display(): return get_legend_display(chart_enum.CORR_CV.value)
def get_corr_scores_legend_display(): return get_legend_display(chart_enum.CORR_SCORES.value)
def get_window_cv_legend_display(): return get_legend_display(chart_enum.WINDOW_CV.value)
def get_roll_corr_legend_display(): return get_legend_display(chart_enum.ROLL_CORR.value)
def get_roll_corr_all_legend_display(): return get_legend_display(chart_enum.ROLL_CORR_ALL.value)
def get_lag_corr_legend_display(): return get_legend_display(chart_enum.LAG_CORR.value)
def get_lag_heat_legend_display(): return get_legend_display(chart_enum.LAG_HEAT.value)


# In[108]:


#*******************************************************************************************
 #
 #  Function Name:  set_bar_chart_legend_display
 #                  set_histogram_chart_legend_display
 #                  set_line_chart_legend_display
 #                  set_pie_chart_legend_display
 #                  set_plot_chart_legend_display
 #
 #                  set_corr_cv_legend_display
 #                  set_corr_scores_legend_display
 #                  set_window_cv_legend_display
 #                  set_roll_corr_legend_display
 #                  set_roll_corr_all_legend_display
 #                  set_lag_corr_legend_display
 #                  set_lag_heat_legend_display
 #
 #  Function Description:
 #      The function sets the chart's legend display indicator.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  boolean        upd_bool         The parameter is the updated legend display indicator.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_bar_chart_legend_display(upd_bool): set_legend_display(upd_bool, chart_enum.BAR.value)
def set_histogram_chart_legend_display(upd_bool): set_legend_display(upd_bool, chart_enum.HISTOGRAM.value)
def set_line_chart_legend_display(upd_bool): set_legend_display(upd_bool, chart_enum.LINE.value)
def set_pie_chart_legend_display(upd_bool): set_legend_display(upd_bool, chart_enum.PIE.value)
def set_plot_chart_legend_display(upd_bool): set_legend_display(upd_bool, chart_enum.PLOT.value)

def set_corr_cv_legend_display(upd_bool): set_legend_display(upd_bool, chart_enum.CORR_CV.value)
def set_corr_scores_legend_display(upd_bool): set_legend_display(upd_bool, chart_enum.CORR_SCORES.value)
def set_window_cv_legend_display(upd_bool): set_legend_display(upd_bool, chart_enum.WINDOW_CV.value)
def set_roll_corr_legend_display(upd_bool): set_legend_display(upd_bool, chart_enum.ROLL_CORR.value)
def set_roll_corr_all_legend_display(upd_bool): set_legend_display(upd_bool, chart_enum.ROLL_CORR_ALL.value)
def set_lag_corr_legend_display(upd_bool): set_legend_display(upd_bool, chart_enum.LAG_CORR.value)
def set_lag_heat_legend_display(upd_bool): set_legend_display(upd_bool, chart_enum.LAG_HEAT.value)


# In[109]:


#*******************************************************************************************
 #
 #  Function Name:  get_bar_chart_legend_fontsize
 #                  get_histogram_chart_legend_fontsize
 #                  get_line_chart_legend_fontsize
 #                  get_pie_chart_legend_fontsize
 #                  get_plot_chart_legend_fontsize
 #
 #                  get_corr_cv_legend_fontsize
 #                  get_corr_scores_legend_fontsize
 #                  get_window_cv_legend_fontsize
 #                  get_roll_corr_legend_fontsize
 #                  get_roll_corr_all_legend_fontsize
 #                  get_lag_corr_legend_fontsize
 #                  get_lag_heat_legend_fontsize
 #
 #  Function Description:
 #      The function retrieves the chart's legend font size.
 #
 #
 #  Return Type: boolean
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
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_bar_chart_legend_fontsize(): return get_legend_fontsize(chart_enum.BAR.value)
def get_histogram_chart_legend_fontsize(): return get_legend_fontsize(chart_enum.HISTOGRAM.value)
def get_line_chart_legend_fontsize(): return get_legend_fontsize(chart_enum.LINE.value)
def get_pie_chart_legend_fontsize(): return get_legend_fontsize(chart_enum.PIE.value)
def get_plot_chart_legend_fontsize(): return get_legend_fontsize(chart_enum.PLOT.value)

def get_corr_cv_legend_fontsize(): return get_legend_fontsize(chart_enum.CORR_CV.value)
def get_corr_scores_legend_fontsize(): return get_legend_fontsize(chart_enum.CORR_SCORES.value)
def get_window_cv_legend_fontsize(): return get_legend_fontsize(chart_enum.WINDOW_CV.value)
def get_roll_corr_legend_fontsize(): return get_legend_fontsize(chart_enum.ROLL_CORR.value)
def get_roll_corr_all_legend_fontsize(): return get_legend_fontsize(chart_enum.ROLL_CORR_ALL.value)
def get_lag_corr_legend_fontsize(): return get_legend_fontsize(chart_enum.LAG_CORR.value)
def get_lag_heat_legend_fontsize(): return get_legend_fontsize(chart_enum.LAG_HEAT.value)


# In[110]:


#*******************************************************************************************
 #
 #  Function Name:  set_bar_chart_legend_fontsize
 #                  set_histogram_chart_legend_fontsize
 #                  set_line_chart_legend_fontsize
 #                  set_pie_chart_legend_fontsize
 #                  set_plot_chart_legend_fontsize
 #
 #                  set_corr_cv_legend_fontsize
 #                  set_corr_scores_legend_fontsize
 #                  set_window_cv_legend_fontsize
 #                  set_roll_corr_legend_fontsize
 #                  set_roll_corr_all_legend_fontsize
 #                  set_lag_corr_legend_fontsize
 #                  set_lag_heat_legend_fontsize
 #
 #  Function Description:
 #      The function sets the chart's legend font size.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  boolean        upd_flt          The parameter is the updated legend font size.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_bar_chart_legend_fontsize(upd_flt): set_legend_fontsize(upd_flt, chart_enum.BAR.value)
def set_histogram_chart_legend_fontsize(upd_flt): set_legend_fontsize(upd_flt, chart_enum.HISTOGRAM.value)
def set_line_chart_legend_fontsize(upd_flt): set_legend_fontsize(upd_flt, chart_enum.LINE.value)
def set_pie_chart_legend_fontsize(upd_flt): set_legend_fontsize(upd_flt, chart_enum.PIE.value)
def set_plot_chart_legend_fontsize(upd_flt): set_legend_fontsize(upd_flt, chart_enum.PLOT.value)

def set_corr_cv_legend_fontsize(upd_flt): set_legend_fontsize(upd_flt, chart_enum.CORR_CV.value)
def set_corr_scores_legend_fontsize(upd_flt): set_legend_fontsize(upd_flt, chart_enum.CORR_SCORES.value)
def set_window_cv_legend_fontsize(upd_flt): set_legend_fontsize(upd_flt, chart_enum.WINDOW_CV.value)
def set_roll_corr_legend_fontsize(upd_flt): set_legend_fontsize(upd_flt, chart_enum.ROLL_CORR.value)
def set_roll_corr_all_legend_fontsize(upd_flt): set_legend_fontsize(upd_flt, chart_enum.ROLL_CORR_ALL.value)
def set_lag_corr_legend_fontsize(upd_flt): set_legend_fontsize(upd_flt, chart_enum.LAG_CORR.value)
def set_lag_heat_legend_fontsize(upd_flt): set_legend_fontsize(upd_flt, chart_enum.LAG_HEAT.value)


# In[111]:


#*******************************************************************************************
 #
 #  Function Name:  get_bar_chart_legend_bbox_to_anchor
 #                  get_histogram_chart_legend_bbox_to_anchor
 #                  get_line_chart_legend_bbox_to_anchor
 #                  get_pie_chart_legend_bbox_to_anchor
 #                  get_plot_chart_legend_bbox_to_anchor
 #
 #                  get_corr_cv_legend_bbox_to_anchor
 #                  get_corr_scores_legend_bbox_to_anchor
 #                  get_window_cv_legend_bbox_to_anchor
 #                  get_roll_corr_legend_bbox_to_anchor
 #                  get_roll_corr_all_legend_bbox_to_anchor
 #                  get_lag_corr_legend_bbox_to_anchor
 #                  get_lag_heat_legend_bbox_to_anchor
 #
 #  Function Description:
 #      The function retrieves the chart's legend bbox to anchor.
 #
 #
 #  Return Type: (float, float)
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
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_bar_chart_legend_bbox_to_anchor(): return get_legend_bbox_to_anchor(chart_enum.BAR.value)
def get_histogram_chart_legend_bbox_to_anchor(): return get_legend_bbox_to_anchor(chart_enum.HISTOGRAM.value)
def get_line_chart_legend_bbox_to_anchor(): return get_legend_bbox_to_anchor(chart_enum.LINE.value)
def get_pie_chart_legend_bbox_to_anchor(): return get_legend_bbox_to_anchor(chart_enum.PIE.value)
def get_plot_chart_legend_bbox_to_anchor(): return get_legend_bbox_to_anchor(chart_enum.PLOT.value)

def get_corr_cv_legend_bbox_to_anchor(): return get_legend_bbox_to_anchor(chart_enum.CORR_CV.value)
def get_corr_scores_legend_bbox_to_anchor(): return get_legend_bbox_to_anchor(chart_enum.CORR_SCORES.value)
def get_window_cv_legend_bbox_to_anchor(): return get_legend_bbox_to_anchor(chart_enum.WINDOW_CV.value)
def get_roll_corr_legend_bbox_to_anchor(): return get_legend_bbox_to_anchor(chart_enum.ROLL_CORR.value)
def get_roll_corr_all_legend_bbox_to_anchor(): return get_legend_bbox_to_anchor(chart_enum.ROLL_CORR_ALL.value)
def get_lag_corr_legend_bbox_to_anchor(): return get_legend_bbox_to_anchor(chart_enum.LAG_CORR.value)
def get_lag_heat_legend_bbox_to_anchor(): return get_legend_bbox_to_anchor(chart_enum.LAG_HEAT.value)


# In[112]:


#*******************************************************************************************
 #
 #  Function Name:  set_bar_chart_legend_bbox_to_anchor
 #                  set_histogram_chart_legend_bbox_to_anchor
 #                  set_line_chart_legend_bbox_to_anchor
 #                  set_pie_chart_legend_bbox_to_anchor
 #                  set_plot_chart_legend_bbox_to_anchor
 #
 #                  set_corr_cv_legend_bbox_to_anchor
 #                  set_corr_scores_legend_bbox_to_anchor
 #                  set_window_cv_legend_bbox_to_anchor
 #                  set_roll_corr_legend_bbox_to_anchor
 #                  set_roll_corr_all_legend_bbox_to_anchor
 #                  set_lag_corr_legend_bbox_to_anchor
 #                  set_lag_heat_legend_bbox_to_anchor
 #
 #  Function Description:
 #      The function sets the chart's legend bbox to anchor.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  float          x_flt            The parameter is the x-coordinate.
 #  float          y_flt            The parameter is the y-coordinate.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_bar_chart_legend_bbox_to_anchor(x_flt, y_flt): set_legend_bbox_to_anchor(x_flt, y_flt, chart_enum.BAR.value)
def set_histogram_chart_legend_bbox_to_anchor(x_flt, y_flt): set_legend_bbox_to_anchor(x_flt, ylabel, chart_enum.HISTOGRAM.value)
def set_line_chart_legend_bbox_to_anchor(x_flt, y_flt): set_legend_bbox_to_anchor(x_flt, y_flt, chart_enum.LINE.value)
def set_pie_chart_legend_bbox_to_anchor(x_flt, y_flt): set_legend_bbox_to_anchor(x_flt, y_flt, chart_enum.PIE.value)
def set_plot_chart_legend_bbox_to_anchor(x_flt, y_flt): set_legend_bbox_to_anchor(x_flt, y_flt, chart_enum.PLOT.value)

def set_corr_cv_legend_bbox_to_anchor(x_flt, y_flt): set_legend_bbox_to_anchor(x_flt, y_flt, chart_enum.CORR_CV.value)
def set_corr_scores_legend_bbox_to_anchor(x_flt, y_flt): set_legend_bbox_to_anchor(x_flt, y_flt, chart_enum.CORR_SCORES.value)
def set_window_cv_legend_bbox_to_anchor(x_flt, y_flt): set_legend_bbox_to_anchor(x_flt, y_flt, chart_enum.WINDOW_CV.value)
def set_roll_corr_legend_bbox_to_anchor(x_flt, y_flt): set_legend_bbox_to_anchor(x_flt, y_flt, chart_enum.ROLL_CORR.value)
def set_roll_corr_all_legend_bbox_to_anchor(x_flt, y_flt): set_legend_bbox_to_anchor(x_flt, y_flt, chart_enum.ROLL_CORR_ALL.value)
def set_lag_corr_legend_bbox_to_anchor(x_flt, y_flt): set_legend_bbox_to_anchor(x_flt, y_flt, chart_enum.LAG_CORR.value)
def set_lag_heat_legend_bbox_to_anchor(x_flt, y_flt): set_legend_bbox_to_anchor(x_flt, y_flt, chart_enum.LAG_HEAT.value)


# In[113]:


#*******************************************************************************************
 #
 #  Function Name:  get_regr_degree
 #
 #  Function Description:
 #      The function retrieves the regression line degree.
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
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_regr_degree(): return regr_line_dict['degree']


# In[114]:


#*******************************************************************************************
 #
 #  Function Name:  get_regr_eqn_coords
 #
 #  Function Description:
 #      The function retrieves the regression equations x-axis and y-axis coordinates.
 #
 #
 #  Return Type: float, float
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
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_regr_eqn_coords(): return regr_line_dict['eqn_x_coord'], regr_line_dict['eqn_y_coord']


# In[115]:


#*******************************************************************************************
 #
 #  Function Name:  get_rvalues_display
 #
 #  Function Description:
 #      The function retrieves the r-value display indicator.
 #
 #
 #  Return Type: boolean
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
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_rvalues_display(): return regr_line_dict['r_disp']


# In[116]:


#*******************************************************************************************
 #
 #  Function Name:  set_regr_degree
 #
 #  Function Description:
 #      The function sets the regression line degree.
 #
 #
 #  Return Type: n/a
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

def set_regr_degree(input_obj):

    global regr_line_dict


    if isinstance(input_obj, int): regr_line_dict['degree'] = np.array([abs(input_obj)])

    elif isinstance(input_obj, float): regr_line_dict['degree'] = np.array([int(abs(input_obj))])

    elif isinstance(input_obj, np.ndarray): regr_line_dict['degree'] = input_obj

    elif isinstance(input_obj, list): regr_line_dict['degree'] = np.array(input_obj)

    elif isinstance(input_obj, pd.Series): regr_line_dict['degree'] = input_obj.to_numpy()


# In[117]:


#*******************************************************************************************
 #
 #  Function Name:  set_regr_eqn_coords
 #
 #  Function Description:
 #      The function sets the regression equations x-axis and y-axis coordinates.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  object         x_crd_obj        The parameter is the regression equation's
 #                                  x-coordinate.
 #  object         y_crd_obj        The parameter is the regression equation's
 #                                  y-coordinate.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_regr_eqn_coords(x_crd_obj, y_crd_obj):

    global regr_line_dict


    if isinstance(x_crd_obj, int) \
        or isinstance(x_crd_obj, float): regr_line_dict['eqn_x_coord'] = [x_crd_obj]

    elif isinstance(x_crd_obj, list): regr_line_dict['eqn_x_coord'] = x_crd_obj


    if isinstance(y_crd_obj, int) \
        or isinstance(y_crd_obj, float): regr_line_dict['eqn_y_coord'] = [y_crd_obj]

    elif isinstance(y_crd_obj, list): regr_line_dict['eqn_y_coord'] = y_crd_obj  


# In[118]:


#*******************************************************************************************
 #
 #  Function Name:  set_rvalues_display
 #
 #  Function Description:
 #      The function sets the r-value display indicator.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  boolean        upd_bool         The parameter is the updated regression value display 
 #                                  indicator.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_rvalues_display(upd_bool):

    global regr_line_dict

    regr_line_dict['r_disp'] = upd_bool


# In[119]:


#*******************************************************************************************
 #
 #  Function Name:  get_bar_chart_colors
 #                  get_histogram_chart_colors
 #                  get_line_chart_colors
 #                  get_pie_chart_colors
 #                  get_plot_chart_colors
 #                  get_scatterplot_chart_colors
 #
 #                  get_corr_cv_chart_colors
 #                  get_corr_scores_chart_colors
 #                  get_window_cv_chart_colors
 #                  get_roll_corr_chart_colors
 #                  get_roll_corr_chart_colors
 #                  get_lag_corr_chart_colors
 #                  get_lag_heat_chart_colors
 #
 #  Function Description:
 #      The function retrieves the chart colors.
 #
 #
 #  Return Type: string or list
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  string         cat              The parameter is the color category.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_bar_chart_colors(cat = ''): return get_chart_colors(chart_enum.BAR.value, cat)
def get_histogram_chart_colors(cat = ''): return get_chart_colors(chart_enum.HISTOGRAM.value, cat)
def get_line_chart_colors(cat = 'line'): return get_chart_colors(chart_enum.LINE.value, cat)
def get_pie_chart_colors(cat = ''): return get_chart_colors(chart_enum.PIE.value, cat)
def get_plot_chart_colors(cat = 'params'): return get_chart_colors(chart_enum.PLOT.value, cat)
def get_scatterplot_chart_colors(cat = 'marker'): return get_chart_colors(chart_enum.PLOT.value, cat)

def get_corr_cv_chart_colors(cat = 'line'): return get_chart_colors(chart_enum.CORR_CV.value, cat)
def get_corr_scores_chart_colors(cat = 'line'): return get_chart_colors(chart_enum.CORR_SCORES.value, cat)
def get_window_cv_chart_colors(cat = 'line'): return get_chart_colors(chart_enum.WINDOW_CV.value, cat)
def get_roll_corr_chart_colors(cat = 'line'): return get_chart_colors(chart_enum.ROLL_CORR.value, cat)
def get_roll_corr_all_chart_colors(cat = 'line'): return get_chart_colors(chart_enum.ROLL_CORR_ALL.value, cat)
def get_lag_corr_colors(cat = 'params'): return get_chart_colors(chart_enum.LAG_CORR.value, cat)
def get_lag_heat_colors(cat = 'params'): return get_chart_colors(chart_enum.LAG_HEAT.value, cat)


# In[120]:


#*******************************************************************************************
 #
 #  Function Name:  set_bar_chart_colors
 #                  set_histogram_chart_colors
 #                  set_line_chart_colors
 #                  set_pie_chart_colors
 #                  set_plot_chart_colors
 #                  set_scatterplot_chart_colors
 #
 #                  set_corr_cv_chart_colors
 #                  set_corr_scores_chart_colors
 #                  set_window_cv_chart_colors
 #                  set_roll_corr_chart_colors
 #                  set_roll_corr_all_chart_colors
 #                  set_lag_corr_chart_colors
 #                  set_lag_heat_chart_colors
 #
 #  Function Description:
 #      The function sets the chart face colors.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  object         upd_obj          The parameter is the updated group of chart colors.
 #  string         cat              The parameter is the color category.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_bar_chart_colors(upd_obj, cat = ''): set_chart_colors(upd_obj, chart_enum.BAR.value, cat)
def set_histogram_chart_colors(upd_obj, cat = ''): set_chart_colors(upd_obj, chart_enum.HISTOGRAM.value, cat)
def set_line_chart_colors(upd_obj, cat = 'line'): set_chart_colors(upd_obj, chart_enum.LINE.value, cat)
def set_pie_chart_colors(upd_obj, cat = ''): set_chart_colors(upd_obj, chart_enum.PIE.value, cat)
def set_plot_chart_colors(upd_obj, cat = 'params'): set_chart_colors(upd_obj, chart_enum.PLOT.value, cat)     
def set_scatterplot_chart_colors(upd_obj, cat = 'marker'): set_chart_colors(upd_obj, chart_enum.SCATTER.value, cat)

def set_corr_cv_colors(upd_obj, cat = 'line'): set_chart_colors(upd_obj, chart_enum.CORR_CV.value)
def set_corr_scores_colors(upd_obj, cat = 'line'): set_chart_colors(upd_obj, chart_enum.CORR_SCORES.value)
def set_window_cv_colors(upd_obj, cat = 'line'): set_chart_colors(upd_obj, chart_enum.WINDOW_CV.value)
def set_roll_corr_colors(upd_obj, cat = 'line'): set_chart_colors(upd_obj, chart_enum.ROLL_CORR.value)
def set_roll_corr_all_colors(upd_obj, cat = 'line'): set_chart_colors(upd_obj, chart_enum.ROLL_CORR_ALL.value)
def set_lag_corr_colors(upd_obj, cat = 'params'): set_chart_colors(upd_obj, chart_enum.LAG_CORR.value, cat)
def set_lag_heat_colors(upd_obj, cat = 'params'): set_chart_colors(upd_obj, chart_enum.LAG_HEAT.value, cat)


# In[121]:


#*******************************************************************************************
 #
 #  Function Name:  get_boxplot_chart_xycols
 #
 #  Function Description:
 #      The function retrieves the boxplot chart dataframe x and y column names.
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
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_boxplot_chart_xycols(): return boxplot_chart_dict['params']['x_col'], boxplot_chart_dict['params']['y_col']


# In[122]:


#*******************************************************************************************
 #
 #  Function Name:  set_boxplot_chart_xycols
 #
 #  Function Description:
 #      The function sets the pie chart explode values.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  string         x_col            The parameter is the x-axis dataframe column name.
 #  string         y_col            The parameter is the y-axis dataframe column name.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_boxplot_chart_xycols(x_col, y_col):

    global boxplot_chart_dict

    boxplot_chart_dict['params']['x_col'] = x_col

    boxplot_chart_dict['params']['y_col'] = y_col


# In[123]:


#*******************************************************************************************
 #
 #  Function Name:  get_line_chart_marker_size
 #                  get_line_chart_linewidth
 #
 #  Function Description:
 #      The function retrieves the line chart attributes.
 #
 #
 #  Return Type: float
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
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_line_chart_marker_size(): return line_chart_dict['marker']['size']
def get_line_chart_linewidth(): return line_chart_dict['line']['linewidth']


# In[124]:


#*******************************************************************************************
 #
 #  Function Name:  set_line_chart_marker_size
 #
 #  Function Description:
 #      The function sets the line chart marker size.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  float          upd_flt          The parameter is the new marker size.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_line_chart_marker_size(upd_flt):

    global line_chart_dict

    line_chart_dict['marker']['size'] = upd_flt


# In[125]:


#*******************************************************************************************
 #
 #  Function Name:  set_line_chart_linewidth
 #
 #  Function Description:
 #      The function sets the line chart line width.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  float          upd_flt          The parameter is the new line width.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_line_chart_linewidth(upd_flt):

    global line_chart_dict

    line_chart_dict['line']['linewidth'] = upd_flt


# In[126]:


#*******************************************************************************************
 #
 #  Function Name:  get_pie_chart_explode
 #                  get_pie_textprops_fontsize
 #
 #  Function Description:
 #      The function retrieves the pie chart attributes.
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
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_pie_chart_explode():      return pie_chart_dict['params']['explode']
def get_pie_textprops_fontsize(): return pie_chart_dict['params']['textprops']['fontsize']


# In[127]:


#*******************************************************************************************
 #
 #  Function Name:  set_pie_chart_explode
 #
 #  Function Description:
 #      The function sets the pie chart explode values.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  object         upd_obj          The parameter is the updated group of pie chart 
 #                                  explode values.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_pie_chart_explode(upd_obj):

    global pie_chart_dict

    pie_chart_dict['params']['explode'] = dtypesx.cnv_data_to_array(upd_obj)


# In[128]:


#*******************************************************************************************
 #
 #  Function Name:  set_pie_textprops_fontsize
 #
 #  Function Description:
 #      The function sets the pie chart text properties fontsize.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  float          upd_flt          The parameter is the updated font size.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_pie_textprops_fontsize(upd_flt):

    global pie_chart_dict

    pie_chart_dict['params']['textprops']['fontsize'] = upd_flt


# In[129]:


#*******************************************************************************************
 #
 #  Function Name:  get_roll_corr_w_mp
 #
 #  Function Description:
 #      The function retrieves the rolling correlation's best window and best minimum 
 #      periods.
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
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_roll_corr_w_mp(): return roll_corr_dict['params']['window'], roll_corr_dict['params']['min_periods']


# In[130]:


#*******************************************************************************************
 #
 #  Function Name:  set_roll_corr_w_mp
 #
 #  Function Description:
 #      The function sets the rolling correlation's best window and best minimum periods.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  int            w_int            The parameter is the updated window.
 #  int            mp_int           The parameter is the minimum periods.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_roll_corr_w_mp(w_int, mp_int):

    global roll_corr_dict

    roll_corr_dict['params']['window'] = w_int

    roll_corr_dict['params']['min_periods'] = mp_int


# In[131]:


#*******************************************************************************************
 #
 #  Function Name:  get_lag_corr_max_lag
 #                  get_lag_corr_annot_xyoffsets
 #                  get_lag_corr_method
 #
 #  Function Description:
 #      The function retrieves the lag correlation attributes.
 #
 #
 #  Return Type: float, float
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
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_lag_corr_max_lag(): return lag_corr_dict['params']['max_lag']
def get_lag_corr_annot_xyoffsets(): return lag_corr_dict['annotation']['xoffset'], lag_corr_dict['annotation']['yoffset']
def get_lag_corr_method(): return lag_corr_dict['params']['method']


# In[132]:


#*******************************************************************************************
 #
 #  Function Name:  set_lag_corr_max_lag
 #
 #  Function Description:
 #      The function sets the lag correlation's maximum lag.
 #
 #
 #  Return Type: float, float
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  integer        upd_int          The parameter is the maximum lag.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_lag_corr_max_lag(upd_int):

    global lag_corr_dict

    lag_corr_dict['params']['max_lag'] = upd_int


# In[133]:


#*******************************************************************************************
 #
 #  Function Name:  set_lag_corr_annot_xyoffsets
 #
 #  Function Description:
 #      The function sets the lag correlation's annotation x- and y-offsets.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  float          x_flt            The parameter is the x-offset.
 #  float          y_flt            The parameter is the y-offset. 
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_lag_corr_annot_xyoffsets(x_flt, y_flt):

    global lag_corr_dict

    lag_corr_dict['annotation']['xoffset'] = x_flt

    lag_corr_dict['annotation']['yoffset'] = y_flt 


# In[134]:


#*******************************************************************************************
 #
 #  Function Name:  set_lag_corr_method
 #
 #  Function Description:
 #      The function sets the lag correlation's method.
 #
 #
 #  Return Type: float, float
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  string         upd              The parameter is the updated correlation method.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_lag_corr_method(upd):

    global lag_corr_dict

    lag_corr_dict['params']['method'] = upd


# In[135]:


#*******************************************************************************************
 #
 #  Function Name:  get_corr_scores_marker_size
 #
 #  Function Description:
 #      The function retrieves the corr scores marker size.
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
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_corr_scores_marker_size(): return corr_scores_dict['marker']['size']


# In[136]:


#*******************************************************************************************
 #
 #  Function Name:  set_corr_scores_marker_size
 #
 #  Function Description:
 #      The function sets the corr scores marker size.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  float          upd_flt          The parameter is the updated marker size. 
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_corr_scores_marker_size(upd_flt):

    global corr_scores_dict

    corr_scores_dict['marker']['size'] = upd_flt


# In[137]:


#*******************************************************************************************
 #
 #  Function Name:  get_lag_heat_max_lag
 #                  get_lag_heat_corr_method
 #
 #  Function Description:
 #      The function retrieves the lag heatmap's attributes.
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
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_lag_heat_max_lag(): return lag_heat_dict['params']['max_lag']
def get_lag_heat_corr_method(): return lag_heat_dict['params']['method']


# In[138]:


#*******************************************************************************************
 #
 #  Function Name:  set_lag_heat_max_lag
 #
 #  Function Description:
 #      The function sets the lag heatmap's maximum lag.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  integer        upd_int          The parameter is the updated maximum lag.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_lag_heat_max_lag(upd_int):

    global lag_heat_dict

    lag_heat_dict['params']['max_lag'] = upd_int


# In[139]:


#*******************************************************************************************
 #
 #  Function Name:  set_lag_heat_corr_method
 #
 #  Function Description:
 #      The function sets the lag heatmap's correlation method.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  string         upd_str          The parameter is the updated correlation method.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_lag_heat_corr_method(upd_str):

    global lag_heat_dict

    lag_heat_dict['params']['method'] = upd_str


# In[140]:


#*******************************************************************************************
 #
 #  Function Name:  get_bar_multichart_fig_dims
 #                  get_boxplot_multichart_fig_dims
 #                  get_histogram_multichart_fig_dims
 #                  get_line_multichart_fig_dims
 #                  get_pie_multichart_fig_dims
 #                  get_plot_multichart_fig_dims
 #                  get_scatterplot_multichart_fig_dims
 #
 #  Function Description:
 #      The function retrieves the multichart figure dimensions (width, length).
 #
 #
 #  Return Type: float, float
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
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_bar_multichart_fig_dims(): return get_multichart_fig_dims(chart_enum.MULTIBAR.value)
def get_boxplot_multichart_fig_dims(): return get_multichart_fig_dims(chart_enum.MULTIBOXPLOT.value)
def get_histogram_multichart_fig_dims(): return get_multichart_fig_dims(chart_enum.MULTIHISTOGRAM.value)
def get_line_multichart_fig_dims(): return get_multichart_fig_dims(chart_enum.MULTILINE.value)
def get_pie_multichart_fig_dims(): return get_multichart_fig_dims(chart_enum.MULTIPIE.value)
def get_plot_multichart_fig_dims(): return get_multichart_fig_dims(chart_enum.MULTIPLOT.value)
def get_scatterplot_multichart_fig_dims(): return get_multichart_fig_dims(chart_enum.MULTISCATTER.value)


# In[141]:


#*******************************************************************************************
 #
 #  Function Name:  set_bar_multichart_fig_dims
 #                  set_boxplot_multichart_fig_dims
 #                  set_histogram_multichart_fig_dims
 #                  set_line_multichart_fig_dims
 #                  set_pie_multichart_fig_dims
 #                  set_plot_multichart_fig_dims
 #                  set_scatterplot_multichart_fig_dims
 #
 #  Function Description:
 #      The function sets the multichartfigure dimesions (width, length)
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  float          width_flt        The parameter is the chart figure's width.
 #  float          length_flt       The parameter is the chart figure's length.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_bar_multichart_fig_dims(width_flt, length_flt): set_multichart_fig_dims(width_flt, length_flt, chart_enum.MULTIBAR.value)
def set_boxplot_multichart_fig_dims(width_flt, length_flt): set_multichart_fig_dims(width_flt, length_flt, chart_enum.MULTIBOXPLOT.value)
def set_histogram_multichart_fig_dims(width_flt, length_flt): set_multichart_fig_dims(width_flt, length_flt, chart_enum.MULTIHISTOGRAM.value)
def set_line_multichart_fig_dims(width_flt, length_flt): set_multichart_fig_dims(width_flt, length_flt, chart_enum.MULTILINE.value)
def set_pie_multichart_fig_dims(width_flt, length_flt): set_multichart_fig_dims(width_flt, length_flt, chart_enum.MULTIPIE.value)
def set_plot_multichart_fig_dims(width_flt, length_flt): set_multichart_fig_dims(width_flt, length_flt, chart_enum.MULTIPLOT.value)
def set_scatterplot_multichart_fig_dims(width_flt, length_flt): set_multichart_fig_dims(width_flt, length_flt, chart_enum.MULTISCATTER.value)


# In[142]:


#*******************************************************************************************
 #
 #  Function Name:  get_bar_multichart_fig_spaces
 #                  get_boxplot_multichart_fig_spaces
 #                  get_histogram_multichart_fig_spaces
 #                  get_line_multichart_fig_spaces
 #                  get_pie_multichart_fig_spaces
 #                  get_plot_multichart_fig_spaces
 #                  get_scatterplot_multichart_fig_spaces
 #
 #  Function Description:
 #      The function retrieves the multichart figure spaces (wspace, hspace).
 #
 #
 #  Return Type: float, float
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
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_bar_multichart_fig_spaces(): return get_multichart_fig_spaces(chart_enum.MULTIBAR.value)
def get_boxplot_multichart_fig_spaces(): return get_multichart_fig_spaces(chart_enum.MULTIBOXPLOT.value)
def get_histogram_multichart_fig_spaces(): return get_multichart_fig_spaces(chart_enum.MULTIHISTOGRAM.value)
def get_line_multichart_fig_spaces(): return get_multichart_fig_spaces(chart_enum.MULTILINE.value)
def get_pie_multichart_fig_spaces(): return get_multichart_fig_spaces(chart_enum.MULTIPIE.value)
def get_plot_multichart_fig_spaces(): return get_multichart_fig_spaces(chart_enum.MULTIPLOT.value)
def get_scatterplot_multichart_fig_spaces(): return get_multichart_fig_spaces(chart_enum.MULTISCATTER.value)


# In[143]:


#*******************************************************************************************
 #
 #  Function Name:  set_bar_multichart_fig_spaces
 #                  set_boxplot_multichart_fig_spaces
 #                  set_histogram_multichart_fig_spaces
 #                  set_line_multichart_fig_spaces
 #                  set_pie_multichart_fig_spaces
 #                  set_plot_multichart_fig_spaces
 #                  set_scatterplot_multichart_fig_spaces
 #
 #  Function Description:
 #      The function sets the multichart figure spaces (wspace, hspace)
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  float          wspace_flt       The parameter is the chart figure's wspace.
 #  float          hspace_flt       The parameter is the chart figure's hspace.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_bar_multichart_fig_spaces(wspace_flt, hspace_flt): set_multichart_fig_spaces(wspace_flt, hspace_flt, chart_enum.MULTIBAR.value)
def set_boxplot_multichart_fig_spaces(wspace_flt, hspace_flt): set_multichart_fig_spaces(wspace_flt, hspace_flt, chart_enum.MULTIBOXPLOT.value)
def set_histogram_multichart_fig_spaces(wspace_flt, hspace_flt): set_multichart_fig_spaces(wspace_flt, hspace_flt, chart_enum.MULTIHISTOGRAM.value)
def set_line_multichart_fig_spaces(wspace_flt, hspace_flt): set_multichart_fig_spaces(wspace_flt, hspace_flt, chart_enum.MULTILINE.value)
def set_pie_multichart_fig_spaces(wspace_flt, hspace_flt): set_multichart_fig_spaces(wspace_flt, hspace_flt, chart_enum.MULTIPIE.value)
def set_plot_multichart_fig_spaces(wspace_flt, hspace_flt): set_multichart_fig_spaces(wspace_flt, hspace_flt, chart_enum.MULTIPLOT.value)
def set_scatterplot_multichart_fig_spaces(wspace_flt, hspace_flt): set_multichart_fig_spaces(wspace_flt, hspace_flt, chart_enum.MULTISCATTER.value)


# In[144]:


#*******************************************************************************************
 #
 #  Function Name:  get_bar_multichart_stacked
 #                  get_boxplot_multichart_stacked
 #                  get_histogram_multichart_stacked
 #                  get_line_multichart_stacked
 #                  get_pie_multichart_stacked
 #                  get_plot_multichart_stacked
 #                  get_scatterplot_multichart_stacked
 #
 #  Function Description:
 #      The function retrieves the multichart's stacked boolean value.
 #
 #
 #  Return Type: boolean
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
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_bar_multichart_stacked(): return get_multichart_stacked(chart_enum.MULTIBAR.value)
def get_boxplot_multichart_stacked(): return get_multichart_stacked(chart_enum.MULTIBOXPLOT.value)
def get_histogram_multichart_stacked(): return get_multichart_stacked(chart_enum.MULTIHISTOGRAM.value)
def get_line_multichart_stacked(): return get_multichart_stacked(chart_enum.MULTILINE.value)
def get_pie_multichart_stacked(): return get_multichart_stacked(chart_enum.MULTIPIE.value)
def get_plot_multichart_stacked(): return get_multichart_stacked(chart_enum.MULTIPLOT.value)
def get_scatterplot_multichart_stacked(): return get_multichart_stacked(chart_enum.MULTISCATTER.value)


# In[145]:


#*******************************************************************************************
 #
 #  Function Name:  set_bar_multichart_stacked
 #                  set_boxplot_multichart_stacked
 #                  set_histogram_multichart_stacked
 #                  set_line_multichart_stacked
 #                  set_pie_multichart_stacked
 #                  set_plot_multichart_stacked
 #                  set_scatterplot_multichart_stacked
 #
 #  Function Description:
 #      The function sets the multichart's stacked boolean value.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  boolean        upd_bool         The parameter is the chart's updated stacked boolean.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_bar_multichart_stacked(input_bool): set_multichart_stacked(input_bool, chart_enum.MULTIBAR.value)
def set_boxplot_multichart_stacked(input_bool): set_multichart_stacked(input_bool, chart_enum.MULTIBOXPLOT.value)
def set_histogram_multichart_stacked(input_bool): set_multichart_stacked(input_bool, chart_enum.MULTIHISTOGRAM.value)
def set_line_multichart_stacked(input_bool): set_multichart_stacked(input_bool, chart_enum.MULTILINE.value)
def set_pie_multichart_stacked(input_bool): set_multichart_stacked(input_bool, chart_enum.MULTIPIE.value)
def set_plot_multichart_stacked(input_bool): set_multichart_stacked(input_bool, chart_enum.MULTIPLOT.value)
def set_scatterplot_multichart_stacked(input_bool): set_multichart_stacked(input_bool, chart_enum.MULTISCATTER.value)


# In[146]:


#*******************************************************************************************
 #
 #  Function Name:  get_bar_multichart_suptitle_xycoords
 #                  get_boxplot_multichart_suptitle_xycoords
 #                  get_histogram_multichart_suptitle_xycoords
 #                  get_line_multichart_suptitle_xycoords
 #                  get_pie_multichart_suptitle_xycoords
 #                  get_plot_multichart_suptitle_xycoords
 #                  get_scatterplot_multichart_suptitle_xycoords
 #
 #  Function Description:
 #      The function retrieves the multichart suptitle x and y coordinates.
 #
 #
 #  Return Type: float, float
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  enum           chart_type       The parameter is the multichart type enumeration value.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_bar_multichart_suptitle_xycoords(): return get_multichart_suptitle_xycoords(chart_enum.MULTIBAR.value)
def get_boxplot_multichart_suptitle_xycoords(): return get_multichart_suptitle_xycoords(chart_enum.MULTIBOXPLOT.value)
def get_histogram_multichart_suptitle_xycoords(): return get_multichart_suptitle_xycoords(chart_enum.MULTIHISTOGRAM.value)
def get_line_multichart_suptitle_xycoords(): return get_multichart_suptitle_xycoords(chart_enum.MULTILINE.value)
def get_pie_multichart_suptitle_xycoords(): return get_multichart_suptitle_xycoords(chart_enum.MULTIPIE.value)
def get_plot_multichart_suptitle_xycoords(): return get_multichart_suptitle_xycoords(chart_enum.MULTIPLOT.value)
def get_scatterplot_multichart_suptitle_xycoords(): return get_multichart_suptitle_xycoords(chart_enum.MULTISCATTER.value)


# In[147]:


#*******************************************************************************************
 #
 #  Function Name:  set_bar_multichart_suptitle_xycoords
 #                  set_boxplot_multichart_suptitle_xycoords
 #                  set_histogram_chart_suptitle_xycoords
 #                  set_line_multichart_suptitle_xycoords
 #                  set_pie_multichart_suptitle_xycoords
 #                  set_plot_multichart_suptitle_xycoords
 #                  set_scatterplot_multichart_suptitle_xycoords
 #
 #  Function Description:
 #      The function sets the multichart suptitle's x and y coordinates.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  float          x_flt            The parameter is the multichart suptitle's x-coordinate.
 #  float          y_flt            The parameter is the multichart suptitle's y-coordinate.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_bar_multichart_suptitle_xycoords(x_flt, y_flt): set_multichart_suptitle_xycoords(x_flt, y_flt, chart_enum.MULTIBAR.value)
def set_boxplot_multichart_suptitle_xycoords(x_flt, y_flt): set_multichart_suptitle_xycoords(x_flt, y_flt, chart_enum.MULTIBOXPLOT.value)
def set_histogram_multichart_suptitle_xycoords(x_flt, y_flt): set_multichart_suptitle_xycoords(x_flt, y_flt, chart_enum.MULTIHISTOGRAM.value)
def set_line_multichart_suptitle_xycoords(x_flt, y_flt): set_multichart_suptitle_xycoords(x_flt, y_flt, chart_enum.MULTILINE.value)
def set_pie_multichart_suptitle_xycoords(x_flt, y_flt): set_multichart_suptitle_xycoords(x_flt, y_flt, chart_enum.MULTIPIE.value)
def set_plot_multichart_suptitle_xycoords(x_flt, y_flt): set_multichart_suptitle_xycoords(x_flt, y_flt, chart_enum.MULTIPLOT.value)
def set_scatterplot_multichart_suptitle_xycoords(x_flt, y_flt): set_multichart_suptitle_xycoords(x_flt, y_flt, chart_enum.MULTISCATTER.value)


# In[148]:


#*******************************************************************************************
 #
 #  Function Name:  get_bar_multichart_supxlabel_xycoords
 #                  get_boxplot_multichart_supxlabel_xycoords
 #                  get_histogram_multichart_supxlabel_xycoords
 #                  get_line_multichart_supxlabel_xycoords
 #                  get_pie_multichart_supxlabel_xycoords
 #                  get_plot_multichart_supxlabel_xycoords
 #                  get_scatterplot_multichart_supxlabel_xycoords
 #
 #  Function Description:
 #      The function retrieves the multichart supxlabel x and y coordinates.
 #
 #
 #  Return Type: float, float
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  enum           chart_type       The parameter is the multichart type enumeration value.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_bar_multichart_supxlabel_xycoords(): return get_multichart_supxlabel_xycoords(chart_enum.MULTIBAR.value)
def get_boxplot_multichart_supxlabel_xycoords(): return get_multichart_supxlabel_xycoords(chart_enum.MULTIBOXPLOT.value)
def get_histogram_multichart_supxlabel_xycoords(): return get_multichart_supxlabel_xycoords(chart_enum.MULTIHISTOGRAM.value)
def get_line_multichart_supxlabel_xycoords(): return get_multichart_supxlabel_xycoords(chart_enum.MULTILINE.value)
def get_pie_multichart_supxlabel_xycoords(): return get_multichart_supxlabel_xycoords(chart_enum.MULTIPIE.value)
def get_plot_multichart_supxlabel_xycoords(): return get_multichart_supxlabel_xycoords(chart_enum.MULTIPLOT.value)
def get_scatterplot_multichart_supxlabel_xycoords(): return get_multichart_supxlabel_xycoords(chart_enum.MULTISCATTER.value)


# In[149]:


#*******************************************************************************************
 #
 #  Function Name:  set_bar_multichart_supxlabel_xycoords
 #                  set_boxplot_multichart_supxlabel_xycoords
 #                  set_histogram_chart_supxlabel_xycoords
 #                  set_line_multichart_supxlabel_xycoords
 #                  set_pie_multichart_supxlabel_xycoords
 #                  set_plot_multichart_supxlabel_xycoords
 #                  set_scatterplot_multichart_supxlabel_xycoords
 #
 #  Function Description:
 #      The function sets the multichart supxlabel's x and y coordinates.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  float          x_flt            The parameter is the multichart supxlabel's x-coordinate.
 #  float          y_flt            The parameter is the multichart supxlabel's y-coordinate.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_bar_multichart_supxlabel_xycoords(x_flt, y_flt): set_multichart_supxlabel_xycoords(x_flt, y_flt, chart_enum.MULTIBAR.value)
def set_boxplot_multichart_supxlabel_xycoords(x_flt, y_flt): set_multichart_supxlabel_xycoords(x_flt, y_flt, chart_enum.MULTIBOXPLOT.value)
def set_histogram_multichart_supxlabel_xycoords(x_flt, y_flt): set_multichart_supxlabel_xycoords(x_flt, y_flt, chart_enum.MULTIHISTOGRAM.value)
def set_line_multichart_supxlabel_xycoords(x_flt, y_flt): set_multichart_supxlabel_xycoords(x_flt, y_flt, chart_enum.MULTILINE.value)
def set_pie_multichart_supxlabel_xycoords(x_flt, y_flt): set_multichart_supxlabel_xycoords(x_flt, y_flt, chart_enum.MULTIPIE.value)
def set_plot_multichart_supxlabel_xycoords(x_flt, y_flt): set_multichart_supxlabel_xycoords(x_flt, y_flt, chart_enum.MULTIPLOT.value)
def set_scatterplot_multichart_supxlabel_xycoords(x_flt, y_flt): set_multichart_supxlabel_xycoords(x_flt, y_flt, chart_enum.MULTISCATTER.value)


# In[150]:


#*******************************************************************************************
 #
 #  Function Name:  get_bar_multichart_supylabel_xycoords
 #                  get_boxplot_multichart_supylabel_xycoords
 #                  get_histogram_multichart_supylabel_xycoords
 #                  get_line_multichart_supylabel_xycoords
 #                  get_pie_multichart_supylabel_xycoords
 #                  get_plot_multichart_supylabel_xycoords
 #                  get_scatterplot_multichart_supylabel_xycoords
 #
 #  Function Description:
 #      The function retrieves the multichart supylabel x and y coordinates.
 #
 #
 #  Return Type: float, float
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  enum           chart_type       The parameter is the multichart type enumeration value.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_bar_multichart_supylabel_xycoords(): return get_multichart_supylabel_xycoords(chart_enum.MULTIBAR.value)
def get_boxplot_multichart_supylabel_xycoords(): return get_multichart_supylabel_xycoords(chart_enum.MULTIBOXPLOT.value)
def get_histogram_multichart_supylabel_xycoords(): return get_multichart_supylabel_xycoords(chart_enum.MULTIHISTOGRAM.value)
def get_line_multichart_supylabel_xycoords(): return get_multichart_supylabel_xycoords(chart_enum.MULTILINE.value)
def get_pie_multichart_supylabel_xycoords(): return get_multichart_supylabel_xycoords(chart_enum.MULTIPIE.value)
def get_plot_multichart_supylabel_xycoords(): return get_multichart_supylabel_xycoords(chart_enum.MULTIPLOT.value)
def get_scatterplot_multichart_supylabel_xycoords(): return get_multichart_supylabel_xycoords(chart_enum.MULTISCATTER.value)


# In[151]:


#*******************************************************************************************
 #
 #  Function Name:  set_bar_multichart_supylabel_xycoords
 #                  set_boxplot_multichart_supylabel_xycoords
 #                  set_histogram_chart_supylabel_xycoords
 #                  set_line_multichart_supylabel_xycoords
 #                  set_pie_multichart_supylabel_xycoords
 #                  set_plot_multichart_supylabel_xycoords
 #                  set_scatterplot_multichart_supylabel_xycoords
 #
 #  Function Description:
 #      The function sets the multichart supylabel's x and y coordinates.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  float          x_flt            The parameter is the multichart supylabel's x-coordinate.
 #  float          y_flt            The parameter is the multichart supylabel's y-coordinate.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_bar_multichart_supylabel_xycoords(x_flt, y_flt): set_multichart_supylabel_xycoords(x_flt, y_flt, chart_enum.MULTIBAR.value)
def set_boxplot_multichart_supylabel_xycoords(x_flt, y_flt): set_multichart_supylabel_xycoords(x_flt, y_flt, chart_enum.MULTIBOXPLOT.value)
def set_histogram_multichart_supylabel_xycoords(x_flt, y_flt): set_multichart_supylabel_xycoords(x_flt, y_flt, chart_enum.MULTIHISTOGRAM.value)
def set_line_multichart_supylabel_xycoords(x_flt, y_flt): set_multichart_supylabel_xycoords(x_flt, y_flt, chart_enum.MULTILINE.value)
def set_pie_multichart_supylabel_xycoords(x_flt, y_flt): set_multichart_supylabel_xycoords(x_flt, y_flt, chart_enum.MULTIPIE.value)
def set_plot_multichart_supylabel_xycoords(x_flt, y_flt): set_multichart_supylabel_xycoords(x_flt, y_flt, chart_enum.MULTIPLOT.value)
def set_scatterplot_multichart_supylabel_xycoords(x_flt, y_flt): set_multichart_supylabel_xycoords(x_flt, y_flt, chart_enum.MULTISCATTER.value)


# In[152]:


#*******************************************************************************************
 #
 #  Function Name:  get_bar_multichart_suptitle_fontsize
 #                  get_boxplot_multichart_suptitle_fontsize
 #                  get_histogram_multichart_suptitle_fontsize
 #                  get_line_multichart_suptitle_fontsize
 #                  get_pie_multichart_suptitle_fontsize
 #                  get_plot_multichart_suptitle_fontsize
 #                  get_scatterplot_multichart_suptitle_fontsize
 #
 #  Function Description:
 #      The function retrieves the multichart suptitle font size.
 #
 #
 #  Return Type: float
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  enum           chart_type       The parameter is the multichart type enumeration value.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_bar_multichart_suptitle_fontsize(): return get_multichart_suptitle_fontsize(chart_enum.MULTIBAR.value)
def get_boxplot_multichart_suptitle_fontsize(): return get_multichart_suptitle_fontsize(chart_enum.MULTIBOXPLOT.value)
def get_histogram_multichart_suptitle_fontsize(): return get_multichart_suptitle_fontsize(chart_enum.MULTIHISTOGRAM.value)
def get_line_multichart_suptitle_fontsize(): return get_multichart_suptitle_fontsize(chart_enum.MULTILINE.value)
def get_pie_multichart_suptitle_fontsize(): return get_multichart_suptitle_fontsize(chart_enum.MULTIPIE.value)
def get_plot_multichart_suptitle_fontsize(): return get_multichart_suptitle_fontsize(chart_enum.MULTIPLOT.value)
def get_scatterplot_multichart_suptitle_fontsize(): return get_multichart_suptitle_fontsize(chart_enum.MULTISCATTER.value)


# In[153]:


#*******************************************************************************************
 #
 #  Function Name:  set_bar_multichart_suptitle_fontsize
 #                  set_boxplot_multichart_suptitle_fontsize
 #                  set_histogram_chart_suptitle_fontsize
 #                  set_line_multichart_suptitle_fontsize
 #                  set_pie_multichart_suptitle_fontsize
 #                  set_plot_multichart_suptitle_fontsize
 #                  set_scatterplot_multichart_suptitle_fontsize
 #
 #  Function Description:
 #      The function sets the multichart suptitle's font size.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  float          fnt_sz_flt       The parameter is the multichart suptitle's font size.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_bar_multichart_suptitle_fontsize(fnt_sz_flt): set_multichart_suptitle_fontsize(fnt_sz_flt, chart_enum.MULTIBAR.value)
def set_boxplot_multichart_suptitle_fontsize(fnt_sz_flt): set_multichart_suptitle_fontsize(fnt_sz_flt, chart_enum.MULTIBOXPLOT.value)
def set_histogram_multichart_suptitle_fontsize(fnt_sz_flt): set_multichart_suptitle_fontsize(fnt_sz_flt, chart_enum.MULTIHISTOGRAM.value)
def set_line_multichart_suptitle_fontsize(fnt_sz_flt): set_multichart_suptitle_fontsize(fnt_sz_flt, chart_enum.MULTILINE.value)
def set_pie_multichart_suptitle_fontsize(fnt_sz_flt): set_multichart_suptitle_fontsize(fnt_sz_flt, chart_enum.MULTIPIE.value)
def set_plot_multichart_suptitle_fontsize(fnt_sz_flt): set_multichart_suptitle_fontsize(fnt_sz_flt, chart_enum.MULTIPLOT.value)
def set_scatterplot_multichart_suptitle_fontsize(fnt_sz_flt): set_multichart_suptitle_fontsize(fnt_sz_flt, chart_enum.MULTISCATTER.value)


# In[154]:


#*******************************************************************************************
 #
 #  Function Name:  get_bar_multichart_supxlabel_fontsize
 #                  get_boxplot_multichart_supxlabel_fontsize
 #                  get_histogram_multichart_supxlabel_fontsize
 #                  get_line_multichart_supxlabel_fontsize
 #                  get_pie_multichart_supxlabel_fontsize
 #                  get_plot_multichart_supxlabel_fontsize
 #                  get_scatterplot_multichart_supxlabel_fontsize
 #
 #  Function Description:
 #      The function retrieves the multichart supxlabel font size.
 #
 #
 #  Return Type: float
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  enum           chart_type       The parameter is the multichart type enumeration value.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_bar_multichart_supxlabel_fontsize(): return get_multichart_supxlabel_fontsize(chart_enum.MULTIBAR.value)
def get_boxplot_multichart_supxlabel_fontsize(): return get_multichart_supxlabel_fontsize(chart_enum.MULTIBOXPLOT.value)
def get_histogram_multichart_supxlabel_fontsize(): return get_multichart_supxlabel_fontsize(chart_enum.MULTIHISTOGRAM.value)
def get_line_multichart_supxlabel_fontsize(): return get_multichart_supxlabel_fontsize(chart_enum.MULTILINE.value)
def get_pie_multichart_supxlabel_fontsize(): return get_multichart_supxlabel_fontsize(chart_enum.MULTIPIE.value)
def get_plot_multichart_supxlabel_fontsize(): return get_multichart_supxlabel_fontsize(chart_enum.MULTIPLOT.value)
def get_scatterplot_multichart_supxlabel_fontsize(): return get_multichart_supxlabel_fontsize(chart_enum.MULTISCATTER.value)


# In[155]:


#*******************************************************************************************
 #
 #  Function Name:  set_bar_multichart_supxlabel_fontsize
 #                  set_boxplot_multichart_supxlabel_fontsize
 #                  set_histogram_chart_supxlabel_fontsize
 #                  set_line_multichart_supxlabel_fontsize
 #                  set_pie_multichart_supxlabel_fontsize
 #                  set_plot_multichart_supxlabel_fontsize
 #                  set_scatterplot_multichart_supxlabel_fontsize
 #
 #  Function Description:
 #      The function sets the multichart supxlabel's font size.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  float          fnt_sz_flt       The parameter is the multichart supxlabel's font size.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_bar_multichart_supxlabel_fontsize(fnt_sz_flt): set_multichart_supxlabel_fontsize(fnt_sz_flt, chart_enum.MULTIBAR.value)
def set_boxplot_multichart_supxlabel_fontsize(fnt_sz_flt): set_multichart_supxlabel_fontsize(fnt_sz_flt, chart_enum.MULTIBOXPLOT.value)
def set_histogram_multichart_supxlabel_fontsize(fnt_sz_flt): set_multichart_supxlabel_fontsize(fnt_sz_flt, chart_enum.MULTIHISTOGRAM.value)
def set_line_multichart_supxlabel_fontsize(fnt_sz_flt): set_multichart_supxlabel_fontsize(fnt_sz_flt, chart_enum.MULTILINE.value)
def set_pie_multichart_supxlabel_fontsize(fnt_sz_flt): set_multichart_supxlabel_fontsize(fnt_sz_flt, chart_enum.MULTIPIE.value)
def set_plot_multichart_supxlabel_fontsize(fnt_sz_flt): set_multichart_supxlabel_fontsize(fnt_sz_flt, chart_enum.MULTIPLOT.value)
def set_scatterplot_multichart_supxlabel_fontsize(fnt_sz_flt): set_multichart_supxlabel_fontsize(fnt_sz_flt, chart_enum.MULTISCATTER.value)


# In[156]:


#*******************************************************************************************
 #
 #  Function Name:  get_bar_multichart_supylabel_fontsize
 #                  get_boxplot_multichart_supylabel_fontsize
 #                  get_histogram_multichart_supylabel_fontsize
 #                  get_line_multichart_supylabel_fontsize
 #                  get_pie_multichart_supylabel_fontsize
 #                  get_plot_multichart_supylabel_fontsize
 #                  get_scatterplot_multichart_supylabel_fontsize
 #
 #  Function Description:
 #      The function retrieves the multichart supylabel font size.
 #
 #
 #  Return Type: float
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  enum           chart_type       The parameter is the multichart type enumeration value.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_bar_multichart_supylabel_fontsize(): return get_multichart_supylabel_fontsize(chart_enum.MULTIBAR.value)
def get_boxplot_multichart_supylabel_fontsize(): return get_multichart_supylabel_fontsize(chart_enum.MULTIBOXPLOT.value)
def get_histogram_multichart_supylabel_fontsize(): return get_multichart_supylabel_fontsize(chart_enum.MULTIHISTOGRAM.value)
def get_line_multichart_supylabel_fontsize(): return get_multichart_supylabel_fontsize(chart_enum.MULTILINE.value)
def get_pie_multichart_supylabel_fontsize(): return get_multichart_supylabel_fontsize(chart_enum.MULTIPIE.value)
def get_plot_multichart_supylabel_fontsize(): return get_multichart_supylabel_fontsize(chart_enum.MULTIPLOT.value)
def get_scatterplot_multichart_supylabel_fontsize(): return get_multichart_supylabel_fontsize(chart_enum.MULTISCATTER.value)


# In[157]:


#*******************************************************************************************
 #
 #  Function Name:  set_bar_multichart_supylabel_fontsize
 #                  set_boxplot_multichart_supylabel_fontsize
 #                  set_histogram_chart_supylabel_fontsize
 #                  set_line_multichart_supylabel_fontsize
 #                  set_pie_multichart_supylabel_fontsize
 #                  set_plot_multichart_supylabele_fontsize
 #                  set_scatterplot_multichart_supylabel_fontsize
 #
 #  Function Description:
 #      The function sets the multichart supylabel's font size.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  float          fnt_sz_flt       The parameter is the multichart supylabel's font size.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_bar_multichart_supylabel_fontsize(fnt_sz_flt): set_multichart_supylabel_fontsize(fnt_sz_flt, chart_enum.MULTIBAR.value)
def set_boxplot_multichart_supylabel_fontsize(fnt_sz_flt): set_multichart_supylabel_fontsize(fnt_sz_flt, chart_enum.MULTIBOXPLOT.value)
def set_histogram_multichart_supylabel_fontsize(fnt_sz_flt): set_multichart_supylabel_fontsize(fnt_sz_flt, chart_enum.MULTIHISTOGRAM.value)
def set_line_multichart_supylabel_fontsize(fnt_sz_flt): set_multichart_supylabel_fontsize(fnt_sz_flt, chart_enum.MULTILINE.value)
def set_pie_multichart_supylabel_fontsize(fnt_sz_flt): set_multichart_supylabel_fontsize(fnt_sz_flt, chart_enum.MULTIPIE.value)
def set_plot_multichart_supylabel_fontsize(fnt_sz_flt): set_multichart_supylabel_fontsize(fnt_sz_flt, chart_enum.MULTIPLOT.value)
def set_scatterplot_multichart_supylabel_fontsize(fnt_sz_flt): set_multichart_supylabel_fontsize(fnt_sz_flt, chart_enum.MULTISCATTER.value)


# In[158]:


#*******************************************************************************************
 #
 #  Function Name:  get_bar_multichart_xysuplabels
 #                  get_boxplot_multichart_xysuplabels
 #                  get_histogram_multichart_xylabels
 #                  get_line_multichart_xysuplabels
 #                  get_pie_multichart_xysuplabels
 #                  get_plot_multichart_xysuplabels
 #                  get_scatterplot_multichart_xysuplabels
 #
 #  Function Description:
 #      The function retrieves the multichart's x-axis suplabel and y-axis suplabel.
 #
 #
 #  Return Type: string, string
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  enum           chart_type       The parameter is the multichart type enumeration value.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_bar_multichart_xysuplabels(): return get_multichart_xysuplabels(chart_enum.MULTIBAR.value)
def get_boxplot_multichart_xysuplabels(): return get_multichart_xysuplabels(chart_enum.MULTIBOXPLOT.value)
def get_histogram_multichart_xylabels(): return get_multichart_xysuplabels(chart_enum.MULTIHISTOGRAM.value)
def get_line_multichart_xysuplabels(): return get_multichart_xysuplabels(chart_enum.MULTILINE.value)
def get_pie_multichart_xysuplabels(): return get_multichart_xysuplabels(chart_enum.MULTIPIE.value)
def get_plot_multichart_xysuplabels(): return get_multichart_xysuplabels(chart_enum.MULTIPLOT.value)
def get_scatterplot_multichart_xysuplabels(): return get_multichart_xysuplabels(chart_enum.MULTISCATTER.value)


# In[159]:


#*******************************************************************************************
 #
 #  Function Name:  set_bar_multichart_xysuplabels
 #                  set_boxplot_multichart_xysuplabels
 #                  set_histogram_chart_xylabels
 #                  set_line_multichart_xysuplabels
 #                  set_pie_multichart_xysuplabels
 #                  set_plot_multichart_xysuplabels
 #                  set_scatterplot_multichart_xysuplabels
 #
 #  Function Description:
 #      The function sets the multichart's x-axis suplabel and y-axis suplabel.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  string         xsuplabel        The parameter is the multichart's x-axis suplabel.
 #  string         ysuplabel        The parameter is the multichart's y-axis suplabel.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_bar_multichart_xysuplabels(xsuplabel, ysuplabel): set_multichart_xysuplabels(xsuplabel, ysuplabel, chart_enum.MULTIBAR.value)
def set_boxplot_multichart_xysuplabels(xsuplabel, ysuplabel): set_multichart_xysuplabels(xsuplabel, ysuplabel, chart_enum.MULTIBOXPLOT.value)
def set_histogram_multichart_xysuplabels(xsuplabel, ysuplabel): set_multichart_xysuplabels(xsuplabel, ysuplabel, chart_enum.MULTIHISTOGRAM.value)
def set_line_multichart_xysuplabels(xsuplabel, ysuplabel): set_multichart_xysuplabels(xsuplabel, ysuplabel, chart_enum.MULTILINE.value)
def set_pie_multichart_xysuplabels(xsuplabel, ysuplabel): set_multichart_xysuplabels(xsuplabel, ysuplabel, chart_enum.MULTIPIE.value)
def set_plot_multichart_xysuplabels(xsuplabel, ysuplabel): set_multichart_xysuplabels(xsuplabel, ysuplabel, chart_enum.MULTIPLOT.value)
def set_scatterplot_multichart_xysuplabels(xsuplabel, ysuplabel): set_multichart_xysuplabels(xsuplabel, ysuplabel, chart_enum.MULTISCATTER.value)


# In[160]:


#*******************************************************************************************
 #
 #  Function Name:  proc_bar_chart_input
 #
 #  Function Description:
 #      The function takes input for a bar chart and processes it for display. If the
 #      input is a Series or Dataframe, the function returns it unchanged. If the input
 #      is a Series dictionary, Series list, or Series array, the function converts
 #      the data to a Dataframe and returns it. Otherwise, the function returns None.
 #
 #
 #  Return Type: series or dataframe or none
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

def proc_bar_chart_input(input_obj):

    if isinstance(input_obj, pd.Series) \
        or isinstance(input_obj, pd.DataFrame): return input_obj

    elif isinstance(input_obj, dict) \
        or isinstance(input_obj, list) \
        or isinstance(input_obj, np.ndarray): return pd.DataFrame(input_obj)

    else: return None


# In[161]:


#*******************************************************************************************
 #
 #  Function Name:  setup_stacked_line_charts
 #
 #  Function Description:
 #      The function sets the parameters for stacked line charts.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  integer        nmbr_chrts       The parameter is the number of charts.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def setup_stacked_line_charts(nmbr_chrts):

    none_array = np.array([None] * nmbr_chrts)


    set_line_chart_title(none_array)

    set_line_chart_colors(stacked_line_chart_colors)

    set_line_chart_xylabels_display(False, False)

    set_line_chart_xylabels(none_array, none_array)

    set_line_chart_xyticks_fontsize(10.0, 10.0)

    set_line_chart_legend_fontsize(10.0)

    set_line_chart_legend_display(True)


    set_line_multichart_fig_dims(15.0, 5.5181)

    set_line_multichart_suptitle_fontsize(18.0)

    set_line_multichart_supxlabel_fontsize(14.0)

    set_line_multichart_supylabel_fontsize(14.0)

    set_line_multichart_stacked(True)


# In[162]:


#*******************************************************************************************
 #
 #  Function Name:  proc_boxplot_chart_input
 #
 #  Function Description:
 #      The function takes input for a boxplot chart and processes it for display. If
 #      the input is a Series list [data, labels] or a DataFrame, the function retrieves 
 #      and returns the data and labels. Otherwise, the function returns None for both 
 #      the data and labels.
 #
 #
 #  Return Type: series, array, or none
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

def proc_boxplot_chart_input(input_obj):

    if isinstance(input_obj, list) and len(input_obj) >= 2:

        data = input_obj[0]

        labels = np.array(input_obj[1])

    elif isinstance(input_obj, pd.DataFrame):

        labels \
            = input_obj[boxplot_chart_dict['params']['x_col']].unique()

        data \
            = [input_obj \
                [input_obj \
                    [boxplot_chart_dict['params']['x_col']] == lbl] \
                    [boxplot_chart_dict['params']['y_col']] \
                        .dropna().values \
               for lbl in labels]

    else: data, labels = None, None


    return data, labels


# In[163]:


#*******************************************************************************************
 #
 #  Function Name:  proc_line_chart_input
 #
 #  Function Description:
 #      The function takes input for a bar chart and processes it for display. If the
 #      input is a Series or Dataframe, the function returns it unchanged. If the input
 #      is a Series list or Series array, the function converts the data to a Series 
 #      and returns it. Otherwise, the function returns None.
 #
 #
 #  Return Type: series or dataframe or none
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

def proc_line_chart_input(input_obj):

    if isinstance(input_obj, pd.Series) \
        or isinstance(input_obj, pd.DataFrame):

        return input_obj

    elif isinstance(input_obj, list \
          or isinstance(input_obj, np.ndarray)) \
            and len(input_obj) >= 2:

        index = dtypesx.cnv_data_to_array(input_obj[0])

        data = dtypesx.cnv_data_to_array(input_obj[1])

        input_series = pd.Series(data, index = index)

        return input_series

    else: return None


# In[164]:


#*******************************************************************************************
 #
 #  Function Name:  proc_pie_chart_input
 #
 #  Function Description:
 #      The function takes input for a pie chart and processes it for display. If the
 #      input is a Series, Series list, Series tuple, or Series array, the function 
 #      retrieves and returns the data and labels. Otherwise, the function returns None 
 #      for both the data and labels.
 #
 #
 #  Return Type: array, array or none, none
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

def proc_pie_chart_input(input_obj):

    if isinstance(input_obj, pd.Series):

        data = input_obj.to_numpy()

        labels = input_obj.index.to_numpy()

    elif isinstance(input_obj, list) \
            or isinstance(input_obj, tuple) \
            or isinstance(input_obj, np.ndarray):

        data = dtypesx.cnv_data_to_array(input_obj[0])

        labels = dtypesx.cnv_data_to_array(input_obj[1])

    else: data, labels = None, None


    return data, labels


# In[165]:


#*******************************************************************************************
 #
 #  Function Name:  proc_plot_chart_input
 #
 #  Function Description:
 #      The function takes input for a plot chart and processes it for display. If the
 #      input is a Series, Series list, Series tuple, or Series array, the function 
 #      retrieves and returns the x-axis and y-axis data as a Series. Otherwise, the 
 #      function returns None.
 #
 #
 #  Return Type: series or none
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

def proc_plot_chart_input(input_obj):

    if isinstance(input_obj, pd.Series):

        temp_obj = input_obj

    elif isinstance(input_obj, list) \
            or isinstance(input_obj, tuple) \
            or isinstance(input_obj, np.ndarray):

        index = dtypesx.cnv_data_to_array(input_obj[0])

        data = dtypesx.cnv_data_to_array(input_obj[1])

        temp_obj = pd.Series(data, index = index)

    else: temp_obj = None


    return temp_obj


# In[166]:


#*******************************************************************************************
 #
 #  Function Name:  proc_scatterplot_chart_input
 #
 #  Function Description:
 #      The function takes input for a scatterplot chart and processes it for display. 
 #      If the input is a Series, Series list, Series tuple, or Series array, the 
 #      function retrieves and returns the x-axis and y-axis data. Otherwise, the 
 #      function returns None for both data.
 #
 #
 #  Return Type: array, array or none, none
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

def proc_scatterplot_chart_input(input_obj):

    if (isinstance(input_obj, list) \
            or isinstance(input_obj, np.ndarray)\
            or isinstance(input_obj, tuple)) \
                and len(input_obj) >= 2:

        x_array = dtypesx.cnv_data_to_array(input_obj[0])

        y_array = dtypesx.cnv_data_to_array(input_obj[1])

    elif isinstance(input_obj, pd.Series):

        y_array = input_obj.index.to_numpy()

        x_array = input_obj.to_numpy()

    else: x_array, y_array = None, None


    return x_array, y_array


# In[167]:


#*******************************************************************************************
 #
 #  Function Name:  proc_pie_multichart_input
 #
 #  Function Description:
 #      The function takes a dataframe, dictionary, or list as input for a pie multichart 
 #      and returns a dataframe.
 #
 #
 #  Return Type: dataframe
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

def proc_pie_multichart_input(input_obj):

    if isinstance(input_obj, pd.DataFrame): return input_obj

    elif isinstance(input_obj, dict): return pd.DataFrame(input_obj)

    elif isinstance(input_obj, list): return pd.DataFrame(input_obj)

    else: None


# In[168]:


#*******************************************************************************************
 #
 #  Function Name:  proc_scatterplot_multichart_input
 #
 #  Function Description:
 #      The function takes input for a scatterplot multichart and processes it for 
 #      display. If the input is a list of Series lists or DataFrame, the function
 #      retrieves and returns the x-axis and y-axis data. Otherwise, the function
 #      returns None for both data.
 #
 #
 #  Return Type: list, list or none, none
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

def proc_scatterplot_multichart_input(input_obj):

    if isinstance(input_obj, list):

        return input_obj[0], input_obj[1]

    elif isinstance(input_obj, pd.DataFrame):

        x_list = []

        y_list = []

        for idx in range(len(input_obj.columns)):

            x_list.append(pd.Series(list(input_obj.index)))

            y_list.append(input_obj.iloc[:, idx])

        return x_list, y_list

    else: return None, None


# In[169]:


#*******************************************************************************************
 #
 #  Function Name:  proc_chart_input
 #
 #  Function Description:
 #      The function takes input for a chart and processes it for display.
 #
 #
 #  Return Type: series / dataframe / series, array / array, array
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  object         input_obj        The parameter is the input object.
 #  enueration     chart_enum_value The parameter indicates the chart type.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def proc_chart_input(input_obj, chart_enum_value):

    if chart_enum_value == chart_enum.LINE.value:

        return proc_line_chart_input(input_obj)

    elif chart_enum_value == chart_enum.BOXPLOT.value:

        return proc_boxplot_chart_input(input_obj)

    elif chart_enum_value == chart_enum.BAR.value:

        return proc_bar_chart_input(input_obj)

    elif chart_enum_value == chart_enum.SCATTER.value:

        return proc_scatterplot_chart_input(input_obj)

    elif chart_enum_value == chart_enum.PIE.value:

        return proc_pie_chart_input(input_obj)

    elif chart_enum_value == chart_enum.HISTOGRAM.value:

        return dtypesx.cnv_data_to_array(input_obj)

    elif chart_enum_value == chart_enum.PLOT.value:

        return proc_plot_chart_input(input_obj)

    elif chart_enum_value == chart_enum.MULTILINE.value:

        return None

    elif chart_enum_value == chart_enum.MULTIPIE.value:

        return proc_pie_multichart_input(input_obj)

    elif chart_enum_value == chart_enum.MULTISCATTER.value:

        return proc_scatterplot_multichart_input(input_obj)


# In[2]:


#*******************************************************************************************
 #
 #  Function Name:  linear_regr_line
 #
 #  Function Description:
 #      The function displays a linear regression line on a chart.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  object         x_obj            The parameter is the x-axis data.
 #  object         y_obj            The parameter is the y-axis data.
 #  float          x_coord_flt      The parameter is the x-coordinate of the text.   
 #  float          y_coord_flt      The parameter is the y-coordinate of the text.
 #  float          coef_prec        The parameter is the coefficient's precision.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def linear_regr_line \
        (x_obj,
         y_obj,
         x_coord_flt,
         y_coord_flt,
         coef_prec = 4):

    x_array = dtypesx.cnv_data_to_array(x_obj)

    y_array = dtypesx.cnv_data_to_array(y_obj)


    (slope, intercept, rvalue, pvalue, stderr) \
        = stats.linregress(x_array, y_array)

    linear_regr_array \
        = (x_array * slope) + intercept


    plt.plot \
        (x_array,
         linear_regr_array,
         color = regr_line_dict['linecolor'],
         linewidth = regr_line_dict['linewidth'],
         alpha = regr_line_dict['alpha'])

    linear_eqn \
        = 'y = ' + f'{slope:,.2e}' \
          + 'x + ' + f'{intercept:,.2e}'

    plt.annotate \
        (linear_eqn,
         (x_coord_flt, y_coord_flt),
         fontsize = regr_line_dict['fontsize'],
         fontweight = regr_line_dict['fontweight'],
         color = regr_line_dict['fontcolor'])   


    rslt_dict = mathx.rtn_stats_values(x_array, y_array)

    proc_rvalues(rslt_dict)


# In[1]:


#*******************************************************************************************
 #
 #  Function Name:  regr_line
 #
 #  Function Description:
 #      The function displays a regression line on a chart.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  object         x_obj            The parameter is the x-axis data.
 #  object         y_obj            The parameter is the y-axis data.
 #  float          x_coord_flt      The parameter is the x-coordinate of the text.   
 #  float          y_coord_flt      The parameter is the y-coordinate of the text.
 #  integer        degree_int       The parameter is the regression polynomial degree.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def regr_line \
        (x_obj,
         y_obj,
         x_coord_flt,
         y_coord_flt,
         degree_int = 1):

    if degree_int <= 1:

        linear_regr_line \
            (x_obj, y_obj,
             x_coord_flt,
             y_coord_flt,
             regr_line_dict['coef_prec'])

        return


    x_array = dtypesx.cnv_data_to_array(x_obj)

    y_array = dtypesx.cnv_data_to_array(y_obj)


    model_eqn_array \
        = mathx.regr_model_eqn_coef \
            (x_array, y_array, 
             degree_int)

    poly_line_array \
        = mathx.rtn_poly_line_array \
            (x_array, y_array)


    model_eqn_disp_array \
        = mathx.regr_model_eqn_coef_disp \
            (x_array, y_array, 
             degree_int,
             regr_line_dict['coef_prec'])

    eqn_lbl \
        = mathx.rtn_eqn_as_text \
            (model_eqn_disp_array,
             regr_line_dict['coef_prec'])


    plt.plot \
        (poly_line_array, 
         model_eqn_array(poly_line_array),
         color = regr_line_dict['linecolor'],
         linewidth = regr_line_dict['linewidth'],
         alpha = regr_line_dict['alpha'])

    plt.annotate \
        (eqn_lbl,
         (x_coord_flt, y_coord_flt),
         fontsize = regr_line_dict['fontsize'],
         fontweight = regr_line_dict['fontweight'],
         color = regr_line_dict['fontcolor'])


    rslt_dict = mathx.rtn_stats_values(x_array, y_array)

    proc_rvalues(rslt_dict)


# In[172]:


#*******************************************************************************************
 #
 #  Function Name:  plot_subplots
 #
 #  Function Description:
 #      The function plots the figure subplots for the multichart.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  dictionary     chart_dict       The parameter is the chart dictionary.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def plot_subplots(chart_dict):

    if chart_dict['figure']['stacked']:

        return \
            plt.subplots \
                (chart_dict['figure']['nplots'], 
                 figsize 
                     = (chart_dict['figure']['width'], 
                        chart_dict['figure']['length']),
                 sharex = chart_dict['figure']['sharex'],
                 sharey = chart_dict['figure']['sharey'])

    else:

        return \
            plt.subplots \
                (figsize 
                     = (chart_dict['figure']['width'], 
                        chart_dict['figure']['length']),
                 nrows = chart_dict['figure']['nrows'], 
                 ncols = chart_dict['figure']['ncols'],
                 sharex = chart_dict['figure']['sharex'],
                 sharey = chart_dict['figure']['sharey'])


# In[173]:


#*******************************************************************************************
 #
 #  Function Name:  plot_subplot
 #
 #  Function Description:
 #      The function plots the figure subplot in the multichart.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  dictionary     chart_dict       The parameter is the chart dictionary.
 #  integer        idx              The parameter is the plot index minus one.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def plot_subplot(chart_dict, idx):

    plt.subplot \
        (chart_dict['figure']['nrows'], 
         chart_dict['figure']['ncols'], 
         idx + 1)


# In[174]:


#*******************************************************************************************
 #
 #  Function Name:  plot_figsize
 #
 #  Function Description:
 #      The function plots the figure dimensions.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  dictionary     chart_dict       The parameter is the chart dictionary.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def plot_figsize(chart_dict):

    return \
        plt.figure \
            (figsize \
                = (chart_dict['figure']['width'], 
                   chart_dict['figure']['length']))


# In[175]:


#*******************************************************************************************
 #
 #  Function Name:  plot_title_axes_stacked
 #
 #  Function Description:
 #      The function plots the stacked multichart's title, x-axis label, and y-axis label.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  object         subplot          The parameter is the subplot object.
 #  dictionary     chart_dict       The parameter is the chart dictionary.
 #  integer        idx              The parameter is the plot index.
 #  integer        last_idx         The parameter is the last plot index.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def plot_title_axes_stacked \
        (subplot,
         chart_dict,
         idx,
         last_idx):

    if chart_dict['title']['display'] \
        and chart_dict['title']['text'][idx] is not None:

        subplot.set_title \
            (chart_dict['title']['text'][idx],
             fontdict = {'fontsize': chart_dict['title']['fontsize'], 
                         'fontstyle': chart_dict['title']['fontstyle'],
                         'fontweight': chart_dict['title']['fontweight']},
             loc = chart_dict['title']['loc'], 
             pad = chart_dict['title']['pad'])        

    if chart_dict['xlabel']['display'] \
        and chart_dict['xlabel']['text'][idx] is not None \
        and idx == last_idx:

        subplot.set_xlabel \
            (chart_dict['xlabel']['text'][idx],  
             fontsize = chart_dict['xlabel']['fontsize'], 
             fontstyle = chart_dict['xlabel']['fontstyle'], 
             fontweight = chart_dict['xlabel']['fontweight'],
             labelpad = chart_dict['xlabel']['labelpad'],
             loc = chart_dict['xlabel']['loc'])

    if chart_dict['ylabel']['display'] \
        and chart_dict['ylabel']['text'][idx] is not None:

        subplot.set_ylabel \
            (chart_dict['ylabel']['text'][idx],  
             fontsize = chart_dict['ylabel']['fontsize'], 
             fontstyle = chart_dict['ylabel']['fontstyle'], 
             fontweight = chart_dict['ylabel']['fontweight'],
             labelpad = chart_dict['ylabel']['labelpad'],
             loc = chart_dict['ylabel']['loc'])


# In[176]:


#*******************************************************************************************
 #
 #  Function Name:  plot_title_axes
 #
 #  Function Description:
 #      The function plots the chart's title, x-axis label, and y-axis label.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  dictionary     chart_dict       The parameter is the chart dictionary.
 #  integer        idx              The parameter is the plot index.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def plot_title_axes(chart_dict, idx = 0):

    if chart_dict['title']['display'] and chart_dict['title']['text'][idx] is not None:

        plt.title \
            (chart_dict['title']['text'][idx],
             fontdict = {'fontsize': chart_dict['title']['fontsize'], 
                         'fontstyle': chart_dict['title']['fontstyle'],
                         'fontweight': chart_dict['title']['fontweight']},
             loc = chart_dict['title']['loc'],
             pad = chart_dict['title']['pad'])

    if chart_dict['xlabel']['display'] and chart_dict['xlabel']['text'][idx] is not None:

        plt.xlabel \
            (chart_dict['xlabel']['text'][idx],
             fontdict = {'fontsize': chart_dict['xlabel']['fontsize'],
                         'fontstyle': chart_dict['xlabel']['fontstyle'],
                         'fontweight': chart_dict['title']['fontweight']},
             loc = chart_dict['xlabel']['loc'],
             labelpad = chart_dict['xlabel']['pad'])

    if chart_dict['ylabel']['display'] and chart_dict['ylabel']['text'][idx] is not None:

        plt.ylabel \
            (chart_dict['ylabel']['text'][idx],
             fontdict = {'fontsize': chart_dict['ylabel']['fontsize'],
                         'fontstyle': chart_dict['ylabel']['fontstyle'],
                         'fontweight': chart_dict['title']['fontweight']},
             loc = chart_dict['ylabel']['loc'],
             labelpad = chart_dict['ylabel']['pad'])   


# In[177]:


#*******************************************************************************************
 #
 #  Function Name:  plot_limits_stacked
 #
 #  Function Description:
 #      The function sets the x-axis and y-axis limits for a stacked multichart.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  object         subplot          The parameter is the subplot object.
 #  dictionary     chart_dict       The parameter is the chart dictionary.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def plot_limits_stacked(subplot, chart_dict):

    if chart_dict['xlim']['display']:

        if chart_dict['xlim']['mode'] == 'set':

            subplot.set_xlim \
                (bottom = chart_dict['xlim']['set']['min'], 
                 top = chart_dict['xlim']['set']['max'],
                 emit = chart_dict['xlim']['emit'],
                 auto = chart_dict['xlim']['auto'])


    if chart_dict['ylim']['display']:

        if chart_dict['ylim']['mode'] == 'set':

            subplot.set_ylim \
                (bottom = chart_dict['ylim']['set']['min'], 
                 top = chart_dict['ylim']['set']['max'],
                 emit = chart_dict['ylim']['emit'],
                 auto = chart_dict['ylim']['auto'])


# In[178]:


#*******************************************************************************************
 #
 #  Function Name:  plot_limits
 #
 #  Function Description:
 #      The function sets the x-axis and y-axis limits.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  dictionary     chart_dict       The parameter is the chart dictionary.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def plot_limits(chart_dict):

    if chart_dict['xlim']['display']:

        if chart_dict['xlim']['mode'] == 'set':

            plt.xlim \
                (chart_dict['xlim']['set']['min'], 
                 chart_dict['xlim']['set']['max'])
        else:

            plt.xlim(left = chart_dict['xlim']['adjust']['left'])

            plt.xlim(right = chart_dict['xlim']['adjust']['right'])


    if chart_dict['ylim']['display']:

        if chart_dict['ylim']['mode'] == 'set':

            plt.ylim \
                (chart_dict['ylim']['set']['min'], 
                 chart_dict['ylim']['set']['max'])
        else:

            plt.ylim(left = chart_dict['ylim']['adjust']['left'])

            plt.ylim(right = chart_dict['ylim']['adjust']['right']) 


# In[179]:


#*******************************************************************************************
 #
 #  Function Name:  plot_ticks_stacked
 #
 #  Function Description:
 #      The function plots the x-axis and y-axis ticks and chart grid 
 #      for a stacked multichart.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  object         subplot          The parameter is the subplot object.
 #  dictionary     chart_dict       The parameter is the chart dictionary.
 #  integer        idx              The parameter is the plot index.
 #  integer        last_idx         The parameter is the last plot index.
 #  array          tick_lbls_array  The optional parameter is the tick labels.
 #  boolean        boxplot_bool     The optional parameter indicates whether the chart 
 #                                  is a boxplot.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def plot_ticks_stacked \
        (subplot,
         chart_dict,
         idx,
         last_idx,
         tick_lbls_array = np.array([], dtype = str),
         boxplot_bool = False):

    if not boxplot_bool:

        if chart_dict['xticks']['display']:

            if idx != last_idx:

                subplot.set_xticklabels(labels = [])

            subplot.tick_params \
                (axis = 'x', 
                 labelrotation = chart_dict['xticks']['rotation'], 
                 labelsize = chart_dict['xticks']['fontsize'])

    else:

        if chart_dict['xticks']['display']:

            ticks_idx_array = np.array([], dtype = int)

            for idx, lbl in enumerate(tick_lbls_array):

                ticks_idx_array = np.append(ticks_idx_array, idx + 1)


            subplot.set_xticks(ticks_idx_array, tick_lbls_array)

            subplot.tick_params \
                (axis = 'x', 
                 labelrotation = chart_dict['xticks']['rotation'], 
                 labelsize = chart_dict['xticks']['fontsize'])


    if chart_dict['yticks']['display']:

        subplot.tick_params \
            (axis = 'y', 
             labelrotation = chart_dict['yticks']['rotation'], 
             labelsize = chart_dict['yticks']['fontsize'])


    if chart_dict['grid']['display']:

        subplot.grid \
            (visible = chart_dict['grid']['visible'],
             which = chart_dict['grid']['which'],
             axis =  chart_dict['grid']['axis'])   


# In[180]:


#*******************************************************************************************
 #
 #  Function Name:  plot_ticks
 #
 #  Function Description:
 #      The function plots the x-axis and y-axis ticks and chart grid.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  dictionary     chart_dict       The parameter is the chart dictionary.
 #  array          tick_lbls_array  The optional parameter is the tick labels.
 #  boolean        boxplot_bool     The optional parameter indicates whether the chart 
 #                                  is a boxplot.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def plot_ticks \
        (chart_dict,
         tick_lbls_array = np.array([], dtype = str),
         boxplot_bool = False):

    if not boxplot_bool:

        if chart_dict['xticks']['display']:

            plt.xticks \
                (fontsize = chart_dict['xticks']['fontsize'], 
                 rotation = chart_dict['xticks']['rotation'])

    else:

        if chart_dict['xticks']['display']:

            ticks_idx_array = np.array([], dtype = int)

            for idx, lbl in enumerate(tick_lbls_array):

                ticks_idx_array = np.append(ticks_idx_array, idx + 1)


            plt.xticks \
                (ticks_idx_array, 
                 tick_lbls_array,
                 fontsize = chart_dict['xticks']['fontsize'], 
                 rotation = chart_dict['xticks']['rotation'])


    if chart_dict['yticks']['display']:

        plt.yticks \
            (fontsize = chart_dict['yticks']['fontsize'], 
             rotation = chart_dict['yticks']['rotation'])


    if chart_dict['grid']['display']:

        plt.grid \
            (visible = chart_dict['grid']['visible'],
             which = chart_dict['grid']['which'],
             axis =  chart_dict['grid']['axis'])   


# In[181]:


#*******************************************************************************************
 #
 #  Function Name:  plot_legend_stacked
 #
 #  Function Description:
 #      The function plots the chart's legend for a stacked multichart.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  array          plot_array       The parameter is the plot array.   
 #  array          names_array      The parameter is the names array.   
 #  object         axs              The parameter is the axes object.
 #  dictionary     chart_dict       The parameter is the chart dictionary.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def plot_legend_stacked \
        (plot_array, 
         names_array, 
         axs, 
         chart_dict):

    if chart_dict['legend']['display']:

        plt.legend \
            (plot_array, 
             names_array, 
             loc = chart_dict['legend']['loc'],
             fontsize = chart_dict['legend']['fontsize'],
             bbox_to_anchor = chart_dict['legend']['bbox_to_anchor'])


# In[182]:


#*******************************************************************************************
 #
 #  Function Name:  plot_legend
 #
 #  Function Description:
 #      The function plots the chart's legend.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  dictionary     chart_dict       The parameter is the chart dictionary.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def plot_legend(chart_dict):

    if chart_dict['legend']['display']:

        plt.legend \
            (loc = chart_dict['legend']['loc'],
             fontsize = chart_dict['legend']['fontsize'],
             bbox_to_anchor = chart_dict['legend']['bbox_to_anchor'])


# In[183]:


#*******************************************************************************************
 #
 #  Function Name:  plot_regr_line
 #
 #  Function Description:
 #      The function plots the chart's regression line.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  array          x_array          The parameter is the x-coordinates.
 #  array          y_array          The parameter is the y-coordinates.
 #  integer        idx              The parameter is the plot index.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def plot_regr_line \
        (x_array, 
         y_array,
         idx = 0):

    try:

        degree     = regr_line_dict['degree'][idx]

    except: degree = regr_line_dict['degree']


    if degree >= 1:

        if degree > 8: degree = 8

        try:

            x_coord = regr_line_dict['eqn_x_coord'][idx]

            y_coord = regr_line_dict['eqn_y_coord'][idx]

        except:

            x_coord = regr_line_dict['eqn_x_coord']

            y_coord = regr_line_dict['eqn_y_coord']


        regr_line(x_array, y_array, x_coord, y_coord, degree_int = degree)


# In[184]:


#*******************************************************************************************
 #
 #  Function Name:  plot_peaks
 #
 #  Function Description:
 #      The function plots the chart's labels for line peaks from a series.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  series         input_series     The parameter is the input series.
 #  dictionary     chart_dict       The parameter is the chart dictionary.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def plot_peaks(input_series, chart_dict):

    if chart_dict['peaks']['display']:

        x_array \
            = dtypesx.cnv_data_to_array \
                (list(input_series.index[chart_dict['peaks']['array']]))

        y_array \
            = dtypesx.cnv_data_to_array \
                (list(input_series.iloc[chart_dict['peaks']['array']]))


        plt.plot \
            (x_array, y_array, 'x', 
             markersize = chart_dict['peaks']['markersize'], 
             color = chart_dict['peaks']['color'][0]) 


        for i, j in zip(x_array, y_array):

            y_coord_flt = j + emp_obj.iloc[chart_dict['peaks']['y_offset']]

            plt.annotate \
                (i, xy = (i, y_coord_flt), 
                 size = chart_dict['peaks']['fontsize'], 
                 color = chart_dict['peaks']['color'][1])


# In[185]:


#*******************************************************************************************
 #
 #  Function Name:  plot_suptitle_axes
 #
 #  Function Description:
 #      The function plots the chart's suptitle, supx-axis label, and supy-axis label.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  object         figure           The parameter is the matplotlib figure object.
 #  dictionary     chart_dict       The parameter is the chart dictionary.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def plot_suptitle_axes(figure, chart_dict):

    if chart_dict['suptitle']['text'] is not None:

        figure.suptitle \
            (t = chart_dict['suptitle']['text'], 
             x = chart_dict['suptitle']['x'],
             y = chart_dict['suptitle']['y'],
             horizontalalignment = chart_dict['suptitle']['horizontalalignment'],
             verticalalignment = chart_dict['suptitle']['verticalalignment'],
             fontproperties = chart_dict['suptitle']['fontproperties'])

    if chart_dict['supxlabel']['text'] is not None:

        figure.supxlabel \
            (t = chart_dict['supxlabel']['text'], 
             x = chart_dict['supxlabel']['x'],
             y = chart_dict['supxlabel']['y'],
             horizontalalignment = chart_dict['supxlabel']['horizontalalignment'],
             verticalalignment = chart_dict['supxlabel']['verticalalignment'],
             fontproperties = chart_dict['supxlabel']['fontproperties'])

    if chart_dict['supylabel']['text'] is not None:

        figure.supylabel \
            (t = chart_dict['supylabel']['text'], 
             x = chart_dict['supylabel']['x'],
             y = chart_dict['supylabel']['y'],
             horizontalalignment = chart_dict['supylabel']['horizontalalignment'],
             verticalalignment = chart_dict['supylabel']['verticalalignment'],
             fontproperties = chart_dict['supylabel']['fontproperties'])


# In[186]:


#*******************************************************************************************
 #
 #  Function Name:  plot_tight_layout
 #
 #  Function Description:
 #      The function sets the tight layout parameters for a multichart.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  dictionary     chart_dict       The parameter is the chart dictionary.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def plot_tight_layout(chart_dict):

    if chart_dict['tight_layout']['display']:

        plt.tight_layout \
            (pad = chart_dict['tight_layout']['pad'],
             h_pad = chart_dict['tight_layout']['h_pad'],
             w_pad = chart_dict['tight_layout']['w_pad'],
             rect = chart_dict['tight_layout']['rect'])


# In[187]:


#*******************************************************************************************
 #
 #  Function Name:  plot_subplots_adjust
 #
 #  Function Description:
 #      The function plots width and height spaces for subplots.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  object         fig              The parameter is the matplotlib figure object.
 #  dictionary     chart_dict       The parameter is the chart dictionary.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def plot_subplots_adjust(fig, chart_dict):

    if chart_dict['figure']['wspace'] is not None \
        and chart_dict['figure']['hspace'] is not None:

        fig.subplots_adjust \
            (wspace = chart_dict['figure']['wspace'], 
             hspace = chart_dict['figure']['hspace'])


# In[188]:


#*******************************************************************************************
 #
 #  Function Name:  plot_bar_chart_series
 #
 #  Function Description:
 #      The function plots a bar chart from a series.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  series         input_series     The parameter is the input series.
 #  dictionary     chart_dict       The parameter is the chart dictionary.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def plot_bar_chart_series(input_series, chart_dict):

    if chart_dict['params']['horizontal']:

        _ = plt.barh \
                (input_series.keys(),
                 input_series,
                 height = chart_dict['horizontal']['height'],
                 left = chart_dict['horizontal']['left'],
                 align = chart_dict['params']['align'],
                 color = chart_dict['params']['color'],
                 edgecolor = chart_dict['params']['edgecolor'],
                 linewidth = chart_dict['params']['linewidth'],
                 tick_label = chart_dict['params']['tick_label'],
                 log = chart_dict['params']['log'],
                 alpha = chart_dict['params']['alpha'])

    else: 

        _ = plt.bar \
                (input_series.keys(),
                 input_series,
                 width = chart_dict['vertical']['width'],
                 bottom = chart_dict['vertical']['bottom'],
                 align = chart_dict['params']['align'],
                 color = chart_dict['params']['color'],
                 edgecolor = chart_dict['params']['edgecolor'],
                 linewidth = chart_dict['params']['linewidth'],
                 tick_label = chart_dict['params']['tick_label'],
                 log = chart_dict['params']['log'],
                 alpha = chart_dict['params']['alpha'])


# In[189]:


#*******************************************************************************************
 #
 #  Function Name:  plot_bar_chart_df
 #
 #  Function Description:
 #      The function plots a bar chart from a Dataframe.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  dataframe      input_df         The parameter is the input DataFrame.
 #  dictionary     chart_dict       The parameter is the chart dictionary.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def plot_bar_chart_df(input_df, chart_dict):

    if chart_dict['params']['horizontal']:

        _ = input_df \
                .plot.barh \
                    (height = chart_dict['horizontal']['height'],
                     left = chart_dict['horizontal']['left'],
                     stacked = chart_dict['params']['stacked'],
                     align = chart_dict['params']['align'],
                     color = chart_dict['params']['color'],
                     edgecolor = chart_dict['params']['edgecolor'],
                     linewidth = chart_dict['params']['linewidth'],
                     tick_label = chart_dict['params']['tick_label'],
                     log = chart_dict['params']['log'],
                     alpha = chart_dict['params']['alpha'])

    else:

        _ = input_df \
                .plot.bar \
                    (width = chart_dict['vertical']['width'],
                     bottom = chart_dict['vertical']['bottom'],
                     stacked = chart_dict['params']['stacked'],
                     align = chart_dict['params']['align'],
                     color = chart_dict['params']['color'],
                     edgecolor = chart_dict['params']['edgecolor'],
                     linewidth = chart_dict['params']['linewidth'],
                     tick_label = chart_dict['params']['tick_label'],
                     log = chart_dict['params']['log'],
                     alpha = chart_dict['params']['alpha'])



# In[190]:


#*******************************************************************************************
 #
 #  Function Name:  plot_bar_chart
 #
 #  Function Description:
 #      The function plots a bar chart only.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  object         input_obj        The parameter is the input object.
 #  dictionary     chart_dict       The parameter is the chart dictionary.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def plot_bar_chart(input_obj, chart_dict):

    if isinstance(input_obj, pd.Series): plot_bar_chart_series(input_obj, chart_dict)

    elif isinstance(input_obj, pd.DataFrame): plot_bar_chart_df(input_obj, chart_dict)


# In[191]:


#*******************************************************************************************
 #
 #  Function Name:  plot_boxplot_chart
 #
 #  Function Description:
 #      The function plots a boxplot chart only.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  list           data_list        The parameter is the series list.
 #  array          tick_lbls_array  The parameter is the tick labels array.
 #  dictionary     chart_dict       The parameter is the chart dictionary.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def plot_boxplot_chart(data_list, tick_lbls_array, chart_dict):

    _ = plt.boxplot \
        (x = data_list,
         notch = chart_dict['params']['notch'], 
         vert = chart_dict['params']['vert'], 
         orientation = chart_dict['params']['orientation'], 
         whis = chart_dict['params']['whis'], 
         widths = chart_dict['params']['widths'], 
         patch_artist = chart_dict['params']['patch_artist'], 
         autorange = chart_dict['params']['autorange'], 
         meanline = chart_dict['params']['meanline'],
         showmeans = chart_dict['params']['showmeans'])


# In[192]:


#*******************************************************************************************
 #
 #  Function Name:  plot_histogram_chart
 #
 #  Function Description:
 #      The function plots a histogram chart only.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  array          data_array       The parameter is the data array.
 #  dictionary     chart_dict       The parameter is the chart dictionary.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def plot_histogram_chart(data_array, chart_dict):

    _ = plt.hist \
            (data_array,
             bins = chart_dict['params']['bins'],
             range = chart_dict['params']['range'],
             density = chart_dict['params']['density'],
             weights = chart_dict['params']['weights'],
             cumulative = chart_dict['params']['cumulative'],
             bottom = chart_dict['params']['bottom'],
             histtype = chart_dict['params']['histtype'],
             align = chart_dict['params']['align'],
             orientation = chart_dict['params']['orientation'],
             rwidth = chart_dict['params']['rwidth'],
             log = chart_dict['params']['log'],
             color = chart_dict['params']['color'],
             label = chart_dict['params']['label'],
             stacked = chart_dict['params']['stacked'],
             edgecolor = chart_dict['params']['edgecolor'],
             facecolor = chart_dict['params']['color'],
             linewidth = chart_dict['params']['linewidth'],
             alpha = chart_dict['params']['alpha'])


# In[193]:


#*******************************************************************************************
 #
 #  Function Name:  plot_line_chart
 #
 #  Function Description:
 #      The function plots a line chart only from a series or dataframe.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  object         input_obj        The parameter is the input object.
 #  dictionary     chart_dict       The parameter is the chart dictionary.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def plot_line_chart(input_obj, chart_dict):

    _ = input_obj \
        .plot \
        .line \
            (color = chart_dict['line']['color'],
             linestyle = chart_dict['line']['linestyle'],
             fillstyle = chart_dict['line']['fillstyle'],
             linewidth = chart_dict['line']['linewidth'],
             alpha = chart_dict['line']['alpha'],
             marker = chart_dict['marker']['shape'],
             markerfacecolor = chart_dict['marker']['color'],
             markeredgecolor = chart_dict['marker']['edgecolor'],
             markersize = chart_dict['marker']['size'],
             markeredgewidth = chart_dict['marker']['edgewidth'],
             logx = chart_dict['params']['logx'],
             logy = chart_dict['params']['logy'],
             loglog = chart_dict['params']['loglog'],
             stacked = chart_dict['params']['stacked'],
             use_index = chart_dict['params']['use_index'])


# In[194]:


#*******************************************************************************************
 #
 #  Function Name:  plot_pie_chart
 #
 #  Function Description:
 #      The function plots a histogram chart only.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  array          data_array       The parameter is the data array.
 #  array          labels_array     The parameter is the labels array.
 #  dictionary     chart_dict       The parameter is the chart dictionary.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def plot_pie_chart(data_array, labels_array, chart_dict):

    _ = plt.pie \
            (data_array,
             labels = labels_array, 
             explode = chart_dict['params']['explode'] * len(data_array), 
             colors = chart_dict['params']['colors'],
             hatch = chart_dict['params']['hatch'],
             autopct = chart_dict['params']['autopct'],
             pctdistance = chart_dict['params']['pctdistance'],
             labeldistance = chart_dict['params']['labeldistance'],
             shadow = chart_dict['params']['shadow'],
             startangle = chart_dict['params']['startangle'],
             radius = chart_dict['params']['radius'],
             counterclock = chart_dict['params']['counterclock'],
             wedgeprops = chart_dict['params']['wedgeprops'],
             textprops = chart_dict['params']['textprops'],
             center = chart_dict['params']['center'],
             frame = chart_dict['params']['frame'],
             rotatelabels = chart_dict['params']['rotatelabels'],
             normalize = chart_dict['params']['normalize'])


# In[195]:


#*******************************************************************************************
 #
 #  Function Name:  plot_plot_chart
 #
 #  Function Description:
 #      The function plots a chart only.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  series         data_series      The parameter is the data series.
 #  dictionary     chart_dict       The parameter is the chart dictionary.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def plot_plot_chart(data_series, chart_dict):

    _ = data_series \
            .plot \
                (scalex = chart_dict['params']['scalex'],
                 scaley = chart_dict['params']['scaley'],
                 color = chart_dict['params']['color'],
                 alpha = chart_dict['params']['alpha'])


# In[196]:


#*******************************************************************************************
 #
 #  Function Name:  plot_scatterplot_chart
 #
 #  Function Description:
 #      The function plots a scatterplot chart only.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  array          x_array          The parameter is the x-axis array.
 #  array          y_array          The parameter is the y-axis array.
 #  dictionary     chart_dict       The parameter is the chart dictionary.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def plot_scatterplot_chart(x_array, y_array, chart_dict):

    _ = plt.scatter \
            (x_array, 
             y_array, 
             marker = chart_dict['marker']['shape'],
             c = chart_dict['marker']['color'],
             s = chart_dict['marker']['size'],
             alpha = chart_dict['marker']['alpha'],
             linewidth = chart_dict['marker']['linewidth'],
             edgecolors = chart_dict['marker']['edgecolors'])


# In[197]:


#*******************************************************************************************
 #
 #  Function Name:  plot_line_multichart_stacked
 #
 #  Function Description:
 #      The function plots a stacked line multichart.
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
 #  string         suptitle         The parameter is the multichart suptitle.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def plot_line_multichart_stacked(input_df, suptitle):

    global line_multichart_dict


    line_multichart_dict['suptitle']['text'] \
        = suptitle

    line_multichart_dict['figure']['nplots'] \
        = dtypesx.rtn_data_obj_size(input_df)

    last_idx \
        = line_multichart_dict['figure']['nplots'] - 1


    fig, axs = plot_subplots(line_multichart_dict)

    plot_suptitle_axes(fig, line_multichart_dict)


    legend_plot_array = np.array([], dtype = object)

    legend_names_array = np.array([], dtype = str)


    if line_chart_dict['ylabel']['text'][0] is None: ylabel_bool = True

    else: ylabel_bool = False


    for idx, subplot in enumerate(axs):

        curr_series = input_df.iloc[:, idx]

        line_subplot, \
            = subplot.plot \
                (curr_series.dropna(), 
                 color = line_chart_dict['line']['color'][idx])


        legend_plot_array = np.append(legend_plot_array, line_subplot)

        legend_names_array = np.append(legend_names_array, curr_series.name)


        if ylabel_bool:

            line_chart_dict['ylabel']['text'] = legend_names_array


        plot_title_axes_stacked(subplot, line_chart_dict, idx, last_idx)

        plot_limits_stacked(subplot, line_chart_dict)

        plot_ticks_stacked(subplot, line_chart_dict, idx, last_idx)


    plot_legend_stacked \
        (legend_plot_array, 
         legend_names_array, 
         axs, 
         line_chart_dict)


    plot_subplots_adjust(fig, line_multichart_dict)


    line_chart_dict['ylabel']['text'] = [None]


    logx.save_matplotlib_image(line_multichart_dict['suptitle']['text'])

    plt.show();


# In[198]:


#*******************************************************************************************
 #
 #  Function Name:  plot_line_multichart
 #
 #  Function Description:
 #      The function plots a line multichart.
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
 #  string         suptitle         The parameter is the multichart suptitle.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def plot_line_multichart(input_df, suptitle):

    global line_multichart_dict


    line_multichart_dict['suptitle']['text'] \
        = suptitle

    line_multichart_dict['figure']['nplots'] \
        = dtypesx.rtn_data_obj_size(input_df)


    nrows, ncols = calc_rows_and_cols(line_multichart_dict)


    line_multichart_dict['figure']['nrows'] = nrows

    line_multichart_dict['figure']['ncols'] = ncols


    fig, axs = plot_subplots(line_multichart_dict)

    plot_suptitle_axes(fig, line_multichart_dict)


    for idx in range(line_multichart_dict['figure']['nplots']):

        plot_subplot(line_multichart_dict, idx)


        series = input_df.iloc[: ,idx]

        plot_line_chart(series.dropna(), line_chart_dict)


        plot_title_axes(line_chart_dict, idx)

        plot_limits(line_chart_dict)

        plot_ticks(line_chart_dict)


        plot_tight_layout(line_multichart_dict)


    plot_subplots_adjust(fig, line_multichart_dict)


    logx.save_matplotlib_image(suptitle)

    plt.show();


# In[199]:


#*******************************************************************************************
 #
 #  Function Name:  plot_pie_multichart
 #
 #  Function Description:
 #      The function plots a pie multichart.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  object         input_obj        The parameter is the input object.
 #  string         suptitle         The parameter is the multichart suptitle.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def plot_pie_multichart(input_obj, suptitle):

    global pie_multichart_dict

    global pie_chart_dict


    data_df = proc_chart_input(input_obj, chart_enum.MULTIPIE.value) 


    pie_multichart_dict['suptitle']['text'] = suptitle

    pie_multichart_dict['figure']['nplots'] = dtypesx.rtn_data_obj_size(data_df)


    nrows, ncols = calc_rows_and_cols(pie_multichart_dict)


    pie_multichart_dict['figure']['nrows'] = nrows

    pie_multichart_dict['figure']['ncols'] = ncols


    fig, axs = plot_subplots(pie_multichart_dict)

    plot_suptitle_axes(fig, pie_multichart_dict)


    for idx in range(pie_multichart_dict['figure']['nplots']):

        plot_subplot(pie_multichart_dict, idx)


        series = data_df.iloc[:, idx]

        data_array = series.to_numpy()


        pie_chart_dict['title']['text'] = series.name.title(),

        labels_array = series.index.to_numpy()


        plot_pie_chart(data_array, labels_array, pie_chart_dict)


        plot_title_axes(pie_chart_dict)

        plot_legend(pie_chart_dict)


        plot_tight_layout(pie_multichart_dict)


    plot_subplots_adjust(fig, pie_multichart_dict)


    logx.save_matplotlib_image(suptitle)

    plt.show();


# In[200]:


#*******************************************************************************************
 #
 #  Function Name:  plot_scatterplot_multichart
 #
 #  Function Description:
 #      The function plots a scatterplot multichart.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  object         input_obj        The parameter is the input object.
 #  string         suptitle         The parameter is the multichart suptitle.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def plot_scatterplot_multichart(input_obj, suptitle):

    global scatterplot_multichart_dict


    scatterplot_multichart_dict['suptitle']['text'] \
        = suptitle

    scatterplot_multichart_dict['figure']['nplots'] \
        = dtypesx.rtn_data_obj_size(input_obj)


    nrows, ncols = calc_rows_and_cols(scatterplot_multichart_dict)


    scatterplot_multichart_dict['figure']['nrows'] = nrows

    scatterplot_multichart_dict['figure']['ncols'] = ncols


    fig, axs = plot_subplots(scatterplot_multichart_dict)

    plot_suptitle_axes(fig, scatterplot_multichart_dict)


    x_list, y_list \
        = proc_chart_input(input_obj, chart_enum.MULTISCATTER.value) 

    for idx in range(scatterplot_multichart_dict['figure']['nplots']):

        plot_subplot(scatterplot_multichart_dict, idx)


        x_array = dtypesx.cnv_data_to_array(x_list[idx])

        y_array = dtypesx.cnv_data_to_array(y_list[idx])


        plot_scatterplot_chart \
            (x_array, y_array, 
             scatterplot_chart_dict)


        plot_title_axes(scatterplot_chart_dict, idx)

        plot_limits(scatterplot_chart_dict)

        plot_ticks(scatterplot_chart_dict)


        plot_regr_line(x_array, y_array, idx)


        plot_tight_layout(scatterplot_multichart_dict)


    logx.save_matplotlib_image(suptitle)

    plt.show();


# In[201]:


#*******************************************************************************************
 #
 #  Function Name:  plot_rolling_corr_lines
 #
 #  Function Description:
 #      The function plots a rolling correlation along with the x-y series.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  series         x_series         The parameter is the x-values series.
 #  series         y_series         The parameter is the y-values series.
 #  string         title            The parameter is the plot title.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def plot_rolling_corr_lines(x_series, y_series, title):

    x_array = dtypesx.cnv_data_to_array(x_series)

    x_idx_array = dtypesx.cnv_data_to_array(x_series.index)


    y_array = dtypesx.cnv_data_to_array(y_series)

    y_idx_array = dtypesx.cnv_data_to_array(y_series.index)


    set_roll_corr_title(title)


    _, axes = plot_subplots(roll_corr_dict)


    rolling_corr_series \
        = mathx.roll_corr_time_series \
            (x_series,
             y_series, 
             roll_corr_dict['params']['window'], 
             roll_corr_dict['params']['min_periods'])


    axes[0].plot \
        (x_idx_array, 
         x_array, 
         color = roll_corr_dict['line']['color'][0], 
         linestyle = roll_corr_dict['line']['linestyle'],
         fillstyle = roll_corr_dict['line']['fillstyle'],
         linewidth = roll_corr_dict['line']['linewidth'],
         alpha = roll_corr_dict['line']['alpha'],
         marker = roll_corr_dict['marker']['shape'],
         markerfacecolor = roll_corr_dict['marker']['color'],
         markeredgecolor = roll_corr_dict['marker']['edgecolor'],
         markersize = roll_corr_dict['marker']['size'],
         markeredgewidth = roll_corr_dict['marker']['edgewidth'])


    axes[0].set_title \
        (roll_corr_dict['title']['text'][0], 
         fontdict = {'fontsize': roll_corr_dict['title']['fontsize'], 
                     'fontstyle': roll_corr_dict['title']['fontstyle'],
                     'fontweight': roll_corr_dict['title']['fontweight']},
         loc = roll_corr_dict['title']['loc'],
         pad = roll_corr_dict['title']['pad'])

    axes[0].set_ylabel \
        (x_series.name.lower(),
         fontdict = {'fontsize': roll_corr_dict['ylabel']['fontsize'],
                     'fontstyle': roll_corr_dict['ylabel']['fontstyle'],
                     'fontweight': roll_corr_dict['title']['fontweight']},
         loc = roll_corr_dict['ylabel']['loc'],
         labelpad = roll_corr_dict['ylabel']['pad'])

    axes[0].grid \
        (visible = roll_corr_dict['grid']['visible'],
         which = roll_corr_dict['grid']['which'],
         axis =  roll_corr_dict['grid']['axis'])   


    axes[1].plot \
        (y_idx_array, 
         y_array,
         color = roll_corr_dict['line']['color'][1], 
         linestyle = roll_corr_dict['line']['linestyle'],
         fillstyle = roll_corr_dict['line']['fillstyle'],
         linewidth = roll_corr_dict['line']['linewidth'],
         alpha = roll_corr_dict['line']['alpha'],
         marker = roll_corr_dict['marker']['shape'],
         markerfacecolor = roll_corr_dict['marker']['color'],
         markeredgecolor = roll_corr_dict['marker']['edgecolor'],
         markersize = roll_corr_dict['marker']['size'],
         markeredgewidth = roll_corr_dict['marker']['edgewidth'])


    axes[1].set_ylabel \
        (y_series.name.lower(),
         fontdict = {'fontsize': roll_corr_dict['ylabel']['fontsize'],
                     'fontstyle': roll_corr_dict['ylabel']['fontstyle'],
                     'fontweight': roll_corr_dict['title']['fontweight']},
         loc = roll_corr_dict['ylabel']['loc'],
         labelpad = roll_corr_dict['ylabel']['pad'])

    axes[1].grid \
        (visible = roll_corr_dict['grid']['visible'],
         which = roll_corr_dict['grid']['which'],
         axis =  roll_corr_dict['grid']['axis'])   


    axes[2].plot \
        (rolling_corr_series.index, 
         rolling_corr_series,
         color = roll_corr_dict['line']['color'][2],
         linestyle = roll_corr_dict['line']['linestyle'],
         fillstyle = roll_corr_dict['line']['fillstyle'],
         linewidth = roll_corr_dict['line']['linewidth'],
         alpha = roll_corr_dict['line']['alpha'],
         marker = roll_corr_dict['marker']['shape'],
         markerfacecolor = roll_corr_dict['marker']['color'],
         markeredgecolor = roll_corr_dict['marker']['edgecolor'],
         markersize = roll_corr_dict['marker']['size'],
         markeredgewidth = roll_corr_dict['marker']['edgewidth'])


    axes[2].set_xlabel \
        (roll_corr_dict['xlabel']['text'][0],
         fontdict = {'fontsize': roll_corr_dict['xlabel']['fontsize'],
                     'fontstyle': roll_corr_dict['xlabel']['fontstyle'],
                     'fontweight': roll_corr_dict['title']['fontweight']},
         loc = roll_corr_dict['xlabel']['loc'],
         labelpad = roll_corr_dict['xlabel']['pad'])

    axes[2].set_ylabel \
        ('rolling_r_value',
         fontdict = {'fontsize': roll_corr_dict['ylabel']['fontsize'],
                     'fontstyle': roll_corr_dict['ylabel']['fontstyle'],
                     'fontweight': roll_corr_dict['title']['fontweight']},
         loc = roll_corr_dict['ylabel']['loc'],
         labelpad = roll_corr_dict['ylabel']['pad'])

    axes[2].grid \
        (visible = roll_corr_dict['grid']['visible'],
         which = roll_corr_dict['grid']['which'],
         axis =  roll_corr_dict['grid']['axis'])

    axes[2].set_ylim(-1.0, 1.0)


    axes[2].axhline \
        (y = roll_corr_dict['axh_out']['y'], 
         color = roll_corr_dict['axh_out']['color'], 
         linestyle = roll_corr_dict['axh_out']['linestyle'], 
         fillstyle = roll_corr_dict['axh_out']['fillstyle'], 
         linewidth = roll_corr_dict['axh_out']['linewidth'],
         alpha = roll_corr_dict['axh_out']['alpha'], 
         label = f"r = ±{roll_corr_dict['axh_out']['y']}")

    axes[2].axhline \
        (y = 0.0, 
         color = roll_corr_dict['axh_ctr']['color'], 
         linestyle = roll_corr_dict['axh_ctr']['linestyle'], 
         fillstyle = roll_corr_dict['axh_ctr']['fillstyle'], 
         linewidth = roll_corr_dict['axh_ctr']['linewidth'],
         alpha = roll_corr_dict['axh_ctr']['alpha'])

    axes[2].axhline \
        (y = operator.neg(roll_corr_dict['axh_out']['y']), 
         color = roll_corr_dict['axh_out']['color'], 
         linestyle = roll_corr_dict['axh_out']['linestyle'], 
         fillstyle = roll_corr_dict['axh_out']['fillstyle'], 
         linewidth = roll_corr_dict['axh_out']['linewidth'],
         alpha = roll_corr_dict['axh_out']['alpha'])


    axes[2].fill_between \
        (rolling_corr_series.index, 
         rolling_corr_series, 0,
         where = (rolling_corr_series > 0), 
         color = roll_corr_dict['axfill_upr']['color'],
         alpha = roll_corr_dict['axfill_upr']['alpha'])

    axes[2].fill_between \
        (rolling_corr_series.index, 
         rolling_corr_series, 0,
         where = (rolling_corr_series < 0), 
         color = roll_corr_dict['axfill_lwr']['color'],
         alpha = roll_corr_dict['axfill_lwr']['alpha'])


    axes[2].legend \
        (fontsize = roll_corr_dict['legend']['fontsize'],
         loc = roll_corr_dict['legend']['loc'],
         bbox_to_anchor = roll_corr_dict['legend']['bbox_to_anchor'])

    plt.tight_layout()


    logx.save_matplotlib_image(roll_corr_dict['title']['text'][0])

    plt.show();


# In[202]:


#*******************************************************************************************
 #
 #  Function Name:  plot_all_rolling_corrs_lines
 #
 #  Function Description:
 #      The function plots a rolling correlation along with the x-y series for the input
 #      series and the series in the comparison dictionary.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  series         input_series     The parameter is the input series.
 #  dictionary     comp_dict        The parameter is the comparison series dictionary.
 #  string         title            The parameter is the plot title.
 #  dataframe/none roll_corr_df     The parameter is a rolling correlation dataframe
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def plot_all_rolling_corrs_lines \
        (input_series, 
         comp_dict, 
         title, 
         roll_corr_df = None):

    _, ax \
        = plt.subplots \
            (figsize \
                 = (roll_corr_all_dict['figure']['width'], 
                    roll_corr_all_dict['figure']['length']))


    ax.axhline \
        (y = roll_corr_all_dict['axh_out']['y'], 
         color = roll_corr_all_dict['axh_out']['color'], 
         linestyle = roll_corr_all_dict['axh_out']['linestyle'], 
         fillstyle = roll_corr_all_dict['axh_out']['fillstyle'], 
         linewidth = roll_corr_all_dict['axh_out']['linewidth'],
         alpha = roll_corr_all_dict['axh_out']['alpha'])

    ax.axhline \
        (y = 0.0, 
         color = roll_corr_all_dict['axh_ctr']['color'], 
         linestyle = roll_corr_all_dict['axh_ctr']['linestyle'], 
         fillstyle = roll_corr_all_dict['axh_ctr']['fillstyle'], 
         linewidth = roll_corr_all_dict['axh_ctr']['linewidth'],
         alpha = roll_corr_all_dict['axh_ctr']['alpha'])

    ax.axhline \
        (y = operator.neg(roll_corr_all_dict['axh_out']['y']), 
         color = roll_corr_all_dict['axh_out']['color'], 
         linestyle = roll_corr_all_dict['axh_out']['linestyle'], 
         fillstyle = roll_corr_all_dict['axh_out']['fillstyle'], 
         linewidth = roll_corr_all_dict['axh_out']['linewidth'],
         alpha = roll_corr_all_dict['axh_out']['alpha'])


    set_roll_corr_all_title(title)


    idx_int = 0

    for label, series in comp_dict.items():

        if roll_corr_df is None:

            wndw_int    = roll_corr_all_dict['params']['window']

            min_prd_int = roll_corr_all_dict['params']['min_periods']

        else:

            wndw_int    = roll_corr_df.loc[series.name, 'window']

            min_prd_int = roll_corr_df.loc[series.name, 'min_period']


        rolling_corr_series \
            = mathx.roll_corr_time_series \
                (input_series, series, wndw_int, min_prd_int)

        try: 

            color = roll_corr_all_dict['line']['color'][idx_int]

            ax.plot \
                (rolling_corr_series.index, 
                 rolling_corr_series,
                 color = color,
                 linestyle = roll_corr_all_dict['line']['linestyle'],
                 fillstyle = roll_corr_all_dict['line']['fillstyle'],
                 linewidth = roll_corr_all_dict['line']['linewidth'],
                 alpha = roll_corr_all_dict['line']['alpha'],
                 marker = roll_corr_all_dict['marker']['shape'],
                 markerfacecolor = roll_corr_all_dict['marker']['color'],
                 markeredgecolor = roll_corr_all_dict['marker']['edgecolor'],
                 markersize = roll_corr_all_dict['marker']['size'],
                 markeredgewidth = roll_corr_all_dict['marker']['edgewidth'],
                 label = label)

        except:

            ax.plot \
                (rolling_corr_series.index, 
                 rolling_corr_series,
                 linestyle = roll_corr_all_dict['line']['linestyle'],
                 fillstyle = roll_corr_all_dict['line']['fillstyle'],
                 linewidth = roll_corr_all_dict['line']['linewidth'],
                 alpha = roll_corr_all_dict['line']['alpha'],
                 marker = roll_corr_all_dict['marker']['shape'],
                 markerfacecolor = roll_corr_all_dict['marker']['color'],
                 markeredgecolor = roll_corr_all_dict['marker']['edgecolor'],
                 markersize = roll_corr_all_dict['marker']['size'],
                 markeredgewidth = roll_corr_all_dict['marker']['edgewidth'],
                 label = label)

        idx_int += 1


    plot_title_axes(roll_corr_all_dict)

    plot_limits(roll_corr_all_dict)

    plot_ticks(roll_corr_all_dict)

    plot_legend(roll_corr_all_dict)


    plt.tight_layout()


    logx.save_matplotlib_image(title)

    plt.show();


# In[203]:


#*******************************************************************************************
 #
 #  Function Name:  plot_corr_cv_errors
 #
 #  Function Description:
 #      The function plots a cv errors for determining the best polynomial degree.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  dictionary     cv_errors_dict   The parameter is the cv errors dictionary.
 #  string         title            The parameter is the plot title.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def plot_corr_cv_errors(cv_errors_dict, title):

    set_corr_cv_title(title)


    degrees_list = list(cv_errors_dict.keys())

    errors_list = list(cv_errors_dict.values())


    best = min(cv_errors_dict, key = cv_errors_dict.get)


    plot_figsize(corr_cv_dict)

    plt.plot \
        (degrees_list, 
         errors_list,
         color = corr_cv_dict['line']['color'],
         linewidth = corr_cv_dict['line']['linewidth'],
         linestyle = corr_cv_dict['line']['linestyle'],
         fillstyle = corr_cv_dict['line']['fillstyle'],
         alpha = corr_cv_dict['line']['alpha'],
         marker = corr_cv_dict['marker']['shape'],
         markerfacecolor = corr_cv_dict['marker']['color'],
         markeredgecolor = corr_cv_dict['marker']['edgecolor'],
         markersize = corr_cv_dict['marker']['size'],
         markeredgewidth = corr_cv_dict['marker']['edgewidth'])

    plt.axvline \
        (x = best, 
         color = corr_cv_dict['axv']['color'], 
         linestyle = corr_cv_dict['axv']['linestyle'],
         fillstyle = corr_cv_dict['axv']['fillstyle'],
         linewidth = corr_cv_dict['axv']['linewidth'],
         alpha = corr_cv_dict['axv']['alpha'],
         label = f'best degree = {best}')


    plot_title_axes(corr_cv_dict)

    plot_limits(corr_cv_dict)

    plot_ticks(corr_cv_dict)

    plot_legend(corr_cv_dict)


    plt.tight_layout()


    logx.save_matplotlib_image(title)

    plt.show();


# In[204]:


#*******************************************************************************************
 #
 #  Function Name:  plot_corr_scores
 #
 #  Function Description:
 #      The function plots a scores for determining the best polynomial degree.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  dictionary     scores_dict      The parameter is the cv errors dictionary.
 #  string         title            The parameter is the plot title.
 #  integer/none   best_val
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def plot_corr_scores(scores_dict, title, best_val = None):

    set_corr_scores_title(title)


    degrees_list = list(scores_dict.keys())

    errors_list = list(scores_dict.values())


    plot_figsize(corr_scores_dict)


    if best_val is None:

        best = max(scores_dict, key = scores_dict.get)

        markerfacecolor = corr_scores_dict['marker']['color']

        plt.plot \
            (degrees_list, 
             errors_list,
             color = corr_scores_dict['line']['color'],
             linewidth = corr_scores_dict['line']['linewidth'],
             linestyle = corr_scores_dict['line']['linestyle'],
             fillstyle = corr_scores_dict['line']['fillstyle'],
             alpha = corr_scores_dict['line']['alpha'],
             marker = corr_scores_dict['marker']['shape'],
             markerfacecolor = markerfacecolor,
             markeredgecolor = corr_scores_dict['marker']['edgecolor'],
             markersize = corr_scores_dict['marker']['size'],
             markeredgewidth = corr_scores_dict['marker']['edgewidth'])

    else:

        best = best_val

        #markerfacecolor \
        #    = np.where(np.array(degrees_list) == best_val, 'lime', 'red').tolist()

        markerfacecolor \
            = np.where \
                (np.array(degrees_list) == best_val, 'lime',
                 np.where \
                     (np.array(degrees_list) < best_val, 'yellow', 'red')) \
                        .tolist()

        plt.plot \
            (degrees_list,
             errors_list,
             color     = corr_scores_dict['line']['color'],
             linewidth = corr_scores_dict['line']['linewidth'],
             linestyle = corr_scores_dict['line']['linestyle'],
             alpha     = corr_scores_dict['line']['alpha'],
             zorder    = 1)

        plt.scatter \
            (degrees_list,
             errors_list,
             c                = markerfacecolor,
             marker           = corr_scores_dict['marker']['shape'],
             edgecolors       = corr_scores_dict['marker']['edgecolor'],
             s                = corr_scores_dict['marker']['size'] ** 2,
             linewidths       = corr_scores_dict['marker']['edgewidth'],
             alpha            = corr_scores_dict['line']['alpha'],
             zorder           = 2)


    plt.axvline \
        (x         = best, 
         color     = corr_scores_dict['axv']['color'], 
         linestyle = corr_scores_dict['axv']['linestyle'],
         fillstyle = corr_scores_dict['axv']['fillstyle'],
         linewidth = corr_scores_dict['axv']['linewidth'],
         alpha     = corr_scores_dict['axv']['alpha'],
         label     = f"best {corr_scores_dict['xlabel']['text'][0]} = {best}",
         zorder    = 3)


    plot_title_axes(corr_scores_dict)

    plot_limits(corr_scores_dict)

    plot_ticks(corr_scores_dict)

    plot_legend(corr_scores_dict)


    plt.tight_layout()


    logx.save_matplotlib_image(title)

    plt.show();


# In[205]:


#*******************************************************************************************
 #
 #  Function Name:  plot_window_cv_errors
 #
 #  Function Description:
 #      The function plots rolling window cv errors for determining the best number 
 #      of windows.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  dataframe      results_df       The parameter is the cv errors results dataframe.
 #  string         title            The parameter is the plot title.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def plot_window_cv_errors(results_df, title):

    best_window_int = results_df['mean_cv_mse'].idxmin()


    idx_array = np.array(results_df.index)

    errors_array = np.array(results_df['mean_cv_mse'])


    set_window_cv_title(title)

    _, ax \
        = plt.subplots \
            (figsize \
                 = (window_cv_dict['figure']['width'], 
                    window_cv_dict['figure']['length']))

    ax.plot \
        (idx_array, 
         errors_array, 
         color = window_cv_dict['line']['color'],
         linewidth = window_cv_dict['line']['linewidth'],
         linestyle = window_cv_dict['line']['linestyle'],
         fillstyle = window_cv_dict['line']['fillstyle'],
         alpha = window_cv_dict['line']['alpha'],
         marker = window_cv_dict['marker']['shape'],
         markerfacecolor = window_cv_dict['marker']['color'],
         markeredgecolor = window_cv_dict['marker']['edgecolor'],
         markersize = window_cv_dict['marker']['size'],
         markeredgewidth = window_cv_dict['marker']['edgewidth'], 
         label = window_cv_dict['ylabel']['text'])


    # Shaded band: mean ± std
    ax.fill_between \
        (idx_array,
         results_df['mean_cv_mse'] - results_df['std_cv_mse'],
         results_df['mean_cv_mse'] + results_df['std_cv_mse'],
         color = window_cv_dict['axfill']['color'],
         alpha = window_cv_dict['axfill']['alpha'], 
         label = '±1 std')

    ax.axvline \
        (x = best_window_int, 
         color = window_cv_dict['axv']['color'], 
         linestyle = window_cv_dict['axv']['linestyle'],
         fillstyle = window_cv_dict['axv']['fillstyle'],
         linewidth = window_cv_dict['axv']['linewidth'],
         alpha = window_cv_dict['axv']['alpha'],
         label = f'best window = {best_window_int}')


    plot_title_axes(window_cv_dict)

    plot_limits(window_cv_dict)

    plot_ticks(window_cv_dict)

    plot_legend(window_cv_dict)


    plt.tight_layout()


    logx.save_matplotlib_image(title)

    plt.show();


# In[206]:


#*******************************************************************************************
 #
 #  Function Name:  plot_lag_corr_line_chart
 #
 #  Function Description:
 #      The function plots the lagging correlation between two series as a line chart.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  series         x_series         The parameter is the x-values series.
 #  series         y_series         The parameter is the y-values series.
 #  string         title            The parameter is the plot title.
 #  int/none       max_lag          The parameter is the maximum lag.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def plot_lag_corr_line_chart(x_series, y_series, title, max_lag = None):

    if max_lag is None: max_lag_int = lag_corr_dict['params']['max_lag']

    else: max_lag_int = max_lag


    corr_method  = mathx.find_opt_corr_method(x_series, y_series)


    lag_corrs_series \
        = mathx.lag_corr_time_series \
            (x_series, y_series, max_lag_int, corr_method)


    corrs_idx_array = np.array(lag_corrs_series.index)

    corrs_array = np.array(lag_corrs_series)


    peak_lag_idx = lag_corrs_series.abs().idxmax()

    peak_r = lag_corrs_series[peak_lag_idx]


    _, ax \
        = plt.subplots \
            (figsize \
                = (lag_corr_dict['figure']['width'], 
                   lag_corr_dict['figure']['length']))


    set_lag_corr_title(title)


    xlabel \
        = f"lag (days)\n← {lag_corr_dict['ylabel']['text'][0]} leads {lag_corr_dict['xlabel']['text'][0]}     " \
            + f"{lag_corr_dict['xlabel']['text'][0]} leads {lag_corr_dict['ylabel']['text'][0]} →"

    set_lag_corr_xylabels(xlabel, 'r-value')


    ax.plot \
        (corrs_idx_array, corrs_array,
         color = lag_corr_dict['line']['color'],
         linestyle = lag_corr_dict['line']['linestyle'],
         fillstyle = lag_corr_dict['line']['fillstyle'],
         linewidth = lag_corr_dict['line']['linewidth'],
         alpha = lag_corr_dict['line']['alpha'],
         marker = lag_corr_dict['marker']['shape'],
         markerfacecolor = lag_corr_dict['marker']['color'],
         markeredgecolor = lag_corr_dict['marker']['edgecolor'],
         markersize = lag_corr_dict['marker']['size'],
         markeredgewidth = lag_corr_dict['marker']['edgewidth'])

    ax.fill_between \
        (corrs_idx_array, corrs_array, 0,
         where = (corrs_array > 0), 
         color = lag_corr_dict['axfill_upr']['color'],
         alpha = lag_corr_dict['axfill_upr']['alpha'])

    ax.fill_between \
        (corrs_idx_array, corrs_array, 0,
         where = (corrs_array < 0), 
         color = lag_corr_dict['axfill_lwr']['color'],
         alpha = lag_corr_dict['axfill_lwr']['alpha'])

    ax.axhline \
        (y = lag_corr_dict['axh_out']['y'], 
         color = lag_corr_dict['axh_out']['color'], 
         linestyle = lag_corr_dict['axh_out']['linestyle'], 
         fillstyle = lag_corr_dict['axh_out']['fillstyle'], 
         linewidth = lag_corr_dict['axh_out']['linewidth'],
         alpha = lag_corr_dict['axh_out']['alpha'], 
         label = f"r = ±{lag_corr_dict['axh_out']['y']}")

    ax.axhline \
        (y = 0.0, 
         color = lag_corr_dict['axh_ctr']['color'], 
         linestyle = lag_corr_dict['axh_ctr']['linestyle'], 
         fillstyle = lag_corr_dict['axh_ctr']['fillstyle'], 
         linewidth = lag_corr_dict['axh_ctr']['linewidth'],
         alpha = lag_corr_dict['axh_ctr']['alpha'])

    ax.axhline \
        (y = operator.neg(roll_corr_dict['axh_out']['y']), 
         color = lag_corr_dict['axh_out']['color'], 
         linestyle = lag_corr_dict['axh_out']['linestyle'], 
         fillstyle = lag_corr_dict['axh_out']['fillstyle'], 
         linewidth = lag_corr_dict['axh_out']['linewidth'],
         alpha = lag_corr_dict['axh_out']['alpha'])

    ax.axvline \
        (x = 0.0, 
         color = lag_corr_dict['axv']['color'], 
         linestyle = lag_corr_dict['axv']['linestyle'],
         fillstyle = lag_corr_dict['axv']['fillstyle'],
         linewidth = lag_corr_dict['axv']['linewidth'],
         alpha = lag_corr_dict['axv']['alpha'],
         label = 'no lag')

    ax.annotate \
        (f'Peak: lag = {peak_lag_idx}, r = {peak_r:.3f}',
         xy = (peak_lag_idx, peak_r),
         xytext \
             = (peak_lag_idx + lag_corr_dict['annotation']['xoffset'], 
                peak_r + lag_corr_dict['annotation']['yoffset']),
         arrowprops \
            = dict \
                (arrowstyle = lag_corr_dict['annotation']['arrw_stl'], 
                 color = lag_corr_dict['annotation']['arrw_clr']),
         fontsize = lag_corr_dict['annotation']['fontsize'])


    plot_title_axes(lag_corr_dict)

    plot_limits(lag_corr_dict)

    plot_ticks(lag_corr_dict)

    plot_legend(lag_corr_dict)


    plt.tight_layout()


    logx.save_matplotlib_image(title)

    plt.show();


# In[207]:


#*******************************************************************************************
 #
 #  Function Name:  plot_lag_corr_bar_chart
 #
 #  Function Description:
 #      The function plots the lagging correlation between two series as a bar chart.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  series         x_series         The parameter is the x-values series.
 #  series         y_series         The parameter is the y-values series.
 #  string         title            The parameter is the plot title.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def plot_lag_corr_bar_chart(x_series, y_series, title):

    lag_corrs_series \
        = mathx.lag_corr_time_series \
            (x_series, 
             y_series, 
             lag_corr_dict['params']['max_lag'], 
             lag_corr_dict['params']['method'])


    if lag_corr_dict['params']['max_lag'] > 30: lag_corr_dict['params']['linewidth'] = 0.0

    else: lag_corr_dict['params']['linewidth'] = 1.5


    corrs_idx_array = np.array(lag_corrs_series.index)

    corrs_array = np.array(lag_corrs_series)


    peak_lag_idx = lag_corrs_series.abs().idxmax()

    peak_r = lag_corrs_series[peak_lag_idx]


    _, ax \
        = plt.subplots \
            (figsize \
                = (lag_corr_dict['figure']['width'], 
                   lag_corr_dict['figure']['length']))


    set_lag_corr_title(title) 

    set_lag_corr_xylabels \
        (f"lag (days)\n← {lag_corr_dict['ylabel']['text'][0]} leads {lag_corr_dict['xlabel']['text'][0]}     " \
             + f"{lag_corr_dict['xlabel']['text'][0]} leads {lag_corr_dict['ylabel']['text'][0]} →", 'r-value')


    colors_array \
        = np.array \
            ([lag_corr_dict['params']['upr_clr'] \
                if r >= 0 else lag_corr_dict['params']['lwr_clr'] \
                for r in corrs_array])


    ax.bar \
        (corrs_idx_array, 
         corrs_array, 
         width = lag_corr_dict['vertical']['width'],
         bottom = lag_corr_dict['vertical']['bottom'],
         align = lag_corr_dict['params']['align'],
         color = colors_array, 
         edgecolor = lag_corr_dict['params']['edgecolor'],
         linewidth = lag_corr_dict['params']['linewidth'],
         tick_label = lag_corr_dict['params']['tick_label'],
         log = lag_corr_dict['params']['log'],
         alpha = lag_corr_dict['params']['alpha'])


    ax.axhline \
        (y = lag_corr_dict['axh_out']['y'], 
         color = lag_corr_dict['axh_out']['color'], 
         linestyle = lag_corr_dict['axh_out']['linestyle'], 
         fillstyle = lag_corr_dict['axh_out']['fillstyle'], 
         linewidth = lag_corr_dict['axh_out']['linewidth'],
         alpha = lag_corr_dict['axh_out']['alpha'], 
         label = f"r = ±{lag_corr_dict['axh_out']['y']}")

    ax.axhline \
        (y = 0.0, 
         color = lag_corr_dict['axh_ctr']['color'], 
         linestyle = lag_corr_dict['axh_ctr']['linestyle'], 
         fillstyle = lag_corr_dict['axh_ctr']['fillstyle'], 
         linewidth = lag_corr_dict['axh_ctr']['linewidth'],
         alpha = lag_corr_dict['axh_ctr']['alpha'])

    ax.axhline \
        (y = operator.neg(roll_corr_dict['axh_out']['y']), 
         color = lag_corr_dict['axh_out']['color'], 
         linestyle = lag_corr_dict['axh_out']['linestyle'], 
         fillstyle = lag_corr_dict['axh_out']['fillstyle'], 
         linewidth = lag_corr_dict['axh_out']['linewidth'],
         alpha = lag_corr_dict['axh_out']['alpha'])


    ax.axvline \
        (x = 0.0, 
         color = lag_corr_dict['axv']['color'], 
         linestyle = lag_corr_dict['axv']['linestyle'],
         fillstyle = lag_corr_dict['axv']['fillstyle'],
         linewidth = lag_corr_dict['axv']['linewidth'],
         alpha = lag_corr_dict['axv']['alpha'],
         label = 'no lag')


    ax.annotate \
        (f'Peak: lag = {peak_lag_idx}, r = {peak_r:.3f}',
         xy = (peak_lag_idx, peak_r),
         xytext \
             = (peak_lag_idx + lag_corr_dict['annotation']['xoffset'], 
                peak_r + lag_corr_dict['annotation']['yoffset']),
         arrowprops \
            = dict \
                (arrowstyle = lag_corr_dict['annotation']['arrw_stl'], 
                 color = lag_corr_dict['annotation']['arrw_clr']),
         fontsize = lag_corr_dict['annotation']['fontsize'])


    plot_title_axes(lag_corr_dict)

    plot_limits(lag_corr_dict)

    plot_ticks(lag_corr_dict)

    plot_legend(lag_corr_dict)


    plt.tight_layout()


    logx.save_matplotlib_image(title)

    plt.show();


# In[208]:


#*******************************************************************************************
 #
 #  Function Name:  plot_lag_heatmap
 #
 #  Function Description:
 #      The function plots the heatmap of lag correlations for all economic variables 
 #      at once. Rows = variables, Columns = lag days
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  series         input_series     The parameter is the input series.
 #  dictionary     comp_dict The parameter is the comparison series dictionary.
 #  string         title            The parameter is the plot title.
 #  integer        max_lag          The parameter is the maximum lag.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def plot_lag_heatmap(input_series, comp_dict, title, max_lag = None):

    if max_lag is None: max_lag_int = lag_heat_dict['params']['max_lag']

    else: max_lag_int = max_lag


    lag_matrix_dict = {}

    for label, series in comp_dict.items():

        corr_method = mathx.find_opt_corr_method(series, input_series)

        lag_matrix_dict[label] \
            = mathx.lag_corr_time_series \
                (input_series, series, max_lag_int, corr_method)


    lag_df = pd.DataFrame(lag_matrix_dict).transpose()


    _, ax \
        = plt.subplots \
            (figsize \
                = (lag_heat_dict['figure']['width'], 
                   lag_heat_dict['figure']['length']))


    im \
        = ax.imshow \
            (lag_df.values * -1.0, 
             aspect = lag_heat_dict['params']['aspect'], 
             cmap = lag_heat_dict['params']['cmap'], 
             vmin = lag_heat_dict['params']['vmin'], 
             vmax = lag_heat_dict['params']['vmax'])


    ax.set_xticks(range(len(lag_df.columns)))

    ax.set_yticks(range(len(lag_df.index)))


    ax.set_xticklabels \
        (np.array(lag_df.columns), 
         rotation = lag_heat_dict['xticks']['rotation'], 
         fontsize = lag_heat_dict['xticks']['fontsize'])

    ax.set_yticklabels \
        (np.array(lag_df.index), 
         rotation = lag_heat_dict['yticks']['rotation'], 
         fontsize = lag_heat_dict['yticks']['fontsize'])


    zero_col = list(lag_df.columns).index(0)


    ax.axvline \
        (x = zero_col, 
         color = lag_heat_dict['axv']['color'], 
         linestyle = lag_heat_dict['axv']['linestyle'],
         fillstyle = lag_heat_dict['axv']['fillstyle'],
         linewidth = lag_heat_dict['axv']['linewidth'],
         label = 'no lag')


    plt.colorbar(im, ax = ax, label = 'r-value')


    ax.set_xlabel \
        (f"lag (days)\n← {lag_heat_dict['ylabel']['text']} leads {lag_heat_dict['xlabel']['text']}" \
            + f"     {lag_heat_dict['xlabel']['text']} leads {lag_heat_dict['ylabel']['text']} →",
         fontdict = {'fontsize': lag_heat_dict['xlabel']['fontsize'], 
                     'fontstyle': lag_heat_dict['xlabel']['fontstyle'],
                     'fontweight': lag_heat_dict['xlabel']['fontweight']},
         labelpad = lag_heat_dict['xlabel']['labelpad'],
         loc = lag_heat_dict['xlabel']['loc'])

    ax.set_title \
        (title,
         fontdict = {'fontsize': lag_heat_dict['title']['fontsize'], 
                     'fontstyle': lag_heat_dict['title']['fontstyle'],
                     'fontweight': lag_heat_dict['title']['fontweight']},
         loc = lag_heat_dict['title']['loc'],
         pad = lag_heat_dict['title']['pad'])


    plot_legend(lag_corr_dict)


    plt.tight_layout()


    logx.save_matplotlib_image(title)

    plt.show();


# In[209]:


#*******************************************************************************************
 #
 #  Function Name:  bar_chart
 #
 #  Function Description:
 #      The function plots a bar chart.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  object         input_obj        The parameter is the input object.
 #  string         title            The parameter is the chart title.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def bar_chart(input_obj, title):

    global bar_chart_dict


    bar_chart_dict['title']['text'] = [title]

    plot_figsize(bar_chart_dict)


    temp_obj = proc_chart_input(input_obj, chart_enum.BAR.value)

    plot_bar_chart(temp_obj, bar_chart_dict)


    plot_title_axes(bar_chart_dict)

    plot_limits(bar_chart_dict)

    plot_ticks(bar_chart_dict)

    plot_legend(bar_chart_dict)


    logx.save_matplotlib_image(title)

    plt.show();


# In[210]:


#*******************************************************************************************
 #
 #  Function Name:  boxplot_chart
 #
 #  Function Description:
 #      The function plots a boxplot chart.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  object         input_obj        The parameter is the input object.
 #  string         title            The parameter is the chart title.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def boxplot_chart(input_obj, title):

    global boxplot_chart_dict


    boxplot_chart_dict['title']['text'] = [title]

    plot_figsize(boxplot_chart_dict)


    data_list, tick_lbls_array = proc_chart_input(input_obj, chart_enum.BOXPLOT.value)

    plot_boxplot_chart(data_list, tick_lbls_array, boxplot_chart_dict)


    plot_title_axes(boxplot_chart_dict)

    plot_limits(boxplot_chart_dict)

    plot_ticks(boxplot_chart_dict, tick_lbls_array, True)


    logx.save_matplotlib_image(title)

    plt.show();


# In[211]:


#*******************************************************************************************
 #
 #  Function Name:  histogram_chart
 #
 #  Function Description:
 #      The function plots a histogram chart.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  object         input_obj        The parameter is the input object.
 #  string         title            The parameter is the chart title.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def histogram_chart(input_obj, title):

    global histogram_chart_dict


    histogram_chart_dict['title']['text'] = [title]        

    plot_figsize(histogram_chart_dict)


    data_array = proc_chart_input(input_obj, chart_enum.HISTOGRAM.value)

    plot_histogram_chart(data_array, histogram_chart_dict)


    plot_title_axes(histogram_chart_dict)

    plot_limits(histogram_chart_dict)

    plot_ticks(histogram_chart_dict)

    plot_legend(histogram_chart_dict)


    logx.save_matplotlib_image(title)

    plt.show();


# In[212]:


#*******************************************************************************************
 #
 #  Function Name:  line_chart
 #
 #  Function Description:
 #      The function plots a line chart.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  object         input_obj        The parameter is the input object.
 #  string         title            The parameter is the chart title.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def line_chart(input_obj, title):

    global line_chart_dict


    line_chart_dict['title']['text'] = [title]        

    plot_figsize(line_chart_dict)


    temp_obj = proc_chart_input(input_obj, chart_enum.LINE.value)

    plot_line_chart(temp_obj, line_chart_dict)


    plot_title_axes(line_chart_dict)

    plot_limits(line_chart_dict)

    plot_ticks(line_chart_dict)

    plot_legend(line_chart_dict)


    logx.save_matplotlib_image(title)

    plt.show();


# In[213]:


#*******************************************************************************************
 #
 #  Function Name:  pie_chart
 #
 #  Function Description:
 #      The function plots a pie chart.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  object         input_obj        The parameter is the input object.
 #  string         title            The parameter is the chart title.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def pie_chart(input_obj, title):

    global pie_chart_dict


    pie_chart_dict['title']['text'] = [title]        

    plot_figsize(scatterplot_chart_dict)


    data_array, labels_array = proc_chart_input(input_obj, chart_enum.PIE.value)

    plot_pie_chart(data_array, labels_array, pie_chart_dict)


    plot_title_axes(pie_chart_dict)

    plot_legend(pie_chart_dict)


    logx.save_matplotlib_image(title)

    plt.show(); 


# In[214]:


#*******************************************************************************************
 #
 #  Function Name:  plot_chart
 #
 #  Function Description:
 #      The function plots a plot chart.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  object         input_obj        The parameter is the input object.
 #  string         title            The parameter is the chart title.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def plot_chart(input_obj, title):

    global plot_chart_dict


    plot_chart_dict['title']['text'] = [title]        

    plot_figsize(histogram_chart_dict)


    temp_obj = proc_chart_input(input_obj, chart_enum.PLOT.value)

    plot_plot_chart(temp_obj, plot_chart_dict)

    plot_peaks(temp_obj, plot_chart_dict)


    plot_title_axes(plot_chart_dict)

    plot_limits(plot_chart_dict)

    plot_ticks(plot_chart_dict)

    plot_legend(plot_chart_dict)


    logx.save_matplotlib_image(title)

    plt.show();


# In[215]:


#*******************************************************************************************
 #
 #  Function Name:  scatterplot_chart
 #
 #  Function Description:
 #      The function plots a scatterplot chart.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  object         input_obj        The parameter is the input object.
 #  string         title            The parameter is the chart title.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def scatterplot_chart(input_obj, title):

    global scatterplot_chart_dict


    scatterplot_chart_dict['title']['text'] = [title]

    plot_figsize(scatterplot_chart_dict)


    x_array, y_array = proc_chart_input(input_obj, chart_enum.SCATTER.value)

    plot_scatterplot_chart(x_array, y_array, scatterplot_chart_dict)


    plot_title_axes(scatterplot_chart_dict)

    plot_limits(scatterplot_chart_dict)

    plot_ticks(scatterplot_chart_dict)


    plot_regr_line(x_array, y_array)


    logx.save_matplotlib_image(title)

    plt.show();


# In[216]:


#*******************************************************************************************
 #
 #  Function Name:  line_multichart
 #
 #  Function Description:
 #      The function plots a line multichart.
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
 #  string         suptitle         The parameter is the multichart suptitle.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def line_multichart(input_df, suptitle):

    if line_multichart_dict['figure']['stacked']: 

        plot_line_multichart_stacked(input_df, suptitle)

    else: plot_line_multichart(input_df, suptitle)


# In[217]:


#*******************************************************************************************
 #
 #  Function Name:  scatterplot_multichart
 #
 #  Function Description:
 #      The function plots a scatterplot multichart.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  object         input_obj        The parameter is the input object.
 #  string         suptitle         The parameter is the multichart suptitle.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def pie_multichart(input_obj, suptitle):

    if pie_multichart_dict['figure']['stacked']: pass

    else: plot_pie_multichart(input_obj, suptitle)


# In[218]:


#*******************************************************************************************
 #
 #  Function Name:  scatterplot_multichart
 #
 #  Function Description:
 #      The function plots a scatterplot multichart.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  object         input_obj        The parameter is the input object.
 #  string         suptitle         The parameter is the multichart suptitle.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def scatterplot_multichart(input_obj, suptitle):

    if scatterplot_multichart_dict['figure']['stacked']: pass

    else: plot_scatterplot_multichart(input_obj, suptitle)


# In[ ]:




