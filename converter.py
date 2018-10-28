from textwrap import dedent
from dectobin import *
from dectooct import *
from dectohex import *
from bintodec import *
from octtodec import *


# Check if it is a valid input
def check_if_number(check):
        try:
            val = int(check)
            return val
        except ValueError:
            return 0


# MAIN FUNCTION
def main():
    number_systems = ['Decimal', 'Binary', 'Octal', 'Hexadecimal']
    print(dedent("""
            -------------------------
            |NUMBER SYSTEM CONVERTER|
            -------------------------
    """))

    for i, j in zip(range(len(number_systems)), number_systems):
        print(f"{i + 1}. {j}\n")

    while True:
        user_input = input('> ')
        choice = check_if_number(user_input)

        if choice == 0:
            print('Invalid')
        else:
            if 0 < choice < 5:
                break
            else:
                print('Invalid!')

    if choice == 1: # Decimal
        print("Convert to:\n")

        for i, j in zip(range(len(number_systems)), number_systems[1:]):
            print(f"{i + 1}. {j}\n")

        while True:
            user_input = input('> ')
            convert = check_if_number(user_input)

            if convert == 0:
                print('Invalid!')
            else:
                if 0 < convert < 4:
                    break
                else:
                    print('Invalid!')

        if convert == 1: # Binary
            print("Decimal to Binary: ")
            while True:
                given = input('> ')
                try:
                    val = int(given)
                    break
                except ValueError:
                    print("Invalid!")
            print(dec_to_bin(val))

        elif convert == 2: #Octal
            print("Decimal to Octal: ")
            while True:
                given = input('> ')
                try:
                    val = int(given)
                    break
                except ValueError:
                    print("Invalid!")
            print(dec_to_oct(val))

        else: # Hexadecimal
            print("Decimal to Hexadecimal: ")
            while True:
                given = input('> ')
                try:
                    val = int(given)
                    break
                except ValueError:
                    print("Invalid!")
            print(dec_to_hex(val))

    elif choice == 2: # Binary
        print("Convert to:\n")
        for i, j in zip(range(len(number_systems)), number_systems[:1]+number_systems[2:]):
            print(f"{i + 1}. {j}\n")

        while True:
            user_input = input('> ')
            convert = check_if_number(user_input)

            if convert == 0:
                print('Invalid!')
            else:
                if 0 < convert < 4:
                    break
                else:
                    print('Invalid!')

        if convert == 1: # Decimal
            print("Binary to Hexadecimal: ", end = '')


        elif convert == 2: # Octal
            pass
        else: # Hexadecimal
            pass

    elif choice == 3: # Octal
        print("Convert to:")
        for i, j in zip(range(len(number_systems)), number_systems[:2]+number_systems[3:]):
            print(f"{i + 1}. {j}")
    else: # Hexadecimal
        for i, j in zip(range(len(number_systems)), number_systems[:3]):
            print(f"{i + 1}. {j}")

main()



# This is the formula for checking hexa symbols
#hex_symbols = ['1', '2', '3', '4', '5', '6', '7', '8',
#               '9', 'A', 'B', 'C', 'D', 'E', 'F']
#while True:
#    given = input('> ')
#    val = []
#    for i in given:
#        if i in hex_symbols:
#            val.append(i)
#        else:
#            break
#    value = ''.join(val)
#    if value == given:
#        break
#    else:
#        print('Invalid!')

#print(hex_to_dec(value))
