import streamlit as st

st.title("Simple Calculator")

num1 = st.number_input("Enter first number")
num2 = st.number_input("Enter second number")

operation = st.selectbox(
    "Choose operation",
    ["Addition", "Subtraction","Multiplication","Division", "Floor Division"]
)

if st.button("Calculate"):

    if operation == "Addition":
        result = num1 + num2

    elif operation == "Subtraction":
        result = num1 - num2

    elif operation == 'Multiplication':
        result = num1 * num2

    elif operation == "Floor Division":
        result = num1 // num2

    # will throw an error if num2 is 0, so we need to handle that case
    elif operation == "Division":
        if num2 == 0:
            st.error("Error: Division by zero is not allowed.")
        else:
            result = num1/num2


    st.success(f"Result: {result}")