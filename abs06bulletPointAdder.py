import pyperclip
text = pyperclip.paste()

pyperclip.copy(text)

lines = text.split(' ')
for i in range(len(lines)):
    lines[i] = '\n'+ lines[i]
    
text = ''.join(lines)
pyperclip.copy(text)
