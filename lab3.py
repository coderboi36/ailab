import string
import itertools
StringArray = [ ['CROSS', 'ROADS'], ['SEND', 'MORE']]
inResultsArray = [ 'DANGER','MONEY']
inPossibleNumsAsStr = '0123456789'
def getNumber(inStr, inDictMapping):
    numAsStr = ''
    for ch in inStr:
        numAsStr = numAsStr + inDictMapping[ch] 
    return int(numAsStr)
def solveCrypt(NumsAsString, inResultStr, inPossibleNumsAsStr):
    nonZeroLetters = []
    strFromStrList = ''
    for numStr in NumsAsString:
        nonZeroLetters.append(numStr[0])
        strFromStrList = strFromStrList + numStr
    nonZeroLetters.append(inResultStr[0])
    strFromStrList = strFromStrList + inResultStr  
    uniqueStrs = ''.join(set(strFromStrList))
    for tup in itertools.permutations(inPossibleNumsAsStr, len(uniqueStrs)):
        dictCharAndDigit = {}
        for i in range(len(uniqueStrs)):
            dictCharAndDigit[uniqueStrs[i]] = tup[i]            
        nonZeroLetterIsZero = False
        for letter in nonZeroLetters:
            if(dictCharAndDigit[letter] == '0'):
                nonZeroLetterIsZero = True
                break
        if(nonZeroLetterIsZero == True):
            continue
        result = getNumber(inResultStr, dictCharAndDigit)     
        testResult = 0
        for numStr in NumsAsString:
            testResult = testResult + getNumber(numStr, dictCharAndDigit)        
        if(testResult == result):
            strToPrint = ''
            for numStr in NumsAsString:
                strToPrint = strToPrint + numStr + '(' + str(getNumber(numStr, dictCharAndDigit)) + ')' + ' + '
            strToPrint = strToPrint[:-3]
            strToPrint = strToPrint + ' = ' + inResultStr + '(' + str(result) + ')'
            print(strToPrint)
            break

for i in range(len(inResultsArray)):
    solveCrypt(StringArray[i], inResultsArray[i], inPossibleNumsAsStr)











def solutions():
    # letters = ('s', 'e', 'n', 'd', 'm', 'o', 'r', 'y')
    all_solutions = list()
    for s in range(9, -1, -1):
        for e in range(9, -1, -1):
            for n in range(9, -1, -1):
                for d in range(9, -1, -1):
                    for m in range(9, 0, -1):
                        for o in range(9, -1, -1):
                            for r in range(9, -1, -1):
                                for y in range(9, -1, -1):
                                    if len(set([s, e, n, d, m, o, r, y])) == 8:
                                        send = 1000 * s + 100 * e + 10 * n + d
                                        more = 1000 * m + 100 * o + 10 * r + e
                                        money = 10000 * m + 1000 * o + 100 * n + 10 * e + y

                                        if send + more == money:
                                            all_solutions.append((send, more, money))
    return all_solutions

print(solutions())