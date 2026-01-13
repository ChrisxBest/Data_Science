# This repository contains machine learning models and projects and is mainly based on supervised learning.
## 1. The focus is set on regression algorithms like Multiple Linear Regression (MLR)
## 2. The focus is set on classification algorithms like Decicion Tree (DT), Logarithmic regression (LR) and KNN 
## 3. Unsupervised Learning like clustering and dimensionality reduction will be added soon.

## General information rf. ML-Multiple linear regression:
1. The data points are independent of each other
2. There is a linear relationship between the feature and the target
3. The residuals are normally distributed
4. The residuals have constant variance
5. The features are independent of each other

## General Workflow:
1. EDA + Outlier Detection using RANSAC, DBSCAN or visualization tools like Boxplots etc.
2. Train-Test-Split of the dataset into feature matrices and target vectors
3. Choosing and building a baseline model, based on the specific task and the evaluation metrics
4. Choosing and building additional models, based on the specific task and the evaluation metrics. Instantiate models with specific hyperparameters
6. Fit model to data (model fitting)
7. Make predictions with trained models to predict dedicated aim datasets
