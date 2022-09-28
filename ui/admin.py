import streamlit
from streamlit_option_menu import option_menu
import database.models
import backend.department
import api.github


def manageDepartments():
    streamlit.session_state.department_option = option_menu(
        "",
        ["View", "Add"],
        icons=["book", "plus"],
        default_index=0,
        orientation="horizontal",
    )

    if streamlit.session_state.department_option == "View":
        for department in database.models.Department.objects:
            dept = api.github.getDepartment(department.orgName)

            streamlit.header(dept["name"])
            streamlit.write(dept["description"])

    elif streamlit.session_state.department_option == "Add":
        cols = streamlit.columns(3)

        cols[1].header("Add Department")
        name = cols[1].text_input(
            "Name of Department",
            help="Found in org main page URL and wce-github-enterprise should have admin access.",
        )

        add = cols[1].button("Add")

        if add:
            orgId = api.github.checkOrg(name)

            if orgId == None:
                cols[1].warning("Invalid organisation", icon="⚠️")
            else:

                error = backend.department.createDepartment(name, orgId)

                if error:
                    cols[1].warning(
                        "Check organisation name or organisation is already added!",
                        icon="⚠️",
                    )
                else:
                    cols[1].success("Organisation added successfully!", icon="✔️")
                    streamlit.session_state.department_option = "View"


def manageBatches():
    pass


def manageGuides():
    pass


def manageTeams():
    pass


def manageStudents():
    pass


def adminSidebar():
    with streamlit.sidebar:
        streamlit.markdown(
            """<h1>Welcome,</h1>
        <h3>{}</h3>""".format(
                "Admin"
            ),
            unsafe_allow_html=True,
        )

        streamlit.sidebar.markdown("<hr />", unsafe_allow_html=True)
        streamlit.session_state.main_option = option_menu(
            "Manage",
            ["Departments", "Batches", "Guides", "Teams", "Students"],
            icons=["gear", "gear", "gear", "gear", "gear"],
            default_index=0,
        )


def adminDashboard():
    streamlit.session_state.main_option = "Departments"
    adminSidebar()

    if streamlit.session_state.main_option == "Departments":
        manageDepartments()
    elif streamlit.session_state.main_option == "Batches":
        manageBatches()
    elif streamlit.session_state.main_option == "Guides":
        manageGuides()
    elif streamlit.session_state.main_option == "Teams":
        manageTeams()
    elif streamlit.session_state.main_option == "Students":
        manageStudents()
