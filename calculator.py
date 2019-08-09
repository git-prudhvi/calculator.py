"""
- Enter these from the options below:
- Plus (+)
- Minus (-)
- Multiplication (*)
- Division (/)
- Quit (q)
Tasks:
[x]: Show the user the main interface and get their input
[x]: Sum two numbers
[x]: Subtract two numbers
[x]: Multiply two numbers
[x]: Divide the two numbers
[x]: Stop running the program when they 'q'
"""


def menu():
    user_input = ''
    while user_input != 'q':
        print("""- Plus (+)
- Minus (-)
- Multiplication (*)
- Division (/)
- Quit (q)""")

        user_input = input('Enter these from the options above: ')
        user_input = user_input.lower()

        if user_input == '+':
            print(f'result= {plus()}')  # result= 2
        elif user_input == '-':
            print(f'result= {minus()}')  # result= 0
        elif user_input == '*':
            print(f'result= {multiplication()}')  # result= 1
        elif user_input == '/':
            print(f'result= {division()}')  # result= 1  or  result= Dividing by 1 and 0 is not possible
        elif user_input == 'q':
            break  # bye
        else:
            print('Unknown command-please try again.')  # WTF


def plus():  # Sum two numbers
    first_number = int(input('Enter the first number: '))
    second_number = int(input('Enter the second number: '))
    return first_number + second_number  # 1+1


def minus():  # Subtract two numbers
    first_number = int(input('Enter the first number: '))
    second_number = int(input('Enter the second number: '))
    return first_number - second_number  # 1-1


def multiplication():  # Multiply two numbers
    first_number = int(input('Enter the first number: '))
    second_number = int(input('Enter the second number: '))
    return first_number * second_number  # 1*1


def division():  # Divide the two numbers
    first_number = int(input('Enter the first number: '))
    second_number = int(input('Enter the second number: '))
    if second_number != 0:
        return first_number / second_number  # 1/1
    else:
        return f'Dividing by {first_number} and 0 is not possible'  # 1/0


menu()  # open Menu


