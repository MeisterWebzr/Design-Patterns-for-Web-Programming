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
        p1.player_avg = 40

        print "Player 1: " + p1.name +" Age: "+ str(p1.age) +" Team: "+p1.team +" Position: " + p1.position + " PPG(avg): " + str(p1.player_avg)


        #PLAYER TWO
        p2 = Player() #data object for player one
        p2.name = "Raymond Jordan" #name attribute for player one
        p2.age = 21  #age attribute for player one
        p2.team = "LA Lakers" #team attribute for player one
        p2.position = "Point Guard" #position attribute for player one
        p2.game1 = 7 #storing average points per game 1
        p2.game2 = 30 #storing average points per game 2
        p2.game3 = 9 #storing average points per game 3
        p2.game4 = 20 #storing average points per game 4
        p2.game5 = 21 #storing average points per game 5
        p2.calc_ppg() #calling the calc_ppg function

        #concatenated the player printout
        print "Player 2: " + p2.name +" Age: "+ str(p2.age) +" Team: "+p2.team +" Position: " + p2.position + " PPG(avg): " + str(p2.player_avg)


        #PLAYER THREE
        p3 = Player() #data object for player one
        p3.name = "Kyle Lewis" #name attribute for player one
        p3.age = 19  #age attribute for player one
        p3.team = "Orlando Magic" #team attribute for player one
        p3.position = "Power Forward" #position attribute for player one
        p3.game1 = 15 #storing average points per game 1
        p3.game2 = 10 #storing average points per game 2
        p3.game3 = 9 #storing average points per game 3
        p3.game4 = 20 #storing average points per game 4
        p3.game5 = 9 #storing average points per game 5
        p3.calc_ppg() #calling the calc_ppg function

        #concatenated the player printout
        print "Player 3: " + p3.name +" Age: "+ str(p3.age) +" Team: "+p3.team +" Position: " + p3.position + " PPG(avg): " + str(p3.player_avg)

        #PLAYER FOUR
        p4 = Player() #data object for player one
        p4.name = "Andrew Allen" #name attribute for player one
        p4.age = 28  #age attribute for player one
        p4.team = "Miami Heat" #team attribute for player one
        p4.position = "Center" #position attribute for player one
        p4.game1 = 15 #storing average points per game 1
        p4.game2 = 20 #storing average points per game 2
        p4.game3 = 3 #storing average points per game 3
        p4.game4 = 20 #storing average points per game 4
        p4.game5 = 21 #storing average points per game 5
        p4.calc_ppg() #calling the calc_ppg function

        #concatenated the player printout
        print "Player 4: " + p4.name +" Age: "+ str(p4.age) +" Team: "+p4.team +" Position: " + p4.position + " PPG(avg): " + str(p4.player_avg)

        #PLAYER FIVE
        p5 = Player() #data object for player one
        p5.name = "Mike Zepeda" #name attribute for player one
        p5.age = 20  #age attribute for player one
        p5.team = "Boston Celtics" #team attribute for player one
        p5.position = "Power Forward" #position attribute for player one
        p5.avg = 15 #avergage points per game
        p5.game1 = 15 #storing average points per game 1
        p5.game2 = 20 #storing average points per game 2
        p5.game3 = 9 #storing average points per game 3
        p5.game4 = 11 #storing average points per game 4
        p5.game5 = 0 #storing average points per game 5
        p5.calc_ppg() #calling the calc_ppg function

        #concatenated the player printout
        print "Player 5: " + p5.name +" Age: "+ str(p5.age) +" Team: "+p5.team +" Position: " + p5.position + " PPG(avg): " + str(p5.player_avg)


       #self.response.write("Welcome to the NBA Ball Stats") #testing write to browser
       #self.response.write("Player 1: " + player1.name)



class Page(object):
    def __init__(self):#initlizing the function of itself to begin
        self.title = "Starting 5 Stats!" #setting title of application
        self.css = "css/main.css" #setting css dir of application
        #setting head to begin structure of html for application
        self.head = """
        <!DOCTYPE HTML>
        <html>
            <head>
                <title>Starting 5</title>
                <link href="{self.css}" rel="stylesheet" type="text/css" />
            </head>
            <header></header>
            <body>
            <div id="bbox">
                <div id="block"></div><div id="midad"><h1>Starting 5 Line up</h1></div><div id="block"></div>
                <a href="?name=Brent Burroughs">Brent Burroughs</a>
                <a href="?name=Raymond Jordan">Raymond Jordan</a>
                <a href="?name=Kyle Lewis">Kyle Lewis</a>
                <a href="?name=Andrew Allen">Andrew Allen</a>
                <a href="?name=Mike Zepeda">Mike Zepeda</a>
            </div>
        """
        self.body = " "
        self.close = """
            </body>
        </html>
        """

    def print_out(self):#function for printing out the page sections
        all = self.head + self.body + self.close#printing out page all with head, body & close elements
        all = all.format(**locals())#printing locals for attaching and updating with locals **
        return all#return all to send all above info to browser






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



    @property#setting property for player avg
    def player_avg(self):
        #calculatintg player avg pts per game
        return self.__player_avg


    @player_avg.setter #setter for player avg getter
    def player_avg(self, new_player_avg):
        #changing new points per game for player one
        self.__player_avg = new_player_avg

    def calc_ppg(self):#new calc for new attributes avg point per game
        self.__player_avg = (self.game1 + self.game2 + self.game3 + self.game4 + self.game5)/5#the calculation for adding all scres then dividing by the number of games in array




#never touch the information below
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
