N = int(input("Quantos números deseja digitar? "))

# Lê o primeiro número, garantindo que esteja no intervalo
num = int(input("Digite o 1º número (entre 0 e 1000): "))
while num < 0 or num > 1000:
    print("Número fora do intervalo! Digite novamente.")
    num = int(input("Digite o 1º número (entre 0 e 1000): "))

menor = num
maior = num
soma = num

# Continua o loop do 2º número em diante
for i in range(1, N):
    num = int(input(f"Digite o {i+1}º número (entre 0 e 1000): "))

    # verifica se está no intervalo
    while num < 0 or num > 1000:
        print("Número fora do intervalo! Digite novamente.")
        num = int(input(f"Digite o {i+1}º número (entre 0 e 1000): "))

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
