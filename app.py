import streamlit as st

st.title("Simple Calculator")

num1 = st.number_input("Enter first number")
num2 = st.number_input("Enter second number")

operation = st.selectbox(
    "Choose operation",
    ["Addition", "Subtraction"]
)

if st.button("Calculate"):

    if operation == "Addition":
        result = num1 + num2

    elif operation == "Subtraction":
        result = num1 - num2


    st.success(f"Result: {result}")