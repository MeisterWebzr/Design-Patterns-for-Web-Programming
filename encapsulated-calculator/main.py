'''
__author__ = 'Meister'
august 13 2014
DPWP Online
'''
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):

        #PLAYER ONE
        p1 = Player() #data object for player one
        p1.name = "Brent Burroughs" #name attribute for player one
        p1.age = 23 #age attribute for player one
        p1.team = "Chicago Bulls" #team attribute for player one
        p1.position = "Power Forward" #position attribute for player one
        p1.avg = ""

        #PLAYER TWO
        p2 = Player() #data object for player one
        p2.name = "Raymond Jordan" #name attribute for player one
        p2.age = 21  #age attribute for player one
        p2.team = "Los Angelas Lakers" #team attribute for player one
        p2.position = "Point Guard" #position attribute for player one


        #PLAYER THREE
        p3 = Player() #data object for player one
        p3.name = "Kyle Lewis" #name attribute for player one
        p3.age = 19  #age attribute for player one
        p3.team = "Orlando Magic" #team attribute for player one
        p3.position = "Power Forward" #position attribute for player one

        #PLAYER FOUR
        p4 = Player() #data object for player one
        p4.name = "Andrew Arellano" #name attribute for player one
        p4.age = 28  #age attribute for player one
        p4.team = "Miami Heat" #team attribute for player one
        p4.position = "Center" #position attribute for player one




        #self.response.write("Welcome to the NBA Ball Stats<br />") #testing write to browser
        #elf.response.write("Player 1: " + player1.name)



class Player(object):#template for data object for players
    def __init__(self):#constructor function
        self.name = ""   #storing public information
        self.age = "" #storing public information
        self.team = "" #storing public information
        self.position = "" #storing public information
        self.ppg = "" #storing public information


class GameStats(object):#template game points calculation
    def __init__(self):#constructor function
        self.stat1 =  0
        self.stat2 =  0
        self.stat3 =  0
        self.stat4 =  0
        self.stat5 =  0
        self.__points_per_game = 0 #setting private ppg attribute










#never touch the information below
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
