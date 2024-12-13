import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#Configurações do remetente
email_sender = ''
#Susbstitua pelo seu endereço de email
senha_sender = ''
#Substitua pela sua senha do email

#Configurações do destinatário
email_destinatatario = ''
#Substitua pelo endereço de email do destinatário

#Criando mesagem
mensagem =MIMEMultipart()
mensagem['From'] = email_sender
mensagem['To'] = email_destinatatario
mensagem['Subject'] = 'Mensagem Especial'

#Corpo da mensagem

corpo_email="""
Olá, tudo bem?
Eu sou um email automático enviado pelo Python
Com muito carinho,
[Gabriel Caramez]
"""

mensagem.attach(MIMEText(corpo_email, 'plain'))

#Enviando email
try:
    servidor = smtplib.SMTP('smtp.gmail.com', 587)
    servidor.starttls()
    servidor.login(email_sender, senha_sender)
    texto = mensagem.as_string()
    servidor.sendmail(email_sender, email_destinatatario, texto)
    servidor.quit()
    print("Email enviado com sucesso para", email_destinatatario)
except Exception as e:
    print("Erro ao enviar email")
    print(e)
finally:
    servidor.quit()