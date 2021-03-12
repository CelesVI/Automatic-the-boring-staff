import re, pyperclip

phoneRegex = re.compile(r'''
# 415-555-0000, 555-0000, (415) 555-0000, 555-0000, ext. 12345
(
((\d\d\d)|(\(\d\d\d))?     # area code (optional)
(\s|-)                      # first separator
\d\d\d                      # first 3 digits
-                           # separator
\d\d\d\d                    # last 4 numbers
(((ext(\.)?\s)|x)           # Extension word-part (optional)
(\d{2,5}))?                 # Extension number-part (optional)
)
''', re.VERBOSE)

emailRegex = re.compile(r'''

[a-zA-Z0-9_.+]+             # Name part
@                           # Symbol @
[a-zA-Z0-9_.+]+             # Domain part
''', re.VERBOSE)

text = pyperclip.paste()

extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

results = '\n'.join(allPhoneNumbers)+'\n'+'\n'.join(extractedEmail)

pyperclip.copy(results)

save = pyperclip.paste()
with open('numbersandemail.txt', 'w') as f:
    f.write(save)

print(allPhoneNumbers)
print(extractedEmail)
print(results)
