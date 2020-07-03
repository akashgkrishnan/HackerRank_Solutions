def pangrams(string):
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    dictionary = {k: False for k in alphabets}

    for item in string:
        if item.lower() in dictionary:
            dictionary[item.lower()] = True

    if all(dictionary.values()):
        return 'pangram'
    return 'not pangram'
print(pangrams('We promptly judged antique ivory buckles for the prize'))
