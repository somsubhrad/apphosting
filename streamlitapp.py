import streamlit as st

def largest_num(x, y, z):
    largest = x
    if y > largest:
        largest = y
    if z > largest:
        largest = z
    return largest

st.title("App for finding the largest among three given numbers - by Somsubhra")

x = st.number_input("Enter the first number: ")
y = st.number_input("Enter the second number: ")
z = st.number_input("Enter the third number: ")

if st.button("Compute the largest number"):
    result = largest_num(x, y, z)
    st.write("The largest number among the three provided inputs is:", result)
