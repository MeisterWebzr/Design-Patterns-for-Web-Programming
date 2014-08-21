'''
Student: Otto Burroughs
Date: 8-21-2014
Assignment: GEA Launcher
'''
import webapp2
import urllib2#here we import all the classes and code needed to request info, receive that info and open info
from xml.etree.ElementTree import QName #from xml.etree dir we setup communication
import xml.etree.ElementTree as ET #import library classes and syntax and setting naming of ET in application

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')



#this will serve as our abstract class with no instances
class Page(object):
    def __init__(self):#constructor function to call functions below
        self.title = "News 4 U!"
        self.css = "css/main.css"
        self.head = '''
<!DOCTYPE HTML>
<html>
    <head><title></title></head>
    <body>'''
        self.body = 'Search top news'
        self.close = '''
    </body>
</html>'''


    

































#never touch info below
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
