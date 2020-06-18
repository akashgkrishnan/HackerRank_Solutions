s = input()
small_letters = []
caps_letters = []
digits = []


for letter in s:
    if letter.islower():
        small_letters.append(letter)

    elif letter.isupper():
        caps_letters.append(letter)

    elif letter.isdigit():
        digits.append(letter)


small_letters.sort()
caps_letters.sort()
digits.sort()

odd = []
even = []

for i in digits:
    if int(i) % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

odd.extend(even)

small_letters.extend(caps_letters)
small_letters.extend(odd)

print("".join(small_letters))
