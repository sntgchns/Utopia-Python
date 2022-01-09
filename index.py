from flask import Flask, render_template, request
from flask_mail import Mail, Message
from config import secret

app = Flask(__name__)

app.config['MAIL_SERVER'] = secret[0]
app.config['MAIL_PORT'] = secret[1]
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = secret[2]
app.config['MAIL_PASSWORD'] = secret[3]

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
                      cc=[''], # Copia
                      bcc=['santiagosonora@gmail.com'], # Copia oculta
                      recipients=[('info@utopiansworld.com', "Utopian's World")]) # Destinatario
        msg.html = f"<html><body style='display: inline-block; background: rgb(221, 199, 161); border: 6px solid green;'><div style='display: flex; justify-content: center; background: rgb(109,0,100);'><h1 style='color: rgb(222,222,222); text-transform: uppercase;'>Utopia</h1></div><div style='display: inline-block; padding: 10px;'><h3 style='display: inline-block; color: rgb(109,0,100); padding: 0; margin: 0;'><b>Este mensaje fue enviado por: </b></h3><p style='display: inline-block; color: rgb(127,111,0); padding: 0 0 0 10px; margin: 0;'>{nombre}</p></div><br><div style='display: inline-block; padding:10px;'><h3 style='display: inline-block; color: rgb(109,0,100); padding: 0; margin: 0;'><b>Su e-mail es: </b></h3><p style='display: inline-block; color: rgb(127,111,0); padding: 0 0 0 10px; margin: 0;'>{email}</p></div><br><div style='display: inline-block; padding:10px;'><h3 style='display: inline-block; color: rgb(109,0,100); padding: 0; margin: 0;'><b>Mensaje: </b></h3><p style='display: inline-block; color: rgb(127,111,0); padding: 0 0 0 10px; margin: 0;'>{mensaje}</p></div></body></html>" 
        mail.send(msg) 
        return render_template('thanks.html', nombre=nombre) 
    return render_template('index.html') 

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404 
    
if __name__ == '__main__':
    app.run(debug=False)
