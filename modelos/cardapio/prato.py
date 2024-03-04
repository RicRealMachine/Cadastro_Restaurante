from modelos.cardapio.itens_do_cardapio import ItemCardapio

class Prato(ItemCardapio):
    def __init__(self, nome , preco, descricao):
        super().__init__(nome, preco)
        self._descricao = descricao
    
    def __str__(self):
      return f"{self._nome} - R$ {self._preco} ({self._descricao})"