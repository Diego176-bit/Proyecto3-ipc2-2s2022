class User:
    def __init__(self,nombre, nit, direccion,email) -> None:
        self.nombre = nombre
        self.nit = nit
        self.direccion = direccion
        self.email = email
        self.password = None
        self.instancias = []
        self.instancia_id = []
        


    def get_nombre(self):
        return self.nombre

    def get_nit(self):
        return self.nit

    def get_direccion(self):
        return self.direccion

    def get_email(self):
        return self.email
    
    def set_nombre(self, nombre):
        self.nombre = nombre
    
    def set_nombre(self, nit):
        self.nit = nit
    
    def set_password(self, password):
        self.password = password
    
    def agregar_instancia(self, instancia):
        if not instancia.id in self.instancia_id:
            self.instancias.append(instancia)
            self.instancia_id.append(instancia.id)
            return True
        return False