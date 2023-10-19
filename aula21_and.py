# Operador lógico and
# and or not
# and - Todas as condições precisam ser verdadeiras
# Se qualquer valor for considerado falso, a expressão inteira será avaliada naquele valor
# São consideradas falsy, mas só quando confrontado com bollean:
# 0, 0.0, ''string vazia, são considerado false.
# Também existe o tipo None que é usado para representar um não valor
'''
entrada = input('[E] Entrar ou [S] Sair: ').upper()
senha_digitada = input('senha: ')

senha_permitida = '123456'
if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')

'''
# Avaliação de curto circuito
# Quando ele encontra uma situação falsa, ele interrompe.
print(True and False and True) 

# String vazia reorna False
print(bool(''))

# 0 retorna False
print(bool(0))

print(True and 0 and True) 