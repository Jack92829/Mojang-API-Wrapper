from .Errors import handle
from .Tokens import generateClientToken
from .Request import Request
from .Endpoints import *
import json
import base64 as b64
from urllib import parse

class Auth:
    """Authorization class containing methods for user authentication"""

    async def authenticate(self, username: 'Mojang username, NOT minecraft playername', password: 'Mojang account password') -> dict:
        """A method to authenticate a User, must be done before using certain methods, automatically saves the accessToken but also returns information"""
        self.mojangUsername = username
        payload = {
            "agent": {
                "name": "Minecraft",
                "version": 1
            },
            "username": username,  
            "password": password,
            "clientToken": self.clientToken,   
            "requestUser": True
        }

        headers = {'content-type': 'application/json'}

        response = await Request.post(AuthserverEndpoints.AUTHENTICATE, payload, headers)
        self.accessToken = response['accessToken']
        self.authenticated = True
        return response


    async def refresh(self):
        """Refreshes a valid access token"""
        if not self.authenticated:
            raise Unauthenticated('User has not been authenticated')

        payload = {
            "accessToken": self.accessToken,
            "clientToken": self.clientToken,
            "selectedProfile": {
                "id": None,
                "name": self.mojangUsername
            },
            "requestUser": True
        }

        headers = {'content-type': 'application/json'}

        response = await Request.post(AuthserverEndpoints.REFRESH, payload, headers)
        self.accessToken = response['accessToken']
        return response


    async def validate(self) -> bool:
        """Checks if an accessToken is usable for authentication with a minecraft server"""
        if not self.authenticated:
            raise Unauthenticated('User has not been authenticated')

        payload = {
            "accessToken": self.accessToken,
            "clientToken": self.clientToken
        }

        headers = {'content-type': 'application/json'}

        try:
            await Request.post(AuthserverEndpoints.VALIDATE, payload, headers)
            return True
        except:
            return False


    async def signout(self, password) -> None:
        """Invalidates an access token using an accounts username and password"""
        if not self.authenticated:
            raise Unauthenticated('User has not been authenticated')

        payload = {
            "username": self.mojangUsername,
            "password": password
        }

        headers = {'content-type': 'application/json'}

        return await Request.post(AuthserverEndpoints.SIGNOUT, payload, headers)


    async def invalidate(self) -> None:
        """Invalidates an access token using a client/access token pair"""
        if not self.authenticated:
            raise Unauthenticated('User has not been authenticated')

        payload = {
            "accessToken": self.accessToken,
            "clientToken": self.clientToken
        }

        headers = {'content-type': 'application/json'}

        return await Request.post(AuthserverEndpoints.INVALIDATE, payload, headers)



class Profile:
    """Empty class to store a profile in upon being called"""
    def __init__(self):
        pass



class User(Auth):
    @classmethod
    async def createUser(minecraftUsername: str, time: 'A UNIX timestamp'=None) -> 'A User object':
        """Returns an object containing a users uuid, minecraft username and client token"""
        self = User()

        self.minecraftUsername = minecraftUsername
        self.mojangUsername = None

        self.uuid = (await User.getUUID(minecraftUsername, time))['id']
        self.authenticated = False
        self.accessToken = None
        self.clientToken = generateClientToken()

        return self


    async def getUUID(self, username: str, time: 'A UNIX timestamp' = None) -> str:
        """A method that gets the UUID of a user, is not neccesary to be used by the user as it is called upon creating a User object"""
        if not time:
            return await Request.get(APIserverEndpoints.GET_UUID.format(username))
        else: 
            return await Request.get(APIserverEndpoints.UUID_AT_TIME.format(username, time))
    

    async def getNameHistory(self) -> list:
        """Getting all past names of a user, includes the current name"""
        return await Request.get(APIserverEndpoints.NAME_HISTORY.format(self.uuid))
    

    async def getProfile(self) -> Profile:
        """Returning a users profile, contains the users skin, id, name, cape and timestamp as attributes"""
        package = await Request.get(SessionServerEndpoints.PROFILE_AND_ADDITIONAL.format(self.uuid))
        package['properties'] = json.loads(b64.b64decode(package['properties'][0]['value']).decode('ascii'))

        profile = Profile()
        profile.id = package['id']
        profile.name = package['name']
        
        if package['properties']['textures'].get('SKIN'):
            profile.skin = package['properties']['textures']['SKIN']['url']
        else: profile.skin = None

        if package['properties']['textures'].get('CAPE'):
            profile.cape = package['properties']['textures']['CAPE']['url']
        else: profile.skin = None
        
        profile.timestamp = package['properties']['timestamp']
        profile.raw = package
        return profile


    async def changeSkin(self, skin_url: str, slimModel: bool = False) -> None:
        """Changing a users skin to the skin in a valid url"""
        if not self.authenticated:
            raise Unauthenticated('User has not been authenticated')

        payload = {
            'model': 'slim' if slimModel else '',
            'url': skin_url
        }

        headers = {
            'Authorization': f'Bearer {self.accessToken}'
        }

        return await Request.post(APIserverEndpoints.SKIN_METHOD.format(self.uuid), payload, headers, True)
        

    async def uploadSkin(self, file: 'Path to a file', slimModel: bool=False) -> None:
        """Uploads a skin to Mojang's servers as well as setting the users skin"""
        if not self.authenticated:
            raise Unauthenticated('User has not been authenticated')

        headers = {
            "Authorization": f"Bearer {self.accessToken}"
        }

        payload = {
            "model": 'slim' if slimModel else '',
            "file": open(file, 'rb')
        }
        
        return await Request.put(APIserverEndpoints.SKIN_METHOD.format(self.uuid), payload, headers)


    async def resetSkin(self) -> None:
        """Resets the users skin to the default one"""
        if not self.authenticated:
            raise Unauthenticated('User has not been authenticated')

        headers = {
            "Authorization": f"Bearer {self.accessToken}"
        }

        return await Request.delete(APIserverEndpoints.SKIN_METHOD.format(self.uuid), headers)
    

    async def checkForSecurityQuestions(self) -> bool:
        """Checks if the IP is not trusted, returns True if the IP is not trusted"""
        if not self.authenticated:
            raise Unauthenticated('User has not been authenticated')
        
        headers = {
            "Authorization": f"Bearer {self.accessToken}"
        }

        try:
            await Request.get(APIserverEndpoints.AUTH_NEEDED, headers)
            return False
        except:
            return True
    

    async def getSecurityQuestions(self) -> list:
        """Return a list of dicts containing security questions for the user to answer"""
        if not self.authenticated:
            raise Unauthenticated('User has not been authenticated')
        
        headers = {
            "Authorization": f"Bearer {self.accessToken}"
        }

        response = await Request.get(APIserverEndpoints.AUTH_LIST, headers)

        if not response:
            raise SecurityQuestionsUnavailable('Your Mojang account has no set security questions and can therefore cannot be validated')
        return response


    async def sendSecurityAnswers(self, answers: list) -> None:
        """Sends back the answers to the security questions in order to validate the IP of the user"""
        if not self.authenticated:
            raise Unauthenticated('User has not been authenticated')
        
        headers = {
            "Authorization": f"Bearer {self.accessToken}"
        }

        return await Request.post(APIserverEndpoints.AUTH_NEEDED, answers, headers)
