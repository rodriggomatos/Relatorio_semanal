from strategy.enviar_por_email import EnviarPorEmail
from api.AsanaApi import AsanaAPI
from models.Project_Status_Manager import TaskColumnsExtractor
from models.Columns_Names import columns_names

def must_send_notification(task):
    """
    Determina se uma notificação deve ser enviada com base nos campos personalizados da tarefa.
    """
    if not task.get('name'): return False
    
    custom_fields = {campo['name']: campo for campo in task.get('custom_fields', [])}
    if not custom_fields: return False    
    
    send_field = custom_fields.get("Enviar", {})
    
    enum_value = send_field.get('enum_value', {})
    
    if(not enum_value): return False
    
    must_send = enum_value.get('name') == "SIM"
    
    return must_send
    
strategy = EnviarPorEmail()

asana = AsanaAPI()

tasks = asana.get_project_tasks()

task_columns_extractor = TaskColumnsExtractor(columns_names(), tasks)  

for task in tasks:
    
    if not must_send_notification(task):continue

    custom_fields = {field['name']: field for field in task.get('custom_fields', [])}    
        
    task_name = task['name']
    
    columns_data = task_columns_extractor.get_columns(task)    
    
    contacts = strategy.get_contacts(custom_fields)
    
    if(not contacts): continue   
    
    #contacts = {'rodrigo@thorusengenharia.com.br'#',amanda@thorusengenharia.com.br'}
   
    strategy.send(task_name, columns_data, contacts)
    
                        
    