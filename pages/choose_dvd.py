import streamlit as st

# Backend storage (you can replace this with a database)
votes = {'option1': 0, 'option2': 0, 'option3': 0, 'option4': 0}
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
