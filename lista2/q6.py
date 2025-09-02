num = int(input("Digite um número inteiro: "))

eh_primo = True  # assumimos que é primo até provar o contrário

if num < 2:  # 0 e 1 não são primos
    eh_primo = False
else:
    for i in range(2, num):
        if num % i == 0:  # se achar algum divisor além de 1 e ele mesmo
            eh_primo = False
            break

if eh_primo:
    print("É primo")
else:
    print("Não é primo")
