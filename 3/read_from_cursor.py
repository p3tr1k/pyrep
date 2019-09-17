#!/usr/bin/python3

import sqlite3 as lite
from prettytable import from_db_cursor

con = lite.connect('test.db')
    
with con:
    
    cur = con.cursor()    
    cur.execute('SELECT * FROM Cities')   
    
    x = from_db_cursor(cur) 

print(x.get_string(title="Australian Cities", fields=["Name", "Rainfall"]))
# print(x)
print(prettytable.__version__)