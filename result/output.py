import logging
import openpyxl
from sklearn.metrics import silhouette_score

# function to write the anomaly values into excel file.Input is dataframe, model output labels, column name we required
def outcalc(datafinal, model_out, column_name):
   
    # output dataframe contain column we required and timestamp with the rows where
    # anomaly data present
    out_df = datafinal.iloc[model_out == -1][['TIMESTAMP', column_name]]
    out_df.to_excel('anomaly_values.xlsx')
    columnarray = datafinal[column_name].values.reshape(-1, 1)
    logging.info('silhoutte_score: %s',str(silhouette_score(columnarray, model_out)))
    logging.info(f'output Head : {out_df.head().to_string}')
