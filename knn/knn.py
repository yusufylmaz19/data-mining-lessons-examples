from multiprocessing.sharedctypes import RawArray
import pandas as pd 
import numpy as np 


iris= pd.read_csv('iris.csv')

x = iris.iloc[:,1:5].values #bağımsız değişkenler
y = iris.iloc[:,5:].values #bağımlı değişken

from sklearn.preprocessing import LabelEncoder
label_encoder=LabelEncoder()
Y=label_encoder.fit_transform(y)

def NormalizeData(data):
    return (data - np.min(data)) / (np.max(data) - np.min(data))

X = NormalizeData(x)

from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.33,random_state=0)

from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
X_train=sc.fit_transform(x_train)
X_test=sc.fit_transform(x_test)


from sklearn.linear_model import LogisticRegression
logr = LogisticRegression(random_state=0)
logr.fit(X_train,y_train)

y_pred = logr.predict(X_test)

from sklearn.metrics import confusion_matrix,accuracy_score
cm = confusion_matrix(y_test,y_pred)

from sklearn.neighbors import KNeighborsClassifier
for i in range(1,10):
    knn=KNeighborsClassifier(n_neighbors=i,metric='minkowski')
    knn.fit(x_train,y_train)

    y_pred=knn.predict(X_test)

    acc = accuracy_score(y_test,y_pred)
    score = knn.score(X_test,y_test)
    print("Score: ",score)
    print("CM: ",cm)
    print("Basic KNN Acc: ",acc)
