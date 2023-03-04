import streamlit as st
import pandas as pd





st.markdown("# Add a DVD")
st.sidebar.markdown("# Add a DVD")


st.write("Add a DVD to database")
st.write("---")



new_entry = {}
new_entry["Title"] = st.text_input("Title: ")

new_entry["Type"] = st.radio("Film or TV series?",
                          ("Film", "Television"), value=False)

new_entry["Genre"] = st.selectbox("Genre:",
                               ("Comedy", "Family", "Horror", "Sci-Fi", "Western"), value=False)

new_entry["Decade"] = st.selectbox("Decade:",
                             ("2020s", "2010s", "2000s" "1990s", "1980s", "1970s", "1960s", "1950s", "1940s", "1930s", "Not sure"), value=False)

def add_dvd():

    st.success("DVD added")


if st.button("Add DVD"):
    add_dvd()

