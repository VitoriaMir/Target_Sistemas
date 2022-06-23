# 4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
# SP – R$67.836,43
# RJ – R$36.678,66
# MG – R$29.229,88
# ES – R$27.165,48
# Outros – R$19.849,53
# Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro
# do valor total mensal da distribuidora.
#  
estado = [{'SP': float('67.83643'), 'RJ': float('36.67866'), 'MG': float('29.22988'), 'ES': float('27.1654'), 'Outros': float('19.84953')}]

for state in estado:
    total = sum(state.values())
    for key, value in state.items():
        soma = (value / total) * 100
        print(f'Porcentagem de {key}: {soma:.2f}%')
