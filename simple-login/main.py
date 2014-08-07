'''
Otto Burroughs
8-7-14
DWPA- online
madlib

'''
#
import webapp2 #use the webapp2 library

class MainHandler(webapp2.RequestHandler): #declaring a class
    def get(self):#funtion that starts everything. Catalyst
        self.response.write('Hello Meister!')
        name = raw_input("Enter your name:   ")
    def additional_functions(self):
        pass
        #code goes here

#never touch the below information
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
