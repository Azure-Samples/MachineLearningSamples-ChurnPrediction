# Customer Churn Prediction

import dataprep
from dataprep.Package import Package
import pickle

from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
import pandas as pd
import numpy as np
import csv
from sklearn.metrics import accuracy_score
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import LabelEncoder

from azureml.logging import get_azureml_logger

# initialize the logger
run_logger = get_azureml_logger() 
run_logger.log('amlrealworld.ChurnPrediction.CATelcoCustomerChurnModeling','true')

with Package.open_package('CATelcoCustomerChurnTrainingSample.dprep') as pkg:
    df = pkg.dataflows[0].get_dataframe(spark=False)

columns_to_encode = list(df.select_dtypes(include=['category','object']))
for column_to_encode in columns_to_encode:
    dummies = pd.get_dummies(df[column_to_encode])
    one_hot_col_names = []
    for col_name in list(dummies.columns):
        one_hot_col_names.append(column_to_encode + '_' + col_name)
    dummies.columns = one_hot_col_names
    df = df.drop(column_to_encode, axis=1)
    df = df.join(dummies)

model = GaussianNB()

random_seed = 42
train, test = train_test_split(df, random_state = random_seed, test_size = 0.3)

target = train['churn'].values
train = train.drop('churn', 1)
train = train.values
model.fit(train, target)

expected = test['churn'].values
test = test.drop('churn', 1)
predicted = model.predict(test)
print("Naive Bayes Classification Accuracy", accuracy_score(expected, predicted))
# log the Naive Bayes Accuracy
run_logger.log("Naive Bayes Accuracy", accuracy_score(expected, predicted))

dt = DecisionTreeClassifier(min_samples_split=20, random_state=99)
dt.fit(train, target)
predicted = dt.predict(test)
print("Decision Tree Classification Accuracy", accuracy_score(expected, predicted))
# log the DTree Accuracy
run_logger.log("DTree Accuracy", accuracy_score(expected, predicted))

# serialize the model on disk in the special 'outputs' folder

print ("Export the model to model.pkl")
f = open('./outputs/model.pkl', 'wb')
pickle.dump(dt, f)
f.close()

