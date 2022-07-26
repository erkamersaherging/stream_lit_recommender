"""
UTILS 
- Helper functions to use for your recommender funcions, etc
- Data: import files/models here e.g.
    - movies: list of movie titles and assigned cluster
    - ratings
    - user_item_matrix
    - item-item matrix 
- Models:
    - nmf_model: trained sklearn NMF model
"""
import pandas as pd
import numpy as np
from fuzzywuzzy import process
import pickle


movies = pd.read_csv('data/movies_clusters_ratings.csv', index_col='movieid')  

with open('data/movies_user_ratings.bin', 'rb') as f:
    R_nmf = pickle.load(f)

with open('data/nmf_zeros.bin', 'rb') as f:
    NMF = pickle.load(f)



def create_user_vector(user_rating):
    """
    Convert dict of user_ratings to a user_vector
    """       
    dict = convert_user_rating(user_rating)
    
    df = R_nmf.iloc[[0]].fillna(0) * 0

    for key in dict:
        df[key]=dict[key]


    return df


def convert_user_rating(user_rating):
    wuzzy_dic = {}
    for key in user_rating:

        wuzzy_key = match_movie_title(key)
        wuzzy_dic[wuzzy_key] = user_rating[key]

    id_dic = {}
    for key in wuzzy_dic:
        
        id_key = give_Id_from_title(key)
        id_dic[id_key]=wuzzy_dic[key]
    return id_dic



def match_movie_title(input_title):
    """
    Matches inputed movie title to existing one in the list with fuzzywuzzy
    """
    matched_title = process.extractOne(input_title, movies['title'])[0]

    return matched_title


def give_Id_from_title(movie_title):
    
    return movies.loc[movies['title']== movie_title].index[0]




# def print_movie_titles(movie_titles):
#     """
#     Prints list of movie titles in cli app
#     """    
#     for movie_id in movie_titles:
#         print(f'> {movie_id}')
#     pass




def lookup_movieId(movieId):
    """
    Convert output of recommendation to movie title
    """
    return movies['title'].loc[movies.index == movieId].values.tolist()


if __name__ == '__main__':
    print(give_Id_from_title('Toy Story'))

    print(match_movie_title('Toy Story'))

    user_rating = {
    'the lion king': 5,
    'terminator': 5,
    'star wars': 2
    }

    print(convert_user_rating(user_rating))

    print(create_user_vector(user_rating))