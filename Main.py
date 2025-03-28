from strategy.enviar_por_email import EnviarPorEmail
from api.AsanaApi import AsanaAPI
from models.Project_Status_Manager import TaskColumnsExtractor
from models.Columns_Names import columns_names
from datetime import datetime

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
    try:
        if not must_send_notification(task):continue

        custom_fields = {field['name']: field for field in task.get('custom_fields', [])}    
            
        task_name = task['name'] 
        
        if(not task_name=="Teste-Automação-Rodrigo"): continue
        
        columns_data = task_columns_extractor.get_columns(task)    
        
        contacts = strategy.get_contacts(custom_fields)
        
        if(not contacts): continue   
        
        #contacts = {'engrodriggo4@gmail.com'}
        
        bbc = ['rodrigo@thorusengenharia.com.br']
        responsable = asana.get_responsible_email(task)
        #if(responsable):
            #bbc.append(responsable)
        
        #strategy.send(task_name, columns_data, contacts)
        
        result = strategy.send_one(task_name, columns_data, contacts, None, bbc)
        if result:
            asana.mark_email_sent(task['gid'], custom_fields, datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        else:
            asana.mark_email_sent(task['gid'], custom_fields, "Email não enviado")
            
        '''
        for contact in contacts:            
            result = strategy.send_one(task_name, columns_data, contact, None, bbc)
            if result:
                asana.mark_email_sent(task['gid'], custom_fields, datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
            else:
                asana.mark_email_sent(task['gid'], custom_fields, "Email não enviado")
        '''
    except Exception as e:       
        asana.mark_email_sent(task['gid'], custom_fields, f"Erro: {str(e)}")
    
    
   
    
                        
    