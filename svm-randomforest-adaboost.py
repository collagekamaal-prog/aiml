import pandas as pd
import numpy as np

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

data = load_breast_cancer(as_frame=True)
df = data.frame

x = df.drop(columns=["target"])
y = df["target"]

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.20, random_state=42, stratify=y
)

# SVM
svm = Pipeline([
    ("scaler", StandardScaler()),
    ("classifier", SVC(kernel="rbf", C=1.0))
])
svm.fit(x_train, y_train)
pred_svm = svm.predict(x_test)

# Random Forest
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(x_train, y_train)
pred_rf = rf.predict(x_test)

# AdaBoost
ada = AdaBoostClassifier(n_estimators=50, learning_rate=1.0, random_state=42)
ada.fit(x_train, y_train)
pred_ada = ada.predict(x_test)

# K-Fold Cross Validation
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
scores = cross_val_score(svm, x_train, y_train, cv=cv, scoring="f1_weighted")

print("K-Fold scores:", scores)
print("Mean:", scores.mean())
print("Standard deviation:", scores.std())

# Evaluation function
def evaluation(y_true, y_pred):
    print("Accuracy:", accuracy_score(y_true, y_pred))
    print("Precision:", precision_score(y_true, y_pred))
    print("Recall:", recall_score(y_true, y_pred))
    print("F1 Score:", f1_score(y_true, y_pred))
    print("Confusion Matrix:\n", confusion_matrix(y_true, y_pred))

print("\nSVM Evaluation")
evaluation(y_test, pred_svm)

print("\nRandom Forest Evaluation")
evaluation(y_test, pred_rf)

print("\nAdaBoost Evaluation")
evaluation(y_test, pred_ada)
