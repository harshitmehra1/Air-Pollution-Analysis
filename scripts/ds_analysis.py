# scripts/ds_analysis.py

import matplotlib.pyplot as plt
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

