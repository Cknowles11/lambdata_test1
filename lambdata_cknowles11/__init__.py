from .df_utils import ONES, ZEROS
import pandas as pd
import numpy as np

__version__ = "0.0.1"
my_str = "This is my string from __init__.py"
day_month_year = def day_month_year(df, column):
    df =df.copy()
    df["day"] = df[column].dt.day
    df["month"] = df[column].dt.month
    df["year"] = df[column].dt.year
    return df

add_list = def add_list(df, series, name):
    df = df.copy()
    series = pd.Series(series)
    df[name] = series
    return df

