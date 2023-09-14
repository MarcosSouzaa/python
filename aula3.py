'''
 Python = Linguagem de Programação
Tipo de Tipagem = Dinâmica / Forte
str -> string -> texto
Strings são textos que estão dentro das aspas  simples ou duplas.
'''
# Ao passar o número abaixo como argumento, o Python já sabe que é número e inteiro
# Isso é Tipagem dinâmica
print(1234)

#string em Aspas simples
print('Marcos Antonio Silva de Souza')

#string em Aspas duplas
print("Marcos Antonio Silva de Souza")

#Escape \ (uma barra invertida) o interpretador vai ler o ítem imediatamente após a barra 
print("Mostrando entre aspas: Marcos \"Antonio\"") # Nesse caso, vou mostrar "Antonio" entre aspas

# r- Posso usar a expressão regular r, se eu quiser mostrar as barras
print(r"Mostrando as barras de escape: Marcos \"Antonio\"")

#Mostrando a palavra entre aspas começando a string entre aspas simples
print('Marcos "Antonio"')

#Mostrando a palavra entre aspas simples começando a string entre aspas duplas
print("Marcos 'Antonio'")