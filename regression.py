import pandas as ps
import numpy as np
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_absolute_error as mae
from sklearn.metrics import mean_squared_error as mse
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt

# ----x data load x----
data = load_diabetes(as_frame=True)
df = data.frame

print(df.head)
print(df.shape)

# ----x defin x and y x----
x = df.drop(columns=["target"]) # x is the table except target column
y = df["target"] # y is only the target column

# x in the on which the y is calculated  


# ----x train test split x----
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.20, random_state=12)
 
print("training = ", len(x_train))
print("testing = ", len(x_test))


# ----x Linear regration x----
linear_model = LinearRegression()
linear_model.fit(x_train,y_train)

y_pred_linear = linear_model.predict(x_test) # predected value of y_test compare with actual y_test

# print(y_pred_linear)
# print(y_test)
#------------------------------------------------

# ----x poly regration x----

poly= PolynomialFeatures(degree=2)

x_train_poly = poly.fit_transform(x_train)

x_test_poly = poly.fit_transform(x_test)
#dont need to convert the y beCAUSE ITS SINGLE TABLE 

poly_model = LinearRegression()
poly_model.fit(x_train_poly, y_train)

y_pred_poly = poly_model.predict(x_test_poly)
#-----------------------------------------------


# ----x mse and mae for linear model x----
mse_linear = mse(y_test, y_pred_linear)
mae_linear = mae(y_test, y_pred_linear)
r2_linear = r2_score(y_test, y_pred_linear)

print("mse_linear: ", mse_linear)
print("mae_linear: ", mae_linear)
print("r2_score", r2_linear)

#------------------------------------
# ----x mse and mae for poly model x----
mse_poly = mse(y_test,y_pred_poly)
mae_poly = mae(y_test,y_pred_poly)
r2_poly = r2_score(y_test, y_pred_poly)

print("mse_poly: ", mse_poly)
print("mae_poly: ", mae_poly)
print("r2_score", r2_poly)
#-------------------------------------
#----x visulization x----

# Create the plot window
plt.figure(figsize=(8, 6))

# Plot actual vs predicted points

plt.scatter(y_pred_linear, y_pred_poly, y_test, color="blue")
line_plot = [min(y_test), max(y_test)]
plt.plot(line_plot, line_plot, color="Red", linestyle="--", linewidth=2, label="Perfect Fit (y = x)")
plt.show()

#-------------------------------------
