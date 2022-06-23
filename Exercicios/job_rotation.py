# Observe o trecho de código abaixo:
#
# int INDICE = 13, SOMA = 0, K = 0;
# enquanto K < INDICE faça
# {
# K = K + 1;
# SOMA = SOMA + K;
# }
# imprimir(SOMA);
#
# Ao final do processamento, qual será o valor da variável SOMA?
indice = int('13')
soma = int('0')
k = int('0')

while k < indice:
    k = k + 1
    soma = soma + k
    print(soma)

