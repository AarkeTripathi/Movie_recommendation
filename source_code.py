import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.linear_model import LinearRegression
import difflib

movie_df=pd.read_csv('movies.csv')
movie_df.head()

selected_features=['genres','keywords','tagline','cast','director']

for feature in selected_features:
    movie_df[feature]=movie_df[feature].fillna('')

combined=movie_df['genres']+' '+movie_df['keywords']+' '+movie_df['tagline']+' '+movie_df['cast']+' '+movie_df['director']

vectorizer=TfidfVectorizer()
feature_vector=vectorizer.fit_transform(combined)
feature_vector

similarity=cosine_similarity(feature_vector)

lst=movie_df['original_title'].to_list()

movie_name=input('Enter the name of your favourite movie: ')

find_close_match=difflib.get_close_matches(movie_name,lst)
movie_name=find_close_match[0]

movie_df.set_index('original_title', inplace=True)  

def return_ind(movie_df,movie_name):
    for i in range(movie_df.shape[0]):
        if movie_df.index[i]==movie_name:
            return i
        
ind=return_ind(movie_df,movie_name)
similarity_score=list(enumerate(similarity[ind]))
sorted_similarity_score=sorted(similarity_score, key=lambda x:x[1], reverse=True)

print('\nMovies recommended for you are:')
for i in range(20):
    index=sorted_similarity_score[i][0]
    print(movie_df.index[index])
