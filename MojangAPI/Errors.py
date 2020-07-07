class PlayerNotFound(Exception):
    pass

class InvalidTimestamp(Exception):
    pass

class IllegalPayload(Exception):
    pass

class Unauthenticated(Exception):
    pass

class ForbiddenOperation(Exception):
    pass

class MethodNotAllowed(Exception):
    pass

class SecurityQuestionsUnavailable(Exception):
    pass

def handle(response):
    if response['error'] == 'IllegalArgumentException':
        raise IllegalPayload(response['errorMessage'])
    elif response['error'] == 'ForbiddenOperationException':
        raise ForbiddenOperation(response['errorMessage'])
    elif response['error'] == 'Method Not Allowed':
        raise MethodNotAllowed(response['errorMessage'])
    else:
        raise Exception(response['errorMessage'])