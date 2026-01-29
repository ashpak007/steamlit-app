import streamlit as st # Importing streamlit library

# Title of the web app
st.write("Yayy.....my first streamlit app.")

# header
st.header("Header")

# sub-header
st.subheader("Sub-header")

# checkbox
# Check if the checkbox is checked
# text display if the checkbox is clicked
if st.checkbox('Show/Hide'):
    #Display the text if clicked the checkbox
    st.text('Showing the widget')

#Radio Button
# First argument : Title of button
# Second argument : Options of the button
status = st.radio("Select the Gender: ", ('Male','Female','Trans'))

# Conditional statement to print
# Show the result using success function
if status == "Male":
    st.success('Male')
elif status == "Female":
    st.success('Female')    
else:
    st.success('Female')    

# Create a button, that when clicked, shows text
if (st.button('Click Me')):
    st.text('Button Clicked')    


def sqr(num):
    return num*num


num = st.number_input('Enter a Number: ')

if (st.button("Calculate Squre")):
    result = sqr(num)
    st.write("Squre of the Number is ",result)