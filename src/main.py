import random

from modules.module import calc_capital_produto
from products.main import crip_rendimento, fags_rendimento, globeco_rendimento, imobfacil_rendimento, tds_rendimento

# Dicionário com todos os produtos e suas funções
produtos = {
    'TDS': tds_rendimento,
    'FAGS': fags_rendimento,
    'CRIP': crip_rendimento,
    'IMOBFÁCIL': imobfacil_rendimento,
    'GLOBECO': globeco_rendimento
}

# --- Entrada do Usuário ---

def main():
    # Valor inicial do investimento
    capital_inicial = float(input("Digite o valor que deseja investir: R$ "))

    # Tempo de simulação (em anos)
    anos = int(input("Por quantos anos deseja simular o investimento? "))

    # Alocação em percentual para cada produto
    print("\nDistribua o capital entre os 5 produtos (a soma deve ser 100%).")
    dist_produto = calc_capital_produto(produtos)

    # --- Simulação Ano a Ano ---
    valores = {}

    # Inicializa os valores com base na alocação
    for nome in produtos:
        valores[nome] = capital_inicial * dist_produto[nome]

    # Mostra os valores iniciais
    print("\n💰 Situação Inicial:")
    for nome, valor in valores.items():
        print(f"{nome}: R$ {valor:.2f}")

    # Simula ano a ano
    for ano in range(1, anos + 1):
        print(f"\n📅 Ano {ano}:")
        for nome in produtos:
            funcao = produtos[nome]
            valores[nome] = funcao(valores[nome])  # Aplica rendimento
            print(f"{nome}: R$ {valores[nome]:.2f}")

    # Total final
    total_final = sum(valores.values())
    print(f"\n🏁 Total final após {anos} anos: R$ {total_final:.2f}")