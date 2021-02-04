# -*- coding: utf-8 -*-
"""SVM_iris.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15o3D2bEye3abdJHaEz0Actl7N5Q5Xb9P
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
# %matplotlib inline
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

iris = load_iris()

dir(iris)

iris.feature_names

iris.target_names

df = pd.DataFrame(iris.data, columns=iris.feature_names)
df.head()

df['target'] = iris.target
df.head()

df[df.target==1].head()

df[df.target==2].head()

df['flower_name'] = df.target.apply(lambda x: iris.target_names[x])
df.head()

df0= df[df.target==0]
df1= df[df.target==1]
df2= df[df.target==2]

plt.xlabel('Sepal length')
plt.ylabel('Sepal widht')
plt.scatter(df0['sepal length (cm)'], df0['sepal width (cm)'], color='green', marker='+')
plt.scatter(df1['sepal length (cm)'], df1['sepal width (cm)'], color='blue', marker='.')

plt.xlabel('Petal length')
plt.ylabel('Petal widht')
plt.scatter(df0['petal length (cm)'], df0['petal width (cm)'], color='green', marker='+')
plt.scatter(df1['petal length (cm)'], df1['petal width (cm)'], color='blue', marker='.')

X = df.drop(['target', 'flower_name'], axis='columns')
y = df.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

len(X_train), len(X_test)

model = SVC(C=10)

model.fit(X_train, y_train)

model.score(X_test, y_test)

model.predict([[5.2,4.0,6.4,2.4]])

