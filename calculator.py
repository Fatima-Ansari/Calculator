import streamlit as st

# Title of the app
st.title("Simple Calculator")

# Create input fields for numbers
num1 = st.number_input("Enter first number:")
num2 = st.number_input("Enter second number:")

# Create a dropdown for selecting the operation
operation = st.selectbox("Choose an operation:", ["Add", "Subtract", "Multiply", "Divide"])

# Create a button to perform the calculation
if st.button("Calculate"):
    if operation == "Add":
        result = num1 + num2
    elif operation == "Subtract":
        result = num1 - num2
    elif operation == "Multiply":
        result = num1 * num2
    elif operation == "Divide":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Cannot divide by zero"
    
    # Display the result
    st.write(f"The result is: {result}")



  
