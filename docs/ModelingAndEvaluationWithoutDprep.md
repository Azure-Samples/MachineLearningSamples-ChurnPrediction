# Churn Prediction using AMLWorkbench - Modeling and Evaluation without .dprep

## 1. Objectives

The aim of this lab is to generate churn classifiers without using .dprep. We will reproduce the steps related to data preparation using pandas for flexibility.

## 2. Data Preparation

The csv file can be read using pandas into a dataframe df. The data preparation tasks such as filling in missing values, dropping columns, and removing duplicates can be performed using `fillna()`, `drop()` and `drop_duplicates()` functions from pandas:

```
df = pd.read_csv('data/CATelcoCustomerChurnTrainingSample.csv')
df = df.fillna(0)
df = df.drop_duplicates()
df = df.drop('year', 1)
df = df.drop('month', 1)
```

The rest of the code related to one-hot encoding, splitting the data, and modeling is pretty much the same as in the previous lab. Ensure that the `CATelcoCustomerChurnTrainingSample.csv` is in the data folder.

## 3. Execution – Local/Docker Container

To run locally, run the below command:

```
az ml experiment submit -c local CATelcoCustomerChurnModelingWithoutDprep.py
```

If you have a Docker engine running locally, in the CLI window, run the below command:

```
az ml experiment submit -c docker CATelcoCustomerChurnModelingWithoutDprep.py
```

[Go to next hands-on lab](https://github.com/Azure/MachineLearningSamples-ChurnPrediction/blob/master/docs/Operationalization.md)
