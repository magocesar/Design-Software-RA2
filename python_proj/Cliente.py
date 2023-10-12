from python_proj.DatabaseScript import Db
from python_proj.ApiRelated import Cep

class Cliente:

    def __init__(self, id, nome, cpf, telefone, cep, numero, complemento):
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.cep = cep
        self.numero = numero
        self.complemento = complemento

    def getFromId(id):
        db = Db()
        result = db.select("cliente", f"id_cliente = {id}", None, None, "id_cliente, nome, cpf, telefone, cep, numero, complemento")
        nome = result[0][1]
        cpf = result[0][2]
        telefone = result[0][3]
        cep = Cep(result[0][4]).getInfo()
        numero = result[0][5]
        complemento = result[0][6]

        return Cliente(id, nome, cpf, telefone, cep, numero, complemento)
