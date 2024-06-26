
import requests
import os
from typing import Dict
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

class AsanaAPI:
    PROJECT_ID = '1203362410644441'
    def __init__(self,base_url='https://app.asana.com/api/1.0/'):
        self.access_token = os.getenv('ASANA_ACCESS_TOKEN')
        if self.access_token is None:
            raise ValueError("ASANA_ACCESS_TOKEN environment variable is not set.")
        self.project_id='1203362410644441'
        self.base_url = base_url
        self.headers = {'Authorization': f'Bearer {self.access_token}'}
    
    def get_project_tasks(self, opt_fields='name,custom_fields,assignee.name,assignee.email'):
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
    
    def get_responsible_email(self, task: Dict) -> str:
        """
        Obtém o responsável pela tarefa a partir dos campos personalizados.
        """
        assignee = task.get('assignee')
        if assignee:
            return assignee.get('email', None)
        return None

    def update_task(self, task_id: str, update_data: Dict) -> None:
            """
            Atualiza uma tarefa no Asana.
            """
            url = f'{self.base_url}tasks/{task_id}'
            response = requests.put(url, headers=self.headers, json=update_data)
            if response.status_code != 200:
                print(f'Erro ao atualizar tarefa {task_id}. Código de status: {response.status_code}, Resposta: {response.json()}')
            
    def mark_email_sent(self, task_id: str, custom_fields: Dict, status: str) -> None:
        """
        Marca no Asana que o email foi enviado ou ocorreu um erro.
        """
        log_envio_gid = None
        for field in custom_fields.values():
            if field['name'] == 'Log Envio':
                log_envio_gid = field['gid']
                break
        
        if log_envio_gid is None:
            print("Campo personalizado 'Log Envio' não encontrado na tarefa.")
            return
        
        update_data = {
            "data": {
                "custom_fields": {
                    log_envio_gid: status
                }
            }
        }
        self.update_task(task_id, update_data)
   
        
   