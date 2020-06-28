
def caesarCipher(string , key):
    if key > 26:

        key = key % 26

    new_string = list(string)

    for i in range(len(string)):
        if new_string[i].isalpha():
            if new_string[i].islower():
                if ord(new_string[i]) + key <= 122:
                    new_string[i] = chr(ord(new_string[i]) + key)
                else:
                    new_string[i] = chr(96 + (ord(new_string[i]) + key - ord('z')))
            else:
                if ord(new_string[i]) + key <= 90:
                    new_string[i] = chr(ord(new_string[i]) + key)
                else:
                    new_string[i] = chr(64 + (ord(new_string[i]) + key - ord('Z')))


    return ''.join(new_string)




if __name__ == '__main__':

    n = int(input())

    s = input()

    k = int(input())

    result = caesarCipher(s, k)

    print(result)
