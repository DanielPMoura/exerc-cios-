print('----------------------------Bem-vindo-------------------------------')

nome=input('Digite o nome do aluno: ')
def escola(u1,u2,u3,u4):
    media = (u1+u2+u3+u4)/4
    if (media>=6):
     print(f'A média do Aluno {nome} é de {media:.1f},parabens!!')
    
    else:
     print(f'O aluno {nome} não passou, e sua média foi{media:.1f}')
       
u1=float(input('Digite a sua nota da 1°unidade'))
u2=float(input('Digite a sua nota da 2°unidade'))
u3=float(input('Digite a sua nota da 3°unidade'))
u4=float(input('Digite a sua nota da 4°unidade'))

escola(u1, u2, u3, u4)