import streamlit as st

# Backend storage (you can replace this with a database)
votes = {'option1': 0, 'option2': 0, 'option3': 0, 'option4': 0}

# Streamlit app
def main():
    st.title('Voting App')
    
    # Display voting options and buttons
    st.subheader('Vote for your favorite option:')
    for option in votes.keys():
        if st.button(option):
            votes[option] += 1

    # Calculate the winner
    winner = max(votes, key=votes.get)

    # Display the winner
    st.subheader(f'The current winner is: {winner}')

if __name__ == '__main__':
    main()
