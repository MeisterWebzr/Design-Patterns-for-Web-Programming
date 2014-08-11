'''
Otto "Meister" Burroughs
8-11-14
DPWP Online
Simple Form
'''
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):

        page_head = '''<!DOCTYPE HTML><!-- Begin HTML -->
<html>
    <head>
        <link rel="stylesheet" href="css/main.css">
        <title>Web work request</title>
    </head>
    <body>'''

        page_body = '''
            <div id="ad"><h1>Summer orders get 25% off</h1></div>
            <fieldset>Summer orders get 25% off</fieldset>
            <form>
            <div class="row"><label>First name:</label><input type="text" name="firstname" required></div>
            <div class="row"><label>Last name:</label><input type="text" name="lastname" required></div>
            <div class="row"><label>Email main:</label><input type="text" name="email" required></div>
            <div class="row"><label>Best Contact#:</label><input type="tel" name="tel" required></div>
            <div class="row">
                <label>Project Type:</label>
                    <select name="project" required>
                        <option value="Graphic Design">Graphic Design</option>
                        <option value="Web Design">Web Design</option>
                        <option value="Prototype Application">Prototype Application</option>
                        <option value="Web Development">Web Development</option>
                        <option value="Network / Hosting">Network / Hosting</option>
                        <option value="Mobile App Design">Mobile App Design</option>
                        <option value="Monthly Web Maintenance">Monthly Web Maintenance</option>
                        <option value="Wireframes / Mockups">Wireframes / Mockups</option>
                        <option value="Company Branding">Company Branding</option>
                        <option value="Hosting">Hosting</option>
                        <option value="Ecommerce Setup">Ecommerce Setup</option>
                    </select>
            </div>
            <div class="row">

                <input type="checkbox" name"Terms" value="Terms" required>You agree to the above information being valid ans true.

            </div>




            <input id="sub" type="submit" name="" value="Submit">

        '''


        page_close = '''
        </form>
    </body>
</html>'''


        if self.request.GET:
            firstname = self.request.GET['firstname']
            lastname = self.request.GET['lastname']
            email = self.request.GET['emai']








#never touch the info below
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
