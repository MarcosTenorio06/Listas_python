#sobre nota media dos alunos
nota1=float(input('Digite a primeira nota: '))
nota2=float(input('Digite a segunda nota: '))
media=(nota1+nota2)/2
if media==10:
    print('aprovado com distinção')
if media>=7:
    print('aprovado')
elif media>=7:
    print('reprovado') 
