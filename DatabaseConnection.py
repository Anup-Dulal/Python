from pymongo import MongoClient

cl = MongoClient()

db = cl.example


detail= [
    {
        "name":"anup",
        "Learning":"python",
    },
    {
        "name":"ram",
        "Learning":"python",
     }
]
collect = db.collect

collect.insert_many(detail)


x = collect.find_one({'name':'ram'})
print(x)