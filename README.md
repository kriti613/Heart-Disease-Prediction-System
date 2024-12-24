# Heart Disease Prediction System

## Overview
This project is a Heart Disease Prediction System that uses machine learning models to predict the presence of heart disease based on patient data. The system leverages a dataset containing 14 features, including demographic, medical, and lifestyle variables, to classify individuals as having heart disease (target = 1) or not (target = 0). 

## Dataset Information

### General Information:
- **Number of Entries:** 1025
- **Number of Features:** 14 (13 predictors + 1 target)
- **Feature Types:** 
  - Continuous: `age`, `trestbps`, `chol`, `thalach`, `oldpeak`
  - Categorical: `sex`, `cp`, `fbs`, `restecg`, `exang`, `slope`, `ca`, `thal`
- **Target:** 
  - 1 (Heart Disease): 526 entries
  - 0 (No Heart Disease): 499 entries

### Dataset Description:
| Feature       | Description                                           |
|---------------|-------------------------------------------------------|
| `age`         | Age of the patient (years)                           |
| `sex`         | Gender (0 = Female, 1 = Male)                        |
| `cp`          | Chest pain type (0-3, indicating severity)           |
| `trestbps`    | Resting blood pressure (mm Hg)                       |
| `chol`        | Serum cholesterol (mg/dl)                            |
| `fbs`         | Fasting blood sugar > 120 mg/dl (0 = No, 1 = Yes)    |
| `restecg`     | Resting ECG results (0-2)                            |
| `thalach`     | Maximum heart rate achieved                          |
| `exang`       | Exercise-induced angina (0 = No, 1 = Yes)            |
| `oldpeak`     | ST depression induced by exercise                    |
| `slope`       | Slope of the ST segment (0-2)                        |
| `ca`          | Number of major vessels (0-4)                        |
| `thal`        | Thalassemia (0-3)                                    |
| `target`      | Presence of heart disease (0 = No, 1 = Yes)          |

### Null Values:
The dataset contains **no null values**.

### Statistical Summary:
- **Mean Age:** 54.43
- **Mean Cholesterol:** 246.00
- **Maximum Heart Rate (Thalach):** Mean = 149.11, Min = 71, Max = 202



## Data Visualization Insights

### 1. Comparing Continuous Variables:
- Box plots showed that individuals with heart disease tend to have higher values for age, resting blood pressure, and cholesterol levels.
<img src="https://github.com/kriti613/Heart-Disease-Prediction-System/blob/main/heart_disease_app/img/BoxPlot.png">

### 2. Comparing Categorical Variables with Target:
- Bar charts revealed potential associations between heart disease and specific patterns of chest pain types, ECG results, and exercise-induced angina.
<img src="https://github.com/kriti613/Heart-Disease-Prediction-System/blob/main/heart_disease_app/img/histogram.png">

### 3. Correlation Heatmap:
- The strongest positive correlation with heart disease was observed for `thalach` (maximum heart rate) with a correlation value of **0.42**. Other features showed weak or no significant correlations.
<img src="https://github.com/kriti613/Heart-Disease-Prediction-System/blob/main/heart_disease_app/img/heatmap.png">

### 4. Scatter Plot Analysis:
- A trend was observed where maximum heart rate decreased with increasing age. The overlap between individuals with and without heart disease was noted.
<img src="https://github.com/kriti613/Heart-Disease-Prediction-System/blob/main/heart_disease_app/img/scatterplot.png">

## Machine Learning Models

### Models Implemented:
1. **Logistic Regression**
2. **Random Forest**
3. **K-Nearest Neighbors (KNN)**
4. **Decision Tree**

### Model Performances:
| Model                 | Accuracy  |
|-----------------------|-----------|
| Decision Tree         | 98.54%    |
| Random Forest         | 98.54%    |
| Logistic Regression   | 78.54%    |
| KNN                   | 73.17%    |

### Best Model:
The **Random Forest model** was selected as the best-performing model due to its high accuracy of **98.54%**.

## Saving the Model
The final model was saved as a pickle file for future use.

```python
filename = 'rf_model.pkl'

# Save the model
with open(filename, 'wb') as file:
    pickle.dump(rf_model, file)
```

## Backend Project Architecture

The architecture of the Heart Disease Prediction System is outlined below:

```plaintext
                           +-----------------------+
                           |   User Interface      |
                           | (HTML Form & CSS)     |
                           +-----------------------+
                                      |
                                      v
                         +----------------------------+
                         |      Flask Backend         |
                         |  - Routes: / & /predict    |
                         +----------------------------+
                                      |
          +---------------------------+--------------------------+
          |                                                      |
          v                                                      v
+-----------------------+                             +-----------------------+
| Input Preprocessing   |                             |     Random Forest     |
| - Validate data       |                             |    Machine Learning   |
| - Format for model    |                             | - Load rf_model.pkl   |
+-----------------------+                             | - Make predictions    |
                                                      +-----------------------+
                                                                 |
                                                                 v
                                                  +-----------------------+
                                                  |    Result & Probability|
                                                  | (Heart Disease: Yes/No |
                                                  |  & Likelihood %)       |
                                                  +-----------------------+
```

## Output

Input Values in the form- 
<img src"">

Prediction Result -
<img src"">

## Conclusion
This project demonstrates the application of machine learning models for predicting heart disease. By analyzing medical data and training various models, the system achieved a high prediction accuracy with the Random Forest model. Future enhancements could involve hyperparameter tuning, feature engineering, and testing on new datasets.
