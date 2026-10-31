
import streamlit as st
from sql_executor import get_table_data, execute_query
from ai_engine import generate_sql
from database import create_database

create_database()

st.set_page_config(
    page_title="AI-Powered SQL Assistant",
    page_icon="🤖",
    layout="wide"
)

# Header
st.title("🤖 AI-Powered SQL Assistant")
st.caption("Convert simple English questions into SQL queries and explore your database.")

st.divider()

# Suggested questions
st.subheader("💡 Try These Questions")

suggested_questions = [
    "Show all students",
    "Show students from Nashik",
    "Show students with marks above 80",
    "Show students with marks below 75",
    "Show highest marks",
    "Show average marks",
    "Count students"
]

selected_question = st.selectbox(
    "Choose a sample question:",
    ["Select a question"] + suggested_questions
)

# Question input
st.subheader("💬 Ask Your Database")

question = st.text_input(
    "Enter your question in English:",
    value="" if selected_question == "Select a question" else selected_question,
    placeholder="Example: Show students from Nashik"
)

if st.button("🚀 Generate SQL and Run", type="primary"):
    if question.strip():
        try:
            sql_query = generate_sql(question)

            if sql_query is None:
                st.warning("Sorry! I couldn't understand your question. Try a suggested question.")
            else:
                st.success("SQL query generated successfully!")

                st.subheader("Generated SQL")
                st.code(sql_query, language="sql")

                result = execute_query(sql_query)

                st.subheader("📊 Query Results")
                st.metric("Total rows returned", len(result))
                st.dataframe(result, use_container_width=True)

        except Exception as e:
            st.error(f"Something went wrong: {e}")
    else:
        st.warning("Please enter a question.")

st.divider()

# Complete database
st.subheader("📚 Explore Student Database")

if st.button("View All Students"):
    try:
        data = get_table_data()
        st.dataframe(data, use_container_width=True)
        st.success(f"Successfully loaded {len(data)} student records.")
    except Exception as e:
        st.error(f"Database error: {e}")

st.divider()

# Footer
st.caption("Built using Python, Streamlit, SQLite and Natural Language Processing.")
