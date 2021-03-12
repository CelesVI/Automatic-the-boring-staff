from sys import stdin
from collections import Counter

def addToInventory(inventory, addItems):
    return dict(Counter(inventory) + Counter(addItems))

def displayInventory(bag):
    print('Inventory:')
    total = 0
    for k,v in bag.items():
        total += v
        print(str(v)+' '+str(k))
    print('Total items: '+str(total))
    
myList = list(map(str,stdin.readline().split()))

d = {x:myList.count(x) for x in myList}

bag = {'gold': 3, 'dagger': 1, 'spell': 2}

newBag = addToInventory(bag, d)

displayInventory(newBag)





