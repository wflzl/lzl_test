#!/usr/bin/env python
# coding=utf-8
import web
import glog
import os
from database import SqliteDb

defaultdb = SqliteDb(os.path.join(os.getcwd(), 'database/name.db'), 'names')
urls = ( '/index|/', 'index','/hello', 'hello', '/test*', 'test', '/template', 'greet')
render = web.template.render('templates')

def read_html(htmlfile):
    return open(htmlfile, 'rb').read()

class index:
    def GET(self):
        return read_html('index.html')
    def POST(self):
        return hello().GET() 
        

class hello:
    def GET(self):
        return "<h1><font color='red'>Hello World!</font><h1>"

class greet:
    def GET(self):
        return render.greeting("lizhiliong")

class test():
    def GET(self):
        user_data = web.input()
        if (user_data.FirstName == ""):
            glog.warning("FirstName mustn't be Null")
        if (user_data.LastName == ""):
            glog.warning("LastName mustn't be Null")
        if not (user_data.FirstName == "" or user_data.LastName == ""):
            if defaultdb.auto_clean_insert(user_data.FirstName, user_data.LastName):
                glog.info("%s %s has been inserted into names" % (user_data.FirstName, user_data.LastName))
            else:
                glog.info("%s %s has been in names" % (user_data.FirstName, user_data.LastName))
        return "<h1>" + user_data.FirstName + "<br>" + user_data.LastName + "</h1>" +\
                "<h2><a href='index'>Back to Index</a></h2>"

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
