import json
dictionary={
    "employee" :{"name" : "immaculate","age":21,"city":"chennai"},
    "employees":{"sam","anitha","binu"},
    "rank":(1,2,3),
    "father":"belcus",
    "salary":40000,
    "height":5.5,
    "employed":True,
    "married":False,
    "children":None,
    }
json_object=json.dumps(dictionary,indent = 9)

with open("sample.json","w") as outfile:
    outfile.write(json_object)


#IMPORT SQI

import sqlite3
import json
import task
conn=sqlite3.connect('day12.db')
print("opened database successfully")
c=conn.cursor()
c.execute('''CREATE TABLE PROFILE1(DATA json);''')
print("Table created")
c.execute('''INSERT INFO PROFILE VALUES(?)''',(json.dumps(task.x),))
c.execute('''SELECT = FROM PROFILE1 ''')
print(c.fetchall())
conn.commit()
c.close()
