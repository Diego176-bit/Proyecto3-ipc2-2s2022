from flask import Blueprint, request
from xml.etree import ElementTree as ET
from datetime import datetime
from recursos.recurso_class import Recurso
from recursos.db_recursos import db_recursos

from categorias.categoria_class import Categoria
from categorias.db_categorias import db_categorias

from configuraciones.configuracion_class import Configuracion
from configuraciones.db_configuraciones import db_configuraciones

from users.users_class import User
from users.db_users import data_base_users

from instancias.instancia_class import Instancia
xml_file = Blueprint('xml_file', __name__, url_prefix='/xml')
@xml_file.route('/xmlEntrada', methods = ['POST'])
def xml():
    """  content = xmltodict.parse(request.get_data())
        
        
        recursos = content.get('archivoConfiguraciones').get('listaRecursos').get('recurso') """
    xml = request.data.decode('utf-8')
    xml_file = ET.XML(xml)
    
    for lista_recursos in xml_file.findall('listaRecursos'):
           lista_recurso = lista_recursos.findall('recurso')
           for recurso in lista_recurso:
               id_recurso = recurso.get('id')
               nombre_recurso = recurso.find('nombre').text
               abreviatura = recurso.find('abreviatura').text
               metrica = recurso.find('metrica').text
               tipo = recurso.find('tipo').text
               valor_hora = recurso.find('valorXhora').text
               nuevo_recurso = Recurso(id_recurso, nombre_recurso,abreviatura, metrica, tipo, valor_hora)
               db_recursos.agregar_recurso(nuevo_recurso)
    
    
    for lista_categorias in xml_file.findall('listaCategorias'):
        lista_categoria = lista_categorias.findall('categoria')
        for categoria in lista_categoria:
            id_cat = categoria.get('id')
            nombre_cat = categoria.find('nombre').text
            descripcion_cat = categoria.find('descripcion').text
            carga_trabajo = categoria.find('cargaTrabajo').text
            
            nueva_categoria = Categoria(id_cat, nombre_cat, descripcion_cat, carga_trabajo)
            
            for lista_configuraciones in categoria.findall('listaConfiguraciones'):
                lista_configuracion = lista_configuraciones.findall('configuracion')
                for configuracion in lista_configuracion:
                    id_config = configuracion.get('id')
                    nombre_config = configuracion.find('nombre').text
                    descripcion_config = configuracion.find('descripcion').text
                    nueva_configuracion = Configuracion(id_config, nombre_config, descripcion_config)
                    
                    for lista_recursos_config in configuracion.findall('recursosConfiguracion'):
                        recursos_config = lista_recursos_config.findall('recurso')
                        for recurso_config in recursos_config:
                            id_recurso_config = recurso_config.get('id')
                            cantidad = recurso_config.text
                            nueva_configuracion.agregar_recurso(id_recurso_config)
                    
                    db_configuraciones.agregar_configuracion(nueva_configuracion)
                    nueva_categoria.agregar_configuracion(id_config)
            
            db_categorias.agregar_categoria(nueva_categoria)
    
    for lista_clientes in xml_file.findall('listaClientes'):
        clientes = lista_clientes.findall('cliente')
        for cliente in clientes:
            nit = cliente.get('nit')
            nombre_cliente = cliente.find('nombre').text
            usuario = cliente.find('usuario').text
            password = cliente.find('clave').text
            direccion = cliente.find('direccion').text
            email = cliente.find('correoElectronico').text
            
            nuevo_cliente = User(nombre_cliente, nit, direccion, email)
            nuevo_cliente.set_user_name(usuario)
            nuevo_cliente.set_password(password)
            
            for lista_instancias in cliente.findall('listaInstancias'):
                instancias = lista_instancias.findall('instancia')
                for instancia in instancias:
                    id_instancia = instancia.get('id')
                    id_config = instancia.find('idConfiguracion').text
                    nombre_instancia = instancia.find('nombre').text
                    estado = instancia.find('estado').text
                    fecha_inicio_str = instancia.find('fechaInicio').text
                    fecha_inicio = datetime.strptime(fecha_inicio_str, '%d-%m-%Y')
                    fecha_final_str = instancia.find('fechaFinal').text
                    fecha_final = datetime.strptime(fecha_final_str, '%d-%m-%Y')
                    nueva_instancia = Instancia(id_instancia, nombre_instancia, fecha_inicio, fecha_final)
                    nueva_instancia.set_configuracion(id_config)
                    tiempo_total = fecha_final - fecha_inicio
                    nueva_instancia.tiempo_total = tiempo_total.days
                    
                    if estado == 'VIGENTE':
                        nueva_instancia.encendido = True
                    
                    nuevo_cliente.agregar_instancia(nueva_instancia)
            data_base_users.add_users(nuevo_cliente)
    
    
    
    return {'msg': 'archivo cargado'},200
    