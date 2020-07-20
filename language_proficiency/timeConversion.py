
def timeConversion(timeIn12):
    amOrPm = timeIn12[-2:]
    time_Stringlist = timeIn12.split(':')

    if amOrPm =='PM':
        if time_Stringlist[0] == '12':
            timeCalc = '12'
        else:
            timeCalc = str(int(time_Stringlist[0]) + 12)

        time_Stringlist[0] = timeCalc

    elif amOrPm == 'AM':
        timeCalc = time_Stringlist[0]

        if timeCalc == '12':
            timeCalc = '00'
        else:
            timeCalc = str(timeCalc)
        time_Stringlist[0] = timeCalc



    return ":".join(time_Stringlist)[:-2]


if __name__ == '__main__':


    s = input()

    result = timeConversion(s)

    print(result)
