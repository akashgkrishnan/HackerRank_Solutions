def hulkSpeech(n):
    if n == 1:
        return 'I hate it'
    if n == 2:
        return 'I hate that I love it'

    prefix = ['I hate ', 'I love ']
    if n % 2 == 0:
        return "that ".join(prefix * (n//2)) + 'it'
    else:
        return "that ".join(prefix * (n//2)) + 'that I hate it'






n = int(input())
print(hulkSpeech(n))
