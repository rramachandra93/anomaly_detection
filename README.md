<p align="center">
  <h1>Anomaly Detection</h1>
</p>


## Requirement

1) Create a generic anomaly detection module, given a feature in csv as input it must extract
   all the anomalies with the time stamp associated with it.
2) Input : column_name
   Output : anomaly value , timestamp(DD/MM/YYYY)
3) Output must be in excel.

## Implementation :

The above request satisfied using an unsupervised clustering algorithm called
OPTICS(Ordering Points To Identify the Clustering Structure).
This algorithm is closely related to DBSCAN, finds core sample of high density and expands clusters from them.
Unlike DBSCAN, keeps cluster hierarchy for a variable neighborhood radius.
The anomaly values fall under label -1. We fiter out that values to find anomalies.

## why OPTICS:
While creating a model for anomaly detection the first algorithm came into mind was DBSCAN.
This is a good algorithm for clustering while we don't know what is the optimal number of clusters(K-means lost here).
But the problem with DBSCAN was, while training a particular dataset we can tune the hyper parameter eps with respect to our data
but while considering a GENERIC model finding optimal eps for each dataset using KNN and plotting elbow method and find eps from
graph is tedious. so OPTICS is a good choice. also using OPTICS the model get good silhouette scores too.

## about sample data:
While looking into the sample data we may think there are lot of outliers. but when closely watch the dat we can see this is not
the case.The range of values is too large but some are also similar in some ways.

The algorithm run on 4 different datasets and obtained descent silhouette scores from 0.64 to 0.92.
Sinve we want to make it a generalized model, tuned it according to give a general decent performance.

## Prerequisites:
- DataFrame must contain a TIMESTAMP column
- The column input must be continuous (Normally we cant say outliers in categorical data. even if one present
   may be it is another category
   
## Working
- install the requirements file
- Run main.py

## Input:
- input file path of DataFrame
- input column name we want to find anomaly

## Output:
The output will be saved on an excel sheet named anomaly_values.xlsx
Output contains timestap of anomaly values and curresponding anomaly values itself.

Output excel sheet:
![picture](https://github.com/rramachandra93/anomaly_detection/blob/main/Screenshots/excel_sheet.png)

console output:
![picture](https://github.com/rramachandra93/anomaly_detection/blob/main/Screenshots/output.png)
