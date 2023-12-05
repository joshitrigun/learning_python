import random
import smtplib
import datetime as dt
import random
now = dt.datetime.now()
weekday = now.weekday()
my_email = "joshitrigun5@gmail.com"
password = "tpqyqequnoushney"

if weekday == 3:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    # print(quote)
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()

        connection.login(user=my_email, password=password)

        connection.sendmail(
            from_addr=my_email,
            to_addrs="iamtrigun@gmail.com",
            msg=f"Subject:Monday motivation\n\n{quote}"
        )

# import smtplib
#
# my_email = "joshitrigun5@gmail.com"
# password = "tpqyqequnoushney"
#
# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     connection.starttls()
#
#     connection.login(user=my_email, password=password)
#
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="iamtrigun@gmail.com",
#         msg="Subject:Happy Birthday\n\nThis is the body of my email"
#     )
#
# import datetime as dt
#
# now = dt.datetime.now()
# date_of_birth = dt.datetime(year=1989, month=7, day=7)
# print(date_of_birth)