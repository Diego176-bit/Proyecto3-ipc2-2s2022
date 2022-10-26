from flask import Blueprint, request
from flask_mail import Message, Mail
from users.db_users import data_base_users
from users.users_class import User


user = Blueprint('user', __name__, url_prefix='/user')
mail = Mail()


@user.route('/register', methods = ['POST'])
def add_user():
        body = request.get_json()
        """ try: """
        if 'nombre' in body and 'nit' in body and 'direccion' in body and 'email' in body:
           new_user = User(body['nombre'],body['nit'],body['direccion'],body['email'])
           if data_base_users.add_users(new_user):
               """ ENVIO EMAIL  """
               msg = Message('registro exitoso a soluciones chapinas S.A', sender= 'paolomedin02@gmail.com', recipients=[body['email']])
               msg.body = 'Tu constraseña es: 123'
               mail.send(msg)
               return {'msg': 'Se agregó el usuario correctamente'}, 200
        else:
            return{'msg': 'Faltan datos'}, 400
        """ except Exception:
        return {'msg': 'Ocurrio un error en el servidor'}, 500 """
