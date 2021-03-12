import smtplib
conn = smtplib.SMTP_SSL('smtp.gmail.com', 465)

conn.login('''Agregar mail y contraseña. Es poco seguro''')
conn.sendmail('fedeinfo31@gmail.com','fedeinfo31@gmail.com', 'Subject: So long...\n\nDear Federico.\n\You are testing email sending.')
conn.quit()
