import streamlit as st
import requests
import io
import csv
import random

st.set_page_config(
    page_title="What shall we watch tonight?",
    page_icon=":vampire:"
)

st.title("What shall we watch tonight?")
st.write("You can have any genre, as long as it's horror...")
st.write("---")

st.write("What are you in the mood for?")


operation_type = st.radio("Film or TV series?",
                          ("Film", "Television"))

operation_genre = st.selectbox("Select the genre you fancy:",
                               ("Any", "Comedy", "Family", "Horror", "Sci-Fi", "Western"))

operation_dec = st.selectbox("Decade:",
                             ("Any", "1930s", "1940s", "1950s", "1960s", "1970s",
                             "1980s", "1990s", "2000s", "2010s", "2020s"))

operation_amount = st.radio("How many suggestions:",
                            ("1", "3", "all"))

url = #"https://raw.githubusercontent.com/JenB-DS/filmapp/main/dvd_collection.csv"
response = requests.get(url)
csv_data = response.content.decode("utf-8")
csv_file = io.StringIO(csv_data)


def pick_film():
    reader = csv.reader(csv_file)
    film_list = []

    try:
        for row in reader:

            if operation_genre == "Any" and operation_dec == "Any":
                if row[1] == operation_type:
                    film_list.append(row[0] + " (" + row[3] + ")")

            elif operation_dec == "Any":
                if row[1] == operation_type and row[2] == operation_genre:
                    film_list.append(row[0] + " (" + row[3] + ")")

            elif operation_genre == "Any":
                if row[1] == operation_type and row[3] == operation_dec:
                    film_list.append(row[0])

            elif row[1] == operation_type and row[2] == operation_genre and row[3] == operation_dec:
                film_list.append(row[0])


        if operation_amount == "all":
            st.success("Here we go...")
            for each in film_list:
                st.write("• " + each)


        elif operation_amount == "1":
            random_index = random.randint(0, len(film_list) - 1)
            st.success(f"Here we go... {film_list[random_index]}")

        elif operation_amount == "3":

            nums = []
            while len(nums) < 3:
                n = random.randint(0, len(film_list) - 1)
                if n not in nums:
                    nums.append(n)
            else:
                # Replace duplicate with a new random number
                n = random.randint(0, len(film_list) - 1)

            shortlist = [film_list[nums[0]], film_list[nums[1]], film_list[nums[2]]]

            st.success("Here's a shortlist...")
            for each in shortlist:
                st.write("• " + each)

    except ValueError:
        st.error("Surprisingly, you don’t own a DVD that matches this criteria!")
        st.error("Please try to resist buying a new DVD, and try the search again.")


if st.button("Suggest something to watch"):
    pick_film()
