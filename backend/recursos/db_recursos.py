
class DbRecursos:
    def __init__(self):
        self.recursos = []
        self.id_recurso = []
    
    def agregar_recurso(self,recurso) -> bool:
        if not recurso.id in self.id_recurso:
            self.recursos.append(recurso)
            self.id_recurso.append(recurso.id)
            return True
        else:
            return False
    
    def obtener_recurso(self,id) -> object:
        for recurso in self.recursos:
            if id == recurso.id:
                return recurso
        return None


db_recursos = DbRecursos()