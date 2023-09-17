# Conversão de tipos, Coerção
# type convertion, typecasting, coercion
# é o ato de converter um tipo em outro
# tipos imutáveis e primitivos
# str, int, float, bool

print(1 + 1)
print('a' + 'b')

# print('1' + 1) ele vai trazer um erro porque não pode concatenar str com inteiro
# no javaScript ele converteria  tudo em int e leria porque tem 'tipagem fraca'
# o python é dinâmico, mas tem tipagem forte e se não falar o tipo, ele não sabe o que fazer

# vendo qual o tipo do valor/objeto
print('1', type('1')) # retornará o tipo string

# fazendo a coerção ou conversão dos tipos
print(int('1'), type(int('1')))# após a conversão, retornará o tipo int

# se eu quiser somar uma string com um número, vou fazer a coerção
print(int('1') + 1) # ele converte e tenho o resultado 2

# convertendo para float
print(float('1') + 1) #vai imprimir um número flutuante
print(type(float('1') + 1)) # para ver qual é o tipo

# verificando o tipo bool
print(bool('')) # uma classe bool vazia é considerada False

#conversão do tipo string para boolean
print(bool(' ')) # uma classe bool com um espaço é considerado str, então é True

# convertendo para string
print(str(11) + 'b') # Eu quero concatenar para exibir 11b, vou ter que converter 11 em str.
