#!/usr/bin/python3
"""script that lists all states with a name starting
with N (upper N) from the database hbtn_0e_0_usa:"""

if __name__ == '__main__':
    """module to order the states by id ASC"""

    import MySQLdb
    import sys

    db = MySQLdb.connect(
        host='localhost',
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3]
    )

    mycursor = db.cursor()
      
    mycursor.execute("SELECT cities.id, cities.name, states.name \
FROM cities JOIN states ON cities.state_id = states.id \
ORDER BY cities.id ASC")
    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)
