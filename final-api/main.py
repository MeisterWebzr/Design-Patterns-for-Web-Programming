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

        if self.request.GET:
            sm = SearchModel()
            sm.search = self.request.GET['search']
            sm.callApi()
            sv = SearchView()
            sv.sdos = sm.dos
            p._body = sv.content
        self.response.write(p.print_out())

'''
self.content = ''   #this code worked
list = xmldoc.getElementsByTagName("title")
self.response.write(xmldoc.getElementsByTagName('title')[0].firstChild.nodeValue+"<br/>")
self.response.write(xmldoc.getElementsByTagName('title')[1].firstChild.nodeValue)
'''


class SearchView(object):
    '''This data will be shown to the user based on the controller '''
    def __init__(self):#contstructor class to init self
        self._sdos = [] #setting search dos view from SearchModel
        self.__content = '<br />' #break tag for visual line placement

    def update(self):#update for items in search list
        for do in self.__sdos:
            self.__content += "Your search results for: " + do.header + '<br/>' #writing title
            self.__content += do.title + '<br/>' #writing title
            self.__content += '<br/>' + do.description + '<br/>'#writing description
            self.__content += '<br/>' + do.link + '<br/>' #writing link
            self.__content += do.pub + '<br />'  #writing link
            self.__content += "All rights reserved by " + do.copyright  #writing link

    @property #read only getter
    def content(self):
        return self.__content #returning content


    @property
    def sdos(self):
        pass


    @sdos.setter
    def sdos(self, arr):
        self.__sdos = arr
        self.update()


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
        print "This is my URL: " + self.__url+self.__search


        #creating object with urllib2
        opener = urllib2.build_opener()
        #getting result from url- request from api
        result = opener.open(request)
        #parse the xml with minidom
        self.__xmldoc = minidom.parse(result)

        #print self.__xmldoc.getElementsByTagName('title')[0].firstChild.nodeValue

        #sorting data from yahoo news api
        self._dos = [] #setting variable for dos array
        do = SearchData() #setting do = to SearchData function
        do.header = self.__xmldoc.getElementsByTagName('title')[0].firstChild.nodeValue #setting do title to item tag name 'title'
        do.title = self.__xmldoc.getElementsByTagName('title')[1].firstChild.nodeValue #setting do title to item tag name 'title'
        do.description = self.__xmldoc.getElementsByTagName('description')[1].firstChild.nodeValue #getting description
        do.link = self.__xmldoc.getElementsByTagName('link')[1].firstChild.nodeValue #getting link info
        do.pub = self.__xmldoc.getElementsByTagName('pubDate')[0].firstChild.nodeValue #getting publish date first child value
        do.copyright = self.__xmldoc.getElementsByTagName('copyright')[0].firstChild.nodeValue #getting copyright info first child value

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
        print "search word: "+ self.__search

class SearchData(object):
    ''' This data object will store the fetch info from model shown by the view'''
    def __init__(self):#contstructor class to init self
        self.header = '' #storing title from media item
        self.title = '' #storing title from media item
        self.description = '' #storing description from media item
        self.link = '' #storing link from media item
        self.pub = '' #storing link from media item
        self.copyright = '' #storing link from media item

#this will serve as our abstract class with no instances
class Page(object):
    def __init__(self):#constructor function to call functions below
        #setting title of application
        self.title="Get your lucky News!"
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
        return  self._head + "Meister's Lucky News. Search and see.. powered by Yahoo!"+ self._form_open + self._form_inputs + self._form_close + self._body + self._close



#never touch info below
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
