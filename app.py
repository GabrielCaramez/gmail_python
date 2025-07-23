from flask import Flask, render_template, request
from Gmail import enviar_email

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        email_destinatario = request.form['email']
        descricao = request.form.get('descricao', '')
        sucesso = enviar_email(email_destinatario, descricao)
        if sucesso:
            return '''
            <div style="
                background: linear-gradient(90deg, #ffe066 60%, #ffb347 100%);
                color: #ff4e50;
                border: 2px solid #ffb347;
                border-radius: 10px;
                max-width: 350px;
                margin: 60px auto;
                padding: 25px 18px;
                font-family: Arial, sans-serif;
                font-size: 1.2em;
                text-align: center;
                box-shadow: 0 4px 16px rgba(255, 78, 80, 0.10);
            ">
                <b>Email enviado com sucesso!</b>
            </div>
            '''
        else:
            return '''
            <div style="
                background: linear-gradient(90deg, #ffb347 60%, #ff4e50 100%);
                color: #fff;
                border: 2px solid #ff4e50;
                border-radius: 10px;
                max-width: 350px;
                margin: 60px auto;
                padding: 25px 18px;
                font-family: Arial, sans-serif;
                font-size: 1.2em;
                text-align: center;
                box-shadow: 0 4px 16px rgba(255, 78, 80, 0.10);
            ">
                <b>Falha ao enviar email.</b>
            </div>
            '''
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
