class DbCategorias:
    def __init__(self) -> None:
        self.categorias = []
        self.id = []
    
    def agregar_categoria(self, categoria) -> bool:
        if not categoria.id in self.id:
            self.categorias.append(categoria)
            self.id.append(categoria.id)
            return True
        return False
