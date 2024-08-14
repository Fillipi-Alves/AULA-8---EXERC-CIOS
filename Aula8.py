# #AULA 8 -  Condicionais
#  Instruções de I/O (entrada e saída)
# Aritméticos
# Atribuição
# Manipulação de dados
# Condicionais em Python
# DOCUMENTAÇÃO CONIDCIONAIS PYTHON 
# 4.2. Instruções de I/O (entrada e saída):
# - Essa parte trata de como um programa pode interagir 
# com o mundo externo, como receber informações (entrada) 
# e enviar informações (saída). Por exemplo, 
# se você tem um programa que precisa pedir para o usuário 
# digitar seu nome, isso seria uma entrada de dados. 
# E se o programa precisa mostrar na tela uma mensagem de saudação 
# com esse nome, isso seria uma saída de dados.

# 4.2.1. Aritméticos:
# - Aqui, estamos falando sobre as operações matemáticas 
# que um programa pode realizar. Isso inclui adição, subtração, 
# multiplicação, divisão e outras operações matemáticas básicas 
# que você pode fazer em um programa de computador.

# 4.2.2. Atribuição:
# - Esta seção trata de como um programa atribui valores a 
# variáveis. Por exemplo, se você tem uma variável 
# chamada "idade" e quer atribuir o valor "30" a ela, 
# você usaria uma instrução de atribuição para fazer isso.

# 4.2.3. Manipulação de dados:
# - Aqui, estamos falando sobre como um programa pode 
# manipular os dados que ele recebeu. Isso pode incluir 
# ordenar uma lista de números, filtrar dados com base em 
# determinados critérios, ou qualquer outra forma de alterar 
# ou processar os dados para obter um resultado desejado.
# ​
# Introdução às Estruturas Condicionais em Python


# As estruturas condicionais são fundamentais na programação, permitindo que um programa
#  tome decisões com base em certas condições. Em Python, você pode usar os 
# comandos `if`, `elif` (abreviação de "else if") e `else` para criar fluxos 
# de execução condicionais. Essas estruturas permitem que você execute diferentes 
# blocos de código com base em avaliações de expressões booleanas (verdadeiro ou falso).

# 1. O Comando if:

# O comando if` é a base das estruturas condicionais em Python. Ele avalia uma 
# expressão booleana e executa o bloco de código aninhado apenas se a expressão 
# for verdadeira. A sintaxe básica é a seguinte:

# if expressao_booleana:
#     # Bloco de código a ser executado se a expressão for verdadeira


# CONDICIONAL SIMPLES

# idade = 18
# if idade >= 18:
#     print("Você é maior de idade.")


# A PARTIR DAQUI É COMPOSTA

# 2. O Comando elif:

# O comando elif é usado para testar múltiplas condições em sequência. 
# Ele só é avaliado se as condições anteriores forem falsas. 
# A sintaxe é a seguinte:

# if expressao_booleana1:
#     # Bloco de código a ser executado se a expressão 1 for verdadeira
# elif expressao_booleana2:
#     # Bloco de código a ser executado se a expressão 2 for verdadeira
# else:
#     # Bloco de código a ser executado se nenhuma expressão for verdadeira




# nota = 85
# if nota >= 90:
#     print("Ótimo desempenho!")
# elif nota >= 70:
#     print("Bom desempenho.")
# else:
#     print("Melhorar na próxima.")


# 3. O Comando else:

# O comando else é usado para 
# definir um bloco de código a ser executado quando 
# todas as condições anteriores forem falsas. Ele não tem uma expressão booleana 
# associada, pois é o último caso a ser considerado quando nenhum dos casos anteriores 
# for verdadeiro.



# numero = 7
# if numero % 2 == 1:
#     print("O número não é par.")
# else:
#     print("O número par.")



# As estruturas condicionais em Python permitem que você crie programas dinâmicos 
# que reagem a diferentes situações. Com o uso de if, `elif` e `else`, você pode 
# controlar o fluxo de execução de acordo com as condições que você define. 
# Isso é essencial para criar programas flexíveis e capazes de lidar com uma 
# variedade de cenários.







# OUTROS EXEMPLOS: 


# meu_carrinho = []
# total_valores = []
# produtos=  ['arroz', 'feijão', 'ervilha']
# valores =  [20.0,18.0,5.]

# produto1 = input('Digite o produto 1')
# produto2 = input('Digite o produto 2')
# produto3 = input('Digite o produto 3')



# # if (produto1, produto2, produto3) == (produtos[0], produtos[1], produtos[2]):
# #     meu_carrinho += (produtos[0], produtos[1], produtos[2])
# #     print(meu_carrinho)
# # if (produto1, produto2, produto3) != produtos:
# #     print('Não existe o produto')

# # if produto1 in produtos or produto2 in produtos or produto3 in produtos:
# #    meu_carrinho.append(produto1)
# #    meu_carrinho.append(produto2)
# #    meu_carrinho.append(produto3)

# # if produto1 in produtos:
# #    meu_carrinho.append(produto1)
# #    print(meu_carrinho)
# #    meu_carrinho2 = meu_carrinho
# # if produto2 in produtos:
# #    meu_carrinho2.append(produto2)
# #    print(meu_carrinho2)
# #    meu_carrinho3 = meu_carrinho2
# # if produto3 in produtos:
# #    meu_carrinho3.append(produto3)








# EXEMPLO COM CONDICIONAIS -  MERCADO 


# produtos = ['arroz', 'Banana', 'Leite', 'feijao', 'pao']
# precos = [1.50, 2.00, 3.20, 2.50, 5.00]


# carrinho = []
# total = 0

# print("Produtos disponíveis:")
# print("1. arroz - R$ 1.50")
# print("2. Banana - R$ 2.00")
# print("3. Leite - R$ 3.20")
# print("4. feijãp - R$ 2.50")
# print("5. pao - R$ 5.00")


# escolha1 = input("Escolha o número do produto que deseja adicionar ao carrinho (ou '0' para finalizar): ")

# if escolha1 == '1':
#     carrinho.append(produtos[0])
#     total += precos[0]
# elif escolha1 == '2':
#     carrinho.append(produtos[1])
#     total += precos[1]
# elif escolha1 == '3':
#     carrinho.append(produtos[2])
#     total += precos[2]
# elif escolha1 == '4':
#     carrinho.append(produtos[3])
#     total += precos[3]
# elif escolha1 == '5':
#     carrinho.append(produtos[4])
#     total += precos[4]


# escolha2 = input("Escolha o número do produto que deseja adicionar ao carrinho (ou '0' para finalizar): ")

# if escolha2 == '1':
#     carrinho.append(produtos[0])
#     total += precos[0]
# elif escolha2 == '2':
#     carrinho.append(produtos[1])
#     total += precos[1]
# elif escolha2 == '3':
#     carrinho.append(produtos[2])
#     total += precos[2]
# elif escolha2 == '4':
#     carrinho.append(produtos[3])
#     total += precos[3]
# elif escolha2 == '5':
#     carrinho.append(produtos[4])
#     total += precos[4]


# escolha3 = input("Escolha o número do produto que deseja adicionar ao carrinho (ou '0' para finalizar): ")

# if escolha3 == '1':
#     carrinho.append(produtos[0])
#     total += precos[0]
# elif escolha3 == '2':
#     carrinho.append(produtos[1])
#     total += precos[1]
# elif escolha3 == '3':
#     carrinho.append(produtos[2])
#     total += precos[2]
# elif escolha3 == '4':
#     carrinho.append(produtos[3])
#     total += precos[3]
# elif escolha3 == '5':
#     carrinho.append(produtos[4])
#     total += precos[4]


# print("\nVocê comprou:")
# if len(carrinho) > 0:
#     print(carrinho)
#     print(f"Total: R$ {total:.2f}")
# else:
#     print("Nenhum produto comprado.")





# EXERCÍCIO AULA 8 


# numero = float(input("Digite um número: "))

# if numero > 0:
#     print("O número é positivo.")
# elif numero < 0:
#     print("O número é negativo.")
# else:
#     print("O número é zero.")


# idade = int(input("Digite a sua idade: "))

# if idade >= 16:
#     print("Você pode votar.")
# else:
#     print("Você não pode votar.")

# numero = int(input("Digite um número: "))


# if numero % 2 == 0:
#     print("O número é par.")
# else:
#     print("O número é ímpar.")

# a = float(input("Digite o comprimento do primeiro lado: "))
# b = float(input("Digite o comprimento do segundo lado: "))
# c = float(input("Digite o comprimento do terceiro lado: "))


# if a + b > c and a + c > b and b + c > a:
#     if a == b == c:
#         print("O triângulo é equilátero.")
#     elif a == b or a == c or b == c:
#         print("O triângulo é isósceles.")
#     else:
#         print("O triângulo é escaleno.")
# else:
#     print("Os comprimentos fornecidos não formam um triângulo.")
 
# numero = int(input("Digite um número: "))


# if numero % 5 == 0 and numero % 7 == 0:
#     print("O número é múltiplo de 5 e 7.")
# else:
#     print("O número não é múltiplo de 5 e 7.")

# numero = float(input("Digite um número: "))


# if numero > 10:
#     print("O número é positivo e maior que 10.")
# else:
#     print("O número não é positivo e maior que 10.")

# numero = int(input("Digite um número: "))
# if numero % 3 == 0 or numero % 5 == 0:
#     print("O número é divisível por 3 ou 5.")
# else:
#     print("O número não é divisível por 3 ou 5.")
