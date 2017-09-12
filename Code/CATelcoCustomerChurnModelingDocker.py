from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
import pandas as pd
import numpy as np
import csv
from sklearn.metrics import accuracy_score
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import LabelEncoder


df = pd.read_csv('CATelcoCustomerChurnTrainingSample.csv')
df = df.drop('year', 1)
df = df.drop('month', 1)
df = df.drop_duplicates()


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

train, test = train_test_split(df, test_size = 0.3)

target = train['churn'].values
train = train.drop('churn', 1)
train = train.values
model.fit(train, target)


expected = test['churn'].values
test = test.drop('churn', 1)
predicted = model.predict(test)
print("Naive Bayes Classification Accuracy", accuracy_score(expected, predicted))

dt = DecisionTreeClassifier(min_samples_split=20, random_state=99)
dt.fit(train, target)
predicted = dt.predict(test)
print("Decision Tree Classification Accuracy", accuracy_score(expected, predicted))