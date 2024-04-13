#!/usr/bin/python3

if __name__ == "__main__":
    username = sys.argv[1]
    passworld = sys.argv[2]
    dbname = sys.argv[3]

    db = MySQLdb.connect(host="localhost",
                         user=username,
                         passworld=passworld,
                         database=dbname,
                         port=3306)
    c = db.cursor()
    c.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id")

    for row in c.fetchall():
        print(row)
