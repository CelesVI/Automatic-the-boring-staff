import webbrowser, sys, pyperclip

sys.argv
if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()
webbrowser.open(r'https://www.google.com/maps/place/'+ address)
