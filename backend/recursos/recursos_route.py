from flask import Blueprint, request
from recursos.recurso_class import Recurso
from recursos.db_recursos import db_recursos

recursos = Blueprint('recursos', __name__, url_prefix='/recurso')

@recursos.route('/crearRecurso', methods=['POST'])
def crear_recurso():
    body = request.get_json()
    try:
        if 'id' in body and 'nombre' in body and 'abreviatura' in body and 'metrica' in body and 'tipo' in body and 'valor_hora' in body:
            nuevo_recurso = Recurso(body['id'], body['nombre'], body['abreviatura'], body['metrica'], body['tipo'], body['valor_hora'])
            if db_recursos.agregar_recurso(nuevo_recurso):
                return {'msg': 'Recurso agregado con exito'}, 200
            else:
                return {'msg': 'Recurso ya existente'}, 400
        else:
            return {'msg': 'Faltan datos para crear el recurso'}, 400
    except:
        return {'msg': 'error en el servidor'}, 500