import pandas as ps
import numpy as np
from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error as mae
from sklearn.metrics import mean_squared_error as mse
from sklearn.metrics import accuracy_score, f1_score
import matplotlib.pyplot as plt

from sklearn.neighbors import KNeighborsClassifier


data = fetch_california_housing(as_frame=True)
df = data.frame

x = df.drop(columns=["MedHouseVal"])
continuous_y = df["MedHouseVal"]

median_price = continuous_y.median()
y = (continuous_y > median_price).astype(int)

#---------------------------------------
#train test split

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.20, random_state=42)

scaler = StandardScaler()

x_train_scaler = scaler.fit_transform(x_train)
x_test_scaler = scaler.transform(x_test)

#---------------------------------------
#logistic regretion 
lg_model = LogisticRegression()
lg_model.fit(x_train_scaler, y_train)

predict_y_lg = lg_model.predict(x_test_scaler)

lg_mse = mse(y_test, predict_y_lg)
lg_mae = mae(y_test, predict_y_lg)
lg_f1 = f1_score(y_test, predict_y_lg)
lg_accuracy_score = accuracy_score(y_test, predict_y_lg)

print("lg MSE=", lg_mse)
print("lg MAE=", lg_mae)
print("lg F1", lg_f1)
print("lg accuacy= ", lg_accuracy_score)



#---------------------------------------------

knn_model = KNeighborsClassifier(n_neighbors=5)
knn_model.fit(x_train_scaler,y_train)

predict_y_knn = knn_model.predict(x_test_scaler)

knn_mse = mse(y_test, predict_y_knn)
knn_mae = mae(y_test, predict_y_knn)

knn_f1 = f1_score(y_test, predict_y_knn)
knn_accuracy_score = accuracy_score(y_test, predict_y_knn)

print("knn MSE= ", knn_mse)
print("knn MAE= ", knn_mae)
print("knn F1= ", knn_f1)
print("knn accuacy= ", knn_accuracy_score)
#-----------------------------------------------

plt.bar(['Logistic Regression', 'KNN'], [accuracy_score(y_test, predict_y_lg), accuracy_score(y_test, predict_y_knn)], color=['blue', 'orange'])
plt.show()
