import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def enviar_email(email_destinatario):
    #Configurações do remetente
    email_sender = 'caramezgabriel72@gmail.com'
    senha_sender = 'wsgq sjxq jyym yjhf'

    #Criando mensagem
    mensagem = MIMEMultipart()
    mensagem['From'] = email_sender
    mensagem['To'] = email_destinatario
    mensagem['Subject'] = 'Mensagem Especial'

    corpo_email = """
    <html>
    <head>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: #fffbe6;
                color: #ff4e50;
                padding: 0;
                margin: 0;
            }
            .container {
                background: #fffde7;
                border: 2px solid #ffb347;
                border-radius: 12px;
                max-width: 400px;
                margin: 30px auto;
                padding: 25px 20px;
                box-shadow: 0 4px 16px rgba(255, 78, 80, 0.10);
            }
            h2 {
                color: #ff9800;
                margin-bottom: 10px;
            }
            p {
                color: #ff4e50;
                font-size: 1.1em;
                margin-bottom: 10px;
            }
            .footer {
                color: #ff9800;
                font-size: 0.95em;
                margin-top: 18px;
                text-align: right;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h2>Olá, tudo bem?</h2>
            <p>
                Eu sou um email automático enviado para garantir sua 
                mesa na <b>BellaCrosta</b>, caso não consiga comparecer,
                por favor, cancele sua reserva.
            </p>
            <div class="footer">
                [Equipe BellaCrosta]
            </div>
        </div>
    </body>
    </html>
    """

    mensagem.attach(MIMEText(corpo_email, 'html'))

    try:
        servidor = smtplib.SMTP('smtp.gmail.com', 587)
        servidor.starttls()
        servidor.login(email_sender, senha_sender)
        texto = mensagem.as_string()
        servidor.sendmail(email_sender, email_destinatario, texto)
        servidor.quit()
        print("Email enviado com sucesso para", email_destinatario)
        return True
    except Exception as e:
        print("Erro ao enviar email")
        print(e)
        return False