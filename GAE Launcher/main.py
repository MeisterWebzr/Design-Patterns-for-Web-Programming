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
        #setting title of application
        self.title = "News 4 U!"
        #setting stylesheet directory
        self.css = "css/main.css"
        #head section of html setup
        self.head = '''
<!DOCTYPE HTML>
<html>
    <head><title></title></head>
    <body>'''
        #body section where all content will go
        self.body = 'Search top news'
        #closing function to wrap end tag of html to print page to browser
        self.close = '''
    </body>
</html>'''


    def print_out(self):#funtion to print out above page
        return  self.head + self.body + self.close# calling and printing all above functions to print html page





































#never touch info below
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
