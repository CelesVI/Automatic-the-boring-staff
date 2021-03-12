import re

batRegex = re.compile(r'Bat(wo)*man')
find = batRegex.search('The adventures of Batwoman')
print(find.group())
find = batRegex.search('The adventures of Batwowowowoman')
print(find.group())

regex = re.compile(r'(\+\*\?)+')
find = regex.search('I learned about +*? regex syntax')
print(find.group())
find = regex.search('I learned about +*?+*?+*?+*? regex syntax')
print(find.group())

'''phoneRegex = re.compile(r'((\d\d\d-)?\d\d\d-\d\d\d\d(,)?)(3)')
find = phoneRegex.search('My phone numbers are 452-666-1237,489-656-7847,547-3650')
print(find.group())'''

haRegex = re.compile(r'(Ha){3,5}')
find = haRegex.search('He "said HaHaHa"')
print(find.group())

digitRegex = re.compile(r'(\d){3,5}')
find = digitRegex.search('1234567890')
print(find.group())

digitRegex = re.compile(r'(\d){3,5}?')
find = digitRegex.search('1234567890')
print(find.group())
