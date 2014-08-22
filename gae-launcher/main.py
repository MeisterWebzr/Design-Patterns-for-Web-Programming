'''
Student: Otto Burroughs
Date: 8-21-2014
Assignment: GEA Launcher
'''
import webapp2
import urllib2#here we import all the classes and code needed to request info, receive that info and open info
from xml.etree.ElementTree import QName #from xml.etree dir we setup communication
#import xml.etree.ElementTree as ET #import library classes and syntax and setting naming of ET in application
import json

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = SearchArea()
        p.inputs = [['search','search','enter search term'],['Submit', 'submit',]]
        self.response.write(p.print_out())

        #if input is entered and searched
        #search = self.request.GET['search']
            #setting url for api
            #url = "http://news.yahoo.com/rss/?p=" +search
            #assembling request
            #request = urllib2.Request(url)
            #creating object with urllib2
            #opener = urllib2.build_opener()
            #getting result from url- request from api
            #result = opener.open(request)

            #parsing with eTree






#this will serve as our abstract class with no instances
class Page(object):
    def __init__(self):#constructor function to call functions below
        #setting title of application
        self.title="News 4 U!"
        self.css="css/self.css" #setting stylesheet directory
        self._head='''
<!DOCTYPE HTML>
<html>
    <head>
    <title>Get the news!</title>
    <link href="{self.css}" rel="stylesheet" type="text/css" />
    </head>
    <body>'''
        #body section where all content will go
        self._body = ''
        #closing function to wrap end tag of html to print page to browser
        self._close = '''
    </body>
</html>'''


    def print_out(self):#funtion to print out above page
        return  self._head + self._body + self._close# calling and printing all above functions to print html page

#constructing super class for search area inputs
class SearchArea(Page):
    def __init__(self):#constructot function for SearchArea class
        #constructing super class
        super(SearchArea, self).__init__()#calling super class into function
        self._form_open = '<form method="GET">' #form open with method GET
        self._form_close = '</form>' #form close
        self.__inputs = [] #setup inputs array index
        self._form_inputs= '' #setup form string inputs section

    @property #setting property of inputs that ill create above
    def inputs(self):
        pass#passing

    @inputs.setter# here ill set the parameters for inputs to go above
    def inputs(self, arr): #setting up array for inputs
        #chaninging private input variable
        self.__inputs = arr #setting private input = array of inputs
        #seting up cycle through array inputs
        for item in arr:
            self._form_inputs += '<input type="'+item[1]+'"name="' +item[0]
            #setting number of arrays depedning on what inputs i create at top of file
            try: #try this
                self._form_inputs += '"placeholder="'+item[2]+'"/>'
            except:# otherwise
                self._form_inputs += '"/>'
        #print self._form_inputs



    #POLYMORPHISM!!!!!!!! ----------------- METHOD OVERRIDING
    def print_out(self):
        #returning the Page printout here using polymorphism to override
        return  self._head + self._body + self._form_open + self._form_inputs + self._form_close + self._close




#never touch info below
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
