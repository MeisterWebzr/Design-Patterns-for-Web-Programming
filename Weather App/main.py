#Otto Burroughs
#notes on inheritance
#
import webapp2
import urllib2 #python classes and code needed to request info, receiving it and opening it
from xml.dom import minidom

class MainHandler(webapp2.RequestHandler):
    def get(self):
       p = FormPage()
       p.inputs = [ ['zip', 'text', 'zip code'], ['Submit', 'submit']]
       self.response.write(p.print_out())


       if self.request.GET:

           zip = self.request.GET['zip']
           url = "http://xml.weather.yahoo.com/forecastrss?p=" + zip
           #get info from API
           url = "http://xml.weather.yahoo.com/forecastrss?p=90210"
           #====1st====> assemble the request <=======
           request = urllib2.Request(url)
           #====2nd====> use the urllib2 to create and object to get the url <=======
           opener = urllib2.build_opener()
           #====3rd====> use the url to get a result - request info from the API <=======
           result = opener.open(request)

           #parse the XML
           xmldoc = minidom.parse(result)
           self.response.write(xmldoc.getElementsByTagName('title')[2].firstChild.nodeValue)

           list = xmldoc.getElementsByTagName("yweather:forecast")
           for item in list:
               print item.attributes['day'].value









#ABSTRACT SUPER CLASS WITH NO INSTANCES ABOVE
class Page(object):#SUPER CLASS #putting object here is borrowing stuff fro object class #ABSRACT CLASS NOW THAT WE HAVE NO INSTANCES
    def __init__(self): #constructor function to call below functions that page needs to access
        self._head = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title>Meister Weather</title>
    </head>
    <body>'''

        self._body = 'Meister Weather Forecast'
        self._close = '''
    </body>
</html>'''


    def print_out(self):
        return self._head + self._body + self._close

class FormPage(Page):
    def __init__(self):#construction function for FormPage class
        #constructor function for super class has to be constructed
        super(FormPage, self).__init__() # or write like ====>   Page.__init__()    <==== MUST CALL SUPER CLASS
        self._form_open = '<form method="GET">'
        self._form_close = '</form>'
        self.__inputs = [] 
        self._form_inputs = ''
        #inputs type="text" value="" name=""
        #<input type="text" value="" name="first_name" placeholder"First name" /> ['first_name', 'text', 'First Name']
        #<input type="text" value="" name="first_name" placeholder"Last name" />
        #<input type="submit" value="submit" />

    @property
    def inputs(self):
        pass

    @inputs.setter
    def inputs(self, arr):
        #changing my private input variable and
        self.__inputs = arr
        #sort through the array to create html inputs
        for item in arr:
           self._form_inputs += '<input type="' + item[1] + '" name=" ' + item[0]
           #if there is a third item.... add it in...
           try:
                self._form_inputs += '" placeholder=" '+ item[2]+'"/>'
           #otherwise end tag
           except:
                self._form_inputs += '" />'
        print self._form_inputs



    #POLYMORPHISM!!!!!!!! ----------------- METHOD OVERRIDING
    def print_out(self):
        return self._head + self._body + self._form_open + self._form_inputs + self._form_close + self._close









#never touch the info below
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
