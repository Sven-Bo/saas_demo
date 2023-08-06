import streamlit as st
from st_paywall import add_auth

st.set_page_config(layout="wide")
st.title("The Most Fantabulous SaaS Ever! 🚀")

is_authenticated = add_auth(required=True)
st.write(is_authenticated)

# After authentication, the email and subscription status is stored in session state.
if st.session_state.user_subscribed:
    st.write("🎉 Yay! You're all set and subscribed! 🎉")
    st.write(f'By the way, your email is {st.session_state.email}... Safe with us! 🤫')
else:
    st.write("Hey there! 👋 You're logged in, but the real magic awaits... ✨")
    st.write("Subscribe now to dive into the full experience! 🌟")

