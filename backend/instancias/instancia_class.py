
from configuraciones.db_configuraciones import db_configuraciones
class Instancia:
    def __init__(self, id):
        self.id = id
        self.configuracion = None
        self.encendido = False
    
    def set_configuracion(self, id_configuracion):
        for configuracion in db_configuraciones.configuraciones:
            if id_configuracion == configuracion.id:
                self.configuracion = configuracion
                return True
        return False