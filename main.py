# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def encode(origin):
    coded = ''
    for char in origin:
        coded += str(int(char) + 3) if '0' <= char <= '6' else '9'
    return coded



def decode(encoded_password):
    decoded_string = ''

    for i in encoded_password:




        x = int(i)

        if x < 3:

            second_value = (10+(x - 3))

            decoded_string += str(second_value)

        else:

            y = x - 3

            decoded_string += str(y)



    return decoded_string


def main():
    password = 0
    while True:
        print('''
Menu
------------- 
1. Encode  
2. Decode  
3. Quit''')
        choice = int(input("\nPlease enter an option: "))
        if choice == 1:
            password = input("Please enter your password to encode: ")
            print("Your password has been encoded and stored!")
        elif choice == 2:


            print(f"The encoded password is {encode(str(password))}, and the original password is {password}.")
        elif choice == 3:
            break


if __name__ == "__main__":
    main()
