import streamlit as st
import re

st.set_page_config(page_title="Password-Strength App", page_icon="🔐", layout="centered")

st.title("🔐 Password Strength Checker")

name = st.text_input("What is Your Name?")
if name:
    st.success(f"Great to have you here, {name}! 😊")

password = st.text_input("Enter your password", type="password")

if st.button("Check Strength"):
    library = []
    score = 0
    password = password.strip()

    if len(password) >= 8:
        score += 1
    else:
        library.append("❌ Your password has less than 8 characters")

    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        library.append("❌ Your password must contain both lowercase and uppercase letters")

    if re.search(r'\d', password):
        score += 1
    else:
        library.append("❌ Your password should include at least one digit")

    if re.search(r'[!@#$%^&*]', password):  
        score += 1
    else:
        library.append("❌ Your password should include at least one special character.(!@#$%^&*)")

    st.progress(score / 4)

    if score == 4:
        st.success("✅ Your password is strong!")
    elif score == 3:
        st.warning("⚠️ Your password is good, but you can make it stronger")
    else:
        st.error("❌ Your password is weak. Please improve it.")

    if library:
        st.header("🔹 Improvement Suggestions")
        for tip in library:
            st.write(tip)
else:
    st.warning("🔒 Enter a unique and secure password!")

