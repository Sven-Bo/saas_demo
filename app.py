import streamlit as st
from st_paywall import add_auth

st.title("This is an awesome SaaS")
st.subheader("Login it first to use it! 🤩")

add_auth(required=True)

#after authentication, the email and subscription status is stored in session state
st.write(st.session_state.email)
st.write(st.session_state.user_subscribed)