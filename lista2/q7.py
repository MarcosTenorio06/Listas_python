N = int(input("Quantos números deseja digitar? "))
numeros = []

for i in range(N):
    num = int(input(f"Digite o {i+1}º número: "))
    numeros.append(num)

print("Menor:", min(numeros))
print("Maior:", max(numeros))
print("Soma:", sum(numeros))
