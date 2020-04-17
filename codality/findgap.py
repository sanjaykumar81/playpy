"""
The problem is given a number N, find the max gap (consecutive zero's between 1) of its binary representation

"""

def solution(N):
    b = "{0:b}".format(N)
    previous = '0'
    gap = False
    gapCount = 0
    result = []
    for current in b:
        if current == '0' and previous == '0' and gap == False:
            previous = current
            continue;
        if current == '0' and previous == '0' and gap == True:
            previous = current
            gapCount += 1
            continue
        if current == '0' and previous == '1' and gap == False:
            previous = current
            gap = True
            gapCount += 1
            continue
        if current == '0' and previous == '1' and gap == True:
            previous = current
            gapCount += 1
            continue
        if current == '1' and previous == '0' and gap == False:
            previous = current
            continue
        if current == '1' and previous == '0' and gap == True:
            previous = current
            result.append(gapCount)
            gapCount = 0
            gap = False
            continue
        if current == '1' and previous == '1' and gap == False:
            continue
        if current == '1' and previous == '1' and gap == True:
            continue

    if len(result) == 0:
        return 0
    else:
        arr = sorted(result)
        return arr[-1]


if __name__ == '__main__':
    result = solution(1041)
    assert result == 5
    result = solution(15)
    assert result == 0
    result = solution(32)
    assert result == 0
    result = solution(12345321)
    assert result == 3
