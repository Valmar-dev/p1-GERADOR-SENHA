#  Arquivo principal do gerador de senha

import auxilio as ax
import estetica as es

# Construindo um painel pra usuário:
es.titulos(es.cores("GERADOR DE SENHA AUTOMÁICA", 'amarelo'))

while True:
    # Construindo o menu de opções:
    es.opicoes(es.cores('DIGITE \033[33m[1]\033[m \033[36mPARA GERAR UMA SENHA\033[m', 'azul claro'), es.cores('DIGITE \033[33m[2]\033[m \033[36mPARA FECHAR PROGRAMA\033[m', 'azul claro'))

    # Validando resposta das opções:
    resposta = ax.validar()

    if resposta == 1:
        # Controlando quantidade de dígitos:
        quantidade = ax.controle()
        # Gerando senha:
        senha_criada = ax.gerador(quantidade)
        es.painel(senha_criada, quantidade)
    else:
        es.titulos(es.cores('FECHANDO PROGRAMA...', 'amarelo'))
        break