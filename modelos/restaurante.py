from modelos.nota import Avaliacao
from modelos.cardapio.itens_do_cardapio import ItemCardapio

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao =[]
        self._cardapio = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self._categoria}' 

    @classmethod
    def listar_restaurantes(cls):
        print('Nome do restaurante'.ljust(25) + 'categoria'.ljust(25) + 'Avaliação'.ljust(25) +'Status')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome}'.ljust(25) + f'{restaurante._categoria}'.ljust(25) + f'{str(restaurante.media_avaliacoes)}'.ljust(25) + f'{restaurante.ativo}' )


    @property
    def ativo(self):
        return '✔' if self._ativo else '❌'

    def alternar_estado(self):
        self._ativo = not self._ativo
          
    def receber_avaliacao(self, cliente, nota):
        if 0 < nota <=5: 
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return '-'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media

 
    @property
    def adicionar_cardapio(self,item):
        if isinstance(item,ItemCardapio):
            self._cardapio.append(item)
    
    def exibir_cardapio(self):
        print(f'cardapio do restaurante{self._nome}\n')
        for i, item in enumerate(self._cardapio, start=1):
            if hasattr(item,'descrição'):
                mensagem_prato = f'{i}. Nome: {item._nome} | Preço R${item._preco} | Descrição {item._descricao}'
                print(mensagem_prato)
            else:
                mensagem_bebida = f'{i}. Nome: {item._nome} | Preço R${item._preco} | Tamanho: {item._tamanho}'
                print(mensagem_bebida)

restaurante_japones = Restaurante('Lamen do tio', 'Japonesa')
    