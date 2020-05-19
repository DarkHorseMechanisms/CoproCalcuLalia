print("Loading. Enter 'exit' to quit.")
from numpy.random import default_rng    # Using numpy's random module, generator function to generate question parts
rng = default_rng()                     # Shorten generator function

## Start Main Function ##
def main():
    questionroll()                      # Generate question (and corresponding solution)
    running = True                      # Set running to true so I can control the loop, and
    while running == True:              # Start the loop.
        userinput = input(question)     # Present the question and allow input
        if userinput.lower == "exit":   # If user asks to exit
            running = False             # Then kill the loop.
        try:                            # Otherwise start check sequence
            if int(userinput) == solution:      # Try matching userinput to solution; if so:
                z = "RIGHT"
            elif int(userinput) != solution:    # If it doesn't then:
                z = "wrong"
            check_list = ["That's ", z, ", you ", rng.choice(insults), "!"]  # Here are the elements for the response
            cuntycheck = ''.join([str(elem) for elem in check_list])  # get that looking nice in an overcomplicated way
            print(cuntycheck)   # print
            if z == "RIGHT":    # and if the user got the question right
                questionroll()  # roll a new question for the loop and start again
        except:
            fuckupmessage()        # If none of that works then just run me off a nice message and retry, same question.
## End Main Function ##

## Start Other Bullshit ##
def roll():                         # when I call roll, make
    w = rng.integers(2, high=16)    # w, which is to be a random int between 2 and 16,
    return w                        # and give it back to me

def questionroll():                 # when I call questionroll,
    x = roll()                      # roll x,
    y = roll()                      # roll y,
    global question                 # Give me a question that I can use anywhere in program.
    questionlist = [str(x), " times ", (y), "?\n"]      # Here I define the parts I will use to build the question
    question = ''.join([str(elem) for elem in questionlist])    # Here I join the parts of questionlist for question
    global solution     # Give me a solution that I can call on from anywhere,
    solution = x * y    # This is what that solution should be, as built from the same parts as the question
    return question     # After all of this, just give me back the question for now

def fuckupmessage():
    g = rng.choice(insults)         # You get two insults if you enter the wrong input type
    h = rng.choice(insults)         # (You're welcome)
    while g == h:                   # I don't want the insults to be the same
        h = rng.choice(insults)     # So reroll the second one until it's not
    f = " a "                       # splitting the indefinite article off but defaulting to 'a',
    if h[0] in 'aeiou':             # so that if the first letter of h (second insult) is a vowel,
        f = " an "                  # I can change the preceding  article to 'an'
    print("You did a fuckup, you ", g, ", and also, you are", f, h, sep='')     # Print that looking nice (different
                                                                                # method as only strings here)
insults = ["shit gobbler",              # This is a tuple containing insults
           "arse monkey",               # They're mostly British, regional, idiosyncratic etc
           "cum snatcher",              # Selected, curated, remembered and created for your amusement while learning
           "dickslap",                  # You can make pull requests to add to this list but be warned your
           "spunknapper",               # addition might not be accepted.
           "squirt burglar",
           "jizzlip",
           "fannyflap",
           "berry",
           "bum admirer",
           "rectal cavity",
           "inferior product",
           "unoriginal",
           "obstacle to intelligent life",
           "imitation human",
           "bad impression",
           "snuck frottage",
           "mongoose",
           "dumblebee",
           "rat's knobcheese",
           "bollock-hat",
           "ample cankle",
           "demonstration of chodery",
           "tig ol' bitty",
           "lone thunderthigh",
           "unkempt pubis",
           "facsimile",#
           "berk",
           "unbeknownst lurking knobgoblin",
           "dick",
           "unexpected clitpunch",
           "unfindable clitoris",
           "shape in the distance",
           "coronavirus hive",
           "decrepit old loon",
           "cake eater",
           "user of glass chopping boards",
           "clunking hate machine"
           "dildonicon"
           ]
if __name__ == '__main__':
    main()