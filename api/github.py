import os
import requests

headers = {
    "Accept": "application/vnd.github+json",
    "Authorization": "Bearer {}".format(os.getenv("GITHUB_TOKEN")),
}


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
