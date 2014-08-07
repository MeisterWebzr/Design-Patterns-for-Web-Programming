
# Opener for madlib super hero game
#String 1
superhero = raw_input("Enter your Superhero's name:  ")
#raw impu for superhero age
age = raw_input("Enter your Superhero's age: ")
#asking sex of super hero
sex = raw_input("Is your Superhero male or female?  ")
#raw input for superhero power
power = raw_input("What's your Superhero power?  ")
#asking for how the super hero got the super powers
how = raw_input("How did your Superhero get those powers? This can be something like, getting hit by lightning or"
                "falling in a bio hazardous river. Be creative!  ")
#asking for how long the super hero took to learn or master the super powers
time = raw_input("How long did it take for your SuperHero to master his powers?  ")
#raw input for flaw question
flaw = raw_input("All Superhero's have flaws, so what flaw does your Superhero have. This can be the power itself or "
                 "something simple like rabbits paralyze his legs or blind him for 10 seconds.  ")

personality = raw_input("What type of personality does your super hero have? ie; Bully, shy, pompous or witty and "
                        "energetic.  ")
outfits = raw_input("How many villians does your Superhero have?  ")

def calcArea(h, w):
        area = h * w
        return area
a = calcArea(210, 122);

print superhero + " is " + age + " "+  sex + ". With " + power + " ability and " + outfits +\
      " x's " + personality + " of a regular human. "+ " Flaw: " + flaw + ". " + superhero +" " + how + \
      ". But, flying through at " + str(a) + " mph wicked fast. " + superhero + " is now entered into the Hall of" \
                                                                                " Fame, see details below."

#"FOR EACH Supehero hall of fame" LOOP
halloffame = ["Superman 2010", "Wonder Woman 2011","Batman 2012", "Meister Webzr 2013", superhero + " 2014"]
for r in halloffame:
    print "W3C Hall of Fame winner " + r
    pass
print "thank you for creating a super hero with Madlib. Type clear and hit ENTER"