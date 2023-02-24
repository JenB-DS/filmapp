import streamlit as st

st.set_page_config(
    page_title="What shall we watch tonight?",
    page_icon=":vampire:"
)

st.title("What shall we watch tonight?")
st.write("You can have any genre, as long as it's horror...")
st.write("---")

st.write("What are you in the mood for?")
 
operation = st.radio("Select any you fancy:",
                    ("Slasher", "Comedy",))

operation1 = st.radio("Era:",
                    ("90s", "70s"))


def pick_film():
    return pick_film


if st.button("Suggest a film"):
    pick_film()