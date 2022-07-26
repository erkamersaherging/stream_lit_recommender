import streamlit as st
import pandas as pd
from recommender import recommend_with_NMF,cluster_recomender

df = pd.read_csv('data/movies_clusters.csv')

st.header('RECOMMENDER v.3000')


col1, col2 = st.columns([3, 1])

user_movie_1 = col1.selectbox(
     'Which movie you would like to rate?',
     df['title'])

user_movie_2 = col1.selectbox(
     'Which movie you would like to rate?',
     df['title'],key = "<movie_2")


user_movie_3 = col1.selectbox(
     'Which movie you would like to rate?',
     df['title'],key = "<movie_3")


user_rate_1 = col2.selectbox(
     'Rate',
     (1,2,3,4,5))

user_rate_2 = col2.selectbox(
     'Rate',
     (1,2,3,4,5),key = "<rate_2")

user_rate_3 = col2.selectbox(
     'Rate',
     (1,2,3,4,5),key = "<rate_3")


user_rating = {
    user_movie_1: user_rate_1,
    user_movie_2: user_rate_2,
    user_movie_3: user_rate_3
    }

rec_list = recommend_with_NMF(user_rating, k=5)

if st.button('reset'):
    st.experimental_rerun()



cont_1 = st.container()
    
col11, col12, col13, col14, col15 = cont_1.columns(5)


if col13.button('show rec'):

    # rec_list = recommend_with_NMF(user_rating, k=5)

    cont_2 = st.container()

    col21, col22, col23, col24, col25 = cont_2.columns(5)

    cols = [col21, col22, col23, col24, col25]
    for i in range(len(rec_list)):
        cols[i].write(rec_list[i])




cont_3 = st.container()
    
col31, col32, col33, col34, col35 = cont_3.columns(5)



if col33.button('show similar'):
    cont_4 = st.container()

    col41, col42, col43, col44, col45 = cont_4.columns(5)

    cols2 = [col41, col42, col43, col44, col45]
    for i in range(len(cols2)):
        cols2[i].subheader(rec_list[i])
        recomendation = cluster_recomender(rec_list[i])
        # cols2[i].write(cluster_recomender(rec_list[0])[0])
        for j in range(5):
            cols2[i].write(cluster_recomender(rec_list[i])[j])

