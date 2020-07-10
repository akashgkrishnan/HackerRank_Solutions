def checkMagazine(magazine, note):
    magazine_dict = dict()
    note_dict = dict()
    for item in magazine:
        if item in magazine_dict:
            magazine_dict[item] += 1
        else:
            magazine_dict[item] = 1

    for item in note:
        if item in note_dict:
            note_dict[item] += 1
        else:
            note_dict[item] = 1

    for key, value in note_dict.items():
        if key in magazine_dict:
            if value > magazine_dict[key]:
                return 'NO'
        else:
            return 'NO'
    return 'YES'


if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    print(checkMagazine(magazine, note))
