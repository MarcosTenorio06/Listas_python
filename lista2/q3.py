while True:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = num1 + num2
    print(f"Resultado: {num1} + {num2} = {resultado}")
    continuar = input("Deseja continuar? (s/n): ").lower()
    if continuar != 's':
        break