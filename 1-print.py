
#Hello wordl#
#Para executar o projeto python, vá no diretório do arquivo#
#digite python nome_arquivo.py#

print("Hello World!")

#Python é um linguagem de tipagem dinamica#
#É uma linguagem de tipagem forte#
#Ou seja não precisa informar o tipo de dado da variavel#

# name = "Resident Evil 4 Remake"
# yearLaunch = 2023
# gamePrice = 300.00
# planeIncluded = False

#Para comentar crtl + ;

#Utilizar na declaração de variável o cameCase com python#

# print(name)
# print(yearLaunch)
# print(gamePrice)
# print(planeIncluded)

#Como identificar o tipo de dado de cada variavel#


# print(type(name))
# print(type(yearLaunch))
# print(type(gamePrice))
# print(type(planeIncluded))

#Inserindo um comportamento dinamico ao programa#
#Usuario inseri os valores ao inves de ter ele direto no código#

name = input("Digite o nome do jogo\n")
#\n - quebra de linha


yearLaunch = int(input("Digite o ano de lançamento do jogo\n"))

#Utiliza a função int porque o retorno da função input é sempre em string


gamePrice = float(input("Digite o valor do jogo\n"))


planeIncluded = bool(input("Está incluido no plano mensal?\n"))

             
#Concatenar valores#

# Alternativa 1
# print("O ano de lançamento do jogo é", yearLaunch)

#Alternativa 2
#Um único print para exibir todas as informações juntas
print("O nome do jogo é:", name, "\n O ano de lançamento do jogo é:", yearLaunch)

#Alternativa 3
print(f"O nome do jogo é: {name} \n O ano de lançamento é: {yearLaunch}")


