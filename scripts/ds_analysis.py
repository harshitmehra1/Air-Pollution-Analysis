# scripts/ds_analysis.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.linear_model import LinearRegression


def forecast_pollution(df, cities_to_forecast):
    print("\n--- Forecasting 2023 & 2024 ---")
    
    year_cols = ['2017', '2018', '2019', '2020', '2021', '2022']

    # Prepare overall graph
    plt.figure(figsize=(10, 6))

    for city in cities_to_forecast:
        print(f"\nForecast for {city}:")
        
        city_df = df[df['CityName'].str.lower() == city.lower()]
        
        if city_df.empty:
            print(f"City '{city}' not found in data.")
            continue
        
        # Extract valid years and values
        pollution_series = city_df[year_cols].iloc[0]
        valid_years = []
        valid_values = []

        for year in year_cols:
            value = pollution_series[year]
            if not np.isnan(value):
                valid_years.append(int(year))
                valid_values.append(value)
        
        # Check if enough data is available
        if len(valid_years) < 3:
            print("Not enough data to forecast reliably (need at least 3 years). Skipping.")
            continue
        
        # Prepare data for model
        X = np.array(valid_years).reshape(-1, 1)
        y = np.array(valid_values)

        # Train model
        model = LinearRegression()
        model.fit(X, y)

        # Predict for future years
        future_years = np.array([2023, 2024]).reshape(-1, 1)
        future_preds = model.predict(future_years)

        # Print forecast
        for year, pred in zip([2023, 2024], future_preds):
            print(f"  Year {year}: Predicted Pollution = {pred:.2f}")

        # Plot historical part → solid line and get the color used
        line_hist, = plt.plot(valid_years, valid_values, marker='o', linestyle='-', label=f'{city} (historical)')
        color = line_hist.get_color()

        # Plot forecast part → dotted line with the same color
        plt.plot([2022, 2023, 2024], [valid_values[-1]] + future_preds.tolist(), 
            marker='x', linestyle='--', label=f'{city} (forecast)', color=color)


    # Finalize combined graph
    plt.title("Pollution Forecast 2023-2024 for Selected Cities")
    plt.xlabel("Year")
    plt.ylabel("Pollution Level")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    # Save combined graph
    plt.savefig('outputs/graphs/forecast_combined.png')
    plt.show()




# Code for Anomaly detection :  

def detect_anomalous_indian_cities(df):
    print("\n--- Detecting Anomalous Indian Cities (Volatility Based) ---")

    year_cols = ['2017', '2018', '2019', '2020', '2021', '2022']

    # Filter Indian cities
    india_df = df[df['Country'].str.lower() == 'india']

    volatility_list = []

    for idx, row in india_df.iterrows():
        city = row['CityName']
        
        # Force pollution values to float
        pollution_values = row[year_cols].values.astype(float)

        # Skip if too many NaN
        if np.isnan(pollution_values).sum() > 2:
            continue

        # Forward fill small missing gaps
        pollution_values = pd.Series(pollution_values).fillna(method='ffill').fillna(method='bfill').values

        # Calculate % year-over-year change
        pct_changes = []
        for i in range(1, len(pollution_values)):
            prev = pollution_values[i-1]
            curr = pollution_values[i]
            pct_change = ((curr - prev) / prev) * 100 if prev != 0 else 0
            pct_changes.append(pct_change)

        # Calculate volatility (std deviation of % changes)
        volatility = np.std(pct_changes)

        volatility_list.append((city, volatility))

    # Create dataframe
    volatility_df = pd.DataFrame(volatility_list, columns=['CityName', 'Volatility'])

    # Top 5 anomalous cities (highest volatility)
    top5_anomalous = volatility_df.sort_values(by='Volatility', ascending=False).head(5)

    print("\nTop 5 Anomalous Indian Cities (by volatility):")
    print(top5_anomalous)

    
    # Plot
    plt.figure(figsize=(8, 5))
    sns.barplot(data=top5_anomalous, x='Volatility', y='CityName', palette='coolwarm')

    plt.title("Top 5 Anomalous Indian Cities (Pollution Volatility)")
    plt.xlabel("Volatility (% change std dev)")
    plt.ylabel("City Name")

    # Add the actual value as text at end of each bar
    for index, value in enumerate(top5_anomalous['Volatility']):
        plt.text(
            value - 4,  # a little offset to the right of bar
            index,      # y position
            f'{value:.2f}%',  # formatted text
            va='center',  # vertical alignment
            ha='center', 
            fontsize=10,
            color='black'
        )

    plt.tight_layout()
    plt.savefig('outputs/graphs/anomalous_indian_cities.png')
    plt.show()
