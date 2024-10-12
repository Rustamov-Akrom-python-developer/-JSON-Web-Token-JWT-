import jwt
import datetime


# Секретный ключ для подписания токена
SECRET_KEY = "your-secret-key"


# Создание токена
def create_token(user_id, username):
    payload = {
        'user_id': user_id,
        'username': username,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1), # Токен действителен 1 час
        'iat': datetime.datetime.utcnow(),
        'nbf': datetime.datetime.utcnow(),
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token


# Проверка токена
def verify_token(token):
    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return decoded
    except jwt.ExpiredSignatureError:
        print("The token has expired")

    except jwt.InvalidTokenError:
        print("Invalid token")


# Пример использования
if __name__=='__main__':
    token = create_token(123, 'akrom')
    print(f"JWT token: {token}")

    decoded_payload = verify_token(token)
    if decoded_payload:
        print(f"Decoded dates: {decoded_payload}")
