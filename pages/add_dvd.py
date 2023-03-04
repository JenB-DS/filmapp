import streamlit as st

st.markdown("# Add a DVD")
st.sidebar.markdown("# Add a DVD")


st.write("Add a DVD to database")
st.write("---")

dvd_name = st.text_input("Title: ")

operation_type = st.radio("Film or TV series?",
                          ("Film", "Television"))

operation_genre = st.selectbox("Select the genre you fancy:",
                               ("Any", "Comedy", "Family", "Horror", "Sci-Fi", "Western"))

operation_dec = st.selectbox("Decade:",
                             ("Any", "1930s", "1940s", "1950s", "1960s", "1970s",
                             "1980s", "1990s", "2000s", "2010s", "2020s"))