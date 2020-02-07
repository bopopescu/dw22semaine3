#!./env/bin/python3
# -*- coding: utf-8 -*-
""" docstring """
from app import App

if __name__ == "__main__":
    App.app.run()





"""
con = pymysql.connect('localhost', 'test', 'test', 'quentinvinot')

with con:
    cur = con.cursor()
    cur.execute("SELECT VERSION()")

    version = cur.fetchone()
    print("Database version: {}".format(version[0]))
""" 