# Programa de investigação sobre crime ( pesquisei pra tirar duvida do asssunto "listas".

print("Responda com SIM ou NAO")

perguntas = [
    "Telefonou para a vítima? ",
    "Esteve no local do crime? ",
    "Mora perto da vítima? ",
    "Devia para a vítima? ",
    "Já trabalhou com a vítima? "
]

respostas_positivas = 0

for pergunta in perguntas:
    resposta = input(pergunta)
    if resposta == "sim":
        respostas_positivas += 1

# Classificação
if respostas_positivas == 2:
    classificacao = "Suspeita"
elif respostas_positivas == 3 or respostas_positivas == 4:
    classificacao = "Cúmplice"
elif respostas_positivas == 5:
    classificacao = "Assassino"
else:
    classificacao = "Inocente"

print(f"\nClassificação: {classificacao}")
