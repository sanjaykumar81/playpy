def solution(A):
    # write your code in Python 3.6
    even_map = {}
    for x in A:
        if even_map.get(x) == None:
            even_map[x] = "ODD"
        else:
            if even_map.get(x) == "ODD":
                even_map[x] = "EVEN"
            elif even_map.get(x) == "EVEN":
                even_map[x] = "ODD"

    for key, value in even_map.items():
        if value == "ODD":
            return key




if __name__ == "__main__":

    result = solution([9, 3, 9, 3, 9, 7, 9])
    print(result)
    assert 2 == result