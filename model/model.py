import warnings
from sklearn.cluster import OPTICS

# model inputs dataframe and input column name.output is cluster labels for each point

warnings.filterwarnings('ignore')
def clusteringmodel(data_frame, column_name):
    model = OPTICS(min_samples=6)
    column_array = data_frame[column_name].values.reshape(-1, 1)
    model.fit(column_array)
    return model.labels_