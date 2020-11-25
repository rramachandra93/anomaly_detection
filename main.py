from preprocess import preprocessing
from model import model
from result import output

dataframe, columnname = preprocessing.data_processing()
clusters = model.clusteringmodel(dataframe, columnname)
output.outcalc(dataframe, clusters, columnname)