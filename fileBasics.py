import shelve

#To open a file in read mode only.
file = open(r'C:\Users\Bravin\Desktop\prueba.txt')
print(file.read())
file = open(r'C:\Users\Bravin\Desktop\prueba.txt')
print(file.readlines())
file.close()
#To write a file. Override previous content.
file = open(r'C:\Users\Bravin\Desktop\prueba.txt', 'w')
file.write('Hello!!!!')
file = open(r'C:\Users\Bravin\Desktop\prueba.txt')
print(file.readlines())
#To write a file. Doesn't Override previous content.
file = open(r'C:\Users\Bravin\Desktop\prueba.txt', 'a')
file.write('Have a nice day')
file.close()

#To save a complex structure like list, dictionary.
shelfFile = shelve.open('mydata')
shelfFile['cats'] = ['Sophie', 'Pooka', 'Simon', 'Fat-tail', 'Cleo']
shelfFile.close()

shelfFile = shelve.open('mydata')
shelfFile['cats']
shelfFile.close()

shelfFile = shelve.open('mydata')
print(list(shelfFile.keys()))
print(list(shelfFile.values()))
