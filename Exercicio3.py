"""3) Crie um programa que leia quanto dinheiro uma pessoa tem na carteira, e calcule quanto poderia comprar de cada moeda estrangeira. Considere a tabela de conversão abaixo:

Valor convertido em real:

Dólar Americano: 4,91
Peso Argentino: 0,02
Dólar Australiano: 3,18
Dólar Canadense: 3,64
Franco Suiço: 0,42
Euro: 5,36
Libra esterlina: 6,21"""

def calcular_conversao(valor_em_real):
    conversoes = {
        'Dólar Americano': valor_em_real / 4.91,
        'Peso Argentino': valor_em_real / 0.02,
        'Dólar Australiano': valor_em_real / 3.18,
        'Dólar Canadense': valor_em_real / 3.64,
        'Franco Suiço': valor_em_real / 0.42,
        'Euro': valor_em_real / 5.36,
        'Libra esterlina': valor_em_real / 6.21
    }
    return conversoes

valor_em_reais = float(input("Digite o valor em reais a ser convertido: "))

resultados = calcular_conversao(valor_em_reais)
print("\nValor convertido para outras moedas:")
for moeda, valor in resultados.items():
    print(f"{moeda}: {valor:.2f}")
