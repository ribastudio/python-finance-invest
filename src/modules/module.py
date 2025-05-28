def calc_capital_produto(produtos):
    alocacoes = {}

    for nome in produtos:
            percentual = float(input(f"Percentual para {nome}: "))
            alocacoes[nome] = percentual / 100

    # Validação da soma
    if round(sum(alocacoes.values()), 2) != 1.0:
        print("\n❌ Erro: A soma dos percentuais deve ser 100%. Encerrando programa.")
        exit()
    
    return alocacoes
