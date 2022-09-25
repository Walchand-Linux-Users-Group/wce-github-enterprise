import streamlit
import requests
from streamlit_option_menu import option_menu
import ui.components.header
import ui.components.footer
import database.mongo
import backend.user
import api.github


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


def getDetails():

    cols = streamlit.columns(
        [
            1,
            1,
            1,
        ]
    )
    cols[1].header("Onboarding")
    githubUsername = cols[1].text_input("Github Username")
    isGuide = cols[1].checkbox("Are you Faculty/Project Guide?")

    if isGuide:
        depertment = cols[1].multiselect(
            "Select your department",
            ["Computer Science and Engineering", "Information Technology"],
        )
    else:
        depertment = cols[1].selectbox(
            "Select your department",
            ["Computer Science and Engineering", "Information Technology"],
        )

        batch = cols[1].selectbox(
            "Select Year of Passing",
            [2023, 2024],
        )

    submit = cols[1].button("Submit")

    if submit:
        id = api.github.checkUsername(githubUsername)

        if id == None:
            cols[1].warning("Invalid Github username", icon="⚠️")
        else:
            user = backend.user.getUser(githubId=id)
            if user == None:
                streamlit.session_state.data["githubId"] = id

                if isGuide:
                    if not backend.user.createGuide():
                        cols[1].warning("Something went wrong", icon="⚠️")
                    else:
                        streamlit.experimental_rerun()
                else:
                    if not backend.user.createUser():
                        cols[1].warning("Something went wrong", icon="⚠️")
                    else:
                        streamlit.experimental_rerun()
            else:
                cols[1].warning("Github username already registered", icon="⚠️")


def guideDashboard():
    setSlidebar()


def studentDashboard():
    setSlidebar()


def dashboard():
    ui.components.header.header()

    user = backend.user.getUser()

    if user == None:
        getDetails()
    else:
        if isinstance(user, database.models.Guide):
            if not user.verified:
                cols = streamlit.columns(3)
                cols[1].info(
                    "Contact administrator to verify your faculty account - github@wcewlug.org",
                    icon="ℹ️",
                )
                refresh = cols[1].button("Refresh")

                if refresh:
                    streamlit.experimental_rerun()
            else:
                guideDashboard()
        else:
            studentDashboard()

    ui.components.footer.footer()
