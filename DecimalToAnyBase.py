def decimalToAnyBase(number, base):
    convertedNum = ''

    while number > 0:
        convertedNum += str(number % base)
        number //= base

    return convertedNum[::-1]


if __name__ == "__main__":
    A = int(input())
    B = int(input())

    print(decimalToAnyBase(A, B))
