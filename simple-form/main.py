'''
Otto "Meister" Burroughs
8-11-14
DPWP Online
Simple Form
'''
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):

        page_head = '''<!DOCTYPE HTML>
<html>
    <head>
        <link rel="stylesheet" href="css/main.css">
        <title>Web work Request</title>
    </head>
    <body>'''

        page_body = '''
            <form>

        '''


        page_close = '''
        </form>
    </body>
</html>'''








#never touch the info below
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
