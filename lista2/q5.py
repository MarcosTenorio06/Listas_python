nome = input("Digite o nome (maior que 3 caracteres): ")
while len(nome) <= 3:
    print("Nome inválido!")
    nome = input("Digite o nome (maior que 3 caracteres): ")

idade = int(input("Digite a idade (entre 0 e 150): "))
while idade < 0 or idade > 150:
    print("Idade inválida!")
    idade = int(input("Digite a idade (entre 0 e 150): "))

salario = float(input("Digite o salário (maior que zero): "))
while salario <= 0:
    print("Salário inválido!")
    salario = float(input("Digite o salário (maior que zero): "))

sexo = input("Digite o sexo ('f' ou 'm'): ").lower()
while sexo not in ['f', 'm']:
    print("Sexo inválido!")
    sexo = input("Digite o sexo ('f' ou 'm'): ").lower()

estado_civil = input("Digite o estado civil ('s', 'c', 'v', 'd'): ").lower()
while estado_civil not in ['s', 'c', 'v', 'd']:
    print("Estado civil inválido!")
    estado_civil = input("Digite o estado civil ('s', 'c', 'v', 'd'): ").lower()

print("Informações validadas com sucesso!")