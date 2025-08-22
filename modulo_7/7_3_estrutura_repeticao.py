# Aula 7.3. Estruturas de repetição
# for (percorrer listas, range)
# while (repetir enquanto uma condição for verdadeira)

maca = {
    "Nome": "Maçã",
    "Preco": 2.5,
    "Promocao": True
}
print(maca)

banana = {
    "Nome": "Banana",
    "Preco": 1.2,
    "Promocao": False
}
print(banana)


pera = {
    "Nome": "Pera",
    "Preco": 3.0,
    "Promocao": True
}
print(pera)

frutas = [maca, banana, pera]
print(frutas)

# Percorrer a lista com um loop for
print("\nFrutas disponíveis:")
for fruta in frutas:
    print(fruta)
    if fruta["Promocao"]:
        print("Esta fruta está em promoção!")

print("\nFrutas em promoção:")
frutas_em_promocao = []
for fruta in frutas:
    if fruta["Promocao"]:
        frutas_em_promocao.append(fruta)
        print(fruta)

# Percorrer a lista com um loop while
print("\nFrutas fora da promoção:")
frutas_fora_da_promocao = []
i = 0
while i < len(frutas):
    if not frutas[i]["Promocao"]:
        frutas_fora_da_promocao.append(frutas[i])
        print(frutas[i])
    i += 1