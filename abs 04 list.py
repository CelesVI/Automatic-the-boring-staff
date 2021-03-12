from sys import stdin

spam = list(map(str, stdin.readline().split()))

def merge(lista):
    lista.insert((len(spam)-1), 'and')
    return ','.join(lista)

print(merge(spam))
