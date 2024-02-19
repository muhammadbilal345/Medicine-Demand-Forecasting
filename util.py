import numpy as np
import pandas as pd
from pmdarima.arima import auto_arima

fd = pd.read_csv('final_data.csv')
fd.set_index('area_name', inplace=True)
fd = fd.T.squeeze()
fd.index = pd.to_datetime(fd.index, format='%Y')

def get_reviews_and_ratings(drug_name, dataframe):
    drug_data = dataframe[dataframe['drugName'] == drug_name]
    reviews = drug_data['review'].tolist()
    ratings = drug_data['rating'].tolist()
    return reviews, ratings

def predict_sales(drug_name, n_years):
    model = auto_arima(fd[drug_name], seasonal=False, suppress_warnings=True, stepwise=True, error_action='ignore')

    model_fit = model.fit(fd[drug_name])

    forecast, conf_int = model_fit.predict(n_periods=n_years, return_conf_int=True)

    forecast = np.where(forecast < 0, 0, forecast)

    idx = pd.date_range(start=fd.index[-1]+pd.offsets.DateOffset(years=1), periods=n_years, freq='AS')

    pred_fd = pd.DataFrame({f'Predicted sales (packs)': forecast}, index=idx)

    fd_pred = fd[[drug_name]].append(pred_fd)

    fd_pred.sort_index(inplace=True)
    
    fd_pred.rename(columns={drug_name: 'Previous sales (packs)'}, inplace=True)
    
    fd_pred['Year'] = fd_pred.index.year

    fd_pred['Combined Sales (packs)'] = (np.where(fd_pred['Predicted sales (packs)'].isnull(), fd_pred['Previous sales (packs)'], fd_pred['Predicted sales (packs)'])).round().astype('int64')

    return fd_pred[['Year', 'Combined Sales (packs)']]