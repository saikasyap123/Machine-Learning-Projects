from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd 
import numpy as np 
def get_title(index):
    return data[data.index==index]['title'].values[0]
def get_index(title):
    return data[data.title==title]['index'].values[0]
cv = CountVectorizer()
data = pd.read_csv('E://movie_dataset.csv')
features =['keywords','cast','genres','director']
for feature in features:
    data[feature] = data[feature].fillna('')
def combine(row):
    return row['keywords']+" "+row['cast']+" "+row['genres']+" "+row['director']
data['combined_features']=data.apply(combine,axis=1)
count_matrix = cv.fit_transform(data['combined_features'])
cosine_sim = cosine_similarity(count_matrix)
movie_user_like='Avatar'
ind = get_index(movie_user_like)
similar_movies = list(enumerate(cosine_sim[ind]))
sorted_movies = sorted(similar_movies,key=lambda x:x[1],reverse=True)
i=0
for movie in sorted_movies:
    print(get_title(movie[0]))
    i=i+1
    if i>50:
        break
#print(data['combined_features'])
#print(data.columns)
#print(data.head())

