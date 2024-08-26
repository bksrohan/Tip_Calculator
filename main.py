import streamlit as st


st.title("Welcome to the Tip Calculator")

total_bill = st.number_input("What was your total bill?")
tip_percentage = int(st.number_input("How much tip would you like to give? "))
people_amount = int(st.number_input("How many people to split the bill? "))

final_tip_amount = (tip_percentage / 100 * total_bill + total_bill)

total_amount = (round(final_tip_amount / people_amount, 2))

st.write(f"Each person should pay: ${total_amount}")