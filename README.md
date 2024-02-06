# Loan Defaulter Prediction

This project aims to provide optimal solutions to a bank by cautioning against the risks associated with loan approvals for businesses. It involves exploratory data analysis, data cleaning, feature engineering, and the application of classification models to predict loan defaulters. The project achieves a 92% accuracy rate in predictions.

### Project Overview

The project encompasses the following steps:

1. **Exploratory Data Analysis (EDA):** Conducted thorough analysis on the dataset to gain insights into the data distribution, relationships between variables, and identify potential patterns.

2. **Data Cleaning:** Cleaned the dataset to handle missing values, outliers, and inconsistencies, ensuring the data is suitable for analysis and modeling.

3. **Feature Engineering:** Engineered relevant features from the dataset to enhance the predictive power of the models.

4. **Modeling:** Applied various classification models including K-Nearest Neighbors, Decision Trees, Naive Bayes, Random Forest, Gradient Boosting, AdaBoost, XGBoost, and Support Vector Machines. Ensemble techniques were also employed to improve model performance.

5. **Hyperparameter Tuning:** Utilized techniques such as GridSearchCV and RandomizedSearchCV to optimize model hyperparameters, enhancing model accuracy.

6. **Model Evaluation:** Evaluated models using metrics such as accuracy, precision, recall, F1-score, and ROC-AUC score to assess performance and identify the best-performing model.

7. **Deployment:** Deployed the predictive model using Flask framework on a Platform-as-a-Service (PAAS) platform, making it accessible for real-time predictions.

### Libraries Used

- Pandas
- NumPy
- Seaborn
- Matplotlib
- Category Encoders
- SciPy
- Scikit-learn
- MLxtend
- XGBoost
- Imbalanced-learn (imblearn)

### Installation

To run the project, install the required libraries using the following command:

```bash
pip install pandas numpy seaborn matplotlib category_encoders scipy scikit-learn mlxtend xgboost imbalanced-learn
```
