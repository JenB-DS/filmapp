import streamlit as st
import random
import requests
import io
import csv

url = "https://raw.githubusercontent.com/JenB-DS/filmapp/main/dvd_collection.csv"
response = requests.get(url)
csv_data = response.content.decode("utf-8")
csv_file = io.StringIO(csv_data)

reader = csv.reader(csv_file)
film_list = []


for row in reader:
    if row[1] == "Film" and row[2] == "Horror":
        film_list.append(row[0])

nums = []
while len(nums) < 3:
    n = random.randint(0, len(film_list) - 1)
    if n not in nums:
        nums.append(n)
    else:
        # Replace duplicate with a new random number
        n = random.randint(0, len(film_list) - 1)

shortlist = [film_list[nums[0]], film_list[nums[1]], film_list[nums[2]]]

# Backend storage (you can replace this with a database)
votes = {shortlist[0]: 0, shortlist[1]: 0, shortlist[2]: 0}
total_votes = 0

# Streamlit app
def main():
    global total_votes
    st.title('Voting App')
    
    # Display voting options and buttons
    st.subheader('Vote for your favorite option:')
    for option in votes.keys():
        if st.button(option):
            votes[option] += 1
            total_votes += 1

    # Show the winner when there are four votes
    if total_votes == 4:
        winner = max(votes, key=votes.get)
        st.subheader(f'The winner is: {winner}')

if __name__ == '__main__':
    main()
