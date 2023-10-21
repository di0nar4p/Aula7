import os
def somar(num1:int, num2:int) -> int:
    return num1 + num2

def subtrair(num1:int,num2:int) -> int:
    return num1 - num2

def multiplicar(num1:int, num2:int) -> int:
    return num1 * num2

def dividir(num1:int, num2:int) -> int:
    if num2 == 0:
        return "OPERAÇÃO INVÁLIDA!"
    else:
        return num1 / num2

while True:
    print('''
                                    =========== CALCULADORA ===========
          
         
          1- SOMA
          2- SUBTRAÇÃO
          3- MULTIPLICAÇÃO
          4- DIVISÃO

          0- SAIR
          ''')


    op= int(input('\nDigite o número da operação que deseja: '))


    match op:


        case 1:
            num1 = int(input('Digite o primeiro valor: '))
            num2 = int(input('Digite o segundo valor: '))
            total = somar(num1, num2)

            print(f'\nA soma de {num1} + {num2} = {total}')
            loop = input('\nDeseja fazer outra operação? (S/N)  ').upper()
            if loop == 'N':
                break
            else:
                os.system('cls') 

        case 2:
            num1 = int(input('Digite o primeiro valor: '))
            num2 = int(input('Digite o segundo valor: '))
            total = subtrair(num1, num2)

            print(f'\nA subtração de {num1} - {num2} = {total}')
            loop = input('\nDeseja fazer outra operação? (S/N)  ').upper()
            if loop == 'N':
                break
            else:
                os.system('cls') 

        case 3:
            num1 = int(input('Digite o primeiro valor: '))
            num2 = int(input('Digite o segundo valor: '))
            total = multiplicar(num1, num2)

            print(f'\nA soma de {num1} * {num2} = {total}')
            loop = input('\nDeseja fazer outra operação? (S/N)  ').upper()
            if loop == 'N':
                break
            else:
                os.system('cls') 

        case 4:
            num1 = int(input('Digite o primeiro valor: '))
            num2 = int(input('Digite o segundo valor: '))
            total = dividir(num1, num2)

            print(f'\nA soma de {num1} / {num2} = {total}')
            loop = input('\nDeseja fazer outra operação? (S/N)  ').upper()
            if loop == 'N':
                break
            else:
                os.system('cls')