import requests


def send_message_to_telegram_bot(api_token, chat_id, message):
	url = f"https://api.telegram.org/bot{api_token}/sendMessage"
	payload = {
		'chat_id': chat_id,
		'text': message
	}

	response = requests.post(url, json=payload)

	if response.status_code == 200:
		print("Заявка відправлена!")
	else:
		print("Помилка. Спробуйте ще раз!")


def stop_chat_bot():
	print("Зупинити чат")
	exit()


api_token = "5948216208:AAGbamsFsZQ89_6v9J59f6V178aqYVHs6C"
chat_id = "YOUR_CHAT_ID"
message = str(input())

send_message_to_telegram_bot(api_token, chat_id, message)

user_input = input("Натисніть будь-яку кнопку, щоб зупинити чат")
stop_chat_bot()