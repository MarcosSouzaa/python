# Operadores Aritméticos

adicao = 10 + 10
subtracao = 10 - 5
multiplicacao = 10 * 10
divisao = 10 / 3 # retorno sempre é um número flutuante
divisao_inteira = 10 // 2.2 # corta as casas decimais
num1 = 25 
num2 = 5
modulo = num1 % num2 # Resto da divisão
# Como sei se um número é divisivel por outro ou se é múltiplo?
# se der resto Zero ex:
# print(10 % 8 == 0) 

exponenciacao = 2 ** 10 # CUIDADO com números Grandes! Estoura a memória

print('Adição', adicao)
print('Subtração', subtracao)
print('Multiplicação', multiplicacao)
print('Divisão', divisao)
print('Divisão Inteira', divisao_inteira)
print('Resto da Divisão de', num1,'por', num2, 'é igual a', modulo)
print('Exponenciação:', exponenciacao)
# se der zero é múltiplo 
print(10 % 8 == 0) # 10 dividido por 9 é igual a 0? não! é False
print(1225 % 5 == 0) # True, é 0.

# o número é Par? se for divisível por 2 é!
numero = 20
print('O número',numero,'é par ou impar?')
if numero % 2 == 0:
    print(numero, "Com certeza é par!")
    print('')
else:
    print("Com certeza é impar!")
    print('')

#Pedindo ao usuário para digitar um número
numero_usuario = int(input("Digite um número inteiro: "))
# Mostra o número digitado pelo usuário
print('Você digitou o número:', numero_usuario)

if numero_usuario % 2 == 0:
    print('O número', numero_usuario, 'é par!')
else:
    print('O número', numero_usuario, 'é impar!')