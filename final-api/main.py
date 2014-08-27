'''
Student: Otto Burroughs
Date: 8-21-2014
Assignment: GEA Launcher
'''
import webapp2
import urllib2#here we import all the classes and code needed to request info, receive that info and open info
from xml.dom  import minidom


class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = SearchArea()
        p.inputs = [['search','text','please enter search term']]
        self.response.write(p.print_out())

        if self.request.GET:

            '''
            self.content = ''
            list = xmldoc.getElementsByTagName("title")
            self.response.write(xmldoc.getElementsByTagName('title')[0].firstChild.nodeValue+"<br/>")
            self.response.write(xmldoc.getElementsByTagName('title')[1].firstChild.nodeValue)
            '''


class SearchView(object):
    '''This data will be shown to the user based on the controller '''
    def __init__(self):#contstructor class to init self
        pass


class SearchModel(object):
    '''This model handles fetching, parsing and sorting from yahoo search api '''
    def __init__(self):#contstructor class to init self
        self.__url = "http://news.search.yahoo.com/rss?p=" #setting url for api
        self.__search = '' #setting string for search input
        self.__xml = '' #linking xml string to model

    #contacting the yahoo news api
    def callApi(self):
        #assembling request
        request = urllib2.Request(self.__url+self.__search)
        #creating object with urllib2
        opener = urllib2.build_opener()
        #getting result from url- request from api
        result = opener.open(request)
        #parse the xml with minidom
        self.__xmldoc = minidom.parse(result)

        #sorting data from yahoo news api
        list = self.__xmldoc.getElementByTagName("media:item") #gettting element by media item
        self._dos = [] #setting variable for dos array
        for item in list: #loop items in search list
            do = SearchData() #setting do = to SearchData function
            do.title = item.attributes['title'].value #setting do.title to item tag name 'title'
            do.description = item.attributes['description'].value #setting do.description to item tag name 'description'
            do.link = item.attributes['link'].value#setting do.link to item tag name 'link'
            self._dos.append(do) #appending dos

    @property #getter for returning dos data
    def dos(self):#init dos to self
        return self._dos #returning dos

    @property
    def search(self):
        pass

    @search.setter #setting search setter
    def search(self, s): #declaring search init to self and s
        self.__search = s #self search variable = s


class SearchData(object):
    ''' This data object will store the fetch info from model shown byt the view'''
    def __init__(self):#contstructor class to init self
        self.title = '' #storing title from media item
        self.description = '' #storing description from media item
        self.link = '' #storing link from media item


#this will serve as our abstract class with no instances
class Page(object):
    def __init__(self):#constructor function to call functions below
        #setting title of application
        self.title="News 4 U!"
        self._head='''
<!DOCTYPE HTML>
<html>
    <head>
    <title>Get the news!</title>
    <link rel="stylesheet" href="css/main.css" >
    </head>
    <body>'''
        #body section where all content will go
        self._body = '<div id="box"></div>'
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
            #setting number of arrays depending on what inputs i create at top of file
            try: #try this
                self._form_inputs += '"placeholder="'+item[2]+'"/>'
            except:# otherwise
                self._form_inputs += '"/>'
        #print self._form_inputs



    #POLYMORPHISM!!!!!!!! ----------------- METHOD OVERRIDING
    def print_out(self):
        #returning the Page printout here using polymorphism to override
        return  self._head + "Meister News powered by Yahoo!"+ self._form_open + self._form_inputs + self._form_close + self._body + self._close




#never touch info below
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
