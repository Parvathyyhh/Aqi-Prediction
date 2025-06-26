AQI Prediction for Kollam, Karyavattom, and Eloor

Project Overview

AQI Prediction is an interactive web-based application developed using Streamlit and a pre-trained machine learning model. The application is designed to estimate the Air Quality Index (AQI) for three key cities in Kerala — Kollam,Karyavattom and Eloor based on user-input pollutant data.

The model has been trained on historical air quality data from 2023 and 2024 ensuring location-specific and data-driven AQI predictions that reflect real-world environmental trends in these regions.

Key Features

* Clean and user-friendly web interface powered by Streamlit
* Input support for major air pollutants:

  * PM10
  * PM2.5
  * CO
  * NO₂
  * SO₂
  * NH₃
  * O₃
* Dropdown menu to select from the three cities: Kollam, Karyavattom, and Eloor
* Predictive output generated upon a single button click
* Immediate display of the predicted AQI value
* Model trained on actual historical pollution data from 2023–2024

How It Works

1. The user enters values for the relevant pollutant parameters.
2. On clicking the "Predict" button, a dropdown menu appears for city selection.
3. The selected city and pollutant data are passed to the pre-trained machine learning model (`aqi.pkl`).
4. The model processes the inputs and returns an AQI prediction.
5. The predicted AQI is displayed on the screen.

Technologies and Tools

| Component        | Description                                       |
| ---------------- | ------------------------------------------------- |
| Frontend         | Streamlit (Python-based web framework)            |
| Backend          | Python, with Pickle for model serialization       |
| Machine Learning | Regression model trained on historical AQI data   |
| Data Source      | Pollution records (2023–2024) for selected cities |
| Pollutants Used  | PM10, PM2.5, CO, NO₂, SO₂, NH₃, O₃                |
