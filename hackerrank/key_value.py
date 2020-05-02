import sys

if __name__ == "__main__":

    number_of_input = int(input())
    phone_book = {}
    for i in range(number_of_input):
        name_phone = input()

        values = name_phone.split()
        if len(values) <= 1:
            i -= 1
            continue
        name = values[0]
        phone = values[1]

        phone_book[name] = phone

    lines = sys.stdin.readlines()
    for i in lines:

        i = i.strip()

        if i in phone_book:
            # sam = 99912222
            print(f"{i}={phone_book.get(i)}")
        else:
            print("Not found")
