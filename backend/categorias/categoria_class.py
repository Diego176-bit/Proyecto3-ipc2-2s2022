
from configuraciones.db_configuraciones import db_configuraciones
class Categoria:
    def __init__(self, id):
        self.id = id
        self.configuraciones = []
    
    def agregar_configuracion(self, id) -> bool:
        configuracion = db_configuraciones.obtener_configuracion(id)
        if configuracion != None:
            self.configuraciones.appende(configuracion)
            return True
        return False