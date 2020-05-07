from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
data = pd.read_csv('E://Iris.csv')
#print(data.head())
labels = data['Species']
X = data.drop(['Id','Species'],axis=1)
#step1:center the data points around origin
#here X_std is original higher dimensional space
X_std = StandardScaler().fit_transform(X)
#step2:let us first transform this into pca subspace but with original dimensions
#pca = PCA(n_components=4)
#X_transform = pca.fit_transform(X_std)
#let us know the variance obtained along each dimension
#print(pca.explained_variance_ratio_)
#here our main motto is to reduce the original dimensions to priniciple components
#let us convert into pca subspace with the two principle components retaining maximum variance
pca = PCA(n_components=2)
X_transform = pca.fit_transform(X_std)
#print(X_transform)
#let us perform the inverse zip on X_transform to extract the first two principle components
pca1 = list(zip(*X_transform))[0]
pca2 = list(zip(*X_transform))[1]
colorsdict = {}
colorsdict['Iris-setosa']='blue'
colorsdict['Iris-versicolor']='red'
colorsdict['Iris-virginica']='green'
#print(pca1)
#print(pca2)
i=0
for label in labels:
    plt.scatter(pca1[i],pca2[i],color=colorsdict[label])
    i=i+1
plt.show()
