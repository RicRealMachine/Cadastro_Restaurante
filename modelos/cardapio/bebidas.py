from modelos.cardapio.itens_do_cardapio import ItemCardapio

class Bebidas(ItemCardapio):
    def __init__(self, nome, preco, tamanho):
        super().__init__(nome, preco)
        self.tamanho = tamanho

    def __str__(self):
        return f"{self.nome} - R$ {self.preco} ({self.tamanho})"