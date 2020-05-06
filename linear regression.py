import pandas as pd   #pylint: disable=unused-import
import matplotlib.pyplot as plt   #pylint: disable=unused-import
from sklearn.linear_model import LinearRegression  #pylint: disable=unused-import
import numpy as np    #pylint: disable=unused-import
from sklearn.metrics import mean_squared_error

data = pd.read_csv('E:\student_scores.csv')
#print(data.describe())
x = data['Hours'].values.reshape(-1,1)
y = data['Scores'].values.reshape(-1,1)
x_train, y_train = x[0:20], y[0:20]
x_test, y_test = x[19:], y[19:]
#print(x_train, x_test)
model = LinearRegression()
model.fit(x_train, y_train)
regression_line = model.predict(x)
print("coefficients: {} ".format(model.coef_))
print("score: {}".format(model.score(x_train,y_train)))
print("error: {}".format(mean_squared_error(y_test,model.predict(x_test))))

plt.plot(x,regression_line)

plt.plot(x,y,'o',color='g')
plt.title('Data Points and Model')
plt.xlabel('Hours')
plt.ylabel('Scores')
plt.legend(loc ="upper right")
plt.tight_layout()
plt.show()