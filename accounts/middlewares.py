from channels.auth import AuthMiddlewareStack
from knox.auth import TokenAuthentication
from asgiref.sync import sync_to_async
from channels.db import database_sync_to_async
from threading import Thread


class TokenAuthMiddleware:
    def __init__(self, inner):
        self.inner = inner
    
    # @sync_to_async
    async def __call__(self, scope, receive, send):
        # try:
        query_string = scope['query_string']
        query_string = str(query_string)
        if 'token=' in query_string:
            token = query_string.replace('token=', '')
            token = eval(token)
            scope['user'], scope['auth_token'] = TokenAuthentication().authenticate_credentials(token)
            print(scope["user"])
        # except:
        #     pass

        return await self.inner(scope, receive, send)

TokenAuthMiddlewareStack = lambda inner: TokenAuthMiddleware(AuthMiddlewareStack(inner))
