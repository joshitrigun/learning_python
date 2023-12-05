##################### Normal Starting Project ######################

import datetime as dt
import random
import pandas as pd
import smtplib

MY_EMAIL = "joshitrigun5@gmail.com"
MY_PASSWORD = "tpqyqequnoushney"

today_tuple = (dt.datetime.now().month, dt.datetime.now().day)


#  2: Use pandas to read the birthdays.csv

data = pd.read_csv('birthdays.csv')

#  3: Use dictionary comprehension to create a dictionary from birthday.csv

# sample dict = {new_key: new_value for (index, data_row} in data.iterrows()}

birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}


#HINT 4: Then you could compare and see if today's month/day tuple matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:
if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Monday Birthday\n\n{contents}"
        )




