def formatIntToTimeString(timeInt):
    hour = str(timeInt)[0: len(str(timeInt))-2]
    min = str(timeInt)[len(str(timeInt))-2: len(str(timeInt))]
    return hour + ':' + min

def displaySchedule(list):
    print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
    print('SCHEDULE:')
    for i in range(len(list[0])):
        print('- ' + formatIntToTimeString(list[0][i]) + ' --> ' + formatIntToTimeString(list[1][i]) + ': ' + list[2][i])

    print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')