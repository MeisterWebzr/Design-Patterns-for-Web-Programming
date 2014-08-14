'''
__author__ = 'Meister'
august 13 2014
DPWP Online
'''
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        
        p = Page()
        self.response.write(p.print_out())

        #PLAYER ONE
        p1 = Player() #data object for player one
        p1.name = "Brent Burroughs" #name attribute for player one
        p1.age = 23 #age attribute for player one
        p1.team = "Chicago Bulls" #team attribute for player one
        p1.position = "Power Forward" #position attribute for player one
        p1.game1 = 15 #storing average points per game 1
        p1.game2 = 20 #storing average points per game 2
        p1.game3 = 9 #storing average points per game 3
        p1.game4 = 20 #storing average points per game 4
        p1.game5 = 21 #storing average points per game 5
        self.response.write("Avg PPG: " + str(p1.player_avg))

        #PLAYER TWO
        p2 = Player() #data object for player one
        p2.name = "Raymond Jordan" #name attribute for player one
        p2.age = 21  #age attribute for player one
        p2.team = "LA Lakers" #team attribute for player one
        p2.position = "Point Guard" #position attribute for player one
        p2.game1 = 15 #storing average points per game 1
        p2.game2 = 20 #storing average points per game 2
        p2.game3 = 9 #storing average points per game 3
        p2.game4 = 20 #storing average points per game 4
        p2.game5 = 21 #storing average points per game 5

        #PLAYER THREE
        p3 = Player() #data object for player one
        p3.name = "Kyle Lewis" #name attribute for player one
        p3.age = 19  #age attribute for player one
        p3.team = "Orlando Magic" #team attribute for player one
        p3.position = "Power Forward" #position attribute for player one
        p3.game1 = 15 #storing average points per game 1
        p3.game2 = 20 #storing average points per game 2
        p3.game3 = 9 #storing average points per game 3
        p3.game4 = 20 #storing average points per game 4
        p3.game5 = 21 #storing average points per game 5


        #PLAYER FOUR
        p4 = Player() #data object for player one
        p4.name = "Andrew Arellano" #name attribute for player one
        p4.age = 28  #age attribute for player one
        p4.team = "Miami Heat" #team attribute for player one
        p4.position = "Center" #position attribute for player one
        p4.game1 = 15 #storing average points per game 1
        p4.game2 = 20 #storing average points per game 2
        p4.game3 = 9 #storing average points per game 3
        p4.game4 = 20 #storing average points per game 4
        p4.game5 = 21 #storing average points per game 5


        #PLAYER FIVE
        p5 = Player() #data object for player one
        p5.name = "Mike Zepeda" #name attribute for player one
        p5.age = 20  #age attri bute for player one
        p5.team = "Boston Celtics" #team attribute for player one
        p5.position = "Power Forward" #position attribute for player one
        p5.avg = 15 #avergage points per game
        p5.game1 = 15 #storing average points per game 1
        p5.game2 = 20 #storing average points per game 2
        p5.game3 = 9 #storing average points per game 3
        p5.game4 = 20 #storing average points per game 4
        p5.game5 = 21 #storing average points per game 5

        #self.response.write("Welcome to the NBA Ball Stats<br />") #testing write to browser
        #elf.response.write("Player 1: " + player1.name)

class Page(object):
    def __init__(self):
        self.title = "Welcome!"
        self.css = "css/main.css"
        self.head = """
<!DOCTYPE HTML>
<html>
    <head>
        <title>{self.title}</title>
        <link href="{self.css}" rel="stylesheet" type="text/css" />
    </head>
    <body>

        """
        self.body = "Welcome to Meister's OOP Python page!"
        self.close = """
    </body>
</html>
        """

    def print_out(self):
        all = self.head + self.body + self.close
        all = all.format(**locals())
        return all


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
        self.__player_avg = 0 #storing team average points as private

    @property
    def player_avg(self):
        #calculate the team average
        self.__player_avg = (self.game1 + self.game2 + self.game3 + self.game4 + self.game5)/5
        return self.__player_avg







#never touch the information below
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
