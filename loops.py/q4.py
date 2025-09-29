import os

usuario=input('Digite seu usuario: ')
senha=str(input('Digite sua senha: '))

for x in range(3):
    
    sen = str(input('Digite sua senha '))

    if sen==senha:
     print('acesso permitido')
     break
    
else:
    print('acesso bloqueado')
    
    