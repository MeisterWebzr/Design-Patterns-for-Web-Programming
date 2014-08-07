# Opener for madlib super hero game
#String 1
superhero = raw_input("Enter your Superhero's name:  ")

#raw impu for superhero age
age = raw_input("Enter your Superhero's age:")
sex = raw_input("Is your Superhero male or female?  ")
'''
if sex = str(male):
    pass
elif sex = str(female):
    pass
else:
    print "please enter either male or female"
'''

power = raw_input("Enter your Superhero's power:  ")
how = raw_input("How did your Superhero get those powers? This can be something like, getting hit by lightning or"
                "falling in a bio hazardous river. Be creative!  ")
time = raw_input("How long did it take for your SuperHero to master his powers?  ")
flaw = raw_input("All Superhero's have flaws, so what flaw does your Superhero have. This can be the power itself or "
                 "something simple like rabbits paralyze his legs or blind him for 10 seconds.  ")

personality = raw_input("What type of personality does your super hero have? ie; Bully, shy, pompous or witty and "
                        "energetic.  ")
outfits = raw_input("How many villians does your Superhero have?  ")

def calcArea(h, w):
        area = h * w
        return area
a = calcArea(210, 240);
#print "My speed  is " + str(a) + " mph"


print superhero + " is " + age + " with "+  sex + " " + power + " that has " + outfits + " x's " + personality + " superpower. "+ " consealing" \
                                                                                                   " and has a deadly flaw that "\
      + flaw + " which derived from " + how + ". But, flying through at " + str(a) + " mph is fast almost the fastest."

'''
#conditional statement determining superhero's power
if age <19:
    #stuff if condition is true
    power = "Animation"
    print superhero + " Your power is " + power + ". Also known as Thought Projection, is the power to bring " \
                                                  "inanimate objects to life or to free a person from petrification." \
                                                  " Mr. Mxyzptlk used this power on a mannequin, a statue, and even " \
                                                  "the Daily Planet."
#else if statement determining super hero power if age is older than 20
elif:
    power = "Gravitokinesis"
    print superhero + " Your power is " + power + ". The ability to control or generate gravity. Though " \
                                                  "Gravitokinesis is not as widespread as other powers, it " \
                                                  "has still managed to be an important power. One of the most" \
                                                  " recent uses of gravitokinesis is in the Marvel Next character, " \
                                                  "whose name is fittingly Gravity."
'''