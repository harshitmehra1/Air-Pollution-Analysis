from scripts.data_cleaning import load_and_clean_data

# Load and clean data
df = load_and_clean_data('data/Air Pollution.csv')

# Basic checks
print(df.info())
print(df.head())
