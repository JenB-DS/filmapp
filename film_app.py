import streamlit as st

st.set_page_config(
    page_title="What shall we watch tonight?",
    page_icon="🧛"
)

st.title("What shall we watch tonight?")
st.write("Pick some specifics and I'll suggest a film")
st.write("---")

st.write("What are you in the mood for?")
 
operation = st.radio("Select any you fancy:",
                    ("90s", "Slasher", "Comedy", "70s"))


def pick_film():
    return pick_film


if st.button("Suggest a film"):
    pick_film()