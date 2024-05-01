
from datetime import date

def prepare_status_message_html_2(task_name, project_status):
    message = f"""
    <!DOCTYPE html>
    <html lang="pt">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Atualização do Projeto</title>
        <style>
            body {{
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background-color: #f4f4f4;
                margin: 0;
                padding: 0;
            }}
            .container {{
                background: #ffffff;
                width: 90%;
                max-width: 600px;
                margin: 20px auto;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 4px 8px rgba(0,0,0,0.15);
            }}
            h2 {{
                font-size: 20px;
                color: #56017d;
            }}
            .status-item {{
                background: #f9f9f9;
                margin: 10px 0;
                padding: 10px;
                border-left: 5px solid #56017d;
                font-size: 16px;
            }}
            .status-label {{
                font-weight: bold;
                color: #56017d;
            }}
            .status-value {{
                color: #46000d;
            }}
            .status-item:hover {{
                transition: box-shadow 0.3s, transform 0.2s;
                box-shadow: 0 5px 15px rgba(0,0,0,0.20); /* Sombra mais intensa no hover */
                transform: translateY(-2px); /* Efeito de elevação sutil */
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h2>Atualização do projeto - {task_name}:</h2>
    """
    
    # Generate the list of status updates with enhanced visual design
    for column, status in project_status.items():
        message += f"<div class='status-item'><span class='status-label'>{column}:</span> <span class='status-value'>{status}</span></div>"

    # Close the HTML tags and add a footer
    message += f"""
            <div class='footer'>
                <p>Email enviado automaticamente.</p>
                <p>Atualizado em {date.today().strftime('%d/%m/%Y')}</p>
            </div>
        </div>
    </body>
    </html>
    """
    return message


def prepare_status_message_html_3(task_name, project_status):    
    
    # Define the HTML header with internal CSS for styling
    message = f"""
    <!DOCTYPE html>
    <html lang="pt">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Atualização do Projeto</title>
        <style>
            body {{
                font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
                background-color: #f7f7f7;
                margin: 0;
                padding: 0;
            }}
            .container {{
                background: #ffffff;
                width: 90%;
                max-width: 600px;
                margin: 30px auto;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0,0,0,0.15);
            }}
            h2 {{
                font-size: 24px;
                color: #333;
                text-align: center;
                margin-bottom: 20px;
            }}
            .status-item {{
                background: linear-gradient(135deg, #ecfdfb, #eaf6f6);
                margin: 10px 0;
                padding: 15px;
                border-left: 5px solid #5cb85c;
                font-size: 16px;
                border-radius: 5px;
            }}
            .status-label {{
                font-weight: bold;
                color: #333;
                display: block; /* Makes the label take a full line */
                margin-bottom: 5px;
            }}
            .status-value {{
                color: #666;
                font-size: 14px;
            }}
            .footer {{
                text-align: center;
                font-size: 12px;
                color: #999;
                margin-top: 20px;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h2>Atualização do projeto - {task_name}</h2>
    """

    # Generate the list of status updates with enhanced visual design
    for column, status in project_status.items():
        message += f"<div class='status-item'><span class='status-label'>{column}</span> <span class='status-value'>{status}</span></div>"

    # Close the HTML tags and add a footer
    message += f"""
            <div class='footer'>Atualizado em {date.today().strftime('%d/%m/%Y')}</div>
        </div>
    </body>
    </html>
    """
    return message


def prepare_status_message_html_4(task_name, project_status):
    message = f"""
    <!DOCTYPE html>
    <html lang="pt">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Atualização do Projeto</title>
        <style>
            body {{
                font-family: 'Arial', sans-serif;
                background-color: #F3F4F6;
                margin: 0;
                padding: 0;
                color: #333;
            }}
            .container {{
                background: #FFFFFF;
                width: 100%;
                max-width: 600px;
                margin: 20px auto;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            }}
            h2 {{
                color: #4A90E2;
                font-size: 24px;
                text-align: center;
            }}
            .status-item {{
                background: #FFFFFF;
                border-bottom: 2px solid #EEF1F4;
                padding: 10px;
                display: flex;
                align-items: center;
            }}
            .status-label {{
                font-weight: bold;
                flex: 1;
            }}
            .status-value {{
                color: #666;
                margin-left: 10px;
            }}
            .status-icon {{
                width: 24px;
                height: 24px;
                margin-right: 10px;
                background-image: url('data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCI+PHBhdGggZmlsbD0iI0YwRDhFQyIgZD0iTTAgMGgyNHYyNEgweiIvPjwvc3ZnPg==');
            }}
            .footer {{
                text-align: center;
                font-size: 12px;
                color: #999;
                padding: 20px;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h2>Atualização do projeto - {task_name}</h2>
    """
    
    for column, status in project_status.items():
        message += f"""
            <div class='status-item'>
                <div class='status-icon'></div>
                <div class='status-label'>{column}</div>
                <div class='status-value'>{status}</div>
            </div>
        """

    message += f"""
            <div class='footer'>Atualizado em {date.today().strftime('%d/%m/%Y')}</div>
        </div>
    </body>
    </html>
    """
    return message

def prepare_status_message_html_5(task_name, project_status):
    message = f"""
    <!DOCTYPE html>
    <html lang="pt">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Atualização do Projeto</title>
        <style>
            body {{
                font-family: 'Arial', sans-serif; /* Usando Arial para uma aparência mais limpa e moderna */
                background-color: #f4f4f4;
                margin: 0;
                padding: 0;
                font-size: 16px;
            }}
            .container {{
                background: #ffffff;
                width: 90%;
                max-width: 600px;
                margin: 20px auto;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 4px 8px rgba(0,0,0,0.15);
            }}
            h2 {{
                font-size: 22px; /* ligeiramente maior para melhor legibilidade */
                color: #FFFFFF; /* cor do texto branco para melhor contraste */
                background: linear-gradient(135deg, #5A67D8, #9F7AEA); /* gradiente de azul para lilás */
                padding: 20px;
                border-radius: 8px 8px 0 0; /* arredondando apenas os cantos superiores */
                text-align: center; /* centralizando o texto */
            }}
            .status-item {{
                background: #f9f9f9;
                margin: 10px 0;
                padding: 10px;
                border-left: 5px solid #8a1796;
                font-size: 16px;
                border-radius: 8px; /* Adicionando bordas arredondadas */
                box-shadow: 0 2px 4px rgba(0,0,0,0.10); /* Adicionando uma sombra leve */
                transition: box-shadow 0.3s, transform 0.2s; /* Suavizando a transição */
            }}
            .status-label {{
                font-weight: bold;
                color: #333333;
                font-size: 16px; 
            }}
            .status-value {{
                color: #4A5568; /* Uma cor mais suave para melhor contraste visual */
                font-size: 14px;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h2>Atualização do projeto - {task_name}:</h2>
    """
    
    # Generate the list of status updates with enhanced visual design
    for column, status in project_status.items():
        message += f"<div class='status-item'><span class='status-label'>{column}</span> <span class='status-value'>{status}</span></div>"

    # Close the HTML tags and add a footer
    message += f"""
            <div class='footer'>Atualizado em {date.today().strftime('%d/%m/%Y')}</div>
        </div>
    </body>
    </html>
    """
    return message


