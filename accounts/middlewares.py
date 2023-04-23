from channels.auth import AuthMiddlewareStack
from knox.auth import TokenAuthentication
from asgiref.sync import sync_to_async

def get_user(token):
   return TokenAuthentication().authenticate_credentials(token)

class TokenAuthMiddleware:
    def __init__(self, inner):
        self.inner = inner
    
    async def __call__(self, scope, receive, send):
        try:
            query_string = scope['query_string']
            query_string = str(query_string)
            if 'token=' in query_string:
                token = query_string.replace('token=', '')
                token = eval(token)
                scope['user'], scope['auth_token'] = await sync_to_async(get_user)(token)
        except:
            pass

        return await self.inner(scope, receive, send)

TokenAuthMiddlewareStack = lambda inner: TokenAuthMiddleware(AuthMiddlewareStack(inner))
