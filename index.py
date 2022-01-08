from flask import Flask, render_template, request
from flask_mail import Mail, Message
from config import mail_username, mail_password

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.ionos.es'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = mail_username
app.config['MAIL_PASSWORD'] = mail_password

mail = Mail(app)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        mensaje = request.form['mensaje']
        msg = Message(subject=f"Contact from UTOPIA", 
                      body=f"Nombre: {nombre}\nEmail: {email}\nMensaje: {mensaje}", 
                      sender=(nombre, email),
                      recipients=['santiagochinas@hotmail.com'])        
        mail.send(msg)
        return render_template('thanks.html', nombre=nombre)
    return render_template('index.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404
    
if __name__ == '__main__':
    app.run(debug=True)
