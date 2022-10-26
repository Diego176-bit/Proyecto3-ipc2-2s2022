from flask import Flask, request
from flask_mail import Mail, Message
from users.db_users import data_base_users
from users.users_class import User
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hola'
app.config['MAIL_SERVER'] = 'smtp.office365.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'paolomedin02@outlook.com'
app.config['MAIL_PASSWORD'] = 'Perrovolador123'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
#app.register_blueprint(user)

mail = Mail(app)


@app.route('/crearCliente', methods = ['POST'])
def add_user():
        body = request.get_json()
        """ try: """
        if 'nombre' in body and 'nit' in body and 'direccion' in body and 'email' in body:
           new_user = User(body['nombre'],body['nit'],body['direccion'],body['email'])
           if data_base_users.add_users(new_user):
               """ ENVIO EMAIL  """
               msg = Message('registro exitoso a soluciones chapinas S.A', sender= 'paolomedin02@outlook.com', recipients=[body['email']])
               msg.body = 'Tu constraseña es: 123'
               mail.send(msg)
               user = data_base_users.get_user(body['nit'])
               user.set_password('123')
               return {'msg': 'Se agregó el usuario correctamente'}, 200
        else:
            return{'msg': 'Faltan datos'}, 400
if __name__ == '__main__':
    app.run(debug=True)

