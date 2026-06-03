from veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, categoria: str):
        self.categoria = categoria
        
    def exibir_dados(self):
        return f' Categoria: {self.categoria} \n Placa: {self.placa}\n Marca: {self.marca} \n Valor da Diária: {self.valor_diaria}  \n Está Disponivel? {self.disponivel} '
        