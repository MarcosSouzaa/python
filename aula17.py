# Fluxo do interpretador em condicionais

'''
condicao = True
if condicao:
    print('Acondição é verdadeira')

# essa informação será impressa pois está fora do if
print('A condição dentro do if foi impressa poi era True')

'''
'''
# nesse próximo caso não será impresso o que estiver dentro do if, condição False
condicao = False
if condicao:
    print('A condição é Falsa')

print('A condição do if não foi impressa porque é Falsa')
'''
'''
# nesse próximo caso será impresso o que estiver dentro do if, condição True
condicao = True
if condicao:
    print('Esse é a impressão do 1º if')
else:
    print('O primeiro if não foi impresso porque era false')
'''

'''
# Usando mais um if
condicao = False
if condicao:
    print('Esse é a impressão do 1º if, pois a condição é verdadeira')
else:
    print('Aqui é a impressão do Else, o primeiro if não foi impresso porque era false')

if 10 == 10: # condição True
    print('Imprime o 2º if se a condição for verdadeira')
    print(type(10 == 10))

'''
'''
# Usando elif para verificar várias condições
# Nesse caso ele só imprimirá o else pois todas condições são falsas
# Depois vai ler o que está fora do if, ou seja, do laço
condicao1 = False
condicao2 = False
condicao3 = False
condicao4 = False

if condicao1:
    print('Código para condição 1')
    print('Repetindo código da condição 1')
elif condicao2:
    print('Código para condição 2')
elif condicao3:
    print('Código para condição 3')
elif condicao4:
    print('Código para condição 4')
else:
    print('Nenhuma condição foi satisfeita')

print('Foi impresso pois está fora do if')

'''

'''
# Se alguma condição for verdadeira, ele executa o código e não executa mais nada
# dentro do laço e já pula para o próximo blocao do código.
condicao1 = False
condicao2 = False
condicao3 = True
condicao4 = False

if condicao1:
    print('Código para condição 1')
    print('Repetindo código da condição 1')
elif condicao2:
    print('Código para condição 2')
elif condicao3:
    print('Código para condição 3')
elif condicao4:
    print('Código para condição 4')
else:
    print('Nenhuma condição foi satisfeita')

print('Foi impresso pois está fora do if')

'''
# Se todas condições forem verdadeiras, ele executa a primeira e não executa mais nada
# dentro do laço e já pula para o próximo blocao do código.
condicao1 = True
condicao2 = True
condicao3 = True
condicao4 = True

if condicao1:
    print('Código para condição 1')
    print('Repetindo código da condição 1')
elif condicao2:
    print('Código para condição 2')
elif condicao3:
    print('Código para condição 3')
elif condicao4:
    print('Código para condição 4')
else:
    print('Nenhuma condição foi satisfeita')

print('Foi impresso pois está fora do if')
