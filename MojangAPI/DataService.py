from .Errors import *
from .Tokens import generateClientToken
from .Request import *
from .Endpoints import *


class Data:
    """Stores methods for getting information not related to Users"""
    @classmethod
    async def getBlockedServers() -> list:
        """Returns a list of SHA1 hashes used to check server addresses against when the client tries to connect"""
        return await Request.get(SessionServerEndpoints.BLOCKED_SERVERS)
    
    @classmethod
    async def getStatistics(cls, item_sold_minecraft=False, prepaid_card_redeemed_minecraft=False, item_sold_cobalt=False, item_sold_scrolls=False, prepaid_card_redeemed_cobalt=False, item_sold_dungeons=False) -> dict:
        """Returns sale data corresponding to the sum of all the requested types"""
        data = {
            "item_sold_minecraft": item_sold_minecraft,
            "prepaid_card_redeemed_minecraft": prepaid_card_redeemed_minecraft,
            "item_sold_cobalt": item_sold_cobalt,
            "item_sold_scrolls": item_sold_scrolls,
            "prepaid_card_redeemed_cobalt": prepaid_card_redeemed_cobalt,
            "item_sold_dungeons": item_sold_dungeons
        }

        payload = {
            "metricKeys": [k for k, v in data.items() if v]
        }
        
        return await Request.post(APIserverEndpoints.STATISTICS, payload, {'content-type': 'application/json'})

    @classmethod
    async def checkServerStatus(cls) -> list:
        """Returns a list of dictionaries containing the status of various Mojang services"""
        return await Request.get(StatusServerEndpoints.CHECK_STATUS)
