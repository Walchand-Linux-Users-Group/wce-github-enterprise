import streamlit
import requests
import ui.components.header
import ui.components.footer
import api.moodle


def login():
    ui.components.header.header()

    cols = streamlit.columns([1, 1, 1])
    cols[1].header("Authentication")
    username = cols[1].text_input("Username")
    password = cols[1].text_input("Password", type="password")
    loginBtn = cols[1].button("Log In")

    if loginBtn:
        res = api.moodle.auth(username, password)

        if res == requests.exceptions.Timeout:
            cols[1].warning("Server is not reachable", icon="⚠️")
        elif res is Exception:
            cols[1].warning(res, icon="⚠️")

        try:
            return res
        except Exception as e:
            cols[1].warning("Invalid Credentials", icon="⚠️")

    ui.components.footer.footer()
