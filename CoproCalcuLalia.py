from numpy.random import default_rng   # Using numpy's random module, generator function to generate question parts

print("Loading.")

rng = default_rng()

def roll():                         # when I call roll,
    w = rng.integers(2, high=16)    # get w, which is going to be a random int between 2 and 16,
    return w                        # and give it back to me

def questionroll():             # when I call questionroll,
    x = roll()                      # roll x,
    y = roll()                      # roll y,

    global question                                     # Give me a question that I can use anywhere in program.

    questionlist = [str(x), " times ", (y), "?\n"]      # Here I define the parts I will use to build the question
    question = ''.join([str(elem) for elem in questionlist])    # Here I join the parts of the question and assign the
                                                                # result to the global 'question' that I made

    global solution     # Give me a solution that I can call on from anywhere,
    solution = x * y    # this is what that solution should be, built from the same parts as the question

    return question     # After all of this, just give me back the question

def fuckupmessage():
    g = rng.choice(insults)         # You get two insults if you enter the wrong input type
    h = rng.choice(insults)
    while g == h:                   # I don't want the insults to be the same
        h = rng.choice(insults)     # So reroll the second one until it's not
    f = " a "                        # splitting the indefinite article off but defaulting to 'a',
    if h[0] in 'aeiou':             # if the first letter of h (second insult) is a vowel,
        f = " an "                    # change article to precede it to 'an'
    print("You did a fuckup, you ", g, ", and also, you are", f, h, sep='')    # Print that shit

insults = ["shit gobbler",              # This is a tuple containing insults
           "arse monkey",               # They're mostly British, regional, idiosyncratic etc
           "cum snatcher",              # Selected and created for humourousness
           "dickslap",
           "spunknapper",
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
           ]

questionroll()                      # Ok so roll me a question, keep it out of the loop though
running = True                      # And set running to true
while running == True:              # Here's me loop
    userinput = input(question)         # Let userinput be the input given by user on seeing question from questionroll
    try:
        if int(userinput) == solution:      # Try matching it to the solution from questionroll. If it matches then
            z = "RIGHT"
        elif int(userinput) != solution:    # If it doesn't then
            z = "wrong"
        check_list = ["That's ", z, ", you ", rng.choice(insults), "!"] # Here are the elements for the response
        cuntycheck = ''.join([str(elem) for elem in check_list])        # get that looking nice in an overcomplicated way
        print(cuntycheck)                                               # print that shit
        if z == "RIGHT":                                                # and if the user got the question right
            questionroll()                                              # roll a new question for the loop
    except:                            # If none of that works then run me off a fuckupmessage. don't change the question
        fuckupmessage()

