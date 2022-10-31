from flask import Blueprint, request
from categorias.categoria_class import Categoria
from categorias.db_categorias import db_categorias
categorias = Blueprint('categorias', __name__, url_prefix='/categorias')

@categorias.route('/crearCategoria', methods= ['POST'])
def crear_categoria():
    body = request.get_json()
    
    if 'id' in body and 'configuraciones' in body:
        categoria = Categoria(body['id'])
        categoria.agregar_configuracion(body['configuraciones'])
        if db_categorias.agregar_categoria(categoria):
            
            return {'msg': 'categoria agregada con exito'}, 200
        
            
    else:
        return {'msg': 'Faltan datos para crear la configuracion'}, 400