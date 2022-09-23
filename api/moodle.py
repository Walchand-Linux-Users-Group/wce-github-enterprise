import requests
import streamlit
import os


def isValid(token):
    try:
        res = requests.get(
            os.getenv("MOODLE_SIGNIN"),
            params={
                "wsfunction": "core_webservice_get_site_info",
                "moodlewsrestformat": "json",
                "wstoken": token,
            },
        )

        jsonObj = res.json()

        if jsonObj["fullname"] != "" and jsonObj["username"] != "":
            streamlit.write("Verified Token")
            return True
        else:
            return False

    except Exception as e:
        return False


def getInfo(token):

    try:
        res = requests.get(
            os.getenv("MOODLE_SIGNIN"),
            params={
                "wsfunction": "core_webservice_get_site_info",
                "moodlewsrestformat": "json",
                "wstoken": token,
            },
        )

        jsonObj = res.json()

        return {
            "fullname": jsonObj["fullname"],
            "username": jsonObj["username"],
            "token": token,
        }

    except Exception as e:
        return e


def auth(username, password):
    try:
        username = username.upper()
        res = requests.get(
            os.getenv("MOODLE_TOKEN"),
            params={
                "username": username,
                "password": password,
                "service": "moodle_mobile_app",
            },
        )

        token = res.json()["token"]

        return getInfo(token)

    except Exception as e:
        return e
