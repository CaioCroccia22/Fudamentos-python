
#Hello wordl#
#Para executar o projeto python, vá no diretório do arquivo#
#digite python nome_arquivo.py#

# print("Hello World!")

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

# name = input("Digite o nome do jogo\n")
# #\n - quebra de linha


# yearLaunch = int(input("Digite o ano de lançamento do jogo\n"))

# #Utiliza a função int porque o retorno da função input é sempre em string


# gamePrice = float(input("Digite o valor do jogo\n"))


# planeIncluded = bool(input("Está incluido no plano mensal?\n"))

             
#Concatenar valores#

# Alternativa 1
# print("O ano de lançamento do jogo é", yearLaunch)

# #Alternativa 2
# #Um único print para exibir todas as informações juntas
# print("O nome do jogo é:", name, "\n O ano de lançamento do jogo é:", yearLaunch)

# #Alternativa 3
# print(f"O nome do jogo é: {name} \n O ano de lançamento é: {yearLaunch}")


#Operadores aritméticos e Relacionais
# num1 = int(input("Digite o primeiro número: "))
# num2 = int(input("Digite o primeiro número: "))

#Aritmeticos
# sum = num1 + num2
# sub = num1 - num2
# div = num1 / num2
# mult = num1 * num2

#Operação para saber o resto da divisão
# mod = num1 % num2
# exp = num1 ** num2
# print(sum, sub, div, mult, mod, exp)

#Comparação
# bigger = num1 > num2
# smaller = num1 < num2
# equal = num1 == num2
# diferrent = num1 != num2
# bigger_equal = num1 >= num2
# smaller_equal = num1 <= num2


#Atribuição

# num1 = num1 + 1
# ou num1 += 1

#Exercicio 1
#Escreve um programa que leia um número e apresente seu antecessor e sucessor

n1 = int(input("Qual número você deseja verificar? "))

suc = n1 + 1
ant = n1 - 1

print(f"O antecessor do número {n1} é {ant} e o sucessor é {suc}")

#Exercicio 2
#Escreva um programa em python que leia 4 números e calcule a média entre eles

n2 = int(input("Qual número você deseja verificar a média? "))
n3 = int(input("Qual número você deseja verificar a média? "))
n4 = int(input("Qual número você deseja verificar a média? "))
n5 = int(input("Qual número você deseja verificar a média? "))

med = (n2 + n3 + n4 + n5) / 4

print(f"A média é igual a {med}")

#Detalhando a utilização de Strings
