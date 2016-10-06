#!/usr/bin/env python
# coding=utf-8
import sqlite3

class MyException(Exception):
    def __init__(self, message=None):
        if message is None:
            message = "Exception message is Null"
        print message

class SqliteDb(object):
    def __init__(self, db_name, table_name = None):
        self.db = sqlite3.connect(db_name)
        self.cursor = self.db.cursor()
        self.table_name = table_name
    
    def reset(self, table_name):
        self.table_name = table_name

    def max(self, col_name, table_name=None):
        if table_name is None:
            if self.table_name is not None:
                table_name = self.table_name
            else:
                raise MyException("Invaild table_name, table name is None")
        script = "select max(%s) from %s" % (col_name, table_name)
        self.cursor.execute(script)
        res = self.cursor.fetchall()
        return res[0][0]

    def find_by_id(self, id, table_name=None, keep_id=True):
        if table_name is None:
            if self.table_name is not None:
                table_name = self.table_name
            else:
                raise MyException("table name is None")
        script = "select * from %s where id = %s" % (table_name, id)
        self.cursor.execute(script)
        res = self.cursor.fetchall()
        if res == []:
            raise MyException("id %s not exists!" % id) 
        if keep_id:
            return res[0]
        else:
            return res[0][1:]

    def auto_insert(self, fname, lname, table_name=None):
        id = self.max('id', table_name) + 1
        return self.insert(id, fname, lname, table_name)
        
    def insert(self, id, fname, lname, table_name=None):
        if table_name is None:
            if self.table_name is not None:
                table_name = self.table_name
            else:
                raise MyException("table name is None")
        if not (type(fname) == str and type(lname) == str):
            raise MyException("type not match, need str, str!")
        script = "insert into %s values ( %s, '%s', '%s')" % (table_name, id, fname, lname)
        try:
            self.cursor.execute(script)
            self.db.commit()
        except Exception as err:
            print err, script
            return False
        return True

if __name__ == '__main__':
    # if you want to execute, run 'python sqlite_sample.py' or './sqlite_sample.py'
    sqldb = SqliteDb('name.db')
    max_id = sqldb.max('id', 'names')
    print 'max id of names is:', max_id
    sqldb.reset('names')
    fname, lname = sqldb.find_by_id(0, keep_id=False)
    print "My name is:", "%s %s" % (fname, lname)
    if sqldb.auto_insert("Zhou", "Zhiqiu"):
        print sqldb.find_by_id(sqldb.max('id'))
