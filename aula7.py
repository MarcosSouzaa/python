# Variáveis são usadas para salvar algo na memória do computador
# PEP8: inicie variáveis com letras minúsculas, pode usar números e underline _.
# PEP 8 é o guia de estilos do código python
# Essa separação por _ (underline), chamamos de snake case
# O sinal de = é o operador de atribuição, usado para atribuir valor à variável
# Uso: nome_variável = expressao

nome_completo = 'Marcos Antonio Silva de Souza'
print(nome_completo) # imprime o valor da variável: Marcos ...

# posso colocar uma expressão enuma variável
soma_dois_mais_dois = 2 + 2
print(soma_dois_mais_dois)

# posso usar as duas variáves
print(nome_completo, soma_dois_mais_dois)

# OBS: variáveis não são utilizadas para repetir códigos , mas para deixar o código mais legível
print(int('1'), type(int('1')))

# Ao invés de escrever várias vezes int('1'), eu crio uma variável
int_um = int('1')
print(int_um, type(int_um))

# Agora, posso mudar o tipo de vários lugares do meu código em um só lugar
int_um = bool('1') # lembrando que nesse caso, o nnome da variável não está adequado, deveria ser bool_1
print(int_um, type(int_um))

# utilização na prática
nome = 'Marcos Souza'
idade = 17
maior_de_idade = idade >= 18

print('Nome: ', nome, '-', 'Idade:', idade)
print('É maior de idade?',  maior_de_idade)



