# Customer Churn Prediction using AMLWorkbench

![Data_Diagram](https://www.usb-antivirus.com/wp-content/uploads/2014/11/tutorial-windwos-10-2-320x202.png)
## Prerequisites

1. Ensure that you have properly installed Azure ML Workbench by following the [installation guide](https://github.com/Azure/ViennaDocs/blob/master/Documentation/Installation.md).

2. For operationalization, it is best if you have Docker engine installed and running locally. If not, you can use the cluster option but be aware that running an (ACS) Azure Container Service can be expensive.

3. This tutorial assumes that you are running Azure ML Workbench on Windows 10 with Docker engine locally installed. If you are using macOS the instruction is largely the same.

## Tutorial Introduction
On average, keeping existing customers is five times cheaper than the cost of recruiting new ones. As a result, marketing executives often find themselves trying to estimate the likelihood of customer churn and finding the necessary actions to minimize the churn rate.

The aim of this solution is to demonstrate predictive churn analytics using AMLWorkbench. This solution provides an easy to use template to develop churn predictive data pipelines for retailers. The template can be used with different datasets and different definitions of churn. The aim of the hands-on labs is to:

1. Understand AMLWorkbench's Data Preparation tools to clean and ingest customer relationship data for churn analytics.

2. Perform feature transformation to handle noisy heterogeneous data.

3. Integrate third-party libraries (such as scikit-learn and azureml) to develop Bayesian and Tree-based classifiers for predicting churn.

4. Perform operationalization.

The solution is located at https://github.com/Azure/MachineLearningSamples-ChurnPrediction

## Use Case Overview
Companies need an effective strategy for managing customer churn. Customer churn includes customers stopping the use of a service, switching to a competitor service, switching to a lower-tier experience in the service or reducing engagement with the service.

In this use case, we look at data from French telecom company Orange to identify customers who are likely to churn in the near term in order to improve the service and create custom outreach campaigns that help retain customers.

Telecom companies face a competitive market. Many carriers lose revenue from postpaid customers due to churn. Hence the ability to accurately identify customer churn can be a huge competitive advantage.

Some of the factors contributing to telecom customer churn includes:

* Perceived frequent service disruptions
* Poor customer service experiences in online/retail stores
* Offers from other competing carriers (better family plan, data plan, etc.).

In this tutorial, we will use a concrete example of building a predictive customer churn model for telecom companies.

## Data Description

The dataset used to ingest is from SIDKDD 2009 competition. It is called CATelcoCustomerChurnTrainingSample.csv and is located in the Data folder. The dataset consists of heterogeneous noisy data (numerical/categorical variables) from French Telecom company Orange and is anonymized.

The variables capture customer demographic information, call statistics (such as avg call duration, call failure rate, etc., contract information, complaint statistics. Churn variable is binary (0 - did not churn and 1 - did churn).

## Tutorial Structure

The folder structure of the tutorial is arranged as follows:
Code: Contains all the code related to churn prediction using AMLWorkbench  

Data: Contains the dataset used in the tutorial  
Labs: Contains all the hands-on labs

The order of Hands-on Labs to carry out the tutorial is as follows:
1. Data Preparation
The files related to Data Preparation in the code folder are CATelcoCustomerChurnTrainingSample.dprep, CATelcoCustomerChurnTrainingSample.dconn and CATelcoCustomerChurnTrainingSample.csv
2. Modeling and Evaluation
The main file related to modeling and evaluation in the code folder is CATelcoCustomerChurnModeling.py
3. Modeling and Evaluation in Docker
The main file for this task in the code folder is CATelcoCustomerChurnModelingDocker.py
4. Operationalization
The main files for performing operationalization are the model (model.pkl) and churn_schema_gen.py

## Conclusion
This tutorial gives an overview of how to perform churn prediction using AMLWorkbench's Data Preparation tools, perform feature engineering to handle noisy heterogeneous data and operationalize.

## Contact
Please feel free to contact Mithun Prasad (miprasad@microsoft.com) with any question or comment.

## Disclaimer
Leave this session as what it is for now. We will update the content once we get more concrete answers from the legal team.