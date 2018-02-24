from twilio.rest import Client
import pyautogui
import time
from datetime import datetime

data = str(datetime.now())
global a 

def msn():
	account_sid = ""
	auth_token  = ""
	client = Client(account_sid, auth_token)
	text = str('Evento inesperado em {}'.format(data))
	message = client.messages.create(to="number",
		from_="numberphonetwilio",
		body = text)

def move():
	a ,b = pyautogui.position()
	x = a 
	while a == x:
		time.sleep(1)
		a,b = pyautogui.position()
		print('Monitorando')
	msn()
move()
