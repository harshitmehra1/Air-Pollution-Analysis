# main.py

from scripts.data_cleaning import load_and_clean_data
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

# Set Seaborn style
sns.set(style="whitegrid")

# Create output folders
os.makedirs('outputs/graphs', exist_ok=True)
os.makedirs('outputs', exist_ok=True)

# Load and clean data
df = load_and_clean_data('data/Air Pollution.csv')
df.to_csv('data/cleaned_air_pollution.csv', index=False)

print("\n==============================")
print("📊 Data Cleaning Done")
print("==============================")

# --- 1. Multi-line Plot: Mumbai, Pune, Nashik ---
print("\n==============================")
print("📈 Plot: Mumbai vs Pune vs Nashik – Pollution Over Years")
print("==============================")

neubrain_cities = ['Mumbai', 'Pune', 'Nashik']
df_neubrain = df[df['CityName'].isin(neubrain_cities)]
df_neubrain = df_neubrain.set_index('CityName')[['2017', '2018', '2019', '2020', '2021', '2022']].T

plt.figure(figsize=(10, 6))
for city in df_neubrain.columns:
    sns.lineplot(data=df_neubrain[city], label=city, marker="o")
plt.title('Pollution Trend (2017–2022) – Mumbai, Pune, Nashik')
plt.xlabel('Year')
plt.ylabel('Pollution Level')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('outputs/graphs/neubrain_cities_trend.png')
plt.show()

# --- 2. Top 10 Most Polluted Cities in 2022 ---
print("\n==============================")
print("⚠️  Top 10 Most Polluted Cities (2022)")
print("==============================")

top10_polluted = df[['CityName', 'Country', '2022']].sort_values(by='2022', ascending=False).head(10)
top10_polluted.to_csv('outputs/top10_most_polluted_2022.csv', index=False)

plt.figure(figsize=(10, 6))
sns.barplot(data=top10_polluted, y="CityName", x="2022", hue="CityName", dodge=False, palette="Reds_r", legend=False)
plt.title('Top 10 Most Polluted Cities (2022)')
plt.xlabel('Pollution Level')
plt.ylabel('City')
plt.tight_layout()
plt.savefig('outputs/graphs/top10_polluted_2022.png')
plt.show()

# --- 3. Top 10 Least Polluted Cities in 2022 ---
print("\n==============================")
print("🍃 Top 10 Least Polluted Cities (2022)")
print("==============================")

least10_polluted = df[['CityName', 'Country', '2022']].dropna().sort_values(by='2022', ascending=True).head(10)
least10_polluted.to_csv('outputs/top10_least_polluted_2022.csv', index=False)

plt.figure(figsize=(10, 6))
sns.barplot(data=least10_polluted, y="CityName", x="2022", hue="CityName", dodge=False, palette="Greens_r", legend=False)
plt.title('Top 10 Least Polluted Cities (2022)')
plt.xlabel('Pollution Level')
plt.ylabel('City')
plt.tight_layout()
plt.savefig('outputs/graphs/top10_least_polluted_2022.png')
plt.show()

# --- 4. Monthly Average Pollution (India – 2022) ---
print("\n==============================")
print("📅 Monthly Average Pollution (India – 2022)")
print("==============================")

monthly_avg = df[['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN',
                  'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']].mean()

plt.figure(figsize=(10, 6))
sns.lineplot(x=monthly_avg.index, y=monthly_avg.values, marker='o', color='steelblue')
plt.title('Monthly Average Pollution (India – 2022)')
plt.xlabel('Month')
plt.ylabel('Average Pollution Level')
plt.grid(True)
plt.tight_layout()
plt.savefig('outputs/graphs/monthly_avg_pollution.png')
plt.show()

# --- 5. Cities with Most Improvement & Decline (2017 vs 2022) ---
print("\n==============================")
print("🔄 Pollution Improvement vs Decline (2017–2022)")
print("==============================")

df['Change_2017_2022'] = df['2022'] - df['2017']
change_df = df[['CityName', 'Change_2017_2022']].dropna()
top_changes = change_df.sort_values(by='Change_2017_2022', ascending=False)

top_worsened = top_changes.head(5)
top_improved = top_changes.tail(5)
compare_df = pd.concat([top_improved, top_worsened])
compare_df = compare_df.set_index('CityName')

plt.figure(figsize=(10, 6))
colors = ['#ff9999' if x > 0 else '#a8e6cf' for x in compare_df['Change_2017_2022']]
compare_df['Change_2017_2022'].plot(kind='barh', color=colors)
plt.axvline(0, color='black', linestyle='--')
plt.title('Cities with Most Improvement & Decline (2017–2022)')
plt.xlabel('Change in Pollution Level')
plt.tight_layout()
plt.savefig('outputs/graphs/improvement_vs_decline.png')
plt.show()

# --- 6. Data Science Analysis - Forecast ---
print("\n==============================")
print("🔮 Forecasting 2023 & 2024")
print("==============================")

from scripts.ds_analysis import forecast_pollution
forecast_cities = ["Mumbai", "Nashik", "Pune"]
forecast_pollution(df, forecast_cities)

# --- 7. Anomaly Detection ---
print("\n==============================")
print("⚠️  Detecting Anomalous Indian Cities (Volatility Based)")
print("==============================")

from scripts.ds_analysis import detect_anomalous_indian_cities
detect_anomalous_indian_cities(df)
