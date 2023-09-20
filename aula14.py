# Usando a função Format
a = 'Café'
b = 'Açucar'
c = 1.1

#minha_string =  'a={} b={} c={:.3f} {}' # note que se eu colocar um novo argumento abaixo e chamar ele vem
#formato = minha_string.format(a, b, c, '1234' ) # a str 1234 é um novo argumento 

# se eu buscasse {} sem colocar nada embaixo, receberia o erro porque estaria buscando algo que já acabou
# IndexError: Replacement index 3 out of range for positional args tuple 
#print(formato)

# Trabalhando com índices
# minha_string =  'a={0} b={1} c={2:.3f}'
# formato = minha_string.format(a, b, c) 
# print(formato)

#Trabalhando com índices não dependo mais da ordem.
#minha_string =  'a={0} a={0} a{0} b={1} c={2:.3f}'
#formato = minha_string.format(a, b, c) 
#print(formato)

#Trabalhando com índices posso inverter a ordem.
#minha_string =  'b={1} a={0} c={2:.3f}'
#formato = minha_string.format(a, b, c) 
#print(formato)

# Ainda assim posso me perder. O ideal é trabalhar com parâmetros nomeados
# são Argumentos(a,b,c), São parâmetros(nome1=a), nome1 é parâmetro e o valor 'a' é argumento
minha_string =  ' a={nome0} b={nome1} c={nome2:.3f}'
formato = minha_string.format(nome0=a, nome1=b, nome2=c) 
print(formato)

# Quando uma função éstá dentro de um objeto ex: string
# ela é chamada de Método