#!/usr/bin/python3

import sys
import MySQLdb

if __name__ == "__main__":
    username=sys.argv[1]
    passwd=sys.argv[2]
    dbname=sys.argv[3]
    searched=sys.argv[4]

    db=MySQLdb.connect(host="localhost",
                       user=username,
                       passworld=passwd,
                       database=dbname,
                       port=3306)

    c = db.cursor()
    c.execute("SELECT * FROM states WHERE name LIKE '{}' ORDER BY states.id".format(searched))

    for row in c.fetchall():
        print(row)
