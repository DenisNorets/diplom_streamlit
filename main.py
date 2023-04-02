import streamlit as st


def demo_app():
    st.title('ChatGPT + StableAI')

    prompt = st.text_area('Prompt for ChatGPT', placeholder='Write a code for simple web page')

    if prompt:

        st.write('Prompt for generating images:')
        st.write(prompt)


if __name__ == '__main__':
    # call main function
    demo_app()
