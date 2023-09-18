# Precedência entre os operadores aritméticos
# 1° (n + n) parênteses e esses são executados de dentro para fora, os mais internos primeiro
# 2° ** potenciação 
# 3º * multiplicação, / divisão, // divição por inteiro, % módulo
# 4° + adição, - subtração

''' 
OBS: se tiver operadores da mesma precedência na mesma conta ex: * e / ou + e -
eles serão executados da esquerda para direita.
'''

conta_1 = 1 + 1 ** 5 + 5  # A ideia era que fosse 2^10 que seria = 1024
print(conta_1) # o resultado foi 7, porque primeiro ele resolveu 1^5 = 1 depois somou com 1+5

# corrigindo
conta_1 = (1 + 1) ** (5 + 5)
print(conta_1)

# cada vez que eu mudo o valor da variável, fica valendo o último valor
conta_1 = (1 + int(0.5 + 0.5)) ** (5 + 5)
print(conta_1)