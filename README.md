## 1. Supervised Machine Learning – Classification (`1_Supervised_ML_classification/`)

The classification notebooks cover end-to-end modeling pipelines in **Scikit-learn**, focusing on structured preprocessing, hyperparameter optimization, model comparison, and ensemble methods.

### Technical Highlights
- **End-to-End Preprocessing Pipelines:** Modular feature transformations using `Pipeline` and `ColumnTransformer` (`4_Pipeline_column_transformer_example.ipynb`) to keep preprocessing clean and reproducible.
- **Hyperparameter Tuning & Evaluation:** Grid search (`GridSearchCV`) evaluated via **ROC-AUC** for imbalanced classification tasks (such as fake account and campaign detection in `2_Fake_accounts_detection_gridsearch_ROC_AUC.ipynb` and `3_Campagnes_gridsearch_ROC_AUC.ipynb`).
- **Model Benchmarking, Ensembling & NLP:** Comparison across KNN, Logistic Regression, Random Forests, ensemble models, and text/NLP workflows with SVM (`0_`–`7_*.ipynb`).

---

## 2. Supervised Machine Learning – Regression (`2_Supervised_ML_regression/`)

This module demonstrates continuous target modeling and regression fundamentals.

### Technical Highlights
- **Multiple Linear Regression:** Modeling relationships between multiple predictor variables and a continuous target in `0_Multiple_linear_regression.ipynb`.

---

## 3. Data Gathering & Web Scraping (`3_Data_gathering/`)

The notebooks in this folder demonstrate programmatic data collection from web sources into structured datasets for downstream analysis.

### Technical Highlights
- **Webpage Data Retrieval:** Fetching and parsing web content in `0_Retrieving data from Webpage.ipynb`.
- **Automated Web Scraping:** Structured scraping workflows in `1_Web_scraping.ipynb`.

---

## 4. Outlier Detection & Robust Modeling (`4_Outlier Detection/`)

These scripts address noisy real-world data by combining anomaly detection with outlier-resistant feature engineering and regression.

### Technical Highlights
- **Statistical Outlier Detection:** Identification of anomalies and extreme values in `1_Outlier_detection.py`.
- **Robust Feature Engineering:** Scaling and feature preparation based on **Median** and **Median Absolute Deviation (MAD)** (`2_Robust_feature_engineering (median & mad).py`).
- **Outlier-Resistant Regression:** Fitting linear models robust to outliers using **RANSAC** (`3_RANSAC-Regression.py`).

---

## 5. Distributed Analytics & ML (`5_PySpark/`)

The PySpark notebooks scale data manipulation and machine learning workflows to distributed computing environments with **Apache Spark**.

### Technical Highlights
- **PySpark DataFrames:** Distributed data transformations and processing in `4_PySpark.ipynb`.
- **Distributed Logistic Regression:** Classification modeling with **PySpark MLlib** in `5_PySpark_LogReg.ipynb`.

---

## 6. End-to-End Classification Project (`6_Supervised_ML_classification_project/`)

This applied project consolidates data preparation, feature engineering, and supervised classification into a complete predictive workflow.

### Technical Highlights
- **Vehicle Defect & Quality Prediction:** Classification pipeline in `0_Bad_cars_detection.ipynb` designed to identify problematic vehicles based on technical and historical features.

---

## Tech Stack
- **Languages:** Python, SQL
- **Machine Learning & Big Data:** Scikit-learn, PySpark (MLlib), Pandas, NumPy
- **Data Acquisition & Visualization:** Requests, BeautifulSoup, Matplotlib, Seaborn
- **Version Control & Environment:** Git, GitHub, Jupyter Notebooks, VS Code