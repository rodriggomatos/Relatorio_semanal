from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
import base64
from email.message import EmailMessage
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import json

class GmailApi:
    def __init__(self):
        creds = None 
        SCOPES = ['https://www.googleapis.com/auth/gmail.send']
        
        self.SCOPES = SCOPES
        creds = None
        '''
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', self.SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file('credentials.json', self.SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.json', 'w') as token:
                token.write(creds.to_json())
        
        
        self.gmail_credentials_path = creds
        self.service = build('gmail', 'v1', credentials=creds)
        '''
        try:
            encoded_token = os.getenv('GOOGLE_TOKEN_BASE64')
            if encoded_token is None:
                raise ValueError("GOOGLE_TOKEN_BASE64 environment variable is not set.")
            token_json = base64.b64decode().decode('utf-8')
            token_data = json.loads(token_json)
            creds = Credentials.from_authorized_user_info(token_data)
            self.gmail_credentials_path = creds
            self.service = build('gmail', 'v1', credentials=creds)
        except Exception as e:
            print("Failed to decode the token:", str(e))
        

    
    def send_email(self, subject: str, body: str, to: str):
        message = EmailMessage()
        message.set_content(body)
        message['To'] = to
        message['Subject'] = subject
        message['From'] = 'rodrigo@thorusengenharia.com.br'

        encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

        create_message = {'raw': encoded_message}
        send_message = self.service.users().messages().send(userId="me", body=create_message).execute()
        print(f'Message Id: {send_message["id"]}')
        
    def send_email_html(self, subject, html_content, to):
        # Create a MIME multipart message
        message = MIMEMultipart('alternative')
        message['to'] = to
        message['subject'] = subject
        message['from'] = 'rodrigo@thorusengenharia.com.br'  # Replace with your sending email

        # Attach the HTML content as a MIMEText object
        message.attach(MIMEText(html_content, 'html'))

        # Encode the message in base64 urlsafe format
        raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

        # Prepare the message for sending
        message_body = {'raw': raw_message}

        # Send the message via Gmail API
        send_message = self.service.users().messages().send(userId="me", body=message_body).execute()
        print(f'Message Id: {send_message["id"]}')

    