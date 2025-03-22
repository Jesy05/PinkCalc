import streamlit as st

# Set page config para el titulo decorado 
st.set_page_config(page_title="Calculadora<3", page_icon="🧮")

# Custom CSS (definir y cohesionar la presentación) for a pink theme
st.markdown("""
<style>
.stButton>button {
    background-color: pink;
    color: white;
    border-radius: 10px;
    border: 2px solid hotpink;
    padding: 10px 24px;
    font-size: 18px;
    width: 100%;
}
.stTextInput>div>div>input {
    background-color: pink;
    color: white;
    border-radius: 10px;
    border: 2px solid hotpink;
    padding: 10px;
}
</style>
""", unsafe_allow_html=True)

# Calculator layout
st.title("Calculator 🧮")

# Initializa sesion para almacenar el current input
if 'calc_input' not in st.session_state:
    st.session_state.calc_input = "0"

# Function to validate input (only allow numbers, operators, and decimal points)
def validate_input(input_str):
    valid_chars = set("0123456789.+-×÷−＋")
    return "".join([char for char in input_str if char in valid_chars])

# Input field for display (now editable)
input_value = st.text_input("", value=st.session_state.calc_input, key="input")

# Validate and update the input value
if input_value != st.session_state.calc_input:
    st.session_state.calc_input = validate_input(input_value)

# Create buttons for the calculator
buttons = [
    '7', '8', '9', '÷',
    '4', '5', '6', '×',
    '1', '2', '3', '−',
    '0', '.', 'C', '＋'
]

# Add a backspace button
buttons.append('⌫')  # Unicode for backspace symbol

# Use columns to create a grid layout
col1, col2, col3, col4 = st.columns(4)

# Function to update the input value
def update_input(value):
    if st.session_state.calc_input == "0":
        st.session_state.calc_input = value
    else:
        st.session_state.calc_input += value

# Function to clear all the input
def clear_input():
    st.session_state.calc_input = "0"

# Function to delete the last character
def backspace():
    if len(st.session_state.calc_input) > 1:
        st.session_state.calc_input = st.session_state.calc_input[:-1]
    else:
        st.session_state.calc_input = "0"

# Function to calculate the result
def calculate_result():
    try:
        # Replace Unicode symbols with standard operators before evaluation
        expression = (
            st.session_state.calc_input
            .replace('÷', '/')
            .replace('×', '*')
            .replace('−', '-')
            .replace('＋', '+')
        )
        st.session_state.calc_input = str(eval(expression))
    except:
        st.session_state.calc_input = "Error"

# Display buttons in a grid
for i, button in enumerate(buttons):
    if i % 4 == 0:
        col = col1
    elif i % 4 == 1:
        col = col2
    elif i % 4 == 2:
        col = col3
    else:
        col = col4

    if button == 'C':
        col.button(button, on_click=clear_input)
    elif button == '⌫':
        col.button(button, on_click=backspace)
    else:
        col.button(button, on_click=update_input, args=(button,))

# Calculate button
if st.button("Calculate", key="calculate"):
    calculate_result()

# Display the result
st.success(f"Result: {st.session_state.calc_input}")
