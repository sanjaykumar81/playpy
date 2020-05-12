if __name__ == '__main__':
    # arr = [
    #     [1, 1, 1, 0, 0, 0],
    #     [0, 1, 0, 0, 0, 0],
    #     [1, 1, 1, 0, 0, 0],
    #     [0, 0, 2, 4, 4, 0],
    #     [0, 0, 0, 2, 0, 0],
    #     [0, 0, 1, 2, 4, 0],
    # ]

    arr = [
        [-1, -1, 0, -9, -2, -2],
        [-2, -1, -6, -8, -2, -5],
        [-1, -1, -1, -2, -3, -4],
        [-1, -9, -2, -4, -4, -5],
        [-7, -3, -3, -2, -9, -9],
        [-1, -3, -1, -2, -4, -5]
    ]

    # for _ in range(6):
    #     arr.append(list(map(int, input().rstrip().split())))

    hour_glass_sum = 0
    for i in range(4):

        for j in range(4):
            x = arr[i][j] + arr[i][j + 1] + arr[i][j + 2]
            y = arr[i + 1][j + 1]
            z = arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2]
            total = x + y + z
            if i ==0 and j ==0:
                hour_glass_sum = total
            elif total > hour_glass_sum:
                hour_glass_sum = total

    print(hour_glass_sum)
    assert -6 == hour_glass_sum
