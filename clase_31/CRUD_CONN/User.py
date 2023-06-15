class User:
    def __init__(self,**kwargs):
        self.nombre = kwargs.get("nombre","unknown")
        self.email = kwargs.get("email","no-email@mail.com")
        self.password = kwargs.get("password","passwd")

    def returned_dict(self):
        return{
            nombre : self.nombre,
            email : self.email,
            edad: self.password
        }