import os

restaurantes =  [{'nome':'Praça', 'categoria':'Japonesa', 'ativo':False},
                {'nome':'Pizza', 'categoria':'Italiana', 'ativo':True},
                {'nome':'Dogs', 'categoria':'Rua', 'ativo':False}]

def nome_prog():
    os.system('cls')
    print('𝑆𝑎𝑏𝑜𝑟 𝐸𝑥𝑝𝑟𝑒𝑠𝑠\n')

def menu():
    print('Menu:\n1. Cadastrar restaurante\n2. Listar resutarantes\n3. Ativar restaurante\n4. Sair\n')

def cadastro_rest():
    os.system('cls')
    print('Cadastro de novos restaurantes\n')

    nome_rest = input('Digite o nome do restaurante que deseja adicionar: ')
    categ_rest = input(f'Digite a categoria do restaurante {nome_rest}: ')

    dados_rest = {'nome':nome_rest,'categoria':categ_rest,'ativo':False}
    restaurantes.append(dados_rest)

    print(f'\n{dados_rest}\nO restaurante foi adicionado com sucesso!\n')

    input('Digite qualquer tecla para retornar ao menu principal')
    main()

def lista_rest():
    os.system('cls')
    print(f'Restaurantes cadastrados: \n')

    for restaurante in restaurantes:
        nome_rest = restaurante['nome']
        categ_rest = restaurante['categoria']
        atv_rest = 'Ativado' if restaurante['ativo'] else 'Desativado'
        print(f'* {nome_rest} | {categ_rest} | {atv_rest}')

    input('Pressione qualquer tecla para continuar')
    main()

def alt_rest():
    nome_rest = input('Digite o nome do restaurante que deseja alterar o estado: ')
    rest_encontrado = False

    for restaurante in restaurantes:
        if nome_rest == restaurante['nome']:
            rest_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = (f'O restaurante {nome_rest} foi ativado com sucesso!') if restaurante['ativo'] else f'O restaurante {nome_rest} foi desativado com sucesso!'

            print(mensagem)
            input('')

        if not rest_encontrado:
            print(f'O restaurante {nome_rest} não foi encontrado')


    main()

def opc():
    opc_escolhida = input('Escolha uma opção: ')    

    match opc_escolhida:
        case '1':
            cadastro_rest()
        case '2':
            lista_rest()
        case '3':
            alt_rest()
        case '4':
            finalizar_app()
        case _:
            os.system('cls')
            print(f'Opção {opc_escolhida} inválida\n')
            menu()
            opc()

def finalizar_app():
    os.system('cls')
    print('Finalizando o app!\n')


def main():
    nome_prog()
    menu()
    opc()


if __name__ == '__main__':
    main()