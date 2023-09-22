# usando a função input
#input('Qual é o seu nome? ')

# Criar uma variável para receber os dados digitados
# Printar o nome digitado utilizando f-springs
'''
nome = input('Qual é o seu nome? ') Aqui ele recebe de volta uma string
print(f'O seu nome é: {nome}')

'''
# Aqui vou pedir informações numéricas, mas lembrando que ele devolve string
'''
numero_1 = input('Digite um número: ')
numero_2 = input('Digite outro número: ')
print(f'A soma do números é: {numero_1 + numero_2}')

'''

# Nesse caso se digitar 1 e 5, vou receber 15, porque ele entende como concatenação de 2 strings.
# Digite um número: 1
# Digite outro número: 5
# A soma do números é: 15

# Para resolver esse problema, tenho que fazer a conversão ou coerção
numero_1 = input('Digite um número: ') # não vou fazer a coerção aqui porque se for digitado letra, quebra o código
numero_2 = input('Digite outro número: ')

# Eu poderia fazer uma checagem aqui se o usuário digitou número.

# vou criar uma nova variável para receber a coerção para int
# Agora o resultado será a soma = 6
int_numero1 = int(numero_1)
int_numero2 = int(numero_2)
print(f'A soma do números é: {int_numero1 + int_numero2}')

