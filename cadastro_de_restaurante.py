import os


restaurantes = [{'nome':'podrão do robson', 'categoria':'lanche', 'ativo':False },
                {'nome':'Torneira de mijo', 'categoria':'bar', 'ativo':True  },
                {'nome':'Pizza do ronaldo', 'categoria':'pizza', 'ativo':False }
]

def exibir_nome_do_programa():
    '''Exibe o nome do programa'''
    print('''
█████████████████████████████████████████████████████████████████
█─▄▄▄▄██▀▄─██▄─▄─▀█─▄▄─█▄─▄▄▀███▄─▄▄▀█▄─▄█▄─█─▄█▄─▄█▄─▀█▄─▄█─▄▄─█
█▄▄▄▄─██─▀─███─▄─▀█─██─██─▄─▄████─██─██─███▄▀▄███─███─█▄▀─██─██─█
▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▀▀▄▄▄▄▀▄▄▀▄▄▀▀▀▄▄▄▄▀▀▄▄▄▀▀▀▄▀▀▀▄▄▄▀▄▄▄▀▀▄▄▀▄▄▄▄▀''')

def exibir_opcoes():
    '''Essa função exibe as opções do menu'''
    print('\n')
    print(25*'*') 
    print('1- cadastrar restaurante')
    print('2- listar restaurantes')
    print('3- ativar restaurante')
    print('4- Sair')
    print(25*'*') 

def voltar():
     '''Essa função volta para o menu principal '''
     input('\nAperte uma tecla para voltar para o menu principal:   ')
     main()

def finalizar_app():
    '''Essa função finaliza a aplicação'''
    exibir_subtitulos('Adeus!')
    

def opcao_invalida():
    '''Essa função avisa que a opção selecionada é invalida'''
    exibir_subtitulos('opção invalida! Tente novamente')
    main()

def exibir_subtitulos(texto): 
    '''Essa função limpa a tela e exibe um subtitulo para simplificar o codigo'''
    os.system('cls')
    linha = '*' * (len(texto) + 4)
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar():
    '''Essa função cadastra novos restaurantes
    Inputs:
    -Nome do restaurante
    -Categoria

    -Output
    -Adiciona um novo restaurante na lista
    '''
    exibir_subtitulos('cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante para cadastro: ')
    categoria = input(f'Categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria,'ativo':False }
    restaurantes.append(dados_do_restaurante)
    print(f'o restaurante {nome_do_restaurante} foi cadastrado com sucesso!!! \n')
    
    voltar()

def listar_restaurantes():
    '''
    Essa função lista os restaurantes já cadastrados

    '''

    exibir_subtitulos('listando restaurantes \n')

    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(22)} | {'Status'}')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo.ljust(20)}')
    
    voltar()

def altenar_estado_do_restaurante():
    '''
    Essa função altera o estado dos restaurantes entre ativo e desativo
    
    '''
    exibir_subtitulos('Alterando estado do restaurante')

    nome_restaurante = input('Qual restaurante você deseja alterar o estado?')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante ['ativo'] = not restaurante['ativo']
            mensagem = f'O restarante {nome_restaurante} foi ativado com sucesso' if restaurante ['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print('restaurante não encontrado')

    voltar()

    

def escolher_opcoes():
    '''
    Essa função escolhe qual a proxima função será executado

    input: 
    - numero da opçâo escolhida
    
    output:
    -executa todas as funções do codigo
        '''
    
    try:
        opcao_escolhida = int(input('escolha uma opção: '))
        match opcao_escolhida:    
            case 1:
                cadastrar()

            
            case 2:
                listar_restaurantes()

            case 3:
               altenar_estado_do_restaurante()

            case 4: 
                print('finalizar app')
                finalizar_app()

            case _: 
                opcao_invalida()
    except:
        opcao_invalida()      


def main():
    '''
    essa função inicia a aplicação e garante que a aplicação funcione em um loop chamando as funções principais
   
     '''

    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()

if __name__ == '__main__':
    main()
