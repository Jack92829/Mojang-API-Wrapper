from uuid import UUID, uuid4

def generateClientToken():
    return uuid4().hex
