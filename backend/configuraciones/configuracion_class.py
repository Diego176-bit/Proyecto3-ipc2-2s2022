
from recursos.db_recursos import db_recursos
class Configuracion:
    def __init__(self, id) -> None:
        self.id = id
        self.recursos = []
    
    def agregar_recurso(self, id):
        recurso = db_recursos.obtener_recurso(id)
        if recurso != None:
            self.recursos.append(recurso)
            return True
        return False