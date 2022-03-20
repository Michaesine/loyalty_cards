from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import time

try:
    conn = MongoClient()
    db = conn.loyalty
    coll = db.loyalty
    # conn.admin.command('ismaster')
    print("Mongo connection initiated successfully.")
except ConnectionFailure:
    print("Could not connect to MongoDB")
    exit()

a = True


def register(na, nu, co):
    record = {
        "name": na,
        "number": nu,
        "code": co,
    }
    coll.insert_one(record)
    coll.find_one()


def find(name):
    query = {"name": name}
    res = coll.find_one(query)
    if res != None:
        time.sleep(0.5)
        print(res)
        time.sleep(2)
    else:
        time.sleep(0.5)
        print("Bestaat niet in de database.")
        time.sleep(2)


def update(option, old, new):
    if option == 1:
        where = {"name": old}
        what = {"$set": {"name": new}}
        coll.update_one(where, what)
    elif option == 2:
        where = {"number": old}
        what = {"$set": {"number": new}}
        coll.update_one(where, what)
    else:
        return "Please select one option."


while a:
    print("1. Register Account")
    print("2. Find Code")
    print("3. Delete Account")
    print("4. Change Account\n")
    option = int(input("Please select an option:\n) "))
    if option == 1:
        print("register")
        name = input("What is your name?\n) ")
        number = input("What is your phone number?\n) ")
        code = input("What is the code?\n) ")
        register(name, number, code)
    elif option == 2:
        print("find")
        name = input("What is your name?\n) ")
        find(name)
    elif option == 3:
        print("delete")
        name = input("What is your name?\n) ")
    elif option == 4:
        print("1. Change Name")
        print("2. Change Phone Number\n")
        option = int(input("Please select an option:\n) "))
        if option == 1:
            curr_name = input("What is your current name?\n) ")
            new_name = input("What is your new name?\n) ")
            update(option, curr_name, new_name)
        elif option == 2:
            curr_num = input("What is your current number?\n) ")
            new_num = input("What is your new number?\n) ")
            update(option, curr_num, new_num)
    else:
        print("Please select ONE of the FOUR options.")
