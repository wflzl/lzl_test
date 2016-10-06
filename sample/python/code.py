#!/usr/bin/env python
# coding=utf-8
import web

urls = ( '/', 'index','/hello', 'hello', '/test*', 'test', '/template', 'greet')
render = web.template.render('templates')
def read_html(htmlfile):
    return open(htmlfile, 'rb').read()

class index:
    def GET(self):
        return read_html('index.html')

class hello:
    def GET(self):
        return "<h1><font color='red'>Hello World!</font><h1>"

class greet:
    def GET(self):
        return render.greeting("lizhiliong")

class test():
    def GET(self):
        user_data = web.input(FirstName="no", LastName="no")
        return "<h1>" + user_data.FirstName + "<br>" + user_data.LastName + "</h1>"

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
