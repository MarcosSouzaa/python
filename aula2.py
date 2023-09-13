#Função print com argumentos
print(1234)

#Função print com mais de um argumento. Tem que separar com vírgulas
print(12,34)
print(56,78)

#Posso usar separador entre os argumentos com a palavra sep = '' ou sep = " "
print(12,34, 1011, sep='-')# O sep nesse caso, é um argumento nomeado
print(56,78, sep='-')

#Posso usar também os argumentos end para indicar o que fazer no fim e read = \r e pular linha \n 
print(12,34, 1011, sep='-', end='\r\n##\n')
 
#Ou não pular linha, 
print(12,34, 1011, sep='-', end='##')
