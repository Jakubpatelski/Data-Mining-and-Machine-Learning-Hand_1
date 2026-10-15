# Assignment 1: Student Motivation Analysis

The analysis uses 223 survey responses provided by the professor, plus historical Copenhagen rainfall data from Open-Meteo.

## 1. Weather and motivation

File: assignment/weather_and_motivation.ipynb

Questions:

- Do students select “It is the most exciting” more often on rainy days?
- Can daily rainfall predict whether a student selects that answer?

The notebook:

- Loads and combines the survey files using load_student_data.py.
- Uses historical Copenhagen rainfall data from **ECMWF’s ERA5 dataset**, accessed through the [Open-Meteo Historical Weather API](https://open-meteo.com/en/docs/historical-weather-api). If the saved CSV is missing, the code sends Copenhagen’s coordinates, the date range **26 August 2020–21 September 2026**, and a request for daily rainfall in millimetres. It converts the API response into a pandas table and saves it as `dataset/copenhagen_weather_daily.csv`. Future runs reuse this CSV instead of downloading it again.
- Converts survey timestamps to Copenhagen time and matches rainfall by date.
- Defines rainy days as days with at least 1 mm of rainfall.
- Compares the percentage selecting “most exciting” using a table and bar chart.
- Checks the comparison within each year.
- Uses `GroupShuffleSplit` to keep responses from the same date together, holding out 20% of dates for testing.
- Uses `StandardScaler` and scikit-learn logistic regression to predict the yes/no answer from rainfall alone.
- Compares test accuracy with a `DummyClassifier` that always predicts the most common training answer.

Result: 52.8% selected “most exciting” on rainy days, compared with 48.0% on days below 1 mm—a difference of 4.8 percentage points.

This does not prove rainfall caused the difference. Cohorts differ, and several students answered on the same day. The 223 responses cover only 45 distinct dates.

**Prediction result:** trained on 194 students from 36 dates and tested on 29 students from nine different dates. Logistic regression got **11/29 correct (37.9%)**, compared with **12/29 (41.4%)** for the baseline. Rainfall alone did not improve prediction on this split. This is a difference of just one student, not evidence that no relationship could exist. Full-day rainfall can include rain after the response, so this is a retrospective analysis rather than a real-time forecast.

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
- Uses scikit-learn’s `StandardScaler` to standardize KNN inputs using training-set statistics only; the decision tree uses the original 0/1 inputs.
- Compares two supervised classifiers:
  - Decision tree: uses scikit-learn, following Lecture #07, to learn yes/no splits on motivation choices, with a maximum depth of three.
  - KNN: uses scikit-learn; predicts the most common year among the five closest training students.
- Compares both models with a baseline that always predicts the most common training year.

Results on the same 45 test students:

| Method | Correct predictions | Accuracy |
|---|---:|---:|
| Most common year baseline | 10/45 | 22.2% |
| Decision tree, maximum depth three | 8/45 | 17.8% |
| KNN, five neighbours | 10/45 | 22.2% |

KNN matched the baseline, while the decision tree performed worse on this split. Neither model predicted the year accurately. This small, exploratory comparison does not establish a reliable advantage; the same test set has been inspected during earlier experiments.

The observed excitement percentage ranged from 36.4% in 2023 to 71.4% in 2021. However, 2021 contains only seven students, and these are different cohorts—not the same students followed over time.
