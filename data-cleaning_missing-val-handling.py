import pandas as pd
import numpy as np

from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

data = load_diabetes(as_frame=True)
df = data.frame

df.drop_duplicates(inplace=True)
df.fillna(df.median(), inplace=True)

x = df.drop(columns=["target"])
y = df["target"]

x_train, x_test, y_train, y_test = train_test_split(
    x, y, random_state=42, test_size=0.20
)

scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)

print("Statistical Analysis:")
print(df.describe())

print("Training data shape:", x_train_scaled.shape)
print("Testing data shape:", x_test_scaled.shape)

df.iloc[:, :5].hist(figsize=(10, 6))
plt.tight_layout()
plt.show()

df.iloc[:, :5].plot(kind="box", figsize=(10, 5))
plt.show()
