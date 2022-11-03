
from recursos.db_recursos import db_recursos
class Configuracion:
    def __init__(self, id, nombre, descripcion) -> None:
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.recursos = []
    
    def agregar_recurso(self, id):
        recurso = db_recursos.obtener_recurso(id)
        if recurso != None:
            self.recursos.append(recurso)
            return True
        return False
    
    def agregar_recursos(self, id_recursos):
        for id_recurso in id_recursos:
            for recurso in db_recursos.recursos:
                if id_recurso == recurso.id:
                    recurso_configuracion = db_recursos.obtener_recurso(id_recurso)
                    self.recursos.append(recurso_configuracion)
    
    def recorrer_recurso(self):
        for i in self.recursos:
            print('id ->', i.id)
            print('nombre ->', i.nombre)