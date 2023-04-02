# streamlit_app.py

import streamlit as st
import mysql.connector


# Initialize connection.
# Uses st.cache_resource to only run once.
@st.cache_resource
def init_connection():
    return mysql.connector.connect(**st.secrets["mysql"])

conn = init_connection()

# Perform query.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
@st.cache_data(ttl=600)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()


def demo_app():
    st.title('ChatGPT + StableAI')

    prompt = st.text_area('Prompt for ChatGPT', placeholder='Write a code for simple web page')

    if prompt:

        st.write('Prompt')
        st.write(prompt)

        rows = run_query("SELECT * from application_for_calculating_the_vore;")

        # Print results.
        for row in rows:
            st.write(f"{row[0]} has a :{row[1]}:")


if __name__ == '__main__':
    # call main function
    demo_app()