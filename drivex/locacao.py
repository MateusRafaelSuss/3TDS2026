from cliente import Cliente
from veiculo import Veiculo
class Locacao:
    def __init__(self, cliente: Cliente, veiculo: Veiculo, quantidade_dias: int):
        self.cliente = cliente
        self.veiculo = veiculo
        self.quantidade_dias = quantidade_dias
        
    def calcular_preco(self):
        return self.quantidade_dias * self.veiculo.valor_diaria
    
    def exibir_dados(self):
        return f'Cleinte: {self.cliente} \n Veiculo: {self.veiculo} \n Quantidade de Dias: {self.quantidade_dias}'
        
    