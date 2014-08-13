'''
__author__ = 'Meister'
august 13 2014
DPWP Online
'''
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):

        player1 = Player() #dataobject for player one
        player1.name = "Brent Burroughs" #name attribute for player one
        player1.age = "21" #age attribute for player one
        player1.team = "Chicago Bulls" #team attribute for player one
        player1.position = "PG" #position attribute for player one






class Player(object):#template for data object for players
    def __init__(self):#constructor function
        self.name = ""   #storing public information
        self.age = "" #storing public information
        self.team = "" #storing public information
        self.position = "" #storing public information
        self.ppg = "" #storing public information

        self.response.write('Hello world!')








#never touch the information below
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
