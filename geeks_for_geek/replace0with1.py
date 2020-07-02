def replace0with5(number):
    number += calculateAddedValue(number)
    return number


def calculateAddedValue(number):


    result = 0


    decimalPlace = 1
 
    if (number == 0):
        result += (5 * decimalPlace)

    while (number > 0):
        if (number % 10 == 0):


            result += (5 * decimalPlace)


        number //= 10
        decimalPlace *= 10

    return result


print(replace0with5(1020))
