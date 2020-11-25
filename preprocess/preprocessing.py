import pandas as pd
import logging

logging.getLogger().setLevel(logging.INFO)
def data_processing():
    file_path  = input('Enter Filepath without quotes:')
    data = pd.read_csv(file_path)

    # print the column names in dataframe
    logging.info('Available column Names are : %s', str(data.columns))

    # enter the column name we need to calculate anomaly data
    column_name = input('Enter Column Name without quotes:')

    # convert datetime string to datetime object and drop other error values
    data['TIMESTAMP'] = pd.to_datetime(data['TIMESTAMP'], errors='ignore')

    # convert all value in the column to numeric values and drop other error values
    data[column_name] = pd.to_numeric(data[column_name], errors='coerce')
    data_new = data.dropna()

    # return dataframe, column name
    return data_new, column_name