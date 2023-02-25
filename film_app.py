import streamlit as st

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
 
operation_genre = st.radio("Select any you fancy:",
                    ("Horror", "Comedy", "Action"))

operation_genre = st.radio("Decade:",
                    ("1990s", "2000s", "2010s"))

operation_amount = st.radio("How many suggestions:",
                    ("1", "3", "all"))


def pick_film():
    return pick_film


if st.button("Suggest a film"):
    pick_film()