import streamlit
import requests
from streamlit_option_menu import option_menu
import ui.components.header
import ui.components.footer


def setSlidebar():

    with streamlit.sidebar:
        streamlit.markdown(
            """<h1>Welcome,</h1>
        <h3>{}</h3>""".format(
                streamlit.session_state.data["fullname"]
            ),
            unsafe_allow_html=True,
        )

        streamlit.sidebar.markdown("<hr />", unsafe_allow_html=True)
        main_option = option_menu(
            "",
            [
                "Projects",
                "Connect",
                "Policy",
            ],
            icons=["house", "person", "gear", "book"],
            default_index=0,
        )

        if main_option == "Services":
            selected = option_menu(
                "",
                ["Compute", "Keypair"],
                icons=["laptop", "key"],
                orientation="horizontal",
                default_index=0,
            )
        elif main_option == "Public API":
            selected = option_menu(
                "",
                ["Compute", "User"],
                icons=["laptop", "person"],
                orientation="horizontal",
                default_index=0,
            )
        elif main_option == "Premium":
            selected = option_menu(
                "",
                ["Features", "Get Premium"],
                icons=["pin", "star"],
                orientation="horizontal",
                default_index=0,
            )
        elif main_option == "Developers":
            selected = option_menu(
                "",
                ["Students", "Faculty"],
                icons=["person", "person"],
                orientation="horizontal",
                default_index=0,
            )


def dashboard():
    ui.components.header.header()

    setSlidebar()

    ui.components.footer.footer()
