# Titanic Survival Prediction using Neural Network

This project predicts **passenger survival on the Titanic** using a **deep neural network** and compares it with KNN and Perceptron models.

## Features
- Data cleaning and preprocessing:
  - Handling missing values (Age, Cabin, Embarked)
  - Encoding categorical variables (Sex)
- Selecting features: Pclass, Sex, Age, SibSp, Parch, Fare
- Building and training a **Neural Network** with TensorFlow/Keras
- Training for 100 epochs with accuracy and loss visualization
- Evaluating performance using:
  - Accuracy
  - Confusion Matrix
  - Precision, Recall, F1-score
- Making predictions for new passengers
- Comparing results with **KNN** and **Perceptron**

## Requirements
- Python 3.x
- pandas
- numpy
- matplotlib
- scikit-learn
- tensorflow

Install dependencies:
```bash
pip install pandas numpy matplotlib scikit-learn tensorflow

Usage

1. Open the project in any Python IDE or Jupyter Notebook.


2. Place the dataset files in the data/ folder:

train.csv (training data)

test.csv (test data)

gender_submission.csv (test labels)



3. Run the notebook or script to:

Train the neural network

Evaluate test performance

Compare with KNN and Perceptron

Make predictions for new passengers


