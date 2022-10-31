
from flask import Blueprint, request
from configuraciones.configuracion_class import Configuracion
from configuraciones.db_configuraciones import db_configuraciones

configuraciones = Blueprint('configuraciones', __name__, url_prefix='/configuraciones')

@configuraciones.route('/crearConfiguracion', methods= ['POST'])
def agregar_configuracion():
    body = request.get_json()
    
    if 'id' in body and 'recursos' in body:
        configuracion = Configuracion(body['id'])
        configuracion.agregar_recursos(body['recursos'])
        if db_configuraciones.agregar_configuracion(configuracion):
            configuracion.recorrer_recurso()
            return {'msg': 'configuracion agregada con exito'}, 200
        
            
    else:
        return {'msg': 'Faltan datos para crear la configuracion'}, 400
    