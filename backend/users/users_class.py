class User:
    def __init__(self,nombre, nit, direccion,email) -> None:
        self.nombre = nombre
        self.nit = nit
        self.direccion = direccion
        self.email = email
        self.password = None
        self.user_name = None
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
    
    def set_user_name(self, user_name):
        self.user_name = user_name
            
    def agregar_instancia(self, instancia):
        if not instancia.id in self.instancia_id:
            self.instancias.append(instancia)
            self.instancia_id.append(instancia.id)
            return True
        return False
    def calcular_factura_instancia(self, id_instancia):
        total_factura = 0
        cadena = ''
        file = open(f'reporte-instancia-{id_instancia}.txt', 'w')
        for instancia in self.instancias:
            if instancia.id == id_instancia:
                cadena += f'TIEMPO EMPLEADO: {instancia.tiempo_total} DIAS\n\n'
                configuracion = instancia.configuracion
                for recurso in configuracion.recursos:
                    
                    cadena += f'RECURSO ID: {recurso.id} ------- {recurso.valor_hora}/h \n'
                    total_factura += float(recurso.valor_hora)*float(instancia.tiempo_total*24)
        
        cadena += f'--------------------------------------------------------------------------------------------\n total: {total_factura}'
        file.write(cadena)
        file.close()
        
    def listar_instancias(self):
        for instancia in self.instancias:
            
            print(f'instancia id: {instancia.id}.\n instancia nombre: {instancia.nombre}.\n\n')