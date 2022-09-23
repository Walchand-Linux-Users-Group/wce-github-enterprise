import ui.login
import ui.dashboard
import api.moodle
import streamlit
import os
from dotenv import load_dotenv

load_dotenv()

WCE_LOGO_PATH = os.getenv("WCE_LOGO_PATH")

streamlit.set_page_config(
    page_title="WCE Project Management",
    page_icon=WCE_LOGO_PATH,
    layout="wide",
    initial_sidebar_state="expanded",
)

if "token" not in streamlit.session_state:
    streamlit.session_state.token = ""
    streamlit.session_state.verified = False
    streamlit.session_state.data = {}

if not api.moodle.isValid(streamlit.session_state.token):
    streamlit.session_state.data = ui.login.login()

    try:
        streamlit.session_state.token = streamlit.session_state.data["token"]
        streamlit.session_state.verified = True
    except Exception as e:
        streamlit.session_state.token = ""
        streamlit.session_state.verified = False

    if streamlit.session_state.verified == True:
        streamlit.experimental_rerun()

else:
    ui.dashboard.dashboard()

    if streamlit.session_state.verified == False:
        streamlit.experimental_rerun()
