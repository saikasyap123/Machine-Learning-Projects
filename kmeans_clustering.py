from copy import deepcopy
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.metrics.pairwise import euclidean_distances
plt.rcParams['figure.figsize'] = (16, 9)
plt.ion()

#####Helper Functions#####
def show_plot(C,X):
    colors = ['r', 'g', 'b', 'y', 'c', 'r']
    for i in range(k):

            points = np.array([X[j] for j in range(len(X)) if clusters[j] == i])
            plt.scatter(points[:, 0], points[:, 1], s=20, c=colors[i], alpha=0.2)
            plt.scatter(C[i,0], C[i,1], marker='D', s=200, c='black',edgecolor='w')

    plt.draw()
    plt.pause(5)
    plt.clf()

def get_random_centeroids(X,k):
    C_x = np.random.randint(0, np.max(X)-20, size=k) 
    C_y = np.random.randint(0, np.max(X)-20, size=k)
    C = np.array(list(zip(C_x, C_y)))
    return C,C_x,C_y    

# Euclidean Distance Caculator
def dist(a, b, ax=1):
    return np.linalg.norm(a - b, axis=ax)    

#######Begin Here###############################
## Step1: Read Dataset 
data = pd.read_csv('E://kmeans_data.csv')
#print(data.head())

## Step2: Get values f1,f2 and plotting it
f1 = data['V1']
f2 = data['V2']
X = list(zip(f1,f2))


## Step3: Plot data and centroids
k = 3
c,c_x,c_y = get_random_centeroids(X,k)
#a = plt.scatter(f1,f2,c='black',s=7)
#b = plt.scatter(c_x,c_y,marker='*',c='red',s=100)
#plt.show(a)

##Init K Random Centroids
c_old = np.zeros(c.shape)
clusters = np.zeros(len(X))
change_in_c = dist(c,c_old,None)
## Step4: Run Kmeans
while change_in_c != 0:    
    ##Part1: Cluster Assignment. Assign points to closest cluster
    for i in range(len(X)):
        distances = dist(X[i],c)
        clusters[i] = np.argmin(distances)

    ##Part2: Cluster Movement: Find the new centroids 
    ##by taking the average value of all points and moving centroid there
    c_old = deepcopy(c)
    for i in range(k):
        points = [X[j] for j in range(len(X)) if clusters[j] == i]
        c[i] = np.mean(points,axis=0)
    show_plot(c,X)
    change_in_c = dist(c,c_old,None)

plt.show()

