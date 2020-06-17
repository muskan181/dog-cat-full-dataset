import smtplib
session = smtplib.SMTP("smtp.gmail.com", 587)
session.starttls()
session.login("muskan.181.ma@gmail.com","march0303")
msg = "Best model trained!"
session.sendmail("muskan.181.ma@gmail.com" , "muskan.181.ma@gmail.com" , msg)
session.quit()
