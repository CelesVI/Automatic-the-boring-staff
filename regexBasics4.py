import re

message = '3 bananas, 2 oranges, 1 lemon'

#Print all the coincidences of 1 or more digit, space and 1 or more letters.
digitRegex = re.compile(r'\d+\s\w+')
find = digitRegex.findall(message)
print(find)

#Return all matches a the groups on the compile.
vowelRegex = re.compile(r'[aeiouAEIOU]')
find = vowelRegex.findall('Robocop eats baby food')
print(find)

#Return all no the matches at the compile.
noVowelRegex = re.compile(r'[^aeiouAEIOU]')
find = noVowelRegex.findall('Robocop eats baby food')
print(find)
