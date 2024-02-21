from neuralprophet import NeuralProphet
import pandas as pd
import openpyxl
import matplotlib.pyplot as plt

def exctract_yhat(forecasts, size):
    columns = forecasts.columns[3:]
    newframe = forecasts[['ds', 'yhat1']].iloc[-size:].copy()
    for col in columns:
        if 'yhat' in col:
            newframe['yhat1'] = newframe['yhat1'].fillna(forecasts[col])
    return newframe

# Read Excel file using openpyxl
dataframe = openpyxl.load_workbook("Dati inclinometrici e pluviometrici_ReCity.xlsx")
dataframe1 = dataframe.active

# Create a list to store rows
rows_list = []

# Iterate through rows and columns to extract data
for row in dataframe1.iter_rows(min_row=2, values_only=True):  
    row_dict = {'ds': row[0], 'y': row[1], 'Pioggia giornaliera [mm]': row[2]}  
    rows_list.append(row_dict)

# Create a Pandas DataFrame
df = pd.DataFrame(rows_list)

# Convert 'ds' to datetime format
df['ds'] = pd.to_datetime(df['ds'], errors='coerce')

# Convert 'y' to numeric format
df['y'] = pd.to_numeric(df['y'], errors='coerce')

# Convert 'Pioggia giornaliera [mm]' to numeric format
df['Pioggia giornaliera [mm]'] = pd.to_numeric(df['Pioggia giornaliera [mm]'], errors='coerce')

# Fill NaN values in the 'y' column with 0
df['y'] = df['y'].fillna(method='ffill')

# Fill NaN values in the 'ds' column with a specific timestamp
df['ds'] = df['ds'].fillna(value=df['ds'].min() - pd.Timedelta(days=1))
print(df.columns)

# Filter data between January 2, 2016, and September 16, 2017
start_date = '2016-01-02'
end_date = '2017-09-16'
df_filtered = df[(df['ds'] >= start_date) & (df['ds'] <= end_date)]

df['y'] = df['y'].fillna(method='ffill')
df['y'] = df['y'].fillna(method='bfill')
df['Pioggia giornaliera [mm]'] = df['Pioggia giornaliera [mm]'].fillna(method='ffill')
df['Pioggia giornaliera [mm]'] = df['Pioggia giornaliera [mm]'].fillna(method='bfill')

#train_proportion = 0.8 
#sz = round(len(df) * train_proportion)
sz = round(len(df)/100*10)
dftrain = df[:- sz].copy()
dftest = df[-sz:].copy()

# Train NeuralProphet model with filtered data and yearly seasonality
model = NeuralProphet(yearly_seasonality=True)
model.add_lagged_regressor('Pioggia giornaliera [mm]')
#model.fit(df_filtered, freq="D")  
model.fit(dftrain, freq="D") 

regressors = dftest.copy()
regressors['y'] = pd.Series([float('nan')]*len(dftest))  
regressors['Pioggia giornaliera [mm]'] = dftest['Pioggia giornaliera [mm]']
   
future = model.make_future_dataframe(dftrain, periods=30, regressors_df=regressors, n_historic_predictions=True)
forecast = model.predict(future)

fig_forecast = model.plot(forecast) 
plt.show()
# Print the available columns in the forecast DataFrame
print(forecast.columns)

# Print the forecasted values
print(forecast[['ds', 'yhat1', 'trend', 'season_yearly', 'season_weekly']])

# Plot the actual values
plt.plot(df_filtered['ds'], df_filtered['y'], label='Actual', color='blue' , marker='.')

# Plot the forecasted values
plt.plot(forecast['ds'], forecast['yhat1'], label='Forecast', color='red')

# Plot the trend, yearly seasonality, and weekly seasonality
plt.plot(forecast['ds'], forecast['trend'], label='Trend', linestyle='--', color='green')

# Check if 'season_yearly' is present in the DataFrame
if 'season_yearly' in forecast.columns:
    plt.plot(forecast['ds'], forecast['season_yearly'], label='Yearly Seasonality', linestyle='--', color='orange')

# Plot the weekly seasonality if present
if 'season_weekly' in forecast.columns:
    plt.plot(forecast['ds'], forecast['season_weekly'], label='Weekly Seasonality', linestyle='--', color='purple')

# Add labels and title
plt.xlabel('Date')
plt.ylabel('Value')
plt.title('Actual vs Forecasted Values with Trend and Seasonality')

# Show the legend
plt.legend()

# Display the plot
plt.show()