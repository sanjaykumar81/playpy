"""
Rotate the element of an array A by K position.

"""


def solution(A, K):
    # write your code in Python 3.6\
    if K > len(A):
        K = K%len(A)
    L = len(A)
    break_point = L-K
    a = A[:break_point]
    b=A[break_point:]
    b.extend(a)
    return b


if __name__ == '__main__':
    result = solution([1,3,4,5],2)
    assert [4,5,1,3] == result
    result = solution([3, 8, 9, 7, 6, 2],4)
    assert [9, 7, 6, 2, 3, 8] == result

    # scenario when K is greater then length of array
    result = solution([3, 8, 9, 7, 6, 2], 14)
    assert [6, 2, 3, 8, 9, 7] == result

