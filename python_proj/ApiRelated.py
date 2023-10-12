import requests, json

class ViaCepApi:
    def __init__(self, cep):
        self.cep = cep
        self.url = f'https://viacep.com.br/ws/{self.cep}/json/'

    def getJson(self):
        return requests.get(self.url).json()
    
class AdapterCepJsonToDict:
    def __init__(self, cep):
        self.cep = cep

    def getDict(self):
        aux = ViaCepApi(self.cep).getJson()
        aux_dict = json.loads(json.dumps(aux))
        return aux_dict
        
class Cep:
    def __init__(self, cep):
        self.cep = cep
        self.dict = AdapterCepJsonToDict(self.cep).getDict()
    
    def getInfo(self):
        return self.dict
    