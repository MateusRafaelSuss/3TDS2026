class Ciente:
    def __init__(self, cpf:str, nome:str, cnh:str):
        self.cpf = cpf
        self.nome = nome
        self.cnh = cnh  
        
    def exibir_dados(self):
        return f'Nome: {self.nome} \n CPF: {self.cpf} \n CNH: {self.cnh}'
        