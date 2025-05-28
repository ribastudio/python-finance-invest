# TDS - Tesouro Direto Simples (renda fixa)
import random


def tds_rendimento(valor):
    taxa = 0.08  # 8% ao ano
    return valor * (1 + taxa)

# FAGS - Fundo de Ações de Grandes Setores (renda variável)
def fags_rendimento(valor):
    taxa = random.uniform(-0.05, 0.15)  # -5% a +15%
    return valor * (1 + taxa)

# CRIP - CriptoSimples (renda variável de alto risco)
def crip_rendimento(valor):
    taxa = random.uniform(-0.30, 0.40)  # -30% a +40%
    return valor * (1 + taxa)

# IMOBFÁCIL - Fundo Imobiliário Acessível (renda fixa)
def imobfacil_rendimento(valor):
    taxa = 0.075  # 7.5% ao ano
    return valor * (1 + taxa)

# GLOBECO - Fundo Global Econômico (renda variável moderada)
def globeco_rendimento(valor):
    taxa = random.uniform(0.01, 0.12)  # +1% a +12%
    return valor * (1 + taxa)