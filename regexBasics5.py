import re

#^ for start with.
begins = re.compile(r'^Hello')
find = begins.search('Hello')
print(find.group())

#$ for end with.
ends = re.compile(r'World$')
find = ends.search('World')
print(find.group())

#Start and finish with
begins = re.compile(r'^\d+$')
find = begins.search('1651616846231686')
print(find.group())

#. for contain in some word a sentence.
begins = re.compile(r'.{1,2}at')
find = begins.findall('The cat in the hat sat on the flat mat')
print(find)

# * for whatever after some point.
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
find = nameRegex.findall('First Name: Federico Last Name: Bravin')
print(find)

#. match anything except newlines. dotall match newlines.
prime = 'Serve the public trust. \Protect the innocents.'
dotStar = re.compile(r'.*', re.DOTALL)
find = dotStar.search(prime)
print(find.group())

#Re.I to match uppercase.
vowelRegex = re.compile(r'[aeiou]', re.I)
find = vowelRegex.findall('Arriba Las MINIfaldas.')
print(find)





