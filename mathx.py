#!/usr/bin/env python
# coding: utf-8

# In[1]:


#*******************************************************************************************
 #
 #  File Name:  mathx.py
 #
 #  File Description:
 #      This Python script, py, contains Python functions for math calculations. 
 #      Here is the list:
 #
 #  za_regr_desc
 #  kpss_rejects_5pct_conclusions
 #  stationarity_conclusions
 #  autocorr_eff_n
 #  calc_clst_factors
 #  is_perf_sqr
 #  is_linear_trend
 #  exp_trend_calc_parm
 #  exp_trend_bool
 #  is_exponential_trend
 #  find_optimal_lag_corr_maxlag
 #  
 #  find_optimal_adf_regression
 #  find_optimal_adf_autolag
 #
 #  opt_adf_stnry_series
 #  opt_kpss_stnry_series
 #
 #  fnd_opt_za_regr_verbose
 #  find_optimal_za_regression
 #
 #  opt_zivot_andrews_series
 #  best_zivot_andrews_series
 #
 #  find_optimal_bp_model
 #  best_bai_perron_parms
 #  
 #  opt_bai_perron_series
 #  best_bai_perron_series
 #
 #  opt_eg_coint_series
 #
 #  validate_granger_lag_inputs
 #  calc_granger_maxlag_cap
 #  calc_granger_var_crit_lags
 #  calc_granger_pacf_lag
 #  assemble_granger_criteria
 #  reconcile_granger_criteria
 #  build_granger_conclusion
 #
 #  build_granger_cv_splits
 #  calc_granger_forecast_mse
 #  calc_granger_pvalue
 #  eval_granger_method_on_fold
 #  aggregate_granger_fold_results
 #  norm_granger_series
 #  score_granger_methods
 #  build_optimal_granger_method_conclusion
 #
 #  find_optimal_granger_lag
 #  find_optimal_granger_method
 #  granger_causality_test
 #  
 #  validate_var_vecm_inputs
 #  check_var_vecm_stationarity
 #  select_vecm_coint_rank
 #  select_var_lag_order
 #  fit_var_model
 #  calc_vecm_half_life
 #  fit_vecm_model
 #  calc_var_vecm_irf
 #  calc_var_vecm_fevd
 #  build_var_vecm_summary_df
 #  fit_var_or_vecm
 #
 #  opt_poly_deg_parms
 #  opt_poly_deg_rslt_dict
 #  find_opt_poly_degree
 #
 #  hp_smooth_matrix
 #  hp_info_crit
 #  find_opt_hp_lambda
 # 
 #  roll_corr_time_series
 #  detrend_time_series
 #  diff_time_series
 #  log_diff_time_series
 #  log_detrend_time_series
 #  hp_filter_time_series
 #  boxcox_time_series
 #
 #  crct_diff_stnry_series
 #  crct_trend_stnry_series
 #  crct_non_stnry_series
 #
 #  regr_model_eqn_coef
 #  regr_model_eqn_coef_disp
 #
 #  rtn_poly_line_array
 #  rtn_eqn_as_text
 #  rtn_r_sqr
 #  rtn_stats_values
 #  
 #  use_median_kfold_cv_errors
 #
 #  opt_poly_degree_mse_rslts
 #  opt_poly_degree_mse
 #  opt_poly_degree_ic_rslts
 #  opt_poly_degree_ic
 #
 #  opt_poly_deg_rslts_list_parms
 #  opt_poly_deg_rslts_list
 #  opt_poly_deg_cnd_list
 #  opt_poly_deg_final_dict
 #  opt_poly_degree
 #
 #  calc_single_corr
 #  calc_single_pval
 #  calc_rolling_corr
 #  calc_rolling_pvals
 #  calc_pct_significant
 #  calc_ac1
 #  calc_ac1_penalty
 #  calc_cv_stats
 #  is_window_feasible
 #  get_fold_sizes
 #  normalize_array
 #  calc_scores
 #  build_window_record
 #  find_opt_roll_wndw_rslts_df
 #  find_optimal_rolling_window
 #
 #  calc_rolling_corr_minp
 #  calc_rolling_pvals_minp
 #  calc_nan_fraction
 #  calc_valid_rc_stats
 #  calc_pct_sig_minp
 #  calc_warmup_cost
 #  calc_stability_ratio
 #  calc_convergence_index
 #  calc_cv_stats_minp
 #  get_cv_fold_sizes_minp
 #  is_minp_feasible
 #  build_minp_record
 #  calc_scores_minp
 #  opt_min_prd_rslts_df
 #  find_optimal_min_periods
 #
 #  select_pct_mth_parms
 #  select_pct_mth
 #  select_percentile_method
 #
 #  has_outliers
 #  find_opt_corr_method
 #  best_method_corr_matrix
 #
 #  calc_fold_errors_array
 #  best_roll_window_rslt_list
 #  best_window_min_period_cv_error
 #  best_window_min_period_cv_error_all
 #
 #  calc_maxlag
 #  calc_maxlag_all
 #  calc_autocorr_maxlag
 #  calc_autocorr_maxlag_all
 #
 #  zivot_andrews_test_summ_df
 #  zivot_andrews_best_test_summ_df
 #  adf_test_summ_df
 #  kpss_test_summ_df
 #  cross_phase_corr_summ_df
 #  bai_perron_segs_list
 #  bai_perron_bbi_bbp
 #  bai_perron_test_summ_df
 #  bai_perron_best_test_summ_df
 #  crss_valid_for_stnry_df
 #  crct_stnry_df
 #
 #  opt_degree_summ_df
 #  eg_coint_test_summ_df
 #  opt_window_summ_df
 #  opt_min_period_summ_df
 #  lag_corr_time_series
 #  rp_corr_at_lag_time_series
 #  lag_corr_summ_df
 #
 #  calc_granger_component_score
 #  calc_var_vecm_component_score
 #  calc_cointegration_component_score
 #  calc_lag_corr_component_score
 #  calc_correlation_component_score
 #  score_one_xy_pair
 #  build_causal_score_summary_df
 #  score_x_vs_y_dict
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  03/04/2024          Initial Development                         Nicholas J. George
 #  02/24/2026          Upgraded Module                             Nicholas J. George
 #
 #******************************************************************************************/

import dtypesx
import logx

import copy
import warnings

import datetime as dt
import numpy    as np
import pandas   as pd
import ruptures as rpt

from scipy.optimize                    import minimize_scalar

from scipy.stats                       import boxcox
from scipy.stats                       import kurtosis
from scipy.stats                       import normaltest
from scipy.stats                       import skew

from scipy.stats                       import shapiro

from scipy.stats                       import pearsonr
from scipy.stats                       import spearmanr
from scipy.stats                       import kendalltau

from scipy.stats                       import ttest_1samp

from sklearn.pipeline                  import Pipeline

from sklearn.metrics                   import r2_score

from sklearn.linear_model              import LinearRegression

from sklearn.metrics                   import mean_squared_error

from sklearn.model_selection           import cross_val_score
from sklearn.model_selection           import KFold
from sklearn.model_selection           import TimeSeriesSplit

from sklearn.preprocessing             import PolynomialFeatures

from statsmodels                       import api as sm

from statsmodels.regression.linear_model import OLS
from statsmodels.tools                   import add_constant
from statsmodels.tsa.api                 import VAR
from statsmodels.tsa.filters.hp_filter   import hpfilter

from statsmodels.tsa.stattools         import adfuller
from statsmodels.tsa.stattools         import coint
from statsmodels.tsa.stattools         import kpss
from statsmodels.tsa.stattools         import grangercausalitytests
from statsmodels.tsa.stattools         import pacf
from statsmodels.tsa.stattools         import zivot_andrews

from statsmodels.tsa.vector_ar.vecm    import VECM
from statsmodels.tsa.vector_ar.vecm    import select_coint_rank

from statsmodels.tools.sm_exceptions   import InterpolationWarning
from statsmodels.tools.sm_exceptions   import ValueWarning

warnings.filterwarnings('ignore', category = InterpolationWarning)
warnings.filterwarnings('ignore', category = FutureWarning)
warnings.filterwarnings("ignore", category = ValueWarning)

pd.options.mode.chained_assignment = None


# In[2]:


CONSTANT_LOCAL_FILE_NAME = 'py'


# In[3]:


adf_regr_array = np.asarray(['c', 'ct', 'ctt', 'n'], dtype = str)

kpss_regr_array = np.asarray(['c', 'ct'], dtype = str)

kpss_nlags_list = ['auto', 'legacy', None]

za_regr_array = np.asarray(['c', 't', 'ct'], dtype = str)

bp_models_array = np.asarray(['l2', 'l1', 'rbf', 'ar'], dtype = str)

eg_coint_trend_list = ['ctt', 'ct', 'c', 'n']

eg_coint_trend_array = np.asarray(eg_coint_trend_list, dtype = str)

adf_autolag_list = ['AIC', 'BIC', 't-stat', None]


granger_valid_methods_list \
    = ['aic', 'bic', 'consensus', 'conservative', 'fpe', 'hqic', 'liberal', 'pacf']

regr_mthd_dict \
    = {'c':   'constant only',
       'ct':  'constant and trend',
       'ctt': 'constant, and linear and quadratic trend',
       'n':   'no constant, no trend'}

regr_mthd_za_dict \
    = {'c':  'intercept only (level shift)',
       't':  'trend only (slope shift)',
       'ct': 'intercept + trend (level & slope shift)'}


model_desc_dict \
    = {'l2':  'mean shift detection (changes in level)',
       'l1':  'median shift (robust to outliers)',
       'rbf': 'mean & variance shift (most general, default)',
       'ar':  'autoregressive model shift'}


# In[4]:


#*******************************************************************************************
 #
 #  Function Name:  za_regr_desc
 #
 #  Function Description:
 #      This function returns the regression method description for a zivot andrews test.
 #
 #
 #  Return Type: string
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  string         regr             The parameter is the regression method for a zivot
 #                                  andrews test.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def za_regr_desc(regr: str) -> str:

    regr = regr.strip().lower()


    if regr == 'c':    desc = 'constant only'

    elif regr == 't':  desc = 'trend only'

    elif regr == 'ct': desc = 'constant and trend'

    else:              desc = None


    return desc


# In[5]:


#*******************************************************************************************
 #
 #  Function Name:  kpss_rejects_5pct_conclusions
 #
 #  Function Description:
 #      This function returns the conclusion for a kpss 5% rejections test.
 #
 #
 #  Return Type: string
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  boolean        adf_rejects_5pct_bool
 #                                  The parameter is the result of the ADF 5% rejects test.
 #  boolean        kpss_rejects_5pct_bool
 #                                  The parameter is the result of the KPSS 5% rejects test.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def kpss_rejects_5pct_conclusions \
        (adf_rejects_5pct_bool:  bool, 
         kpss_rejects_5pct_bool: bool) \
-> str:

    if adf_rejects_5pct_bool and kpss_rejects_5pct_bool:

        conclusion = 'ambiguous — likely structural break, run ZA'

    elif not adf_rejects_5pct_bool and kpss_rejects_5pct_bool:

        conclusion = 'strong unit root'

    elif adf_rejects_5pct_bool and not kpss_rejects_5pct_bool:

        conclusion = 'strong stationarity'

    elif not adf_rejects_5pct_bool and not kpss_rejects_5pct_bool:

        conclusion = 'ambiguous — possibly near-unit-root or fractionally integrated'

    else: conclusion = None


    return None


# In[6]:


#*******************************************************************************************
 #
 #  Function Name:  stationarity_conclusions
 #
 #  Function Description:
 #      This function returns a result, conclusion, and recommendation based on the
 #      outcome of a ADF test and a KPSS test.
 #
 #
 #  Return Type: string, string, string
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  boolean        adf_bool         The parameter is the result of the ADF test.
 #  boolean        kpss_bool        The parameter is the result of the KPSS test.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def stationarity_conclusions \
        (adf_bool:  bool, 
         kpss_bool: bool) \
-> tuple[str, str, str]:

    if adf_bool and kpss_bool:

        result         = 'stationary'

        conclusion     = 'Both tests agree the series is stationary.'

        recommendation = 'No action needed.'

    elif adf_bool and not kpss_bool:

        result         = 'difference stationary' 

        conclusion     = 'Both tests agree a unit root exists.'

        recommendation = 'Try detrending and differencing.'

    elif not adf_bool and kpss_bool:

        result         = 'trend-stationary'

        conclusion     = 'Stationary around a trend.'

        recommendation = 'Try detrending, differencing, and log.'

    elif not adf_bool and not kpss_bool:

        result         = 'inconclusive'

        conclusion     = 'Results conflict.'

        recommendation = 'Try log, differencing, and box-cox.'

    else:

        result         = None

        conclusion     = None

        recommendation = None

    return result, conclusion, recommendation


# In[7]:


#*******************************************************************************************
 #
 #  Function Name:  autocorr_eff_n
 #
 #  Function Description:
 #      This function returns the most effective n value for autocorrelation.
 #
 #
 #  Return Type: integer
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  series         data_series      The parameter is the input data series.
 #  integer        n                This parameter is the number of data points.
 #  integer        n_lags           This parameter is the number of lags.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def autocorr_eff_n \
        (data_series: pd.Series,
         n:           int,
         n_lags:      int = 90) \
-> int:

    acf_sum_flt = 0.0

    for lag in range(1, min(n_lags + 1, n // 2)):

        r_flt = data_series.autocorr(lag = lag)

        if np.isnan(r_flt): break

        acf_sum_flt += r_flt

        if abs(r_flt) < 1.96 / np.sqrt(float(n)): break

    ess_flt = float(n) / max(1.0, 1.0 + 2.0 * acf_sum_flt)

    return max(10, int(ess_flt))


# In[8]:


#*******************************************************************************************
 #
 #  Function Name:  calc_clst_factors
 #
 #  Function Description:
 #      This function calculates and returns the two closest factors of an integer.
 #
 #
 #  Return Type: integer, integer
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  integer        input_obj        The parameter is the input object.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def calc_clst_factors(input_obj) -> tuple[int, int]:

    c, int_bool = dtypesx.check_pos_int(input_obj)

    if int_bool == False: return None, None


    a, b, i = 1, c, 0  

    while a < b:

        i += 1

        if c % i == 0:

            a = i

            b = c // a

    return b, a


# In[9]:


#*******************************************************************************************
 #
 #  Function Name:  is_perf_sqr
 #
 #  Function Description:
 #      This function indicates whether the input is a perfect square.
 #
 #
 #  Return Type: boolean
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  integer        input_obj        The parameter is the input object.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def is_perf_sqr(input_obj: object) -> bool:

    data_int, int_bool = dtypesx.check_pos_int(input_obj)

    if int_bool == False: return data_int


    if data_int == 0 or data_int == 1: return True


    x_int = data_int // 2

    seen = set([x_int])


    while x_int * x_int != data_int:

        x_int = (x_int + (data_int // x_int)) // 2

        if x_int in seen: return False

        seen.add(x_int)


    return True


# In[10]:


#*******************************************************************************************
 #
 #  Function Name:  is_linear_trend
 #
 #  Function Description:
 #      This function returns True if the series has a statistically significant 
 #      linear trend.
 #
 #
 #  Return Type: boolean
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  series         input_series     The parameter is the input series.
 #  integer        prec             The parameter is the output number precision.
 #  float          alpha            The parameter is the p-value threshold.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def is_linear_trend \
        (input_series: pd.Series,
         prec:         int   = 6,
         alpha:        float = 0.05) \
-> bool:

    y_array, y_bool = dtypesx.check_data_dtype_array(input_series)

    if y_bool == False: return y_array


    X_array = np.arange(len(y_array), dtype = float)

    X_with_const_array = sm.add_constant(X_array)


    model = sm.OLS(y_array, X_with_const_array).fit()

    p_value = model.pvalues[1]


    return round(p_value, prec) < round(alpha, prec)


# In[11]:


#*******************************************************************************************
 #
 #  Function Name:  exp_trend_calc_parms
 #
 #  Function Description:
 #      This function calculates and returns parameters for determining exponential
 #      growth in a time series.
 #
 #
 #  Return Type: bool, float, float, float, float
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  array          data_array       The parameter is an array of time series values.
 #  array          t_array          The parameter is an array of sequential index values 
 #                                  for the time series.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def exp_trend_calc_parms \
        (data_array: np.ndarray,
         t_array   : np.ndarray) \
-> tuple[bool, float, float, float, float]:

    all_pos_bool             = bool(np.all(data_array > 0))

    if all_pos_bool:

        log_array            = np.log(data_array)

        log_r_flt, log_p_flt = pearsonr(t_array, log_array)

        log_lin_r2_flt       = log_r_flt ** 2

        log_lin_p_flt        = log_p_flt


        coeffs_array         = np.polyfit(t_array, log_array, 1)

        growth_rate_flt      = coeffs_array[0]

        doubling_flt         = np.log(2) / growth_rate_flt if growth_rate_flt > 0 else np.inf

    else:

        log_lin_r2_flt       = 0.0

        log_lin_p_flt        = 1.0

        growth_rate_flt      = 0.0

        doubling_flt         = np.inf

    return \
        all_pos_bool, \
        log_lin_r2_flt, \
        log_lin_p_flt, \
        growth_rate_flt, \
        doubling_flt


# In[12]:


#*******************************************************************************************
 #
 #  Function Name:  exp_trend_bool
 #
 #  Function Description:
 #      This function determines whether a time series exhibits exponential growth by
 #      counting the reasons it does not.
 #
 #
 #  Return Type: boolean
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  bool           all_pos_bool     The parameter indicates whether the time series has 
 #                                  all positive values.
 #  float          log_lin_p        The parameter is logarithm of the p value the log-linear 
 #                                  model must achieve..
 #  float          log_lin_r2       The parameter is logarithm of the R² the log-linear 
 #                                  model must achieve.
 #  float          lin_r2           The parameter is logarithm of the R² the linear model
 #                                  must achieve.
 #  float          min_r2           The parameter is the minimum R² the log-linear model
 #                                  must achieve.
 #  float          lin_vs_exp_gap   The parameter is the minimum margin by which 
 #                                  log-linear R² must beat linear R².
 #  float          growth_rate      The parameter is the log-linear model growth rate.
 #  integer        prec             The parameter is the output number precision.
 #  float          alpha            The parameter is the p-value threshold.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def exp_trend_bool \
        (all_pos_bool:   bool,
         log_lin_p:      float,
         log_lin_r2:     float,
         lin_r2:         float,
         min_r2:         float,
         lin_vs_exp_gap: float,
         growth_rate:    float,
         prec:           int   = 6,
         alpha:          float = 0.05) \
-> bool:

    reasons_int = 0

    if not all_pos_bool: reasons_int += 1

    if round(log_lin_p, prec) >= round(alpha, prec):  reasons_int += 1

    if round(log_lin_r2, prec) < round(min_r2, prec): reasons_int += 1

    if round((log_lin_r2 - lin_r2), prec) \
        < round(lin_vs_exp_gap, prec):                reasons_int += 1

    if growth_rate <= 0:                              reasons_int += 1


    exp_bool = reasons_int <= 0

    return exp_bool       


# In[13]:


#*******************************************************************************************
 #
 #  Function Name:  is_exponential_trend
 #
 #  Function Description:
 #      This function determines whether a time series exhibits exponential growth by
 #      comparing the fit quality of a linear OLS vs a log-linear OLS model.
 #
 #      A series is flagged as exponential when:
 #      1. All values are positive (log is defined)
 #      2. The log-linear model R² exceeds min_r2
 #      3. The log-linear model R² exceeds the linear model R² by at least lin_vs_exp_gap
 #      4. The log-linear correlation is statistically significant (p < alpha)
 #      5. The estimated growth rate is positive
 #
 #
 #  Return Type: boolean
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  object         input_obj        The parameter is the input object.
 #  float          min_r2           The parameter is the minimum R² the log-linear 
 #                                  model must achieve.
 #  float          lin_vs_exp_gap   The parameter is the minimum margin by which 
 #                                  log-linear R² must beat linear R².
 #  integer        prec             The parameter is the output number precision.
 #  float          alpha            The parameter is the p-value threshold.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def is_exponential_trend \
        (input_obj:      object,
         min_r2:         float = 0.80,
         lin_vs_exp_gap: float = 0.05,
         prec:           int   = 6,
         alpha:          float = 0.05) \
-> bool:

    data_array, data_bool = dtypesx.check_data_dtype_array(input_obj)

    if data_bool == False: return data_array


    n_int                 = len(data_array)

    t_array               = np.arange(n_int, dtype = float)


    lin_r_flt, lin_p_flt  = pearsonr(t_array, data_array)

    lin_r2_flt            = lin_r_flt ** 2


    all_pos_bool, \
    log_lin_r2_flt, \
    log_lin_p_flt, \
    growth_rate_flt, \
    doubling_flt \
        = exp_trend_calc_parms(data_array, t_array)


    exp_bool \
        = exp_trend_bool \
            (all_pos_bool, log_lin_p_flt, log_lin_r2_flt, lin_r2_flt, 
             min_r2, lin_vs_exp_gap, growth_rate_flt, prec, alpha)

    return exp_bool


# In[14]:


#*******************************************************************************************
 #
 #  Function Name:  find_optimal_lag_corr_maxlag
 #
 #  Function Description:
 #      This function returns the optimal max lag for lag correlation based on the lags 
 #      from a var/vecm analysis and a Granger Causality Test.
 #
 #
 #  Return Type: int
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  series         X_series         The parameter is an x-values array.
 #  series         y_series         The parameter is a y-values array.
 #  integer        var_vecm_lag     The parameter is the lag from a var/vecm analysis.
 #  integer        granger_lag      The parameter is the lag from a granger causality test.
 #  integer        abs_upr_bnd      The parameter is the minimum number of observations.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def find_optimal_lag_corr_maxlag \
        (X_series:         pd.Series,
         y_series:         pd.Series,
         var_vecm_lag:     int,
         granger_lag:      int,
         abs_upr_bnd:      int = 60) \
-> int:

    opt_maxlag  = min(abs_upr_bnd, max(abs(granger_lag) * 3, abs(var_vecm_lag) * 2))

    return opt_maxlag


# In[15]:


#*******************************************************************************************
 #
 #  Function Name:  find_optimal_adf_regression
 #
 #  Function Description:
 #      This function find the optimal regression specification for the Augmented 
 #      Dickey-Fuller test by evaluating all four regression types and selecting 
 #      the one that produces the strongest evidence against the unit root null 
 #      hypothesis, relative to the appropriate critical value.
 #
 #
 #  Return Type: string, dictionary
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  object         input_obj        The parameter is the input object.
 #  integer/none   maxlag           The parameter is the maximum lag which is included 
 #                                  in test, default value of 12*(nobs/100)^{1/4} is used 
 #                                  when None.
 #  string         autolag          The parameter is the method to select the lag length 
 #                                  when using automatic selection.
 #  integer        prec             The parameter is the output number precision.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def find_optimal_adf_regression \
        (data_array: np.ndarray,
         maxlag:     int   = None,
         autolag:    str   = 'BIC',
         prec:       int   = 6,
         alpha:      float = 0.05) \
-> tuple[str, dict]:

    results_dict = {}

    opt_margin_flt = 1.0*(10**3)

    for regr in adf_regr_array:

        if autolag is None:

            adf_stat, \
            p_value, \
            used_lag, \
            n_obs, \
            crit_vals_dict \
                = adfuller \
                    (data_array,
                     regression = regr,
                     autolag    = autolag,
                     maxlag     = maxlag)

        else:

            adf_stat, \
            p_value, \
            used_lag, \
            n_obs, \
            crit_vals_dict, _ \
                = adfuller \
                    (data_array,
                     regression = regr,
                     autolag    = autolag,
                     maxlag     = maxlag)


        cv_5pct_flt       = crit_vals_dict['5%']

        margin_flt        = adf_stat - cv_5pct_flt

        rejects_5pct_bool = round(adf_stat, prec) < round(cv_5pct_flt, prec)


        if round(opt_margin_flt, prec) >= round(margin_flt, prec):

            opt_adf_stat_flt      = adf_stat

            opt_p_value_flt       = p_value

            opt_used_lag          = used_lag

            opt_n_obs             = n_obs

            opt_crit_vals_dict    = copy.deepcopy(crit_vals_dict)

            opt_margin_flt        = margin_flt

            opt_rejects_5pct_bool = rejects_5pct_bool

            opt_regression        = regr

            opt_regr_mthd         = regr_mthd_dict[regr]

            opt_autolag_mthd      = autolag


    opt_stationary_bool = round(opt_p_value_flt, prec) < round(alpha, prec)


    result_dict \
        = {'regression':   str(opt_regression),
           'regr. mthd.':  str(opt_regr_mthd),
           'adf_stat':     float(round(opt_adf_stat_flt,          prec)),
           'p_value':      float(round(opt_p_value_flt,           prec)),
           'used_lag':     int(opt_used_lag),
           'n_obs':        int(opt_n_obs),
           '1%':           float(round(opt_crit_vals_dict['1%'],  prec)),
           '5%':           float(round(opt_crit_vals_dict['5%'],  prec)),
           '10%':          float(round(opt_crit_vals_dict['10%'], prec)),
           'margin':       float(round(opt_margin_flt,            prec)),
           'rejects_5pct': bool(opt_rejects_5pct_bool),
           'stationary':   bool(opt_stationary_bool)}

    return opt_regr_mthd, result_dict


# In[16]:


#*******************************************************************************************
 #
 #  Function Name:  find_optimal_adf_autolag
 #
 #  Function Description:
 #      This function find the optimal autolag parameter for the Augmented Dickey-Fuller 
 #      test by evaluating all four lag selection methods and selecting the one that
 #      produces the strongest evidence against the unit root null hypothesis, relative 
 #      to the 5% critical value.
 #
 #
 #  Return Type: string, dictionary
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  object         input_obj        The parameter is the input object.
 #  string         regression       The parameter is the regression method.
 #  integer/none   maxlag           The parameter is the maximum lag which is included 
 #                                  in test, default value of 12*(nobs/100)^{1/4} is used 
 #                                  when None.
 #  integer        prec             The parameter is the output number precision.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def find_optimal_adf_autolag \
        (data_array: np.ndarray,
         regression: str   = 'c',
         maxlag:     int   = None,
         prec:       int   = 6,
         alpha:      float = 0.05) \
-> tuple[str, dict]:

    results_dict = {}

    opt_margin_flt = 1.0*(10**3)

    for autolag in adf_autolag_list:

        if autolag is None:

            adf_stat, \
            p_value, \
            used_lag, \
            n_obs, \
            crit_vals_dict \
                = adfuller \
                    (data_array,
                     regression = regression,
                     autolag    = autolag,
                     maxlag     = maxlag)

        else:

            adf_stat, \
            p_value, \
            used_lag, \
            n_obs, \
            crit_vals_dict, _ \
                = adfuller \
                    (data_array,
                     regression = regression,
                     autolag    = autolag,
                     maxlag     = maxlag)


        cv_5pct_flt       = crit_vals_dict['5%']

        margin_flt        = adf_stat - cv_5pct_flt

        rejects_5pct_bool = round(adf_stat, prec) < round(cv_5pct_flt, prec)


        if round(opt_margin_flt, prec) >= round(margin_flt, prec):

            opt_adf_stat_flt      = adf_stat

            opt_p_value_flt       = p_value

            opt_used_lag          = used_lag

            opt_n_obs             = n_obs

            opt_crit_vals_dict    = copy.deepcopy(crit_vals_dict)

            opt_margin_flt        = margin_flt

            opt_rejects_5pct_bool = rejects_5pct_bool

            opt_autolag_mthd      = autolag


    opt_stationary_bool = round(opt_p_value_flt, prec) < round(alpha, prec)


    result_dict \
        = {'autolag':      str(opt_autolag_mthd),
           'adf_stat':     float(round(opt_adf_stat_flt,          prec)),
           'p_value':      float(round(opt_p_value_flt,           prec)),
           'used_lag':     int(opt_used_lag),
           'n_obs':        int(opt_n_obs),
           '1%':           float(round(opt_crit_vals_dict['1%'],  prec)),
           '5%':           float(round(opt_crit_vals_dict['5%'],  prec)),
           '10%':          float(round(opt_crit_vals_dict['10%'], prec)),
           'margin':       float(round(opt_margin_flt,            prec)),
           'rejects_5pct': bool(opt_rejects_5pct_bool),
           'stationary':   bool(opt_stationary_bool)}

    return opt_autolag_mthd, result_dict


# In[17]:


#*******************************************************************************************
 #
 #  Function Name:  opt_adf_stnry_series
 #
 #  Function Description:
 #      This function returns the result based on a minimal p value from a time series
 #      Augmented Dickey-Fuller (ADF) test. This test checks whether a time series has
 #      a unit root (i.e., is non-stationary), formalizing why the correlations cannot 
 #      be taken at face value.
 #
 #
 #  Return Type: dict
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  object         input_obj        The parameter is the input object.
 #  integer/none   maxlag           The parameter is the maximum lag which is included 
 #                                  in test, default value of 12*(nobs/100)^{1/4} is used 
 #                                  when None.
 #  integer        prec             The parameter is the output number precision.
 #  float          alpha            The parameter is the p-value threshold.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def opt_adf_stnry_series \
        (input_obj:  object,
         index:      str,
         maxlag:     int   = None,
         prec:       int   = 6,
         alpha:      float = 0.05) \
-> tuple[str, str, dict]:

    data_array, data_bool = dtypesx.check_data_dtype_array(input_obj)

    if data_bool == False: return None


    opt_margin_flt = 1.0*(10**3)

    for regr in adf_regr_array:

        for autolag in adf_autolag_list:

            if autolag is None:

                adf_stat, \
                p_value, \
                used_lag, \
                n_obs, \
                crit_vals_dict \
                    = adfuller \
                        (data_array,
                         regression = regr,
                         autolag    = autolag,
                         maxlag     = maxlag)

            else:

                adf_stat, \
                p_value, \
                used_lag, \
                n_obs, \
                crit_vals_dict, _ \
                    = adfuller \
                        (data_array,
                         regression = regr,
                         autolag    = autolag,
                         maxlag     = maxlag)


            cv_5pct_flt       = crit_vals_dict['5%']

            margin_flt        = adf_stat - cv_5pct_flt

            rejects_5pct_bool = round(adf_stat, prec) < round(cv_5pct_flt, prec)


            if round(opt_margin_flt, prec) >= round(margin_flt, prec):

                opt_adf_stat_flt      = adf_stat

                opt_p_value_flt       = p_value

                opt_used_lag          = used_lag

                opt_n_obs             = n_obs

                opt_crit_vals_dict    = copy.deepcopy(crit_vals_dict)

                opt_margin_flt        = margin_flt

                opt_rejects_5pct_bool = rejects_5pct_bool

                opt_regr_mthd         = regr_mthd_dict[regr]

                opt_autolag_mthd      = autolag


    result_dict \
        = {'series':       index,
           'adf_stat':     float(round(opt_adf_stat_flt,          prec)),
           'p_value':      float(round(opt_p_value_flt,           prec)),
           'used_lag':     int(opt_used_lag),
           'n_obs':        int(opt_n_obs),
           '1%':           float(round(opt_crit_vals_dict['1%'],  prec)),
           '5%':           float(round(opt_crit_vals_dict['5%'],  prec)),
           '10%':          float(round(opt_crit_vals_dict['10%'], prec)),
           'margin':       float(round(opt_margin_flt,            prec)),
           'regr. mthd.':  str(opt_regr_mthd),
           'autolag':      str(opt_autolag_mthd),
           'stationary':   bool(opt_rejects_5pct_bool)}

    return result_dict


# In[18]:


#*******************************************************************************************
 #
 #  Function Name:  opt_kpss_stnry_series
 #
 #  Function Description:
 #      This function returns the optimal Kwiatkowski-Phillips-Schmidt-Shin (KPSS) test 
 #      result for a time series based on a minimal p value. The ADF test checks whether 
 #      a series has a unit root (i.e., is non-stationary), formalizing why the full-period 
 #      correlations cannot be taken at face value. This test has a reversed null hypothesis 
 #      compared to the ADF test.
 #
 #
 #  Return Type: dictionary
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  object         input_object     The parameter is the input object.
 #  string/integer nlags            The parameter indicates the number of lags.
 #  integer        prec             The parameter is the output number precision.
 #  float          alpha            The parameter is the p-value threshold.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def opt_kpss_stnry_series \
        (input_obj:   object,
         index:       str,
         max_lags:    int = None,
         prec:        int    = 6,
         alpha:       float  = 0.05) \
-> dict:

    data_array, data_bool = dtypesx.check_data_dtype_array(input_obj)

    if data_bool == False: return None


    opt_margin_flt = 1.0*(10**3)

    for regr in kpss_regr_array:

        for nlags in kpss_nlags_list:

            kpss_stat, p_value, n_lags_used, crit_vals_dict \
                = kpss(data_array, regression = regr, nlags = nlags, store = False)


            cv_5pct_flt       = crit_vals_dict['5%']

            margin_flt        = kpss_stat - cv_5pct_flt

            rejects_5pct_bool = round(kpss_stat, prec) > round(cv_5pct_flt, prec)


            if round(opt_margin_flt, prec) >= round(margin_flt, prec):

                    opt_kpss_stat_flt     = kpss_stat

                    opt_p_value_flt       = p_value

                    opt_n_lags            = nlags

                    opt_n_lags_used       = n_lags_used

                    opt_crit_vals_dict    = copy.deepcopy(crit_vals_dict)

                    opt_margin_flt        = margin_flt

                    opt_regr_mthd         = regr_mthd_dict[regr]

                    opt_rejects_5pct_bool = rejects_5pct_bool

                    opt_stationarity      = not opt_rejects_5pct_bool


    result_dict \
        = {'series':       index,
           'kpss_stat':    float(round(opt_kpss_stat_flt,         prec)),
           'p_value':      float(round(opt_p_value_flt,           prec)),
           'n_lags':       str(opt_n_lags),
           'n_lags_used':  int(opt_n_lags_used),
           '1%':           float(round(opt_crit_vals_dict['1%'],  prec)),
           '5%':           float(round(opt_crit_vals_dict['5%'],  prec)),
           '10%':          float(round(opt_crit_vals_dict['10%'], prec)),
           'margin':       float(round(opt_margin_flt,            prec)),
           'regr. mthd.':  str(opt_regr_mthd),
           'stationary':   bool(not opt_rejects_5pct_bool)}

    return result_dict


# In[19]:


#*******************************************************************************************
 #
 #  Function Name:  fnd_opt_za_regr_verbose
 #
 #  Function Description:
 #      This function reports the results for the find_optimal_za_regression function. 
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  dict           results_dict     The parameter is the results dictionary
 #  string         optimal_method   The parameter is the optimal regression method.
 #  boolean        any_rejects_bool The parameter indicates if there are any rejects.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def fnd_opt_za_regr_verbose \
        (results_dict:     dict,
         optimal_method:   str,
         any_rejects_bool: bool):

    if not any_rejects_bool:

        print('WARNING: No regression method rejects the unit root null at the 5% level.\n'   + \
              'The series may contain a unit root that persists across all specifications.\n' + \
              f"Returning '{optimal_method}' as the closest to rejection.\n\n")


    print(f"\n{'='*65}\n"                                           + \
          '  Zivot-Andrews Regression Selection\n'                  + \
          f"{'='*65}\n"                                             + \
          f"{'Method':<8} {'Stat':>8} {'CV 5%':>8} "              + \
          f"{'Margin':>8} {'Lag':>5} {'Break':>7} {'Reject?':>9}\n" + \
          f"{'-'*57}\n")

    for method in za_regr_array:

        r = results_dict[method]

        marker = ' <-- optimal' if method == optimal_method else ''

        print(f"{method:<8} {r['stat']:>8.4f} {r['cv_5pct']:>8.4f}\n"       + \
              f"{r['margin']:>8.4f} {r['baselag']:>5} {r['breakpoint']:>7}\n" + \
              f"{'Yes' if r['rejects_5pct'] else 'No':>9}{marker}\n")

    print(f"{'='*65}\n" + \
          f"  Optimal method : {optimal_method}\n"                   + \
          '  Selection rule : most negative (stat - CV 5%) margin\n' + \
          f"{'='*65}\n")


# In[20]:


#*******************************************************************************************
 #
 #  Function Name:  find_optimal_za_regression
 #
 #  Function Description:
 #      This function find the optimal regression method for the Zivot-Andrews structural 
 #      break test by evaluating all three regression specifications and selecting the one 
 #      that provides the strongest evidence against the null hypothesis of a unit root
 #      with structural break.
 #
 #      The Zivot-Andrews test evaluates three models:
 #          'c'  - Allows for a one-time change in the level (intercept break)
 #          't'  - Allows for a one-time change in the trend slope (trend break)
 #          'ct' - Allows for breaks in both the level and trend simultaneously
 #
 #      Selection criterion:
 #          The optimal regression is the one that produces the most negative test 
 #          statistic relative to its corresponding critical value at the 5%
 #          significance level. This is measured by the margin:
 #
 #              margin = test_statistic - critical_value_5pct
 #
 #      A more negative margin means the test statistic is further into the rejection
 #      region, indicating stronger evidence of stationarity around a structural break
 #      under that specification.
 #
 #
 #  Return Type: string, dictionary
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  array          data_array       The parameter is the time series to test, which 
 #                                  should be a univariate series with no NaN values.
 #  string         autolag          The parameter is the method to select the lag length 
 #                                  when using automatic selection.
 #  integer        prec             The parameter is the output number precision.
 #  boolean        verbose          The parameter, if True, prints a diagnostic table of 
 #                                  results for all three regression methods.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def find_optimal_za_regression \
        (data_array: np.ndarray,
         autolag:     str = 'BIC',
         prec:        int = 6,
         verbose:     bool = False) \
-> tuple[str, dict]:

    results_dict = {}

    for method in za_regr_array:

        za_stat, p_value, crit_vals_dict, baselag, brk_pt \
            = zivot_andrews \
                (data_array, 
                 regression = method, 
                 autolag    = autolag)


        cv_5pct_flt       = crit_vals_dict['5%']

        margin_flt        = za_stat - cv_5pct_flt

        rejects_5pct_bool = round(za_stat, prec) < round(cv_5pct_flt, prec)


        results_dict[method] \
            = {'za_stat':      float(round(za_stat,               prec)),    
               'p_value':      float(round(p_value,               prec)),     
               '1%':           float(round(crit_vals_dict['1%'],  prec)),
               '5%':           float(round(crit_vals_dict['5%'],  prec)),
               '10%':          float(round(crit_vals_dict['10%'], prec)),
               'baselag':      int(baselag),
               'breakpoint':   int(brk_pt),
               'margin':       float(round(margin_flt,            prec)),
               'rejects_5pct': bool(rejects_5pct_bool)}


    optimal_method   = min(results_dict, key = lambda m: results_dict[m]['margin'])

    any_rejects_bool = any(r['rejects_5pct'] for r in results_dict.values())


    if verbose: fnd_opt_za_regr_verbose(results_dict, optimal_method, any_rejects_bool)


    return optimal_method, results_dict


# In[21]:


#*******************************************************************************************
 #
 #  Function Name:  opt_zivot_andrews_series
 #
 #  Function Description:
 #      This function returns the Zivot Andrews test on a time series.
 #
 #
 #  Return Type: dictionary
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  object         input_obj        The parameter is the input object.
 #  float          trim             The parameter is the percentage of series at begin/end 
 #                                  to exclude from break-period calculation in range 
 #                                  [0, 0.333] 
 #  string         maxlag           The parameter is the maximum lag which is included 
 #                                  in test, default value of 12*(nobs/100)^{1/4} is used 
 #                                  when None.
 #  string         autolag          The parameter is the method to select the lag length 
 #                                  when using automatic selection.
 #  integer        prec             The parameter is the output number precision.
 #  float          alpha            The parameter is the p-value threshold.
 #  float          ambiguous        The parameter is the upper bound for the ambiguous zone.
 #  boolean        verbose          The parameter, if True, prints a diagnostic table of 
 #                                  results for all three regression methods.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def opt_zivot_andrews_series \
        (input_obj: object,
         trim:      float  = 0.15,
         maxlag:    object = None,
         autolag:   str    = 'BIC',
         prec:      int    = 6,
         alpha:     float  = 0.05,
         ambiguous: float  = 0.15,
         verbose:   bool   = False) \
-> dict:

    data_array, data_bool = dtypesx.check_data_dtype_array(input_obj)

    if data_bool == False: return None


    if maxlag is None: maxlag_int = int(12.0 * (float(len(data_array)) / 100.0)**(0.25))

    else:              maxlag_int = int(abs(maxlag))


    n_int              = len(data_array)

    regr_method, _ \
        = find_optimal_za_regression \
            (data_array,
             autolag   = autolag,
             prec      = prec,
             verbose   = verbose)


    za_stat, \
    p_value, \
    crit_vals_dict, \
    lags_used, \
    break_seq_idx \
        = zivot_andrews \
            (data_array,
             trim       = trim,
             maxlag     = maxlag_int,
             regression = regr_method,
             autolag    = autolag)


    brk_pct_flt         = float(break_seq_idx) / float(n_int) * 100.0

    rejects_5pct_bool   = round(za_stat, prec) < round(crit_vals_dict['5%'], prec)


    break_index = input_obj.index[break_seq_idx]

    if isinstance(break_index, dt.date) \
        or isinstance(break_index, dt.datetime):           brk_idx = break_index.strftime('%Y-%m-%d')

    else:                                                brk_idx = str(break_index)


    if    round(p_value, prec) < round(alpha, prec):     stationary = 'stationary with break'

    elif  round(p_value, prec) < round(ambiguous, prec): stationary = 'ambiguous'

    else:                                                stationary = 'non-stationary'


    result_dict \
        = {'za_stat':      float(round(za_stat,               prec)),
           'p_value':      float(round(p_value,               prec)),
           '1%':           float(round(crit_vals_dict['1%'],  prec)),
           '5%':           float(round(crit_vals_dict['5%'],  prec)),
           '10%':          float(round(crit_vals_dict['10%'], prec)),
           'n_obs':        int(n_int),
           'lags_used':    int(lags_used),
           'break_sq_idx': int(break_seq_idx),
           'break_index':  brk_idx,
           'break_pct':    float(round(brk_pct_flt,           1)),
           'regr_mthd':    str(za_regr_desc(regr_method)),
           'autolag':      str(autolag),
           'rejects_5pct': bool(rejects_5pct_bool),
           'stationary':   stationary}


    return result_dict


# In[22]:


#*******************************************************************************************
 #
 #  Function Name:  best_zivot_andrews_series
 #
 #  Function Description:
 #      This function returns optimal Kwiatkowski-Phillips-Schmidt-Shin (KPSS) test 
 #      results for a series.
 #
 #
 #  Return Type: float, float, dictionary, integer, integer, integer, float, string, 
 #               string, boolean
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  object         input_obj        The parameter is the input object.
 #  float          trim             The parameter is the percentage of series at begin/end 
 #                                  to exclude from break-period calculation in range 
 #                                  [0, 0.333] 
 #  string         maxlag           The parameter is the maximum lag which is included 
 #                                  in test, default value of 12*(nobs/100)^{1/4} is used 
 #                                  when None.
 #  integer        prec             The parameter is the output number precision.
 #  float          alpha            The parameter is the p-value threshold.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def best_zivot_andrews_series \
        (input_obj: object,
         trim:      float  = 0.15,
         maxlag:    object = None,
         prec:      int    = 6,
         alpha:     float  = 0.05) \
-> tuple[float, float, dict, int, int, int, float, str, str, bool]:

    data_array, data_bool = dtypesx.check_data_dtype_array(input_obj)

    if data_bool == False: return None, None, None, None, None, None, None, None, None, None


    if maxlag is None: maxlag_int = int(12.0 * (float(len(data_array)) / 100.0)**(0.25))

    else:              maxlag_int = int(abs(maxlag))


    n_int            = len(data_array)

    best_p_value_flt = 0.0


    for regr in za_regr_array:

        for lag in adf_autolag_list:

            za_stat, p_value, critical_values, lags_used, break_index \
                = zivot_andrews \
                    (data_array,
                     trim = trim,
                     maxlag = maxlag_int,
                     regression = regr,
                     autolag = lag)

            if round(p_value, prec) >= round(best_p_value_flt, prec):

                best_za_stat_flt    = za_stat

                best_p_value_flt    = p_value

                best_crit_vals_dict = copy.deepcopy(critical_values)

                best_n_int          = n_int

                best_lags_used_int  = lags_used

                best_brk_idx_int    = break_index

                best_brk_pct_flt    = float(best_brk_idx_int) / float(n_int) * 100.0

                best_regr_mthd      = regr_mthd_za_dict[regr]

                best_autolag_mthd   = str(lag)

                best_stnry_bool     = round(best_p_value_flt, prec) < round(alpha, prec)

    return \
        best_za_stat_flt, \
        best_p_value_flt, \
        best_crit_vals_dict, \
        best_n_int, \
        best_lags_used_int, \
        best_brk_idx_int, \
        best_brk_pct_flt, \
        best_regr_mthd, \
        best_autolag_mthd, \
        best_stnry_bool


# In[23]:


#*******************************************************************************************
 #
 #  Function Name:  find_optimal_bp_model
 #
 #  Function Description:
 #      This function find the optimal ruptures segmentation model for Bai-Perron-style 
 #      structural break detection by evaluating all four cost models and selecting the 
 #      one that minimises the Bayesian Information Criterion (BIC).
 #
 #
 #  Return Type: string, dictionary
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  array          data_array       The parameter is the data array.
 #  array          signal_array     The parameter is the signal array.
 #  integer/none   n_breaks         The parameter determines whether to use Binary 
 #                                  Segmentation to find exactly this many breaks.
 #                                  Overrides penalty when provided.
 #  integer        max_breaks       The parameter is the maximum number of breaks to 
 #                                  consider.
 #  integer        min_size         The parameter is the minimum number of observations 
 #                                  between two breaks.
 #  integer        jump             The parameter is the subsampling — only consider 
 #                                  every jump-th point as a candidate break. 
 #                                  Lower = more precise but slower
 #  float/none     penalty          The parameter is the penalty value for PELT algorithm. 
 #                                  Higher = fewer breaks detected
 #                                  None triggers auto-calibration
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def find_optimal_bp_model \
        (data_array:   np.ndarray,
         signal_array: np.ndarray,
         n_breaks:     int   = None,
         max_breaks:   int   = 5,
         min_size:     int   = 10,
         jump:         int   = 5,
         penalty:      float = None) \
-> tuple[str, dict]:

    n = len(signal_array)

    if (1 + 1) * min_size > n:

        raise \
            ValueError \
                (f'Series length ({n}) is too short to support even 1 breakpoint '
                 f'with min_size = {min_size}. The function needs at least {2 * min_size} observations.')


    max_k = min(max_breaks, n // min_size - 1)

    if max_k < 1: max_k = 1


    params_per_seg_dict = {'l2': 1, 'l1': 1, 'rbf': 1, 'ar': 2}


    results_dict = {}

    for model_name in bp_models_array:

        algo \
            = rpt.Dynp \
                (model    = model_name,
                 min_size = min_size,
                 jump     = jump) \
                    .fit(signal_array)

        pps = params_per_seg_dict[model_name]

        if penalty is not None:

            bkps        = algo.predict(pen = penalty)

            cost        = algo.cost.sum_of_costs(bkps)

            proxy_rss   = max(cost, 1e-10)

            k_total     = len(bkps) - 1

            k_params    = (k_total + 1) * pps + k_total

            bic         = n * np.log(proxy_rss / n) + k_params * np.log(n)

            results_dict[model_name] \
                = {'breakpoints':    bkps,
                   'n_breakpoints':  k_total,
                   'cost':           cost,
                   'bic':            bic,
                   'bic_normalised': None,
                   'optimal_k':      None,
                   'params_per_seg': pps,
                   'is_optimal':     False}

        else:

            k_range   = [n_breaks] if n_breaks is not None else range(1, max_k + 1)


            bic_by_k_dict  = {}

            cost_by_k_dict = {}

            bkps_by_k_dict = {}

            for k in k_range:

                try:

                    bkps      = algo.predict(n_bkps = k)

                    cost      = algo.cost.sum_of_costs(bkps)

                    proxy_rss = max(cost, 1e-10)

                    k_params  = (k + 1) * pps + k

                    bic       = n * np.log(proxy_rss / n) + k_params * np.log(n)


                    bic_by_k_dict[k]  = bic

                    cost_by_k_dict[k] = cost

                    bkps_by_k_dict[k] = bkps

                except: continue


            if not bic_by_k_dict: continue


            optimal_k = min(bic_by_k_dict, key = bic_by_k_dict.get)

            results_dict[model_name] \
                = {'breakpoints'   : bkps_by_k_dict[optimal_k],
                   'n_breakpoints' : len(bkps_by_k_dict[optimal_k]) - 1,
                   'cost'          : cost_by_k_dict[optimal_k],
                   'bic'           : bic_by_k_dict[optimal_k],
                   'bic_normalised': None,
                   'optimal_k'     : optimal_k,
                   'bic_by_k'      : bic_by_k_dict,
                   'params_per_seg': pps,
                   'is_optimal'    : False}

    if not results_dict:

        raise ValueError('All models failed: the series may be too short for the given min_size.')


    for model_name in results_dict:

        own_min = results_dict[model_name]['bic']

        bic_vals = results_dict[model_name].get('bic_by_k', {own_min: own_min})

        own_min  = min(bic_vals.values()) if bic_vals else own_min


        results_dict[model_name]['bic_normalised'] = results_dict[model_name]['bic'] - own_min


    optimal_model = min(results_dict, key = lambda m: results_dict[m]['bic_normalised'])

    results_dict[optimal_model]['is_optimal'] = True


    return optimal_model, results_dict


# In[24]:


#*******************************************************************************************
 #
 #  Function Name:  bai_perron_parms
 #
 #  Function Description:
 #      This function provides the raw array and algorithm name for a Bai-Perron Test.
 #
 #
 #  Return Type: integer, string, string, list
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  array          data_array       The parameter is the data array.
 #  array          signal_array     The parameter is the signal array.
 #  integer        max_breaks       The parameter is the maximum number of breaks to 
 #                                  consider.
 #  integer        min_size         The parameter is the minimum number of observations 
 #                                  between two breaks.
 #  integer        jump             The parameter is the subsampling — only consider 
 #                                  every jump-th point as a candidate break. 
 #                                  Lower = more precise but slower
 #  float/none     penalty          The parameter is the penalty value for PELT algorithm. 
 #                                  Higher = fewer breaks detected
 #                                  None triggers auto-calibration
 #  integer/none   n_breaks         The parameter determines whether to use Binary 
 #                                  Segmentation to find exactly this many breaks.
 #                                  Overrides penalty when provided.
 #  integer        prec             The parameter is the output number precision.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def bai_perron_parms \
        (data_array:    np.ndarray,
         signal_array:  np.ndarray,
         max_breaks:    int,
         min_size:      int,
         jump:          int,
         penalty:       object,
         n_breaks:      object,
         prec:          int = 6) \
-> tuple[int, str, str, list]:

    n_int = len(data_array)

    most_brks_fnd_int = 0

    model, _ \
        = find_optimal_bp_model \
            (data_array,
             signal_array,
             n_breaks   = n_breaks,
             max_breaks = max_breaks,
             min_size   = min_size,
             jump       = jump,
             penalty    = penalty)


    if n_breaks is not None:

        pen_used_flt = None

        algorithm    = 'binseg'


        algo \
            = rpt.Binseg \
                (model    = model, 
                 min_size = min_size, 
                 jump     = jump) \
                    .fit(signal_array)

        raw_array \
            = algo.predict \
                (n_bkps  = n_breaks, 
                 pen     = pen_used_flt, 
                 epsilon = None)

    else:

        if penalty is None: penalty = np.log(float(n_int)) * np.std(data_array)


        pen_used_flt = round(penalty, prec)

        algorithm    = 'pelt'


        algo \
            = rpt.Pelt \
                (model    = model, 
                 min_size = min_size, 
                 jump     = jump) \
                    .fit(signal_array)

        raw_array    = algo.predict(pen = pen_used_flt)


    brk_idxs_list = sorted([b for b in raw_array if b < n_int])[:max_breaks]


    result_dict \
        = {'n':         n_int,
           'model':     model,
           'algorithm': algorithm,
           'brk_idxs':  brk_idxs_list}

    return result_dict


# In[25]:


#*******************************************************************************************
 #
 #  Function Name:  opt_bai_perron_series
 #
 #  Function Description:
 #      This function detects the maximum multiple structural breaks in a time series 
 #      using the Bai-Perron method via the ruptures library.
 #
 #      Two detection modes (mutually exclusive):
 #      - Penalty mode  (penalty != None) : PELT algorithm finds the optimal
 #        number of breaks automatically, penalising for complexity.
 #      - Fixed mode    (n_breaks != None): Binary segmentation finds exactly
 #        n_breaks breakpoints.
 #      - Default       (both None)       : Penalty mode with auto-calibrated
 #        penalty = log(n) * std(series).
 #
 #
 #  Return Type: integer, string, string, list, list, list
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  object         input_obj        The parameter is the input object.
 #  object         signal_obj       The parameter is the signal object.
 #  integer        max_breaks       The parameter is the maximum number of breaks to 
 #                                  consider.
 #  integer        min_size         The parameter is the minimum number of observations 
 #                                  between two breaks.
 #  integer        jump             The parameter is the subsampling — only consider 
 #                                  every jump-th point as a candidate break. 
 #                                  Lower = more precise but slower
 #  float/none     penalty          The parameter is the penalty value for PELT algorithm. 
 #                                  Higher = fewer breaks detected
 #                                  None triggers auto-calibration
 #  integer/none   n_breaks         The parameter determines whether to use Binary 
 #                                  Segmentation to find exactly this many breaks.
 #                                  Overrides penalty when provided.
 #  integer        prec             The parameter is the output number precision.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def opt_bai_perron_series \
        (input_obj:  object, 
         signal_obj: object,
         max_breaks: int    = 5,
         min_size:   int    = 30, 
         jump:       int    = 5, 
         penalty:    object = None, 
         n_breaks:   object = None, 
         prec:       int    = 6) \
-> tuple[int, str, str, list, list, list]:

    data_array, data_bool     = dtypesx.check_data_dtype_array(input_obj)

    signal_array, signal_bool = dtypesx.check_data_dtype_array(signal_obj)

    if data_bool == False or signal_bool == False: return None, None, None, None, None, None


    parms_result_dict \
        = bai_perron_parms \
            (data_array, 
             signal_array, 
             max_breaks = max_breaks, 
             min_size   = min_size, 
             jump       = jump, 
             penalty    = penalty, 
             n_breaks   = n_breaks, 
             prec       = prec)                

    brk_pcts_list \
        = [round(float(b) / float(parms_result_dict['n']) * 100.0, 1) \
           for b in parms_result_dict['brk_idxs']]

    seg_bnds_list = [0] + parms_result_dict['brk_idxs'] + [parms_result_dict['n']]


    result_dict \
        = {'n':         parms_result_dict['n'],
           'model':     parms_result_dict['model'],
           'algorithm': parms_result_dict['algorithm'],
           'brk_idxs':  parms_result_dict['brk_idxs'],
           'brk_pcts':  brk_pcts_list,
           'seg_bnds':  seg_bnds_list}

    return result_dict


# In[26]:


#*******************************************************************************************
 #
 #  Function Name:  best_bai_perron_parms
 #
 #  Function Description:
 #      This function provides the raw array and algorithm name for a Bai-Perron Test.
 #
 #
 #  Return Type: integer, string, string, list
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  array          data_array       The parameter is the data array.
 #  array          signal_array     The parameter is the signal array.
 #  integer        max_breaks       The parameter is the maximum number of breaks to 
 #                                  consider.
 #  integer        min_size         The parameter is the minimum number of observations 
 #                                  between two breaks.
 #  integer        jump             The parameter is the subsampling — only consider 
 #                                  every jump-th point as a candidate break. 
 #                                  Lower = more precise but slower
 #  float/none     penalty          The parameter is the penalty value for PELT algorithm. 
 #                                  Higher = fewer breaks detected
 #                                  None triggers auto-calibration
 #  integer/none   n_breaks         The parameter determines whether to use Binary 
 #                                  Segmentation to find exactly this many breaks.
 #                                  Overrides penalty when provided.
 #  integer        prec             The parameter is the output number precision.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def best_bai_perron_parms \
        (data_array:    np.ndarray,
         signal_array:  np.ndarray,
         max_breaks:    int,
         min_size:      int,
         jump:          int,
         penalty:       object,
         n_breaks:      object,
         prec:          int = 6) \
-> tuple[int, str, str, list]:

    best_n_int = len(data_array)

    most_brks_fnd_int = 0

    for model in bp_models_array:

        if n_breaks is not None:

            pen_used_flt = None

            algorithm    = 'binseg'


            algo \
                = rpt.Binseg \
                    (model = model, 
                     min_size = min_size, 
                     jump = jump) \
                        .fit(signal_array)

            raw_array \
                = algo.predict \
                    (n_bkps = n_breaks, 
                     pen = pen_used_flt, 
                     epsilon = None)

        else:

            if penalty is None: penalty = np.log(float(best_n_int)) * np.std(data_array)


            pen_used_flt = round(penalty, prec)

            algorithm    = 'pelt'


            algo \
                = rpt.Pelt \
                    (model = model, 
                     min_size = min_size, 
                     jump = jump) \
                        .fit(signal_array)

            raw_array    = algo.predict(pen = pen_used_flt)


        break_idxs_list = sorted([b for b in raw_array if b < best_n_int])[:max_breaks]

        if most_brks_fnd_int <= len(break_idxs_list):

            most_brks_fnd_int  = len(break_idxs_list)

            best_model         = model

            best_algorithm     = algorithm

            best_brk_idxs_list = copy.deepcopy(break_idxs_list)


    return \
        best_n_int, \
        best_model, \
        best_algorithm, \
        best_brk_idxs_list


# In[27]:


#*******************************************************************************************
 #
 #  Function Name:  best_bai_perron_series
 #
 #  Function Description:
 #      This function detects the maximum multiple structural breaks in a time series 
 #      using the Bai-Perron method via the ruptures library.
 #
 #      Two detection modes (mutually exclusive):
 #      - Penalty mode  (penalty != None) : PELT algorithm finds the optimal
 #        number of breaks automatically, penalising for complexity.
 #      - Fixed mode    (n_breaks != None): Binary segmentation finds exactly
 #        n_breaks breakpoints.
 #      - Default       (both None)       : Penalty mode with auto-calibrated
 #        penalty = log(n) * std(series).
 #
 #
 #  Return Type: integer, string, string, list, list, list
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  object         input_obj        The parameter is the input object.
 #  object         signal_obj       The parameter is the signal object.
 #  integer        max_breaks       The parameter is the maximum number of breaks to 
 #                                  consider.
 #  integer        min_size         The parameter is the minimum number of observations 
 #                                  between two breaks.
 #  integer        jump             The parameter is the subsampling — only consider 
 #                                  every jump-th point as a candidate break. 
 #                                  Lower = more precise but slower
 #  float/none     penalty          The parameter is the penalty value for PELT algorithm. 
 #                                  Higher = fewer breaks detected
 #                                  None triggers auto-calibration
 #  integer/none   n_breaks         The parameter determines whether to use Binary 
 #                                  Segmentation to find exactly this many breaks.
 #                                  Overrides penalty when provided.
 #  integer        prec             The parameter is the output number precision.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def best_bai_perron_series \
        (input_obj:  object, 
         signal_obj: object,
         max_breaks: int    = 5,
         min_size:   int    = 30, 
         jump:       int    = 5, 
         penalty:    object = None, 
         n_breaks:   object = None, 
         prec:       int    = 6) \
-> tuple[int, str, str, list, list, list]:

    data_array, data_bool     = dtypesx.check_data_dtype_array(input_obj)

    signal_array, signal_bool = dtypesx.check_data_dtype_array(signal_obj)

    if data_bool == False or signal_bool == False: return None, None, None, None, None, None


    best_n_int, \
    best_model, \
    best_algorithm, \
    best_brk_idxs_list \
        = best_bai_perron_parms \
            (data_array, 
             signal_array, 
             max_breaks, 
             min_size, 
             jump, 
             penalty, 
             n_breaks, 
             prec)                

    best_brk_pcts_list \
        = [round(float(b) / float(best_n_int) * 100.0, 1) for b in best_brk_idxs_list]

    seg_bnds_list = [0] + best_brk_idxs_list + [best_n_int]


    return \
        best_n_int, \
        best_model, \
        best_algorithm, \
        best_brk_idxs_list, \
        best_brk_pcts_list, \
        seg_bnds_list


# In[28]:


#*******************************************************************************************
 #
 #  Function Name:  build_coint_X
 #
 #  Function Description:
 #      This function builds cointegration data for processing from the x-axis values.
 #
 #
 #  Return Type: array
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  array          X                The parameter is the x-axis array.
 #  integer        n                The parameter is the size of the y-axis array.
 #  array          t                The parameter is the sequential y-axis index array.
 #  string         trend            The parameter is the cointegration trend.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def build_coint_X \
        (X:     np.ndarray,
         n:     int,
         t:     np.ndarray,
         trend: str) \
-> np.ndarray:

    cols = [X]

    if trend in ('c', 'ct', 'ctt'): cols.append(np.ones(n))

    if trend in ('ct', 'ctt'):      cols.append(t)

    if trend == 'ctt':              cols.append(t ** 2)

    return np.column_stack(cols)


# In[29]:


#*******************************************************************************************
 #
 #  Function Name:  build_coint_X
 #
 #  Function Description:
 #      This function calculates the BIC residual value.
 #
 #
 #  Return Type: float
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  array          residuals        The parameter is the residual values array.
 #  integer        k                The parameter is the x-array cointegration dimension.
 #  integer        n                The parameter is the size of the y-axis array.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def bic(residuals: np.ndarray, k: int, n: int) -> float:

    rss = np.sum(residuals ** 2)

    if rss <= 0: return np.inf

    else:        return n * np.log(rss / n) + k * np.log(n)


# In[30]:


#*******************************************************************************************
 #
 #  Function Name:  rtn_trend_desc
 #
 #  Function Description:
 #      This function returns the trend description from the trend.
 #
 #
 #  Return Type: string
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  string         trend            The parameter is the cointegration trend.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def rtn_trend_desc(trend: str) -> str:

    if   trend == 'c':   return 'constant trend'

    elif trend == 'ct':  return 'constant and linear trend'

    elif trend == 'ctt': return 'quadratic trend'

    elif trend == 'n':   return 'no trend'

    else:                return None


# In[31]:


#*******************************************************************************************
 #
 #  Function Name:  opt_eg_coint_result_dict
 #
 #  Function Description:
 #      This function calculates and returns the cointegration test results.
 #
 #
 #  Return Type: dataframe
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  series         y_series         The parameter is an array of time series values and
 #                                  the effect variable (must be stationary).
 #  series         X_series         The parameter is an array of time series values and
 #                                  the causal variable (must be stationary).
 #  integer        maxlag           The parameter is the maximum lag.
 #  string         trend            The parameter is the cointegration trend.
 #  string         autolag          The parameter is the method to use when automatically 
 #                                  determining the lag length.
 #  integer        prec             The parameter is the output number precision.
 #  float          alpha            The parameter is the p-value threshold.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def opt_eg_coint_result_dict \
        (y_array: np.ndarray,
         X_array: np.ndarray,
         maxlag:  object,
         trend:   str,
         autolag: str,
         prec:    int   = 6,
         alpha:   float = 0.05) \
-> np.ndarray:

    n_int             = len(y_array)

    t_array           = np.arange(n_int, dtype = float)


    X_coint           = build_coint_X(X_array, n_int, t_array, trend)


    ols_fit           = OLS(y_array, X_coint).fit()

    residuals_array   = ols_fit.resid


    k_coint_int       = X_coint.shape[1]

    bic_val_flt       = bic(residuals_array, k_coint_int, n_int)


    mean_tstat_flt, mean_pvalue_flt \
        = ttest_1samp(residuals_array, popmean = 0.0)


    X_trend_array     = add_constant(t_array)


    trend_fit         = OLS(residuals_array, X_trend_array).fit()

    trend_fstat_flt   = trend_fit.fvalue

    trend_fpval_flt   = trend_fit.f_pvalue


    passes_mean_bool  = round(mean_pvalue_flt, prec)  > round(alpha, prec)

    passes_trend_bool = round(trend_fpval_flt, prec)  > round(alpha, prec)

    passes_both_bool  = passes_mean_bool and passes_trend_bool


    raw \
        = coint \
            (y_array, 
             X_array, 
             trend   = trend, 
             autolag = autolag, 
             maxlag  = maxlag)


    coint_stat_flt    = raw[0]

    p_value_flt       = raw[1]

    cv_array          = raw[2]

    cv_5pct_flt       = cv_array[1]


    margin_flt        = coint_stat_flt - cv_5pct_flt

    is_coint_bool     = round(p_value_flt, prec) < round(alpha, prec)

    trend_desc        = rtn_trend_desc(trend)


    result_dict \
        = {'coint_stat':         float(round(coint_stat_flt,           prec)),
           'p_value':            float(round(p_value_flt,              prec)),
           '1%':                 float(round(cv_array[0],              prec)),
           '5%':                 float(round(cv_array[1],              prec)),
           '10%':                float(round(cv_array[2],              prec)),
           'margin':             float(round(margin_flt,               prec)),
           'trend':              str(trend),
           'trend_desc':         trend_desc,
           'autolag':            str(autolag),
           'resid_mean':         float(round(np.mean(residuals_array), prec)),
           'resid_mean_tstat':   float(round(mean_tstat_flt,           prec)),
           'resid_mean_pvalue':  float(round(mean_pvalue_flt,          prec)),
           'resid_trend_fstat':  float(round(trend_fstat_flt,          prec)),
           'resid_trend_pvalue': float(round(trend_fpval_flt,          prec)),
           'resid_bic':          float(round(bic_val_flt,              prec)),
           'passes_mean_test':   bool(passes_mean_bool),
           'passes_trend_test':  bool(passes_trend_bool),
           'passes_both':        bool(passes_both_bool),
           'cointegrated':       bool(is_coint_bool)}

    return result_dict


# In[32]:


#*******************************************************************************************
 #
 #  Function Name:  opt_eg_coint_series
 #
 #  Function Description:
 #      This function calculates the augmented Engle-Granger two-step cointegration test
 #      for two time series.
 #
 #
 #  Return Type: dataframe
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  object         y_obj            The parameter is the array holding the y values.
 #                                  the causal variable (must be stationary).
 #  object         X_obj            The parameter is the array holding the x values.
 #  integer        maxlag           The parameter is the maximum lag.
 #  integer        prec             The parameter is the output number precision.
 #  float          alpha            The parameter is the p-value threshold.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def opt_eg_coint_series \
        (y_obj:  object,
         X_obj:  object,
         maxlag: object = None,
         prec:   int    = 6, 
         alpha:  float  = 0.05) \
-> dict:

    y_array, y_bool = dtypesx.check_data_dtype_array(y_obj)

    X_array, X_bool = dtypesx.check_data_dtype_array(X_obj)

    if X_bool == False or y_bool == False: return None


    true_list  = []

    false_list = []


    for trend in eg_coint_trend_array:

        for autolag in adf_autolag_list:

            result_dict \
                = opt_eg_coint_result_dict \
                    (y_array  = y_array,
                     X_array  = X_array,
                     maxlag   = maxlag,
                     trend    = trend,
                     autolag  = autolag,
                     prec     = prec,
                     alpha    = alpha)

            if result_dict['cointegrated']: true_list.append(result_dict)

            else:                           false_list.append(result_dict)


    true_len_int = len(true_list)

    if   true_len_int == 0: results_dict = min(false_list, key = lambda r: r['p_value'])

    elif true_len_int == 1: results_dict = true_list[0]

    else:

        best_trend   = max(set(d['trend'] for d in true_list), \
                          key = lambda t: eg_coint_trend_list.index(t))

        results_dict = min((d for d in true_list if d['trend'] == best_trend),
                            key = lambda d: d['resid_bic'])

    return results_dict


# In[33]:


#*******************************************************************************************
 #
 #  Function Name:  validate_granger_lag_inputs
 #
 #  Function Description:
 #      This function validates inputs for optimal Granger lag selection and returns the
 #      aligned, dropna DataFrame used by all downstream functions.
 #
 #
 #  Return Type: dataframe
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  series         X_series         The parameter is an array of time series values and
 #                                  the causal variable (must be stationary).
 #  series         y_series         The parameter is an array of time series values and
 #                                  the effect variable (must be stationary).
 #  integer        minlag           The parameter is the minimum lag.
 #  integer        maxlag           The parameter is the maximum lag.
 #  string         method           The parameter is the lag selection method.
 #  integer        min_obs          The parameter is the minimum number of observations.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def validate_granger_lag_inputs \
        (X_series: pd.Series,
         y_series: pd.Series,
         minlag:   int,
         maxlag:   int,
         method:   str,
         min_obs:  int = 20) \
-> pd.DataFrame:

    if method not in granger_valid_methods_list:

        logx.print_and_log_text \
            ('\033[1m'
             +  f"Invalid method: '{method}'. Choose from {granger_valid_methods_list}"
             + '\033[0m')


    data_df    = pd.DataFrame({'x': X_series, 'y': y_series}).dropna()


    n_int      = len(data_df)

    if n_int < min_obs:

        logx.print_and_log_text \
            ('\033[1m'
             + f'Series too short for reliable lag selection ({n_int} observations).\n' \
             + f'Minimum recommended is {min_obs}.'
             + '\033[0m')


    maxlag_cap = min(maxlag, n_int // 5)

    if maxlag_cap < minlag:

        logx.print_and_log_text \
            ('\033[1m'
             + f'Effective maxlag ({maxlag_cap}) is less than minlag ({minlag}).\n'
             + 'Shorten minlag or supply a longer series.'
             + '\033[0m')


    return data_df


# In[34]:


#*******************************************************************************************
 #
 #  Function Name:  calc_granger_maxlag_cap
 #
 #  Function Description:
 #      This function returns the effective max lag after applying the n // 5 length-based 
 #      cap, which prevents over-parameterization on short series.
 #
 #
 #  Return Type: integer
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  integer        n                The parameter is the number of data points.
 #  integer        minlag           The parameter is the minimum lag.
 #  integer        maxlag           The parameter is the maximum lag.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def calc_granger_maxlag_cap \
        (n:      int, 
         minlag: int,
         maxlag: int) \
-> int:

    return max(minlag, min(maxlag, n // 5))


# In[35]:


#*******************************************************************************************
 #
 #  Function Name:  calc_granger_var_crit_lags
 #
 #  Function Description:
 #      This function fits a VAR model and returns the optimal lag selected by each of the
 #      four standard information criteria: AIC, BIC, HQIC, and FPE.
 #
 #
 #  Return Type: dictionary
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  dataframe      data_df          The parameter is the input dataframe.
 #  integer        minlag           The parameter is the minimum lag.
 #  integer        maxlag_cap       The parameter is the maximum lag cap.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def calc_granger_var_crit_lags \
        (data_df:    pd.DataFrame,
         minlag:     int,
         maxlag_cap: int) \
-> dict:

    var_selected = VAR(data_df).select_order(maxlags = maxlag_cap)

    orders       = var_selected.selected_orders

    return \
        {criterion: max(minlag, int(orders.get(criterion, 1))) \
         for criterion in ('aic', 'bic', 'hqic', 'fpe')}    


# In[36]:


#*******************************************************************************************
 #
 #  Function Name:  calc_granger_pacf_lag
 #
 #  Function Description:
 #      This function returns the last lag at which the PACF of the x-series (causal 
 #      variable) exceeds the 95% significance threshold (1.96 / sqrt(n)).
 #
 #
 #  Return Type: integer
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  dataframe      n                The parameter is the input dataframe.
 #  integer        minlag           The parameter is the minimum lag.
 #  integer        maxlag_cap       The parameter is the maximum lag cap.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def calc_granger_pacf_lag \
        (data_df:    pd.DataFrame,
         minlag:     int,
         maxlag_cap: int) \
-> int:

    n_int        = len(data_df)

    pacf_vals    = pacf(data_df['x'], nlags = maxlag_cap, method = 'ywm')

    sig_flt      = 1.96 / np.sqrt(n_int)


    sig_lags_list \
        = [lag for lag, val in enumerate(pacf_vals)
           if lag >= minlag and abs(val) > sig_flt]

    return max(sig_lags_list) if sig_lags_list else minlag


# In[37]:


#*******************************************************************************************
 #
 #  Function Name:  assemble_granger_criteria
 #
 #  Function Description:
 #      This function merges the VAR information criteria lags and the PACF lag into a 
 #      single flat dictionary used for reconciliation and reporting.
 #
 #
 #  Return Type: dictionary
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  dictionary     var_lags_dict    The parameter is the variable lags dictionary.
 #  integer        maxlag_cap      The parameter is the maximum lag cap.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def assemble_granger_criteria \
        (var_lags_dict: dict,
         pacf_lag:      int) \
-> dict:

    return {**var_lags_dict, 'pacf': pacf_lag}


# In[38]:


#*******************************************************************************************
 #
 #  Function Name:  reconcile_granger_criteria
 #
 #  Function Description:
 #      This function applies the chosen selection method to the full criteria dictionary 
 #      and returns both the method-specific lag and the consensus (median) lag.
 #
 #
 #  Return Type: integer
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  dictionary     all_crit_dict    The parameter is all granger criteria dictionary.
 #  integer        minlag           The parameter is the minimum lag.
 #  string         method           The parameter is the lag selection method.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def reconcile_granger_criteria \
        (all_crit_dict: dict,
         minlag:        int,
         method:        str) \
-> tuple[int, int]:

    val_list     = list(all_crit_dict.values())

    cons_lag_int = max(minlag, int(np.median(val_list)))

    method_map_dict \
        = {'consensus':    cons_lag_int,
           'aic':          all_crit_dict['aic'],
           'bic':          all_crit_dict['bic'],
           'hqic':         all_crit_dict['hqic'],
           'fpe':          all_crit_dict['fpe'],
           'pacf':         all_crit_dict['pacf'],
           'conservative': max(minlag, int(min(val_list))),
           'liberal':      max(minlag, int(max(val_list)))}

    return method_map_dict[method], cons_lag_int


# In[39]:


#*******************************************************************************************
 #
 #  Function Name:  build_granger_conclusion
 #
 #  Function Description:
 #      This function validates inputs for optimal Granger lag selection and returns the
 #      aligned, dropna DataFrame used by all downstream functions.
 #
 #
 #  Return Type: dataframe
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  integer        opt_lag          The parameter is the optimal lag.
 #  dictionary     all_crit_dict    The parameter is all granger criteria dictionary.
 #  integer        n                The parameter is the number of data points.
 #  integer        maxlag_cap       The parameter is the maximum lag cap.
 #  string         method           The parameter is the lag selection method.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def build_granger_conclusion \
        (opt_lag:       int,
         all_crit_dict: dict,
         n:             int,
         maxlag_cap:    int,
         method:        str) \
-> str:

    val_list   = list(all_crit_dict.values())

    spread_int = max(val_list) - min(val_list)


    if   len(set(val_list)) == 1: conf_str = 'all criteria agree'

    elif spread_int <= 2:         conf_str = 'criteria are in close agreement'

    elif spread_int <= 5:         conf_str = 'criteria show moderate disagreement'

    else:                         conf_str = 'criteria diverge substantially: interpret with caution'


    crit_str = ', '.join(f'{k.upper()}={v}' for k, v in all_crit_dict.items())

    out_str \
        = f'optimal lag ({method}): {opt_lag}. ' \
            + f'{conf_str} (range: {min(val_list)}–{max(val_list)}). ' \
            + f'{crit_str}.\n' \
            + f'series length: {n} observations; maxlag capped at {maxlag_cap}. '

    return out_str


# In[40]:


#*******************************************************************************************
 #
 #  Function Name:  build_granger_cv_splits
 #
 #  Function Description:
 #      This function produces walk-forward (expanding window) cross-validation splits 
 #      for a bivariate time series DataFrame. Each split yields a train fold that grows
 #      by one increment and a fixed-size test fold immediately following it.
 #
 #      Walk-forward CV is used rather than random k-fold because randomly shuffling time 
 #      series breaks temporal autocorrelation structure, which would corrupt both the VAR 
 #      lag selection and the Granger F-test.
 #
 #
 #  Return Type: list[tuple[dataframe, dataframe]]
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  dataframe      data_df          The parameter is the input dataframe.
 #  integer        n_splits         The parameter is the number of folds; minimum train 
 #                                  size is len(df) // (n_splits + 1).
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def build_granger_cv_splits \
        (data_df:  pd.DataFrame,
         n_splits: int) \
-> list[tuple[pd.DataFrame, pd.DataFrame]]:

    n_int         = len(data_df)

    fold_size_int = n_int // (n_splits + 1)


    splits_list    = []

    for i in range(1, n_splits + 1):

        train_end_int = fold_size_int * i

        test_end_int  = train_end_int + fold_size_int


        train_df      = data_df.iloc[:train_end_int]

        test_df       = data_df.iloc[train_end_int:test_end_int]


        if len(train_df) >= 20 and len(test_df) >= 5:

            splits_list.append((train_df, test_df))


    return splits_list


# In[41]:


#*******************************************************************************************
 #
 #  Function Name:  calc_granger_forecast_mse
 #
 #  Function Description:
 #      This function computes one-step-ahead rolling forecast MSE for both series by
 #      iteratively forecasting one step ahead using a sliding history window of length 
 #      equal to the selected lag.
 #
 #      This is used to assess whether the lag chosen by a given method produce a VAR 
 #      model that genuinely generalizes to held-out data, as opposed to merely fitting 
 #      the training window well.
 #
 #
 #  Return Type: float, float
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  varresults     var_fit          The parameter is the fitted VAR model on the train 
 #                                  fold.
 #  dataframe      train_df         The parameter is the training fold (provides forecast 
 #                                  history).
 #  dataframe      test_df          The parameter is the test fold (provides actuals)
 #  integer        lag              The parameter is the lag used to fit the VAR model.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def calc_granger_forecast_mse \
        (var_fit:  object,
         train_df: pd.DataFrame,
         test_df:  pd.DataFrame,
         lag:      int) \
-> tuple[float, float]:

    history_array = train_df.values[-lag:] if lag > 0 else train_df.values[-1:]

    pred_array    = var_fit.forecast(history_array, steps = len(test_df))

    actuals_array = test_df.values


    mse_x_flt = float(np.mean((pred_array[:, 0] - actuals_array[:, 0]) ** 2))

    mse_y_flt = float(np.mean((pred_array[:, 1] - actuals_array[:, 1]) ** 2))

    return mse_x_flt, mse_y_flt    


# In[42]:


#*******************************************************************************************
 #
 #  Function Name:  calc_granger_pvalue
 #
 #  Function Description:
 #      This function runs the Granger causality F-test on df at exactly the specified 
 #      lag (x→y direction) and returns the SSR-based F-test p-value.
 #
 #      A separate function is used rather than inlining the call because 
 #      grangercausalitytests requires careful column ordering (['y', 'x'] for the
 #      x→y direction) and returns a nested dict that is non-trivial to unpack.
 #
 #
 #  Return Type: float
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  dataframe      data_df          The parameter is the input dataframe.
 #  integer        lag              The parameter is the exact lag at which to run the 
 #                                  test.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def calc_granger_pvalue \
        (data_df: pd.DataFrame, 
         lag:     int) \
-> float:

    try:

        results_dict \
            = grangercausalitytests \
                (data_df[['y', 'x']], 
                 maxlag = lag, 
                 verbose = False)

        return float(results_dict[lag][0]['ssr_ftest'][1])

    except Exception: return 1.0


# In[43]:


#*******************************************************************************************
 #
 #  Function Name:  eval_granger_method_on_fold
 #
 #  Function Description:
 #      This function computes one-step-ahead rolling forecast MSE for both series by
 #      iteratively forecasting one step ahead using a sliding history window of length 
 #      equal to the selected lag.
 #
 #      This is used to assess whether the lag chosen by a given method produce a VAR 
 #      model that genuinely generalizes to held-out data, as opposed to merely fitting 
 #      the training window well.
 #
 #
 #  Return Type: dictionary
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  dataframe      train_df         The parameter is the training fold (provides forecast 
 #                                  history).
 #  dataframe      test_df          The parameter is the test fold (provides actuals)
 #  integer        minlag           The parameter is the minimum lag.
 #  integer        maxlag           The parameter is the maximum lag.
 #  string         method           The parameter is the lag selection method.
 #  integer        min_obs          The parameter is the minimum number of observations.
 #  integer        prec             The parameter is the output number precision.
 #  float          alpha            The parameter is the p-value threshold.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def eval_granger_method_on_fold \
        (train_df:   pd.DataFrame,
         test_df:    pd.DataFrame,
         minlag:     int,
         maxlag:     int,
         method:     str,
         min_obs:    int   = 20,
         prec:       int   = 6,
         alpha:      float = 0.05) \
-> dict:

    _, lag_result_dict \
            = find_optimal_granger_lag \
                (train_df['x'], train_df['y'],
                 minlag  = minlag,
                 maxlag  = maxlag,
                 method  = method,
                 min_obs = min_obs)


    lag_int     = lag_result_dict['optimal_lag']

    var_fit     = VAR(train_df).fit(lag_int)


    mse_x_flt, mse_y_flt \
        = calc_granger_forecast_mse \
            (var_fit, train_df, test_df, lag_int)

    p_value_flt = calc_granger_pvalue(train_df, lag_int)


    results_dict \
        = {'lag':         int(lag_int),
           'mse_x':       float(mse_x_flt),
           'mse_y':       float(mse_y_flt),
           'mse_mean':    float((mse_x_flt + mse_y_flt) / 2.0),
           'p_value':     float(p_value_flt),
           'significant': round(p_value_flt, prec) < round(alpha, prec)}

    return results_dict


# In[44]:


#*******************************************************************************************
 #
 #  Function Name:  aggregate_granger_fold_results
 #
 #  Function Description:
 #      This function aggregates per-fold evaluation metrics for a single method into 
 #      summary statistics used for method comparison.
 #
 #
 #  Return Type: dictionary
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  list           fold_results_list          
 #                                  The parameter is the list of fold results dictionaries.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def aggregate_granger_fold_results \
        (fold_results_list: list[dict]) \
-> dict:

    mse_vals_array  = [r['mse_mean']       for r in fold_results_list]

    p_vals_array    = [r['p_value']        for r in fold_results_list]

    lag_vals_array  = [r['lag']            for r in fold_results_list]

    sig_count_int   = sum(r['significant'] for r in fold_results_list)


    total_folds_int = len(fold_results_list)

    significance_rate_flt \
        = float(sig_count_int) / float(total_folds_int) if total_folds_int > 0 else 0.0


    results_dict \
        = {'mean_mse':          float(np.mean(mse_vals_array)),
           'std_mse':           float(np.std(mse_vals_array)),
           'mean_p_value':      float(np.mean(p_vals_array)),
           'significant_folds': int(sig_count_int),
           'total_folds':       int(total_folds_int),
           'significance_rate': significance_rate_flt,
           'mean_lag':          float(np.mean(lag_vals_array)),
           'std_lag':           float(np.std(lag_vals_array))}

    return results_dict


# In[45]:


#*******************************************************************************************
 #
 #  Function Name:  norm_granger_series
 #
 #  Function Description:
 #      This function normalizes a granger series.
 #
 #
 #  Return Type: series
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  series         data_series      The parameter is the granger series.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def norm_granger_series(data_series: pd.Series) -> pd.Series:

    rng = data_series.max() - data_series.min()

    out_series \
        = (data_series - data_series.min()) / rng \
           if rng > 0 else pd.Series(0.5, index = data_series.index)

    return out_series


# In[46]:


#*******************************************************************************************
 #
 #  Function Name:  score_granger_methods
 #
 #  Function Description:
 #      This function converts per-method aggregate statistics into a normalized composite
 #      score and returns a ranked DataFrame.
 #
 #      Scoring components (each normalized to [0, 1] across methods):
 #          - MSE score       : 1 - normalized(mean_mse)     — lower MSE is better
 #          - Stability score : 1 - normalized(std_mse)      — lower variance is better
 #          - P-value score   : 1 - normalized(mean_p_value) — lower p-value is better
 #          - Lag stability   : 1 - normalized(std_lag)      — consistent lag selection
 #                                                             across folds is better
 #
 #      The composite score is the unweighted mean of the four components. MSE and
 #      p-value are not combined into a single metric because they measure different 
 #      things: MSE reflects generalization quality, p-value reflects causal signal 
 #      strength. A method that scores well on both is more trustworthy than one that 
 #      excels on only one dimension.
 #
 #
 #  Return Type: dataframe
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  dictionary     aggr_dict        The parameter is a dictionary of aggregate granger 
 #                                  fold results.
 #  string         index            The parameter is the output dataframe index name.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def score_granger_methods \
        (aggr_dict: dict[str, dict],
         index:     str = 'method') \
-> pd.DataFrame:

    records_list = []

    for method, agg in aggr_dict.items():

        records_list.append({'method': method, **agg})


    scores_df    = pd.DataFrame(records_list).set_index(index)


    scores_df['mse_score']       = 1 - norm_granger_series(scores_df['mean_mse'])
    scores_df['stability_score'] = 1 - norm_granger_series(scores_df['std_mse'])
    scores_df['pval_score']      = 1 - norm_granger_series(scores_df['mean_p_value'])
    scores_df['lag_stab_score']  = 1 - norm_granger_series(scores_df['std_lag'])


    scores_df['composite_score'] \
        = scores_df[['mse_score', 'stability_score', 'pval_score', 'lag_stab_score']] \
            .mean(axis = 1)

    scores_df \
        = scores_df.sort_values('composite_score', ascending = False)

    return scores_df


# In[47]:


#*******************************************************************************************
 #
 #  Function Name:  build_optimal_granger_method_conclusion
 #
 #  Function Description:
 #      This function produces a plain-English summary of which method won, why, and how
 #      much it outperformed the runner-up.
 #
 #
 #  Return Type: string
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  dataframe      scores_df        The parameter is the granger scores dataframe
 #  dictionary     aggr_dict        The parameter is a dictionary of aggregate granger 
 #                                  fold results.
 #  string         best_method      The parameter is the name of the top-ranked method.
 #  integer        prec             The parameter is the output number precision.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def build_optimal_granger_method_conclusion \
        (scores_df:    pd.DataFrame,
         aggr_dict:    dict[str, dict],
         best_method:  str,
         prec:         int = 6) \
-> str:

    best_df    = scores_df.loc[best_method]

    runner_df  = scores_df.iloc[1]


    margin_flt = best_df['composite_score'] - runner_df['composite_score']

    agg_dict   = aggr_dict[best_method]


    if   margin_flt > 0.10: conf_str = 'clearly outperformed all alternatives'

    elif margin_flt > 0.04: conf_str = 'moderately outperformed the runner-up'

    else:                   conf_str = 'narrowly outperformed the runner-up: results are close'


    out_str \
        = f"Optimal method: '{best_method}' ({conf_str}).\n"                           + \
          f"Composite score: {best_df['composite_score']:.{prec}f}\n"                  + \
          f"(runner-up '{runner_df.name}': {runner_df['composite_score']:.{prec}f},\n" + \
          f'margin: {margin_flt:.{prec}f}).\n'                                         + \
          f"Mean forecast MSE: {agg_dict['mean_mse']:.{prec}f},\n"                     + \
          f"mean p-value: {agg_dict['mean_p_value']:.{prec}f},\n"                      + \
          f"significance rate: {agg_dict['significance_rate']:.0%},\n"                 + \
          f"mean lag selected: {agg_dict['mean_lag']:.{prec}f}\n"                      + \
          f"(std: {agg_dict['std_lag']:.{prec}f}).\n"

    return out_str


# In[48]:


#*******************************************************************************************
 #
 #  Function Name:  find_optimal_granger_lag
 #
 #  Function Description:
 #      This function calculates the optimal maximum lag for the Granger Causality Test 
 #      using multiple information criteria and ACF/PACF analysis, then reconciles them
 #      via a configurable selection method.
 #
 #
 #  Return Type: integer, dictionary
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  series         X_series         The parameter is an array of time series values and
 #                                  the causal variable (must be stationary).
 #  series         y_series         The parameter is an array of time series values and
 #                                  the effect variable (must be stationary).
 #  integer        minlag           The parameter is the minimum lag.
 #  string         maxlag           The parameter is the maximum lag to test.
 #  string         method           The parameter is the lag selection method.
 #  integer        min_obs          The parameter is the minimum number of observations.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def find_optimal_granger_lag \
        (X_series: pd.Series,
         y_series: pd.Series,
         minlag:   int    = 1,
         maxlag:   object = None,
         method:   str    = 'consensus',
         min_obs:  int    = 20) \
-> tuple[int, dict]:

    if maxlag is None: maxlag_int = int(12.0 * (float(len(X_series)) / 100.0)**(0.25))

    else:              maxlag_int = int(abs(maxlag))


    data_df \
        = validate_granger_lag_inputs \
            (X_series, y_series, minlag, maxlag_int, method, min_obs)


    n_int                  = len(data_df)


    maxlag_cap_int \
        = calc_granger_maxlag_cap \
            (n = n_int, 
             minlag        = minlag, 
             maxlag        = maxlag_int)

    var_lags_dict \
        = calc_granger_var_crit_lags \
            (data_df, 
             minlag        = minlag, 
             maxlag_cap    = maxlag_cap_int)

    pacf_lag_int \
        = calc_granger_pacf_lag \
            (data_df, 
             minlag        = minlag, 
             maxlag_cap    = maxlag_cap_int)

    all_crit_dict \
        = assemble_granger_criteria \
            (var_lags_dict = var_lags_dict, 
             pacf_lag      = pacf_lag_int)


    opt_lag_int, \
    consensus_lag_int \
        = reconcile_granger_criteria \
            (all_crit_dict = all_crit_dict, 
             minlag        = minlag, 
             method        = method)

    conclusion \
        = build_granger_conclusion \
            (opt_lag       = opt_lag_int, 
             all_crit_dict = all_crit_dict, 
             n             = n_int, 
             maxlag_cap    = maxlag_cap_int, 
             method        = method)


    rslt_dict \
        = {'optimal_lag':   int(opt_lag_int),
           'all_criteria':  all_crit_dict,
           'consensus_lag': int(consensus_lag_int),
           'method_used':   method,
           'series_length': int(n_int),
           'maxlag_cap':    int(maxlag_cap_int),
           'conclusion':    conclusion}

    return opt_lag_int, rslt_dict


# In[49]:


#*******************************************************************************************
 #
 #  Function Name:  find_optimal_granger_method
 #
 #  Function Description:
 #      This function empirically identifies the best lag-selection method for the Granger
 #      Causality Test by evaluating all methods via walk-forward cross-validation on the 
 #      actual series and ranking them on a composite score of forecast accuracy, stability, 
 #      and causal signal strength.
 #
 #
 #  Return Type: string, dictionary, dataframe
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  series         X_series         The parameter is an array of time series values and
 #                                  the causal variable (must be stationary).
 #  series         y_series         The parameter is an array of time series values and
 #                                  the effect variable (must be stationary).
 #  integer        minlag           The parameter is the minimum lag.
 #  object         maxlag           The parameter is the maximum lag to test, default 
 #                                  value of 12*(nobs/100)^{1/4} is used when None.
 #  integer        n_splits         The parameter is the number of walk-forward CV folds.
 #  integer        min_obs          The parameter is the minimum number of observations.
 #  string         method           The parameter is the information criterion method ('aic' 
 #                                  or 'bic').
 #  string         index            The parameter is the output dataframe index name for
 #                                  score_granger_methods. 
 #  integer        prec             The parameter is the output number precision.
 #  float          alpha            The parameter is the p-value threshold.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def find_optimal_granger_method \
        (X_series: pd.Series,
         y_series: pd.Series,
         minlag:   int    = 1,
         maxlag:   object = None,
         n_splits: int    = 5,
         min_obs:  int    = 20,
         method:   str    = 'bic',
         index:    str    = 'method',
         prec:     int    = 6,
         alpha:    float  = 0.05) \
-> tuple[str, dict, pd.DataFrame]:

    if maxlag is None: maxlag_int = int(12.0 * (float(len(X_series)) / 100.0)**(0.25))

    else: maxlag_int = int(abs(maxlag))


    data_df \
        = validate_granger_lag_inputs \
            (X_series, y_series, minlag, maxlag_int, method, min_obs)

    splits_list = build_granger_cv_splits(data_df, n_splits)


    aggr_dict   = {}

    for method in granger_valid_methods_list:

        fold_results_list \
            = [eval_granger_method_on_fold \
                   (train, 
                    test, 
                    minlag, 
                    maxlag_int, 
                    method, 
                    min_obs, 
                    prec, 
                    alpha) \
               for train, test in splits_list]

        aggr_dict[method] \
            = aggregate_granger_fold_results(fold_results_list)


    scores_df   = score_granger_methods(aggr_dict, index)


    best_method = scores_df.index[0]

    conclusion  = build_optimal_granger_method_conclusion(scores_df, aggr_dict, best_method, prec)


    results_dict \
        = {'optimal_method': best_method,
           'aggregates':     aggr_dict,
           'conclusion':     conclusion}

    return best_method, results_dict, scores_df


# In[50]:


#*******************************************************************************************
 #
 #  Function Name:  granger_causality_test
 #
 #  Function Description:
 #      This function tests Granger causality in both directions between X_series and 
 #      y_series. Both series must be stationary prior to calling this function.
 #
 #
 #  Return Type: dataframe, dictionary
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  series         X_series         The parameter is the x-values (causal) series (must 
 #                                  be stationary).
 #  series         y_series         The parameter is the y-values (effect) series (must 
 #                                  be stationary).
 #  integer        minlag           The parameter is the minimum lag.
 #  string         maxlag           The parameter is the maximum lag to test, default 
 #                                  value of 12*(nobs/100)^{1/4} is used when None.
 #  integer        maxlag_lmt       The parameter is the minimum number of observations.
 #  string         method           The parameter is the lag selection method.
 #  integer        min_obs          The parameter is the minimum number of observations.
 #  integer        prec             The parameter is the output number precision.
 #  float          alpha            The parameter is the p-value threshold.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def granger_causality_test \
        (X_series:   pd.Series,
         y_series:   pd.Series,
         minlag:     int    = 1,
         maxlag:     object = None,
         maxlag_lmt: int    = 60,
         method:     str    = 'consensus',
         min_obs:    int    = 20,
         prec:       int    = 6, 
         alpha:      float  = 0.05) \
-> tuple[pd.DataFrame, dict]:

    data_df = pd.DataFrame({'x': X_series, 'y': y_series}).dropna()

    data_df = data_df[['y', 'x']]


    if maxlag is None: 

        g_lag, _ \
            = find_optimal_granger_lag \
                (X_series, 
                 y_series, 
                 minlag  = minlag,
                 maxlag  = maxlag,
                 method  = method, 
                 min_obs = min_obs)

    else: g_lag = maxlag


    results_dict = grangercausalitytests(data_df, maxlag = g_lag, verbose = False)

    found_bool = False


    results_list = []

    for lag, rslt in results_dict.items():

        f_stat_flt         = rslt[0]['ssr_ftest'][0]

        f_p_val_flt        = rslt[0]['ssr_ftest'][1]


        chi2_stat_flt      = rslt[0]['ssr_chi2test'][0]

        chi2_p_val_flt     = rslt[0]['ssr_chi2test'][1]


        lrtest_stat_flt    = rslt[0]['lrtest'][0]

        lrtest_p_val_flt   = rslt[0]['lrtest'][1]


        params_f_stat_flt  = rslt[0]['params_ftest'][0]

        params_f_p_val_flt = rslt[0]['params_ftest'][1]


        f_sig_bool         = round(f_p_val_flt,        prec) < round(alpha, prec)

        chi2_sig_bool      = round(chi2_p_val_flt,     prec) < round(alpha, prec)

        lrtest_sig_bool    = round(lrtest_p_val_flt,   prec) < round(alpha, prec)

        params_f_sig_bool  = round(params_f_p_val_flt, prec) < round(alpha, prec)


        if (f_sig_bool and chi2_sig_bool \
                and lrtest_sig_bool and params_f_sig_bool) \
            or (not f_sig_bool and not chi2_sig_bool \
                and not lrtest_sig_bool and not params_f_sig_bool):

            conclusion   = 'high confidence'

        elif (lrtest_sig_bool != f_sig_bool and lrtest_sig_bool != chi2_sig_bool \
              and lrtest_sig_bool != params_f_sig_bool) \
                or (lrtest_sig_bool == chi2_sig_bool and f_sig_bool == params_f_sig_bool \
                    and lrtest_sig_bool == True):

            conclusion   = 'non-normal residuals or insufficient sample size'

        elif f_sig_bool != params_f_sig_bool:

            conclusion   = 'numerical precision issue'

        else: conclusion = 'inconclusive results'


        results_list.append \
            ({'lag':                  int(lag),
              'f_statistic':          float(round(f_stat_flt,         prec)),
              'chi2_statistic':       float(round(chi2_stat_flt,      prec)),
              'lrtest_statistic':     float(round(lrtest_stat_flt,    prec)),
              'params_f_statistic':   float(round(params_f_stat_flt,  prec)),
              'f_p_value':            float(round(f_p_val_flt,        prec)),
              'chi2_p_value':         float(round(chi2_p_val_flt,     prec)),
              'lrtest_p_value':       float(round(lrtest_p_val_flt,   prec)),
              'params_f_p_value':     float(round(params_f_p_val_flt, prec)),
              'f_significant':        bool(f_sig_bool),
              'chi2_significant':     bool(chi2_sig_bool),
              'lrtest_significant':   bool(lrtest_sig_bool),
              'params_f_significant': bool(params_f_sig_bool),
              'conclusion':           conclusion})


        if f_sig_bool and chi2_sig_bool and lrtest_sig_bool and params_f_sig_bool: 

            found_bool = True

            break


    if found_bool == True:

        results_df = pd.DataFrame(results_list).set_index('lag')

        best_dict  = results_df.iloc[-1].to_dict()

    else:

        if g_lag > maxlag_lmt:

            results_df   = pd.DataFrame(results_list).set_index('lag').iloc[:maxlag_lmt, :]

        else: results_df = pd.DataFrame(results_list).set_index('lag').iloc[:g_lag, :]


        best_df   = results_df[results_df['f_p_value'] == results_df['f_p_value'].min()]

        best_dict = best_df.iloc[0].to_dict()        


    display_df \
        = results_df \
            .drop \
                (columns \
                     = ['chi2_statistic', 
                        'lrtest_statistic', 
                        'params_f_statistic', 
                        'chi2_p_value', 
                        'lrtest_p_value', 
                        'params_f_p_value'])

    return display_df, best_dict


# In[51]:


#*******************************************************************************************
 #
 #  Function Name:  validate_var_vecm_inputs
 #
 #  Function Description:
 #      This function validates and aligns two time series into a bivariate DataFrame for
 #      use in VAR/VECM estimation.
 #
 #
 #  Return Type: dataframe
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  series         X_series         The parameter is an array of time series values and
 #                                  the causal variable.
 #  series         y_series         The parameter is an array of time series values and
 #                                  the effect variable.
 #  integer        maxlag           The parameter is the maximum lag to be used downstream; 
 #                                  validated against series length here to fail fast.
 #  integer        min_obs          The parameter is the minimum number of observations.
 #  boolean        vrb_bool         The parameter is the 
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def validate_var_vecm_inputs \
        (X_series: pd.Series,
         y_series: pd.Series,
         maxlag:   int,
         min_obs:  int  = 20,
         vrb_bool: bool = False) \
-> pd.DataFrame:

    data_df = pd.DataFrame({'x': X_series, 'y': y_series}).dropna()

    n_int  = len(data_df)

    if n_int < min_obs:

        if vrb_bool:

            logx.print_and_log_text \
                ('\033[1m'
                 + f'Series too short for VAR/VECM estimation ({n_int} observations). '
                 + f'Minimum required: {min_obs}.'
                 + '\033[0m')

    if maxlag >= n_int // 5:

        if vrb_bool:

            logx.print_and_log_text \
                ('\033[1m'
                 + f'maxlag ({maxlag}) is too large for series length ({n_int}).\n' \
                 + f'Use maxlag < {n_int // 5}'
                 + '\033[0m')

    return data_df


# In[52]:


#*******************************************************************************************
 #
 #  Function Name:  check_var_vecm_stationarity
 #
 #  Function Description:
 #      This function runs the Augmented Dickey-Fuller test on each series and returns
 #      a stationarity summary. This determines whether VAR (stationary) or VECM 
 #      (non-stationary but cointegrated) is the appropriate model.
 #
 #
 #  Return Type: dictionary
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  dataframe      data_df          The parameter is an aligned bivariate DataFrame with 
 #                                  columns ['x', 'y'].
 #  string         autolag          The parameter is the method to use when automatically 
 #                                  determining the lag length.
 #  integer        prec             The parameter is the output number precision.
 #  float          alpha            The parameter is the p-value threshold.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def check_var_vecm_stationarity \
        (data_df: pd.DataFrame,
         autolag: str   = 'AIC',
         prec:    int   = 6,
         alpha:   float = 0.05) \
-> dict:

    results_dict = {}

    for col in ('x', 'y'):

        adf_stat, p_value, _, _, _, _ \
            = adfuller \
                (data_df[col], 
                 autolag = autolag)


        stationary_bool = round(p_value, prec) < round(alpha, prec)

        conclusion \
            = (f"Series '{col}' is {'stationary' if stationary_bool else 'non-stationary'} "
               f"(ADF = {adf_stat:.{prec}f}, p = {p_value:.{prec}f}).")


        results_dict[col] \
            = {'adf_stat':   round(float(adf_stat), prec),
               'p_value':    round(float(p_value),  prec),
               'stationary': bool(stationary_bool),
               'conclusion': conclusion}


    return results_dict   


# In[53]:


#*******************************************************************************************
 #
 #  Function Name:  select_vecm_coint_rank
 #
 #  Function Description:
 #      This function uses Johansen's trace and maximum eigenvalue tests to determine
 #      the cointegration rank for VECM estimation.
 #
 #      For a bivariate system the rank can be 0 (no cointegration → use VAR
 #      on differences), 1 (one cointegrating relationship → use VECM), or 2
 #      (both series are stationary → use VAR on levels, though this case
 #      should have been caught by check_var_vecm_stationarity).
 #
 #
 #  Return Type: dictionary
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  dataframe      data_df          The parameter is an aligned bivariate DataFrame with 
 #                                  columns ['x', 'y'].
 #  string         maxlag           The parameter is the lag used for the cointegration 
 #                                  rank test.
 #  float          alpha            The parameter is the p-value threshold.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def select_vecm_coint_rank \
        (data_df: pd.DataFrame,
         maxlag:  int,
         alpha:   float = 0.05) \
-> dict:

    # use -1 for no deterministic terms, use 0 for intercept only, 1 for intercept + trend

    det_order_int = -1   

    trace_result \
        = select_coint_rank \
            (data_df, det_order_int, maxlag, method = 'trace',  signif = alpha)

    maxeig_result \
        = select_coint_rank \
            (data_df, det_order_int, maxlag, method = 'maxeig', signif = alpha)


    rank_int = int(trace_result.rank)


    if trace_result.rank == maxeig_result.rank: 

        agreement = 'Trace and max-eigenvalue tests agree'

    else:

        agreement \
            = (f'Trace rank = {trace_result.rank}, '
               f'max-eigenvalue rank={maxeig_result.rank} — using trace result')


    rank_intrprn \
        = {0: 'No cointegration detected — VAR on first differences is appropriate.',
           1: 'One cointegrating relationship detected — VECM is appropriate.',
           2: 'Both series appear stationary at levels — VAR on levels is appropriate.'} \
                .get(rank_int, f'Rank = {rank_int} — review manually.')


    results_dict \
        = {'rank':          int(rank_int),
           'trace_result':  trace_result,
           'maxeig_result': maxeig_result,
           'conclusion':    f'{agreement}. {rank_intrprn}'}

    return results_dict


# In[54]:


#*******************************************************************************************
 #
 #  Function Name:  select_var_lag_order
 #
 #  Function Description:
 #      This function selects the optimal VAR lag order using AIC, BIC, HQIC, and FPE
 #      information criteria, returning all four alongside the BIC-preferred lag as 
 #      the default recommendation for causal inference.
 #
 #
 #  Return Type: dictionary
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  dataframe      data_df          The parameter is an aligned bivariate DataFrame with 
 #                                  columns ['x', 'y'].
 #  string         maxlag          The parameter is the maximum lag to evaluate.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def select_var_lag_order \
        (data_df: pd.DataFrame,
         maxlag: int) \
-> dict:

    orders   = VAR(data_df).select_order(maxlags = maxlag).selected_orders


    aic_lag  = max(1, int(orders.get('aic',  1)))

    bic_lag  = max(1, int(orders.get('bic',  1)))

    hqic_lag = max(1, int(orders.get('hqic', 1)))

    fpe_lag  = max(1, int(orders.get('fpe',  1)))


    conclusion \
        = (f'Recommended lag (BIC): {bic_lag}.\n'
           f'AIC = {aic_lag}, BIC = {bic_lag}, HQIC = {hqic_lag}, FPE = {fpe_lag}.')


    results_dict \
        = {'recommended_lag': bic_lag,
           'aic_lag':         aic_lag,
           'bic_lag':         bic_lag,
           'hqic_lag':        hqic_lag,
           'fpe_lag':         fpe_lag,
           'conclusion':      conclusion}

    return results_dict


# In[55]:


#*******************************************************************************************
 #
 #  Function Name:  fit_var_model
 #
 #  Function Description:
 #      This function fits a Vector Autoregression (VAR) model at the specified lag order
 #      and extracts key diagnostic statistics.
 #
 #      VAR is appropriate when both series are stationary (either naturally
 #      or after differencing) and cointegration rank is 0.
 #
 #
 #  Return Type: dictionary
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  dataframe      data_df          The parameter is an aligned bivariate DataFrame with 
 #                                  columns ['x', 'y'].
 #  integer        lag              The parameter is the lag order for the VAR model.
 #  integer        prec             The parameter is the output number precision.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def fit_var_model \
        (data_df: pd.DataFrame,
         lag:     int,
         prec:    int = 6) \
-> dict:

    model    = VAR(data_df).fit(lag)

    roots    = [abs(r) for r in model.roots]

    stable   = all(r < 1.0 for r in roots)


    params_x = model.params['x']

    params_y = model.params['y']


    summary_df \
        = pd.DataFrame \
            ({'coef_x_equation': params_x,
              'coef_y_equation': params_y})


    stability \
        = 'STABLE — all roots inside unit circle' \
            if stable else 'UNSTABLE — roots outside unit circle; interpret with caution'

    conclusion \
        = (f'VAR({lag}) fitted.\n'
           f'AIC = {model.aic:.{prec}f}, BIC = {model.bic:.{prec}f}.\n'
           f'Stability: {stability}.')


    results_dict \
        = {'model':      model,
           'lag':        lag,
           'aic':        round(float(model.aic), prec),
           'bic':        round(float(model.bic), prec),
           'roots':      roots,
           'is_stable':  stable,
           'summary_df': summary_df,
           'conclusion': conclusion}

    return results_dict


# In[56]:


#*******************************************************************************************
 #
 #  Function Name:  calc_vecm_half_life
 #
 #  Function Description:
 #      This function calculates the error correction half-life from an adjustment speed
 #      coefficient (alpha).
 #
 #      The half-life is the number of periods required for half of a deviation from the 
 #      long-run equilibrium to be corrected. A shorter half-lifeindicates faster mean 
 #      reversion.
 #
 #      For COVID/equity data: a half-life of 5 days suggests the market corrects half of 
 #      any COVID-driven disequilibrium within one trading week.
 #
 #
 #  Return Type: float
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  float          alpha            The parameter is the speed-of-adjustment coefficient 
 #                                  and should be negative for a mean-reverting series. 
 #                                  If the value is positive or zero, the function returns 
 #                                  inf (no mean reversion).
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def calc_vecm_half_life(alpha: float) -> float:

    if alpha >= 0 or alpha <= -1: return float('inf')

    else: return float(-np.log(2) / np.log(1 + alpha))


# In[57]:


#*******************************************************************************************
 #
 #  Function Name:  fit_vecm_model
 #
 #  Function Description:
 #      This function fits a Vector Error Correction Model (VECM) at the specified lag 
 #      and cointegration rank, and extracts the cointegrating vector, adjustment
 #      coefficients (alpha), and model diagnostics.
 #
 #      VECM is appropriate when both series are non-stationary (I(1)) but share a long-run 
 #      equilibrium relationship (cointegration rank >= 1). The VECM decomposes each series' 
 #      movement into a long-run error correction term and short-run VAR dynamics.
 #
 #
 #  Return Type: dictionary
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  dataframe      data_df          The parameter is the levels (non-differenced) bivariate 
 #                                  dataframe.
 #  integer        lag              The parameter is the number of lagged difference terms 
 #                                  (VECM lag = VAR lag - 1; the conversion is handled 
 #                                  internally).
 #  integer        rank             The parameter is the cointegration rank.
 #  integer        prec             The parameter is the output number precision.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def fit_vecm_model \
        (data_df: pd.DataFrame,
         lag:     int,
         rank:    int,
         prec:    int = 6) \
-> dict:

    vecm_lag_int   = max(1, lag - 1)

    rank           = min(rank, 1)

    model \
        = VECM \
            (data_df, 
             k_ar_diff     = vecm_lag_int, 
             coint_rank    = rank, 
             deterministic = 'n') \
                .fit()

    alpha_series \
        = pd.Series(model.alpha.flatten(), index=['x', 'y'], name = 'alpha')


    beta_raw       = model.beta

    beta_df \
        = pd.DataFrame \
            (beta_raw,
             index   = ['x', 'y'],
             columns = [f'coint_vec_{i + 1}' for i in range(beta_raw.shape[1])])


    dominant_alpha_flt \
        = float(alpha_series[abs(alpha_series) == abs(alpha_series).max()].iloc[0])

    half_life_flt \
        = calc_vecm_half_life(dominant_alpha_flt)


    b_series       = beta_df.iloc[:, 0]


    b0_flt         = float(b_series.iloc[0])

    b1_flt         = float(b_series.iloc[1])


    if abs(b0_flt) > 1e-10:

        b1_norm_flt = b1_flt / b0_flt

        long_run_eq = f'x - ({-b1_norm_flt:.{prec}f}) * y = 0  (long-run equilibrium)'

    else: long_run_eq = f'beta = {b_series.values}  (non-standard normalization)'


    is_stable_bool  = not all(a >= 0 for a in alpha_series.values)


    mean_reversion \
        = 'CONFIRMED' if is_stable_bool else 'NOT CONFIRMED — check alpha signs'

    conclusion \
        = ( f'VECM(lag = {vecm_lag_int}, rank = {rank}) fitted. '
            f"Adjustment speeds — x: {alpha_series['x']:.{prec}f}, y: {alpha_series['y']:.{prec}f}. "
            f'Error correction half-life: {half_life_flt:.{prec}f} periods. '
            f'{long_run_eq}. '
            f'Mean reversion: {mean_reversion}.')


    results_dict \
        = {'model':       model,
           'lag':         vecm_lag_int,
           'rank':        rank,
           'alpha':       alpha_series,
           'beta':        beta_df,
           'half_life':   half_life_flt,
           'long_run_eq': long_run_eq,
           'is_stable':   is_stable_bool,
           'conclusion':  conclusion}

    return results_dict


# In[58]:


#*******************************************************************************************
 #
 #  Function Name:  calc_var_vecm_irf
 #
 #  Function Description:
 #      This function computes Impulse Response Functions (IRFs) for a fitted VAR or VECM
 #      model. IRFs show how a one-standard-deviation shock to one series propagates through 
 #      both series over time.
 #
 #      For your COVID/equity analysis, the x→y IRF answers: if COVID cases spike by one 
 #      standard deviation today, how does the stock index respond over the next N trading 
 #      days?
 #
 #
 #  Return Type: dictionary
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  dictionary     model_result_dict
 #                                  The parameter is the model result dictionary.
 #  string         model_type       The parameter is the model type ('var' or 'vecm').
 #  integer        periods          The parameter is the forecast horizon for IRF.
 #  integer        prec             The parameter is the output number precision.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def calc_var_vecm_irf \
        (model_result_dict: dict,
         model_type:        str,
         periods:           int = 30,
         prec:              int = 6) \
-> dict:

    fitted           = model_result_dict['model']

    irf              = fitted.irf(periods)

    irf_vals_array   = irf.irfs


    irf_df \
        = pd.DataFrame \
            ({'x_shock_x_response': irf_vals_array[:, 0, 0],
              'x_shock_y_response': irf_vals_array[:, 1, 0],
              'y_shock_x_response': irf_vals_array[:, 0, 1],
              'y_shock_y_response': irf_vals_array[:, 1, 1]})

    irf_df.index.name = 'period'


    x_to_y_array     = irf_df['x_shock_y_response']

    peak_idx_int     = int(abs(x_to_y_array).idxmax())

    peak_val_flt     = float(x_to_y_array.iloc[peak_idx_int])


    net_effect_flt   = float(x_to_y_array.sum())


    if   net_effect_flt > 0.01:  sign = 'positive'

    elif net_effect_flt < -0.01: sign = 'negative'

    else:                        sign = 'mixed'


    conclusion \
        = (f'IRF ({model_type.upper()}, {periods} periods):\n'
           f'A one-SD shock to x produces a {sign} net response in y.\n'
           f'Peak x→y effect at lag {peak_idx_int} '
           f'(magnitude: {peak_val_flt:.{prec}f}).\n'
           f'Cumulative x→y response: {net_effect_flt:.{prec}f}.')


    results_dict \
        = {'irf_obj':     irf,
           'irf_df':      irf_df,
           'peak_effect': {'lag':       peak_idx_int, 
                           'magnitude': round(peak_val_flt, prec)},
           'sign':         sign,
           'conclusion':   conclusion}

    return results_dict


# In[59]:


#*******************************************************************************************
 #
 #  Function Name:  calc_var_vecm_fevd
 #
 #  Function Description:
 #      This function computes the Forecast Error Variance Decomposition (FEVD) for a 
 #      fitted VAR or VECM model. FEVD quantifies what fraction of the forecast error
 #      variance of each series is attributable to shocks from each series.
 #
 #      For your analysis: the FEVD answers what percentage of the stock index's
 #      forecast uncertainty is explained by COVID case shocks vs. the index's
 #      own history.
 #
 #
 #  Return Type: dictionary
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  dictionary     model_result_dict
 #                                  The parameter is the model result dictionary.
 #  string         model_type       The parameter is the model type ('var' or 'vecm').
 #  integer        periods          The parameter is the forecast horizon for IRF.
 #  integer        prec             The parameter is the output number precision.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def calc_var_vecm_fevd \
        (model_result_dict: dict,
         model_type:        str,
         periods:           int = 30,
         prec:              int = 6) \
-> dict:

    if model_type == 'vecm':

        vecm_model   = model_result_dict['model']

        var_data     = pd.DataFrame(vecm_model.model.endog, columns = ['x', 'y'])

        var_lag      = vecm_model.k_ar

        fitted       = VAR(var_data).fit(var_lag)

    else: fitted = model_result_dict['model']


    fevd             = fitted.fevd(periods)

    decomp           = fevd.decomp


    fevd_df \
        = pd.DataFrame \
            ({'period':             range(periods),
              'y_variance_from_x':  decomp[1, :, 0],
              'y_variance_from_y':  decomp[1, :, 1],
              'x_variance_from_x':  decomp[0, :, 0],
              'x_variance_from_y':  decomp[0, :, 1]}) \
                .set_index('period')


    x_share_in_y_flt = float(decomp[1, -1, 0])

    y_own_share_flt  = float(decomp[1, -1, 1])


    if   x_share_in_y_flt > 0.20: influence = 'substantial'

    elif x_share_in_y_flt > 0.05: influence = 'moderate'

    else:                         influence = 'minimal'


    conclusion \
        = (f'FEVD ({model_type.upper()}, horizon = {periods}):\n'
           f"x shocks explain {x_share_in_y_flt:.{prec}%} of y's forecast variance "
           f'({influence} influence).\n'
           f"y's own shocks explain {y_own_share_flt:.{prec}%} of its own variance.")


    results_dict \
        = {'fevd_obj':     fevd,
           'fevd_df':      fevd_df,
           'x_share_in_y': round(x_share_in_y_flt, prec),
           'y_own_share':  round(y_own_share_flt,  prec),
           'conclusion':   conclusion}

    return results_dict


# In[60]:


#*******************************************************************************************
 #
 #  Function Name:  build_var_vecm_summary_df
 #
 #  Function Description:
 #      This function assembles a single-row summary DataFrame from all pipeline stage 
 #      outputs, suitable for inclusion in a notebook summary table alongside other
 #      pairwise results.ty is explained by COVID case shocks vs. the index's own history.
 #
 #
 #  Return Type: dataframe
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  dictionary     stationarity_dict
 #                                  The parameter is the var/vecm stationarity dictionary.
 #  dictionary     coint_dict       The parameter is the vecm cointegration rank 
 #                                  dictionary.
 #  dictionary     lag_order_dict   The parameter is the var lag order dictionary.
 #  dictionary     model_result_dict   
 #                                  The parameter is the var/vecm fit model dictionary.
 #  dictionary     irf_result_dict  The parameter is the var/vecm impulse response 
 #                                  functions dictionary.
 #  dictionary     fevd_result_dict The parameter is the forecast error variance 
 #                                  decomposition dictionary.
 #  string         model_type       The parameter is the model type ('var' or 'vecm').
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def build_var_vecm_summary_df \
        (stationarity_dict: dict,
         coint_dict:        dict,
         lag_order_dict:    dict,
         model_result_dict: dict,
         irf_result_dict:   dict,
         fevd_result_dict:  dict,
         model_type:        str) \
-> pd.DataFrame:

    half_life \
        = (model_result_dict.get('half_life', float('nan'))
           if model_type == 'vecm' else float('nan'))

    results_df \
        = pd.DataFrame \
            ([{'model_type':        model_type.upper(),
               'x_stationary':      stationarity_dict['x']['stationary'],
               'y_stationary':      stationarity_dict['y']['stationary'],
               'coint_rank':        coint_dict['rank'],
               'lag':               model_result_dict['lag'],
               'is_stable':         model_result_dict['is_stable'],
               'aic':               model_result_dict.get('aic', float('nan')),
               'bic':               model_result_dict.get('bic', float('nan')),
               'irf_peak_lag':      irf_result_dict['peak_effect']['lag'],
               'irf_peak_mag':      irf_result_dict['peak_effect']['magnitude'],
               'irf_sign':          irf_result_dict['sign'],
               'fevd_x_share_in_y': fevd_result_dict['x_share_in_y'],
               'fevd_y_own_share':  fevd_result_dict['y_own_share'],
               'half_life':         half_life}])

    return results_df


# In[61]:


#*******************************************************************************************
 #
 #  Function Name:  fit_var_or_vecm
 #
 #  Function Description:
 #      This function is thefull VAR/VECM pipeline for two time series and automatically 
 #      determines whether VAR or VECM is appropriate based on stationarity and
 #      cointegration tests, fits the correct model, and computes IRFs and FEVD.
 #
 #      Decision logic:
 #          Both stationary            → VAR on levels
 #          Both non-stationary,
 #            cointegration rank >= 1  → VECM on levels
 #          Both non-stationary,
 #            cointegration rank == 0  → VAR on first differences
 #
 #
 #  Return Type: dict
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  series         X_series         The parameter is an array of time series values and
 #                                  the causal variable.
 #  series         y_series         The parameter is an array of time series values and
 #                                  the effect variable.
 #  integer        maxlag           The parameter is the maximum lag to evaluate.
 #  integer        min_obs          The parameter is the minimum number of observations.
 #  string         autolag          The parameter is the method to use when automatically 
 #                                  determining the lag length.
 #  integer        periods          The parameter is the forecast horizon for IRF.
 #  boolean        vrb_bool         The parameter is the indicator of verbosity.
 #  integer        prec             The parameter is the output number precision.
 #  float          alpha            The parameter is the p-value threshold.
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def fit_var_or_vecm \
        (X_series: pd.Series,
         y_series: pd.Series,
         maxlag:   object = None,
         min_obs:  int    = 20,
         autolag:  str    = 'AIC',
         periods:  int    = 30,
         vrb_bool: bool   = False,
         prec:     int    = 6,
         alpha:    float  = 0.05) \
-> dict:

    if maxlag is None: maxlag_int = int(12.0 * (float(len(X_series)) / 100.0)**(0.25))

    else:              maxlag_int = int(abs(maxlag))


    data_df             = validate_var_vecm_inputs(X_series, y_series, maxlag_int, min_obs, vrb_bool)

    n_int               = len(data_df)


    effective_maxlag    = min(maxlag_int, n_int // 8 if n_int < 150 else n_int // 5)

    effective_maxlag    = max(1, effective_maxlag)


    stationarity_dict \
        = check_var_vecm_stationarity \
            (data_df, 
             autolag = autolag, 
             prec    = prec, 
             alpha   = alpha)


    coint_dict = select_vecm_coint_rank(data_df, effective_maxlag, alpha)

    lag_order_dict      = select_var_lag_order(data_df, effective_maxlag)

    lag_int             = lag_order_dict['recommended_lag']


    cointegrated_bool   = coint_dict['rank'] >= 1

    both_stationary_bool \
        = stationarity_dict['x']['stationary'] and stationarity_dict['y']['stationary']


    if both_stationary_bool:

        model_type      = 'var'

        data_for_fit_df = data_df

    elif cointegrated_bool:

        model_type      = 'vecm'

        data_for_fit_df = data_df

    else:

        model_type      = 'var'

        data_for_fit_df = data_df.diff().dropna()


    if model_type == 'var':

        model_result_dict = fit_var_model(data_for_fit_df, lag_int, prec)

    else: 

        model_result_dict \
            = fit_vecm_model \
                (data_for_fit_df, 
                 lag_int, 
                 coint_dict['rank'], 
                 prec = prec)


    irf_result_dict \
        = calc_var_vecm_irf \
            (model_result_dict, 
             model_type, 
             periods = periods, 
             prec    = prec)

    fevd_result_dict \
        = calc_var_vecm_fevd \
            (model_result_dict, 
             model_type, 
             periods = periods + 1, 
             prec    = prec)


    summary_df \
        = build_var_vecm_summary_df \
            (stationarity_dict,
             coint_dict,
             lag_order_dict,
             model_result_dict,
             irf_result_dict,
             fevd_result_dict,
             model_type)


    conclusion \
        = (f'{X_series.name.upper()} VS. {y_series.name.upper()} ANALYSIS\n\n'
           f'Model selected: {model_type.upper()}.\n\n'
           f"{stationarity_dict['x']['conclusion']}\n\n"
           f"{stationarity_dict['y']['conclusion']}\n\n"
           f"{coint_dict['conclusion']}\n\n"
           f"{lag_order_dict['conclusion']}\n\n"
           f"{model_result_dict['conclusion']}\n\n"
           f"{irf_result_dict['conclusion']}\n\n"
           f"{fevd_result_dict['conclusion']}\n")


    results_dict \
        = {'model_type':   model_type,
           'stationarity': stationarity_dict,
           'coint':        coint_dict,
           'lag_order':    lag_order_dict,
           'model_result': model_result_dict,
           'irf_result':   irf_result_dict,
           'fevd_result':  fevd_result_dict,
           'summary_df':   summary_df,
           'conclusion':   conclusion}

    return results_dict


# In[62]:


#*******************************************************************************************
 #
 #  Function Name:  opt_poly_deg_parms
 #
 #  Function Description:
 #      This function calculates several parameters for finding the optimal polynomial 
 #      degree for detrending a time series.
 #
 #
 #  Return Type: array, float, float
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  array          data_array       The parameter is an array of time series values.
 #  array          t_array          The parameter is an array of sequential index values 
 #                                  for the time series.
 #  integer        degree           The parameter is the polynomial degree.
 #  integer        n                The parameter is the number of data points in the 
 #                                  time series.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def opt_poly_deg_parms \
        (data_array: np.ndarray,
         t_array:    np.ndarray,
         degree:     int,
         n:          int) \
-> tuple[np.ndarray, float, float]:

    coeffs_array    = np.polyfit(t_array, data_array, degree)

    fitted_flt      = np.polyval(coeffs_array, t_array)

    residuals_array = data_array - fitted_flt


    sse_flt         = np.sum(residuals_array ** 2)

    sigma2_flt      = sse_flt / float(n)


    log_l_flt \
        = float(-n) / 2.0 * np.log(2.0 * np.pi * sigma2_flt) - sse_flt / (2.0 * sigma2_flt)


    k_int           = degree + 2

    aic_flt         = 2.0 * float(k_int) - 2.0 * log_l_flt

    bic_flt         = float(k_int) * np.log(float(n)) - 2.0 * log_l_flt


    return residuals_array, aic_flt, bic_flt


# In[63]:


#*******************************************************************************************
 #
 #  Function Name:  opt_poly_deg_rslt_dict
 #
 #  Function Description:
 #      This function calculates and returns te results list for finding the optinal 
 #      polynomial degree for detrending a time series.
 #
 #
 #  Return Type: list
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  array          data_array       The parameter is an array of time series values.
 #  integer        max_degree       The parameter is the highest polynomial degree to try.
 #  string/integer nlags            The parameter indicates the number of lags.
 #  integer/none   maxlag           The parameter is the maximum lag which is included 
 #                                  in test, default value of 12*(nobs/100)^{1/4} is used 
 #                                  when None.      
 #  integer        prec             The parameter is the output number precision.
 #  float          alpha            The parameter is the p-value threshold.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def opt_poly_deg_rslt_dict \
        (data_array: np.ndarray,
         max_degree: int,
         nlags:      object,
         maxlag:     int,
         prec:       int   = 6,
         alpha:      float = 0.05) \
-> list:

    n_int         = len(data_array)

    t_array       = np.arange(n_int, dtype = float)


    results_list = []

    for degree in range(1, max_degree + 1):

        residuals_array, aic_flt, bic_flt \
            = opt_poly_deg_parms(data_array, t_array, degree, n_int)

        adf_result_dict \
            = opt_adf_stnry_series \
                (residuals_array,
                 index = 'series',
                 maxlag = maxlag,
                 prec = prec,
                 alpha = alpha)

        kpss_result_dict \
            = opt_kpss_stnry_series \
                (residuals_array,
                 index = 'series',
                 prec = prec,
                 alpha = alpha)

        stnry_bool = adf_result_dict['stationary'] and kpss_result_dict['stationary']

        results_list.append \
            ({'degree':     int(degree),
              'aic':        float(round(aic_flt, prec)),
              'bic':        float(round(bic_flt, prec)),
              'stationary': bool(stnry_bool)})


    return results_list


# In[64]:


#*******************************************************************************************
 #
 #  Function Name:  find_opt_poly_degree
 #
 #  Function Description:
 #      This function finds the optimal polynomial degree for detrending a time series
 #      by fitting degrees 1..max_degree and scoring each via AIC/BIC, then confirming 
 #      stationarity of the residuals with ADF + KPSS.
 #
 #
 #  Return Type: integer
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  object         input_obj        The parameter is the input object.
 #  integer        max_degree       The parameter is the highest polynomial degree to try.
 #  string         criterion        The parameter is the model selection criteria ('aic' 
 #                                  or 'bic').
 #  string/integer nlags            The parameter indicates the number of lags.
 #  integer/none   maxlag           The parameter is the maximum lag which is included 
 #                                  in test, default value of 12*(nobs/100)^{1/4} is used 
 #                                  when None.
 #  integer        prec             The parameter is the output number precision.
 #  float          alpha            The parameter is the p-value threshold.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def find_opt_poly_degree \
        (input_obj:    object,
         max_degree:   int    = 10,
         criterion:    str    = 'bic',
         nlags:        object = 'auto',
         maxlag:       object = None,
         prec:         int    = 6,
         alpha:        float  = 0.05) \
-> int:

    data_array, data_bool = dtypesx.check_data_dtype_array(input_obj)

    if data_bool == False: return data_array


    if maxlag is None: maxlag_int = int(12.0 * (float(len(data_array)) / 100.0)**(0.25))

    else:              maxlag_int = int(abs(maxlag))


    results_list \
        = opt_poly_deg_rslt_dict \
            (data_array, max_degree, nlags, maxlag_int, prec, alpha)


    stnry_results_list = [r for r in results_list if r['stationary']]

    candidates_list \
        = stnry_results_list if stnry_results_list else results_list


    criterion       = dtypesx.strip_rmv_nmbr_space_case(criterion, 'lower')

    if criterion == 'aic' or criterion == 'bic':

        best_dict   = min(candidates_list, key = lambda r: r[criterion])

    else: best_dict = min(candidates_list, key = lambda r: r['bic'])


    return best_dict['degree']


# In[65]:


#*******************************************************************************************
 #
 #  Function Name:  hp_smooth_matrix
 #
 #  Function Description:
 #      This function constructs the HP filter smoother matrix H such that trend = H @ y.
 #
 #      The smoother matrix is derived from the closed-form solution to the HP minimisation 
 #      problem. Given the second-difference matrix D, the trend satisfies:
 #
 #      trend = (I + lambda * D'D)^{-1} y  =  H(lambda) @ y
 # 
 #      The trace of H gives the effective degrees of freedom consumed by the trend component, 
 #      used for AIC/BIC penalisation.
 #
 #  Return Type: array (n x n)
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  float          hp_lambda        The parameter is the HP smoothing parameter (lambda).
 #  integer        n                The parameter is the number of data points in the 
 #                                  time series.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def hp_smooth_matrix \
        (hp_lambda: float,
         n:         int) \
-> np.ndarray:

    e_array = np.ones(n)


    D_array = np.diag(e_array) - 2 * np.diag(e_array[:-1], -1) + np.diag(e_array[:-2], -2)

    D_array = D_array[2:, :]


    I_array = np.eye(n)

    H_array = np.linalg.solve(I_array + hp_lambda * D_array.T @ D_array, I_array)


    return H_array


# In[66]:


#*******************************************************************************************
 #
 #  Function Name:  hp_info_crit
 #
 #  Function Description:
 #      This function computes an information criterion for a given log-lambda on 
 #      series y.
 #
 #      The function evaluates the HP filter at exp(log_lambda), then scores the residual 
 #      (cycle) component using the chosen criterion. The search is conducted in log-space 
 #      so that minimization explores small and large lambda values with equal resolution.
 #
 #  Return Type: float
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  float          log_lambda       The parameter is the natural log of the HP lambda 
 #                                  parameter.
 #  array          y                The parameter is the time series, as a 1-D float array.
 #  string         criterion        The parameter is one of the following statistical 
 #                                  methods: 'aic', 'bic', or 'mse'.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def hp_info_crit \
        (log_lambda: float, 
         y:          np.ndarray,
         criterion:  str) \
-> float:

    lambda_flt     = np.exp(log_lambda)

    cycle_array, _ = hpfilter(y, lamb = lambda_flt)

    n_int          = len(y)


    sse_flt        = np.sum(cycle_array ** 2)

    sigma2_flt     = sse_flt / float(n_int)


    if criterion == 'mse': return sigma2_flt

    if sigma2_flt <= 0: return np.inf


    H_array        = hp_smooth_matrix(lambda_flt, n_int)

    edf_flt        = np.trace(H_array)


    log_lik_flt \
        = float(-n_int) / 2.0 * np.log(2.0 * np.pi * sigma2_flt) - sse_flt / (2.0 * sigma2_flt)


    criterion           = dtypesx.strip_rmv_nmbr_space_case(criterion, 'lower')

    if criterion == 'aic': 

        info_crit_flt   = -2.0 * log_lik_flt + 2 * edf_flt

    else: info_crit_flt = -2.0 * log_lik_flt + np.log(float(n_int)) * edf_flt


    return info_crit_flt


# In[67]:


#*******************************************************************************************
 #
 #  Function Name:  find_opt_hp_lambda
 #
 #  Function Description:
 #      This function finds the optimal lambda for the Hodrick-Prescott filter by
 #      minimizing an information criterion over the HP smoothing parameter lambda. 
 #      The method treats the HP filter as a linear smoother to compute effective 
 #      degrees of freedom via the trace of the smoother matrix. The scalar search 
 #      is then performed in log-space over lambda_bounds.
 #
 #  Return Type: float
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  object         input_obj        The parameter is the input object.
 #  array          lambda_tuple     The parameter is the bounds for the lambda search.
 #  string         criterion        The parameter is one of the following statistical 
 #                                  methods: 'aic', 'bic', or 'mse'.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def find_opt_hp_lambda \
        (input_obj:    object,
         lambda_tuple: tuple = (1, 1e9),
         criterion:    str   = 'bic') \
-> float:

    y_array, y_bool = dtypesx.check_data_dtype_array(input_obj)

    if y_bool == False: return y_array


    log_bnds_tuple  = (np.log(lambda_tuple[0]), np.log(lambda_tuple[1]))

    criterion       = dtypesx.strip_rmv_nmbr_space_case(criterion, case = 'lower')


    result \
        = minimize_scalar \
            (hp_info_crit,
             bounds = log_bnds_tuple,
             method = 'bounded',
             args = (y_array, criterion))


    opt_lambda_flt   = np.exp(result.x)

    return opt_lambda_flt


# In[68]:


#*******************************************************************************************
 #
 #  Function Name:  roll_corr_time_series
 #
 #  Function Description:
 #      This function applies rolling Pearson correlation to a time series.
 #
 #
 #  Return Type: series
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  series         X_series         The parameter is the x-values series.
 #  series         X_series         The parameter is the x-values series.
 #  integer        window           The parameter is the number of trading days 
 #                                  (30 ≈ 1.5 months, 60 ≈ 3 months).
 #  integer        min_periods      The parameter is the minimum observations required 
 #                                  to compute a value.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/18/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def roll_corr_time_series \
        (X_series:    pd.Series, 
         y_series:    pd.Series, 
         window:      int = 30, 
         min_periods: int = 20) \
-> pd.Series:

    data_df = pd.DataFrame({'x': X_series, 'y': y_series}).dropna()

    rolling_corr_series \
        = data_df['x'] \
            .rolling \
                (window = window, 
                 min_periods = min_periods) \
                    .corr(data_df['y'])

    return rolling_corr_series


# In[69]:


#*******************************************************************************************
 #
 #  Function Name:  detrend_time_series
 #
 #  Function Description:
 #      This function removes the trend from a time series.
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
 #  object         degree           The parameter is the degree of the polynomial trend.
 #  integer        max_degree       The parameter is the highest polynomial degree to try.
 #  string         criterion        The parameter is the model selection criteria ('aic' 
 #                                  or 'bic').
 #  string/integer nlags            The parameter indicates the number of lags.
 #  integer/none   maxlag           The parameter is the maximum lag which is included 
 #                                  in test, default value of 12*(nobs/100)^{1/4} is used 
 #                                  when None.
 #  integer        prec             The parameter is the output number precision.
 #  float          alpha            The parameter is the p-value threshold.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def detrend_time_series \
        (input_series: pd.Series,
         degree:       object = None,
         max_degree:   int    = 10,
         criterion:    str    = 'bic',
         nlags:        object = 'auto',
         maxlag:       int    = 20,
         prec:         int    = 6,
         alpha:        float  = 0.05) \
-> pd.Series:

    data_series, data_array, data_bool \
        = dtypesx.check_data_series_dtype_array(input_series)

    if data_bool == False: return data_series


    degree, int_bool = dtypesx.check_pos_int(degree)

    if int_bool == False: 

        degree \
            = find_opt_poly_degree \
                (data_series,
                 max_degree,
                 criterion,
                 nlags,
                 maxlag,
                 prec,
                 alpha)

    t_array = np.arange(len(data_array), dtype = float)

    coeffs_array     = np.polyfit(t_array, data_array, degree)


    data_array       = data_array - np.polyval(coeffs_array, t_array)


    data_series \
        = pd.Series \
            (data_array, 
             index = data_series.index, 
             name = data_series.name)\
                .dropna()

    data_series      = dtypesx.rtn_date_idxs(data_series)


    return data_series


# In[70]:


#*******************************************************************************************
 #
 #  Function Name:  diff_time_series
 #
 #  Function Description:
 #      This function applies differencing to a time series.
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
 #  int            diff_len         The parameter is the differencing length.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def diff_time_series \
        (input_series: pd.Series, 
         diff_len:     object = None) \
-> pd.Series:

    data_series = input_series.dropna()


    if diff_len is None: data_series = data_series.diff().dropna()

    elif isinstance(diff_len, float):

        diff_len    = int(abs(diff_len))

        if diff_len > 0: data_series = data_series.diff(diff_len).dropna()

        else: data_series = data_series.diff().dropna()

    elif isinstance(diff_len, int): 

        diff_len    = abs(diff_len)

        if diff_len > 0: data_series = data_series.diff(diff_len).dropna()

        else: data_series = data_series.diff().dropna()

    data_series = dtypesx.rtn_date_idxs(data_series)


    return data_series


# In[71]:


#*******************************************************************************************
 #
 #  Function Name:  log_diff_time_series
 #
 #  Function Description:
 #      This function applies a logarithm and differencing to a time series.
 #
 #
 #  Return Type: series
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  series         data_series      The parameter is the input series.
 #  int            diff_len         The parameter is the differencing length.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def log_diff_time_series \
        (input_series: pd.Series, 
         diff_len:     object = None) \
-> pd.Series:

    data_series = input_series.dropna()

    data_series = np.log(data_series)

    data_series = diff_time_series(data_series, diff_len = diff_len)

    data_series = dtypesx.rtn_date_idxs(data_series)

    return data_series


# In[72]:


#*******************************************************************************************
 #
 #  Function Name:  log_detrend_time_series
 #
 #  Function Description:
 #      This function applies a logarithm and polynomial-detrending to a time series.
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
 #  object         degree           This parameter is the degree of the polynomial 
 #                                  detrending.
 #  integer        max_degree       The parameter is the highest polynomial degree to try.
 #  string         criterion        The parameter is the model selection criteria ('aic' 
 #                                  or 'bic').
 #  string/integer nlags            The parameter indicates the number of lags.
 #  integer/none   maxlag           The parameter is the maximum lag which is included 
 #                                  in test, default value of 12*(nobs/100)^{1/4} is used 
 #                                  when None.
 #  integer        prec             The parameter is the output number precision.
 #  float          alpha            The parameter is the p-value threshold.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def log_detrend_time_series \
        (input_series: pd.Series,
         degree:       object = None,
         max_degree:   int    = 10,
         criterion:    str    = 'bic',
         nlags:        object = 'auto',
         maxlag:       int    = 20,
         prec:         int    = 6,
         alpha:        float  = 0.05) \
-> pd.Series:

    data_series, data_array, data_bool \
        = dtypesx.check_data_series_dtype_array(input_series)

    if data_bool == False: return data_series


    degree, int_bool = dtypesx.check_pos_int(degree)

    if int_bool == False: 

        degree \
            = find_opt_poly_degree \
                (data_series, max_degree, criterion, nlags, maxlag, prec, alpha)


    n_int            = len(data_array)

    log_array        = np.log(data_array)

    t_array          = np.arange(n_int, dtype = float)


    poly_coefs_array = np.polyfit(t_array, log_array, degree)

    trend_array      = np.polyval(poly_coefs_array, t_array)

    residuals_array  = log_array - trend_array


    data_series \
        = pd.Series \
            (residuals_array, 
             index = data_series.index, 
             name = data_series.name)\
                .dropna()

    data_series = dtypesx.rtn_date_idxs(data_series)

    return data_series


# In[73]:


#*******************************************************************************************
 #
 #  Function Name:  hp_filter_time_series
 #
 #  Function Description:
 #      This function applies a Hodrick-Prescott filter to a time series.
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
 #  array          lambda_tuple     The parameter is the bounds for the lambda search.
 #  string         criterion        The parameter is one of the following statistical 
 #                                  methods: 'aic', 'bic', or 'mse'.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def hp_filter_time_series \
        (input_series: pd.Series,
         lambda_tuple: tuple = (1, 1e9),
         criterion:    str   = 'bic') \
-> pd.Series:

    data_series, data_array, data_bool \
        = dtypesx.check_data_series_dtype_array(input_series)

    if data_bool == False: return data_series


    lambda_flt  = find_opt_hp_lambda(data_series, lambda_tuple, criterion)

    cycle, _    = hpfilter(data_array, lamb = lambda_flt)


    data_series \
        = pd.Series \
            (cycle.values, 
             index = data_series.index, 
             name = data_series.name) \
                .dropna()

    data_series = dtypesx.rtn_date_idxs(data_series)

    return data_series


# In[74]:


#*******************************************************************************************
 #
 #  Function Name:  boxcox_time_series
 #
 #  Function Description:
 #      This function applies a Box-Cox transformation to a time series, automatically 
 #      handling non-positive values by shifting the data.
 #
 #
 #  Return Type: series, float
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
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def boxcox_time_series(input_series: pd.Series) -> tuple[pd.Series, float]:

    data_series, data_array, data_bool \
        = dtypesx.check_data_series_dtype_array(input_series)

    if data_bool == False: return data_series


    if np.min(data_array) <= 0:

        shift_flt        = abs(np.min(data_array)) + 1.0

        data_pos_array   = data_array + shift_flt

    else: data_pos_array = data_array.copy()


    bc_array, lambda_flt = boxcox(data_pos_array)

    bc_series \
        = pd.Series \
            (bc_array,
             index = data_series.index,
             name  = data_series.name) \
                .dropna()

    return bc_series, lambda_flt


# In[75]:


#*******************************************************************************************
 #
 #  Function Name:  crct_diff_stnry_series
 #
 #  Function Description:
 #      This function corrects a difference stationary time series to achieve stationarity.
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
 #  boolean        vrb_bool         The parameter is the indicator for verbosity.
 #  integer/none   maxlag           The parameter is the maximum lag which is included 
 #                                  in test, default value of 12*(nobs/100)^{1/4} is used 
 #                                  when None.
 #  string         index            The parameter is the output index name.
 #  float          min_r2           The parameter is the minimum R² the log-linear 
 #                                  model must achieve.
 #  float          lin_vs_exp_gap   The parameter is the minimum margin by which 
 #                                  log-linear R² must beat linear R².
 #  integer        max_degree       The parameter is the highest polynomial degree to try.
 #  string         criterion        The parameter is the model selection criteria ('aic' 
 #                                  or 'bic').
 #  integer        prec             The parameter is the output number precision.
 #  float          alpha            The parameter is the p-value threshold.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def crct_diff_stnry_series \
        (input_series:   pd.Series,
         vrb_bool:       bool   = True,
         maxlag:         object = None,
         index:          str    = 'series',
         min_r2:         float  = 0.80,
         lin_vs_exp_gap: float  = 0.05,
         max_degree:     int    = 10,
         criterion:      str    = 'bic',
         nlags:          object = 'auto',
         prec:           int    = 6, 
         alpha:          float  = 0.05) \
-> pd.Series:

    data_series = input_series.dropna()


    if maxlag is None: maxlag_int = int(12.0 * (float(len(data_series)) / 100.0)**(0.25))

    else:              maxlag_int = int(abs(maxlag))


    if vrb_bool:

        logx.print_and_log_text \
            ('\033[1m'
             + f'DIFFERENCE STATIONARY TIME SERIES DETECTED: {data_series.name}.\n' 
             + '\033[0m')


    if is_linear_trend(data_series, prec, alpha): 

        if vrb_bool:

            logx.print_and_log_text \
                ('\033[1m'
                 + 'Linear trend detected:\n'
                 + f'Detrending (first degree polynomial) time series {data_series.name}...\n'
                 + '\033[0m')

        crct_series \
            = detrend_time_series \
                (data_series, 
                 degree     = 1,
                 max_degree = max_degree,
                 criterion  = criterion,
                 nlags      = nlags,
                 maxlag     = maxlag_int,
                 prec       = prec,
                 alpha      = alpha)

    else: 

        if vrb_bool:

            logx.print_and_log_text \
                ('\033[1m' 
                 + f'Detrending (optimal polynomial degree) time series {data_series.name}...\n'
                 + '\033[0m')

        crct_series \
            = detrend_time_series \
                (data_series, 
                 degree     = None,
                 max_degree = max_degree,
                 criterion  = criterion,
                 nlags      = nlags,
                 maxlag     = maxlag_int,
                 prec       = prec,
                 alpha      = alpha)


    adf_results_dict \
        = opt_adf_stnry_series \
            (crct_series, 
             index  = index, 
             maxlag = maxlag, 
             prec   = prec, 
             alpha  = alpha)

    kpss_results_dict \
        = opt_kpss_stnry_series \
            (crct_series, 
             index = index, 
             prec  = prec, 
             alpha = alpha)

    if not adf_results_dict['stationary'] or not kpss_results_dict['stationary']: 

        if vrb_bool:

            logx.print_and_log_text \
                ('\033[1m' 
                 + f'Differencing (period = 1) time series {data_series.name}...\n' 
                 + '\033[0m')

        crct_series = diff_time_series(crct_series, diff_len = None)


    adf_results_dict \
        = opt_adf_stnry_series \
            (crct_series, 
             index  = index, 
             maxlag = maxlag, 
             prec   = prec, 
             alpha  = alpha)

    kpss_results_dict \
        = opt_kpss_stnry_series \
            (crct_series, 
             index = index, 
             prec  = prec, 
             alpha = alpha)

    if not adf_results_dict['stationary'] or not kpss_results_dict['stationary']: 

        if is_exponential_trend(crct_series, min_r2, lin_vs_exp_gap, prec, alpha):

            if vrb_bool:

                logx.print_and_log_text \
                    ('\033[1m' \
                     + 'Exponential trend detected:\n' \
                     + f'applying logarithm and detrending (optimal degree) to time series {data_series.name}...\n' \
                     + '\033[0m')

            crct_series \
                = log_detrend_time_series \
                    (crct_series,
                     degree     = None,
                     max_degree = max_degree,
                     criterion  = criterion,
                     nlags      = nlags,
                     maxlag     = maxlag_int,
                     prec       = prec,
                     alpha      = alpha)

        else: 

            if vrb_bool:

                logx.print_and_log_text \
                    ('\033[1m' 
                     + f'Applying Hodrick-Prescott filter to time series {data_series.name}...\n' 
                     + '\033[0m')

            crct_series = hp_filter_time_series(crct_series)


    adf_results_dict \
        = opt_adf_stnry_series \
            (crct_series, 
             index  = index, 
             maxlag = maxlag, 
             prec   = prec, 
             alpha  = alpha)

    kpss_results_dict \
        = opt_kpss_stnry_series \
            (crct_series, 
             index = index, 
             prec  = prec, 
             alpha = alpha)

    if not adf_results_dict['stationary'] or not kpss_results_dict['stationary']: 

        if vrb_bool:

            logx.print_and_log_text \
                ('\033[1m' 
                 + f'Detrending (optimal polynomial degree) time series {data_series.name}...\n' 
                 + '\033[0m')

        crct_series \
            = detrend_time_series \
                (crct_series, 
                 degree     = None,
                 max_degree = max_degree,
                 criterion  = criterion,
                 nlags      = nlags,
                 maxlag     = maxlag_int,
                 prec       = prec,
                 alpha      = alpha)


    if vrb_bool: logx.print_and_log_text('\n')


    return crct_series        


# In[76]:


#*******************************************************************************************
 #
 #  Function Name:  crct_trend_stnry_series
 #
 #  Function Description:
 #      This function corrects for stationarity in a trend stationary time series.
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
 #  boolean        vrb_bool         The parameter is the indicator for verbosity.
 #  integer/none   maxlag           The parameter is the maximum lag which is included 
 #                                  in test, default value of 12*(nobs/100)^{1/4} is used 
 #                                  when None.
 #  string         index            The parameter is the output index name.
 #  float          min_r2           The parameter is the minimum R² the log-linear 
 #                                  model must achieve.
 #  float          lin_vs_exp_gap   The parameter is the minimum margin by which 
 #                                  log-linear R² must beat linear R².
 #  integer        max_degree       The parameter is the highest polynomial degree to try.
 #  string         criterion        The parameter is the model selection criteria ('aic' 
 #                                  or 'bic').
 #  integer        prec             The parameter is the output number precision.
 #  float          alpha            The parameter is the p-value threshold.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def crct_trend_stnry_series \
        (input_series:   pd.Series,
         vrb_bool:       bool   = True,
         maxlag:         object = None,
         index:          str    = 'series',
         min_r2:         float  = 0.80,
         lin_vs_exp_gap: float  = 0.05,
         max_degree:     int    = 10,
         criterion:      str    = 'bic',
         nlags:          object = 'auto',
         prec:           int    = 6, 
         alpha:          float  = 0.05) \
-> pd.Series:

    data_series = input_series.dropna()


    if maxlag is None: maxlag_int = int(12.0 * (float(len(data_series)) / 100.0)**(0.25))

    else:              maxlag_int = int(abs(maxlag))


    if vrb_bool:

        logx.print_and_log_text \
            ('\033[1m'
             + f'TREND-STATIONARY TIME SERIES DETECTED: {data_series.name}.\n' 
             + '\033[0m')


        logx.print_and_log_text \
            ('\033[1m' 
             + f'Detrending (optimal polynomial degree) time series {data_series.name}...\n'
             + '\033[0m')


    crct_series \
        = detrend_time_series \
            (data_series, 
             degree     = None,
             max_degree = max_degree,
             criterion  = criterion,
             nlags      = nlags,
             maxlag     = maxlag_int,
             prec       = prec,
             alpha      = alpha)


    adf_results_dict \
        = opt_adf_stnry_series \
            (crct_series, 
             index  = index, 
             maxlag = maxlag, 
             prec   = prec, 
             alpha  = alpha)

    kpss_results_dict \
        = opt_kpss_stnry_series \
            (crct_series, 
             index = index, 
             prec  = prec, 
             alpha = alpha)

    if not adf_results_dict['stationary'] or not kpss_results_dict['stationary']: 

        if vrb_bool:

            logx.print_and_log_text \
                ('\033[1m' 
                 + f'Differencing (period = 1) time series {data_series.name}...\n' 
                 + '\033[0m')

        crct_series = diff_time_series(crct_series, diff_len = None)


    adf_results_dict \
        = opt_adf_stnry_series \
            (crct_series, 
             index  = index, 
             maxlag = maxlag, 
             prec   = prec, 
             alpha  = alpha)

    kpss_results_dict \
        = opt_kpss_stnry_series \
            (crct_series, 
             index = index, 
             prec  = prec, 
             alpha = alpha)

    if not adf_results_dict['stationary'] or not kpss_results_dict['stationary']: 

        if is_linear_trend(crct_series, prec, alpha) \
            or is_exponential_trend(crct_series, min_r2, lin_vs_exp_gap, prec, alpha):

            if vrb_bool:

                logx.print_and_log_text \
                    ('\033[1m' \
                     + 'Linear or exponential trend detected:\n' \
                     + f'logarithm and differencing (period = 1) applied to time series {data_series.name}...\n' \
                     + f'detrending time series {data_series.name}...' \
                     + '\033[0m')

            crct_series = log_diff_time_series(crct_series, diff_len = None)

            crct_series \
                = detrend_time_series \
                    (data_series, 
                     degree     = None,
                     max_degree = max_degree,
                     criterion  = criterion,
                     nlags      = nlags,
                     maxlag     = maxlag_int,
                     prec       = prec,
                     alpha      = alpha)

        else: 

            if vrb_bool:

                logx.print_and_log_text \
                    ('\033[1m' 
                     + f'Applying Box-Cox transformation to time series {data_series.name}...\n' 
                     + '\033[0m')

            crct_series, _ = boxcox_time_series(crct_series)


    if vrb_bool: logx.print_and_log_text('\n')

    return crct_series


# In[77]:


#*******************************************************************************************
 #
 #  Function Name:  crct_non_stnry_series
 #
 #  Function Description:
 #      This function attempts to correct a time series to achieve stationarity that has
 #      failed both the ADF and KPSS tests.
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
 #  boolean        vrb_bool         The parameter is the indicator for verbosity.
 #  integer/none   maxlag           The parameter is the maximum lag which is included 
 #                                  in test, default value of 12*(nobs/100)^{1/4} is used 
 #                                  when None.
 #  string         index            The parameter is the output index name.
 #  float          min_r2           The parameter is the minimum R² the log-linear 
 #                                  model must achieve.
 #  float          lin_vs_exp_gap   The parameter is the minimum margin by which 
 #                                  log-linear R² must beat linear R².
 #  integer        prec             The parameter is the output number precision.
 #  float          alpha            The parameter is the p-value threshold.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def crct_non_stnry_series \
        (input_series:   pd.Series,
         vrb_bool:       bool   = True,
         maxlag:         object = None,
         index:          str    = 'series',
         min_r2:         float  = 0.80,
         lin_vs_exp_gap: float  = 0.05,
         prec:           int    = 6, 
         alpha:          float  = 0.05) \
-> pd.Series:

    data_series = input_series.dropna()


    if maxlag is None: maxlag_int = int(12.0 * (float(len(data_series)) / 100.0)**(0.25))

    else:              maxlag_int = int(abs(maxlag))


    if vrb_bool:

        logx.print_and_log_text \
            ('\033[1m'
             + f'NON-STATIONARY TIME SERIES DETECTED: {data_series.name}.\n' 
             + '\033[0m')


    if is_exponential_trend(data_series, min_r2, lin_vs_exp_gap, prec, alpha):

        if vrb_bool:

            logx.print_and_log_text \
                ('\033[1m' \
                 + 'Exponential trend detected:\n' \
                 + f'logarithm and differencing applied to time series {data_series.name}...\n' \
                 + f'Differencing (period = 1) time series {data_series.name}...' \
                 + '\033[0m')

        crct_series = log_diff_time_series(data_series, diff_len = None)

        crct_series = diff_time_series(crct_series, diff_len = None)

    else: 

        if vrb_bool:

            logx.print_and_log_text \
                ('\033[1m' 
                 + f'Differencing (period = 1) time series {data_series.name}...\n' 
                 + '\033[0m')

        crct_series = diff_time_series(data_series, diff_len = None)


    adf_results_dict \
        = opt_adf_stnry_series \
            (crct_series, 
             index  = index, 
             maxlag = maxlag, 
             prec   = prec, 
             alpha  = alpha)

    kpss_results_dict \
        = opt_kpss_stnry_series \
            (crct_series, 
             index = index, 
             prec  = prec, 
             alpha = alpha)

    if not adf_results_dict['stationary'] or not kpss_results_dict['stationary']: 

        if vrb_bool:

            logx.print_and_log_text \
                ('\033[1m' 
                 + f'Differencing (period = 1) time series {data_series.name}...\n' 
                 + '\033[0m')

        crct_series = diff_time_series(crct_series, diff_len = None)


    adf_results_dict \
        = opt_adf_stnry_series \
            (crct_series, 
             index  = index, 
             maxlag = maxlag, 
             prec   = prec, 
             alpha  = alpha)

    kpss_results_dict \
        = opt_kpss_stnry_series \
            (crct_series, 
             index = index, 
             prec  = prec, 
             alpha = alpha)

    if not adf_results_dict['stationary'] or not kpss_results_dict['stationary']:

        if vrb_bool:

            logx.print_and_log_text \
                ('\033[1m' 
                 + 'Applying Box-Cox transformation and differencing (period = 1) ' \
                 + f'to time series {data_series.name}...\n' 
                 + '\033[0m')

        crct_series, _ = boxcox_time_series(crct_series)

        crct_series = diff_time_series(crct_series, diff_len = None)


    if vrb_bool: logx.print_and_log_text('\n')

    return crct_series 


# In[78]:


#*******************************************************************************************
 #
 #  Function Name:  regr_model_eqn_coef_disp
 #
 #  Function Description:
 #      This function returns the coefficients for a regression equation using x-y series
 #      truncated for display purposes.
 #
 #
 #  Return Type: np.poly1d object
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  array          X_obj            The parameter is the object holding the x values.
 #  array          y_obj            The parameter is the object holding the y values.
 #  object         degree           This parameter is the degree of the polynomial.
 #  integer        prec             This parameter is the coefficient precision.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def regr_model_eqn_coef_disp \
        (X_obj:  object, 
         y_obj:  object, 
         degree: object, 
         prec:   int = 6) \
-> object:

    X_array, X_bool = dtypesx.check_data_dtype_array(X_obj)

    y_array, y_bool = dtypesx.check_data_dtype_array(y_obj)

    if X_bool == False or y_bool == False: return X_array


    degree, int_bool = dtypesx.check_pos_int(degree)

    if int_bool == False: return None


    data_poly1d = np.poly1d(np.polyfit(X_array, y_array, degree))


    eqn_coeffs_array = data_poly1d.coeffs

    if len(eqn_coeffs_array) == 0: eqn_poly1d = np.poly1d([0])

    else: eqn_poly1d = np.poly1d(eqn_coeffs_array)


    return eqn_poly1d


# In[79]:


#*******************************************************************************************
 #
 #  Function Name:  regr_model_eqn_coef
 #
 #  Function Description:
 #      This function returns the coefficients for a regression equation using x-y series.
 #
 #
 #  Return Type: np.poly1d object
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  object         X_obj            The parameter is the array holding the x values.
 #  object         y_obj            The parameter is the array holding the y values.
 #  object         degree           This parameter is the degree of the polynomial.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def regr_model_eqn_coef \
        (X_obj:  object, 
         y_obj:  object, 
         degree: object) \
-> object:

    X_array, X_bool  = dtypesx.check_data_dtype_array(X_obj)

    y_array, y_bool  = dtypesx.check_data_dtype_array(y_obj)

    if X_bool == False or y_bool == False: return X_array


    degree, int_bool = dtypesx.check_pos_int(degree)

    if int_bool == False: return None


    data_poly1d      = np.poly1d(np.polyfit(X_array, y_array, degree))

    return data_poly1d


# In[80]:


#*******************************************************************************************
 #
 #  Function Name:  rtn_poly_line_array
 #
 #  Function Description:
 #      This function returns a polynomial line as an array.
 #
 #
 #  Return Type: array
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  obj            X_obj            The parameter is the object holding the x values.
 #  obj            y_obj            The parameter is the object holding the y values.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def rtn_poly_line_array \
        (X_obj: object, 
         y_obj: object) \
-> np.ndarray:

    X_array, X_bool = dtypesx.check_data_dtype_array(X_obj)

    y_array, y_bool = dtypesx.check_data_dtype_array(y_obj)

    if X_bool == False or y_bool == False: return X_array


    poly_line_array \
        = np.linspace \
            (X_array.min(), 
             X_array.max(), 
             abs(int((X_array.max() - y_array.min()) / 2.0)))

    return poly_line_array


# In[81]:


#*******************************************************************************************
 #
 #  Function Name:  rtn_eqn_as_text
 #
 #  Function Description:
 #      This function returns the model equation as a string.
 #
 #
 #  Return Type: string
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  array          model_eqn_array  The parameter is a array of coefficients for a 
 #                                  polynomial.
 #  integer        coef_prec        The parameter is the precision of the equation's 
 #                                  coefficients.
 # 
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def rtn_eqn_as_text \
        (model_eqn_array: np.ndarray, 
         coef_prec:       int = 2) \
-> str:

    degree_int = len(model_eqn_array)

    for idx, term in enumerate(model_eqn_array):

        temp_eqn = f'{term:.2e}'

        if degree_int > 1: temp_eqn += 'x' + '^' + str(degree_int)

        elif degree_int == 1: temp_eqn += 'x'


        if degree_int == len(model_eqn_array): final_eqn = temp_eqn

        else: final_eqn += ' + ' + temp_eqn


        degree_int -= 1


    return 'y = ' + final_eqn


# In[82]:


#*******************************************************************************************
 #
 #  Function Name:  rtn_r_sqr
 #
 #  Function Description:
 #      This function returns the r-squared value from x-y series.
 #
 #
 #  Return Type: float
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  object         X_obj            The parameter is the object holding the x-values.
 #  object         y_obj            The parameter is the object holding the y-values.
 #  object         degree           The parameter is the degree of the polynomial.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def rtn_r_sqr \
        (X_obj:  object, 
         y_obj:  object, 
         degree: object) \
-> float:

    X_array, X_bool  = dtypesx.check_data_dtype_array(X_obj)

    y_array, y_bool  = dtypesx.check_data_dtype_array(y_obj)

    if X_bool == False or y_bool == False: return X_array


    degree, int_bool = dtypesx.check_pos_int(degree)

    if int_bool == False: return degree


    coeffs_array     = np.polyfit(X_array, y_array, degree)

    pPoly1D          = np.poly1d(coeffs_array)


    yhat_array       = pPoly1D(X_array)

    ybar_flt         = np.sum(y_array) / len(y_array)


    ssreg_flt        = np.sum(((yhat_array - ybar_flt) ** 2))

    sstot_flt        = np.sum(((y_array - ybar_flt) ** 2))


    rslt_flt         = ssreg_flt / sstot_flt

    return rslt_flt


# In[83]:


#*******************************************************************************************
 #
 #  Function Name:  rtn_stats_values
 #
 #  Function Description:
 #      This function returns the r and p values for statistical correlations.
 #
 #
 #  Return Type: dict
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  object         X_obj            The parameter is the object holding the x-values.
 #  object         y_obj            The parameter is the object holding the y-values.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def rtn_stats_values \
        (X_obj: object, 
         y_obj: object) \
-> dict:

    X_array, X_bool          = dtypesx.check_data_dtype_array(X_obj)

    y_array, y_bool          = dtypesx.check_data_dtype_array(y_obj)

    if X_bool == False or y_bool == False: return X_array


    X_cln_array              = X_array[~np.isnan(X_array)]

    y_cln_array              = y_array[~np.isnan(y_array)]    


    r_prsn_flt, p_prsn_flt   = pearsonr(X_cln_array, y_cln_array)

    r_sprmn_flt, p_sprmn_flt = spearmanr(X_cln_array, y_cln_array)

    tau_kndl_flt, p_kndl_flt = kendalltau(X_cln_array, y_cln_array)


    rslt_dict \
        = {'r-value (pearson)':  round(r_prsn_flt, 3),
           'r-value (spearman)': round(r_sprmn_flt, 3),
           'tau (kendall)':      round(tau_kndl_flt, 3),
           'p-value (pearson)':  round(p_prsn_flt, 3),
           'p-value (spearman)': round(p_sprmn_flt, 3),
           'p-value (kendall)':  round(p_kndl_flt, 3)}

    return rslt_dict


# In[84]:


#*******************************************************************************************
 #
 #  Function Name:  use_median_kfold_cv_errors
 #
 #  Function Description:
 #      This function returns True if the median is more appropriate than the mean
 #      for summarising K-Fold CV errors across folds
 #
 #      Evaluates four criteria:
 #      1. High coefficient of variation — fold errors are inconsistent
 #      2. High skewness                 — fold error distribution is asymmetric
 #      3. High excess kurtosis          — heavy tails / extreme fold errors
 #      4. Outlier folds                 — one or more folds are anomalous
 #
 #
 #  Return Type: bool
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  object         fold_errors_obj  The parameter is the k-fold errors object.
 #  dictionary     attr_dict        The parameter is the distribution thresholds.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def use_median_kfold_cv_errors \
        (fold_errors_obj: object,
         attr_dict:       dict \
                            = {'cv_thrhld':   0.5,
                               'skew_thrhld': 1.0,
                               'kurt_thrhld': 3.0,
                               'outlier_z':   2.5}) \
-> bool:

    fold_errs_array, fold_errs_bool \
        = dtypesx.check_data_dtype_array(fold_errors_obj)

    if fold_errs_bool == False or len(fold_errs_array) < 3: return False


    mean_flt      = np.mean(fold_errs_array)

    std_flt       = np.std(fold_errs_array, ddof = 1)


    cv_flt        = std_flt / mean_flt if mean_flt != 0 else 0.0

    skew_flt      = skew(fold_errs_array)

    kurt_flt      = kurtosis(fold_errs_array, fisher = True)


    z_scores_array \
        = np.abs \
            ((fold_errs_array - mean_flt) / std_flt) \
             if std_flt > 0 else np.zeros(len(fold_errs_array))


    use_kfold_bool    = (cv_flt                > attr_dict['cv_thrhld']   or \
                         abs(skew_flt)         > attr_dict['skew_thrhld'] or \
                         kurt_flt              > attr_dict['kurt_thrhld'] or \
                         np.any(z_scores_array > attr_dict['outlier_z']))

    return use_kfold_bool


# In[85]:


#*******************************************************************************************
 #
 #  Function Name:  opt_poly_degree_mse_rslts
 #
 #  Function Description:
 #      This function calculates the results for the best polynomial degree using 
 #      K-Fold cross-validation with MSE.
 #
 #
 #  Return Type: integer, dictionary
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  object         X_obj            The parameter is the x-values object.
 #  object         X_obj            The parameter is the y-values object.
 #  integer        max_degree       The parameter is the maximum polynomial degree.
 #  integer        k_folds          The parameter is the number of k-folds.
 #  integer        random_state     The parameter is the random state.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def opt_poly_degree_mse_rslts \
        (X_array:      np.ndarray, 
         y_array:      np.ndarray,
         max_degree:   int = 10, 
         k_folds:      int = 5, 
         random_state: int = 42) \
-> tuple[int, dict]:

    kf \
        = KFold \
            (n_splits     = k_folds, 
             shuffle      = True, 
             random_state = random_state)

    cv_errors_dict = {}

    for degree in range(1, max_degree + 1):

        poly              = PolynomialFeatures(degree = degree)

        fold_errors_array = np.asarray([])

        for train_idx, val_idx in kf.split(X_array):

            X_train_array, X_val_array = X_array[train_idx], X_array[val_idx]

            y_train_array, y_val_array = y_array[train_idx], y_array[val_idx]


            X_train_poly_array         = poly.fit_transform(X_train_array)

            X_val_poly_array           = poly.transform(X_val_array)


            model = LinearRegression()

            model.fit(X_train_poly_array, y_train_array)


            y_pred_array = model.predict(X_val_poly_array)

            fold_errors_array \
                = np.append \
                    (fold_errors_array, 
                     mean_squared_error(y_val_array, y_pred_array))


        if not use_median_kfold_cv_errors(fold_errors_array): 

            cv_errors_dict[degree]   = np.mean(fold_errors_array)

        else: cv_errors_dict[degree] = np.median(fold_errors_array)


    best_deg_int = min(cv_errors_dict, key = cv_errors_dict.get)

    return best_deg_int, cv_errors_dict


# In[86]:


#*******************************************************************************************
 #
 #  Function Name:  opt_poly_degree_mse
 #
 #  Function Description:
 #      This function returns the best polynomial degree using K-Fold cross-validation 
 #      with MSE.
 #
 #
 #  Return Type: integer, dictionary
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  object         X_obj            The parameter is the x-values object.
 #  object         X_obj            The parameter is the y-values object.
 #  integer        max_degree       The parameter is the maximum polynomial degree.
 #  integer        k_folds          The parameter is the number of k-folds.
 #  integer        random_state     The parameter is the random state.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def opt_poly_degree_mse \
        (X_obj:        object, 
         y_obj:        object, 
         max_degree:   int = 10, 
         k_folds:      int = 5, 
         random_state: int = 42) \
-> tuple[int, dict]:

    X_array, X_bool \
        = dtypesx.check_data_dtype_array(X_obj)

    y_array, y_bool \
        = dtypesx.check_data_dtype_array(y_obj)

    if X_bool == False or y_bool == False: return X_array


    data_df = pd.DataFrame({'x': X_array, 'y': y_array}).dropna()


    X_array = data_df['x'].values.reshape(-1, 1)

    y_array = data_df['y'].values


    best_deg_int, cv_errors_dict \
        = opt_poly_degree_mse_rslts \
            (X_array, y_array, max_degree, k_folds, random_state)

    return best_deg_int, cv_errors_dict


# In[87]:


#*******************************************************************************************
 #
 #  Function Name:  opt_poly_degree_ic_rslts
 #
 #  Function Description:
 #      This function calculates the results for the best polynomial degree using AIC/BIC.
 #
 #
 #  Return Type: integer, dictionary
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  object         X_obj            The parameter is the x-values object.
 #  object         y_obj            The parameter is the y-values object.
 #  integer        max_degree       The parameter is the maximum polynomial degree.
 #  string         criterion        The parameter is the model selection criteria ('aic' 
 #                                  or 'bic'). #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def opt_poly_degree_ic_rslts \
        (X_array:    np.ndarray,
         y_array:    np.ndarray,
         max_degree: int,
         criterion:  str) \
-> tuple[int, dict]:

    n_int          = len(y_array)

    cv_errors_dict = {}

    for degree in range(1, max_degree + 1):

        poly = PolynomialFeatures(degree = degree)


        X_poly_array    = poly.fit_transform(X_array)

        k_int           = X_poly_array.shape[1]


        model = LinearRegression()

        model.fit(X_poly_array, y_array)


        y_pred_array    = model.predict(X_poly_array)

        residuals_array = y_array - y_pred_array


        sse_flt         = np.sum(residuals_array**2)

        sigma2_flt      = sse_flt / float(n_int)

        log_likelihood_flt \
            = float(-n_int) / 2.0 * np.log(2.0 * np.pi * sigma2_flt) - sse_flt / (2.0 * sigma2_flt)


        if criterion == 'aic': 

            cv_errors_dict[degree] \
                = 2.0 * float(k_int) - 2.0 * log_likelihood_flt

        else: 

            cv_errors_dict[degree] \
                = float(k_int) * np.log(float(n_int)) - 2.0 * log_likelihood_flt


    best_deg_int        = min(cv_errors_dict, key = cv_errors_dict.get)

    return best_deg_int, cv_errors_dict


# In[88]:


#*******************************************************************************************
 #
 #  Function Name:  opt_poly_degree_ic
 #
 #  Function Description:
 #      This function returns the best polynomial degree using AIC/BIC, which assume 
 #      the residuals are normally distributed, which is questionable for noisy
 #      percentage-change financial data with MSE.
 #
 #
 #  Return Type: integer, dictionary
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  object         X_obj            The parameter is the x-values object.
 #  object         y_obj            The parameter is the y-values object.
 #  integer        max_degree       The parameter is the maximum polynomial degree.
 #  string         criterion        The parameter is the model selection criteria ('aic' 
 #                                  or 'bic'). #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def opt_poly_degree_ic \
        (X_obj:      object, 
         y_obj:      object, 
         max_degree: int = 10, 
         criterion:  str = 'bic') \
-> tuple[int, dict]:

    X_array, X_bool = dtypesx.check_data_dtype_array(X_obj)

    y_array, y_bool = dtypesx.check_data_dtype_array(y_obj)

    if X_bool == False or y_bool == False: return None, None


    data_df         = pd.DataFrame({'x': X_array, 'y': y_array}).dropna()

    criterion       = dtypesx.strip_rmv_nmbr_space_case(criterion, case = 'lower') 


    X_array         = data_df['x'].values.reshape(-1, 1)

    y_array         = data_df['y'].values


    best_deg_int, cv_errors_dict \
        = opt_poly_degree_ic_rslts \
            (X_array, y_array, max_degree, criterion)      

    return best_deg_int, cv_errors_dict


# In[89]:


#*******************************************************************************************
 #
 #  Function Name: opt_poly_deg_rslts_list_parms
 #
 #  Function Description:
 #      This function finds the optimal polynomial degree for correlation between two time 
 #      series using a combination of AIC, cross-validated R², and overfitting detection.
 #
 #
 #  Return Type: float, float, float, float, boolean
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  array          X_array          The parameter is the x-values array.
 #  array          y_array          The parameter is the y-values array.
 #  integer        n                The parameter is the number of data points in the
 #                                  y-array.
 #  integer        degree           The parameter is the correlation polynomial degree.
 #  integer        cv_folds         The parameter is the number of cross-validation folds.
 #  float          ovrft_r2_gp      The parameter is the maximum allowed gap between train 
 #                                  and CV R².
 #  integer        prec             The parameter is the output number precision.
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def opt_poly_deg_rslts_list_parms \
        (X_array:        np.ndarray,
         y_array:        np.ndarray,
         n:              int,
         degree:         int,
         cv_folds:       int   = 5,
         ovrft_r2_gp:    float = 0.15,
         prec:           int   = 6) \
-> tuple[float, float, float, float, bool]:

    pipeline \
        = Pipeline \
            ([('poly',  PolynomialFeatures \
                            (degree = degree, 
                             include_bias = True)),
              ('model', LinearRegression())])

    pipeline.fit(X_array, y_array)


    y_pred_array    = pipeline.predict(X_array)

    train_r2_flt    = r2_score(y_array, y_pred_array)


    cv_scores_array \
        = cross_val_score \
            (pipeline,
             X_array, 
             y_array, 
             cv = cv_folds, 
             scoring = 'r2')

    cv_r2_flt       = np.mean(cv_scores_array)

    cv_r2_std_flt   = np.std(cv_scores_array)


    residuals_array = y_array - y_pred_array

    sse_flt         = np.sum(residuals_array ** 2)

    k_int           = degree + 2


    overfit_bool \
        = round((train_r2_flt - cv_r2_flt), prec) > round(ovrft_r2_gp, prec)

    aic_flt \
        = float(n) * np.log(sse_flt / float(n) + 1e-10) + 2.0 * float(k_int)


    return \
        train_r2_flt, \
        cv_r2_flt, \
        cv_r2_std_flt, \
        aic_flt, \
        overfit_bool


# In[90]:


#*******************************************************************************************
 #
 #  Function Name:  opt_poly_deg_rslts_list
 #
 #  Function Description:
 #      This function finds the results dictionary list for optimal correlation polynomial.
 #
 #
 #  Return Type: list
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  array          X_array          The parameter is the x-values array.
 #  array          y_array          The parameter is the y-values array.
 #  integer        n                The parameter is the number of data points in the
 #                                  y-array.
 #  integer        max_degree       The parameter is the maximum polynomial degree.
 #  integer        cv_folds         The parameter is the number of cross-validation folds.
 #  float          ovrft_r2_gp      The parameter is the maximum allowed gap between train 
 #                                  and CV R².
 #  integer        prec             The parameter is the output number precision.
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def opt_poly_deg_rslts_list \
        (X_array:        np.ndarray,
         y_array:        np.ndarray,
         n:              int,
         max_degree:     int   = 10,
         cv_folds:       int   = 5,
         ovrft_r2_gp:    float = 0.15,
         prec:           int   = 6) \
-> list:

    results_list = []

    for degree in range(1, max_degree + 1):

        train_r2_flt, \
        cv_r2_flt, \
        cv_r2_std_flt, \
        aic_flt, \
        overfit_bool \
            = opt_poly_deg_rslts_list_parms \
                (X_array, 
                 y_array, 
                 n           = n, 
                 degree      = degree, 
                 cv_folds    = cv_folds,
                 ovrft_r2_gp = ovrft_r2_gp,
                 prec        = prec)

        results_list.append \
            ({'degree':    int(degree),
              'train_r2':  round(float(train_r2_flt),  prec),
              'cv_r2':     round(float(cv_r2_flt),     prec),
              'cv_r2_std': round(float(cv_r2_std_flt), prec),
              'aic':       round(float(aic_flt),       prec),
              'overfit':   bool(overfit_bool)})


    return results_list


# In[91]:


#*******************************************************************************************
 #
 #  Function Name:  opt_poly_deg_cnd_list
 #
 #  Function Description:
 #      This function finds the candidates dictionary list for optimal correlation 
 #      polynomial.
 #
 #
 #  Return Type: list
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  list           results_list     The parameter is the results dictionary list.
 #  float          aic_wgt          The parameter is the weight given to AIC score in 
 #                                  combined ranking.
 #  float          cv_wgt           The parameter is the weight given to CV R² in combined 
 #                                  ranking.
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def opt_poly_deg_cnd_list \
        (results_list: list,
         aic_wgt:      float,
         cv_wgt:       float) \
-> list:

    aics_array     = np.asarray([r['aic'] for r in results_list])

    cv_r2s_array   = np.asarray([r['cv_r2'] for r in results_list])


    aic_rng_flt    = aics_array.max() - aics_array.min() + 1e-10

    cv_rng_flt     = cv_r2s_array.max() - cv_r2s_array.min() + 1e-10


    aic_norm_array = 1 - (aics_array - aics_array.min()) / aic_rng_flt

    cv_norm_array  = (cv_r2s_array - cv_r2s_array.min()) / cv_rng_flt


    for i, r in enumerate(results_list):

        r['aic_norm']       = float(aic_norm_array[i])

        r['cv_norm']        = float(cv_norm_array[i])

        r['combined_score'] = float(aic_wgt * aic_norm_array[i] + cv_wgt * cv_norm_array[i])


    non_overfit_list = [r for r in results_list if not r['overfit']]


    cnds_list        = non_overfit_list if non_overfit_list else results_list  

    return cnds_list


# In[92]:


#*******************************************************************************************
 #
 #  Function Name:  opt_poly_deg_final_dict
 #
 #  Function Description:
 #      This function finds the final results dictionary for optimal correlation polynomial.
 #
 #
 #  Return Type: dictionary
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  array          X_array          The parameter is the x-values array.
 #  array          y_array          The parameter is the y-values array.
 #  list           results_list     The parameter is the results dictionary list.
 #  list           cnds_list        The parameter is the candidates list.
 #  integer        prec             The parameter is the output number precision.
 #  float          alpha            The parameter is the p-value threshold.
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def opt_poly_deg_final_dict \
        (X_array:      np.ndarray,
         y_array:      np.ndarray,
         results_list: list,
         cnds_list:    list,
         prec:         int   = 6,
         alpha:        float = 0.05) \
-> dict:

    best_dict = max(cnds_list, key = lambda r: r['combined_score'])


    best_pipeline \
        = Pipeline \
            ([('poly',  PolynomialFeatures \
                           (degree       = best_dict['degree'], 
                            include_bias = True)),
              ('model', LinearRegression())])

    best_pipeline.fit(X_array, y_array)


    tmp_coeff_list = best_pipeline.named_steps['model'].coef_.tolist()


    coeff_list     = [x for x in tmp_coeff_list]

    if len(coeff_list) > 1: coeff_list = coeff_list[1:]

    coeff_list     = [f'{x:.2e}' for x in coeff_list[::-1]]


    intercept_flt  = best_pipeline.named_steps['model'].intercept_

    intercept      = f'{intercept_flt:.2e}'


    degree1_dict   = next(r for r in results_list if r['degree'] == 1)

    lin_adq_bool \
        = round((best_dict['cv_r2'] - degree1_dict['cv_r2']), prec) < round(alpha, prec)


    final_dict \
        = {'best_degree':         best_dict['degree'],
           'coefficients':        coeff_list,
           'intercept':           intercept,
           'train_r2':            round(float(best_dict['train_r2']), prec),
           'cv_r2':               round(float(best_dict['cv_r2']), prec),
           'cv_r2_std':           round(float(best_dict['cv_r2_std']), prec),
           'aic':                 round(float(best_dict['aic']), prec),
           'linearity_adequate':  lin_adq_bool}

    return final_dict


# In[93]:


#*******************************************************************************************
 #
 #  Function Name:  opt_poly_degree
 #
 #  Function Description:
 #      This function finds the optimal polynomial degree for correlation between two time 
 #      series using a combination of AIC, cross-validated R², and overfitting detection.
 #
 #
 #  Return Type: integer, dictionary, dictionary, dataframe
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  object         X_obj            The parameter is the x-values object.
 #  object         y_obj            The parameter is the y-values object.
 #  integer        max_degree       The parameter is the maximum polynomial degree.
 #  integer        cv_folds         The parameter is the number of cross-validation folds.
 #  float          aic_wgt          The parameter is the weight given to AIC score in 
 #                                  combined ranking.
 #  float          cv_wgt           The parameter is the weight given to CV R² in combined 
 #                                  ranking.
 #  float          ovrft_r2_gp      The parameter is the maximum allowed gap between train 
 #                                  and CV R².
 #  integer        min_smpls_per_prm
 #                                  The parameter is the minimum data points per model 
 #                                  parameter.
 #  integer        prec             The parameter is the output number precision.
 #  float          alpha            The parameter is the p-value threshold.
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def opt_poly_degree \
        (X_obj:                 object,
         y_obj:                 object,
         max_degree:            int   = 10,
         cv_folds:              int   = 5,
         aic_wgt:               float = 0.5,
         cv_wgt:                float = 0.5,
         ovrft_r2_gp:           float = 0.15,
         min_smpls_per_prm:     int   = 3,
         prec:                  int   = 6,
         alpha:                 float = 0.05) \
-> tuple[int, dict, dict, pd.DataFrame]:

    X_array, X_bool = dtypesx.check_data_dtype_array(X_obj)

    y_array, y_bool = dtypesx.check_data_dtype_array(y_obj)

    if X_bool == False or y_bool == False: return X_array


    X_array          = X_array.reshape(-1, 1)

    n_int            = len(y_array)


    max_feasible_int = max(1, n_int // min_smpls_per_prm - 1)

    max_degree       = min(max_degree, max_feasible_int)

    cv_folds         = min(cv_folds, n_int)


    results_list \
        = opt_poly_deg_rslts_list \
            (X_array, y_array, n_int,
             max_degree, cv_folds,
             ovrft_r2_gp, prec)

    cnds_list \
        = opt_poly_deg_cnd_list \
            (results_list,
             aic_wgt, cv_wgt)

    final_dict \
        = opt_poly_deg_final_dict \
            (X_array, y_array,
             results_list, cnds_list,
             prec, alpha)


    cmb_score_dict   = {}

    for rslt_dict in results_list:

        cmb_score_dict[rslt_dict['degree']] = rslt_dict['combined_score']


    results_df       = pd.DataFrame(results_list)

    results_df \
        = results_df \
            [['degree', 'train_r2', 'cv_r2', 'cv_r2_std', 'cv_norm', 
              'aic', 'aic_norm', 'overfit', 'combined_score']]


    return \
        final_dict['best_degree'], \
        cmb_score_dict, \
        final_dict, \
        results_df


# In[94]:


#*******************************************************************************************
 #
 #  Function Name:  calc_single_corr
 #
 #  Function Description:
 #      This function returns the correlation coefficient for a single window.
 #
 #
 #  Return Type: float
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  array          X_array          The parameter is the x-values array.
 #  array          y_array          The parameter is the y-values array.
 #  string         method           The parameter is the correlation method.   
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def calc_single_corr \
        (X_array: np.ndarray,
         y_array: np.ndarray,
         method:  str) \
-> float:

    method = dtypesx.strip_rmv_nmbr_space_case(method, case = 'lower')


    if   method == 'pearson':  r, _ = pearsonr(X_array, y_array)

    elif method == 'spearman': r, _ = spearmanr(X_array, y_array)

    elif method == 'kendall':  r, _ = kendalltau(X_array, y_array)

    else:                      r    = None


    return r


# In[95]:


#*******************************************************************************************
 #
 #  Function Name:  calc_single_pval
 #
 #  Function Description:
 #      This function returns the p-value for a single window correlation.
 #
 #
 #  Return Type: float
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  array          X_array          The parameter is the x-values array.
 #  array          y_array          The parameter is the y-values array.
 #  string         method           The parameter is the correlation method.   
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def calc_single_pval \
        (X_array: np.ndarray,
         y_array: np.ndarray,
         method:  str) \
-> float:

    method = dtypesx.strip_rmv_nmbr_space_case(method, case = 'lower')


    if   method == 'pearson':  _, p = pearsonr(X_array, y_array)

    elif method == 'spearman': _, p = spearmanr(X_array, y_array)

    elif method == 'kendall':  _, p = kendalltau(X_array, y_array)

    else:                         p = None


    return p


# In[96]:


#*******************************************************************************************
 #
 #  Function Name:  calc_rolling_corr
 #
 #  Function Description:
 #      This function returns the rolling correlation series for a given window size.
 #
 #
 #  Return Type: array
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  array          X_array          The parameter is the x-values array.
 #  array          y_array          The parameter is the y-values array.
 #  int            window           The parameter is the window size.
 #  string         method           The parameter is the correlation method.   
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def calc_rolling_corr \
       (X_array: np.ndarray,
        y_array: np.ndarray,
        window:  int,
        method:  str) \
-> np.ndarray:

    method = dtypesx.strip_rmv_nmbr_space_case(method, case = 'lower')

    roll_corr_array \
        = np.asarray \
            ([calc_single_corr(X_array[i - window:i], y_array[i - window:i], method)
              for i in range(window, len(X_array) + 1)])

    return roll_corr_array


# In[97]:


#*******************************************************************************************
 #
 #  Function Name:  calc_rolling_pvals
 #
 #  Function Description:
 #      This function returns the rolling p-value series for a given window size.
 #
 #
 #  Return Type: array
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  array          X_array          The parameter is the x-values array.
 #  array          y_array          The parameter is the y-values array.
 #  int            window           The parameter is the window size.
 #  string         method           The parameter is the correlation method.   
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def calc_rolling_pvals \
        (X_array: np.ndarray,
         y_array: np.ndarray,
         window:  int,
         method:  str) \
-> np.ndarray:

    roll_array \
        = np.asarray \
            ([calc_single_pval(X_array[i - window:i], y_array[i - window:i], method)
              for i in range(window, len(X_array) + 1)])

    return roll_array


# In[98]:


#*******************************************************************************************
 #
 #  Function Name:  calc_pct_significant
 #
 #  Function Description:
 #      This function returns the fraction of rolling windows with a significant 
 #      correlation.
 #
 #
 #  Return Type: float
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  array          X_array          The parameter is the x-values array.
 #  array          y_array          The parameter is the y-values array.
 #  int            window           The parameter is the window size.
 #  string         method           The parameter is the correlation method.
 #  float          alpha            The parameter is the p-value threshold.
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def calc_pct_significant \
        (X_array: np.ndarray,
         y_array: np.ndarray,
         window:  int,
         method:  str,
         alpha:   float = 0.05) \
-> float:

    pvals_array = calc_rolling_pvals(X_array, y_array, window, method)

    pct_sig_flt = float(np.mean(pvals_array < alpha))

    return pct_sig_flt


# In[99]:


#*******************************************************************************************
 #
 #  Function Name:  calc_ac1
 #
 #  Function Description:
 #      This function returns the lag-1 autocorrelation of a rolling correlation series
 #      (returns 0.0 if the series is too short). 
 #
 #
 #  Return Type: float
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  array          rc_array         The parameter is the rolling correlation array.
 #  int            min_window       The parameter is the minimum window size.
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def calc_ac1 \
        (rc_array:   np.ndarray,
         min_window: int = 3) \
-> float:

    if len(rc_array) < min_window: return 0.0

    else: return np.corrcoef(rc_array[:-1], rc_array[1:])[0, 1]


# In[100]:


#*******************************************************************************************
 #
 #  Function Name:  calc_ac1_penalty
 #
 #  Function Description:
 #      This function penalises lag-1 autocorrelation outside the target range [0.3, 0.85].
 #
 #      Below 0.3 the window is too small (noisy).
 #      Above 0.85 the window is too large (over-smoothed).
 #
 #
 #  Return Type: float
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  float          ac1              The parameter is the lag-1 autocorrelation.
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def calc_ac1_penalty(ac1: float) -> float: return max(0.0, ac1 - 0.85) + max(0.0, 0.3 - ac1)


# In[101]:


#*******************************************************************************************
 #
 #  Function Name:  calc_rolling_pvals
 #
 #  Function Description:
 #      This function returns (cv_mean, cv_std) — the mean and std of mean absolute
 #      rolling correlation across TimeSeriesSplit folds.
 #
 #
 #  Return Type: float, float
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  array          X_array          The parameter is the x-values array.
 #  array          y_array          The parameter is the y-values array.
 #  int            window           The parameter is the window size.
 #  string         method           The parameter is the correlation method.   
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def calc_cv_stats \
        (X_array: np.ndarray,
         y_array: np.ndarray,
         tscv:    TimeSeriesSplit,
         window:  int,
         method:  str) \
-> tuple[float, float]:

    fold_means_array     = np.asarray([], dtype = float)

    for _, test_idx in tscv.split(X_array):

        if len(test_idx) < window: continue


        rc_fold_array    = calc_rolling_corr(X_array[test_idx], y_array[test_idx], window, method)

        fold_means_array = np.append(fold_means_array, np.mean(np.abs(rc_fold_array)))


    if list(fold_means_array): return np.mean(fold_means_array), np.std(fold_means_array)

    else: return 0.0, 1.0


# In[102]:


#*******************************************************************************************
 #
 #  Function Name:  is_window_feasible
 #
 #  Function Description:
 #      This function returns True if all CV folds are large enough for the window and
 #      requires every fold to have at least window * min_factor points.
 #
 #
 #  Return Type: boolean
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  int            window           The parameter is the window size.
 #  list[int]      fold_sizes       The parameter is a list of fold sizes.
 #  int            min_factor       The parameter is the minimum factor for feasibility.   
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def is_window_feasible \
        (window:      int,
         fold_sizes:  list[int],
         min_factor:  int = 2) \
-> bool:

    return min(fold_sizes) >= window * min_factor


# In[103]:


#*******************************************************************************************
 #
 #  Function Name:  get_fold_sizes
 #
 #  Function Description:
 #      This function returns a list of training fold sizes for a given TimeSeriesSplit.
 #
 #
 #  Return Type: list[int]
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  array          X_array          The parameter is the x-values array.
 #  TimeSeriesSplit         
 #                 tscv             The parameter is the time series split object.
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_fold_sizes \
        (X_array:    np.ndarray,
         tscv:       TimeSeriesSplit) \
-> list[int]:

    return [len(train_idx) for train_idx, _ in tscv.split(X_array)]


# In[104]:


#*******************************************************************************************
 #
 #  Function Name:  normalize_array
 #
 #  Function Description:
 #      This function normalises an array to [0, 1]. If invert = True, lower values score 
 #      higher (e.g. std, penalty).
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
 #  bool           invert           The parameter is the inversion indicator.
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def normalize_array \
        (data_array: np.ndarray,
         invert:     bool = False) \
-> np.ndarray:

    lo_flt     = np.min(data_array)

    hi_flt     = np.max(data_array)


    rng_flt    = hi_flt - lo_flt + 1e-10


    norm_array = (data_array - lo_flt) / rng_flt

    norm_array = 1 - norm_array if invert else norm_array


    return norm_array.astype(float)


# In[105]:


#*******************************************************************************************
 #
 #  Function Name:  calc_scores
 #
 #  Function Description:
 #      This function normalises all scoring components across windows and computes
 #      a weighted combined score for each window.
 #
 #      Weights
 #      -------
 #      Mean absolute rolling r  : 0.25
 #      % windows significant    : 0.20
 #      Stability (low rc_std)   : 0.20
 #      CV mean absolute r       : 0.20
 #      CV consistency (low std) : 0.10
 #      AC1 penalty              : 0.05
 #
 #
 #  Return Type: list[dict]
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  list[dict]     results_list     The parameter is the results dictionary list.
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def calc_scores(results_list: list[dict]) -> list[dict]:

    rc_abs_norm_array  = normalize_array(np.asarray([r['rc_abs']      for r in results_list]), invert = False)

    pct_sig_norm_array = normalize_array(np.asarray([r['pct_sig']     for r in results_list]), invert = False)

    stability_array    = normalize_array(np.asarray([r['rc_std']      for r in results_list]), invert = True)

    cv_norm_array      = normalize_array(np.asarray([r['cv_mean']     for r in results_list]), invert = False)

    cv_con_norm_array  = normalize_array(np.asarray([r['cv_std']      for r in results_list]), invert = True)

    ac1_norm_array     = normalize_array(np.asarray([r['ac1_penalty'] for r in results_list]), invert = True)


    for i, r in enumerate(results_list):

        r['score'] \
            = (0.25 * np.nan_to_num(rc_abs_norm_array[i])  + \
               0.20 * np.nan_to_num(pct_sig_norm_array[i]) + \
               0.20 * np.nan_to_num(stability_array[i])    + \
               0.20 * np.nan_to_num(cv_norm_array[i])      + \
               0.10 * np.nan_to_num(cv_con_norm_array[i])  + \
               0.05 * np.nan_to_num(ac1_norm_array[i]))


    return results_list


# In[106]:


#*******************************************************************************************
 #
 #  Function Name:  build_window_record
 #
 #  Function Description:
 #      This function computes and returns all metrics for a single window size.
 #
 #
 #  Return Type: dict
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  array          X_array          The parameter is the x-values array.
 #  array          y_array          The parameter is the y-values array.
 #  TimeSeriesSplit         
 #                 tscv             The parameter is the time series split object.
 #  int            window           The parameter is the window size.
 #  string         method           The parameter is the correlation method.
 #  integer        prec             The parameter is the output number precision.
 #  float          alpha            The parameter is the p-value threshold.
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def build_window_record \
        (X_array:    np.ndarray,
         y_array:    np.ndarray,
         tscv:       TimeSeriesSplit,
         window:     int,
         min_window: int,
         method:     str,
         prec:       int   = 6,
         alpha:      float = 0.05) \
-> dict:

    rc_array       = calc_rolling_corr(X_array, y_array, window, method)

    rc_mean_flt    = np.mean(rc_array)

    rc_std_flt     = np.std(rc_array)

    rc_abs_flt     = abs(rc_mean_flt)


    is_stable_bool = round(rc_std_flt, prec) < round(alpha, prec)

    pct_sig_flt    = calc_pct_significant(X_array, y_array, window, method, alpha)


    ac1_flt        = calc_ac1(rc_array, min_window)

    ac1_pen_flt    = calc_ac1_penalty(ac1_flt)


    cv_mean_flt, cv_std_flt \
        = calc_cv_stats(X_array, y_array, tscv, window, method)


    wndw_dict \
        = {'window':      window,
           'rc_mean':     rc_mean_flt,
           'rc_abs':      rc_abs_flt,
           'rc_std':      rc_std_flt,
           'is_stable':   is_stable_bool,
           'pct_sig':     pct_sig_flt,
           'cv_mean':     cv_mean_flt,
           'cv_std':      cv_std_flt,
           'ac1':         ac1_flt,
           'ac1_penalty': ac1_pen_flt}

    return wndw_dict


# In[107]:


#*******************************************************************************************
 #
 #  Function Name:  opt_roll_wndw_rslts_df
 #
 #  Function Description:
 #      This function returns a dataframe from the results list
 #
 #
 #  Return Type: dataframe
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  list[dict]     results_list     The parameter is the results dictionary list.
 #  integer        prec             The parameter is the output number precision.
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def opt_roll_wndw_rslts_df \
        (results_list: list,
         prec:         int = 6) \
-> pd.DataFrame:

    rslts_df = pd.DataFrame({})

    for rslt_dict in results_list:

        rslts_df.loc[rslt_dict['window'], 'rc_mean'] \
            = float(round(rslt_dict['rc_mean'],     prec))

        rslts_df.loc[rslt_dict['window'], 'rc_std'] \
            = float(round(rslt_dict['rc_std'],      prec))

        rslts_df.loc[rslt_dict['window'], 'pct_sig'] \
            = float(round(rslt_dict['pct_sig'],     prec))

        rslts_df.loc[rslt_dict['window'], 'cv_mean'] \
            = float(round(rslt_dict['cv_mean'],     prec))

        rslts_df.loc[rslt_dict['window'], 'cv_std'] \
            = float(round(rslt_dict['cv_std'],      prec))

        rslts_df.loc[rslt_dict['window'], 'is_stable'] \
            = bool(rslt_dict['is_stable'])

        rslts_df.loc[rslt_dict['window'], 'ac1'] \
            = float(round(rslt_dict['ac1'],         prec))

        rslts_df.loc[rslt_dict['window'], 'ac1_penalty'] \
            = float(round(rslt_dict['ac1_penalty'], prec))

        rslts_df.loc[rslt_dict['window'], 'score'] \
            = float(round(rslt_dict['score'],       prec))

    rslts_df.index.name = 'window'

    return rslts_df


# In[108]:


#*******************************************************************************************
 #
 #  Function Name:  find_optimal_rolling_window
 #
 #  Function Description:
 #      This function finds the optimal window size for a rolling correlation between
 #      two time series by balancing correlation stability, statistical significance,
 #      and temporal consistency across cross-validated folds.
 #
 #
 #  Return Type: integer, dictionary, dataframe
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  object          X_obj           The parameter is the x-values object.
 #  object          y_obj           The parameter is the y-values object.
 #  int             min_window      The parameter is the minimum window size.
 #  int             max_window      The parameter is the maximum window size.
 #  int             n_splits        The parameter is the number of TimeSeriesSplit folds.
 #  string          method          The parameter is the correlation method.
 #  int             min_factor      The parameter is the minimum factor for feasibility. 
 #  integer         prec            The parameter is the output number precision.
 #  float           alpha           The parameter is the p-value threshold.
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def find_optimal_rolling_window \
        (X_obj:           object,
         y_obj:           object,
         min_window:      int   = 5,
         max_window:      int   = None,
         n_splits:        int   = 5,
         method:          str   = 'pearson',
         min_factor:      int   = 2,
         prec:            int   = 6,
         alpha:           float = 0.05) \
-> tuple[int, dict, pd.DataFrame]:

    X_array, X_bool = dtypesx.check_data_dtype_array(X_obj)

    y_array, y_bool = dtypesx.check_data_dtype_array(y_obj)

    if X_bool == False or y_bool == False: return X_array


    min_window      = max(min_window, 3)


    if max_window is None: max_window = len(X_array) // 4

    else:                  max_window = min(max_window, len(X_array) // 2)


    tscv            = TimeSeriesSplit(n_splits = n_splits)

    fold_sizes_list = get_fold_sizes(X_array, tscv)


    results_list    = []

    for w in range(min_window, max_window + 1):

        if not is_window_feasible(w, fold_sizes_list, min_factor = min_factor): continue

        record_dict \
            = build_window_record \
                (X_array, y_array, tscv, w, min_window, method, prec, alpha)

        if round(record_dict['cv_mean'], prec) == 0 \
            or round(record_dict['cv_std'], prec) == 1: continue

        results_list.append(record_dict)


    results_list    = calc_scores(results_list)

    results_df      = opt_roll_wndw_rslts_df(results_list, prec)


    best_dict       = max(results_list, key = lambda r: r['score'])

    opt_wndw        = best_dict['window']


    final_best_dict \
        = {'optimal_window':   int(opt_wndw),
           'rc_mean':          float(round(best_dict['rc_mean'],         prec)),
           'rc_std':           float(round(best_dict['rc_std'],          prec)),
           'pct_significant%': float(round(best_dict['pct_sig'] * 100.0, prec)),
           'cv_mean':          float(round(best_dict['cv_mean'],         prec)),
           'cv_std':           float(round(best_dict['cv_std'],          prec)),
           'is_stable':        bool(best_dict['is_stable']),
           'ac1':              float(round(best_dict['ac1'],             prec)),
           'ac1_penalty':      float(round(best_dict['ac1_penalty'],     prec)),
           'score%':           float(round(best_dict['score'] * 100.0,   prec))}

    return opt_wndw, final_best_dict, results_df


# In[109]:


#*******************************************************************************************
 #
 #  Function Name:  calc_rolling_corr_minp
 #
 #  Function Description:
 #      This function returns the rolling correlation series, and windows shorter than 
 #      min_periods yield np.nan.
 #
 #
 #  Return Type: array
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  array          X_array          The parameter is the x-values array.
 #  array          y_array          The parameter is the y-values array.
 #  int            window           The parameter is the window size.
 #  int            min_periods      The parameter is the minimum number of periods.
 #  string         method           The parameter is the correlation method.   
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def calc_rolling_corr_minp \
        (X_array:     np.ndarray,
         y_array:     np.ndarray,
         window:      int,
         min_periods: int,
         method:      str) \
-> np.ndarray:

    n_int         = len(X_array)

    result_array  = np.full(n_int, np.nan)

    for i in range(n_int):

        start_int = max(0, i - window + 1)

        xi_array, yi_array \
            = X_array[start_int:i + 1], y_array[start_int:i + 1]

        if len(xi_array) >= min_periods:

            result_array[i] = calc_single_corr(xi_array, yi_array, method)

    return result_array


# In[110]:


#*******************************************************************************************
 #
 #  Function Name:  calc_rolling_pvals_minp
 #
 #  Function Description:
 #      This function returns the rolling p-value series, and windows shorter than 
 #      min_periods yield np.nan.
 #
 #
 #  Return Type: array
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  array          X_array          The parameter is the x-values array.
 #  array          y_array          The parameter is the y-values array.
 #  int            window           The parameter is the window size.
 #  int            min_periods      The parameter is the minimum number of periods.
 #  string         method           The parameter is the correlation method.   
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def calc_rolling_pvals_minp \
        (X_array:     np.ndarray,
         y_array:     np.ndarray,
         window:      int,
         min_periods: int,
         method:      str) \
-> np.ndarray:

    n_int         = len(X_array)

    result_array  = np.full(n_int, np.nan)

    for i in range(n_int):

        start_int = max(0, i - window + 1)

        xi_array, yi_array \
            = X_array[start_int:i + 1], y_array[start_int:i + 1]

        if len(xi_array) >= min_periods:

            result_array[i] = calc_single_pval(xi_array, yi_array, method)

    return result_array


# In[111]:


#*******************************************************************************************
 #
 #  Function Name:  calc_nan_fraction
 #
 #  Function Description:
 #      This function returns the fraction of NaN values in a rolling correlation series.
 #      High NaN fraction means min_periods is too large for the window.
 #
 #
 #  Return Type: float
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  array          rc_array          The parameter is the rolling correlation array.
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def calc_nan_fraction(rc_array: np.ndarray) -> float:

    frac_flt = np.mean(np.isnan(rc_array))

    return frac_flt


# In[112]:


#*******************************************************************************************
 #
 #  Function Name:  calc_valid_rc_stats
 #
 #  Function Description:
 #      This function returns (mean, std, abs_mean) of the non-NaN rolling correlations.
 #      The function returns (0, 1, 0) if no valid values exist.
 #
 #
 #  Return Type: float, float, float
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  array          rc_array          The parameter is the rolling correlation array.
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def calc_valid_rc_stats(rc_array: np.ndarray) -> tuple[float, float, float]:

    valid_array = rc_array[~np.isnan(rc_array)]

    if len(valid_array) == 0: return 0.0, 1.0, 0.0

    else: return np.mean(valid_array), np.std(valid_array), np.mean(np.abs(valid_array))


# In[113]:


#*******************************************************************************************
 #
 #  Function Name:  calc_pct_sig_minp
 #
 #  Function Description:
 #      This function returns the fraction of valid rolling windows with significant 
 #      correlation.
 #
 #
 #  Return Type: float
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  array          X_array          The parameter is the x-values array.
 #  array          y_array          The parameter is the y-values array.
 #  int            window           The parameter is the window size.
 #  int            min_periods      The parameter is the minimum number of periods.
 #  string         method           The parameter is the correlation method.
 #  float          alpha            The parameter is the p-value threshold.
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def calc_pct_sig_minp \
        (X_array:     np.ndarray,
         y_array:     np.ndarray,
         window:      int,
         min_periods: int,
         method:      str,
         alpha:       float = 0.05) \
-> float:

    pvals_array = calc_rolling_pvals_minp(X_array, y_array, window, min_periods, method)

    valid_array = pvals_array[~np.isnan(pvals_array)]


    if len(valid_array) == 0: return 0.0

    else: return np.mean(valid_array < alpha)


# In[114]:


#*******************************************************************************************
 #
 #  Function Name:  calc_warmup_cost
 #
 #  Function Description:
 #      This function returns the fractional data loss due to the warmup period.
 #      A higher min_periods discards more of the series before the first valid 
 #      correlation can be computed.
 #
 #
 #  Return Type: float
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  int            min_periods      The parameter is the minimum number of periods.
 #  int            n                The parameter is the number of data points.
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def calc_warmup_cost(min_periods: int, n: int) -> float: return min_periods / n


# In[115]:


#*******************************************************************************************
 #
 #  Function Name:  calc_stability_ratio
 #
 #  Function Description:
 #      This function returns the ratio of std to abs mean of valid rolling correlations.
 #      Lower is more stable. Returns 1.0 if abs_mean is near zero.
 #
 #
 #  Return Type: float
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  array          rc_array          The parameter is the rolling correlation array.
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def calc_stability_ratio(rc_array: np.ndarray) -> float:

    valid_array  = rc_array[~np.isnan(rc_array)]

    if len(valid_array) == 0: return 1.0


    abs_mean_flt = np.mean(np.abs(valid_array))

    std_flt      = np.std(valid_array)


    if abs_mean_flt < 1e-10: return 1.0

    else: return std_flt / abs_mean_flt


# In[116]:


#*******************************************************************************************
 #
 #  Function Name:  calc_convergence_index
 #
 #  Function Description:
 #      This function measures how quickly the rolling correlation stabilises after the
 #      warmup period by comparing the standard deviation of the first third of valid 
 #      values to the standard deviation of the last third. A value close to 1.0 means 
 #      the series stabilized quickly. Returns 0.0 if insufficient valid data.
 #
 #
 #  Return Type: float
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  array          rc_array          The parameter is the rolling correlation array.
 #  integer        min_thrhld        The parameter is the minimum threshold for data.
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def calc_convergence_index(rc_array: np.ndarray, min_thrhld: int = 6) -> float:

    valid_array   = rc_array[~np.isnan(rc_array)]

    if len(valid_array) <  min_thrhld: return 0.0


    third_int     = len(valid_array) // 3


    std_early_flt = np.std(valid_array[:third_int])

    std_late_flt  = np.std(valid_array[-third_int:])


    denom_flt     = std_early_flt + 1e-10


    ratio_flt     = std_late_flt / denom_flt

    conv_idx_flt  = np.clip(ratio_flt, 0.0, 1.0)


    return conv_idx_flt


# In[117]:


#*******************************************************************************************
 #
 #  Function Name:  calc_cv_stats_minp
 #
 #  Function Description:
 #      This function returns (cv_mean, cv_std) of mean absolute rolling correlation
 #      across TimeSeriesSplit folds.
 #
 #
 #  Return Type: float, float
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  array          X_array          The parameter is the x-values array.
 #  array          y_array          The parameter is the y-values array.
 #  TimeSeriesSplit         
 #                 tscv             The parameter is the time series split object.
 #  int            window           The parameter is the window size.
 #  int            min_periods      The parameter is the minimum number of periods.
 #  string         method           The parameter is the correlation method.
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def calc_cv_stats_minp \
        (X_array:     np.ndarray,
         y_array:     np.ndarray,
         tscv:        TimeSeriesSplit,
         window:      int,
         min_periods: int,
         method:      str) \
-> tuple[float, float]:

    fold_means_array = np.asarray([], dtype = float)

    for _, test_idx in tscv.split(X_array):

        if len(test_idx) < min_periods: continue

        rc_fold_array \
            = calc_rolling_corr_minp \
                (X_array[test_idx], 
                 y_array[test_idx], 
                 window, 
                 min_periods, 
                 method)

        valid_array  = rc_fold_array[~np.isnan(rc_fold_array)]

        if len(valid_array) > 0: 

            fold_means_array \
                = np.append(fold_means_array, np.mean(np.abs(valid_array)))


    if not list(fold_means_array): return 0.0, 1.0

    else: return np.mean(fold_means_array), np.std(fold_means_array)


# In[118]:


#*******************************************************************************************
 #
 #  Function Name:  get_cv_fold_sizes_minp
 #
 #  Function Description:
 #      This function returns a list of test fold sizes for a given TimeSeriesSplit.
 #
 #
 #  Return Type: list[int]
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  array          X_array          The parameter is the x-values array.
 #  TimeSeriesSplit         
 #                 tscv             The parameter is the time series split object.
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def get_cv_fold_sizes_minp \
        (X_array:     np.ndarray,
         tscv:        TimeSeriesSplit) \
-> list[int]:

    tst_fld_sz_list = [len(test_idx) for _, test_idx in tscv.split(X_array)]

    return tst_fld_sz_list


# In[119]:


#*******************************************************************************************
 #
 #  Function Name:  is_minp_feasible
 #
 #  Function Description:
 #      This function returns True if min_periods is valid:
 #
 #      - Must be at least 3 (minimum for a meaningful correlation)
 #      - Must not exceed the window size
 #      - At least one CV fold must be large enough
 #
 #
 #  Return Type: boolean
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  int            min_periods      The parameter is the minimum number of periods.
 #  int            window           The parameter is the window size.
 #  list[int]      fold_sizes       The parameter is the fold sizes.
 #  integer        min_thrhld       The parameter is the minimum threshold for data.
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def is_minp_feasible \
        (min_periods: int,
         window:      int,
         fold_sizes:  list[int],
         min_thrhld:  int = 3) \
-> bool:

    if    min_periods     < min_thrhld:  return False

    elif  min_periods     > window:      return False

    elif  max(fold_sizes) < min_periods: return False

    else: return True


# In[120]:


#*******************************************************************************************
 #
 #  Function Name:  build_minp_record
 #
 #  Function Description:
 #      This function computes and returns all metrics for a single min_periods candidate.
 #
 #
 #  Return Type: dict
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  array          X_array          The parameter is the x-values array.
 #  array          y_array          The parameter is the y-values array.
 #  TimeSeriesSplit         
 #                 tscv             The parameter is the time series split object.
 #  int            window           The parameter is the window size.
 #  int            min_periods      The parameter is the minimum number of periods.
 #  integer        min_thrhld       The parameter is the minimum threshold for data.
 #  string         method           The parameter is the correlation method.
 #  float          alpha            The parameter is the p-value threshold.
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def build_minp_record \
        (X_array:     np.ndarray,
         y_array:     np.ndarray,
         tscv:        TimeSeriesSplit,
         window:      int,
         min_periods: int,
         min_thrhld:  int,
         method:      str,
         alpha:       float = 0.05) \
-> dict:

    n_int           = len(X_array)

    rc_array        = calc_rolling_corr_minp(X_array, y_array, window, min_periods, method)

    nan_frac_flt    = calc_nan_fraction(rc_array)

    pct_sig_flt     = calc_pct_sig_minp(X_array, y_array, window, min_periods, method, alpha)

    warmup_cost_flt = calc_warmup_cost(min_periods, n_int)

    stability_flt   = calc_stability_ratio(rc_array)

    convergence_flt = calc_convergence_index(rc_array, min_thrhld)


    cv_mean_flt, cv_std_flt \
        = calc_cv_stats_minp(X_array, y_array, tscv, window, min_periods, method)

    rc_mean_flt, rc_std_flt, rc_abs_flt \
        = calc_valid_rc_stats(rc_array)


    result_dict \
        = {'min_periods':  min_periods,
           'rc_mean':      rc_mean_flt,
           'rc_abs':       rc_abs_flt,
           'rc_std':       rc_std_flt,
           'nan_frac':     nan_frac_flt,
           'pct_sig':      pct_sig_flt,
           'warmup_cost':  warmup_cost_flt,
           'stability':    stability_flt,
           'convergence':  convergence_flt,
           'cv_mean':      cv_mean_flt,
           'cv_std':       cv_std_flt}

    return result_dict


# In[121]:


#*******************************************************************************************
 #
 #  Function Name:  calc_scores_minp
 #
 #  Function Description:
 #      This function normalises all scoring components and computes a weighted combined
 #      score for each min_periods candidate.
 #
 #      Weights
 #      -------
 #      CV mean absolute r       : 0.25  generalisation across folds
 #      % windows significant    : 0.20  reliability of significance
 #      Stability ratio          : 0.20  consistency of rolling r
 #      Warmup cost              : 0.15  data efficiency
 #      Convergence index        : 0.10  speed of stabilisation
 #      NaN fraction             : 0.05  coverage of the series
 #      CV consistency           : 0.05  fold-to-fold cv stability
 #
 #
 #  Return Type: list[dict]
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  list[dict]     results_list     The parameter is the results dictionary list.
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def calc_scores_minp(results_list: list[dict]) -> list[dict]:

    rc_abs_norm_array \
        = normalize_array(np.asarray([r['rc_abs']      for r in results_list]), invert = False)

    pct_sig_norm_array \
        = normalize_array(np.asarray([r['pct_sig']     for r in results_list]), invert = False)

    stability_norm_array \
        = normalize_array(np.asarray([r['stability']   for r in results_list]), invert = True)

    warmup_norm_array \
        = normalize_array(np.asarray([r['warmup_cost'] for r in results_list]), invert = True)

    conv_norm_array \
        = normalize_array(np.asarray([r['convergence'] for r in results_list]), invert = False)

    nan_norm_array \
        = normalize_array(np.asarray([r['nan_frac']    for r in results_list]), invert = True)

    cv_norm_array \
        = normalize_array(np.asarray([r['cv_mean']     for r in results_list]), invert = False)

    cv_con_norm_array \
        = normalize_array(np.asarray([r['cv_std']      for r in results_list]), invert = True)


    for i, r in enumerate(results_list):

        r['score'] \
            = (0.25 * np.nan_to_num(cv_norm_array[i])        + \
               0.20 * np.nan_to_num(pct_sig_norm_array[i])   + \
               0.20 * np.nan_to_num(stability_norm_array[i]) + \
               0.15 * np.nan_to_num(warmup_norm_array[i])    + \
               0.10 * np.nan_to_num(conv_norm_array[i])      + \
               0.05 * np.nan_to_num(nan_norm_array[i])       + \
               0.05 * np.nan_to_num(cv_con_norm_array[i]))

    return results_list


# In[122]:


#*******************************************************************************************
 #
 #  Function Name:  opt_min_prd_rslts_df
 #
 #  Function Description:
 #      This function returns a dataframe from the results list
 #
 #
 #  Return Type: dataframe
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  list[dict]     results_list     The parameter is the results dictionary list.
 #  integer        prec             The parameter is the output number precision.
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def opt_min_prd_rslts_df \
        (results_list: list,
         prec:         int = 6) \
-> pd.DataFrame:

    rslts_df = pd.DataFrame({})

    for rslt_dict in results_list:

        rslts_df.loc[rslt_dict['min_periods'], 'rc_mean'] \
            = float(round(rslt_dict['rc_mean'],     prec))

        rslts_df.loc[rslt_dict['min_periods'], 'rc_std'] \
            = float(round(rslt_dict['rc_std'],      prec))

        rslts_df.loc[rslt_dict['min_periods'], 'nan_frac'] \
            = float(round(rslt_dict['nan_frac'],    prec))

        rslts_df.loc[rslt_dict['min_periods'], 'pct_sig'] \
            = float(round(rslt_dict['pct_sig'],     prec))

        rslts_df.loc[rslt_dict['min_periods'], 'warmup_cost'] \
            = float(round(rslt_dict['warmup_cost'], prec))

        rslts_df.loc[rslt_dict['min_periods'], 'stability'] \
            = float(round(rslt_dict['stability'],   prec))

        rslts_df.loc[rslt_dict['min_periods'], 'convergence'] \
            = float(round(rslt_dict['convergence'], prec))

        rslts_df.loc[rslt_dict['min_periods'], 'cv_mean'] \
            = float(round(rslt_dict['cv_mean'],     prec))

        rslts_df.loc[rslt_dict['min_periods'], 'cv_std'] \
            = float(round(rslt_dict['cv_std'],      prec))

        rslts_df.loc[rslt_dict['min_periods'], 'score'] \
            = float(round(rslt_dict['score'],       prec))

    rslts_df.index.name = 'min_periods'

    return rslts_df


# In[123]:


#*******************************************************************************************
 #
 #  Function Name:  find_optimal_min_periods
 #
 #  Function Description:
 #      This function finds the optimal min_periods for a rolling correlation between two
 #      time series, given a fixed window size.
 #
 #      min_periods controls how many observations are required before the
 #      first valid correlation is computed. Too low → noisy early estimates.
 #      Too high → excessive data loss during warmup.
 #
 #
 #  Return Type: dictionary
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  object         X_obj            The parameter is the x-values object.
 #  object         y_obj            The parameter is the y-values object.
 #  int            window           The parameter is the window size.
 #  integer        n_splits         The parameter is the number of CV folds.
 #  string         method           The parameter is the correlation method.
 #  integer        min_thrhld       The parameter is the minimum threshold for data.
 #  bool           pct_bool         The parameter is an indicator of whether certain 
 #                                  results are represented as a percentage rather than 
 #                                  a decimal.
 #  integer        prec             The parameter is the output number precision.
 #  float          alpha            The parameter is the p-value threshold.
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def find_optimal_min_periods \
        (X_obj:      object,
         y_obj:      object,
         window:     int,
         n_splits:   int   = 5,
         method:     str   = 'pearson',
         min_thrhld: int   = 3,
         pct_bool:   bool  = True,
         prec:       int   = 6,
         alpha:      float = 0.05) \
-> tuple[int, dict, pd.DataFrame]:

    X_array, X_bool = dtypesx.check_data_dtype_array(X_obj)

    y_array, y_bool = dtypesx.check_data_dtype_array(y_obj)

    if X_bool == False or y_bool == False: return X_array


    n_int           = len(X_array)


    tscv            = TimeSeriesSplit(n_splits = n_splits)

    fold_sizes_list = get_cv_fold_sizes_minp(X_array, tscv)


    results_list    = []

    for mp in range(min_thrhld, window + 1):

        if not is_minp_feasible(mp, window, fold_sizes_list, min_thrhld): continue


        record_dict \
            = build_minp_record \
                (X_array, 
                 y_array, 
                 tscv        = tscv, 
                 window      = window, 
                 min_periods = mp,
                 min_thrhld  = min_thrhld,
                 method      = method,
                 alpha       = alpha)

        results_list.append(record_dict)


    results_list    = calc_scores_minp(results_list)

    results_df      = opt_min_prd_rslts_df(results_list, prec)


    best_dict       = max(results_list, key = lambda r: r['score'])

    min_prd_int     = best_dict['min_periods']


    if pct_bool: fct_flt = 100.0

    else:        fct_flt = 1.0


    final_dict \
        = {'min_period':       int(min_prd_int),
           'window':           int(window),
           'rc_mean':          float(round(best_dict['rc_mean'],           prec)),
           'rc_std':           float(round(best_dict['rc_std'],            prec)),
           'cv_mean':          float(round(best_dict['cv_mean'],           prec)),
           'cv_std':           float(round(best_dict['cv_std'],            prec)),
           'nan_fraction':     float(round(best_dict['nan_frac'],          prec)),
           'pct_significant%': float(round(best_dict['pct_sig'] * fct_flt, prec)),
           'warmup_cost':      float(round(best_dict['warmup_cost'],       prec)),
           'stability':        float(round(best_dict['stability'],         prec)),
           'convergence':      float(round(best_dict['convergence'],       prec)),
           'score%':           float(round(best_dict['score']   * fct_flt, prec))}


    return min_prd_int, final_dict, results_df


# In[124]:


#*******************************************************************************************
 #
 #  Function Name:  select_pct_mth_parms
 #
 #  Function Description:
 #      This function finds the parameters for the optimal method for numpy.percentile.
 #
 #
 #  Return Type: boolean, boolean, boolean, boolean, boolean, boolean
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  array          data_array       The parameter is the input data array.
 #  integer        small_smple_thrhld       
 #                                  The parameter is the threshld for a small sample.
 #  integer        shapiro_thrhld   The parameter is the Shapiro-Wills threshold.
 #  integer        prec             The parameter is the output number precision.
 #  float          alpha            The parameter is the p-value threshold.
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def select_pct_mth_parms \
        (data_array:         np.ndarray,
         small_smple_thrhld: int   = 30, 
         shapiro_thrhld:     int   = 5000,
         prec:               int   = 6,
         alpha:              float = 0.05) \
-> tuple[bool, bool, bool, bool, bool, bool]:

    data_array           = data_array[~np.isnan(data_array)]

    n_int                = len(data_array)


    _, p_norm_flt \
        = shapiro(data_array) \
            if n_int <= shapiro_thrhld \
            else normaltest(data_array)


    skewness_flt         = skew(data_array)

    kurtosis_flt         = kurtosis(data_array)


    is_norm_bool         = round(p_norm_flt, prec) > round(alpha, prec)

    is_int_bool          = np.all(data_array == data_array.astype(int))


    n_unq_int            = len(np.unique(data_array))

    has_many_ties_bool   = round((float(n_unq_int) / float(n_int)), prec) < round(0.5, prec)


    is_small_sample_bool = n_int < small_smple_thrhld

    is_skewed_bool       = abs(skewness_flt) > 1.0

    is_heavy_tail_bool   = kurtosis_flt > 3.0


    return \
        bool(is_norm_bool), \
        bool(is_int_bool), \
        bool(has_many_ties_bool), \
        bool(is_small_sample_bool), \
        bool(is_skewed_bool), \
        bool(is_heavy_tail_bool)


# In[125]:


#*******************************************************************************************
 #
 #  Function Name:  select_pct_mth
 #
 #  Function Description:
 #      This function finds the optimal method based for numpy.percentile on the boolean 
 #      parameters.
 #
 #
 #  Return Type: string
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  array          data_array       The parameter is the input data array.
 #  integer        small_smple_thrhld       
 #                                  The parameter is the threshld for a small sample.
 #  integer        shapiro_thrhld   The parameter is the Shapiro-Wills threshold.
 #  integer        prec             The parameter is the output number precision.
 #  float          alpha            The parameter is the p-value threshold.
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def select_pct_mth \
        (is_norm_bool:         bool,
         is_int_bool:          bool,
         has_many_ties_bool:   bool,
         is_small_sample_bool: bool,
         is_skewed_bool:       bool,
         is_heavy_tail_bool:   bool) \
-> str:

    if is_int_bool or has_many_ties_bool:

        if is_small_sample_bool: method = 'inverted_cdf'

        else:                    method = 'averaged_inverted_cdf'

    elif is_norm_bool and not is_skewed_bool and not is_heavy_tail_bool:

        if is_small_sample_bool: method = 'normal_unbiased'

        else:                    method = 'linear'

    elif is_skewed_bool or is_heavy_tail_bool:

        if is_small_sample_bool: method = 'hazen'

        else:                    method = 'median_unbiased'

    elif is_small_sample_bool:   method = 'weibull'

    else:                        method = 'interpolated_inverted_cdf'


    return method


# In[126]:


#*******************************************************************************************
 #
 #  Function Name:  select_percentile_method
 #
 #  Function Description:
 #      This function finds the optimal method for numpy.percentile.
 #
 #
 #  Return Type: string
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  object         input_obj        The parameter is the input object.
 #  integer        small_smple_thrhld       
 #                                  The parameter is the threshld for a small sample.
 #  integer        shapiro_thrhld   The parameter is the Shapiro-Wills threshold.
 #  integer        prec             The parameter is the output number precision.
 #  float          alpha            The parameter is the p-value threshold.
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def select_percentile_method \
        (input_obj:          object, 
         small_smple_thrhld: int   = 30,
         shapiro_thrhld:     int   = 5000,
         prec:               int   = 6,
         alpha:              float = 0.05) \
-> str:

    data_array, data_bool = dtypesx.check_data_dtype_array(input_obj)

    if data_bool == False: return data_array


    is_norm_bool, \
    is_int_bool, \
    has_many_ties_bool, \
    is_small_sample_bool, \
    is_skewed_bool, \
    is_heavy_tail_bool \
        = select_pct_mth_parms \
            (data_array,
             small_smple_thrhld = small_smple_thrhld, 
             shapiro_thrhld     = shapiro_thrhld,
             prec               = prec, 
             alpha              = alpha)


    method \
        = select_pct_mth \
            (is_norm_bool,
             is_int_bool,
             has_many_ties_bool,
             is_small_sample_bool,
             is_skewed_bool,
             is_heavy_tail_bool)

    return method


# In[127]:


#*******************************************************************************************
 #
 #  Function Name:  has_outliers
 #
 #  Function Description:
 #      This function determines if a series of data points has outliers.
 #
 #
 #  Return Type: boolean
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  dataframe      input_df         The parameter is the input dataframe.
 #  integer        small_smple_thrhld             
 #                                  The parameter is the small sample threshold.
 #  integer        shapiro_thrhld   The parameter is the Shapiro-Wills threshold.
 #  integer        prec             The parameter is the output number precision.
 #  float          alpha            The parameter is the p-value threshold.
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def has_outliers \
        (input_obj:          object, 
         small_smple_thrhld: int   = 30,
         shapiro_thrhld:     int   = 5000,
         prec:               int   = 6,
         alpha:              float = 0.05) \
-> bool:

    data_array, data_bool = dtypesx.check_data_dtype_array(input_obj)

    if data_bool == False: return data_array


    method \
        = select_percentile_method \
            (data_array, 
             small_smple_thrhld = small_smple_thrhld,
             shapiro_thrhld     = shapiro_thrhld,
             prec               = prec,
             alpha              = alpha)


    q1, q3        = np.percentile(data_array, [25, 75], method = method)

    iqr           = q3 - q1


    outliers_bool = np.any((data_array < q1 - 1.5 * iqr) | (data_array > q3 + 1.5 * iqr))

    return bool(outliers_bool)


# In[128]:


#*******************************************************************************************
 #
 #  Function Name:  find_opt_corr_method
 #
 #  Function Description:
 #      This function calculates the optimal method for a correlation.
 #
 #
 #  Return Type: string
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  object         X_obj            The parameter is the x-values object.
 #  object         y_obj            The parameter is the y-values object.
 #  integer        small_smple_thrhld             
 #                                  The parameter is the small sample threshold.
 #  integer        shapiro_thrhld   The parameter is the Shapiro-Wills threshold.
 #  integer        prec             The parameter is the output number precision.
 #  float          alpha            The parameter is the p-value threshold.
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def find_opt_corr_method \
        (X_obj:              object, 
         y_obj:              object,
         small_smple_thrhld: int   = 30,
         shapiro_thrhld:     int   = 5000,
         prec:               int   = 6,
         alpha:              float = 0.05) \
-> str:

    X_array, X_bool = dtypesx.check_data_dtype_array(X_obj)

    y_array, y_bool = dtypesx.check_data_dtype_array(y_obj)

    if X_bool == False or y_bool == False: return X_array


    n_int = len(X_array)

    if n_int <= 100:

        _, p_norm_x_flt = shapiro(X_array)

        _, p_norm_y_flt = shapiro(y_array)

    else:

        _, p_norm_x_flt = normaltest(X_array)

        _, p_norm_y_flt = normaltest(y_array)


    norm_alpha_flt      = alpha / 10.0 if n_int > 200 else alpha

    both_norm_bool \
        = (round(p_norm_x_flt, prec) > round(norm_alpha_flt, prec)
           and round(p_norm_y_flt, prec) > round(norm_alpha_flt, prec))


    skew_x_flt          = abs(skew(X_array))

    skew_y_flt          = abs(skew(y_array))

    kurt_x_flt          = abs(kurtosis(X_array))

    kurt_y_flt          = abs(kurtosis(y_array))


    prct_norm_bool \
        = (round(skew_x_flt, prec) < 1.0 and round(skew_y_flt, prec) < 1.0
           and round(kurt_x_flt, prec) < 3.0 and round(kurt_y_flt, prec) < 3.0)

    is_normal_bool \
        = both_norm_bool or (prct_norm_bool and n_int >= small_smple_thrhld)

    xhas_outliers_bool \
        = has_outliers \
            (X_array,
             small_smple_thrhld = small_smple_thrhld,
             shapiro_thrhld     = shapiro_thrhld,
             prec               = prec,
             alpha              = alpha) 

    yhas_outliers_bool \
        = has_outliers \
            (y_array,
             small_smple_thrhld = small_smple_thrhld,
             shapiro_thrhld     = shapiro_thrhld,
             prec               = prec,
             alpha              = alpha) 

    outlrs_prnt_bool     = xhas_outliers_bool or yhas_outliers_bool


    if is_normal_bool and not outlrs_prnt_bool: method = 'pearson'

    elif n_int >= small_smple_thrhld:           method = 'spearman'

    else:                                       method = 'kendall'


    return method


# In[129]:


#*******************************************************************************************
 #
 #  Function Name:  best_method_corr_matrix
 #
 #  Function Description:
 #      This function calculates the correlation matrix with optimal methods for each 
 #      correlation.
 #
 #
 #  Return Type: dataframe or dataframe, dataframe
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  dataframe      input_df         The parameter is the input dataframe.
 #  string         mode             The parameter is the output mode ('data', 'method', 
 #                                  'both').
 #  integer        small_smple_thrhld             
 #                                  The parameter is the small sample threshold.
 #  integer        shapiro_thrhld   The parameter is the Shapiro-Wills threshold.
 #  integer        prec             The parameter is the output number precision.
 #  float          alpha            The parameter is the p-value threshold.
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def best_method_corr_matrix \
        (input_df:           pd.DataFrame, 
         mode:               str   = 'data',
         index:              str   = 'series',
         small_smple_thrhld: int   = 30,
         shapiro_thrhld:     int   = 5000,
         prec:               int   = 6,
         alpha:              float = 0.05):

    mode       = dtypesx.strip_rmv_nmbr_space_case(mode, case = 'lower')


    data_df    = pd.DataFrame()

    mth_df     = pd.DataFrame()

    tmp_df     = input_df.dropna()


    name_array = np.asarray(tmp_df.columns)


    for idx in name_array:

        for col in name_array:

            if idx != col:

                corr_method \
                    = find_opt_corr_method \
                        (tmp_df.loc[:, idx], 
                         tmp_df.loc[:, col],
                         small_smple_thrhld = small_smple_thrhld,
                         shapiro_thrhld     = shapiro_thrhld,
                         prec               = prec,
                         alpha              = alpha)

                data_df.loc[idx, col] \
                    = tmp_df.loc[:, idx].corr(tmp_df.loc[:, col], method = corr_method)

                mth_df.loc[idx, col] = corr_method

            else: 

                data_df.loc[idx, col] = 1.0

                mth_df.loc[idx, col]  = ''


    data_df.index.name = index


    if mode == 'data':     return data_df

    elif mode == 'method': return mth_df

    elif mode == 'both':   return data_df, mth_df


# In[130]:


#*******************************************************************************************
 #
 #  Function Name:  calc_fold_errors_array
 #
 #  Function Description:
 #      This function calculates the fold errors array to find time-series cross-validation.
 #
 #
 #  Return Type: array
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  dataframe      data_df          The parameter is the input dataframe.
 #  iterator       tscv_itr         The parameter is the time series split iterator.
 #  integer        window           The parameter is the presented window size.
 #  integer        min_periods      The parameter is the minimum number of periods.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def calc_fold_errors_array \
        (data_df:     pd.DataFrame,
         tscv_itr:    object,
         window:      int,
         min_periods: int) \
-> np.ndarray:

    fold_errors_array = np.asarray([])

    for train_idx, val_idx in tscv_itr:

        train_df          = data_df.iloc[train_idx]

        val_df            = data_df.iloc[val_idx]


        train_roll_corr_time_series \
            = train_df['x'] \
                .rolling \
                    (window = window, 
                     min_periods = min_periods) \
                        .corr(train_df['y']) \
                        .dropna()

        if len(train_roll_corr_time_series) < 2: continue


        val_actual_corr_series \
            = val_df['x'] \
                .rolling \
                    (window = window,
                     min_periods = min_periods) \
                        .corr(val_df['y']) \
                        .dropna()

        if len(val_actual_corr_series) < 2: continue


        predicted_flt     = train_roll_corr_time_series.mean()

        mse_flt           = np.mean((val_actual_corr_series - predicted_flt) ** 2)


        fold_errors_array = np.append(fold_errors_array, mse_flt)


    return fold_errors_array


# In[131]:


#*******************************************************************************************
 #
 #  Function Name:  best_roll_window_rslt_list
 #
 #  Function Description:
 #      This function calculates the results for the time-series cross-validation to find
 #      the optimal rolling window size and minimum periods.
 #
 #
 #  Return Type: list
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  dataframe      data_df          The parameter is the input dataframe.
 #  array          wndw_cnd_array  The parameter is the array of window sizes to test.
 #  float          min_period_ratio The parameter is the number of minimum period ratio. 
 #                                  min_periods = int(window * min_period_ratio)
 #                                  0.75 means 75% of the window must be filled
 #  integer        n_splits         The parameter is the number of CV folds.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def best_roll_window_rslt_list \
        (data_df:          pd.DataFrame,
         wndw_cnd_array:   np.ndarray,
         min_period_ratio: float = 0.75,
         n_splits:         int   = 5) \
-> list: 

    results_list          = []

    for window in wndw_cnd_array:

        tscv_itr          = TimeSeriesSplit(n_splits = n_splits).split(data_df)

        min_periods_int   = max(2, int(window * min_period_ratio))


        fold_errors_array \
            = calc_fold_errors_array \
                (data_df, tscv_itr, window, min_periods_int)

        if len(fold_errors_array) > 0:

            if not use_median_kfold_cv_errors(fold_errors_array):

                mse_flt   = np.mean(fold_errors_array)

            else: mse_flt = np.median(fold_errors_array)


            results_list \
                .append \
                    ({'window':      window,
                      'min_periods': min_periods_int,
                      'mean_cv_mse': mse_flt,
                      'std_cv_mse':  np.std(fold_errors_array)})


    return results_list


# In[132]:


#*******************************************************************************************
 #
 #  Function Name:  best_window_min_period_cv_error
 #
 #  Function Description:
 #      This function uses time-series cross-validation to find the optimal rolling 
 #      window size and minimum periods.
 #
 #
 #  Return Type: integer, integer, dataframe
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  series         X_series         The parameter is the x-values series.
 #  series         y_series         The parameter is the y-values series.
 #  array          wndw_cnd_array   The parameter is the array of window sizes to test.
 #  float          min_period_ratio The parameter is the number of minimum period ratio. 
 #                                  min_periods = int(window * min_period_ratio)
 #                                  0.75 means 75% of the window must be filled
 #  integer        n_splits         The parameter is the number of CV folds.
 #  string         index            The parameter is the name of the output dataframe 
 #                                  index.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def best_window_min_period_cv_error \
        (X_series:         pd.Series, 
         y_series:         pd.Series, 
         wndw_cnd_array:   object = None, 
         min_period_ratio: float  = 0.75,
         n_splits:         int    = 5,
         index:            str    = 'window') \
-> tuple[int, int, pd.DataFrame]:

    data_df              = pd.DataFrame({'x': X_series, 'y': y_series}).dropna()

    n_int                = len(data_df)


    if wndw_cnd_array is None:

        min_w_int        = max(5, n_int // 50)

        max_w_int        = min(120, n_int // 5)

        step_int         = max(1, (max_w_int - min_w_int) // 20)


        wndw_cnd_array   = np.asarray(range(min_w_int, max_w_int + 1, step_int))


    results_list \
        = best_roll_window_rslt_list \
            (data_df,
             wndw_cnd_array,
             min_period_ratio,
             n_splits)

    results_df           = pd.DataFrame(results_list).set_index(index)


    best_window_int      = results_df['mean_cv_mse'].idxmin()

    best_min_periods_int = int(results_df.loc[best_window_int, 'min_periods'])


    return best_window_int, best_min_periods_int, results_df


# In[133]:


#*******************************************************************************************
 #
 #  Function Name:  best_window_min_period_cv_error_all
 #
 #  Function Description:
 #      This function returns a summary dataframe of best window sizes and minimum 
 #      periods per series.
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
 #  dictionary     comp_dict        The parameter is the comparison series dictionary.
 #  string         index            The parameter is the output dataframe index name.
 #  array          wndw_cnd_array   The parameter is the array of window sizes to test.
 #  float          min_period_ratio The parameter is the number of minimum period ratio. 
 #                                  min_periods = int(window * min_period_ratio)
 #                                  0.75 means 75% of the window must be filled
 #  integer        n_splits         The parameter is the number of CV folds.
 #  string         wndw_index       The parameter is the window datafame index name.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def best_window_min_period_cv_error_all \
        (input_series:     pd.Series, 
         comp_dict:        dict, 
         index:            str    = 'series',
         wndw_cnd_array:   object = None, 
         min_period_ratio: float  = 0.75,
         n_splits:         int    = 5,
         wndw_index:       str    = 'window') \
-> pd.DataFrame:

    rows_list = []

    for label, series in comp_dict.items():

        best_w_int, best_mp_int, _ \
            = best_window_min_period_cv_error \
                (input_series, 
                 series,
                 wndw_cnd_array   = wndw_cnd_array,
                 min_period_ratio = min_period_ratio,
                 n_splits         = n_splits,
                 index            = wndw_index)

        rows_list \
            .append \
                ({index: label,
                  'best_window': best_w_int,
                  'min_periods': best_mp_int})

    wndws_df = pd.DataFrame(rows_list).set_index(index)

    return wndws_df


# In[134]:


#*******************************************************************************************
 #
 #  Function Name:  calc_maxlag
 #
 #  Function Description:
 #      This function calculates the optimum maximum lag by calculating correlations
 #      over a range.
 #
 #
 #  Return Type: integer
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  series         X_series         The parameter is the x-values series.
 #  series         y_series         The parameter is the y-values series.
 #  string         method           The parameter is the correlation method.
 #  integer        maxlag           The parameter is the maximum lag.
 #  integer        prec             The parameter is the precision of the numbers.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def calc_maxlag \
        (X_series: pd.Series, 
         y_series: pd.Series,
         method:   str = 'pearson',
         maxlag:   int = 180,
         prec:     int = 6) \
-> int:

    data_df       = pd.DataFrame({'x': X_series, 'y': y_series}).dropna()


    best_lag_int  = 0

    best_corr_flt = 0


    for lag in range(-maxlag, maxlag + 1):

        if lag > 0:   corr_flt = data_df['x'].corr(data_df['y'].shift(-lag), method = method)

        elif lag < 0: corr_flt = data_df['x'].shift(lag).corr(data_df['y'],  method = method)

        else:         corr_flt = data_df['x'].corr(data_df['y'],             method = method)


        if round(abs(corr_flt), prec) >= round(abs(best_corr_flt), prec): 

            best_corr_flt = corr_flt

            best_lag_int  = lag


    return best_lag_int


# In[135]:


#*******************************************************************************************
 #
 #  Function Name:  calc_maxlag_all
 #
 #  Function Description:
 #      This function calculates the optimum maximum lag by calculating correlations
 #      over a range for an x-value series and a series dictionary of y-value series.
 #
 #
 #  Return Type: integer
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  series         X_series         The parameter is the x-values series.
 #  dict           comp_dict        The parameter is the comparison series dictionary.
 #  string         method           The parameter is the correlation method.
 #  integer        maxlag           The parameter is the maximum lag.
 #  integer        prec             The parameter is the precision of the numbers.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def calc_maxlag_all \
        (X_series:  pd.Series,
         comp_dict: dict, 
         method:    str = 'pearson',
         maxlag:    int = 180,
         prec:      int = 6) \
-> int:

    maxlag_int = 0

    for _, y_series in comp_dict.items():

        lag_int \
            = calc_maxlag \
                (X_series, 
                 y_series, 
                 method = method, 
                 maxlag = maxlag,
                 prec   = prec)

        if abs(lag_int) >= abs(maxlag_int): maxlag_int = lag_int


    return maxlag_int


# In[136]:


#*******************************************************************************************
 #
 #  Function Name:  calc_autocorr_maxlag
 #
 #  Function Description:
 #      This function uses autocorrelation to calculate the optimum maximum lag.
 #
 #
 #  Return Type: integer
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  series         X_series         The parameter is the x-values series.
 #  series         y_series         The parameter is the y-values series.
 #  integer        max_cap          The parameter is hard upper limit on returned lag.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def calc_autocorr_maxlag \
        (X_series: pd.Series, 
         y_series: pd.Series, 
         max_cap:  int = 90) \
-> int:

    data_df     = pd.DataFrame({'x': X_series, 'y': y_series}).dropna()


    n_int       = len(data_df)

    if n_int < 10: return None


    ess_x_int   = autocorr_eff_n(data_df['x'], n_int, max_cap)

    ess_y_int   = autocorr_eff_n(data_df['y'], n_int, max_cap)


    ess_int     = max(ess_x_int, ess_y_int)

    lag_int     = int(np.sqrt(float(ess_int)))


    maxlag_int  = min(lag_int, max_cap)

    return maxlag_int


# In[137]:


#*******************************************************************************************
 #
 #  Function Name:  calc_autocorr_maxlag_all
 #
 #  Function Description:
 #      This function uses autocorrelation to calculate the optimum maximum lag from
 #      an x-series and a comparison dictionary of y-series.
 #
 #
 #  Return Type: integer
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  series         X_series         The parameter is the x-series.
 #  dictionary     comp_dict        The parameter is the comparison series dictionary.
 #  integer        max_cap          The parameter is hard upper limit on returned lag.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def calc_autocorr_maxlag_all \
        (X_series:  pd.Series,
         comp_dict: dict, 
         max_cap:   int = 90) \
-> int:

    maxlag_int  = 0

    for _, y_series in comp_dict.items():

        lag_int = calc_autocorr_maxlag(X_series, y_series, max_cap)

        if maxlag_int <= lag_int: maxlag_int = lag_int

    return maxlag_int


# In[138]:


#*******************************************************************************************
 #
 #  Function Name:  zivot_andrews_test_summ_df
 #
 #  Function Description:
 #      This function returns the Zivot-Andrews structural break unit root test as a
 #      dataframe on a series dictionary.
 #
 #      Unlike the standard ADF test, Zivot-Andrews allows for a single structural break 
 #      in either the intercept, trend, or both, and finds the break point endogenously 
 #      by minimising the t-statistic across all candidate break dates.
 #
 #      H0: Series has a unit root with a single structural break.
 #      H1: Series is stationary with a one-time structural break.
 #
 #
 #  Return Type: dataframe
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  dictionary     series_dict      The parameter is the input series dictionary.
 #  float          trim             The parameter is the percentage of series at begin/end 
 #                                  to exclude from break-period calculation in range 
 #                                  [0, 0.333] 
 #  string         maxlag           The parameter is the maximum lag which is included 
 #                                  in test, default value of 12*(nobs/100)^{1/4} is used 
 #                                  when None.
 #  string         autolag          The parameter is the method to select the lag length 
 #                                  when using automatic selection.
 #  string         index            The parameter is the output index name.
 #  integer        prec             The parameter is the output number precision.
 #  float          alpha            The parameter is the p-value threshold.
 #  boolean        verbose          The parameter, if True, prints a diagnostic table of 
 #                                  results for all three regression methods.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def zivot_andrews_test_summ_df \
        (series_dict: dict,
         trim:        float  = 0.15,
         maxlag:      object = None,
         autolag:     str    = 'BIC',
         index:       str    = 'series',
         prec:        int    = 6,
         alpha:       float  = 0.05,
         verbose:     bool   = False) \
-> pd.DataFrame:

    rows_list = []

    for name, series in series_dict.items():

        data_series = series.copy().dropna().astype(float)


        if maxlag is None: maxlag_int = int(12.0 * (float(len(data_series)) / 100.0)**(0.25))

        else:              maxlag_int = int(abs(maxlag))


        result_dict \
            = opt_zivot_andrews_series \
                (data_series,
                 trim    = trim,
                 maxlag  = maxlag_int,
                 autolag = autolag,
                 prec    = prec,
                 alpha   = alpha,
                 verbose = verbose)


        break_pct  = str(result_dict['break_pct']) + '%'


        rows_list \
            .append \
                ({index:          name,
                  'za_stat':      float(round(result_dict['za_stat'], prec)),
                  'p_value':      float(round(result_dict['p_value'], prec)),
                  '1%':           float(round(result_dict['1%'],      prec)),
                  '5%':           float(round(result_dict['5%'],      prec)),
                  '10%':          float(round(result_dict['10%'],     prec)),
                  'n_obs':        int(result_dict['n_obs']),
                  'lags_used':    int(result_dict['lags_used']),
                  'break_sq_idx': int(result_dict['break_sq_idx']),
                  'break_index':  str(result_dict['break_index']),
                  'break_pct':    str(break_pct),
                  'regr_mthd':    str(result_dict['regr_mthd']),
                  'autolag':      str(result_dict['autolag']),
                  'rejects_5pct': bool(result_dict['rejects_5pct']),
                  'stationary':   str(result_dict['stationary'])})


    results_df = pd.DataFrame(rows_list).set_index(index)

    return results_df


# In[139]:


#*******************************************************************************************
 #
 #  Function Name:  zivot_andrews_best_test_summ_df
 #
 #  Function Description:
 #      This function returns the Zivot-Andrews structural break unit root test as a
 #      dataframe on a series dictionary.
 #
 #      Unlike the standard ADF test, Zivot-Andrews allows for a single structural break 
 #      in either the intercept, trend, or both, and finds the break point endogenously 
 #      by minimising the t-statistic across all candidate break dates.
 #
 #      H0: Series has a unit root with a single structural break.
 #      H1: Series is stationary with a one-time structural break.
 #
 #
 #  Return Type: dataframe
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  dictionary     series_dict      The parameter is the input series dictionary.
 #  float          trim             The parameter is the percentage of series at begin/end 
 #                                  to exclude from break-period calculation in range 
 #                                  [0, 0.333] 
 #  string         maxlag           The parameter is the maximum lag which is included 
 #                                  in test, default value of 12*(nobs/100)^{1/4} is used 
 #                                  when None.
 #  string         index            The parameter is the output index name.
 #  integer        prec             The parameter is the output number precision.
 #  float          alpha            The parameter is the p-value threshold.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def zivot_andrews_best_test_summ_df \
        (series_dict: dict,
         trim:        float  = 0.15,
         maxlag:      object = None,
         index:       str    = 'series',
         prec:        int    = 6,
         alpha:       float  = 0.05) \
-> pd.DataFrame:

    rows_list      = []

    for name, series in series_dict.items():

        data_array = dtypesx.cnv_data_to_array(series.dropna())


        if maxlag is None: maxlag_int = int(12.0 * (float(len(data_array)) / 100.0)**(0.25))

        else:              maxlag_int = int(abs(maxlag))


        best_za_stat_flt, \
        best_p_value_flt, \
        best_crit_vals_dict, \
        best_n_int, \
        best_lags_used_int, \
        best_brk_idx_int, \
        best_brk_pct_flt, \
        best_regr_mthd, \
        best_autolag_mthd, \
        best_stnry_bool \
            = best_zivot_andrews_series \
                (data_array, 
                 trim   = trim, 
                 maxlag = maxlag_int, 
                 prec   = prec, 
                 alpha  = alpha)

        break_pct  = f'{round(best_brk_pct_flt, prec)}%'

        rows_list \
            .append \
                ({index:         name,
                  'za_stat':     round(best_za_stat_flt,           prec),    
                  'p_value':     round(best_p_value_flt,           prec),      
                  '1%':          round(best_crit_vals_dict['1%'],  prec),
                  '5%':          round(best_crit_vals_dict['5%'],  prec),
                  '10%':         round(best_crit_vals_dict['10%'], prec),
                  'n_obs':       best_n_int,
                  'lags_used':   best_lags_used_int,
                  'break_index': best_brk_idx_int,
                  'break_pct':   break_pct,
                  'regr_mthd':   best_regr_mthd,
                  'autolag':     best_autolag_mthd,
                  'stationary':  best_stnry_bool})


    results_df = pd.DataFrame(rows_list).set_index(index)

    return results_df


# In[140]:


#*******************************************************************************************
 #
 #  Function Name:  adf_test_summ_df
 #
 #  Function Description:
 #      This function returns Augmented Dickey-Fuller (ADF) test results as a dataframe
 #      for a series dictionary. The ADF test checks whether a series has a unit root 
 #      (i.e., is non-stationary), formalizing why the full-period correlations cannot
 #      be taken at face value.
 #
 #
 #  Return Type: dataframe
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  dictionary     series_dict      The parameter is the input series dictionary.
 #  string         regression       The parameter is null hypothesis for the ADF test 
 #                                  ('c', 'ct', 'ctt', or None).
 #  string         autolag          The parameter is the method to use when automatically 
 #                                  determining the lag length (0, 1, 2, ... , maxlag).
 #  string/none    maxlag           The parameter is the maximum lag which is included 
 #                                  in test, default value of 12*(nobs/100)^{1/4} is used 
 #                                  when None.
 #  string         index            The parameter is the output index name.
 #  integer        prec             The parameter is the output number precision.
 #  float          alpha            The parameter is the p-value threshold.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def adf_test_summ_df \
        (series_dict: dict, 
         regression:  str    = 'c',
         autolag:     str    = 'AIC',
         maxlag:      object = None,
         index:       str    = 'series',
         prec:        int    = 6,
         alpha:       float  = 0.05) \
-> pd.DataFrame:

    autolag        = dtypesx.strip_rmv_nmbr_space_case(autolag, case = 'upper')

    rows_list      = []

    for name, series in series_dict.items():

        data_array = dtypesx.cnv_data_to_array(series.dropna())

        result_dict \
            = opt_adf_stnry_series \
                (data_array,
                 index  = name,
                 maxlag = maxlag,
                 prec   = prec,
                 alpha  = alpha)

        rows_list.append(result_dict)


    results_df = pd.DataFrame(rows_list).set_index(index)

    return results_df


# In[141]:


#*******************************************************************************************
 #
 #  Function Name:  kpss_test_summ_df
 #
 #  Function Description:
 #      This function returns optimal Kwiatkowski-Phillips-Schmidt-Shin (KPSS) test 
 #      results as a dataframe for a series dictionary. This test has a reversed null 
 #      hypothesis compared to the ADF test.
 #
 #
 #  Return Type: dataframe
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  dictionary     series_dict      The parameter is the input series dictionary.
 #  string         regression       The parameter is null hypothesis for the ADF test 
 #                                  ('c', 'ct', 'ctt', or None).
 #  string         autolag          The parameter is the method to use when automatically 
 #                                  determining the lag length (0, 1, 2, ... , maxlag).
 #  string/none    maxlag           The parameter is the maximum lag which is included 
 #                                  in test, default value of 12*(nobs/100)^{1/4} is used 
 #                                  when None.
 #  string         index            The parameter is the output index name.
 #  integer        prec             The parameter is the output number precision.
 #  float          alpha            The parameter is the p-value threshold.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def kpss_test_summ_df \
        (series_dict: dict, 
         max_lags:    int    = None,
         index:       str    = 'series',
         prec:        int    = 6,
         alpha:       float  = 0.05) \
-> pd.DataFrame:

    rows_list      = []

    for name, series in series_dict.items():

        data_array = dtypesx.cnv_data_to_array(series.dropna())

        result_dict \
            = opt_kpss_stnry_series \
                (data_array,
                 index    = name,
                 max_lags = max_lags,
                 prec     = prec,
                 alpha    = alpha)

        rows_list.append(result_dict)


    results_df = pd.DataFrame(rows_list).set_index(index)

    return results_df


# In[142]:


#*******************************************************************************************
 #
 #  Function Name:  cross_phase_corr_summ_df
 #
 #  Function Description:
 #      This function builds a cross-phase correlation summary table.
 #
 #
 #  Return Type: dataframe
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  dictionary     series_dict      The parameter is the input series dictionary.
 #  dictionary     comp_dict        The parameter is the comparison series dictionary.
 #  string         method           The parameter is the correlation method.
 #  string         index            The parameter is the output index name.
 #  boolean        bonferroni       The parameter indicates whether to apply Bonferroni 
 #                                  correction across all phase comparisons for each 
 #                                  index (divides alpha by the number of phases).
 #  integer        prec             The parameter is the output number precision.
 #  float          alpha            The parameter is the p-value threshold.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def cross_phase_corr_summ_df \
        (series_dict: dict, 
         comp_dict:   dict,
         method:      str   = 'pearson',
         index:       str   = 'series',
         bonferroni:  bool  = False,
         prec:        int   = 6,
         alpha:       float = 0.05) \
-> pd.DataFrame:

    corr_funcs_dict \
        = {'pearson':  pearsonr,
           'spearman': spearmanr,
           'kendall':  kendalltau}


    phases_array  = np.asarray(list(series_dict.keys()))

    indices_array = np.asarray(list(comp_dict.keys()))


    method        = dtypesx.strip_rmv_nmbr_space_case(method, case = 'lower')

    alpha_adj_flt \
        = (alpha / float(len(phases_array))) \
            if bonferroni and len(phases_array) > 0 else alpha


    rows_dict     = {}

    for idx in indices_array:

        row_dict  = {}

        for phase in phases_array:

            series      = series_dict[phase]

            comp_series = comp_dict[idx][phase]


            data_df     = pd.DataFrame({'x': series, 'y': comp_series}).dropna()

            if len(data_df) < 4:

                row_dict[phase] = np.nan

                continue


            _, p_flt    = corr_funcs_dict[method](data_df['x'], data_df['y'])

            stars_tuple \
                = ('***' if p_flt < 0.001 else
                   '**'  if p_flt < 0.01  else
                   '*'   if round(p_flt, prec) < round(alpha_adj, prec) else 
                   '')


            row_dict[phase] = f'{r:+.3f}{stars_tuple}'


        rows_dict[idx] = row_dict


    results_df = pd.DataFrame(rows_dict).transpose().set_index(index)

    return results_df


# In[143]:


#*******************************************************************************************
 #
 #  Function Name:  bai_perron_segs_list
 #
 #  Function Description:
 #      This function creates a segments list for a Bai-Perron test.
 #
 #
 #  Return Type: list
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  array          data_array       The parameter is the data array.
 #  list           seg_bnds_list    The parameter is segments bounds list.
 #  integer        prec             The parameter is the output number precision.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def bai_perron_segs_list \
        (data_array:    np.ndarray,
         seg_bnds_list: list,
         prec:          int = 6) \
-> list:

    segs_list     = []

    for i in range(len(seg_bnds_list) - 1):

        start_int = seg_bnds_list[i]

        end_int   = seg_bnds_list[i + 1]


        seg_list  = list(data_array[start_int:end_int])

        segs_list \
            .append \
                ({'segment':         i + 1,
                  'start':           start_int,
                  'end':             end_int - 1,
                  'n_obs':           len(seg_list),
                  'mean':            round(float(np.mean(seg_list)), prec),
                  'std':             round(float(np.std(seg_list)),  prec),
                  'min':             round(float(min(seg_list)),     prec),
                  'max':             round(float(max(seg_list)),     prec),
                  'pct_change_mean': None})


    for i in range(1, len(segs_list)):

        prev_mean_flt = segs_list[i - 1]['mean']

        curr_mean_flt = segs_list[i]['mean']


        if prev_mean_flt != 0:

            segs_list[i]['pct_change_mean'] \
                = round((curr_mean_flt - prev_mean_flt) / abs(prev_mean_flt) * 100.0, prec)


    return segs_list


# In[144]:


#*******************************************************************************************
 #
 #  Function Name:  bai_perron_bbi_bbp
 #
 #  Function Description:
 #      This function returns the the break indices list and the break percentages list
 #      as text strings.
 #
 #
 #  Return Type: string, string
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  array          data_array       The parameter is the data array.
 #  list           seg_bnds_list    The parameter is segments bounds list.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def bai_perron_bbi_bbp \
        (break_idxs_list: list,
         break_pcts_list: list) \
-> tuple[str, str]:

    if len(break_idxs_list) <= 0: bbi = 'n/a'

    else:                         bbi = str(break_idxs_list)


    if len(break_pcts_list) <= 0: bbp = 'n/a'

    else:                         bbp = str(break_pcts_list)


    return bbi, bbp


# In[145]:


#*******************************************************************************************
 #
 #  Function Name:  bai_perron_test_summ_df
 #
 #  Function Description:
 #      This function detects the maximum multiple structural breaks in each series 
 #      in a dictionary using the Bai-Perron method via the ruptures library and
 #      returns the results as a dataframe.
 #
 #      Two detection modes (mutually exclusive):
 #      - Penalty mode  (penalty != None) : PELT algorithm finds the optimal
 #        number of breaks automatically, penalising for complexity.
 #      - Fixed mode    (n_breaks != None): Binary segmentation finds exactly
 #        n_breaks breakpoints.
 #      - Default       (both None)       : Penalty mode with auto-calibrated
 #        penalty = log(n) * std(series).
 #
 #
 #  Return Type: dataframe
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  dictionary     series_dict      The parameter is the input series dictionary.
 #  integer        max_breaks       The parameter is the maximum number of breaks to 
 #                                  consider.
 #  integer        min_size         The parameter is the minimum number of observations 
 #                                  between two breaks.
 #  integer        jump             The parameter is the subsampling — only consider 
 #                                  every jump-th point as a candidate break. 
 #                                  Lower = more precise but slower
 #  float/none     penalty          The parameter is the penalty value for PELT algorithm. 
 #                                  Higher = fewer breaks detected
 #                                  None triggers auto-calibration
 #  integer/none   n_breaks         The parameter determines whether to use Binary 
 #                                  Segmentation to find exactly this many breaks.
 #                                  Overrides penalty when provided.
 #  string         index            The parameter is the output index name.
 #  integer        prec             The parameter is the output number precision.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def bai_perron_test_summ_df \
        (series_dict: dict,
         max_breaks:  int    = 5,
         min_size:    int    = 30,
         jump:        int    = 5,
         penalty:     object = None,
         n_breaks:    object = None,
         index:       str    = 'series',
         prec:        int    = 6) \
-> pd.DataFrame:

    rows_list = []

    for name, series in series_dict.items():

        data_array      = dtypesx.cnv_data_to_array(series.dropna())

        signal_array    = data_array.reshape(-1, 1)


        result_dict \
            = opt_bai_perron_series \
                (data_array, 
                 signal_array, 
                 max_breaks = max_breaks, 
                 min_size   = min_size, 
                 jump       = jump, 
                 penalty    = penalty, 
                 n_breaks   = n_breaks, 
                 prec       = prec)


        model_desc      = model_desc_dict[result_dict['model']]


        segs_list       = bai_perron_segs_list(data_array, result_dict['seg_bnds'], prec = prec)

        bbi, bbp        = bai_perron_bbi_bbp(result_dict['brk_idxs'], result_dict['brk_pcts'])        


        rows_list \
            .append \
                ({index:           name,
                  'n_breaks':      len(result_dict['brk_idxs']),
                  'break_indices': bbi,
                  'break_pcts':    bbp,
                  'n_obs':         result_dict['n'],
                  'model':         result_dict['model'],
                  'model_desc':    model_desc,
                  'algorithm':     result_dict['algorithm']})


    results_df = pd.DataFrame(rows_list).set_index(index)

    return results_df


# In[146]:


#*******************************************************************************************
 #
 #  Function Name:  bai_perron_best_test_summ_df
 #
 #  Function Description:
 #      This function detects the maximum multiple structural breaks in each series 
 #      in a dictionary using the Bai-Perron method via the ruptures library and
 #      returns the results as a dataframe.
 #
 #      Two detection modes (mutually exclusive):
 #      - Penalty mode  (penalty != None) : PELT algorithm finds the optimal
 #        number of breaks automatically, penalising for complexity.
 #      - Fixed mode    (n_breaks != None): Binary segmentation finds exactly
 #        n_breaks breakpoints.
 #      - Default       (both None)       : Penalty mode with auto-calibrated
 #        penalty = log(n) * std(series).
 #
 #
 #  Return Type: dataframe
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  dictionary     series_dict      The parameter is the input series dictionary.
 #  integer        max_breaks       The parameter is the maximum number of breaks to 
 #                                  consider.
 #  integer        min_size         The parameter is the minimum number of observations 
 #                                  between two breaks.
 #  integer        jump             The parameter is the subsampling — only consider 
 #                                  every jump-th point as a candidate break. 
 #                                  Lower = more precise but slower
 #  float/none     penalty          The parameter is the penalty value for PELT algorithm. 
 #                                  Higher = fewer breaks detected
 #                                  None triggers auto-calibration
 #  integer/none   n_breaks         The parameter determines whether to use Binary 
 #                                  Segmentation to find exactly this many breaks.
 #                                  Overrides penalty when provided.
 #  string         index            The parameter is the output index name.
 #  integer        prec             The parameter is the output number precision.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def bai_perron_best_test_summ_df \
        (series_dict: dict,
         max_breaks:  int    = 5,
         min_size:    int    = 30,
         jump:        int    = 5,
         penalty:     object = None,
         n_breaks:    object = None,
         index:       str    = 'series',
         prec:        int    = 6) \
-> pd.DataFrame:

    rows_list = []

    for name, series in series_dict.items():

        data_array      = dtypesx.cnv_data_to_array(series.dropna())

        signal_array    = data_array.reshape(-1, 1)


        best_n_int, \
        best_model, \
        best_algorithm, \
        best_brk_idxs_list, \
        best_brk_pcts_list, \
        seg_bnds_list \
            = best_bai_perron_series \
                (data_array, 
                 signal_array, 
                 max_breaks, 
                 min_size, 
                 jump, 
                 penalty, 
                 n_breaks, 
                 prec)

        best_model_desc = model_desc_dict[best_model]


        segs_list       = bai_perron_segs_list(data_array, seg_bnds_list, prec = prec)

        bbi, bbp        = bai_perron_bbi_bbp(best_brk_idxs_list, best_brk_pcts_list)        


        rows_list \
            .append \
                ({index:           name,
                  'n_breaks':      len(best_brk_idxs_list),
                  'break_indices': bbi,
                  'break_pcts':    bbp,
                  'n_obs':         best_n_int,
                  'model':         best_model,
                  'model_desc':    best_model_desc,
                  'algorithm':     best_algorithm})


    results_df = pd.DataFrame(rows_list).set_index(index)

    return results_df


# In[147]:


#*******************************************************************************************
 #
 #  Function Name:  crss_valid_for_stnry_df
 #
 #  Function Description:
 #      This function returns cross-validation results as a dataframe for a series 
 #      dictionary.
 #
 #
 #  Return Type: dataframe
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  dictionary     series_dict      The parameter is the input series dictionary.
 #  string/none    maxlag           The parameter is the maximum lag which is included 
 #                                  in test, default value of 12*(nobs/100)^{1/4} is used 
 #                                  when None.
 #  string/integer nlags            The parameter indicates the number of lags.
 #  string         index            The parameter is the output index name.
 #  integer        prec             The parameter is the output number precision.
 #  float          alpha            The parameter is the p-value threshold.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def crss_valid_for_stnry_df \
        (series_dict: dict,
         maxlag:      object = None,
         nlags:       object = 'auto',
         index:       str    = 'series',
         prec:        int    = 6,
         alpha:       float  = 0.05) \
-> pd.DataFrame:

    adf_df \
        = adf_test_summ_df \
            (series_dict,
             maxlag = maxlag,
             index  = index,
             prec   = prec,
             alpha  = alpha)

    kpss_df \
        = kpss_test_summ_df \
            (series_dict,
             max_lags = maxlag,
             index    = index,
             prec     = prec,
             alpha    = alpha)


    rows_list           = []

    for name, series in series_dict.items():

        adf_stnry_bool  = bool(adf_df.loc[name, 'stationary'])

        kpss_stnry_bool = bool(kpss_df.loc[name, 'stationary'])

        result, conclusion, recommendation \
            = stationarity_conclusions(adf_stnry_bool, kpss_stnry_bool) 

        rows_list \
            .append \
                ({index:               name,
                  'adf_stationary':    adf_stnry_bool,
                  'kpss_stationary':   kpss_stnry_bool,
                  'result':            result,
                  'conclusion':        conclusion,
                  'recommendation':    recommendation})


    results_df = pd.DataFrame(rows_list).set_index(index)

    return results_df


# In[148]:


#*******************************************************************************************
 #
 #  Function Name:  crct_stnry_df
 #
 #  Function Description:
 #      This function adjusts each series in the dictionary to achieve stationary
 #      and returns the results in a dataframe.
 #
 #
 #  Return Type: dataframe
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  dictionary     series_dict      The parameter is the input series dictionary.
 #  string/integer nlags            The parameter indicates the number of lags.
 #  integer/none   maxlag           The parameter is the maximum lag which is included 
 #                                  in test, default value of 12*(nobs/100)^{1/4} is used 
 #                                  when None.
 #  string         index            The parameter is the output index name.
 #  float          min_r2           The parameter is the minimum R² the log-linear 
 #                                  model must achieve.
 #  float          lin_vs_exp_gap   The parameter is the minimum margin by which 
 #                                  log-linear R² must beat linear R².
 #  integer        max_degree       The parameter is the highest polynomial degree to try.
 #  string         criterion        The parameter is the model selection criteria ('aic' 
 #                                  or 'bic').
 #  boolean        vrb_bool         The parameter is the indicator for verbosity.
 #  integer        prec             The parameter is the output number precision.
 #  float          alpha            The parameter is the p-value threshold.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def crct_stnry_df \
        (series_dict:    dict,
         nlags:          object = 'auto',
         maxlag:         object = None,
         index:          str    = 'series',
         min_r2:         float  = 0.80,
         lin_vs_exp_gap: float  = 0.05,
         max_degree:     int    = 10,
         criterion:      str    = 'bic',
         vrb_bool:       bool   = True,
         prec:           int    = 6,
         alpha:          float  = 0.05) \
-> pd.DataFrame:

    rows_list           = []

    for name, series in series_dict.items():

        data_series     = series.dropna()


        adf_results_dict \
            = opt_adf_stnry_series \
                (data_series, 
                 index  = index, 
                 maxlag = maxlag, 
                 prec   = prec, 
                 alpha  = alpha)

        kpss_results_dict \
            = opt_kpss_stnry_series \
                (data_series, 
                 index = index, 
                 prec  = prec, 
                 alpha = alpha)


        if not adf_results_dict['stationary'] \
            and kpss_results_dict['stationary']: 

            data_series \
                = crct_diff_stnry_series \
                    (data_series, 
                     vrb_bool       = vrb_bool,
                     maxlag         = maxlag,
                     index          = index,
                     min_r2         = min_r2,
                     lin_vs_exp_gap = lin_vs_exp_gap,
                     max_degree     = max_degree,
                     criterion      = criterion,
                     prec           = prec, 
                     alpha          = alpha)

        elif adf_results_dict['stationary'] \
                and not kpss_results_dict['stationary']: 

            data_series \
                = crct_trend_stnry_series \
                    (data_series, 
                     vrb_bool       = vrb_bool,
                     maxlag         = maxlag,
                     index          = index,
                     min_r2         = min_r2,
                     lin_vs_exp_gap = lin_vs_exp_gap,
                     max_degree     = max_degree,
                     criterion      = criterion,
                     prec           = prec, 
                     alpha          = alpha)

        elif not adf_results_dict['stationary'] \
                and not kpss_results_dict['stationary']: 

            data_series \
                = crct_non_stnry_series \
                    (data_series, 
                     vrb_bool       = vrb_bool,
                     maxlag         = maxlag,
                     index          = index,
                     min_r2         = min_r2,
                     lin_vs_exp_gap = lin_vs_exp_gap,
                     prec           = prec, 
                     alpha          = alpha)

        else:

            if vrb_bool:

                logx.print_and_log_text \
                    ('\033[1m' \
                     + f'STATIONARY TIME SERIES DETECTED: {name}.\n\n' \
                     + '\033[0m')

            else: pass


        rows_list.append(data_series)


    data_df            = pd.concat(rows_list, axis = 1).dropna()

    data_df.index.name = index


    return data_df


# In[149]:


#*******************************************************************************************
 #
 #  Function Name:  opt_degree_summ_df
 #
 #  Function Description:
 #      This function summarizes the optimal polynomial degree for correlation between an 
 #      x-series and a series dictionary using a combination of AIC, cross-validated R², 
 #      and overfitting detection.
 #
 #
 #  Return Type: dataframe
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  series         X_series         The parameter is the x-series.
 #  dictionary     comp_dict        The parameter is the comparison series dictionary.
 #  integer        max_degree       The parameter is the maximum polynomial degree.
 #  integer        cv_folds         The parameter is the number of cross-validation folds.
 #  float          aic_wgt          The parameter is the weight given to AIC score in 
 #                                  combined ranking.
 #  float          cv_wgt           The parameter is the weight given to CV R² in combined 
 #                                  ranking.
 #  float          ovrft_r2_gp      The parameter is the maximum allowed gap between train 
 #                                  and CV R².
 #  integer        min_smpls_per_prm
 #                                  The parameter is the minimum data points per model 
 #                                  parameter.
 #  string         index            The parameter is the output index name.
 #  integer        prec             The parameter is the output number precision.
 #  float          alpha            The parameter is the p-value threshold.
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def opt_degree_summ_df \
        (X_series:          pd.Series, 
         comp_dict:         dict,
         max_degree:        int   = 10,
         cv_folds:          int   = 5,
         aic_wgt:           float = 0.5,
         cv_wgt:            float = 0.5,
         ovrft_r2_gp:       float = 0.15,
         min_smpls_per_prm: int   = 3,
         index:             str   = 'series',
         prec:              int   = 6,
         alpha:             float = 0.05) \
-> pd.DataFrame:

    idx_array     = np.asarray([], dtype = str)

    rows_list     = []


    for name, y_series in comp_dict.items():

        _, _, opt_dict, _ \
            = opt_poly_degree \
                (X_series, 
                 y_series,
                 max_degree        = max_degree,
                 cv_folds          = cv_folds,
                 aic_wgt           = aic_wgt,
                 cv_wgt            = cv_wgt,
                 ovrft_r2_gp       = ovrft_r2_gp,
                 min_smpls_per_prm = min_smpls_per_prm,
                 prec              = prec,
                 alpha             = alpha)

        idx_array = np.append(idx_array, y_series.name)

        rows_list.append(opt_dict)


    opt_df        = pd.DataFrame(rows_list)

    opt_df[index] = idx_array

    opt_df        = opt_df.set_index(index)                   

    return opt_df


# In[150]:


#*******************************************************************************************
 #
 #  Function Name:  eg_coint_test_summ_df
 #
 #  Function Description:
 #      This function applies the Engle-Granger cointegration test to a series
 #      dictionary and returns the results in a dataframe.
 #
 #
 #  Return Type: dataframe
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  series         X_series         The parameter is the x-series.
 #  dictionary     comp_dict        The parameter is the comparison series dictionary.
 #  string         index            The parameter is the output index name.
 #  integer/none   maxlag           The parameter is the maximum lag which is included 
 #                                  in test, default value of 12*(nobs/100)^{1/4} is used 
 #                                  when None.
 #  integer        prec             The parameter is the output number precision.
 #  float          alpha            The parameter is the p-value threshold.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def eg_coint_test_summ_df \
        (X_series:  pd.DataFrame, 
         comp_dict: dict, 
         index:     str    = 'series',
         maxlag:    object = None,
         prec:      int    = 6, 
         alpha:     float  = 0.05) \
-> pd.DataFrame:

    rows_list   = []

    for name, y_series in comp_dict.items():

        data_df = pd.DataFrame({'x': X_series, 'y': y_series}).dropna()


        X_array = dtypesx.cnv_data_to_array(data_df['x'])

        y_array = dtypesx.cnv_data_to_array(data_df['y'])


        result_dict \
            = opt_eg_coint_series \
                (y_array,
                 X_array,
                 maxlag  = maxlag,
                 prec    = prec, 
                 alpha   = alpha)

        result_dict[index] = y_series.name

        rows_list.append(result_dict)


    results_df = pd.DataFrame(rows_list).set_index(index)

    drop_list \
        = ['1%', '5%', '10%', 'margin', 'resid_mean', 'resid_mean_tstat', 'resid_mean_pvalue', 
           'resid_trend_fstat', 'resid_trend_pvalue', 'resid_bic', 'passes_both', 'trend']

    results_df = results_df.drop(columns = drop_list)


    return results_df


# In[151]:


#*******************************************************************************************
 #
 #  Function Name:  opt_window_summ_df
 #
 #  Function Description:
 #      This function summarizes the optimal window size for a rolling correlation 
 #      between an x-series series and a series dictionary by balancing correlation 
 #      stability, statistical significance, and temporal consistency across 
 #      cross-validated folds.
 #
 #
 #  Return Type: dataframe, array
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  series          X_series        The parameter is the x-series.
 #  dictionary      comp_dict       The parameter is the comparison series dictionary. 
 #  int             min_window      The parameter is the minimum window size.
 #  int             max_window      The parameter is the maximum window size.
 #  int             n_splits        The parameter is the number of TimeSeriesSplit folds.
 #  int             min_factor      The parameter is the minimum factor for feasibility. 
 #  string          index           The parameter is the dataframe index name.
 #  integer         small_smple_thrhld             
 #                                  The parameter is the small sample threshold.
 #  integer         shapiro_thrhld  The parameter is the Shapiro-Wills threshold.
 #  integer         prec            The parameter is the output number precision.
 #  float           alpha           The parameter is the p-value threshold.
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def opt_window_summ_df \
        (X_series:           pd.Series, 
         comp_dict:          dict,
         min_window:         int   = 5,
         max_window:         int   = None,
         n_splits:           int   = 5,
         min_factor:         int   = 2,
         index:              str   = 'series',
         small_smple_thrhld: int   = 30,
         shapiro_thrhld:     int   = 5000,
         prec:               int   = 6,
         alpha:              float = 0.05) \
-> tuple[pd.DataFrame, np.ndarray]:

    rows_list         = []

    w_array           = np.asarray([], dtype = int)


    for name, y_series in comp_dict.items():

        corr_method \
            = find_opt_corr_method \
                (X_series, 
                 y_series,
                 small_smple_thrhld = small_smple_thrhld,
                 shapiro_thrhld     = shapiro_thrhld,
                 prec               = prec,
                 alpha              = alpha)

        w_int, opt_dict, _ \
            = find_optimal_rolling_window \
                (X_series,
                 y_series,
                 min_window = min_window,
                 max_window = max_window,
                 n_splits   = n_splits,
                 method     = corr_method,
                 min_factor = min_factor,
                 prec       = prec,
                 alpha      = alpha)

        w_array       = np.append(w_array, w_int)

        rows_list.append(opt_dict)


    opt_df            = pd.DataFrame(rows_list)

    opt_df.index      = list(comp_dict)

    opt_df.index.name = index

    return opt_df, w_array


# In[152]:


#*******************************************************************************************
 #
 #  Function Name:  opt_min_period_summ_df
 #
 #  Function Description:
 #      This function summarizes the optimal min_periods for a rolling correlation 
 #      between an x-series a series dictionary, given a fixed window size.
 #
 #      min_periods controls how many observations are required before the
 #      first valid correlation is computed. Too low → noisy early estimates.
 #      Too high → excessive data loss during warmup.
 #
 #
 #  Return Type: dictionary
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  series         X_series         The parameter is the x-series.
 #  dictionary     comp_dict        The parameter is the comparison series dictionary. 
 #  int            window           The parameter is the window size.
 #  integer        n_splits         The parameter is the number of CV folds.
 #  integer        min_thrhld       The parameter is the minimum threshold for data.
 #  bool           pct_bool         The parameter is an indicator of whether certain 
 #                                  results are represented as a percentage rather than 
 #                                  a decimal.
 #  string         index            The parameter is the dataframe index name.
 #  integer        prec             The parameter is the output number precision.
 #  float          alpha            The parameter is the p-value threshold.
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def opt_min_period_summ_df \
        (X_series:     pd.Series, 
         comp_dict:    dict,
         window_array: np.ndarray,
         n_splits:     int   = 5,
         min_thrhld:   int   = 3,
         pct_bool:     bool  = True,
         index:        str   = 'series',
         prec:         int   = 6,
         alpha:        float = 0.05) \
-> pd.DataFrame:

    rows_list         = []

    i                 = 0


    for name, y_series in comp_dict.items():

        corr_method   = find_opt_corr_method(y_series, X_series)

        _, opt_dict, _ \
            = find_optimal_min_periods \
                (X_series,
                 y_series,
                 window     = window_array[i],
                 n_splits   = n_splits,
                 method     = corr_method,
                 min_thrhld = min_thrhld,
                 pct_bool   = pct_bool,
                 prec       = prec,
                 alpha      = alpha)

        rows_list.append(opt_dict)

        i += 1


    opt_df            = pd.DataFrame(rows_list)

    opt_df.index      = list(comp_dict)

    opt_df.index.name = index

    return opt_df


# In[153]:


#*******************************************************************************************
 #
 #  Function Name:  lag_corr_time_series
 #
 #  Function Description:
 #      This function returns correlation between x and y at each lag from -maxlag 
 #      to +maxlag.
 #
 #      Positive lag: x leads y (x predicts future y)
 #      Negative lag: y leads x (y predicts future x)
 #
 #
 #  Return Type: series
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  series         X_series         The parameter is the x-values series.
 #  series         y_series         The parameter is the y-values series.
 #  integer        maxlag          The parameter is the maximum lag.
 #  string         method           The parameter is the correlation method.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def lag_corr_time_series \
        (X_series: pd.Series, 
         y_series: pd.Series, 
         maxlag:   object = None, 
         method:   str    = 'pearson') \
-> pd.Series:

    data_df               = pd.DataFrame({'x': X_series, 'y': y_series}).dropna()


    if maxlag is None: maxlag_int = int(12.0 * (float(len(data_df)) / 100.0)**(0.25))

    else:              maxlag_int = int(abs(maxlag))


    results_dict          = {}

    for lag in range(-maxlag_int, maxlag_int + 1):

        if lag > 0:   corr_flt = data_df['x'].corr(data_df['y'].shift(-lag), method = method)

        elif lag < 0: corr_flt = data_df['x'].shift(lag).corr(data_df['y'],  method = method)

        else:         corr_flt = data_df['x'].corr(data_df['y'],             method = method)


        results_dict[lag] = corr_flt


    results_series = pd.Series(results_dict)

    return results_series


# In[154]:


#*******************************************************************************************
 #
 #  Function Name:  rp_corr_at_lag_time_series
 #
 #  Function Description:
 #      This function returns both r-values and p-values at each lag in the series.
 #      
 #      Positive lag: x leads y. 
 #      Negative lag: y leads x.
 #
 #
 #  Return Type: series, series
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  series         X_series         The parameter is the x-values series.
 #  series         y_series         The parameter is the y-values series.
 #  integer        maxlag           The parameter is the maximum lag.
 #  string         method           The parameter is the correlation method.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def rp_corr_at_lag_time_series \
        (X_series: pd.Series, 
         y_series: pd.Series, 
         maxlag:   int = 180, 
         method:   str = 'pearson') \
-> tuple[pd.Series, pd.Series]:

    method         = dtypesx.strip_rmv_nmbr_space_case(method, case = 'lower')

    data_df        = pd.DataFrame({'X': X_series, 'y': y_series}).dropna()


    r_results_dict = {}

    p_results_dict = {}


    for lag in range(-maxlag, maxlag + 1):

        if lag > 0:

            paired_df \
                = pd.DataFrame \
                    ({'X': data_df['X'].values,
                      'y': data_df['y'].shift(-lag).values}) \
                        .dropna()

        elif lag < 0:

            paired_df \
                = pd.DataFrame \
                    ({'X': data_df['X'].shift(lag).values,
                      'y': data_df['y'].values}) \
                        .dropna()

        else: paired_df = data_df.copy()


        if paired_df['X'].std() == 0 or paired_df['y'].std() == 0:

            r_results_dict[lag] = 0.0

            p_results_dict[lag] = 1.0

        else:

            if   method == 'pearson':  r, p = pearsonr(paired_df['X'], paired_df['y'])

            elif method == 'spearman': r, p = spearmanr(paired_df['X'], paired_df['y'])

            elif method == 'kendall':  r, p = kendalltau(paired_df['X'], paired_df['y'])

            else:                      r, p = None, None


            r_results_dict[lag] = r

            p_results_dict[lag] = p


    r_series = pd.Series(r_results_dict)

    p_series = pd.Series(p_results_dict)


    return r_series, p_series


# In[155]:


#*******************************************************************************************
 #
 #  Function Name:  lag_corr_summ_df
 #
 #  Function Description:
 #      This function returns a summary dataframe with same_day_r, peak_lag_days, peak_r,
 #      peak_p, bonferroni_significant, and improvement for each series. peak_p uses the 
 #      Bonferroni correction for the number of lags tested, since we are selecting the 
 #      peak r from multiple comparisons.
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
 #  dictionary     comp_dict        The parameter is the comparison series dictionary.
 #  integer        maxlag           The parameter is the maximum lag.
 #  string         index            The parameter is the index column name.
 #  integer        prec             The parameter is the output number precision.
 #  float          alpha            The parameter is the p-value threshold.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def lag_corr_summ_df \
        (X_series:  pd.Series, 
         comp_dict: dict, 
         maxlag:    int   = 180,
         index:     str   = 'series',
         prec:      int   = 6,
         alpha:     float = 0.05) \
-> pd.DataFrame:

    num_lags_int              = 2 * maxlag + 1

    rows_list                 = []


    for label, y_series in comp_dict.items():

        corr_method           = find_opt_corr_method(y_series, X_series)

        r_lag_series, p_lag_series \
            = rp_corr_at_lag_time_series \
                (X_series,
                 y_series,
                 maxlag = maxlag,
                 method = corr_method)


        r_same_day_flt        = r_lag_series[0]

        p_same_day_flt        = p_lag_series[0]


        lag_peak_int          = r_lag_series.abs().idxmax()

        r_peak_flt            = r_lag_series[lag_peak_int]


        p_peak_flt            = p_lag_series[lag_peak_int]

        p_peak_bonferroni_flt = min(num_lags_int * p_peak_flt, 1.0)


        sig_bool              = round(p_same_day_flt,        prec) < round(alpha, prec)

        sig_pk_bool           = round(p_peak_bonferroni_flt, prec) < round(alpha, prec)

        r_improv_flt          = round(abs(r_peak_flt) - abs(r_same_day_flt), prec)


        rows_list.append \
            ({index: label,
              'r_same_day':        round(r_same_day_flt,        prec),
              'p_same_day':        round(p_same_day_flt,        prec),
              'significant':       sig_bool,
              'peak_lag':          lag_peak_int,
              'r_peak':            round(r_peak_flt,            prec),
              'raw_p_peak':        round(p_peak_flt,            prec),
              'p_peak_bonferroni': round(p_peak_bonferroni_flt, prec),
              'significant_peak':  sig_pk_bool,
              'r_improvement':     r_improv_flt})


    summ_df \
        = pd.DataFrame \
            (rows_list) \
                .set_index(index) \
                .sort_values('r_improvement', ascending = False)      

    return summ_df


# In[156]:


#*******************************************************************************************
 #
 #  Function Name:  calc_granger_component_score
 #
 #  Function Description:
 #      This function scores the Granger causality component for one X-Y pair. 
 #      To do so, it evaluates both the X->Y and Y->X directions and rewards 
 #      unidirectional causality from X to Y. Bidirectional causality scores 
 #      lower than unidirectional because it weakens the causal interpretation.
 #  
 #      Scoring logic (all values normalized to [0, 1]):
 #          x_causes_y_score  : 1.0 if X->Y significant at best lag, else
 #                              scaled by (1 - min_p_value) to reward
 #                              near-significant results
 #          y_causes_x_score  : inverted — lower is better (we want X->Y,
 #                              not Y->X)
 #          directionality    : 1.0 if X->Y only, 0.5 if bidirectional,
 #                              0.25 if Y->X only, 0.0 if neither
 #          component_score   : weighted combination of the three above
 #
 #
 #  Return Type: dictionary
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  series         X_series         The parameter is an array of time series values and
 #                                  the causal variable (must be stationary).
 #  series         y_series         The parameter is an array of time series values and
 #                                  the effect variable (must be stationary).
 #  integer        minlag           The parameter is the minimum lag.
 #  string         maxlag           The parameter is the maximum lag to test, default 
 #                                  value of 12*(nobs/100)^{1/4} is used when None.
 #  integer        maxlag_lmt       The parameter is the minimum number of observations.
 #  integer        n_splits         The parameter is the number of walk-forward CV folds.
 #  integer        min_obs          The parameter is the minimum number of observations.
 #  string         index            The parameter is the output dataframe index name for
 #                                  score_granger_methods. 
 #  integer        prec             The parameter is the output number precision.
 #  float          alpha            The parameter is the p-value threshold.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def calc_granger_component_score \
        (X_series:   pd.Series,
         y_series:   pd.Series,
         minlag:     int    = 1,
         maxlag:     object = None,
         maxlag_lmt: int    = 60,
         n_splits:   int    = 5,
         min_obs:    int    = 20,
         method:     str    = 'bic',
         index:      str    = 'method',
         prec:       int    = 6,
         alpha:      float  = 0.05) \
-> dict:

    data_df = pd.DataFrame({'X': X_series, 'y': y_series}).dropna()


    X_series = data_df['X']

    y_series = data_df['y']


    grngr_mth, _, _ \
        = find_optimal_granger_method \
            (X_series, 
             y_series,
             minlag   = minlag,
             maxlag   = maxlag,
             n_splits = n_splits,
             min_obs  = min_obs,
             method   = method,
             index    = index,
             prec     = prec,
             alpha    = alpha)

    g_lag, _ \
        = find_optimal_granger_lag \
            (X_series, 
             y_series, 
             minlag  = minlag, 
             maxlag  = maxlag, 
             method  = grngr_mth, 
             min_obs = min_obs)


    _, xy_best_dict \
        = granger_causality_test \
            (X_series, 
             y_series,
             minlag     = minlag,
             maxlag     = g_lag,
             maxlag_lmt = maxlag_lmt,
             method     = grngr_mth,
             min_obs    = min_obs,
             prec       = prec, 
             alpha      = alpha)

    _, yx_best_dict \
        = granger_causality_test \
            (y_series, 
             X_series, 
             minlag     = minlag,
             maxlag     = g_lag,
             maxlag_lmt = maxlag_lmt,
             method     = grngr_mth,
             min_obs    = min_obs,
             prec       = prec, 
             alpha      = alpha)


    xy_p_flt = float(xy_best_dict.get('f_p_value', 1.0))

    yx_p_flt = float(yx_best_dict.get('f_p_value', 1.0))


    x_causes_y_bool = round(xy_p_flt, prec) < round(alpha, prec)

    y_causes_x_bool = round(yx_p_flt, prec) < round(alpha, prec)


    if x_causes_y_bool and not y_causes_x_bool:

        directionality      = 'x_to_y'

        direction_score_flt = 1.0

    elif x_causes_y_bool and y_causes_x_bool:

        directionality      = 'bidirectional'

        direction_score_flt = 0.5

    elif not x_causes_y_bool and y_causes_x_bool:

        directionality      = 'y_to_x'

        direction_score_flt = 0.25

    else:

        directionality      = 'none'

        direction_score_flt = 0.0


    xy_p_score_flt = max(0.0, 1.0 - xy_p_flt)

    yx_penalty_flt = max(0.0, 1.0 - yx_p_flt)


    component_score_flt \
        = (0.50 * direction_score_flt + \
           0.35 * xy_p_score_flt      + \
           0.15 * (1.0 - yx_penalty_flt))

    conclusion \
        = (f'Granger: {directionality} '
           f'(X -> Y p = {xy_p_flt:.{prec}f}, Y -> X p = {yx_p_flt:.{prec}f}). '
           f'Component score: {component_score_flt:.{prec}f}.')


    scores_dict \
        = {'x_causes_y':      x_causes_y_bool,
           'y_causes_x':      y_causes_x_bool,
           'x_causes_y_p':    round(xy_p_flt, prec),
           'y_causes_x_p':    round(yx_p_flt, prec),
           'directionality':  directionality,
           'component_score': round(component_score_flt, prec),
           'conclusion':      conclusion}

    return scores_dict


# In[157]:


#*******************************************************************************************
 #
 #  Function Name:  calc_var_vecm_component_score
 #
 #  Function Description:
 #      This function scores the VAR/VECM component for one X-Y pair using IRF peak 
 #      effect, FEVD x_share_in_y, and model stability.
 #
 #      Scoring logic:
 #          irf_score:       scaled abs(peak x->y IRF magnitude) relative to
 #                           the y-series standard deviation — rewards large
 #                           proportional impulse responses
 #          fevd_score:      x_share_in_y at terminal period — directly measures
 #                           what fraction of y's forecast variance X explains
 #          stable_score:    1.0 if model is stable, 0.0 if not
 #          half_life_score: for VECM only — shorter half-life = faster mean 
 #                           reversion = stronger equilibrium pull; normalized 
 #                           via exp(-half_life / 30)
 #
 #
 #  Return Type: dictionary
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  series         X_series         The parameter is an array of time series values and
 #                                  the causal variable (must be stationary).
 #  series         y_series         The parameter is an array of time series values and
 #                                  the effect variable (must be stationary).
 #  integer        maxlag           The parameter is the maximum lag for VAR/VECM.
 #  integer        min_obs          The parameter is the minimum number of observations.
 #  string         autolag          The parameter is the method to use when automatically 
 #                                  determining the lag length.
 #  integer        periods          The parameter is the forecast horizon for IRF.
 #  boolean        vrb_bool         The parameter is the indicator of verbosity.
 #  integer        prec             The parameter is the output number precision.
 #  float          alpha            The parameter is the p-value threshold.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def calc_var_vecm_component_score \
        (X_series: pd.Series,
         y_series: pd.Series,
         maxlag:   int,
         min_obs:  int   = 20,
         autolag:  str   = 'AIC',
         periods:  int   = 30,
         vrb_bool: bool  = False,
         prec:     int   = 6,
         alpha:    float = 0.05) \
-> dict:

    data_df          = pd.DataFrame({'X': X_series, 'y': y_series}).dropna()


    X_series         = data_df['X']

    y_series         = data_df['y']


    results_dict \
        = fit_var_or_vecm \
            (X_series, 
             y_series, 
             maxlag   = maxlag,
             min_obs  = min_obs,
             autolag  = autolag,
             periods  = periods, 
             vrb_bool = vrb_bool, 
             prec     = prec, 
             alpha    = alpha)


    summary_df       = results_dict['summary_df'].iloc[0]

    irf_dict         = results_dict['irf_result']

    fevd_dict        = results_dict['fevd_result']

    model_type       = results_dict['model_type']


    irf_mag_flt      = abs(float(irf_dict['peak_effect']['magnitude']))

    irf_peak_lag_int = int(irf_dict['peak_effect']['lag'])

    irf_sign         = irf_dict['sign']


    fevd_share_flt   = float(fevd_dict['x_share_in_y'])

    is_stable_bool   = bool(summary_df['is_stable'])

    half_life_flt    = float(summary_df.get('half_life', np.nan))


    y_std_flt        = float(y_series.std())

    irf_score_flt    = min(1.0, irf_mag_flt / y_std_flt) if y_std_flt > 0 else 0.0


    fevd_score_flt   = min(1.0, fevd_share_flt)


    stable_score_flt = 1.0 if is_stable_bool else 0.0


    if model_type == 'vecm' and not np.isnan(half_life_flt) and half_life_flt > 0:

        half_life_score_flt = float(np.exp(-half_life_flt / 30.0))

    else: half_life_score_flt = 0.0


    if model_type == 'vecm':

        component_score_flt \
            = (0.30 * irf_score_flt    + \
               0.30 * fevd_score_flt   + \
               0.25 * stable_score_flt + \
               0.15 * half_life_score_flt)
    else:

        component_score_flt \
            = (0.35 * irf_score_flt  + \
               0.40 * fevd_score_flt + \
               0.25 * stable_score_flt)


    conclusion \
        = (f'VAR/VECM ({model_type.upper()}): '
           f'IRF peak at lag {irf_peak_lag_int} ({irf_sign}), '
           f'FEVD x_share = {fevd_share_flt:.{prec}f}, '
           f'stable = {is_stable_bool}. '
           f'Component score: {component_score_flt:.{prec}f}.')

    half_life_scr_flt \
        = half_life_flt if not np.isnan(half_life_flt) else np.nan


    scores_dict \
        = {'model_type':      model_type,
           'irf_peak_lag':    irf_peak_lag_int,
           'irf_peak_mag':    round(irf_mag_flt,         prec),
           'irf_sign':        irf_sign,
           'fevd_x_share':    round(fevd_share_flt,      prec),
           'half_life':       round(half_life_scr_flt,   prec),
           'is_stable':       is_stable_bool,
           'component_score': round(component_score_flt, prec),
           'conclusion':      conclusion}

    return scores_dict


# In[158]:


#*******************************************************************************************
 #
 #  Function Name:  calc_cointegration_component_score
 #
 #  Function Description:
 #      This function scores the Engle-Granger cointegration component for one X-Y pair.
 #      Cointegration establishes a long-run equilibrium relationship, which supports 
 #      a causal interpretation when combined with Granger results.
 #
 #      Scoring logic:
 #          p_score:      1 - p_value (rewards lower p-values continuously, not
 #                        just binary significant/not)
 #          cointegrated: binary bonus — cointegrated pairs score at least 0.5
 #
 #
 #  Return Type: dictionary
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  series         X_series         The parameter is an array of time series values and
 #                                  the causal variable (must be stationary).
 #  series         y_series         The parameter is an array of time series values and
 #                                  the effect variable (must be stationary).
 #  integer/none   maxlag           The parameter is the maximum lag which is included 
 #                                  in test, default value of 12*(nobs/100)^{1/4} is used 
 #                                  when None.
 #  string         index            The parameter is the output index name.
 #  integer        prec             The parameter is the output number precision.
 #  float          alpha            The parameter is the p-value threshold.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def calc_cointegration_component_score \
        (X_series: pd.Series,
         y_series: pd.Series,
         maxlag:   int    = 20,
         index:    str    = 'series', 
         prec:     int    = 6,
         alpha:    float  = 0.05) \
-> dict:

    data_df             = pd.DataFrame({'X': X_series, 'y': y_series}).dropna()


    X_series            = data_df['X']

    y_series            = data_df['y']


    coint_df \
        = eg_coint_test_summ_df \
            (X_series, 
             comp_dict = {'y': y_series},
             index     = index,
             maxlag    = maxlag,
             prec      = prec,
             alpha     = alpha)

    p_value_flt         = float(coint_df['p_value'].iloc[0])

    cointegrated_bool   = round(p_value_flt, prec) < round(alpha, prec)


    p_score_flt         = max(0.0, 1.0 - p_value_flt)

    coint_bonus_flt     = 0.5 if cointegrated_bool else 0.0


    component_score_flt = min(1.0, 0.5 * p_score_flt + coint_bonus_flt)

    conclusion \
        = (f"Cointegration: {'confirmed' if cointegrated_bool else 'not confirmed'} "
           f'(p = {p_value_flt:.{prec}f}). '
           f'Component score: {component_score_flt:.{prec}f}.')


    scores_dict \
        = {'cointegrated':    cointegrated_bool,
           'p_value':         round(p_value_flt,         prec),
           'component_score': round(component_score_flt, prec), 
           'conclusion':      conclusion}

    return scores_dict


# In[159]:


#*******************************************************************************************
 #
 #  Function Name:  calc_lag_corr_component_score
 #
 #  Function Description:
 #      This function scores the lag correlation component for one X-Y pair. Rewards 
 #      a high peak correlation, a meaningful improvement over same-day correlation,
 #      and a positive lag (X leading Y, not Y leading X).
 #
 #      Scoring logic:
 #          abs_r_peak:    abs(r_peak) — strength of the best delayed correlation
 #          improvement:   r_peak - r_same_day, normalized — rewards cases where
 #                         the lagged relationship is stronger than contemporaneous
 #          lag_sign:      1.0 if peak lag > 0 (X leads Y), 0.5 if lag == 0,
 #                         0.0 if peak lag < 0 (Y leads X)
 #
 #
 #  Return Type: dictionary
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  series         X_series         The parameter is an array of time series values and
 #                                  the causal variable (must be stationary).
 #  series         y_series         The parameter is an array of time series values and
 #                                  the effect variable (must be stationary).
 #  integer        maxlag           The parameter is the search horizon for lag 
 #                                  correlation.
 #  string         index            The parameter is the index column name.
 #  integer        prec             The parameter is the output number precision.
 #  float          alpha            The parameter is the p-value threshold.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def calc_lag_corr_component_score \
        (X_series: pd.Series,
         y_series: pd.Series,
         maxlag:   object = None,
         index:    str    = 'series',
         prec:     int    = 6,
         alpha:    float  = 0.05) \
-> dict:

    data_df           = pd.DataFrame({'X': X_series, 'y': y_series}).dropna()


    X_series          = data_df['X']

    y_series          = data_df['y']


    lag_df \
        = lag_corr_summ_df \
            (X_series, 
             comp_dict = {'y': y_series},
             maxlag    = maxlag,
             index     = index,
             prec      = prec,
             alpha     = alpha)


    r_same_day_flt    = float(lag_df['r_same_day'].iloc[0])

    r_peak_flt        = float(lag_df['r_peak'].iloc[0])


    peak_lag_int      = int(lag_df['peak_lag'].iloc[0])

    r_improvement_flt = float(lag_df['r_improvement'].iloc[0])


    abs_r_score_flt   = abs(r_peak_flt)


    impr_score_flt    = min(1.0, max(0.0, r_improvement_flt))


    if peak_lag_int > 0:    lag_sign_score_flt = 1.0

    elif peak_lag_int == 0: lag_sign_score_flt = 0.5

    else:                   lag_sign_score_flt = 0.0


    component_score_flt \
        = (0.50 * abs_r_score_flt + \
           0.30 * impr_score_flt  + \
           0.20 * lag_sign_score_flt)

    conclusion \
        = (f'Lag correlation: r_peak = {r_peak_flt:.{prec}f} at lag {peak_lag_int} '
           f'(same-day r = {r_same_day_flt:.{prec}f}, '
           f'improvement = {r_improvement_flt:.{prec}f}). '
           f'Component score: {component_score_flt:.{prec}f}.')


    scores_dict \
        = {'r_same_day':      round(r_same_day_flt,      prec),
           'r_peak':          round(r_peak_flt,          prec),
           'peak_lag':        peak_lag_int,
           'r_improvement':   round(r_improvement_flt,   prec),
           'component_score': round(component_score_flt, prec),
           'conclusion':      conclusion}

    return scores_dict


# In[160]:


#*******************************************************************************************
 #
 #  Function Name:  calc_correlation_component_score
 #
 #  Function Description:
 #      This function scores the contemporaneous correlation component for one X-Y pair
 #      using the optimal correlation method already established in the pipeline.
 #
 #     Scoring logic:
 #         abs_r:          abs(correlation coefficient) — strength of association
 #         p_score:        1 - p_value — rewards statistical significance
 #        component_score: weighted combination
 #
 #
 #  Return Type: dictionary
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  series         X_series         The parameter is an array of time series values and
 #                                  the causal variable (must be stationary).
 #  series         y_series         The parameter is an array of time series values and
 #                                  the effect variable (must be stationary).
 #  integer        prec             The parameter is the output number precision.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def calc_correlation_component_score \
        (X_series: pd.Series,
         y_series: pd.Series,
         prec:     int = 6) \
-> dict:

    paired_df = pd.DataFrame({'X': X_series, 'y': y_series}).dropna()

    if paired_df['X'].std() == 0 or paired_df['y'].std() == 0:

        conclusion \
            = ('Correlation undefined: one or both series are constant. '
               'Component score set to 0.0.')

        scores_dict \
            = {'correlation':     0.0,
               'p_value':         1.0,
               'method':          'none',
               'component_score': 0.0,
               'warning':         'constant_input',
               'conclusion':      conclusion}

        return scores_dict


    X_series  = paired_df['X']

    y_series  = paired_df['y']


    method    = find_opt_corr_method(X_series, y_series)


    if method == 'pearson':    r, p = pearsonr(X_series, y_series)

    elif method == 'spearman': r, p = spearmanr(X_series, y_series)

    else:                      r, p = kendalltau(X_series, y_series)


    abs_r_score_flt = abs(float(r))

    p_score_flt     = max(0.0, 1.0 - float(p))


    component_score_flt \
        = (0.60 * abs_r_score_flt + 0.40 * p_score_flt)

    conclusion \
        = (f'Correlation ({method}): r = {r:.{prec}f}, p = {p:.{prec}f}. '
           f'Component score: {component_score_flt:.{prec}f}.')


    scores_dict \
        = {'correlation':     round(float(r),            prec),
           'p_value':         round(float(p),            prec),
           'method':          method,
           'component_score': round(component_score_flt, prec),
           'warning':         None,
           'conclusion':      conclusion}    

    return scores_dict


# In[161]:


#*******************************************************************************************
 #
 #  Function Name:  score_one_xy_pair
 #
 #  Function Description:
 #      This function computes the full weighted causal association score for one X-Y 
 #      pairby running all five component scorers and combining them.
 #
 #
 #  Return Type: dictionary
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  series         X_series         The parameter is an array of time series values and
 #                                  the causal variable (must be stationary).
 #  series         y_series         The parameter is an array of time series values and
 #                                  the effect variable (must be stationary).
 #  string         y_name           The parameter is the label for the Y series (used in 
 #                                  output).
 #  dict           weights_dict     The parameter is the component weights dictionary.
 #  integer        periods          The parameter is the forecast horizon for IRF.

 #  integer        minlag           The parameter is the minimum lag.
 #  integer        maxlag           The parameter is the search horizon for lag 
 #                                  correlation.
 #  integer        maxlag_lmt       The parameter is the minimum number of observations.
 #  integer        n_splits         The parameter is the number of walk-forward CV folds.
 #  integer        min_obs          The parameter is the minimum number of observations.
 #  string         autolag          The parameter is the method to use when automatically 
 #                                  determining the lag length.
 #  string         method           The parameter is the correlation method.
 #  string         mth_index        The parameter is the output dataframe index name.
 #  string         srs_index        The parameter is the output dataframe index name.
 #  boolean        vrb_bool         The parameter is the indicator of verbosity.
 #  integer        prec             The parameter is the output number precision.
 #  float          alpha            The parameter is the p-value threshold.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def score_one_xy_pair \
        (X_series:     pd.Series,
         y_series:     pd.Series,
         y_name:       str,
         weights_dict: dict \
                        = {'granger':       0.30,  # causal direction and significance
                           'var_vecm':      0.25,  # system dynamics, IRF, FEVD
                           'cointegration': 0.20,  # long-run equilibrium relationship
                           'lag_corr':      0.15,  # peak delayed association
                           'correlation':   0.10}, # contemporaneous association
         periods:      int    = 30,
         minlag:       int    = 1,
         maxlag:       int    = 20,
         maxlag_lmt:   int    = 60,
         n_splits:     int    = 5,
         min_obs:      int    = 20,
         autolag:      str    = 'AIC',
         method:       str    = 'bic',
         mth_index:    str    = 'method',
         srs_index:    str    = 'series',
         vrb_bool:     bool   = False,
         prec:         int    = 6,
         alpha:        float  = 0.05) \
-> dict:

    data_df           = pd.DataFrame({'X': X_series, 'y': y_series}).dropna()


    X_series          = data_df['X']

    y_series          = data_df['y']


    if maxlag is None: maxlag_int = int(12.0 * (float(len(data_df)) / 100.0)**(0.25))

    else:              maxlag_int = int(abs(maxlag))


    granger_res_dict \
        = calc_granger_component_score \
            (X_series, 
             y_series, 
             minlag     = minlag, 
             maxlag     = maxlag_int, 
             maxlag_lmt = maxlag_lmt,
             n_splits   = n_splits,
             min_obs    = min_obs,
             method     = method,
             index      = mth_index,
             prec       = prec, 
             alpha      = alpha)

    var_vecm_res_dict \
        = calc_var_vecm_component_score \
            (X_series, 
             y_series, 
             maxlag   = maxlag_int,
             min_obs  = min_obs,
             autolag  = autolag,
             periods  = periods,
             vrb_bool = vrb_bool,
             prec     = prec,
             alpha    = alpha)


    coint_res_dict \
        = calc_cointegration_component_score \
            (X_series, 
             y_series,
             maxlag = maxlag_int,
             index  = srs_index,
             prec   = prec,
             alpha  = alpha)

    lag_res_dict \
        = calc_lag_corr_component_score \
            (X_series,
             y_series,
             maxlag = maxlag_int * 3,
             index  = srs_index,
             prec   = prec,
             alpha  = alpha)

    corr_res_dict     = calc_correlation_component_score(X_series, y_series, prec = prec)


    component_scores_dict \
        = {'granger':       granger_res_dict['component_score'],
           'var_vecm':      var_vecm_res_dict['component_score'],
           'cointegration': coint_res_dict['component_score'],
           'lag_corr':      lag_res_dict['component_score'],
           'correlation':   corr_res_dict['component_score']}

    weighted_score_flt \
        = sum \
            (component_scores_dict[k] * weights_dict[k] \
             for k in weights_dict)

    conclusion \
        = (f'Pair X vs. {y_name} — weighted score: {weighted_score_flt:.{prec}f}. '
           f"Granger = {component_scores_dict['granger']:.{prec}f} (w = {weights_dict['granger']}), "
           f"VAR/VECM = {component_scores_dict['var_vecm']:.{prec}f} (w = {weights_dict['var_vecm']}), "
           f"Coint = {component_scores_dict['cointegration']:.{prec}f} (w = {weights_dict['cointegration']}), "
           f"LagCorr = {component_scores_dict['lag_corr']:.{prec}f} (w = {weights_dict['lag_corr']}), "
           f"Corr = {component_scores_dict['correlation']:.{prec}f} (w = {weights_dict['correlation']}).")


    scores_dict \
        = {'y_name':           y_name,
           'granger':          granger_res_dict,
           'var_vecm':         var_vecm_res_dict,
           'cointegration':    coint_res_dict,
           'lag_corr':         lag_res_dict,
           'correlation':      corr_res_dict,
           'weighted_score':   round(weighted_score_flt, prec),
           'component_scores': component_scores_dict,
           'conclusion':       conclusion}

    return scores_dict


# In[162]:


#*******************************************************************************************
 #
 #  Function Name:  build_causal_score_summary_df
 #
 #  Function Description:
 #      This function assembles a summary DataFrame from a list of scored X-Y pairs, 
 #      with one row per Y series and columns for every component score, key diagnostic 
 #      values, and the final weighted score.
 #
 #
 #  Return Type: dataframe
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  list[dict]     pair_results_list     
 #                                  The parameter is the list of outputs from 
 #                                  score_one_xy_pair.
 #  boolean        scr_pct_bool     The parameter is the indicator of the scores being 
 #                                  percents.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def build_causal_score_summary_df \
        (pair_results_list: list[dict],
         scr_pct_bool:      bool = False) \
-> pd.DataFrame:

    rows_list = []

    for r in pair_results_list:

        if scr_pct_bool: fct_flt = 100.0

        else:            fct_flt = 1.0

        rows_list.append \
            ({'y_name':            r['y_name'],
              'weighted_score':    r['weighted_score']                    * fct_flt,
              'granger_score':     r['component_scores']['granger']       * fct_flt,
              'var_vecm_score':    r['component_scores']['var_vecm']      * fct_flt,
              'coint_score':       r['component_scores']['cointegration'] * fct_flt,
              'lag_corr_score':    r['component_scores']['lag_corr']      * fct_flt,
              'corr_score':        r['component_scores']['correlation']   * fct_flt,
              'granger_direction': r['granger']['directionality'],
              'x_causes_y_p':      r['granger']['x_causes_y_p'],
              'y_causes_x_p':      r['granger']['y_causes_x_p'],
              'irf_sign':          r['var_vecm']['irf_sign'],
              'fevd_x_share':      r['var_vecm']['fevd_x_share'],
              'cointegrated':      r['cointegration']['cointegrated'],
              'r_peak':            r['lag_corr']['r_peak'],
              'peak_lag':          r['lag_corr']['peak_lag']})


    scores_df \
        = pd.DataFrame(rows_list) \
              .set_index('y_name') \
              .sort_values('weighted_score', ascending = False)

    return scores_df


# In[163]:


#*******************************************************************************************
 #
 #  Function Name:  score_x_vs_y_dict
 #
 #  Function Description:
 #      This function computes the full weighted causal association score for X against 
 #      each y series in y_dict and returns both the per-pair details and a ranked
 #     summary dataframe.
 #
 #
 #  Return Type: integer, dictionary
 #
 #
 #  Function Parameters:
 #
 #  Type           Name             Description
 #  ------------   --------------   --------------------------------------------------
 #  series         X_series         The parameter is an array of time series values and
 #                                  the causal variable (must be stationary).
 #  dictionary     y_dict           The parameter is the y series keyed by name.
 #  dict           weights_dict     The parameter is the component weights dictionary.
 #  integer        minlag           The parameter is the minimum lag.
 #  integer        maxlag           The parameter is the maximum lag for Granger and 
 #                                  VAR/VECM.
 #  integer        periods          The parameter is the forecast horizon for IRF.
 #  boolean        vrb_bool         The parameter is the indicator of verbosity.
 #  integer        prec             The parameter is the output number precision.
 #  float          alpha            The parameter is the p-value threshold.
 #  boolean        scr_pct_bool     The parameter is the indicator of the scores being 
 #                                  percents.
 #  string         causal_version   The parameter is the causal version.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  02/24/2026          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def score_x_vs_y_dict \
        (X_series:       pd.Series,
         y_dict:         dict[str, pd.Series],
         weights_dict:   dict \
                            = {'granger':       0.30,  # causal direction and significance
                               'var_vecm':      0.25,  # system dynamics, IRF, FEVD
                               'cointegration': 0.20,  # long-run equilibrium relationship
                               'lag_corr':      0.15,  # peak delayed association
                               'correlation':   0.10}, # contemporaneous association
         minlag:         int    = 1,
         maxlag:         object = None,
         maxlag_lmt:     int    = 60,
         periods:        int    = 30,
         n_splits:       int    = 5,
         min_obs:        int    = 20,
         autolag:        str    = 'BIC',
         method:         str    = 'bic',
         mth_index:      str    = 'method',
         srs_index:      str    = 'series',
         vrb_bool:       bool   = False,
         prec:           int    = 6,
         alpha:          float  = 0.05,
         scr_pct_bool:   bool   = False,
         causal_version: str    = '1.0') \
-> tuple[float, dict]:

    if abs(sum(weights_dict.values()) - 1.0) > 1e-9:

        logx.print_and_log_text \
            ('\033[1m'
             + 'Weights must sum to 1.0. The current sum is ' \
                 f'{sum(weights_dict.values()):.{prec}f}.'
             + '\033[0m')


    if maxlag is None: maxlag_int = int(12.0 * (float(len(X_series)) / 100.0)**(0.25))

    else:              maxlag_int = int(abs(maxlag))


    pair_results_list \
        = [score_one_xy_pair \
               (X_series,
                y_series,
                y_name       = y_name,
                weights_dict = weights_dict,
                periods      = periods,
                minlag       = minlag,
                maxlag       = maxlag_int,
                maxlag_lmt   = maxlag_lmt,
                n_splits     = n_splits,
                min_obs      = min_obs,
                autolag      = autolag,
                method       = method,
                mth_index    = mth_index,
                srs_index    = srs_index,
                vrb_bool     = vrb_bool,
                prec         = prec,
                alpha        = alpha) \
           for y_name, y_series in y_dict.items()]


    summary_df        = build_causal_score_summary_df(pair_results_list, scr_pct_bool = scr_pct_bool)

    overall_score_flt = round(float(summary_df['weighted_score'].mean()), prec)


    best_pair         = summary_df['weighted_score'].idxmax()

    strict_pair        = summary_df['weighted_score'].idxmin()


    conclusion \
        = (f'Causal association score (v{causal_version}): '
           f'overall mean = {overall_score_flt:.{prec}f} across {len(y_dict)} Y series. '
           f'Strongest pair: {best_pair} '
           f"({summary_df.loc[best_pair, 'weighted_score']:.{prec}f}). "
           f'Weakest pair: {strict_pair} '
           f"({summary_df.loc[strict_pair, 'weighted_score']:.{prec}f}). "
           'Weights — ' + ', '.join(f'{k} = {v}' for k, v in weights_dict.items()) + '.')


    scores_dict \
        = {'pair_results':  pair_results_list,
           'summary_df':    summary_df,
           'overall_score': overall_score_flt,
           'best_pair':     best_pair,
           'strict_pair':   strict_pair,
           'weights_used':  weights_dict,
           'conclusion':    conclusion}     

    return overall_score_flt, scores_dict


# In[ ]:




