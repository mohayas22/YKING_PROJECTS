
import streamlit as st
import pandas as pd
import pickle
import requests

st.set_page_config(
     page_title="yking projects",
     page_icon="🧊",
     layout="wide",
     initial_sidebar_state="expanded",
)


def fecth_poster(movie_id):
    url = 'https://api.themoviedb.org/3/movie/{}?api_key=b5c50fc69fb332bbc0b18c9f7ae16d83&language=en-US'.format(movie_id)
    data = requests.get(url)
    data = data .json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/"+ poster_path
    return full_path




def recommend(movie):
    movie_index = movies[movies['title']== movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)),reverse = True , key = lambda x:x[1])[1:7]
    
    recommended_movies= []
    recommended_movie_poster = []
    for i in movie_list:
        # fetch poster from API
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_poster.append(fecth_poster(movie_id))   
        recommended_movies.append( movies.iloc[i[0]].title)
         
        
    return recommended_movies,recommended_movie_poster
 


st.title('MOVIE RECOMMENDATION SYSTEM  - by Yking')

movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = movies_dict = pickle.load(open('similatrity.pkl', 'rb'))

selected_movie_name = st.selectbox(
     'Please select a movie from below.',
     (movies['title'].values))

st.write('You selected:', selected_movie_name)




if st.button('Recommend Movies'):
    names, poster = recommend(selected_movie_name)
    col1, col2, col3 , col4 , col5,col6 = st.columns(6)

    with col1:
        st.text(names[0])
        st.image(poster[0])

    with col2:
        st.text(names[1])
        st.image(poster[1])
    with col3:
        st.text(names[2])
        st.image(poster[2])
    with col4:
        st.text(names[3])
        st.image(poster[3])
    with col5:
        st.text(names[4])
        st.image(poster[4]) 
    with col6:
        st.text(names[5])
        st.image(poster[5]) 
    