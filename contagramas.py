# Logica de programacao deste script #
# Resolvendo equação linear com python #
# Objetivo descobrir e expor 2 Valores: O preço do kg(vlkg), O preço da grama(vlgrama).
# Ex: 250g(qtgrama) Custaram 520(b), quanto custa 1kg e 1g?
# Receber os valores de quantidade(qtgrama) e preco(vlgrama) das gramas #
# qtgrama*x=1000 | 
# Precisamos achar o valor do X, para saber quantas gramas(inseridas no input) completam 1kg(1000g)
# vlkg = b*x | O valor da grama vezes X retorna o valor do kg
# vlgrama = vlkg / 1000
print("**************************************")
qtgrama = float(input("*** Insira a quantidade em Gramas:"))
vlgrama = float(input("*** Insira o valor pago nas Gramas:"))
print("**************************************")
qtgrama = int(qtgrama)
vlgrama = int(vlgrama)
# 1000 / qtgrama = b | b * qtgrama = x | r = x / qtgrama
# r = valor a ser multiplicado pra dar 1000
# acha o valor do X #
b = 1000 / qtgrama
x = b * qtgrama
kx = qtgrama / qtgrama
r = kx * qtgrama
solved = x / r
vlkg = vlgrama * solved

print(f'(*) O kg custou {vlkg} (*)')
resultg = int(vlkg) / 1000
print(f"[*] Cada grama custou: {resultg} [*]")
confirma = resultg * qtgrama
# print(f"Confirma quanto você pagou pela multiplicação de {resultg}x{qtgrama}={confirma}")