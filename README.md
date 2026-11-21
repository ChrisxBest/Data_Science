## 1. Supervised Machine Learning (`0_Supervised_ML_regression/`, `1_Supervised_ML_classification/`, `4_Supervised_ML_classification_project/`)

The supervised learning modules cover regression and classification pipelines in **Scikit-learn**, focusing on reproducible data preprocessing, systematic model evaluation, and hyperparameter optimization.

### Technical Highlights
- **End-to-End Preprocessing Pipelines:** Modular feature transformations using `Pipeline` and `ColumnTransformer` to keep preprocessing structured and reproducible.
- **Hyperparameter Tuning & Evaluation:** Grid search (`GridSearchCV`) evaluated via **ROC-AUC** for imbalanced classification workflows (such as fake account and campaign detection).
- **Model Benchmarking & Ensembling:** Comparison across KNN, Logistic Regression, Random Forests, Support Vector Machines (SVM), NLP workflows, and ensemble models.
- **Capstone Classification Project:** End-to-end vehicle defect/quality classification workflow in `0_Bad_cars_detection.ipynb`.

---

## 2. Outlier Detection & Robust Modeling (`2_Outlier Detection/`)

These scripts address noisy real-world datasets by combining anomaly detection with outlier-resistant feature engineering and regression.

### Technical Highlights
- **Statistical Outlier Detection:** Identification of anomalies and extreme values in `1_Outlier_detection.py`.
- **Robust Feature Engineering:** Scaling and transformation based on **Median** and **Median Absolute Deviation (MAD)** (`2_Robust_feature_engineering (median & mad).py`).
- **Outlier-Resistant Regression:** Fitting linear models robust to outliers using **RANSAC** (`3_RANSAC-Regression.py`).

---

## 3. Data Gathering & Web Scraping (`3_Data_gathering/`)

The notebooks in this folder demonstrate programmatic extraction of external web data into structured datasets for downstream analysis.

### Technical Highlights
- **Webpage Data Retrieval:** Fetching and parsing web content in `0_Retrieving data from Webpage.ipynb`.
- **Automated Web Scraping:** Structured scraping workflows in `1_Web_scraping.ipynb`.

---

## 4. Distributed Analytics & ML (`5_PySpark/`)

The PySpark notebooks scale data manipulation and machine learning workflows to distributed computing environments with **Apache Spark**.

### Technical Highlights
- **PySpark DataFrames:** Distributed data transformations and processing in `4_PySpark.ipynb`.
- **Distributed Logistic Regression:** Classification modeling with **PySpark MLlib** in `5_PySpark_LogReg.ipynb`.

---

## Tech Stack
- **Languages:** Python, SQL
- **Machine Learning & Big Data:** Scikit-learn, PySpark (MLlib), Pandas, NumPy
- **Data Acquisition & Visualization:** Requests, BeautifulSoup, Matplotlib, Seaborn
- **Version Control & Environment:** Git, GitHub, Jupyter Notebooks, VS Code