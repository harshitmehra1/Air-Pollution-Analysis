# src/data_cleaning.py

import pandas as pd
import numpy as np

def load_and_clean_data(filepath):
    df = pd.read_csv(filepath, encoding='latin1')
    
    columns_to_clean = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG',
                        'SEP', 'OCT', 'NOV', 'DEC', '2021', '2020', '2019', '2018', '2017']
    
    for col in columns_to_clean:
        df[col] = df[col].replace('-', np.nan)
        df[col] = pd.to_numeric(df[col], errors='coerce')
    
    return df
