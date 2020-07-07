class APIserverEndpoints:
    GET_UUID = 'https://api.mojang.com/users/profiles/minecraft/{}'
    UUID_AT_TIME = 'https://api.mojang.com/users/profiles/minecraft/{}?at={}'
    NAME_HISTORY = 'https://api.mojang.com/user/profiles/{}/names'
    PLAYERS = 'https://api.mojang.com/profiles/minecraft'
    SKIN_METHOD = 'https://api.mojang.com/user/profile/{}/skin'
    AUTH_NEEDED = 'https://api.mojang.com/user/security/location'
    AUTH_LIST = 'https://api.mojang.com/user/security/challenges'
    STATISTICS = 'https://api.mojang.com/orders/statistics'


class AuthserverEndpoints:
    AUTHENTICATE = 'https://authserver.mojang.com/authenticate'
    REFRESH = 'https://authserver.mojang.com/refresh'
    VALIDATE = 'https://authserver.mojang.com/validate'
    SIGNOUT = 'https://authserver.mojang.com/signout'
    INVALIDATE = 'https://authserver.mojang.com/invalidate'


class SessionServerEndpoints:
    PROFILE_AND_ADDITIONAL = 'https://sessionserver.mojang.com/session/minecraft/profile/{}'
    BLOCKED_SERVERS = 'https://sessionserver.mojang.com/blockedservers'


class StatusServerEndpoints:
    CHECK_STATUS = 'https://status.mojang.com/check'