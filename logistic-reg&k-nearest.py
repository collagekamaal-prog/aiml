import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

data = fetch_california_housing(as_frame=True)
df = data.frame

x = df.drop(columns=["MedHouseVal"])
y_continuous = df["MedHouseVal"]

price_median = y_continuous.median()
y = (y_continuous > price_median).astype(int)

x_train, x_test, y_train, y_test = train_test_split(
    x, y, random_state=42, test_size=0.20
)

scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)

lg_model = LogisticRegression(max_iter=1000)
lg_model.fit(x_train_scaled, y_train)
lg_pred_y = lg_model.predict(x_test_scaled)

print("Logistic Regression")
print("Accuracy:", accuracy_score(y_test, lg_pred_y))
print("Precision:", precision_score(y_test, lg_pred_y))
print("Recall:", recall_score(y_test, lg_pred_y))
print("F1 Score:", f1_score(y_test, lg_pred_y))
print("Confusion Matrix:\n", confusion_matrix(y_test, lg_pred_y))

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(x_train_scaled, y_train)
knn_pred_y = knn.predict(x_test_scaled)

print("\nK-Nearest Neighbors")
print("Accuracy:", accuracy_score(y_test, knn_pred_y))
print("Precision:", precision_score(y_test, knn_pred_y))
print("Recall:", recall_score(y_test, knn_pred_y))
print("F1 Score:", f1_score(y_test, knn_pred_y))
print("Confusion Matrix:\n", confusion_matrix(y_test, knn_pred_y))

cm = confusion_matrix(y_test, lg_pred_y)
plt.imshow(cm, cmap="Blues")
for i in range(2):
    for j in range(2):
        plt.text(j, i, cm[i, j], ha="center", va="center")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Logistic Regression Confusion Matrix")
plt.colorbar()
plt.show()
