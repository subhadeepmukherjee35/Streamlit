import streamlit as st

st.title("Salary Prediction")

experience = st.number_input("Enter Year of Experience")

experience = experience * 10000


if st.button('Predict'):
	st.write("Predicted Salary:", experience)