import streamlit as st
from st_paywall import add_auth

st.set_page_config(layout="wide")
st.title("The Most Fantabulous SaaS Ever! 🚀")

add_auth(required=True)

# ONLY AFTER THE AUTHENTICATION, THE USER WILL SEE THIS ⤵
# The email and subscription status is stored in session state.
st.write(f"Subscription Status: {st.session_state.user_subscribed}")
st.write("🎉 Yay! You're all set and subscribed! 🎉")
st.write(f'By the way, your email is {st.session_state.email}... Safe with us! 🤫')