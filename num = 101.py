num = 101

while True:
    if num % 7 == 0 and num % 3 == 0:
        print("O primeiro número acima de 100 divisível por 7 e por 3 é:", num)
        break  
    num += 1  
    notas = [8.5, 4.0, 10.0, 7.5, 6.0, 9.0]

soma = 0
contador_aprovadas = 0

for nota in notas:
    soma += nota
    if nota >= 7.0:
        contador_aprovadas += 1

media = soma / len(notas)

print("Média das notas:", media)
print("Quantidade de notas >= 7.0:", contador_aprovadas)

lista_A = [1, 2, 3, 4, 5]
lista_B = [4, 5, 6, 7, 8]
comuns = []

for elemento in lista_A:
    if elemento in lista_B:
        comuns.append(elemento)

print("Elementos comuns às duas listas:", comuns)

estoque = [
    {"nome": "Teclado", "preco": 150.00, "quantidade": 5},
    {"nome": "Mouse", "preco": 80.00, "quantidade": 12},
    {"nome": "Monitor", "preco": 700.00, "quantidade": 3},
    {"nome": "Headset", "preco": 250.00, "quantidade": 8}
]

valor_total_estoque = 0

print("Resumo do estoque:\n")

for item in estoque:
    valor_produto = item["preco"] * item["quantidade"]
    valor_total_estoque += valor_produto
    print(f"{item['nome']}: {item['quantidade']} unidades x R$ {item['preco']:.2f} = R$ {valor_produto:.2f}")

    num = 101  

while True:
    if num % 7 == 0 and num % 3 == 0:  
        print("O primeiro número acima de 100 divisível por 7 e por 3 é:", num)
        break  
    num += 1  

    sku = "PRD-004-A-v2"


sku_limpo = sku.replace("-", "").upper()

print("SKU formatado:", sku_limpo)