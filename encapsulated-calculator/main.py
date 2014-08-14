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
        p1.avg = 28

        #PLAYER TWO
        p2 = Player() #data object for player one
        p2.name = "Raymond Jordan" #name attribute for player one
        p2.age = 21  #age attribute for player one
        p2.team = "LA Lakers" #team attribute for player one
        p2.position = "Point Guard" #position attribute for player one
        p2.avg = 35

        #PLAYER THREE
        p3 = Player() #data object for player one
        p3.name = "Kyle Lewis" #name attribute for player one
        p3.age = 19  #age attribute for player one
        p3.team = "Orlando Magic" #team attribute for player one
        p3.position = "Power Forward" #position attribute for player one
        p3.avg = 12 #avergage points per game


        #PLAYER FOUR
        p4 = Player() #data object for player one
        p4.name = "Andrew Arellano" #name attribute for player one
        p4.age = 28  #age attribute for player one
        p4.team = "Miami Heat" #team attribute for player one
        p4.position = "Center" #position attribute for player one
        p4.avg = 20 #avergage points per game


        #PLAYER FIVE
        p5 = Player() #data object for player one
        p5.name = "Mike Zepeda" #name attribute for player one
        p5.age = 20  #age attri bute for player one
        p5.team = "Boston Celtics" #team attribute for player one
        p5.position = "Power Forward" #position attribute for player one
        p5.avg = 15 #avergage points per game

        print p5.team_avg

        #self.response.write("Welcome to the NBA Ball Stats<br />") #testing write to browser
        #elf.response.write("Player 1: " + player1.name)



class Player(object):#template for data object for players
    def __init__(self):#constructor function
        self.name = ""   #storing public information player name
        self.age = "" #storing public information player age
        self.team = "" #storing public information player team name
        self.position = "" #storing public information player position
        self.game1 = 0 #storing average points per game player 1
        self.game2 = 0 #storing average points per game player 2
        self.game3 = 0 #storing average points per game player 3
        self.game4 = 0 #storing average points per game player 4
        self.game5 = 0 #storing average points per game player 5
        self.__team_avg = 0 #storing team average points as private

    @property
    def team_avg(self):
        #calculate the team average
        return self.__team_avg







#never touch the information below
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
