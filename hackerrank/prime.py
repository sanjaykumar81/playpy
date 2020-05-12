def printPrime(numbers):
    for x in numbers:
        prime = False
        if x in [1, 2, 3, 5, 7, 11, 13, 17, 19, 23]:
            print("Prime")
            continue
        for i in range(2, int(x / 2)):
            if x % i == 0:
                print("Not prime")
                prime = False
                break
            else:
                prime = True
        if prime:
            print("Prime")


if __name__ == "__main__":
    i = int(input())
    numbers = []
    for x in range(i):
        numbers.append(int(input()))
    printPrime(numbers)
