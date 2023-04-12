import string, secrets

def generate_token() -> str:    
    numbers = string.digits
    token = ""
    while len(token) < 5:
        token += ''.join(secrets.choice(numbers))
    return token
