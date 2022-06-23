# 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores
# anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde,
# informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado
# pertence ou não a sequência.

numero = int(input('Digite um número de 0 a 1000: '))

if numero < 0 or numero > 1000:
    print('Número inválido!')
else:
    fibonacci = [0, 1]
    cont = 0
    while numero > cont:
        cont = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(cont)

        if cont > numero:
            print(f'O número {numero} não pertence à sequência de Fibonacci!')
            break
        elif numero == cont:
            print(f'O número {numero} pertence à sequência de Fibonacci!')
            break
