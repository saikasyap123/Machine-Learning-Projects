import pandas as pd 
from sklearn.feature_extraction.text import CountVectorizer
from sklearn import svm
from sklearn.model_selection import GridSearchCV

data = pd.read_csv("E://spam.csv")
#print(data.head())
#print(data.describe())
X = data['EmailText']
Y = data['Label']
x_train, y_train = X[0:4457], Y[0:4457]
x_test, y_test = X[4457:], Y[4457:]
cv = CountVectorizer()
train_new = cv.fit_transform(x_train)
tuned_params = {'kernel':['linear','rbf'],'gamma':[1e-3,1e-4],'C':[1,10,100,1000]}
#GridSearchCv will help us to find better parameters for the model
model = GridSearchCV(svm.SVC(),tuned_params)
model.fit(train_new,y_train)
print("Best model params: {}".format(model.best_params_))
test_new = cv.transform(x_test)
print("Accuracy :{}".format(model.score(test_new,y_test)))
