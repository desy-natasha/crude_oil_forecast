# Brent Crude Oil Price Forecast Model

## Overview
This is a forecasting model that compares the performance of two approaches: univariate and multivariate analysis to predict the brent crude oil price. The process includes data preparation, ensuring stationarity, identifying relevant predictors, and model evaluation.

## Installation
- Python 3.8
- pandas
- numpy
- seaborn
- statsmodels
- pmdarima

Clone this repository and install required packages:
```bash
pip install -r requirements.txt
```

## Usage

### 1. Dataset Preparation
Ensure the dataset can be found in `[ROOT_DIR]/crude_oil_forecast/data`, which retrieved from [www.eia.gov](www.eia.gov).

### 2. Run the Scripts

- **Data Preprocessing**:
  ```bash
  python src/data_processing.py
  ```
- **Model Training and Evaluation**:
  ```bash
  python src/model.py
  ```
- **Data Visualization**:
  ```bash
  python src/visualization.py
  ```

### 3. Model Training
Forecast model training will be performed in the `[ROOT_DIR]/crude_oil_forecast/notebook`:
```bash
jupyter notebook notebook/forecasting_crude_oil.ipynb
```
