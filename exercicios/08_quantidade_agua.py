# Altere o programa anterior para considerar a quantidade de garrafas de água

texto = """
Escolha a sua água para comprar:
(1) Água mineral natural - R$ 1,50
(2) Água mineral com gás - R$ 2,50
"""

opcao = input(texto)

valor_item = 0

if opcao == "1":
    valor_item = 1.5

elif opcao == "2":
    valor_item = 2.5

if valor_item == 0:
    print("Entre com uma opção das opções disponíveis, por favor!")

else:
    quantidade = input("Quantas garrafas? ")
    quantidade = int(quantidade)

    conta = valor_item * quantidade
    print("Sua conta deu: R$", conta)