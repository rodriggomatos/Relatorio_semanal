from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

class WhatsAppBot:
    def __init__(self):
        account_sid = os.getenv('TWILIO_ACCOUNT_SID')
        auth_token = os.getenv('TWILIO_AUTH_TOKEN')
        sender_number = os.getenv('TWILIO_SENDER_NUMBER')
        self.client = Client(account_sid, auth_token)
        self.sender_number = sender_number
    
    def send_message(self, destino, mensagem):
        message = self.client.messages.create(
            from_=f'whatsapp:{self.sender_number}',
            body=mensagem,
            to=f'whatsapp:{destino}'
        )
        print(f'Mensagem enviada com SID: {message.sid} para {destino}')