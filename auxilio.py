# arquivo secundário para ajudar.

# criando função para controle de senha:
def controle():
    while True:
        try:
            digitos = int(input('Digite quantos dígitos será sua senha (máximo: 8): '))
            if 1 <= digitos <= 8:
                return digitos
            else:
                print('O máximo de dígitos é 8, tente novamente!')
        except:
            print('Valor inválido, Digite um valor inteiro (máximo: 8)')


# criando o gerador de senha:
def gerador(quant_digitos):
    from string import ascii_letters
    from random import choice, randint

    lista_senha = list()
    ultimo_digito = 'numero'
    for contador in range(quant_digitos):
        if ultimo_digito == 'numero':
            tipo = 'letra'
        else:
            tipo = 'numero'

        if tipo == 'letra':    
            sorteio_letras = choice(ascii_letters)
            lista_senha.append(sorteio_letras)
        else:
            sorteio_numeros = str(randint(0,9))
            lista_senha.append(sorteio_numeros)
        ultimo_digito = tipo
    senha_pronta = ''.join(lista_senha)
    return senha_pronta