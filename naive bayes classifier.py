import pandas as pd  
import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import mean_squared_error

data = pd.read_csv('E:/titanic.csv')
data = data.drop(["Name"],axis=1)
#print(data.describe())
#print(data.head())
ages = data["Age"].values
fares = data["Fare"].values
survived = data["Survived"].values
colors =[]
for item in survived:
    if item ==0:
        colors.append('red')
    else:
        colors.append('green')
features = data.drop(['Survived'],axis =1).values
targets = data['Survived'].values
x_train, y_train = features[0:710], targets[0:710]
x_test, y_test = features[710:], targets[710:]
model = GaussianNB()
model.fit(x_train,y_train)
predicted_values = model.predict(x_test)
for item in zip(y_test,predicted_values):
    print("Actual: {} Predicted: {}".format(item[0],item[1]))

print(model.score(x_test,y_test))
#plt.scatter(ages,fares,s=50,color=colors)
#plt.title("Data Ages vs Fares")
#plt.show()

