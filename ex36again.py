print "Welcome back princess. Where you wanna go? 1. bubble room or door 2. pink room?"

room = raw_input("--> ")

if room == "1":
    print "Wow!! Welcome to bubbleroom! Hope you will enjoy here."
    print "1. Drink those bubble as soda."
    print "2. Swimming in the bubble room."

    princess = raw_input("> ")

    if princess == "1":
        print "Enjoy! The bubble soda, princess."
    elif princess == "2":
        print "Bubble colours of the day is baby blue, enjoy it princess!"
    else:
        print "Do you want to try a %s massage today, princess?" % princess

elif room == "2":
    print "Welcome back princess! your favourite bedroom the pink room, princess.What would you like to do?"
    print "1. change outfit."
    print "2. have a nap."

    pink = raw_input("--> ")

    if pink == "1":
        print "Which dresses do you like to change today, princess?"
    elif pink == "2":
        print "Have a nice dream, princess."
    else:
        print "Do you want to have some afternoon tea, princess?"
else:
    print "You are not princess, G4S will catch you and kill you!!"