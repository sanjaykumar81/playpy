
class Difference():
    def __init__(self, arr):
        self.arr = arr
        self.maximumDifference = 0

    def computeDifference(self):
        sorted_arr = sorted(self.arr)

        self.maximumDifference = abs(sorted_arr[0] - sorted_arr[len(sorted_arr) - 1])


if __name__ == "__main__":
    a = [1, 2, 5]

    d = Difference(a)
    d.computeDifference()
    print(d.maximumDifference)
