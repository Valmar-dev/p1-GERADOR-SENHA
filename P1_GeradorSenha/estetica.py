# Arquivo para adicionar cores e organizar a estrutura.

# LInhas:S
def linha():
    print('--' * 25)

#cores:
def cores(texto, cor):
    paletas = {
        'preto': f'\033[30m{texto}\033[m',
        'vermelho': f'\033[31m{texto}\033[m',
        'verde': f'\033[32m{texto}\033[m',
        'amarelo': f'\033[33m{texto}\033[m',
        'azul escuro': f'\033[34m{texto}\033[m',
        'roxo': f'\033[35m{texto}\033[m',
        'azul claro': f'\033[36m{texto}\033[m',
    }
    return paletas[cor]

# criando função para gerar títulos:
def titulos(msg):
    print('--' * 25)
    print(msg.center(50))
    print('--' * 25)

# criando menu de opções:
def opicoes(op1, op2):
    print(f'< {op1} >')
    print(f'< {op2} >')
    print('--' * 25)

# criando painel da senha gerada:
def painel(senha, digitos):
    from time import sleep
    import os
    os.system('cls')
    print('--' * 25)
    print(cores(f'GERANDO SENHA DE {digitos} DÍGITOS...', 'amarelo'))
    sleep(3)
    os.system('cls')
    print(cores('SENHA GERADA!', 'verde'))
    sleep(2)
    os.system('cls')
    print('=-' * 25)
    print(cores('SUA SENHA ->', 'azul escuro'), end= '')
    print('[ ', end= '')
    for item in senha:
        print(cores(f'{item} ', 'amarelo'), end= '')
    print(']')
    print('=-' * 25)

