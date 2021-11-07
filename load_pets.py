import sqlite3
from sqlite3 import Error
database="./pets.db"
try:
    pets_db=sqlite3.connect(database)
except Error as e:
    print(e)


def person():
    db_cursor=pets_db.cursor()
    person_query='''INSERT INTO Person VALUES (?,?,?,?);'''
    values=[
        (int(1),'James','Smith',int(41)),
        (int(2),'Diana','Greene',int(23)),
        (int(3),'Sara','White',int(27)),
        (int(4),'William','Gibson',int(23)),
    ]
    db_cursor.executemany(person_query,values)
    pets_db.commit()
    print(db_cursor.rowcount, " rows were inserted.")

def pet():
    db_cursor=pets_db.cursor()
    pet_query="INSERT INTO Pet VALUES (?,?,?,?,?)"
    values=[
        (int(1),'Rusty','Dalmation',int(4),int(1)),
        (int(2),'Bella','AlaskanMalamute',int(3),int(0)),
        (int(3), 'Max','CockerSpaniel',int(1),int(0)),
        (int(4),'Rocky','Beagle',int(7),int(0)),
        (int(5),'Rufus','CockerSpaniel',int(1),int(0)),
        (int(6),'Spot','Bloodhound',int(2),int(1))
    ]
    db_cursor.executemany(pet_query,values)
    pets_db.commit()
    print(db_cursor.rowcount, " rows were inserted.")

def person_pet():
    db_cursor=pets_db.cursor()
    person_pet_query="INSERT INTO Person_Pet VALUES (?,?)"
    values=[
        (int(1),int(1)),
        (int(1),int(2)),
        (int(2),int(3)),
        (int(2),int(4)),
        (int(3),int(5)),
        (int(4),int(6))
    ]
    db_cursor.executemany(person_pet_query,values)
    pets_db.commit()
    print(db_cursor.rowcount, " rows were inserted.")

def main():
    person()
    pet()
    person_pet()

if __name__ == "__main__":
    main()