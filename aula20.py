# Exercício de comparação com if e comparadores
primeiro_valor = input('Digite o primeiro valor: ')
segundo_valor = input('Digite o segundo valor: ')

valor1 = int(primeiro_valor)
valor2 = int(segundo_valor)

if valor1 > valor2:
    print(f'{valor1= } é maior ' f'do que {valor2= }')
elif valor1 == valor2:
    print(f'{valor1= } é igual a ' f'{valor2= }') 
else:
    print(f'{valor2= } é maior ' f' do que {valor1= }')
