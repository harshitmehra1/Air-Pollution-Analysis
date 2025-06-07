# scripts/data_cleaning.py

import pandas as pd
import numpy as np

def load_and_clean_data(filepath):
    df = pd.read_csv(filepath, encoding='latin1')
    
    # Split 'City' column into 'Country' and 'CityName'
    df[['Country', 'CityName']] = df.apply(lambda row: pd.Series({
        'Country': row['City'].split(',')[-1].strip(),
        'CityName': row['City'].split(',')[0].replace(row['City'].split(',')[-1].strip(), '').strip()
    }), axis=1)

    # Drop original 'City' column
    df = df.drop(columns=['City'])

    # Clean columns
    columns_to_clean = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG',
                        'SEP', 'OCT', 'NOV', 'DEC', '2021', '2020', '2019', '2018', '2017']
    
    for col in columns_to_clean:
        df[col] = df[col].replace('-', np.nan)
        df[col] = pd.to_numeric(df[col], errors='coerce')
    
    # Reorder columns for better readability
    cols = ['Rank', 'CityName', 'Country', 'JAN', 'FEB', 'MAR', 'APR', 'MAY',
            'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC', '2017', '2018', '2019', '2020', '2021', '2022']

    df = df[cols]
    
    return df
