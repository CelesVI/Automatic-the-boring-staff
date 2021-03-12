import imapclient
conn = imapclient.IMAPClient('imap.gmail.com', ssl=True)
conn.login('Agregar mail y contraseña')
conn.select_folder('INBOX', readonly=True)
UIDs = conn.search(['SINCE 20-Aug-2018'])
print(UIDs)