import streamlit as st
import csv




st.markdown("# This page is under construction")
st.sidebar.markdown("# Add a DVD")


st.write("Attempts to add a DVD, will just be shouting into the void")
st.write("---")


Title = st.text_input("Title: ")

Type = st.radio("Film or TV series?",
                          ("Film", "Television"), index=-1)

Genre = st.selectbox("Genre:",
                               ("Comedy", "Family", "Horror", "Sci-Fi", "Western"), index=-1)

Decade = st.selectbox("Decade:",
                             ("2020s", "2010s", "2000s" "1990s", "1980s", "1970s", "1960s", "1950s", "1940s", "1930s", "Not sure"), index=-1)

if st.button('Add DVD'):
    # Write the user-submitted data to a CSV file
    with open('newdvd.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([Title, Type, Genre, Decade])
    st.success('DVD added')
