import streamlit as st
import pandas as pd
import csv




st.markdown("# Add a DVD")
st.sidebar.markdown("# Add a DVD")


st.write("Add a DVD to database")
st.write("---")


Title = st.text_input("Title: ")

Type = st.radio("Film or TV series?",
                          ("Film", "Television"))

Genre = st.selectbox("Genre:",
                               ("Comedy", "Family", "Horror", "Sci-Fi", "Western"))

Decade = st.selectbox("Decade:",
                             ("2020s", "2010s", "2000s" "1990s", "1980s", "1970s", "1960s", "1950s", "1940s", "1930s", "Not sure"))

if st.button('Add DVD'):
    # Write the user-submitted data to a CSV file
    with open('newdvd.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([Title, Type, Genre, Decade])
    st.success('DVD added')
