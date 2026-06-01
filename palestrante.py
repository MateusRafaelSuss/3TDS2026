from decimal import Decimal
from typing import List, Dict
class Palestrante:
    def __init__(self, nome:str, idade:str, curriculo:str, especialidade:str, custo:Decimal):
        self.nome = nome
        self.idade = idade
        self.curriculo = curriculo
        self.especialidade = especialidade
        self.custo = custo
        
    def __repr__(self):
        return f'{self.nome}, {self.idade}, {self.curriculo}, {self.especialidade}, {self.custo}'
        
    @classmethod
    def create_palestrante(cls, data: Dict):
        return cls(
            nome = data['nome'],
            idade = data['idade'],
            curriculo = data['curriculo'],
            especialidade = data['especialidade'],
            custo = data['custo']
        )
        
        