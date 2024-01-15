
import random
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
simbolos = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Bem-vindo ao Gerador de Senhas!")
nr_letras= int(input("Quantas letras você gostaria de ter em sua senha?\n")) 
nr_simbolos = int(input("Quantos símbolos você gostaria de ter em sua senha?\n"))
nr_numeros = int(input("Quantos números você gostaria de ter em sua senha\n"))

#Categorias com ordenação. Ex: JAL@#$123
letras_random = random.sample(letras, nr_letras)

simbolos_random = random.sample(simbolos, nr_simbolos)

numeros_random = random.sample(numeros, nr_numeros)

senha = "".join(letras_random + simbolos_random + numeros_random)
print(senha)


#Categorias não ordenadas. Ex: #J1!A@Q3@2
lista_random = "".join(random.sample(senha, len(senha)))
print(lista_random)