N = int(input("Quantos números deseja digitar? "))

# Primeiro número fora do laço
num = int(input("Digite o 1º número: "))
menor = num
maior = num
soma = num

# Agora continua do 2º número em diante
for i in range(1, N):
    num = int(input(f"Digite o {i+1}º número: "))

    # compara para achar menor e maior
    if num < menor:
        menor = num
    if num > maior:
        maior = num

    # soma os valores
    soma = soma + num

print("Menor:", menor)
print("Maior:", maior)
print("Soma:", soma)
