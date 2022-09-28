import os
import requests
import streamlit

headers = {
    "Accept": "application/vnd.github+json",
    "Authorization": "Bearer {}".format(os.getenv("GITHUB_TOKEN")),
}


def checkOrg(orgName):
    res = requests.get(
        "https://api.github.com/orgs/{}/memberships/{}".format(
            orgName, "wce-github-enterprise"
        ),
        headers=headers,
    )

    res = res.json()

    try:
        if res["role"] == "admin":
            return res["organization"]["id"]

        return None
    except Exception as e:
        return None


def getDepartment(orgName):
    res = requests.get(
        "https://api.github.com/orgs/{}".format(orgName),
        headers=headers,
    )

    res = res.json()

    try:
        return res
    except Exception as e:
        return None


def checkUsername(githubUsername):
    res = requests.get(
        "https://api.github.com/users/{}".format(githubUsername), headers=headers
    )

    res = res.json()

    try:
        id = res["id"]
        return id
    except Exception as e:
        return None
