import streamlit as st

# Set page config for a cute title and icon
st.set_page_config(page_title="Calculator", page_icon="🧮")

# Custom CSS for a pink theme
st.markdown("""
<style>
.stButton>button {
    background-color: pink;
    color: white;
    border-radius: 10px;
    border: 2px solid hotpink;
    padding: 10px 24px;
}
.stTextInput>div>div>input {
    background-color: pink;
    color: white;
}
</style>
""", unsafe_allow_html=True)

# Calculator layout
st.title("Calculator 🧮")

# Input fields
num1 = st.number_input("Enter first number", value=0.0)
num2 = st.number_input("Enter second number", value=0.0)

# Operation selection
operation = st.radio("Choose operation", ["Add", "Subtract", "Multiply", "Divide"])

# Calculate result
if st.button("Calculate"):
    if operation == "Add":
        result = num1 + num2
    elif operation == "Subtract":
        result = num1 - num2
    elif operation == "Multiply":
        result = num1 * num2
    elif operation == "Divide":
        result = num1 / num2 if num2 != 0 else "Error: Division by zero"
    st.success(f"Result: {result}")
