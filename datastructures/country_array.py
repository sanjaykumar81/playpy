import random

def solution(A):
    # write your code in Python 3.6
    return get_country_count(A)


def get_country_count(A):
    country_array = [0 for i in range(len(A))]
    for i in range(len(country_array)):
        country_array[i] = [0 for j in range(len(A[0]))]

    count = fill_country_area(country_array, A, 0)
    for ele in country_array:
        print(ele)
    return count


def fill_country_area(country_area_map, A, countries_count):
    N = len(A)
    M = len(A[0])

    for i in range(N):
        for j in range(M):
            if i == 0 and j == 0:
                country_area_map[i][j] = "C" + str(countries_count)
                countries_count += 1
            elif i == 0:
                countries_count = first_row_country_mapper(A, country_area_map, countries_count, i, j)
            elif j == 0:
                countries_count = first_column_country_mapper(A, country_area_map, countries_count, i, j)
            else:
                countries_count = cell_county_mapper(A, country_area_map, countries_count, i, j)

    return countries_count


def check_previous_connected_cells_and_update(A, i, j, country_area_map, country_code, countries_count):
    if j != 0 and A[i][j] == A[i][j - 1]:
        country_area_map[i][j - 1] = country_code
        countries_count -= 1
        check_previous_connected_cells_and_update(A, i, j - 1, country_area_map, country_code, countries_count)
    elif i != 0 and A[i][j] == A[i - 1][j]:
        country_area_map[i - 1][j] = country_code
        countries_count -= 1
        check_previous_connected_cells_and_update(A, i - 1, j, country_area_map, country_code, countries_count)


def cell_county_mapper(A, country_area_map, countries_count, i, j):
    if A[i][j] == A[i][j - 1] and A[i][j] == A[i - 1][j]:
        country_code = country_area_map[i - 1][j]
        mark_country(country_area_map, i, j, country_code)
        mark_country(country_area_map, i, j - 1, country_code)
        countries_count -= 1
        check_previous_connected_cells_and_update(A, i, j - 1, country_area_map, country_code, countries_count)
    elif A[i][j] == A[i][j - 1]:
        mark_country(country_area_map, i, j, country_area_map[i][j - 1])
    elif A[i][j] == A[i - 1][j]:
        mark_country(country_area_map, i, j, country_area_map[i - 1][j])
    else:
        country = "C" + str(countries_count)
        mark_country(country_area_map, i, j, country)
        countries_count += 1
    return countries_count


def first_row_country_mapper(A, country_area_map, countries_count, i, j):
    if A[i][j] == A[i][j - 1]:
        mark_country(country_area_map, i, j, country_area_map[i][j - 1])
    else:
        country = "C" + str(countries_count)
        mark_country(country_area_map, i, j, country)
        countries_count += 1
    return countries_count


def first_column_country_mapper(A, country_area_map, countries_count, i, j):
    if A[i][j] == A[i - 1][j]:
        mark_country(country_area_map, i, j, country_area_map[i - 1][j])
    else:
        country = "C" + str(countries_count)
        mark_country(country_area_map, i, j, country)
        countries_count += 1
    return countries_count


def mark_country(country_area_map, i, j, country):
    country_area_map[i][j] = country


if __name__ == "__main__":
    A = [0 for x in range(20)]
    for row in range(len(A)):
        A[row] = [abs(random.randrange(1, 5)) for x in range(5)]

    A = [
        [3, 4, 3],
        [3, 2, 4],
        [3, 1, 4],
        [1, 4, 4],
        [1, 2, 3],
        [1, 3, 3],

    ]
    # output of the country mapping
    # countries = [
    #     ['C0', 'C1', 'C2'],
    #     ['C0', 'C3', 'C4'],
    #     ['C0', 'C5', 'C4'],
    #     ['C6', 'C4', 'C4'],
    #     ['C6', 'C7', 'C8'],
    #     ['C6', 'C8', 'C8'],
    # ]
    for row in A:
        print(row)
    result = solution(A)

    assert 9 == result
