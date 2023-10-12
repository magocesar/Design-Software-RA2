from python_proj.DatabaseScript import Db

class Login:
    def __init__(self, login, senha):
        self.login = login
        self.senha = senha

        if self.getFromBd():
            self.autenticado = True
        else:
            self.autenticado = False

    def getFromBd(self):
        db = Db()
        result = db.select("adm", f"login = '{self.login}'")
        if result != []:
            if result[0][2] == self.senha:
                self.id = result[0][0]
                return True
            else:
                return False
        else:
            return False
        
    def getAutenticado(self):
        return self.autenticado
    
l = Login("adm@123", "123")
print(l.getAutenticado())