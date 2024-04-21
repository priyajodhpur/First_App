import streamlit as st
st.balloons()
st.title("Hello , This Is My first App")
st.write("let us create app")
st.text_input("Please Enter your Name")
x=st.number_input("Are you Working",options=["Yes","No"])
if x=="Yes":
    st.write("You can choose Weekend Batch")
else:
     St.write("You can choose weekdays Batch")
st.sidebar.markdown("Test Results")


