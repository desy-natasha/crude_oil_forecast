import seaborn as sns
import matplotlib.pyplot as plt

def price_time_series_plot(df,y_axis,y_label,title,forecast=False,df_forecast=None):
    fig = plt.figure(figsize=(23,5))
    palette = sns.color_palette('mako')

    sns.lineplot(data=df, x='Month', y=y_axis, palette=palette) 

    if forecast == True:
        sns.lineplot(data=df_forecast, x='Month', y=y_axis, palette=palette)
        plt.legend(['Actual Value','Forecast Value'])

    plt.ylabel(y_label)
    plt.title(title)
    
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(25,7))

def production_consumption_time_series_plot(df_prod,df_cons,y_axis,y_label,country):
    # create figure with two axes side-by-side
    fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(23, 5))
    palette = sns.color_palette('mako')

    sns.lineplot(data=df_prod, x='Month', y=y_axis, palette=palette, ax=ax1) 
    ax1.set_ylabel(y_label)
    ax1.set_title(country+' Petroleum Production')

    sns.lineplot(data=df_cons, x='Month', y=y_axis.replace('Production', 'Consumption'), palette=palette, ax=ax2) 
    ax2.set_ylabel(y_label.replace('Production', 'Consumption'))
    ax2.set_title(country+' Petroleum Consumption')

    plt.tight_layout()
    plt.show()