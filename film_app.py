import streamlit as st
import csv

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
    with open('https://raw.githubusercontent.com/JenB-DS/filmapp/main/dvd_collection.csv') as csvfile:

        csv_reader = csv.reader(csvfile)
        film_list = []
        for row in csv_reader:
            if row[1] == operation_type:
                film_list.append(row[0])

    st.success(f"Here we go... {film_list}")


if st.button("Suggest something to watch"):
    pick_film()
