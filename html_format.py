
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


def prepare_status_message_html_6(task_name, project_status):
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
                background-color: #f4f4f9;
                margin: 0;
                padding: 0;
                color: #333;
                line-height: 1.6;
            }}
            .container {{
                background: #ffffff;
                width: 90%;
                max-width: 650px;
                margin: 40px auto;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.12);
                border: 1px solid #ddd;
            }}
            .header {{
                text-align: center;
                margin-bottom: 25px;
                padding-bottom: 15px;
                border-bottom: 2px solid #56017d;
            }}
            .logo {{
                width: 100%;
                max-width: 180px;
                margin-bottom: 15px;
            }}
            h2 {{
                font-size: 22px;
                color: #56017d;
                text-align: center;
                margin-bottom: 15px;
            }}
            .status-container {{
                padding: 10px 0;
            }}
            .status-item {{
                background: #f9f9f9;
                margin: 10px 0;
                padding: 15px;
                border-left: 6px solid #56017d;
                font-size: 16px;
                border-radius: 6px;
                box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
                transition: box-shadow 0.3s ease-in-out, transform 0.2s;
            }}
            .status-item:hover {{
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
                transform: translateY(-3px);
            }}
            .status-label {{
                font-weight: bold;
                color: #56017d;
                font-size: 16px;
                display: block;
                margin-bottom: 5px;
            }}
            .status-value {{
                color: #333;
                font-size: 14px;
            }}
            .footer {{
                text-align: center;
                font-size: 12px;
                color: #777;
                margin-top: 20px;
                padding-top: 15px;
                border-top: 1px solid #ddd;
            }}
            .footer p {{
                margin: 5px 0;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <!-- Espaço reservado para a logo da empresa -->
                <img src="https://storage.googleapis.com/thosrus-imagens/logo_thorus_versoes_roxa.png" alt="Logo da Empresa" class="logo">
            </div>
            <h2>Atualização do Projeto - {task_name}</h2>
            <div class="status-container">
    """

    for column, status in project_status.items():
        message += f"""
            <div class='status-item'>
                <span class='status-label'>{column}:</span>
                <span class='status-value'>{status}</span>
            </div>
        """

    message += f"""
            </div>
            <div class="footer">
                <p>Atualizado em {date.today().strftime('%d/%m/%Y')}</p>
                <p>Este e-mail foi gerado automaticamente.</p>
            </div>
        </div>
    </body>
    </html>
    """
    return message

from datetime import date

def prepare_status_message_html_7(task_name, project_status):
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
                text-align: center;
            }}
            .logo {{
                width: 100%;
                max-width: 180px;
                margin-bottom: 20px;
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
                text-align: left;
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
                box-shadow: 0 5px 15px rgba(0,0,0,0.20);
                transform: translateY(-2px);
            }}
            .footer {{
                font-size: 12px;
                color: #777;
                margin-top: 20px;
                padding-top: 10px;
                border-top: 1px solid #ddd;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <!-- Imagem da empresa -->
            <img src="https://storage.googleapis.com/thosrus-imagens/logo_thorus_versoes_roxa.png" alt="Logo da Empresa" class="logo">
            
            <h2>Atualização do projeto - {task_name}:</h2>
    """

    # Gera a lista de status com o mesmo design
    for column, status in project_status.items():
        message += f"<div class='status-item'><span class='status-label'>{column}:</span> <span class='status-value'>{status}</span></div>"

    # Fecha as tags HTML e adiciona um rodapé
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


from datetime import date

def prepare_status_message_html_8_cloud(task_name, project_status):
    message = f"""
    <!DOCTYPE html>
    <html lang="pt">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Atualização do Projeto</title>
        <style>
            :root {{
                --primary-color: #56017d;
                --secondary-color: #46000d;
                --background-color: #f8f9fa;
                --card-background: #ffffff;
                --hover-shadow: 0 8px 24px rgba(86, 1, 125, 0.15);
                --border-radius: 12px;
                --spacing-sm: 8px;
                --spacing-md: 16px;
                --spacing-lg: 24px;
            }}
            
            * {{
                box-sizing: border-box;
                margin: 0;
                padding: 0;
            }}
            
            body {{
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background-color: var(--background-color);
                color: #333;
                line-height: 1.6;
                padding: var(--spacing-lg);
            }}
            
            .container {{
                background: var(--card-background);
                width: 100%;
                max-width: 650px;
                margin: 0 auto;
                padding: var(--spacing-lg) var(--spacing-lg) calc(var(--spacing-lg) * 1.5);
                border-radius: var(--border-radius);
                box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1);
            }}
            
            .header {{
                display: flex;
                flex-direction: column;
                align-items: center;
                margin-bottom: var(--spacing-lg);
                padding-bottom: var(--spacing-lg);
                border-bottom: 1px solid #eee;
            }}
            
            .logo {{
                width: 100%;
                max-width: 180px;
                margin-bottom: var(--spacing-md);
                transition: transform 0.3s ease;
            }}
            
            .logo:hover {{
                transform: scale(1.05);
            }}
            
            h2 {{
                font-size: 24px;
                color: var(--primary-color);
                text-align: center;
                margin-top: var(--spacing-md);
                font-weight: 600;
            }}
            
            .project-title {{
                font-weight: 700;
                background: linear-gradient(45deg, var(--primary-color), #8a2be2);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                background-clip: text;
                display: inline-block;
            }}
            
            .status-container {{
                display: grid;
                gap: var(--spacing-md);
                margin: var(--spacing-lg) 0;
            }}
            
            .status-item {{
                background: #fafafa;
                padding: var(--spacing-md);
                border-radius: var(--border-radius);
                border-left: 4px solid var(--primary-color);
                box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
                transition: all 0.3s ease;
                display: flex;
                flex-direction: column;
            }}
            
            .status-item:hover {{
                box-shadow: var(--hover-shadow);
                transform: translateY(-2px);
                background-color: #f5f0ff;
            }}
            
            .status-label {{
                font-weight: 600;
                color: var(--primary-color);
                margin-bottom: var(--spacing-sm);
                font-size: 15px;
            }}
            
            .status-value {{
                color: var(--secondary-color);
                font-size: 16px;
                word-wrap: break-word;
            }}
            
            .footer {{
                font-size: 13px;
                color: #777;
                margin-top: var(--spacing-lg);
                padding-top: var(--spacing-md);
                border-top: 1px solid #eee;
                text-align: center;
            }}
            
            .footer p:first-child {{
                margin-bottom: var(--spacing-sm);
            }}
            
            .date-info {{
                background-color: #f5f0ff;
                display: inline-block;
                padding: 4px 8px;
                border-radius: 4px;
                font-weight: 500;
                margin-top: var(--spacing-sm);
            }}
            
            @media (max-width: 600px) {{
                body {{
                    padding: var(--spacing-sm);
                }}
                
                .container {{
                    padding: var(--spacing-md);
                }}
                
                h2 {{
                    font-size: 20px;
                }}
                
                .status-item {{
                    padding: var(--spacing-sm);
                }}
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <!-- Imagem da empresa -->
                <img src="https://storage.googleapis.com/thosrus-imagens/logo_thorus_versoes_roxa.png" alt="Logo da Empresa" class="logo">
                
                <h2>Atualização do projeto<br><span class="project-title">{task_name}</span></h2>
            </div>
            
            <div class="status-container">
    """
    
    # Gera a lista de status com o design melhorado
    for column, status in project_status.items():
        message += f"""
                <div class="status-item">
                    <span class="status-label">{column}</span>
                    <span class="status-value">{status}</span>
                </div>
        """
    
    # Fecha as tags HTML e adiciona um rodapé melhorado
    message += f"""
            </div>
            
            <div class="footer">
                <p>Este email foi gerado automaticamente pelo sistema.</p>
                <p class="date-info">Atualizado em {date.today().strftime('%d/%m/%Y')}</p>
            </div>
        </div>
    </body>
    </html>
    """
    return message




from datetime import date

def prepare_status_message_html_9(task_name, project_status):
    message = f"""
    <!DOCTYPE html>
    <html lang="pt">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Atualização do Projeto</title>
        <style>
            /* Configuração global */
            body {{
                font-family: 'Inter', Arial, sans-serif;
                background-color: #f4f7fc;
                margin: 0;
                padding: 0;
                color: #333;
                line-height: 1.6;
            }}
            .container {{
                width: 90%;
                max-width: 650px;
                background: #ffffff;
                margin: 40px auto;
                padding: 30px;
                border-radius: 12px;
                box-shadow: 0 8px 20px rgba(0, 0, 0, 0.15);
                text-align: center;
            }}

            /* Modo escuro automático */
            @media (prefers-color-scheme: dark) {{
                body {{
                    background-color: #121212;
                    color: #e0e0e0;
                }}
                .container {{
                    background-color: #1e1e1e;
                    box-shadow: none;
                }}
                .status-item {{
                    background: #252525;
                    color: #ddd;
                }}
            }}

            /* Cabeçalho */
            .header {{
                border-bottom: 3px solid #6C5DD3;
                padding-bottom: 15px;
            }}
            .logo {{
                width: 160px;
                margin-bottom: 15px;
            }}
            h2 {{
                font-size: 24px;
                color: #6C5DD3;
                margin-top: 15px;
                font-weight: 600;
            }}

            /* Indicadores visuais */
            .badge {{
                display: inline-block;
                padding: 6px 12px;
                font-size: 12px;
                font-weight: bold;
                border-radius: 16px;
                color: white;
            }}
            .badge-pending {{ background: #f39c12; }}  /* Amarelo */
            .badge-completed {{ background: #2ecc71; }} /* Verde */
            .badge-delayed {{ background: #e74c3c; }} /* Vermelho */

            /* Timeline visual */
            .timeline {{
                list-style: none;
                padding: 20px 0;
                position: relative;
                margin: 20px auto;
                max-width: 500px;
            }}
            .timeline:before {{
                content: "";
                position: absolute;
                width: 3px;
                background: #6C5DD3;
                top: 0;
                bottom: 0;
                left: 50%;
                margin-left: -1.5px;
            }}
            .timeline-item {{
                padding: 10px;
                position: relative;
                width: 50%;
                margin-bottom: 20px;
            }}
            .timeline-item:nth-child(odd) {{
                left: 0;
            }}
            .timeline-item:nth-child(even) {{
                left: 50%;
            }}
            .timeline-content {{
                background: #ffffff;
                padding: 15px;
                border-radius: 6px;
                box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            }}

            /* Botão CTA */
            .button {{
                display: inline-block;
                margin-top: 25px;
                background: linear-gradient(135deg, #6C5DD3, #8E80E2);
                color: #fff;
                padding: 14px 28px;
                border-radius: 8px;
                text-decoration: none;
                font-size: 16px;
                font-weight: bold;
                transition: background 0.3s ease-in-out;
            }}
            .button:hover {{
                background: linear-gradient(135deg, #8E80E2, #6C5DD3);
            }}

            /* Rodapé */
            .footer {{
                margin-top: 30px;
                font-size: 12px;
                color: #777;
                padding-top: 10px;
                border-top: 1px solid #ddd;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <img src="https://storage.googleapis.com/thosrus-imagens/logo_thorus_versoes_roxa.png" alt="Logo da Empresa" class="logo">
                <h2>Atualização do Projeto - {task_name}</h2>
            </div>
            
            <div class="status-container">
    """

    for column, status in project_status.items():
        badge_class = "badge-completed" if "Concluído" in status else "badge-pending" if "Em andamento" in status else "badge-delayed"
        message += f"""
            <div class='status-item'>
                <span class='status-label'>{column}:</span> <span class="badge {badge_class}">{status}</span>
            </div>
        """

    message += f"""
            </div>

            <!-- Seção Timeline -->
            <ul class="timeline">
                <li class="timeline-item"><div class="timeline-content">✅ Início do Projeto</div></li>
                <li class="timeline-item"><div class="timeline-content">🛠 Desenvolvimento em Andamento</div></li>
                <li class="timeline-item"><div class="timeline-content">📅 Revisão Final Agendada</div></li>
            </ul>

            <a href="#" class="button">Ver Detalhes</a>

            <div class="footer">
                <p>Email enviado automaticamente.</p>
                <p>Atualizado em {date.today().strftime('%d/%m/%Y')}</p>
            </div>
        </div>
    </body>
    </html>
    """
    return message
