import re

#Sub replace first param in second param.
namesRegex = re.compile(r'Agent (\w)\w*')
namesRegex.findall('Agent Alice gave the secret documents to Agent Bob.')
sub = namesRegex.sub(r'Agent \1*****', 'Agent Alice gave the secret documents to Agent Bob.')
print(sub)


#Verbose allows add comments and white to regex.
phoneRegex = re.compile(r'''
\d\d\d  #area code
-
\d\d\d  #first 3 digits
-
\d\d\d\d #last 4 digits
\sx\d{2,4}
''', re.VERBOSE)
