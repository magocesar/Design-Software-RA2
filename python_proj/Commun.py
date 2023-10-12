from python_proj.DatabaseScript import Db

class Commun():

    #Pagination Functions

    #Calculate the start and end of the query based on the current page
    def calculateStartEnd(currentPage):
        start = (currentPage - 1) * 20 + 1
        end = start + 20
        return start, end
    
    #Calculate the number of pages based on the number of clients
    def calcPages(numberOfClients):
        totalPages = numberOfClients // 20
        if numberOfClients % 20 != 0:
            totalPages += 1
        return totalPages

    #Homepage Functions

    #Get the number of clients
    def getNumberOfClients():
        db = Db()
        result = db.select("cliente", None, None, None, "count(*)")
        return result[0][0]

    #Calculate the number of pages for the homepage
    def calcHomepagePages():
        numberOfClients = Commun.getNumberOfClients()
        return Commun.calcPages(numberOfClients)
    
    #Start the query for the homepage
    def HomepageQueryInit(currentPage):
        start, end = Commun.calculateStartEnd(currentPage)
        return Commun.getHomepageQuery(start, end)
    
    #Get the query for the homepage
    def getHomepageQuery(start, end):
        db = Db()
        result = db.select("cliente", None, None, f"{start - 1}, {end - start}", "id_cliente, nome, cpf, telefone, cep")
        return result
    
    #Search Functions
        
    #Start the query for the search
    def SearchQueryInit(search):
        return Commun.getSearchQuery(search)
    
    #Get the query for the search
    def getSearchQuery(search):
        db = Db()
        result = db.select("cliente", f"nome like '%{search}%' or cpf like '%{search}%' or telefone like '%{search}%' or cep like '%{search}%'", None, f"{0}, {20}", "id_cliente, nome, cpf, telefone, cep")
        return result
    
    