from flask import Flask, render_template, request, json
from flask_mail import Mail, Message
from config import mail_username, mail_password, secret, sitekey
import requests

app = Flask(__name__)

app.config['SECRET_KEY'] = secret
app.config['MAIL_SERVER'] = 'smtp.ionos.es'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = mail_username
app.config['MAIL_PASSWORD'] = mail_password

mail = Mail(app)

def is_human(captcha_response):
    payload = {'response':captcha_response, 'secret':secret, 'remoteip': request.remote_addr}
    response = requests.post("https://www.google.com/recaptcha/api/siteverify", payload)
    response_text = json.loads(response.text)
    return response_text['success']

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        email = request.form['email']
        celular = request.form['celular']
        mensaje = request.form['mensaje']
        captcha_response = request.form['g-recaptcha-response']
        msg = Message(subject=f"Correo de {nombre} {apellido}", body=f"Nombre: {nombre}\nApellido: {apellido}\nEmail: {email}\nCelular: {celular}\nMensaje: {mensaje}", sender=mail_username, recipients=['santiagochinas@hotmail.com'])
        if is_human(captcha_response):
            status = ""
        mail.send(msg)
        return render_template('index.html')
    return render_template('index.html', sitekey=sitekey)

if __name__ == '__main__':
    app.run(debug=True)
