# Churn Prediction using AMLWorkbench - Modeling and Evaluation
## 1. Objectives

The aim of this lab is to use the .dprep file created from the previous lab to develop a churn classifier. More specifically, in this lab, we will use sklearn library’s Naïve Bayesian and Decision Tree algorithm to develop a churn classifier, evaluate, and compare.

## 2. Data Access Code

2.1.    The previous lab showed how to create a .dprep file. Use the .dprep file to generate data access code file by going to File Explorer, selecting the .dprep file and then choosing Generate Data Access Code File via right-click drop-down menu.

![GenerateDataAccessCode](Images/GenerateDataAccessCode.png)

2.2.    A new python file called CATelcoCustomerChurnTrainingSample.py is created. Rename the file to CATelcoCustomerChurnModeling.py and copy the content of CATelcoCustomerChurnModeling.py from the github repo into this file. We will be using this file to perform modeling using the transformed data.

```
with Package.open_package('CATelcoCustomerChurnTrainingSample.dprep') as pkg:
    df = pkg.dataflows[0].get_dataframe()
```
In the preceding code, the dataframe df can then be used in the code for advanced analytics.

## 3. One-hot encoding

The dataset imported from French Telecom company Orange consists of heterogeneous noisy data (numerical/categorical variables). One hot encoding transforms categorical features to a format that works better with classification and regression algorithms. Some algorithms, like random forests, handle categorical values natively. Then, one hot encoding is not necessary. The process of one hot encoding may seem tedious, but fortunately, most modern machine learning libraries (such as pandas) can take care of it.

The following code is used to perform one-hot encoding:

```
columns_to_encode = list(df.select_dtypes(include=['category','object']))
for column_to_encode in columns_to_encode:
    dummies = pd.get_dummies(df[column_to_encode])
    one_hot_col_names = []
    for col_name in list(dummies.columns):
        one_hot_col_names.append(column_to_encode + '_' + col_name)
    dummies.columns = one_hot_col_names
    df = df.drop(column_to_encode, axis=1)
    df = df.join(dummies)
```
Code highlights

* list(df.select_dtypes(include=['category','object'])) identifies all categorical fields.
* get_dummies converts categorical variable into dummy/indicator variables.
* There can be more than one categorical variable containing the same values. Hence, column_to_encode + '_' + col_name is used to produce a unique column name.

## 4. Modeling and Evaluation

Naïve Bayes

In this lab, we will begin with Sklearn’s GaussianNB to build our model. GaussianNB implements the Gaussian Naive Bayes algorithm for classification. The likelihood of the features is assumed to be Gaussian:

![Algorithm](Images/Formula.png)

The parameters are estimated using maximum likelihood.

Sklearn’s function train_test_split can be used to split the dataset for performing training and testing using a 70/30 proportion. In the following code, the target churn variable is specified for building the model.

```
model = GaussianNB()
train, test = train_test_split(df, test_size = 0.3)

target = train['churn'].values
train = train.drop('churn', 1)
train = train.values
model.fit(train, target)
```

For evaluation, you can generate the expected and predicted values by running the following code:

```
expected = test['churn'].values
test = test.drop('churn', 1)
predicted = model.predict(test)
```

The metrics module from sklearn implements functions assessing prediction error for specific purposes such as classification, clustering, regression, etc. The classification_report function from the metrics module produces a report of commonly used measures such as precision, recall, f-measure for the test data. In addition, accuracy_score is a straightforward function that you can leverage to get the accuracy of the classifier. accuracy_score takes in expected and predicted values as shown below:

```
accuracy_score(expected, predicted)
```
Decision Tree
Decision Trees are a non-parametric supervised learning method used for classification and regression. The goal is to create a model that predicts the value of a target variable by learning simple decision rules inferred from the churn data features.

The train and test datasets created from the above section can be used to build a Decision Tree Classifier. The Decision Tree is initialized with two parameters: min_samples_split=20 requires 20 samples in a node for it to be split and random_state=99 to seed the random number generator. The below code can be used to build the tree and get the accuracy to compare with the Naïve Bayes classifier.

```
dt = DecisionTreeClassifier(min_samples_split=20, random_state=99)
dt.fit(train, target)
predicted = dt.predict(test)
print("Decision Tree Classification Accuracy", accuracy_score(expected, predicted))
```
## 5. Execution – Local Computer

Launch the Command Line Interface (CLI) window by clicking on File --> Open Command-Line Interface. When you launch the CLI window from AMLWorkbench, you will automatically be placed in the project folder. The CLI needs to authenticate and set the current subscription to the one your AMLWorkbench Team Account is in. Run the following az commands from the CLI window launched from AMLWorkbench.

```
az login
az account list –o table
az account set –s <subscription_id_where_your_AMLWorkbench_team_account_is_in>
```
The following command executes the CATelcoCustomerChurnModeling.py file locally. After the execution finishes, you should see the output in the CLI window. The classification report is printed out using the metrics module for both Naïve Bayes and Decision Tree classifiers.

```
az ml experiment submit -c local CATelcoCustomerChurnModeling.py
```

![CLIwindow](Images/CLIWindow.png)

## 6. Jobs

On successful run, you will also find entries in Jobs tab. On selecting the job, notice the evaluation metrics obtained.

![Evaluation_Metrics](Images/EvaluationMetrics.png)

## 7. Pickled Model

In the CATelcoCustomerChurnModeling.py script, we serialize the decision tree model using the popular object serialization package -- pickle, into a file named model.pkl on disk. The code snippet is as follows:

```
print ("Export the model to model.pkl")
f = open('./outputs/model.pkl', 'wb')
pickle.dump(dt, f)
f.close()
```
When you executed the CATelcoCustomerChurnModeling.py script using the az ml execute command, the model was written to the outputs folder with the name model.pkl. This folder is only accessible from the AMLWorkbench app. You can find it in the run history detail page and download this binary file by clicking on the download button next to the file name.

![OutputSfolder](Images/OutputsFolder.png)

Download the model file model.pkl and save it to the root of your project folder. You need it in the later steps.

[Go to next hands-on lab]()
