import smtplib
import datetime as dt
import random

my_email = "rajasabarish874@gmail.com"
my_pass = "Sabarish@1965"

now = dt.datetime.now()
day_of_week = now.weekday()
with open("quotes.txt") as quote_file:
    all_quotes = quote_file.readlines()
    quote = random.choice(all_quotes)
if day_of_week == 1:
    with smtplib.SMTP("smtp.gmail.com") as connection :
        connection.starttls()
        connection.login(my_email, my_pass)
        connection.sendmail(
            from_addr=my_email,
            to_addrs= my_email, 
            msg=f"Subject:MONDAY MOTIVATION \n\n{quote}")
