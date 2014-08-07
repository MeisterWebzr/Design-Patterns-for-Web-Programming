#one line comments
'''

All of these line are called doc strings- used to label functions just before the first line of the function
 DOC STRING
'''


first_name = "Kermit"
last_name = "De Frog"

#underscore is used opposed to camel casing in all pythin code


#response = raw_input("Enter your name  ")

#print "Hello there Meister, ",  response


birth_year = 1981
current_year = 2014
age = current_year - birth_year
#print "Hello young buck!, you're " + str(age)+ " years old."



'''

do not use increments or decrementers



'''

#int(var) for creating strings into numbers 

budget = 75

if budget > 100:
    #stuff if condition is true
    brand = "nike"
    #print"Awesome! you can buy some " + brand + " shoes."
elif budget > 70:
    #print "you can afford to buy some AND 1 kicks"
    pass
else:
    pass

characters =["Meister", " brent"," Katelyn","Mara"]
characters.append("Gabbana dog")
#print characters[0]


movies = dict() #create dictionary object
movies = {"Eddie Murphy":"Coming to America", "Friday":"Chris Tucker"}
# print movies["Eddie Murphy"]

'''

while Loops in python
can look in an array, arrange
can look in objects
look through dictionary


'''
'''
#WHILE LOOP --------------------
i = 0
while i<9:
    print "The count is", i
    i = i+1
pass

print "end while loop"


#FOR LOOP------------------------

for i in range(0,10):
    print "The count is", i
    i = i+1

'''

#"FOR EACH" LOOP-----------------
#great for objects and arrays----

designers = ["Meister Webzr", "Otto Burroughs", "yada yada", "the others"]
for r in designers:
   #print r
    #print "One of the best designers is"
    pass


'''

#FUNCTIONS-----------------------

def calcArea(h, w):
    area = h * w
    return area
a = calcArea(20, 40);
print "My area is " + str(a) + "sqft"

'''
'''
#object OOP CHANGE CONTENT TO BE DYNAMIC USING **LOCAL()
title = "Meister Works"
body = "Freelance Web Designer & Developer"
message = '''
'''
    <DOCTYPE HTML>
    <html>
        <head>
            <title>{title}</title>
        </head>
        <body>
            <h1>{body}</h1
        </body>
    </html>
'''
#message = message.format(**locals())
#print message
print "Hello Otto"