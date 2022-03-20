from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

try:
    conn = MongoClient()
    db = conn.loyalty
    coll = db.loyalty
    conn.admin.command('ismaster')
    print("Mongo connection initiated successfully.\n\n")
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
        print(res)
        return res
    else:
        print("Bestaat niet in de database.")
        return "Bestaat niet in de database."



def delete(code):
    query = {"code": code}
    coll.delete_one(query)


def update(option, old, new):
    if option == str(1):
        where = {"name": old}
        what = {"$set": {"name": new}}
        coll.update_one(where, what)
    elif option == str(2):
        where = {"number": old}
        what = {"$set": {"number": new}}
        coll.update_one(where, what)
