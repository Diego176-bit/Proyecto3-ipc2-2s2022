
from configuraciones.db_configuraciones import db_configuraciones
class Categoria:
    def __init__(self, id, nombre, descripcion, carga_trabajo):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.carga_trabajo = carga_trabajo
        self.configuraciones = []
    
    def agregar_configuracion(self, id) -> bool:
        configuracion = db_configuraciones.obtener_configuracion(id)
        if configuracion != None:
            self.configuraciones.appende(configuracion)
            return True
        return False

    def agregar_configuracion(self, id_configuraciones):
        for id_configuracion in id_configuraciones:
            for configuracion in db_configuraciones.configuraciones:
                if id_configuracion == configuracion.id:
                    configuracion_categoria = db_configuraciones.obtener_configuracion(id_configuracion)
                    self.configuraciones.append(configuracion_categoria)