import jwt
import datetime

# Секретный ключ для подписания токена
SECRET_KEY = "your-sercet-key"

# Данные, которые мы хотим закодировать в токен
payload = {
    'user_id': 123,
    'username': 'akrom',
    'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=3600)
}

# Создание JWT токена
token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

print(f"JWT token: {token}")

# Проверка и декодирование токена
try:
    decoded_payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
    print(f"Decoded date: {decoded_payload}")
except jwt.ExpiredSignatureError:
    print("The token has expired")

except jwt.InvalidTokenError:
    print("Invalid token")
