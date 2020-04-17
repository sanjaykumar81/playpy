import math


def solution(A):
    total = sum(A)
    current_min = 0
    previous_min = 0
    left_sum = 0
    right_sum = 0
    for i in range(len(A) - 1):
        left_sum += A[i]
        right_sum = total - left_sum
        current_min = abs(right_sum - left_sum)
        # print(f"left_sum: {left_sum}, right_sum: {right_sum}: current_min {current_min}, previous_min: {
        # previous_min}")
        if i == 0:
            previous_min = current_min
        if current_min < previous_min:
            previous_min = current_min

    return previous_min


if __name__ == "__main__":
    result = solution([0, 0])
    print(result)
    assert 0 == result

    result = solution([1, 1])
    print(result)
    assert 0 == result

    result = solution([-1, -1])
    print(result)
    assert 0 == result

    result = solution([-1000, 0, 1000])
    print(result)
    assert 2000 == result

    result = solution([3, 6])
    print(result)
    assert 3 == result

    result = solution([-1000, 1000])
    print(result)
    assert 2000 == result

    result = solution([600000, 300000])
    print(result)
    assert 300000 == result

    result = solution([1, 1, 1, 1, 1, 1])
    print(result)
    assert 0 == result

    result = solution([1, 1, 1, 1, 1, 1, 1])
    print(result)
    assert 1 == result

    result = solution([3, 1, 1, 1, 1, 1, 1, 6])
    print(result)
    assert 1 == result

    A = [100, 0, 1, 2, 3, 4, 5, 6, 7, 7, 1000, -1000, 2, 3, 4, 5, 6, 666, 7, 9, 0, 0, 0, 0, 0, 0, 5, 5, 5, 5, 5, 5, 5,
         5, 5, 5, 5, 5, 5, 5, 5, 5, 53, 1, 1, 1, 1, 1, 1, 6]
    result = solution(A)
    print(result)
    assert 660 == result
