# strategy/enviar_por_email.py
from strategy.metodo_de_envio import MetodoDeEnvio
from api.GmailAPI import GmailApi
from html_format import  prepare_status_message_html_2
class EnviarPorEmail(MetodoDeEnvio):
    def __init__(self):
        self.gmail = GmailApi()
    
    
    def get_contacts(self, custom_fields):        
     
        emails_str = custom_fields.get("Contatos (e-mail):").get('text_value')
        
        if emails_str is None:return []

        # Remove espaços em branco da string emails
        emails_str = emails_str.replace(" ", "")
        
        # Divide a string em uma lista usando '/' como separador
        email_list = emails_str.split('/')
        
        # Filtra qualquer string vazia que possa existir na lista
        email_list = [email for email in email_list if email]
        
        return email_list

     
    def send(self, task_name, columns_data, contacts):
        for contact in contacts:
            try:
                html_content = prepare_status_message_html_2(task_name, columns_data)
                assunto = f"Status do Projeto - {task_name}"
                self.gmail.send_email_html(assunto, html_content, contact)
                print(f"Email enviado para {contact}")
            except Exception as e:
                print(e)
                
    def send_one(self, subject: str, html_content: str, to: str, cc: list = None, bcc: list = None) -> bool:
        try:
            html_content = prepare_status_message_html_2(subject, html_content)
            assunto = f"Status do Projeto - {subject}"
            self.gmail.send_email_html(assunto, html_content, to, cc, bcc)
            print(f"Email enviado para {to}")
            return True
        except Exception as e:
            print(e)
            return False

            
    def send_notifications(self, task_name, columns_data, contacts):
        for contact in contacts:
            self.send(task_name, columns_data, contact) 
