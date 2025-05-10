import csv
import pandas as pd

def csv_to_list_of_dict(filename):
    users = []
    with open(filename, 'r', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            users.append(row)

    return users


def get_user():
    user_name = 'Kalin'
    users = csv_to_list_of_dict('user1_account.csv')
    print(users)

def myFilter(el):
   return True if el['name'] == user_name else False

res = list(filter(myFilter.users))[0]
print(res)



columns = ['name','pincode', 'balance']
get_user()
my_filter()