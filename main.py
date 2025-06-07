# main.py

from scripts.data_cleaning import load_and_clean_data
import matplotlib.pyplot as plt
import pandas as pd

# Load and clean data
df = load_and_clean_data('data/Air Pollution.csv')

# Check basic info
print(df.info())
print(df.head())

# --- Top 10 Most Polluted Cities ---
top10_polluted = df[['City', '2022']].sort_values(by='2022', ascending=False).head(10)
print("\nTop 10 Most Polluted Cities in 2022:")
print(top10_polluted)
top10_polluted.to_csv('outputs/top10_most_polluted_2022.csv', index=False)

# --- Top 10 Least Polluted Cities ---
least_polluted = df[df['2022'] > 0][['City', '2022']].sort_values(by='2022', ascending=True).head(10)
print("\nTop 10 Least Polluted Cities in 2022:")
print(least_polluted)
least_polluted.to_csv('outputs/top10_least_polluted_2022.csv', index=False)

# --- Monthly Trend Plot ---
monthly_avg = df[['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN',
                  'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']].mean()

plt.figure(figsize=(10, 6))
monthly_avg.plot(marker='o', color='blue')
plt.title('Monthly Average Pollution (2022)')
plt.xlabel('Month')
plt.ylabel('Average Pollution Level')
plt.grid(True)
plt.savefig('outputs/graphs/monthly_trend_2022.png')
plt.show()

# --- Yearly Trend Plot ---
yearly_avg = df[['2017', '2018', '2019', '2020', '2021', '2022']].mean()

plt.figure(figsize=(8, 6))
yearly_avg.plot(marker='o', color='green')
plt.title('Yearly Average Pollution Trend')
plt.xlabel('Year')
plt.ylabel('Average Pollution Level')
plt.grid(True)
plt.savefig('outputs/graphs/yearly_trend.png')
plt.show()



# Save the full cleaned data to CSV for Power BI use
df.to_csv('data/cleaned_air_pollution.csv', index=False)

