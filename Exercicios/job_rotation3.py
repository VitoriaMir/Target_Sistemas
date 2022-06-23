# 3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que
# desejar, que calcule e retorne:
# • O menor valor de faturamento ocorrido em um dia do mês;
# • O maior valor de faturamento ocorrido em um dia do mês;
# • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

# IMPORTANTE:
# a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
# b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no
# cálculo da média;
import json

with open('dados.json', encoding='utf-8') as arquivo:
    dados = json.load(arquivo)

# • O menor valor de faturamento ocorrido em um dia do mês;
valor = []
for dado in dados:
    if dado['valor'] == float('0.0'):
        continue
    else:
        valor.append(dado['valor'])

menor = min(valor)
menor_dia = [dado for dado in dados if dado['valor'] == menor]
print(f'O menor valor de faturamento ocorrido em um dia do mês é {menor_dia[0]["valor"]} no dia {menor_dia[0]["dia"]}.')

# • O maior valor de faturamento ocorrido em um dia do mês;
maior = max(valor)
maior_dia = [dado for dado in dados if dado['valor'] == maior]
print(f'O maior valor de faturamento ocorrido em um dia do mês é {maior_dia[0]["valor"]} no dia {maior_dia[0]["dia"]}.')

# • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.
media_mensal = sum(valor) / len(valor)
media_dia = [dado for dado in dados if dado['valor'] > media_mensal]
print(f'Número de dias no mês em que o valor de faturamento diário foi superior à média mensal: {len(media_dia)}')

arquivo.close()
