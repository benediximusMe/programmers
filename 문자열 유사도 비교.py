# 내장함수를 이용하는 방법
# from difflib import SequenceMatcher
#
# def similar(a, b):
#     return SequenceMatcher(None, a, b).ratio()
#
# print(similar('Apple','Apple'))


# Levenshtein Distance
# 편차 거리차이 방법
# 한글자 글자의 차이(삽입, 삭제, 대체)를 거리로 계산한다
# https://www.yceffort.kr/2018/05/31/Levenshtein-distance/


import math


def getDistance(s1,s2):
    longStrLen = len(s1)+1
    shortStrLen =  len(s2) + 1
    cost = []
    newcost = []

    for i in range(longStrLen):
        cost.append(i)
        newcost.append(i)

    for i in range(1,shortStrLen):
        newcost.append(i)
        newcost[0] = i

        for j in range(1,longStrLen):
            match = 0
            if s1[j-1] != s2[i-1]:
                match = 1
            replace = cost[j-1] + match
            insert = cost[j] + 1
            delete = newcost[j-1] + 1

            newcost[j]= min(insert,delete,replace)

        temp = cost
        cost = newcost
        newcost = temp

    return cost[longStrLen-1]




print(getDistance('Apple','aaple'))
# 차이가 발생하는 개수만큼 리턴하네
