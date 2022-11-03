
from configuraciones.db_configuraciones import db_configuraciones
class Instancia:
    def __init__(self, id, nombre, fecha_inicio, fecha_final):
        self.id = id
        self.nombre = nombre
        self.fecha_inicio = fecha_inicio
        self.fecha_final = fecha_final
        self.tiempo_total = 0
        self.configuracion = None
        self.encendido = False
    
    def set_configuracion(self, id_configuracion):
        for configuracion in db_configuraciones.configuraciones:
            if id_configuracion == configuracion.id:
                self.configuracion = configuracion
                return True
        return False