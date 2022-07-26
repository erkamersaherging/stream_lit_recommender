"""
Contains various recommondation implementations
all algorithms return a list of movieids
"""

import pandas as pd
from utils import match_movie_title,give_Id_from_title,convert_user_rating,create_user_vector,lookup_movieId,movies
import pickle
import numpy as np



def recommend_random(movies, user_rating, k=5):
    """
    return k random unseen movies for user 
    """

    return random_movies


# def recommend_most_popular(user_rating, movies, ratings, k=5):
#     """
#     return k movies from list of 50 best rated movies unseen for user
#     """

#     return popular movies


# def recommend_from_same_cluster(user_rating, movies, k=3):

#     return best_rated_title, movie_titles

def cluster_recomender(movie_you_like):

    if movies['title'].isin([movie_you_like]).max():
        
        list = [movie_you_like]

        boolean_series = movies['title'].isin(list)
        
        cluster = movies.loc[boolean_series]['cluster_no'].item()

        filter = movies['cluster_no'] == cluster

        movies_from_cluster = movies[['title','cluster_no']].loc[filter]

        recommendations = movies_from_cluster[['title']].sample(5).to_numpy()

        list = recommendations.tolist()

        clean=[]
        for i in range(len(list)):
            clean.append(list[i][0])


        

        return clean



def recommend_with_NMF(user_rating, k=5):

    # discard seen movies and sort the prediction
    
    # return a list of movie ids


    with open('data/nmf_zeros.bin', 'rb') as f:
        NMF = pickle.load(f)

    with open('data/movies_user_ratings.bin', 'rb') as f:
        R_nmf = pickle.load(f)
    #convert user rating
    df = create_user_vector(user_rating)

    P = NMF.transform(df)

    Q = NMF.components_

    R = np.dot(P,Q)

    S = R[0].copy()

    S.sort()

    mask = np.isin(R[0], S[-5:])

    movieids = R_nmf.columns[mask]

    recomendations = []

    for i in movieids:
        title = lookup_movieId(i)
        recomendations.append(title[0])

    return recomendations





def recommend_with_user_similarity(user_item_matrix, user_rating, k=5):
    pass


def similar_movies(movieId, movie_movie_distance_matrix):
    pass



if __name__ == '__main__':

    user_rating = {
    'heat': 5,
    'saw': 5,
    'paris,texas': 2
    }

    print(recommend_with_NMF(user_rating, k=5))
    print(cluster_recomender('Toy Story'))
