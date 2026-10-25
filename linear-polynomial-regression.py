import pandas as pd
import numpy as np

from sklearn.datasets import load_diabetes
from sklearn.metrics import mean_absolute_error as mae
from sklearn.metrics import mean_squared_error as mse
from sklearn.metrics import r2_score as r2
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

data = load_diabetes(as_frame=True)
df = data.frame

x = df.drop(columns=["target"])
y = df["target"]

x_train, x_test, y_train, y_test = train_test_split(
    x, y, random_state=42, test_size=0.20
)

linear_model = LinearRegression()
linear_model.fit(x_train, y_train)
y_pred_linear = linear_model.predict(x_test)

mse_linear = mse(y_test, y_pred_linear)
mae_linear = mae(y_test, y_pred_linear)
r2_linear = r2(y_test, y_pred_linear)

print("Linear Regression")
print("MSE:", mse_linear)
print("MAE:", mae_linear)
print("R2 Score:", r2_linear)

poly = PolynomialFeatures(degree=2)
x_train_poly = poly.fit_transform(x_train)
x_test_poly = poly.transform(x_test)

poly_model = LinearRegression()
poly_model.fit(x_train_poly, y_train)
y_pred_poly = poly_model.predict(x_test_poly)

mae_poly = mae(y_test, y_pred_poly)
mse_poly = mse(y_test, y_pred_poly)
r2_poly = r2(y_test, y_pred_poly)

print("\nPolynomial Regression")
print("MSE:", mse_poly)
print("MAE:", mae_poly)
print("R2 Score:", r2_poly)
