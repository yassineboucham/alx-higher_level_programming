#!/usr/bin/python3

"""sql inj"""

import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]

db = MySQLdb.connect(host="localhost",
                   user=username,
                   password=passwd,
                   database=db_name,
                   port=3306
                   )
c = db.cursor()