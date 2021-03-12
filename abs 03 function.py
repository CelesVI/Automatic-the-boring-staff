number = int(input())

def collatz(number):
    print(number)
    if(number == 1):
        return 1
    else:
        if (number % 2 == 0):
            return int(collatz(number // 2))
        else:
            return int(collatz(3 * number + 1))

print(collatz(number))
