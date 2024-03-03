from modelos.restaurante import Restaurante
from modelos.cardapio.bebidas import Bebidas
from modelos.cardapio.prato import Prato

restaurante_japones = Restaurante('JapaJá', 'Japonês' )
bebida_suco = Bebidas('Suco de manga', 5.6, 'pequeno')
prato_arroz = Prato('Arroz Japones', 30, 'arroz grudadinho para comer com hashi' )
restaurante_japones.adicionar_cardapio(bebida_suco)
restaurante_japones.adicionar_cardapio(prato_arroz)


def main():
     print(prato_arroz)
     print(bebida_suco)

if __name__ == '__main__':
    main()