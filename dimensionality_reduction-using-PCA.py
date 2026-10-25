import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

data = load_breast_cancer(as_frame=True)
x = data.data
y = data.target

print("Features before PCA:", x.shape[1])

x_train, x_test, y_train, y_test = train_test_split(
    x, y, random_state=42, test_size=0.20, stratify=y
)

scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

model = LogisticRegression(max_iter=1000)
model.fit(x_train, y_train)
y_pred = model.predict(x_test)

print("Accuracy before PCA:", accuracy_score(y_test, y_pred))

pca = PCA(n_components=2)
x_train_pca = pca.fit_transform(x_train)
x_test_pca = pca.transform(x_test)

print("Features after PCA:", x_train_pca.shape[1])

model2 = LogisticRegression(max_iter=1000)
model2.fit(x_train_pca, y_train)
y_pred_pca = model2.predict(x_test_pca)

print("Accuracy after PCA:", accuracy_score(y_test, y_pred_pca))

print("Explained variance by 2 components:", pca.explained_variance_ratio_.sum())

plt.scatter(x_train_pca[:, 0], x_train_pca[:, 1], c=y_train)
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.title("PCA Visualization")
plt.show()
