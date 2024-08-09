import streamlit as st

# Title of the app
st.title("Simple Calculator")
st.subheader("Created by Engr. Adnan Munir")
# Input fields for the two numbers
num1 = st.number_input("Enter the first number:", step=1.0)
num2 = st.number_input("Enter the second number:", step=1.0)

# Dropdown to select the operation
operation = st.selectbox("Select Operation:", ["Add", "Subtract", "Multiply", "Divide"])

# Perform the calculation
if st.button("Calculate"):
    if operation == "Add":
        result = num1 + num2
        st.write(f"The result of {num1} + {num2} is {result}")
    elif operation == "Subtract":
        result = num1 - num2
        st.write(f"The result of {num1} - {num2} is {result}")
    elif operation == "Multiply":
        result = num1 * num2
        st.write(f"The result of {num1} * {num2} is {result}")
    elif operation == "Divide":
        if num2 != 0:
            result = num1 / num2
            st.write(f"The result of {num1} / {num2} is {result}")
        else:
            st.write("Error: Division by zero is not allowed.")
