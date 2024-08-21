# arquivo secundário para ajudar.

# criando função para controle de senha:
def controle():
    from estetica import linha, cores
    from time import sleep
    import os
    while True:
        os.system('cls')
        try:
            linha()
            digitos = int(input(cores('Digite quantos dígitos será sua senha (máximo: 20): ', 'amarelo')))
            if 1 <= digitos <= 20:
                return digitos
            else:
                os.system('cls')
                linha()
                print(cores('Você deve digitar um valor entre 1 e 20!', 'vermelho'))
                sleep(3)
                os.system('cls')
        except:
            os.system('cls')
            linha()
            print(cores('Valor inválido, Digite um valor inteiro (máximo: 20)', 'vermelho'))
            sleep(3)
            os.system('cls')


# criando o gerador de senha:
def gerador(quant_digitos):
    from string import ascii_letters
    from random import choice, randint

    lista_simbolos = ['!', '@', '#', '$', '%', '&']
    lista_senha = list()
    ultimo_digito = 'numero'
    for contador in range(quant_digitos):
        if ultimo_digito == 'numero':
            tipo = 'letra'
        elif ultimo_digito == 'letra':
            tipo = 'simbolo'
        else:
            tipo = 'numero'

        if tipo == 'letra':    
            sorteio_letras = choice(ascii_letters)
            lista_senha.append(sorteio_letras)
        elif tipo == 'simbolo':
            sorteio_simbolos = choice(lista_simbolos)
            lista_senha.append(sorteio_simbolos)
        else:
            sorteio_numeros = str(randint(0,9))
            lista_senha.append(sorteio_numeros)
        ultimo_digito = tipo
    senha_pronta = ''.join(lista_senha)
    return senha_pronta


def validar():
    from estetica import linha, cores, titulos, opicoes
    import os
    from time import sleep
    while True:
        try:
            resposta = int(input(cores('Escolha uma das opções acima [1/2]: ', 'amarelo')))
            if resposta != 1 and resposta != 2:
                os.system('cls')
                print(cores('Erro, digite apenas 1 ou 2', 'vermelho'))
                sleep(3)
                os.system('cls')
                titulos(cores("GERADOR DE SENHA AUTOMÁTICA", 'amarelo'))
                opicoes(cores('DIGITE \033[33m[1]\033[m \033[36mPARA GERAR UMA SENHA\033[m', 'azul claro'), cores('DIGITE \033[33m[2]\033[m \033[36mPARA FECHAR PROGRAMA\033[m', 'azul claro'))

            else:
                return resposta 
        except:
            os.system('cls')
            print(cores('Resposta inválida, digite 1 ou 2', 'vermelho'))
            sleep(3)
            os.system('cls')
            titulos(cores("GERADOR DE SENHA AUTOMÁTICA", 'amarelo'))
            opicoes(cores('DIGITE \033[33m[1]\033[m \033[36mPARA GERAR UMA SENHA\033[m', 'azul claro'), cores('DIGITE \033[33m[2]\033[m \033[36mPARA FECHAR PROGRAMA\033[m', 'azul claro'))