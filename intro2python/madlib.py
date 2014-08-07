
#Opener for madlib super hero game
#String 1
superhero = raw_input("Enter your Superhero's name  ")

#raw impu for superhero age
age = raw_input("Enter your Superhero's age  ")


#conditional statement determining superhero's power
if age < 20:
    #stuff if condition is true
    power = "Animation"
    print superhero + " Your power is " + power + ". Also known as Thought Projection, is the power to bring inanimate objects to life or to free a person from petrification. Mr. Mxyzptlk used this power on a mannequin, a statue, and even the Daily Planet."
#else if statement determining super hero power if age is older than 20
elif age > 20:
    power = "Gravitokinesis"
    print superhero + " Your power is " + power + ". The ability to control or generate gravity. Though Gravitokinesis is not as widespread as other powers, it has still managed to be an important power. One of the most recent uses of gravitokinesis is in the Marvel Next character, whose name is fittingly Gravity."
    pass