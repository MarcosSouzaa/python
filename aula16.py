# if / elif      /....../else
# se / se não se /....../senão

entrada = input(f'Você quer "entrar" ou "sair"?\n')

if entrada == 'entrar':
    print('Você entrou no sistema')
elif entrada == 'sair':
    print('Você saiu do sistema')
else:
    print('Você não digitou nem Entrar e nem Sair!')