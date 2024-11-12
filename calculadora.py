#!/bin/bash



primeiro_numero = input("Coloque o primeiro número AQUI >>>")
primeiro_numero = int(primeiro_numero) # Conversão de String para Inteiro
print (primeiro_numero)

segundo_numero = input("Coloque o segundo número AQUI >>>")
segundo_numero = int(segundo_numero) # Conversão de String para Inteiro
print (segundo_numero)

soma = primeiro_numero + segundo_numero
print ("Soma:" , soma)

exponenciacao = primeiro_numero ** segundo_numero
print ("Exponenciação" , exponenciacao)

subtracao = primeiro_numero - segundo_numero
print ("Subtração" , subtracao)

multiplicacao = primeiro_numero * segundo_numero
print ("Multiplicação" , multiplicacao)

if segundo_numero != 0 :
    divisao = primeiro_numero / segundo_numero
    print("Divisão:", divisao)
else:
    print("Divisão: Não é possível dividir por zero.") # Evitar divisão por zero
