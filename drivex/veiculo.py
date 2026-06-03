from typing import List, Dict
from db import VEICULOS, CLIENTES, LOCACOES


class Veiculo:
    def __init__(self, placa: str, marca: str, valor_diaria: float, disponivel: bool = True ):
        self.placa = placa,
        self.marca = marca,
        self.valor_diaria = valor_diaria,
        self.disponivel= disponivel
    @classmethod
    def buscar_por_placa(cls, placa):
        for veiculo in VEICULOS:
            if veiculo.placa == placa:
                return veiculo
            return None
        
    def exibir_dados(self):
        return f'Placa: {self.placa}\n Marca: {self.marca} \n Valor da Diária: {self.valor_diaria}  \n Está Disponivel? {self.disponivel}'
    
    @classmethod
    def cadastrar_veiculo(cls, placa, marca, valor_diaria, disponivel):
        print('CADASTRAR VEICULO:')
        tipo = input('Digite 1 para Carro \n Digite 2 para Moto')
        if tipo == 1:
            placa = input('Digite a placa:')
            marca = input("Digite a marca:")
            valor_diaria = input("Digite o Valor da Diária:")
            disponivel = input('Está disponivel?')