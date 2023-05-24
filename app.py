import streamlit as st
from key import get_bard_answer

# Streamlit app
def main():
    st.title("Bard API Demo")

    # Input question
    question = st.text_input("Enter your question")

    if question:
        # Get answer using the question and answer function
        content = get_bard_answer(question)

        # Display the answer
        st.markdown("### Answer:")
        st.write(content)


if __name__ == "__main__":
    main()
