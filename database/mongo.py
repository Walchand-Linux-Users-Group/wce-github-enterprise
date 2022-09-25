from mongoengine import *
from mongoengine import *
import os

connect(host=os.getenv("MONGO_URI"))
