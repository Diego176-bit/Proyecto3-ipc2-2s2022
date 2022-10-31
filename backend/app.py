from flask import Flask, request
from flask_mail import Mail, Message
from users.db_users import data_base_users
from users.users_class import User
from instancias.instancia_class import Instancia
from recursos.recursos_route import recursos
from configuraciones.configuraciones_route import configuraciones
from categorias.categorias_route import categorias
app = Flask(__name__)



""" CLIENTE """
app.config['MAIL_SERVER'] = 'smtp.office365.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'paolomedin02@outlook.com'
app.config['MAIL_PASSWORD'] = 'Perrovolador123'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)

@app.route('/crearInstancia', methods=['POST'])
def crear_instancia():
    body = request.get_json()
    if 'nit_usuario' in body and 'id_isntancia' in body and 'id_configuracion' in body:
        usuario = data_base_users.get_user(body['nit_usuario'])
        if usuario != None:
            instancia = Instancia(body['id_instancia'])
            if instancia.set_configuracion(body['id_configuracion']):
                usuario.agregar_instancia(instancia)
                return {'msg': 'indtancia creada con exito'}, 200
            else: return {'msg': 'la configuracion no existe'},400
        else: return {'msg': 'el usuario no existe'},400
            




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

app.register_blueprint(recursos)
app.register_blueprint(configuraciones)
app.register_blueprint(categorias)
if __name__ == '__main__':
    app.run(debug=True)

