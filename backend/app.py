
from flask import Flask, request
from flask_mail import Mail, Message
from users.db_users import data_base_users
from users.users_class import User
from instancias.instancia_class import Instancia
from recursos.recursos_route import recursos
from configuraciones.configuraciones_route import configuraciones
from configuraciones.db_configuraciones import db_configuraciones
from categorias.categorias_route import categorias
from xml_file.xml_route import xml_file
from datetime import datetime
usuario_actual = None
app = Flask(__name__)



""" CLIENTE """
app.config['MAIL_SERVER'] = 'smtp.office365.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'paolomedin02@outlook.com'
app.config['MAIL_PASSWORD'] = 'Perrovolador123'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)
@app.route('/', methods = ['POST'])
def inicio_sesion():
    global usuario_actual
    body = request.get_json()
    if 'user_name' in body and 'password' in body:
        usuario_actual = data_base_users.get_user_sesion(body['user_name'], body['password'])
        if usuario_actual != None:
            print('')
            print('-----------------------------------------')
            print(f'Bienvenido {usuario_actual.nombre} ')
            
            while True:
                print('1. crear instancia.')
                print('2. modificar instancia')
                print('3. eliminar instancia')
                print('4. listar instancias')
                print('5. genrar factura instancia')
                
                opcion = input('elige una opcion: ')
                if opcion == '1':
                    db_configuraciones.listar_configuraciones()
                    configuracion_id = input('seleccione el id de la configuracion: ')
                   
                    id_instancia = input('ingresa el id de la instancia: ')
                    nombre_instancia = input('ingresa el nombre de la instancia: ')
                    fecha_inicio_str = input('ingresa la fecha inicio de la instancia: ')
                    fecha_final_str = input('ingresa la fecha final de la instancia: ')
                    fecha_inicio = datetime.strptime(fecha_inicio_str, '%d/%m/%Y')
                    fecha_final = datetime.strptime(fecha_final_str, '%d/%m/%Y')
                    total_tiempo = fecha_final -fecha_inicio
                    
                    nueva_instancia = Instancia(id_instancia, nombre_instancia, fecha_inicio, fecha_final)
                    nueva_instancia.tiempo_total = total_tiempo.days
                    print('1.instancia Vigente')
                    print('2. instancia Cancelada')
                    vigencia = input(' escoge una opcion de vigencia: ')
                    if vigencia == '1':
                        nueva_instancia.encendido = True
                    elif vigencia == '2':
                        nueva_instancia.encendido = False
                    nueva_instancia.set_configuracion(configuracion_id)
                    usuario_actual.agregar_instancia(nueva_instancia)
                if opcion == '4':
                    usuario_actual.listar_instancias()
                if opcion == '5':
                    print('')
                    print('#############################')
                    print('genrear factura')
                    id_instancia = input('cual es el id de la instancia: ')
                    print('#############################')
                    print('')
                    print('')
                    usuario_actual.calcular_factura_instancia(id_instancia)
                if opcion == '6':
                    break
            print('-----------------------------------------')
            
            return {'msg': 'inicio de sesion exitoso'},200
        else:
            return {'msg': 'inicio de sesion fallido'},400

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
               user = data_base_users.get_user(body['nit'])
               user_name = body['nombre'].strip().lower()+ body['nit'][0:3]
               user.set_user_name(user_name)
               user.set_password('123')
               """ ENVIO EMAIL  """
               msg = Message('registro exitoso a soluciones chapinas S.A', sender= 'paolomedin02@outlook.com', recipients=[body['email']])
               msg.body = f'Tu usuario es: {user_name} \n Tu constraseña es: 123'
               mail.send(msg)
               
               
               return {'msg': 'Se agregó el usuario correctamente'}, 200
        else:
            return{'msg': 'Faltan datos'}, 400
@app.route('/consultarDatos', methods=['GET'])
def consultar_datos():
    global usuario_actual
    return {
            'nombre': usuario_actual.nombre,
            'nit': usuario_actual.nit,
            'instancias':usuario_actual.instancias
            }





""" Bluepints """
app.register_blueprint(recursos)
app.register_blueprint(configuraciones)
app.register_blueprint(categorias)
app.register_blueprint(xml_file)
if __name__ == '__main__':
    app.run(debug=True)

