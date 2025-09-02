#feita sem pesquisar sobre as listas.
respostas_positivas = 0

resposta = input("Telefonou para a vítima? (sim/não): ")
if resposta == "sim":
    respostas_positivas += 1

resposta = input("Esteve no local do crime? (sim/não): ")
if resposta == "sim":
    respostas_positivas += 1

resposta = input("Mora perto da vítima? (sim/não): ")
if resposta == "sim":
    respostas_positivas += 1

resposta = input("Devia para a vítima? (sim/não): ")
if resposta == "sim":
    respostas_positivas += 1

resposta = input("Já trabalhou com a vítima? (sim/não): ")
if resposta == "sim":
    respostas_positivas += 1

if respostas_positivas == 2:
    classificacao = "Suspeita"
elif respostas_positivas == 3 or respostas_positivas == 4:
    classificacao = "Cúmplice"
elif respostas_positivas == 5:
    classificacao = "Assassino"
else:
    classificacao = "Inocente"

print("Classificação: ", classificacao)