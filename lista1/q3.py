# Programa para verificar se uma letra é vogal ou consoante
vogais= 'aeiouAEIOU'
letra=input('digite alguma letra: ')
if letra in vogais:
    print(f'A letra {letra} é uma vogal')
else:
    print(f'A letra {letra} é uma consoante')
 
#  ou

# letra = input("Digite uma letra: ").lower()

# if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
#     print("Vogal")
# else:
#     print("Consoante")
