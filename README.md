# Time Series Forecasting with NeuralProphet

![111388960-6c367e80-866d-11eb-91c1-46f2c0d21879](https://github.com/Andrea280197/Neuralprophet-time-series-forecasting/assets/119070619/a08454ca-760d-4a4f-825a-ac2c71a869f1)


## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [File Descriptions](#file-descriptions)
- [License](#license)

## Introduction

Time series forecasting involves predicting future values based on historical data points. The NeuralProphet library provides a neural network-based approach for time series forecasting, which can capture complex patterns and relationships in the data.

This project demonstrates the following steps:

- Data Preparation: Data is loaded from an Excel file containing inclinometric and pluviometric measurements.

- Preprocessing: The data is preprocessed, including handling missing values, converting data types, and filtering based on date ranges.

- Model Training: A NeuralProphet model is trained using the prepared data, with additional features such as lagged regressors for improved forecasting accuracy.

- Evaluation and Visualization: The trained model is used to make predictions, and the results are visualized using plots to assess the model's performance.

## Installation

To run the project locally, follow these steps:

Clone the repository to your local machine:

`git clone https://github.com/your-username/your-repository.git`

Navigate to the project directory:

`cd your-repository`

Install the required dependencies using pip:

`pip install -r requirements.txt`

## Usage

To use the project, follow these steps:

- Ensure that you have installed the required dependencies as mentioned in the Installation section.

- Place your Excel data file containing inclinometric and pluviometric measurements in the project directory.

- Update the data.py script to point to your data file and adjust any parameters as necessary.

- Run the data.py script to perform data processing, model training, and forecasting:

 `python data.py`

After running the script, you should see visualizations and output related to the forecasted values and model performance.

![Figure_1](https://github.com/Andrea280197/Neuralprophet-time-series-forecasting/assets/119070619/18467c7a-a4a9-4047-ad2d-aa432b27ba67)


## File Descriptions

- data.py: Main Python script for data processing, model training, and forecasting.

- requirements.txt: Text file containing a list of Python dependencies required for the project.

- Dati inclinometrici e pluviometrici_ReCity.xlsx: Sample Excel file containing inclinometric and pluviometric data.


## License

This project is licensed under the MIT License.
