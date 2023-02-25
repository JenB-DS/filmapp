import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="What shall we watch tonight?",
    page_icon=":vampire:"
)

st.title("What shall we watch tonight?")
st.write("You can have any genre, as long as it's horror...")
st.write("---")

st.write("What are you in the mood for?")


operation_type = st.radio("Film or TV?", 
                          ("Film", "TV"))
 
operation_genre = st.selectbox("Select the genre you fancy:",
                    ("Any", "Horror", "Comedy", "Action"))

operation_genre = st.selectbox("Decade:",
                    ("Any", "1990s", "2000s", "2010s"))

operation_amount = st.radio("How many suggestions:",
                    ("1", "3", "all"))


def pick_film():
    url = 'https://github.com/JenB-DS/filmapp/blob/06314ceab28256f408d40f2ebd027de6d0607020/dvd_collection.csv?raw=true'
    dvds = pd.read_csv(url,index_col=0)
    film_list = []
    for film in dvds:
        if operation_type == dvds("Type"):
            pick_film.append[film]
    return film_list


if st.button("Suggest something to watch"):
    pick_film()

