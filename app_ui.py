import streamlit as st
import pickle

# load model correctly
model = pickle.load(open("model.pkl", "rb"))

# UI title
st.title("Salary Prediction 💼")

# input field
exp = st.number_input("Enter Experience", min_value=0, max_value=50, value=1)

# button action
if st.button("Predict"):
    result = model.predict([[exp]])   # 2D input

    st.write(f"Predicted Salary: ₹ {int(result[0])}")
