# Complete the repeatedString function below.
def repeatedString(string, number):
    a_inString = string.count('a')

    a_in_repeated_String = a_inString * ((n // len(string))-1)

    a_inLeftoverString = string[:n % len(string)].count('a')

    return a_inString  + a_inLeftoverString + a_in_repeated_String


if __name__ == '__main__':

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    print(result)
