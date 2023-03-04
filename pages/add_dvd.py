import streamlit as st
import pandas as pd
from git import Repo

st.markdown("# Add a DVD")
st.sidebar.markdown("# Add a DVD")


st.write("Add a DVD to database")
st.write("---")



new_entry = {}
new_entry["Title"] = st.text_input("Title: ")

new_entry["Type"] = st.radio("Film or TV series?",
                          ("Film", "Television"))

new_entry["Genre"] = st.selectbox("Genre:",
                               ("Comedy", "Family", "Horror", "Sci-Fi", "Western"))

new_entry["Decade"] = st.selectbox("Decade:",
                             ("2020s", "2010s", "2000s" "1990s", "1980s", "1970s", "1960s", "1950s", "1940s", "1930s", "Not sure"))

def add_dvd():
    url = "https://raw.githubusercontent.com/JenB-DS/filmapp/main/dvd_collection.csv"
    df = pd.read_csv(url)
    df = df.append(new_entry, ignore_index=True)
    df.to_csv('dvd_collection.csv', index=False)
    repo = Repo('C:\Users\burto\OneDrive\Documents\2_Personal\Projects\Films\streamlit_film')
    repo.git.add('dvd_collection.csv')
    repo.git.commit('-m', 'Update data.csv')
    repo.git.push()
    st.success("DVD added")


if st.button("Add DVD"):
    add_dvd()

