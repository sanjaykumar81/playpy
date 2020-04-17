def solution(start,end, jump):
    diff = end - start
    if diff == 0:
        return 0;
    elif diff%jump == 0:
        return diff//jump
    else:
        return  (diff//jump) + 1


if __name__ == "__main__":
    result = solution(1, 10, 3)
    print(result)
    assert 3 == result
