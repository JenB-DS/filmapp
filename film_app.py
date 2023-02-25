import streamlit as st
import requests
import io
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

operation_dec = st.selectbox("Decade:",
                    ("Any", "1990s", "2000s", "2010s"))

operation_amount = st.radio("How many suggestions:",
                    ("1", "3", "all"))

url = 'https://raw.githubusercontent.com/JenB-DS/filmapp/main/dvd_collection.csv'
response = requests.get(url)
csv_data = response.content.decode("utf-8")
csv_file = io.StringIO(csv_data)

def pick_film():
    reader = csv.reader(csv_file)
    film_list = []
    for row in reader:
        if row[1] == operation_type and row[2] == operation_genre and row[3] == operation_dec:
            film_list.append(row[0])

    st.success(f"Here we go... {film_list}")


if st.button("Suggest something to watch"):
    pick_film()
