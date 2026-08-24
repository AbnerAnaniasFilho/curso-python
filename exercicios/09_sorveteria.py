#Faça o programa de uma sorveteria, onde o usuário pode escolher:
# Tipo de sorvete: casquinha (R$1,00), cascão (R$2,50), cestinha (R$4,00)
# Sabor do sorvete: morango, creme, chocolate
# Cobertura: caramelo (R$1,50), morango (R$1,50), chocolate (R$1,50), sem cobertura (R$0,00)
# Apresente o valor a ser pago

texto = """
Escolha um tipo de sorvete:
(01) casquinha (R$1,00) 
(02) cascão (R$2,50)
(03) cestinha (R$4,00)
"""

tipo = input(texto)

texto = """
Escolha um tipo de sorvete:
(01) morango 
(02) creme
(03) chocolate
"""

sabor = input(texto)

texto = """
Escolha uma cobertura para o sorvete:
(01) caramelo (R$1,50) 
(02) morango (R$1,50)
(03) chocolate (R$1,50)
(04) sem cobertura (R$0,00)
"""

cobertura = input(texto)

valor_pago = 0

if tipo == "01":
    valor_pago = 1

elif tipo == "02":
    valor_pago = 2.5

elif tipo == "03":
    valor_pago = 4

if cobertura in ("01", "02", "03"):
    valor_pago += 1.5

print("O valor a ser pago é de R$", valor_pago)