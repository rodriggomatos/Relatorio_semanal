
from AsanaApi import AsanaAPI
from Project_Status_Manager import ProjectStatusManager
from GmailAPI import GmailApi

from datetime import date
#from WhatsApp_bot import WhatsAppBot
from html_format import *

def configura_ambiente():
    """
    Configura variáveis de ambiente e inicializa serviços necessários.
    """    
    
    #global whatsapp
    #whatsapp = WhatsAppBot()
    
    global gmail
    gmail = GmailApi()
    
    global asana 
    asana = AsanaAPI()

def processa_tarefas():
    """
    Processa as tarefas do projeto utilizando APIs e envia notificações.
    """
    asana_api = AsanaAPI()
    tasks = asana_api.get_project_tasks()
    project_status_manager = ProjectStatusManager(colunas_projetos(), tasks)
    
    enviar_notificacoes(tasks, project_status_manager)

def prepare_status_message(task_name, project_status):
    #message = "🔄 *Atualiação:*\n\n"  # Título em negrito
    message = f"🔄 *Atualização do projeto - {task_name}:*\n\n"
    for column, status in project_status.items():
        # Nome da coluna em negrito e valor em itálico para destaque
        message += f"*{column}:* _{status}_\n"
    return message

def colunas_projetos():
    return [    
        "Status PPCI",
        "PPCI - Data Aprovação",
        "Status Hidro Cia de Águas",
        "Status Hidro Prefeitura",
        "Status Elétrico legal",        
        "Fase do projeto",
        "Direcionamentos",        
        "Relatório de arquitetura",
        "Fase 00",
        "Fase 01",
        "Fase 02",
        "Fase 03",
    ]

def enviar_notificacoes(tasks, project_status_manager):
    """
    Envia atualizações sobre o status das tarefas por e-mail ou WhatsApp.
    """
    enviar_via_whatsapp = False
    enviar_via_email = True
    i = 0
    for task in tasks:
        if not task.get('name') or not deve_enviar_notificacao(task):continue

        updated_project_status = project_status_manager.get_project_status(task)        
        
        if enviar_via_whatsapp and task.get('custom_fields', {}).get('WhatsApp'):
            message = prepare_status_message(task['name'], updated_project_status)
            envia_whatsapp(task['custom_fields']['WhatsApp'], message)
            
        if enviar_via_email:
            html_content = prepare_status_message_html_2(task['name'], updated_project_status)
            assunto = f"Status do Projeto - {task['name']}"
            gmail.send_email_html(assunto, html_content, "rodrigo@thorusengenharia.com.br")
            print("Email enviado")
            i += 1
          

def deve_enviar_notificacao(task):
    """
    Determina se uma notificação deve ser enviada com base nos campos personalizados da tarefa.
    """
    send_field = task.get('custom_fields', {}).get("Enviar", {})
    enum_value = send_field.get('enum_value', {})
    return enum_value.get('name') == "SIM"

def envia_whatsapp(numero, mensagem):
    """
    Envia uma mensagem via WhatsApp para o número especificado.
    """
    #whatsapp.send_message(numero, mensagem)

def process_emails(emails_str):
    """
    Processa uma string contendo emails separados por '/' e remove espaços indesejados.

    Args:
    emails_str (str): A string de emails a ser processada.

    Returns:
    list: Uma lista contendo os emails processados.
    """
    if emails_str is None:
        return []

    # Remove espaços em branco da string
    emails_str = emails_str.replace(" ", "")
    
    # Divide a string em uma lista usando '/' como separador
    email_list = emails_str.split('/')
    
    # Filtra qualquer string vazia que possa existir na lista
    email_list = [email for email in email_list if email]
    
    return email_list

if __name__ == '__main__':
    configura_ambiente()
    
    tasks = asana.get_project_tasks()
    
    project_status_manager = ProjectStatusManager(colunas_projetos(), tasks)
    
    enviar_via_whatsapp = False
    
    enviar_via_email = True
    
    i=0
    
    for task in tasks:
        task_name = task.get('name')       
        
        #if(task_name != '23027 - Lumma - Seven - Porto Belo - SC'): continue

        if not task_name: continue
        
        custom_fields = {campo['name']: campo for campo in task.get('custom_fields', [])}        
        send_field = custom_fields.get("Enviar")
        
        if not send_field: continue
        
        enum_value = send_field.get('enum_value', {})
        if enum_value is not None and enum_value.get('name') == "SIM":               
            updated_project_status = project_status_manager.get_project_status(task)           
            message = prepare_status_message(task_name, updated_project_status)                    
           
            if(enviar_via_whatsapp):
                #destination = '+5511932112195'           
                whatsapp_field = custom_fields.get("WhatsApp")
                
                if whatsapp_field and whatsapp_field.get('text_value'):
                    whatsapp_number = whatsapp_field.get('text_value').strip()
                    destination = whatsapp_number
            
            if(enviar_via_email):
                emails = custom_fields.get("Contatos (e-mail):")
                list_emails = process_emails(emails.get('text_value'))
                html_content = prepare_status_message_html_2(task_name, updated_project_status)
                assunto = f"Status do Projeto - {task_name}"
                list_emails = {'rodrigo@thorusengenharia.com.br', 'amanda@thorusengenharia.com.br'}
                for email in list_emails:
                    try:
                        gmail.send_email_html(assunto, html_content, 'rodrigo@thorusengenharia.com.br')
                        print(f"Email enviado para {email}")
                        i = i + 1
                    except Exception as e:
                        gmail.send_email(assunto, html_content, 'rodrigo@thorusengenharia.com.br')
        
                  
