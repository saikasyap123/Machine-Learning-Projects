import pandas as pd
import matplotlib.pyplot as plt  

### Helper function use when needed
def plot_regression_line(X,m,b):
        regression_x = X.values
        regression_y = []
        for x in regression_x:
		        y = m*x+b
		        regression_y.append(y)
        plt.plot(regression_x,regression_y)
        plt.pause(1)
        
	    
	

##Step 1: Read the CSV file and plot

data = pd.read_csv('E://student_scores.csv')
#print(data.head())
X = data['Hours']
Y = data['Scores']
plt.plot(X,Y,'o')
plt.title('Data Points')
plt.xlabel('Hours')
plt.ylabel('Scores')
#plt.show()
##Step2: Def a func grad_desc such that it takes m,b and returns a better value of m,b 
##so that the error reduces
m=0
b=0
def grad_desc(X,Y,m,b):

        for item in zip(X,Y):
            x = item[0]
            y_actual = item[1]
            y_pred = m*x+b
            error = y_pred - y_actual
            delta_m = -1*(error*x)*0.005
            delta_b = -1*error*0.005
            m = m + delta_m
            b = b + delta_b
        return m,b

m,b = grad_desc(X,Y,m,b)
plot_regression_line(X,m,b)
plt.show()
