from os import system, name
import constant

# screen cleaning function after each run
def clean_screen():
    if name == 'nt':        # Windows
        _ = system('cls')
    else:                   # Linux and MacOS
        _ = system('clear')

def inputNumbers():
    while(True):
        try:
            n1 = float(input('\nInput the first number: '))
            n2 = float(input('\nInput the second number: '))
            break
        except ValueError:
            print('\n>>>>> You didn\'t put a number. Try again! <<<<<\n')
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
    while(True):
        try:
            print(f'\n{x} ÷ {y} = {round(float(x)/y, 2)}\n\n')
            break
        except ZeroDivisionError:
            print(f'\n{x} ÷ {y} = X (it\'s not possible to divide by zero :)\n')
            break

def calculator():
    clean_screen()
    print(constant.WELCOME_TEXT)
    print(constant.INITIAL_TEXT)

    while(True):
        try:
            option = int(input('Input your option: '))
            break
        except ValueError:
            print('\n>>>>> You didn\'t put a number. Try again! <<<<<\n')

    if option < 0 or option > 4:
        while(True):
            print('\n>>>>> Invalid option! <<<<<\n')
            option = int(input('Input your correct option: '))
            if option >= 0 and option <= 4:
                break
    
    if option == 0:
        print('\nBye bye\n')
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