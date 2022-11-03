class DbUsers:
    def __init__(self) -> None:
        self.users = []
        self.nit_users =[]
    def add_users(self, user):
        self.users.append(user)
        return True
    
    def get_user(self, nit):
        for user in self.users:
            if user.get_nit() == nit:
                return user
        return None

    def get_user_sesion(self, user_name, password):
        for user in self.users:
            if user_name == user.user_name and user.password == password:
                return user
        return None

data_base_users = DbUsers() 