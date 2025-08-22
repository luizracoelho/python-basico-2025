# Aula 7.4. Controle de fluxo
# break (interrompe o loop)
# continue (pula para a próxima iteração)

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

# Exemplo de uso do break
print("\nExemplo de uso do break:")
for fruta in frutas:
    if fruta["Nome"] == "Banana":
        break
    print(fruta)

# Exemplo de uso do continue
print("\nExemplo de uso do continue:")
for fruta in frutas:
    if not fruta["Promocao"]:
        continue
    print(fruta)

# Exemplo utilizando um while true
carrinho = []
print("\nCardápio de frutas:\n=====================")
for index, fruta in enumerate(frutas):
    print(f"[{index + 1}] {fruta['Nome']} - R${fruta['Preco']:.2f}")

while True:
    opcao = int(input("\nEscolha qual fruta você deseja digitando o número correspondente. Caso você queira finalizar sua compra, digite 0:"))

    if opcao == 0:
        break

    indice = opcao - 1

    if 0 <= indice < len(frutas):
        carrinho.append(frutas[indice])
        print(f"Você adicionou {frutas[indice]['Nome']} ao carrinho.")
    else:
        print("Opção inválida. Tente novamente.")

print("\nCarrinho de compras:\n=====================")
for item in carrinho:
    print(f"- {item['Nome']} - R${item['Preco']:.2f}")
