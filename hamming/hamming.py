def distance(strand_a, strand_b):

    if len(strand_a) != len(strand_b):
        raise ValueError("values passed is not of same length")
    list_a = list(strand_a)
    list_b = list(strand_b)
    if list_a == list_b:
        return 0
    else:
        count = 0
        position = []
        for i in range(len(list_a)):
            if list_a[i] != list_b[i]:
                count += 1
                position.append(i)

        print(position)
        return count
