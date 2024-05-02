
import requests
from twilio.rest import Client
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
import base64
from email.message import EmailMessage
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from dotenv import load_dotenv

load_dotenv()

class AsanaAPI:
    PROJECT_ID = '1203362410644441'
    def __init__(self,base_url='https://app.asana.com/api/1.0/'):
        self.access_token = os.getenv('ASANA_ACCESS_TOKEN')
        self.project_id='1203362410644441'
        self.base_url = base_url
        self.headers = {'Authorization': f'Bearer {self.access_token}'}
    
    def get_project_tasks(self, opt_fields='name,custom_fields,assignee.name'):
        endpoint = f'projects/{AsanaAPI.PROJECT_ID}/tasks'
        params = {'opt_fields': opt_fields}
        return self._make_paginated_request(endpoint, params=params)
    
    def _make_paginated_request(self, endpoint, params=None):
        all_data = []
        while True:
            response = requests.get(f'{self.base_url}{endpoint}', headers=self.headers, params=params)
            if response.status_code == 200:
                json_response = response.json()
                all_data.extend(json_response.get('data', []))
                next_page = json_response.get('next_page')
                if not next_page:
                    break
                params['offset'] = next_page['offset']
            else:
                print(f'Erro ao acessar {endpoint}. Código de status: {response.status_code}')
                break
        return all_data
