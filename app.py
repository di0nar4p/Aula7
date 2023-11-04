import os
import math as m

def soma(num1: int, num2: int) -> int:
    return num1 + num2

def subtracao(num1: int, num2: int) -> int:
    return num1 - num2

def multiplicacao(num1: int, num2: int) -> int:
    return num1 * num2

def divisao(num1: int, num2: int) -> int:
    try:
        if num2 == 0:
            raise ZeroDivisionError
    except ZeroDivisionError:
        return 'Não é possível dividir um valor por zero!'
    return num1 / num2

memoria = []  # memória


while True:
    print('''
                          =========== CALCULADORA ===========


          1- SOMA
          2- SUBTRAÇÃO
          3- MULTIPLICAÇÃO
          4- DIVISÃO
          5- POTÊNCIA
          6- SENO
          7- COSENO
          8- TANGENTE
          9- MEMÓRIA

          0- SAIR
          ''')

    op = int(input('\nDigite o número da operação que deseja: '))

    match op:
        case 1:
            num1 = int(input('Digite o primeiro valor: '))
            num2 = int(input('Digite o segundo valor: '))
            total = soma(num1, num2)

            print(f'\nA soma de {num1} + {num2} = {total}')
            
            mem= input('\nDeseja armazenar o valor? (S/N)  ').upper()
            if mem== 'N':
                continue
            else:
                memoria.append(total)

            loop= input('\nDeseja fazer outra operação? (S/N)  ').upper()
            if loop == 'N':
                break
            else:
                os.system('cls') 
        case 2:
            num1 = int(input('Digite o primeiro valor: '))
            num2 = int(input('Digite o segundo valor: '))
            total = subtracao(num1, num2)

            print(f'\nA subtração de {num1} - {num2} = {total}')
            mem= input('\nDeseja armazenar o valor? (S/N)  ').upper()
            if mem== 'N':
                continue
            else:
                memoria.append(total)

            loop= input('\nDeseja fazer outra operação? (S/N)  ').upper()
            if loop == 'N':
                break
            else:
                os.system('cls') 

        case 3:
            num1 = int(input('Digite o primeiro valor: '))
            num2 = int(input('Digite o segundo valor: '))
            total = multiplicacao(num1, num2)

            print(f'\nA multiplicação de {num1} x {num2} = {total}')
            mem= input('\nDeseja armazenar o valor? (S/N)  ').upper()
            if mem== 'N':
                continue
            else:
                memoria.append(total)

            loop= input('\nDeseja fazer outra operação? (S/N)  ').upper()
            if loop == 'N':
                break
            else:
                os.system('cls') 

        case 4:
            num1 = int(input('Digite o primeiro valor: '))
            num2 = int(input('Digite o segundo valor: '))
            total = divisao(num1, num2)

            print(f'\nA divisão de {num1} ÷ {num2} = {total}')
            mem= input('\nDeseja armazenar o valor? (S/N)  ').upper()
            if mem== 'N':
                continue
            else:
                memoria.append(total)

            loop= input('\nDeseja fazer outra operação? (S/N)  ').upper()
            if loop == 'N':
                break
            else:
                os.system('cls') 

        case 5:
            num1 = int(input('Digite o número a ser calculado: '))
            num2 = int(input('Digite a potência desejada: '))
            total = m.pow(num1, num2)

            print(f'O número {num1} elevado à potência de {num2} é: {total}')
            mem= input('\nDeseja armazenar o valor? (S/N)  ').upper()
            if mem== 'N':
                continue
            else:
                memoria.append(total)

            loop= input('\nDeseja fazer outra operação? (S/N)  ').upper()
            if loop == 'N':
                break
            else:
                os.system('cls') 

        case 6:
            num1 = float(input('Informe o valor do ângulo: '))
            total = m.sin(num1)
            print(f'Seno de {num1}º é igual a {total:.10f} radianos.')
            mem= input('\nDeseja armazenar o valor? (S/N)  ').upper()
            if mem== 'N':
                continue
            else:
                memoria.append(total)

            loop= input('\nDeseja fazer outra operação? (S/N)  ').upper()
            if loop == 'N':
                break
            else:
                os.system('cls') 


        case 7:
            num1 = float(input('Informe o ângulo: '))
            total = m.cos(num1)
            print(f'Coseno de {num1}º é igual a {total} radianos.')
            mem= input('\nDeseja armazenar o valor? (S/N)  ').upper()
            if mem== 'N':
                continue
            else:
                memoria.append(total)

            loop= input('\nDeseja fazer outra operação? (S/N)  ').upper()
            if loop == 'N':
                break
            else:
                os.system('cls') 

        case 8:
            num1 = float(input('Informe o ângulo: '))
            total = m.tan(num1)
            print(f'Tangente de {num1}º é igual a {total} radianos.')
            mem= input('\nDeseja armazenar o valor? (S/N)  ').upper()
            if mem== 'N':
                continue
            else:
                memoria.append(total)

            loop= input('\nDeseja fazer outra operação? (S/N)  ').upper()
            if loop == 'N':
                break
            else:
                os.system('cls') 

        case 9:
            print(*memoria)
            loop = input('\nDeseja fazer outra operação? (S/N)  ').upper()
            if loop == 'N':
                break
            else:
                os.system('cls')

        case 0:
            print('Aplicação encerrada!!')
            break