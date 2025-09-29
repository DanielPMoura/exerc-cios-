# Faça um programa que armazene os nomes de 5 alunos em uma lista e depois
# exiba esses nomes um por um.

nomes=[]
for x in range(5):
    n=input('Digite um nome: ')
    nomes.append(n)
    
for x in nomes:
    print(x)