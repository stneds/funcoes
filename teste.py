import os
restaurantes = [{'nome':'Praça','categoria':'Japonesa','ativo':False},
                {'nome':'Pizza Suprema', 'categoria':'Italiana','ativo':True},
                {'nome':'Cantina','categoria':'Italiano','ativo':False}]
def exibir_nome():
    '''Essa função é responsável por exibir a logo do restaurante '''
    print('Sabor express\n\n')
def exibir_opc():
    '''Essa função é responsável por exibir as opções de escolha'''
    print('1.Cadastrar restaurante')
    print('2.Listar restaurante')
    print('3.Ativar restaurante')
    print('4.Sair\n')

def finalizar():
    '''Essa função é responsável por finalizar o sistema'''
    os.system('cls')
    print('Finalizando app...\n\n')

def menu():
    '''Essa função é responsável por voltar ao menu'''
    input('Digite qualquer tecla para retornar ao menu ')
    main()

def sub(texto):
    '''Essa função é responsável por exibir um subtitulo '''
    os.system('cls')
    print(texto)
    print('')


def invalida():
    '''Essa função é responsável por informar que a opção escolhida foi invalida'''
    print('Opcção inválida!!\n')
    menu()

def cadastrar_restaurante():
    '''Essa função é responsável por cadastar um novo restaurante'''
    sub('Cadastro de novos restuarantes\n')
    nome_do_restaurante= input('Informe o nome do restaurante que deseja cadastrar:')
    categoria= input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}:')
    dados_do_restaurante= {'nome':nome_do_restaurante,'categoria':categoria, 'ativo':False}
    restaurantes.append(nome_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado!!')
    menu()

def listar_restaurante():
    '''Essa função é responsável por listar um restaurante'''
    sub('Os restaurantes disponíveis são:')
    for i in restaurantes:
        nome_restaurante= i ['nome']
        categoria=i['categoria']
        ativo=i['ativo']
        print(f'- { nome_restaurante} | {categoria} | {ativo}')


def alternar_estado():
    '''Essa função é responsável por alterar o estado de um restaurante'''
    sub('Alterando estado do restaurante') 
    nome_restaurante= input('Digite o nome do restaurante que deseja alterar o estado:')
    restaurante_encontrado= False
    for restaurante in restaurantes:
     if nome_restaurante == restaurante['nome']:
        restaurante_encontrado = True
        restaurante['ativo'] = not restaurante['ativo']
        mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
        print(mensagem)

    if not restaurante_encontrado:
     print('O restaurante não foi encontrado.')
           
def escolher_opc():
     
    try:
         
        opc=int(input('Escolha uma das opções acima:'))

        def finalizar():
            os.system('cls')
            print('Finalizando app...\n\n')
        if opc == 1 :
            cadastrar_restaurante()
        elif opc==2:
            listar_restaurante()
        elif opc==3:
            alternar_estado()
        elif opc==4:
            finalizar()
        else:
            invalida()
    except:
        invalida()
def main():
    '''Essa função é responsável por retornar ao menu inicial '''
    os.system('cls')
    exibir_nome()
    exibir_opc()
    escolher_opc()

if __name__ == '__main__':
    main()



