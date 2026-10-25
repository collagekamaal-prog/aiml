import pandas as ps
import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.model_selection import StratifiedKFold, cross_val_score
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

data = load_breast_cancer(as_frame= True)
df= data.frame

x = df.drop(columns=["target"])
y = df["target"]

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.20, random_state=42, stratify=y)

#-----------------------------------------
#svm

svm = Pipeline([('scaller', StandardScaler()), ('classifier', SVC(kernel='rbf', C=1.0))])

svm.fit(x_train, y_train)

predsvm = svm.predict(x_test)

#---------------------------------------------------------
#Random forest 

rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(x_train,y_train)
pred_rf = rf.predict(x_test)

#-------------------------------------------------------------
#AdaBoost

ada = AdaBoostClassifier(n_estimators=50, learning_rate=1.0, random_state=42)

ada.fit(x_train,y_train)
pred_ada = ada.predict(x_test)

#---------------------------------------------------------------
#kfold cross validation

cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

scores = cross_val_score(svm, x_train, y_train, cv=cv, scoring='f1_weighted')

print('fold scores: ',scores )
print('Mean: ', scores.mean)
print('std', scores.std)


#-------------------------------------------------------------------------
#evaluatio function

def evaluation(y_true, y_pred):
    print('accuracy: ', accuracy_score(y_true, y_pred))
    print('precision: ',precision_score(y_pred, y_pred))
    print('recall: ', recall_score(y_true, y_pred))
    print('f1_score: ', f1_score(y_true, y_pred))
    print('confusion matrix: ', confusion_matrix(y_true, y_pred))
    

evaluation(y_test,predsvm)
evaluation(y_test, pred_rf)
evaluation(y_test, pred_ada)
#-----------------------------------------------------------------------------
