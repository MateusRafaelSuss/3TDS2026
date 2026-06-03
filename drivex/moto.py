from veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, cilindradas: int):
        self.cilindradas = cilindradas
        
    def exibir_dados(self):
        return f'Placa: {self.placa}\n Marca: {self.marca} \n Cilindradas: {self.cilindradas} Valor da Diária: {self.valor_diaria}  \n Está Disponivel? {self.disponivel} '
        