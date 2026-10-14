# Assignment 1: Student Motivation Analysis

The analysis uses 223 survey responses provided by the professor, plus historical Copenhagen rainfall data from Open-Meteo.

## 1. Weather and motivation

File: assignment/weather_and_motivation.ipynb

Question: Do students select “It is the most exciting” more often on rainy days?

The notebook:

- Loads and combines the survey files using load_student_data.py.
- Uses historical Copenhagen rainfall data from **ECMWF’s ERA5 dataset**, accessed through the [Open-Meteo Historical Weather API](https://open-meteo.com/en/docs/historical-weather-api). If the saved CSV is missing, the code sends Copenhagen’s coordinates, the date range **26 August 2020–21 September 2026**, and a request for daily rainfall in millimetres. It converts the API response into a pandas table and saves it as `dataset/copenhagen_weather_daily.csv`. Future runs reuse this CSV instead of downloading it again.
- Converts survey timestamps to Copenhagen time and matches rainfall by date.
- Defines rainy days as days with at least 1 mm of rainfall.
- Compares the percentage selecting “most exciting” using a table and bar chart.
- Checks the comparison within each year.

Result: 52.8% selected “most exciting” on rainy days, compared with 48.0% on days below 1 mm—a difference of 4.8 percentage points.

This does not prove rainfall caused the difference. Cohorts differ, and several students answered on the same day. The 223 responses cover only 45 distinct dates.

This notebook contains descriptive analysis, not a machine-learning model.

## 2. Motivation and year

File: assignment/motivation_year.ipynb

Questions:

- How does the percentage selecting “most exciting” differ across years?
- Can students’ motivation choices predict their survey year?

The notebook:

- Loads the survey and extracts the year from each timestamp.
- Plots excitement percentages across years.
- Converts five motivation categories into 0/1 columns, allowing multiple selections.
- Combines “business skills” and “commercially useful skills” into one category.
- Splits students into 80% training and 20% testing, preserving representation of each year.
- Standardizes inputs using training-set statistics only.
- Implements two supervised classifiers directly with NumPy:
  - Nearest-centroid: predicts the year with the closest average motivation profile.
  - KNN: predicts the most common year among the five closest training students.
- Compares both models with a baseline that always predicts the most common training year.

Results on the same 45 test students:

| Method | Correct predictions | Accuracy |
|---|---:|---:|
| Most common year baseline | 10/45 | 22.2% |
| Nearest-centroid | 12/45 | 26.7% |
| KNN, five neighbours | 10/45 | 22.2% |

Nearest-centroid performed slightly better, but neither model predicted the year accurately. This small, exploratory comparison does not establish a reliable advantage.

The observed excitement percentage ranged from 36.4% in 2023 to 71.4% in 2021. However, 2021 contains only seven students, and these are different cohorts—not the same students followed over time.
