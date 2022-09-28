import streamlit
from mongoengine import *
import database.models


def createDepartment(orgName, orgId):
    try:
        newDept = database.models.Department(orgName=orgName, orgId=orgId)

        newDept.save()
        return False
    except Exception as e:
        return True
