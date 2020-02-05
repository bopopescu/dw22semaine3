#!./env/bin/python3
# -*- coding: utf-8 -*-
""" docstring """

import pymysql
import web
"""
con = pymysql.connect('localhost', 'test', 'test', 'quentinvinot')

with con:
    cur = con.cursor()
    cur.execute("SELECT VERSION()")

    version = cur.fetchone()
    print("Database version: {}".format(version[0]))
"""
urls = (
    '/', 'index'
)

db = web.database(
    dbn='mysql',
    host='localhost',
    port=3306,
    user='test',
    pw='test',
    db='quentinvinot',
)

class index:
    def GET(self):
        return "hello world"

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()

