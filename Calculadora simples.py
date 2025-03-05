num1 = float(input('Digite um número:'))
num2 = float(input('Digite um número:'))

operacoes = input('Escolha qual operação deseja fazer:, (+, -, /, *)')

if operacoes == '+':
    resultado = num1 + num2
    print('O resultado da soma é:', resultado)
elif operacoes == '-':
    resultado = num1 - num2
    print('O resultado da subtração é:', resultado)
elif operacoes == '/':
    resultado = num1 / num2
    print('O resultado da divisão é:', resultado)
elif operacoes == '*':
    resultado = num1 * num2
    print('O resultado da multiplicação é:', resultado)
else:
    print('Refaça a operação!')
    