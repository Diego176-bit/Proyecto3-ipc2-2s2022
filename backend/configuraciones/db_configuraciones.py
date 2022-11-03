class DbConfiguraciones:
    def __init__(self):
        self.configuraciones = []
        self.id = []
    
    def agregar_configuracion(self, configuracion):
        if not configuracion.id in self.id:
            self.configuraciones.append(configuracion)
            self.id.append(configuracion.id)
            return True
        return False
    
    def obtener_configuracion(self, id):
        for configuracion in self.configuraciones:
            if configuracion.id == id:
                return configuracion
        return None    
    def listar_configuraciones(self):
        for i in self.configuraciones:
            print(f'id: {i.id} nombre: {i.nombre}')
db_configuraciones = DbConfiguraciones()