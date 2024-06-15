from modelos.avaliacao import Avaliacao

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._status = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self._categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        print('Nome do Restaurante'.ljust(21) + '|' + ' Categoria do Restaurante'.ljust(21) + '|' + ' Status do Restaurante'.ljust(21))
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(20)} | {restaurante._categoria.ljust(23)} | {restaurante.status.ljust(20)}')

    @property
    def status(self):
        return '✔️' if self._status else '❌'
    
    def alternar_estado(self):
        self._status = not self._status

    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)