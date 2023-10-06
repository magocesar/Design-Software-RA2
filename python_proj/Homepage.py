from python_proj.DatabaseScript import Db

class Homepage():
    def getNumberOfClients():
        db = Db()
        result = db.select("cliente", None, None, None, "count(*)")
        return result[0][0]

    def calculateTotalPages():
        numberOfClients = Homepage.getNumberOfClients()
        totalPages = numberOfClients // 20
        if numberOfClients % 20 != 0:
            totalPages += 1
        return totalPages
    
    def selectClientLimit(start, end):
        db = Db()
        result = db.select("cliente", None, None, f"{start - 1}, {end - start}", "id_cliente, nome, cpf, telefone, cep")
        return result
    
    def selectClient(currentPage):
        start = (currentPage - 1) * 20 + 1
        end = start + 20
        return Homepage.selectClientLimit(start, end)

    

    