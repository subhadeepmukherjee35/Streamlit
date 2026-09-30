import streamlit as st

st.title("My First Website using Text Input !!")

my_name = st.text_input("Enter your Name :")


if st.button("Submit"):
	st.success(f"Welcome {my_name}")




