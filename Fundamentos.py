
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

# n1 = int(input("Qual número você deseja verificar? "))

# suc = n1 + 1
# ant = n1 - 1

# print(f"O antecessor do número {n1} é {ant} e o sucessor é {suc}")

# #Exercicio 2
# #Escreva um programa em python que leia 4 números e calcule a média entre eles

# n2 = int(input("Qual número você deseja verificar a média? "))
# n3 = int(input("Qual número você deseja verificar a média? "))
# n4 = int(input("Qual número você deseja verificar a média? "))
# n5 = int(input("Qual número você deseja verificar a média? "))

# med = (n2 + n3 + n4 + n5) / 4

# print(f"A média é igual a {med}")

# #Detalhando a utilização de Strings

gameName = "Fifa23"
# # gameName2 = "fifa23"
# # print(gameName == gameName2)

# #Conclusão python é uma linguagem case sensitive

# gameDescription = """
#     Fifa 23 é um jogo de futebol 
#     desenvolvido pela EA sports

# """
# print(gameDescription)

# #Operações com strings

# gameName = "Fifa"
# gameYear = "23"


# #1 - Operação de concatenação de strings
# gameFullName = gameName + gameYear
# print(gameFullName)

# #2 - Operação de multiplicação de string

# line = "="

# print(line * 25)

# #3 - Procurar palavra dentro de String
# print("Fifa" in gameDescription)#Retorno em valor lógico


#Slice - fatiando strings
# 1 - Busque toda string a partir da primeira posição
#O primeiro indice é 0
print(gameName[0:])

#2 - Busque toda string até a última posição
print(gameName[:7])

#3 - Busque toda a string da 3 até a ultima posição
print(gameName[2:])

#string[inicio:fim:passo] - indice inicial posição 0 | indice final -1
#passo = incremento. Por padrão o número é o 1

#4 - Busquqe toda a string de 2 em 2
print(gameName[::2])

#5 - Busque todas string no indice impares
print(gameName[1::2])

#6 - Inverta uma string de trás para frente
print(gameName[::-1])

#Metodos em strigs

str = "Olá python"

print(str.upper()) #Retornar string em maiuscula

print(str.lower()) #Retornar string em minuscula

print(str.capitalize()) #Apanas primeira letra maiuscula

print(str.title()) #Apenas a primeira letra em maiuscula

print(str.center(20, "-")) #(qnt caracter, preenchimento)Retorna a string centralizada

print(str.find("y")) #Retorna a posição que o caractere foi encontrado

print(str.count("o")) #Conta os caracteres

print(str.replace("Olá", "Tchau")) #Substitui caracter

print(str.split(',')) #Quebra uma string



#Exercicio 
#invertendo caracter

str1 = "Fifa 23"

char = str1[0].lower()

new_str = str1.replace(char, '$')

new_game = char + new_str[1:]

print(new_game)

#Troca de caracter
st1 = 'cab' #zyb
st2 = 'zyx' #cax

st1_new = st1[2:] #b
st2_new = st2[2:] #x

st1_repl = st2[:2] + st1_new #zyb
print(st1_repl) #zyb

st2_repl = st1[:2] + st2_new #cax
print(st2_repl)


#Listas 
#Lista dá para agrupar as informações em uma única variável
gameFifa = ["Fifa 23", 2023, 90.50, True]

#1 - Buscar os dois primeiros itens da lista
print(gameFifa[0:2])


#2 - Buscar o ultimo item da lista
print(gameFifa[-1])

#3 - Buscar item até uma determinada posição
print(gameFifa[:3])

#4 - Buscar itens de uma posição em diante
print(gameFifa[1:4])

gameList = ["Resident Evil", "Fifa 23", 
            "The Legend of Zelda", "Red Dead 2", "Mario Bros"]

#Metodos
# 1 - Saber o tamanho da lista
print(len(gameList))

# 2 - Recuperar um item da lista pelo Indice
print(gameList.index("Mario Bros"))

# 3 - Adicionar item ao final da lista
gameList.append("GTA V")
print(gameList)

# 4 - Ordenar Lista
gameList.sort()
print(gameList)

# 5 - Copiar os itens de uma lista para outra4
gameReset = gameList.copy()
gameReset.remove("GTA V")
print(gameReset)

# 6 - Remove todos os itens da lista
gameList.clear()

#Tuplas
gamesTuple = ("Fifa23", "Read Dead 2", 
              "GTA V", "Mario Bros", "The Legend of Zelda")

# Não é possivel adicionar valores na tupla
# Não é possivel remover valores na tupla
# Não é possível ordenar valores em uma tupla

#Set

gamesSet = {"Fifa23", "Read Dead 2", 
              "GTA V", "Mario Bros", "The Legend of Zelda"}

# Não é possivel recuperar valores via fatiamento ou slice

#1 - Buscar o tamanho do set
print(len(gamesSet))

# 2 - True e 1 são o mesmo valor
exampleSet = {"Fifa 23", True, 1, 90.50}
print(exampleSet)

# 3 - Adicionar item de outro set
gamesSet.update(exampleSet)
print(gamesSet)

# 4 - Remover um item no set
gamesSet.remove(True)
gamesSet.remove(90.50)
print(gamesSet)