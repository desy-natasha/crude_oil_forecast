import numpy as np
import pandas as pd
from statsmodels.tsa.stattools import grangercausalitytests, adfuller
from sklearn.metrics import mean_absolute_error, mean_squared_error

#define a function to do ADF Test (Stationary Test)
def adfuller_test(series, signif=0.05, name=''):
    r = adfuller(series)

    # Print Summary
    print(f' Augmented Dickey-Fuller Test on "{name}"', "\n   ", '-'*47)
    print(f' Null Hypothesis: Data has unit root. Non-Stationary.')
    print(f' Significance Level    = {signif}')
    print(f' Test Statistic        = {r[0]}')

    p_value = r[1]
    if p_value <= signif:
        print(f" => P-Value = {p_value} Rejecting Null Hypothesis.")
        print(f" => Series is Stationary.")
    else:
        print(f" => P-Value = {p_value}")
        print(f" => Series is Non-Stationary.")    

# define a function to do Grangers Causality Test
def grangers_causation_test(data, variables, target_var, test='ssr_chi2test', maxlag=15):    
    df = pd.DataFrame(np.zeros((1, len(variables))), columns=variables)

    for c in df.columns:
        test_result = grangercausalitytests(data[[target_var, c]], maxlag=maxlag, verbose=False)
        p_values = [round(test_result[i+1][0][test][1],4) for i in range(maxlag)]
        min_p_value = np.min(p_values)
        df.loc[0, c] = min_p_value

    return df 

def invert_differentiation(df_train, df_forecast, col_name):
    df_fc = df_forecast.copy()
    invert_forecast = df_train[col_name].iloc[-1] + df_fc.cumsum()
    
    return invert_forecast

def evaluate_forecast(model, df_validation, df_forecast):
    mae = mean_absolute_error(df_validation, df_forecast)
    mse = mean_squared_error(df_validation, df_forecast)
    rmse = np.sqrt(mse)

    print("Model:", model)
    print("MAE:", mae)
    print("MSE:", mse)
    print("RMSE:", rmse, "\n")