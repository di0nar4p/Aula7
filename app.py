import os
def soma(num1:int,num2:int) -> int:
    return num1+num2

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
            num1= int(input('Digite o primeiro valor: '))
            num2= int(input('Digite o segundo valor: '))
            total= soma(num1,num2)

            print(f'\nA soma de {num1} + {num2}= {total}')
            loop= input('\nDeseja fazer outra operação? (S/N)  ').upper()
            if loop == 'N':
                break
            else:
                os.system('cls') 