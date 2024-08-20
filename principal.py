#  Arquivo principal do gerador de senha

import auxilio as ax
import estetica as es

# Construindo um painel pra usuário
es.titulos("GERADOR DE SENHA")

# Controlando quantidade de dígitos:
quantidade = ax.controle()

# Gerando senha:
senha_criada = ax.gerador(quantidade)