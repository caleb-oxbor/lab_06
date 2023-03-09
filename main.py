# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def encode(origin):
    coded = ''
    for char in origin:
        coded += str(int(char) + 3) if '0' <= char <= '6' else '9'
    return coded


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
