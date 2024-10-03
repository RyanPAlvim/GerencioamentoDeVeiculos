from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self, nome: str, ano:int, valor_diaria: float):
        self.nome = nome
        self.ano = ano
        self.valor_diaria = valor_diaria

    @abstractmethod
    def calcular_valor_aluguel(self, dias: int):
        ...

class Carro(Veiculo):
    
    def calcular_valor_aluguel(self, dias: int):
        total = self.valor_diaria * dias 
        if dias > 7:
            return total - (total * 5/100)
        return total

class Moto(Veiculo):

    def calcular_valor_aluguel(self, dias: int):
        return self.valor_diaria * dias