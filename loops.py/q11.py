# Crie um programa que solicite 10 números ao usuário, armazene-os em uma lista
# e exiba apenas os números pares.

numero=[]

for x in range (10):
    valor=int(input('Digite um valor: '))
  
    if valor%2==0:
        numero.append(valor)
        
print(numero)
        
        
        