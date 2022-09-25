import streamlit
from mongoengine import *
import database.models


def createUser():
    try:
        newUser = database.models.User(
            fullname=streamlit.session_state.data["fullname"],
            username=streamlit.session_state.data["username"],
            moodleId=streamlit.session_state.data["moodleId"],
            githubId=streamlit.session_state.data["githubId"],
        )

        newUser.save()
        return True
    except Exception as e:
        return False


def createGuide():
    try:
        newGuide = database.models.Guide(
            fullname=streamlit.session_state.data["fullname"],
            username=streamlit.session_state.data["username"],
            moodleId=streamlit.session_state.data["moodleId"],
            githubId=streamlit.session_state.data["githubId"],
        )

        newGuide.save()
        return True
    except Exception as e:
        return False


def getUser(moodleId=None, githubId=None):

    if moodleId != None:
        return database.models.User.objects(moodleId=moodleId).first()
    elif githubId != None:
        return database.models.User.objects(githubId=githubId).first()

    return database.models.User.objects(
        moodleId=streamlit.session_state.data["moodleId"]
    ).first()
