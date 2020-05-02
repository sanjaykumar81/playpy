def diagonalDifference(arr):
    # Write your code here
    sum_1 = 0
    sum_2 = 0
    for i in range(len(arr)):
        sum_1 = sum_1 + arr[i][i]
    for i in range(1, len(arr) + 1):
        print(i)
        sum_2 = sum_2 + arr[-i][i - 1]

    return abs(sum_1 - sum_2)


def solution(N):
    b = "{0:b}".format(N)
    previous = '0'
    gap = False
    gapCount = 0
    result = []
    for current in b:
        print(current)
        if current == '0' and previous == '0' and gap == False:
            previous = current
            print(f"previous: {previous}, gapCount= {gapCount}, gap: {gap}")
            continue;
        if current == '0' and previous == '0' and gap == True:
            previous = current
            gapCount += 1
            print(f"previous: {previous}, gapCount= {gapCount}, gap: {gap}")
            continue
        if current == '0' and previous == '1' and gap == False:
            previous = current
            gap = True
            gapCount += 1
            print(f"previous: {previous}, gapCount= {gapCount}, gap: {gap}")
            continue
        if current == '0' and previous == '1' and gap == True:
            previous = current
            gapCount += 1
            print(f"previous: {previous}, gapCount= {gapCount}, gap: {gap}")
            continue
        if current == '1' and previous == '0' and gap == False:
            previous = current
            print(f"previous: {previous}, gapCount= {gapCount}, gap: {gap}")
            continue
        if current == '1' and previous == '0' and gap == True:
            previous = current
            result.append(gapCount)
            gapCount = 0
            gap = False
            print(f"previous: {previous}, gapCount= {gapCount}, gap: {gap}")
            continue
        if current == '1' and previous == '1' and gap == False:
            print(f"previous: {previous}, gapCount= {gapCount}, gap: {gap}")
            continue
        if current == '1' and previous == '1' and gap == True:
            print(f"previous: {previous}, gapCount= {gapCount}, gap: {gap}")
            continue

    print(f"result : {result}")
    arr = sorted(result)
    print(arr)
    return arr.pop(,None)


def merge(arr1, arr2):
    i = 0
    j = 0

    temp_arr = []
    x = 0
    for x in range(len(arr1) + len(arr2)):

        if arr1[i] < arr2[j]:
            temp_arr.append(arr1[i])
            i += 1
            if i == len(arr1):
                temp_arr.extend(arr2[j:])
                break
        else:
            temp_arr.append(arr2[j])
            j += 1
            if j == len(arr2):
                temp_arr.extend(arr1[i:])
                break

    return temp_arr


if __name__ == '__main__':
    # result = merge([5,6,7,8],[1,2,3,4,5])

    # print(result)

    result = solution(15)
    print(result)
