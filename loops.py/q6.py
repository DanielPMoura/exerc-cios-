print('------------------Bem vindo ao GAME-----------------------------')
import os
import random

num=[]
for x in range(1,101):
    num.append(x)
    
sorteio=random.choice(num)

while True:
    valor=int(input('Digite um valor '))
    os.system('cls')
      

    if (valor<sorteio):
        print('numero é maior')
    
    elif(valor>sorteio):
      print('o numero é menor')
    
    elif(valor==sorteio):
        print('parabens')
    
    