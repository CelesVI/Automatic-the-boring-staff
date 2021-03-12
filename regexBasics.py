import re

message = 'Call me 415-555-1011 tomorrow, or at 415-555-9990'

#Crear regex object con compile.
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
#Crear objecto match con search.
found = phoneNumRegex.search(message)
#Crear string del objecto match.
print(found.group())
