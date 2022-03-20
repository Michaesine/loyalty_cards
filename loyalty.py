from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import time

try:
    conn = MongoClient()
    db = conn.loyalty
    coll = db.loyalty
    conn.admin.command('ismaster')
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


while a:
    print("1. Register Account")
    print("2. Find Code")
    print("3. Delete Account")
    print("3. Change Account\n")
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
        print("1. Change Name\n")
        print("2. Change Phone Number\n")
        option = int(input("Please select an option:\n) "))
        if option == 1:
            print(1)
        elif option == 2:
            print(2)
    else:
        print("Please select ONE of the FOUR options.")
