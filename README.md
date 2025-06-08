# 🌍 Air Pollution Analysis Project

This repository contains an exploratory data analysis (EDA) project on global air pollution trends.  
It was created as part of an internship assignment for **Neubrain Solutions**, an AI & Strategy consulting firm based in Mumbai.

- **Skills demonstrated:** Data Cleaning, Exploratory Analysis, Insight Communication, Data Visualization, Time Series Forecasting, Anomaly Detection  
- **Tools used:** Python (Pandas, Seaborn, Matplotlib, Scikit-Learn)



---



## 📌 Project Overview

Air pollution is one of the most urgent environmental challenges globally.  
This project analyzes pollution levels across hundreds of cities over several years to uncover key patterns, detect anomalies, and generate **forecast-driven** and **volatility-based** visuals for strategic decisions.

**Special focus** was given to **Mumbai, Pune, and Nashik** — locations where **Neubrain Solutions** has its offices (as per their website) — to provide actionable insights for their own city environments.



---



## 🛠️ Process

### 1️⃣ Data Cleaning

- Replaced placeholder values (`-`) with `NaN`
- Converted all pollution columns to numeric format
- Split the original `City` column into two separate columns: `CityName` and `Country`
- Rearranged year columns (`2017` to `2022`) into chronological order
- Saved the cleaned dataset as `data/cleaned_air_pollution.csv` for reuse in visualizations



---



## 📊 Visual Analysis (Python + Seaborn/Matplotlib)

### 📈 1. Mumbai vs Pune vs Nashik – Pollution Over Years
![City Trend](outputs/graphs/neubrain_cities_trend.png)

**Interpretation:**  
This multi-line chart shows how air pollution levels changed in three key Maharashtra cities between 2017 and 2022.  

- All cities saw a **dip in 2020**, most likely due to **COVID-19 lockdowns** and reduced human activity.
- **Pune** maintained a **relatively lower pollution level** compared to Mumbai and Nashik throughout the years.
- **Mumbai and Nashik** showed **higher and more fluctuating pollution trends**.

> **Why these cities?**  
> Neubrain Solutions has offices in these three cities — this visualization helps inform **strategic decisions** and **regional presence**.

**Additional Insight:**  
The chart reflects trends in **PM2.5 concentration**, which is a key indicator of air quality and health risk.  
Further analysis can explore **seasonal trends** or **policy interventions** that influenced these trends.



---



### 🌆 2. Top 10 Most Polluted Cities (2022)
![Top Polluted](outputs/graphs/top10_polluted_2022.png)

**Interpretation:**  

This enhanced bar chart uses a **red color gradient** to visually represent the **intensity of pollution** across the most polluted cities in 2022.

- Most of the top 10 cities are in **India**, highlighting a **severe regional concentration** of air quality issues in the country.
- Cities with **extremely high pollution levels** (deep red bars) should be **prioritized** for policy interventions, urban planning, and public health actions.
- The list is dominated by **industrial hubs** and **high-density urban areas**.

**Additional Insight:**  
Many of these cities also face **seasonal pollution events** (e.g., **stubble burning** in North India).  
Understanding whether pollution is **steady or spikes seasonally** is critical for designing **effective responses**.



---



### 🍃 3. Top 10 Least Polluted Cities (2022)
![Least Polluted](outputs/graphs/top10_least_polluted_2022.png)

**Interpretation:**  

This bar chart highlights the cities with the **cleanest air in 2022**, using a **green color gradient** to indicate lower pollution levels.

- The **lightest bars** represent the cities with the **lowest PM2.5 levels**.
- These often correspond to regions with **lower industrial activity**, **better environmental regulations**, or **natural geographic advantages**.
- These cities can serve as **benchmarks or models** for cleaner air strategies in other regions.

**Additional Insight:**  
It would be valuable to analyze whether these cities:

- Are located in **hilly / coastal regions** with better air circulation.
- Have implemented **successful pollution control policies**.
- Benefit from **lower population density** or **sustainable urban planning**.



---



### 📅 4. Monthly Average Pollution Trend (India – 2022)
![Monthly Average](outputs/graphs/monthly_avg_pollution.png)

**Interpretation:**  

This line chart shows the **monthly average PM2.5 levels across India** for the year 2022.

- **Pollution peaks during the winter months** (Nov–Jan), likely driven by:
  - **Temperature inversion**, trapping pollutants near the ground.
  - **Stubble burning** in northern India.
  - **Firecrackers** during festivals.
  - **Increased use of heating and industrial processes**.
  
- **Pollution drops during monsoon and summer months** (June–August), when:
  - **Rainfall helps wash out particulates**.
  - **Wind patterns improve air circulation**.

**Additional Insight:**  
Public health measures — such as **air quality advisories**, **temporary restrictions**, and **awareness campaigns** — should be **timed seasonally** to protect vulnerable populations during **peak pollution months**.



---



### 🔄 5. Pollution Improvement vs Decline (2017–2022)
![Change Chart](outputs/graphs/improvement_vs_decline.png)

**Interpretation:**  


This comparative chart shows:

- **Top 10 cities with the most improvement** in air quality (marked in **green**).
- **Top 10 cities with the worst decline** in air quality (marked in **red**) between 2017 and 2022.

- **Cities like Pune** have shown **significant improvement**, likely due to:
  - **Effective pollution control measures**
  - **Regulatory actions**
  - **Shifts in industry or transportation patterns**

- **Cities like Jaipur** saw **notable worsening trends**, indicating a need for:
  - **Targeted interventions**
  - **Stricter enforcement**
  - **Emergency action plans**

**Additional Insight:**  
This visualization can guide policymakers to:

- **Study success stories** and replicate effective strategies.
- **Prioritize cities** with worsening trends for **urgent policy attention**.



---



### 🔮 6. Pollution Trend Forecast for Key Indian Cities (2023 & 2024)
![Forecast Combined](outputs/graphs/forecast_combined.png)

**Interpretation:**  

This combined **pollution trend forecast** uses a **Linear Regression model** to project future pollution levels for **Mumbai, Pune, and Nashik** in **2023 and 2024**.

- **Solid lines** represent actual **historical pollution trends** (2017–2022).
- **Dashed lines** represent the **forecasted pollution levels** for the upcoming years (2023–2024).

**Observations:**

- **Mumbai** shows a slightly declining trend into 2024.
- **Nashik** shows a consistent declining trend.
- **Pune** shows a small increasing trend — an important point to monitor.

**Business Context:**  
These three cities were specifically chosen for forecasting because they represent **Neubrain Solutions' office locations** according to the company website. The insights generated are thus directly relevant to the company's operational environment and can inform potential workplace or CSR initiatives.

**Technical Note:**  
While this analysis involves **forecasting pollution over time**, it is implemented using **simple linear regression on time (year)** — a trend projection method. This is not a full time series model (such as ARIMA or LSTM), but it provides a quick and interpretable estimation of potential future trends based on historical patterns.

**Business Value:**  
Such trend-based forecasting is useful for:

- Anticipating **future air quality risks**.
- Informing **urban planning**.
- Guiding **corporate decisions** related to office locations, employee health, and community engagement.



---



### ⚠️ 7. Top 5 Anomalous Indian Cities (Pollution Volatility)
![Anomalous Indian Cities](outputs/graphs/anomalous_indian_cities.png)

**Interpretation:**  

This bar chart ranks Indian cities by **pollution volatility**, calculated as the **standard deviation of year-on-year percentage change** in pollution levels.

Higher volatility suggests irregular and unstable pollution patterns, which may result from:

- **Fluctuating industrial activity**
- **Meteorological factors** (e.g., wind patterns, rainfall, temperature inversions)
- **Festive or seasonal pollution events**
- **Possible data quality issues or gaps**

**Color Note:**  
The bar colors represent volatility intensity — **red bars indicate higher volatility**, **blue bars indicate lower volatility**.  
This allows for quick visual identification of the most unstable pollution patterns.

### 📊 Current Top 5 Most Volatile Indian Cities:

| City     | Volatility (%) |
|----------|----------------|
| Kanpur   | 45.01%         |
| Gaya     | 33.25%         |
| Agra     | 32.19%         |
| Nagpur   | 28.57%         |
| Bhiwani  | 27.71%         |

**Additional Insight:**  
Cities with high volatility are harder to predict and require **continuous, real-time monitoring** to support **public health advisories** and **policy action**.

For example:

> **Kanpur’s extreme volatility** suggests the influence of both **seasonal pollution spikes** and **industrial activity cycles**.



---



## 💡 Key Insights

- **South Asian cities**, particularly those in **India**, dominate the list of the **world's most polluted urban areas**.
- **Winter months (Nov–Jan)** consistently see a **surge in pollution** due to a mix of climatic conditions and cultural factors (e.g., **festivals**, **stubble burning**).
- The year **2020** witnessed a **sharp global decline in pollution**, strongly linked to **COVID-19 lockdowns** and **reduced economic activity**.
- Cities like **Pune** show **successful pollution control**, with steadily **declining pollution trends**.
- In contrast, **Kanpur** and **Gaya** exhibit **high volatility**, signaling the need for **deeper analysis** and **targeted interventions**.
- The use of **forecasting models** and **volatility analysis** provides **innovative approaches** to proactively manage pollution risks, rather than reacting after pollution events occur.



---



## 🚀 How to Run the Project

```bash
# 1. Clone the repository
git clone <your-repo-url>

# 2. Navigate to the project directory
cd Air-Pollution-Analysis

# 3. Install dependencies
pip install pandas numpy matplotlib seaborn scikit-learn

# 4. Run the main script to generate outputs
python main.py
