
def solution(A):
    length = len(A)
    if length ==0:
        return 1
    if length ==1:
        if A[0] == 1:
            return 2
        else:
            return 1

    sorted_A = sorted(A)
    for i in range(length):
        if sorted_A[i] == i+1:
            continue
        else:
            return i+1
    return i+2

if __name__ == "__main__":

    result = solution([1])
    print(result)
    assert 2 == result
    result = solution([1,3,2,5])
    print(result)
    assert 4 == result
    result = solution([1,3,2,4])
    print(result)
    assert 5 == result

