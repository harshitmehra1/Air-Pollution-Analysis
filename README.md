# 🌍 Air Pollution Analysis Project

This repository contains an exploratory data analysis (EDA) project on global air pollution trends.  
It was created as part of an internship assignment for **Neubrain Solutions**, an AI & Strategy consulting firm based in Mumbai.

- **Skills demonstrated:** Data Cleaning, Exploratory Analysis, Insight Communication, Data Visualization  
- **Tools used:** Python (Pandas, Seaborn, Matplotlib)


---

## 📌 Project Overview

Air pollution is one of the most urgent environmental challenges globally.  
This project analyzes pollution levels across hundreds of cities over several years to uncover key patterns and generate insight-driven visuals for strategic decisions.

---

## 🛠️ Process

### 1️⃣ Data Cleaning

- Replaced placeholder values (`-`) with `NaN`
- Converted all pollution columns to numeric format
- Split the original `City` column into two separate columns: `CityName` and `Country`
- Rearranged year columns (`2017` to `2022`) into chronological order
- Saved the cleaned dataset as `data/cleaned_air_pollution.csv` for reuse in visualizations and Power BI

---

## 📊 Visual Analysis (Python + Seaborn/Matplotlib)

### 📈 1. Mumbai vs Pune vs Nashik – Pollution Over Years
![City Trend](outputs/graphs/neubrain_cities_trend.png)

**Interpretation:**  
This multi-line chart shows how air pollution levels changed in three key Maharashtra cities between 2017 and 2022. While all cities saw a dip in 2020, Pune maintained a relatively lower pollution level compared to Mumbai and Nashik.

---

### 🌆 2. Top 10 Most Polluted Cities (2022)
![Top Polluted](outputs/graphs/top10_polluted_2022.png)

**Interpretation:**  
This enhanced bar chart uses a color gradient to show the intensity of pollution. Most of the top 10 cities are in India, showcasing the regional concentration of air quality issues.

---

### 🍃 3. Top 10 Least Polluted Cities (2022)
![Least Polluted](outputs/graphs/top10_least_polluted_2022.png)

**Interpretation:**  
These cities recorded the lowest pollution in 2022. The lightest bars represent the cleanest air, reflecting lower industrial density and better environmental regulations.

---

### 📅 4. Monthly Average Pollution Trend
![Monthly Average](outputs/graphs/monthly_avg_pollution.png)

**Interpretation:**  
Pollution peaks in **winter months** (Nov–Jan) and dips during the **monsoon and summer** (June–August), reflecting seasonal human and industrial activities.

---

### 🔄 5. Pollution Improvement vs Decline (2017–2022)
![Change Chart](outputs/graphs/improvement_vs_decline.png)

**Interpretation:**  
This pastel-colored chart shows the top 10 cities with the most improvement (green) and worst decline (red) in pollution levels over five years. While cities like Pune improved, others like Jaipur worsened significantly.

---

## 💡 Key Insights

- **South Asian cities**, especially in **India**, dominate the list of most polluted locations.
- **Winter seasons** consistently see a surge in pollution due to climatic and cultural factors (e.g., festivals, stubble burning).
- **2020** witnessed a sharp decline in pollution globally, likely due to **COVID-19 lockdowns**.
- Cities like **Pune** show potential as success stories with declining pollution trends.
- Data storytelling with color gradients and comparative visuals helps uncover geographic and temporal pollution patterns.

---

## 🚀 How to Run the Project

```bash
# 1. Clone the repository
git clone <your-repo-url>

# 2. Navigate to the project directory
cd Air-Pollution-Analysis

# 3. Install dependencies
pip install pandas numpy matplotlib seaborn

# 4. Run the main script to generate outputs
python main.py