import requests

#Get a web page.
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
print(res.status_code)
print(len(res.text))
print(res.text[500:])

#Save web page dat into a file.
file = open('RomeoAndJuliet.txt', 'wb')
for chuck in res.iter_content(1000000):
    file.write(chuck)
