#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3 as sqlite

uId_s = input("zadaj id: ")
uPrice_s = input("zadaj cenu: ")

uId = int(uId_s)
uPrice = int(uPrice_s)

con = sqlite.connect('ydb.db')

with con:

    cur = con.cursor()
    cur.execute("UPDATE cars SET price=? WHERE id=?", (uPrice, uId))

    print(f"Number of rows updated: {cur.rowcount}")