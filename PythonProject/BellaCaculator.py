import random
import collections
from collections import defaultdict




def get_random( pMin, pMax):
    if pMin < 0:
        pMin = 0
    if pMax > 100:
        pMax = 100
    return random.randint(pMin, pMax)


def generate(pCount, pMin, pMax, pSum=100):
#   generate a defaultdict with tuple of 4 element
#   tuple (num1, op, num2, '=', num3)
#   13 + 33 = ()    13 + () = 33    33 - 13 = ()    () - 13 = 33
    if pCount <= 0:
        return
    modNum = 3
    xStr = "(   )"
    dd = defaultdict()
    i = 0
    while len(dd) < pCount:
        small = get_random(pMin, pMax)
        big = get_random(pMin, pMax)
        if small > big:
            t = small
            small = big
            big = t

        if (small + big) < pSum:
            # make op '+'
            if i%modNum == 0:
                # put x on left
                prob = (xStr, '+', small, '=', big )
            else:
                prob = (small, '+', big, '=', xStr)
        else:
            # make op '-'
            if i%modNum == 0:
                prob = (big, '-', small, '=', xStr)
            else:
                if small + big < 100:
                    prob = (xStr, '-', small, '=', big)

        # print 'debug t=', t
        if prob not in dd:
            dd[prob] = prob
        i = i + 1
    # print dd.items()
    return dd

def pretty_print(pList, pCol=4):
    i = 1
    paragraphConst = 1
    paragraph = 0
    defCol = 4
    if pCol > 0:
        defCol = pCol

    for item in pList:
        if i < defCol:
            print_one(item, False)
            # print item, "\t",
            i = i + 1
        else:
            print_one(item, True)
            # print (item)
            i = 1
            paragraph = paragraph + 1
        if paragraph == paragraphConst:
            # print ""
            paragraph = 0

def print_one(pTuple, pReturn=False):
#     pTuple in format of (num1, op, num2, '=', num3)
#     e.g. ("13", '+', "33", '=', "(    )")
        if pReturn:
            print "%s%s%s%s%s" %(pTuple[0],pTuple[1],pTuple[2],pTuple[3],pTuple[4])
        else:
            print "%s%s%s%s%s" %(pTuple[0],pTuple[1],pTuple[2],pTuple[3],pTuple[4]), " ",

dd = generate(50, 5, 99, 200)
pretty_print(dd )
# print dd


