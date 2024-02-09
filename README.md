# Loan Defaulter Prediction

This project aims to provide optimal solutions to a bank by cautioning against the risks associated with loan approvals for businesses. It involves exploratory data analysis, data cleaning, feature engineering, and the application of classification models to predict loan defaulters. The project achieves a 92% accuracy rate in predictions.

### Project Interfaces
<img width="1440" alt="Screenshot 2024-02-06 at 15 30 13" src="https://github.com/PraveenLiyanage/Loan-Defaulter-Prediction/assets/111709030/65d1320a-0ece-4484-8c98-c468a2d8a88e">
<img width="1440" alt="Screenshot 2024-02-06 at 15 36 20" src="https://github.com/PraveenLiyanage/Loan-Defaulter-Prediction/assets/111709030/76df717a-20ee-4dd5-8c64-077a285b7b04">
<img width="1440" alt="Screenshot 2024-02-06 at 15 37 49" src="https://github.com/PraveenLiyanage/Loan-Defaulter-Prediction/assets/111709030/e4b6b2f5-c459-480b-b23c-c5659e1203be">

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
