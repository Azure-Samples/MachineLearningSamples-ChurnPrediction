# Customer Churn Prediction using Azure Machine Learning

## Link of the Gallery GitHub Repository
Following is the link to the public GitHub repository where all the codes are hosted:

[https://github.com/Azure/MachineLearningSamples-ChurnPrediction](https://github.com/Azure/MachineLearningSamples-ChurnPrediction)

## Prerequisites

* Ensure that you have properly installed Azure Machine Learning Workbench by following the [installation guide](./quick-start-installation.md).

* For operationalization, it is best if you have Docker engine installed and running locally. If not, you can use the cluster option but be aware that running an Azure Container Service (ACS) can be expensive.

* This scenario assumes that you are running Azure Machine Learning (AML) Workbench on Windows 10 with Docker engine locally installed. If you are using macOS the instruction is largely the same.

## Introduction
On average, keeping existing customers is five times cheaper than the cost of recruiting new ones. As a result, marketing executives often find themselves trying to estimate the likelihood of customer churn and find the necessary actions to minimize the churn rate.

The aim of this solution is to demonstrate predictive churn analytics using AML Workbench. This solution provides an easy to use template to develop churn predictive data pipelines for retailers. The template can be used with different datasets and different definitions of churn. The aim of the hands-on example is to:

1. Understand AML Workbench's Data Preparation tools to clean and ingest customer relationship data for churn analytics.

2. Perform feature transformation to handle noisy heterogeneous data.

3. Integrate third-party libraries (such as scikit-learn and azureml) to develop Bayesian and Tree-based classifiers for predicting churn.

4. Perform operationalization.

## Use Case Overview
Companies need an effective strategy for managing customer churn. Customer churn includes customers stopping the use of a service, switching to a competitor service, switching to a lower-tier experience in the service or reducing engagement with the service.

In this use case, we look at data from French telecom company Orange to identify customers who are likely to churn in the near term in order to improve the service and create custom outreach campaigns that help retain customers.

Telecom companies face a competitive market. Many carriers lose revenue from postpaid customers due to churn. Hence the ability to accurately identify customer churn can be a huge competitive advantage.

Some of the factors contributing to telecom customer churn include:

* Perceived frequent service disruptions
* Poor customer service experiences in online/retail stores
* Offers from other competing carriers (better family plan, data plan, etc.).

In this scenario, we will use a concrete example of building a predictive customer churn model for telecom companies.

## Data Description

The dataset used to ingest is from the SIDKDD 2009 competition. It is called CATelcoCustomerChurnTrainingSample.csv and is located in the Data folder. The dataset consists of heterogeneous noisy data (numerical/categorical variables) from French Telecom company Orange and is anonymized.

The variables capture customer demographic information, call statistics (such as average call duration, call failure rate, etc., contract information, complaint statistics. Churn variable is binary (0 - did not churn, 1 - did churn).

## Scenario Structure

The folder structure of this scenario is arranged as follows:

* **Code**: Contains all the code related to churn prediction using AML Workbench  
* **Data**: Contains the dataset used in the scenario 
* **Labs**: Contains the detailed walktrhough of this chrun prediction example

The order of Hands-on Labs is as follows:

| Order| File Name | Realted Files in the Code Folder |
|--|-----------|------|
| 1 | `DataPreparation.md` | 'CATelcoCustomerChurnTrainingSample.dprep'<br>'CATelcoCustomerChurnTrainingSample.dconn'<br>'CATelcoCustomerChurnTrainingSample.csv' |
| 2 | `ModelingAndEvaluation.md` | 'CATelcoCustomerChurnModeling.py' |
| 3 | `ModelingAndEvaluationDocker.md` | 'CATelcoCustomerChurnModelingDocker.py' |
| 4 | `Operationalization.md` | 'model.pkl'<br>'churn_schema_gen.py' |

Follow the Labs in the sequential manner described above. The total estimated time to complete this scenario end-to-end is about XXmins.

## Conclusion
This scenario gives an overview of how to perform churn prediction using AML Workbench's Data Preparation tools, perform feature engineering to handle noisy heterogeneous data and operationalize the preditive model.

## Contact
Please feel free to contact Mithun Prasad (miprasad@microsoft.com) with any question or comment.
