
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

# gameName = "Fifa23"
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


# #Slice - fatiando strings
# # 1 - Busque toda string a partir da primeira posição
# #O primeiro indice é 0
# print(gameName[0:])

# #2 - Busque toda string até a última posição
# print(gameName[:7])

# #3 - Busque toda a string da 3 até a ultima posição
# print(gameName[2:])

# #string[inicio:fim:passo] - indice inicial posição 0 | indice final -1
# #passo = incremento. Por padrão o número é o 1

# #4 - Busquqe toda a string de 2 em 2
# print(gameName[::2])

# #5 - Busque todas string no indice impares
# print(gameName[1::2])

# #6 - Inverta uma string de trás para frente
# print(gameName[::-1])

# #Metodos em strigs

# str = "Olá python"

# print(str.upper()) #Retornar string em maiuscula

# print(str.lower()) #Retornar string em minuscula

# print(str.capitalize()) #Apanas primeira letra maiuscula

# print(str.title()) #Apenas a primeira letra em maiuscula

# print(str.center(20, "-")) #(qnt caracter, preenchimento)Retorna a string centralizada

# print(str.find("y")) #Retorna a posição que o caractere foi encontrado

# print(str.count("o")) #Conta os caracteres

# print(str.replace("Olá", "Tchau")) #Substitui caracter

# print(str.split(',')) #Quebra uma string



# #Exercicio 
# #invertendo caracter

# str1 = "Fifa 23"

# char = str1[0].lower()

# new_str = str1.replace(char, '$')

# new_game = char + new_str[1:]

# print(new_game)

# #Troca de caracter
# st1 = 'cab' #zyb
# st2 = 'zyx' #cax

# st1_new = st1[2:] #b
# st2_new = st2[2:] #x

# st1_repl = st2[:2] + st1_new #zyb
# print(st1_repl) #zyb

# st2_repl = st1[:2] + st2_new #cax
# print(st2_repl)


# #Listas 
# #Lista dá para agrupar as informações em uma única variável
# gameFifa = ["Fifa 23", 2023, 90.50, True]

# #1 - Buscar os dois primeiros itens da lista
# print(gameFifa[0:2])


# #2 - Buscar o ultimo item da lista
# print(gameFifa[-1])

# #3 - Buscar item até uma determinada posição
# print(gameFifa[:3])

# #4 - Buscar itens de uma posição em diante
# print(gameFifa[1:4])

# gameList = ["Resident Evil", "Fifa 23", 
#             "The Legend of Zelda", "Red Dead 2", "Mario Bros"]

# #Metodos
# # 1 - Saber o tamanho da lista
# print(len(gameList))

# # 2 - Recuperar um item da lista pelo Indice
# print(gameList.index("Mario Bros"))

# # 3 - Adicionar item ao final da lista
# gameList.append("GTA V")
# print(gameList)

# # 4 - Ordenar Lista
# gameList.sort()
# print(gameList)

# # 5 - Copiar os itens de uma lista para outra4
# gameReset = gameList.copy()
# gameReset.remove("GTA V")
# print(gameReset)

# # 6 - Remove todos os itens da lista
# gameList.clear()

# #Tuplas
# gamesTuple = ("Fifa23", "Read Dead 2", 
#               "GTA V", "Mario Bros", "The Legend of Zelda")

# # Não é possivel adicionar valores na tupla
# # Não é possivel remover valores na tupla
# # Não é possível ordenar valores em uma tupla

# #Set

# gamesSet = {"Fifa23", "Read Dead 2", 
#               "GTA V", "Mario Bros", "The Legend of Zelda"}

# # Não é possivel recuperar valores via fatiamento ou slice

# #1 - Buscar o tamanho do set
# print(len(gamesSet))

# # 2 - True e 1 são o mesmo valor
# exampleSet = {"Fifa 23", True, 1, 90.50}
# print(exampleSet)

# # 3 - Adicionar item de outro set
# gamesSet.update(exampleSet)
# print(gamesSet)

# # 4 - Remover um item no set
# gamesSet.remove(True)
# gamesSet.remove(90.50)
# print(gamesSet)

# #Dicionario
# gameFifaDict = {
#     "name": "Fifa 23",
#     "yearLauch" : 2023,
#     "gamePrice" : 90.50,
#     "classification" :8.5,
#     "genre": ["esporte", "familia"]
# }
# print(gameFifaDict)
# print(type(gameFifaDict))
# print(len(gameFifaDict))

# # 1- recuperar um elemento do dicionario
# print(gameFifaDict.get('classification'))

# # 2 - Buscar apenas os valores do dicionario
# print(gameFifaDict.values())


# # 3 - Buscar apenas as chaves do dicionario
# print(gameFifaDict.keys)

# # 4 - Buscar itens do dicionario com chave e valor
# print(gameFifaDict.items())
# #Retorno em tuplas

# #5 - Adicionar itens do dicionario
# gameFifaDict["Players"] = 2
# print(gameFifaDict)


# #Dicionarios Aninhados
# #Um dicionario dentro de outro
# import pprint

# gamesDicti = {
#     "Resident Evil 4" : {
#         "yearLaunch" : 2023,
#         "classification" : 9.8,
#         "genre" : ["Ação", "aventura"]
#     },
#     "Mario Odyssey" : {
#         "yearLaunch" : 2017,
#         "classification" : 10.0,
#         "genre" : ["aventura"]
#     },
#     "Donkey Kong country" : {
#         "yearLaunch" : 2018,
#         "classification" : 8.0,
#         "genre" : ["aventura"]
#     }
# }
# pp = pprint.PrettyPrinter(depth=4)
# pp.pprint(gamesDicti)

# #1 - Buscar informação dentro de um dicionário aninhado
# print("O genero de Mario Odyssey é:", gamesDicti["Mario Odyssey"]["genre"])


# # 2 - Adicionar novo item
# gamesDicti["Mario Odyssey"]["players"] =  1
# print(gamesDicti["Mario Odyssey"])

# # 3 - Excluir itens de um dicionario
# del gamesDicti["Resident Evil 4"]
# pp.pprint(gamesDicti)

# #Utilizando Condições com if/Else
# name = input("Digite o nome do jogo\n")
# yearLaunch = int(input("Digite o ano de lançamento do jogo\n"))
# classification = float(input("Digite a nota de classificação\n"))


# if classification > 8.0 and yearLaunch > 2010:
#     print(f"O jogo {name} é bom")
# else:
#     print(f"O jogo {name} é ruim")


# #Calculadora
# num1 = int(input("Digite o número a ser calculado:\n"))
# num2 = int(input("Digite outro número a ser calculado:\n"))
# operation = input("Digite a operação a ser realizada: (+ - * /)\n")

# if operation == "+":
#     result = num1 + num2
#     print({f"A soma é:{result}"})
# elif operation == "-":
#     result = num1 - num2
#     print(f"A subtração é {result}")
# elif operation == "*":
#     result = num1 * num2
#     print(f"A multiplicação é {result}")
# elif operation == "/":
#     result = num1 / num2
#     print(f"O resto da divisão é {result}")
# else:
#     print("Operação invalida")

#Limitação das casas decimais {result:.2f} - Limitado duas casas decimais
#Exercicios
#Calculo da distancia
# distance = float(input("Qual distancia será percorrida(em km)?\n"))

# if distance <= 200:
#     value = 0.5 * distance
# else:
#     value = distance * 0.35

# print(f"O valor da corrida será {value}")

# #Salario
# wage = float(input("Quanto você recebe?\n"))

# if wage >= 1.250:  
#     percentage = wage * 0.10
    
# else:
#     percentage = wage * 0.15

# newWage = percentage + wage
# print(f"O valor do seu salário é {newWage}")


# #Laço de repetição for
# #É por meio do laço de repetição que intera valores de um colection
# #É possível fazer com lista,tuplas,set, dicionario
# gameList = ["Resident Evil", "Fifa 23", 
#      "The Legend of Zelda", "Red Dead 2", "Mario Bros"]


# # 1 - Iterando valores de uma lista
# for game in gameList:
#     print(game)

# # 2 -Quando a codição for atendida, loop será encerrado
# for game in gameList:
#     if game == "Red Dead 2": #Ele para na interação
#         break
#     print(game)

# # 3 - Quando a condição for atendida, o loop vai para a próxima interação
# for game in gameList:
#     if game == "Red Dead 2": # Ele pula a interação
#         continue
#     print(game)


# # 4 - Avaliação do jogo

# # O range - é de 0 até o valor limite(X)
# gameName = input("Digite o nome do jogo\n")
# gameRating = int(input("Digite quantas avaliações deseja fazer no jogo\n"))

# sum = 0
# for i in range(gameRating):
#     note = float(input("Digite a nota para o jogo\n"))
#     sum += note #sum = sum + note
# print(f"A média de avaliação do jogo {gameName} é {sum/gameRating}")


# #Laço de repetição While
# gameName = input("Digite o nome do jogo\n")
# qtdRating = 0
# totalRating = 0
# rating = 0
# average = 0
# #As variaveis são inicializados com 0
# #Por ser de tipagem dinamica o interpretador precisa de um valor


# while (rating != -1):
#     rating = float(input("Informe a nota do jogo\n"))
#     if (rating != -1):
#         totalRating += rating
#         qtdRating += 1
#         average = totalRating / qtdRating
# print(f"Média das avaliações do jogo {gameName} é {average}")

# #List Comprehesion
# # 1 -Liste valores de 0 a 10 que sejam menor do que 4
# for i in range(10):
#     if i <= 4:
#         print(i)

# #É possível fazer esse código usando uma linha de código - List Comprehension
# listNumbers = [i for i in range(10) if i < 4]
# print(listNumbers)

# # Jogos que possuem a letra a
# list = [x for x in gameList if "a" in x]
# print(list)

#Exercicio
# -> Faça um programa para escrever a contagem regressiva e disparar um "beep"
# import winsound
# x = 10
# while x >= 0:
#     print(x)
#     x -= 1
# winsound.Beep(2500, 500)


# # -> Faça um programa que calcule a tabuada de um número com valores iniciais e finais
# numero1 = int(input("Tabuada de: \n"))
# numero2 = int(input("Começa em: \n"))
# numero3 = int(input("Até: \n"))
# x = numero2
# while x <= numero3:
#     print(f"A tabuado de {numero1} x {x} = {numero1 * x}")
#     x += 1

# #Funções
# #Reaproveita execução de blocos sem duplicar o código

# def welcome():
#     print("Hello World")


# welcome()

# def sum():
#     return 5 + 4
# print(sum())

# # Função para cadastrar um jogo
# def create_game():
#     name = input("Digite o nome do jogo:\n")
#     yearLaunch = int(input("Digite o ano que o jogo foi lançado\n"))
#     gamePrice = float(input("Digite o preço do jogo\n"))

#     print(f"{name} - R$ {gamePrice}")


# create_game()
# create_game()

# #Funções com Argumentos
# def rating_games(qtdRating):
#     gameName = input("Digite o nome do jogo: \n")
#     sum = 0
#     for i in range(qtdRating):
#         note = float(input("Digite a nota para o jogo: \n"))
#         sum += note
#     print(f"A média de avaliação do jogo {gameName} é {sum / qtdRating}")
# rating = int(input("Digite quantas avaliações deseja fazer no jogo\n"))
# rating_games(rating)

# #Função Recursivo
# #Quando dentro dela é feito uma ou mais chamadas dentro dela mesma
# #Ex: Fatorial 3 -> 3 * 2 * 1
# #1 - Fatorial
# def factorial(numero):
#     if numero == 1:
#         return 1
#     else:
#         return (numero * factorial(numero - 1))

# num = int(input("Digite o número para o fatorial: \n"))
# print(f"O fatorial do {num} é: {factorial(num)}")

# # 2 - A soma total de um número
# def somaTotal(number):
#     if number == 1:
#         return 1
#     else:
#         return (number + somaTotal(number - 1))
    
# soma = int(input("Digite o numero para fazer a soma total\n"))
# print(f"A soma do número {soma} é: {somaTotal(soma)}")

# #Utilizando função com Args Kwargs
# #*Args
# #Utilizamos quando não temos certeza de quantos argumentos queremos ter em uma função
# #Os argumentos são passados como uma tupla
# #*Kwargs - Além dos valores podemos passar também as respectivas chaves para cada argumento

# #   1 -Soma de Numeros
# def soma(*num):
#     sum_total = 0
#     for n in num:
#         sum_total += n
#     print(f"A soma é: {sum_total}")

# soma(7)
# soma(7,6,3,4,2)

# def presentation(**data):
#     for key, value in data.items():
#         print(f"{key} - {value}")

# presentation(name="Pyhton", category="Backend", level="Iniciante")
# presentation(name="Visão computacional com Python", category="IA", level="Avançado")
# presentation(name="Dashbord com Dash", category="Data Science", level="Intermediário")


#Função Lambda

# # 1 - Função de potencia de número
# power = lambda num: num **2

# #2 - Função paraa verificar se um número é par
# pair = lambda x: x % 2 ==0

# #3 - Função que divide um número por outro
# divNum = lambda x, y : x /y

# #4 - Função que inverte uma string
# reverse = lambda s: s[::-1]

# print(power(5))
# print(reverse("Olá mundo"))

#Exercicio
#Conta letras maiusculas e minusculas
#-> Escreva uma função python que receba uma 
# string e conte o número de letras maiusculas e minusculas desta string

# def check_char(text):
#     type = {"Uppercase": 0, "Lowercase": 0}
#     for char in text:
#         if char.isupper():
#             type["Uppercase"] += 1
#         elif char.islower():
#             type["Lowercase"] += 1
#     print("Texto original:", text)
#     print("Número de letra maiúsculas:", type["Uppercase"])
#     print("Número de letras minúsculas:", type["Lowercase"])

# word = input("Digite a frase que deseja:\n")
# check_char(word)

#Lista números pares e impares de uma lista

# def check_number(numbers):
#     pairs = []
#     odd = []
#     for n in numbers:
#         if n % 2 == 0:
#             pairs.append(n)
#         else:
#             odd.append(n)

# sequence = list(input("Digite os números:\n"))
# print(check_number(sequence))





