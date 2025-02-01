import pandas as pd

def data_preparation(df, multivariate_var=False, target_var=False):
    df['Month'] = pd.to_datetime(df['Month'], format='%b %Y')
    df = df.sort_values(by=['Month']).reset_index(drop=True)
    df = df.dropna()
    
    # option to exclude old data to ensure each multivariate dataframe have the same time frame
    if multivariate_var == True:
        if target_var == True:
            df = df[df['Month'].dt.year <= 2024].reset_index(drop=True)
        else: 
            df = df[df['Month'].dt.year <= 2022].reset_index(drop=True)
            
        df = df[df['Month'].dt.year >= 2000].reset_index(drop=True)
            
    else:
        # exclude projection data from df
        df = df[df['Month'].dt.year <= 2024].reset_index(drop=True)
        
    df = df.set_index('Month')  

    return df
