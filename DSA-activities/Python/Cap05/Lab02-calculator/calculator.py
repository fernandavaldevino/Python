from os import system, name
import constant

# screen cleaning function after each run
def clean_screen():
    if name == 'nt':        # Windows
        _ = system('cls')
    else:                   # Linux and MacOS
        _ = system('clear')

def inputNumbers():
    n1 = float(input('\nInforme o primeiro número: '))
    n2 = float(input('\nInforme o segundo número: '))
    return n1,n2

def soma():
    x,y = inputNumbers()
    print(f'\n{x} + {y} = {x+y}\n\n')

def subtracao():
    x,y = inputNumbers()
    print(f'\n{x} - {y} = {x-y}\n\n')

def multiplicacao():
    x,y = inputNumbers()
    print(f'\n{x} x {y} = {x*y}\n\n')

def divisao():
    x,y = inputNumbers()
    if y != 0:
        print(f'\n{x} ÷ {y} = {round(float(x)/y, 2)}\n\n') 
    else:
        print(f'\n{x} ÷ {y} = X (it\'s not possible :)')

def calculator():
    clean_screen()
    print(constant.WELCOME_TEXT)
    print(constant.INITIAL_TEXT)
    option = int(input('Informe a sua opção: '))

    if option < 0 or option > 4:
        while(True):
            print('\n>>>>> Opção inválida! <<<<<\n')
            option = int(input('Informe a sua opção corretamente: '))
            if option >= 0 and option <= 4:
                break
    
    if option == 0:
        exit
    elif option == 1:
        soma()
    elif option == 2:
        subtracao()
    elif option == 3:
        multiplicacao()
    elif option == 4:
        divisao()       
        


if __name__ == '__main__':
    calculator()