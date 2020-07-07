from uuid import uuid4

def generateClientToken():
    return uuid4().hex
