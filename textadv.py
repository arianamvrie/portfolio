gameOn = True

while gameOn:
    print ("It's your senior year! And this is your last chance to make memories with the people you've known throughout your four years of high school. Will you be able to find your balance with your school work and having fun? Or will having fun take a toll on where life takes you?")
    print("Party or Study?")
    option = input()
    if option == "study":
        print("You decided to go and be studious while all of your friends go out to the party, but you end up acing your test the following morning!")
        print("You're at home and decide to study some more when all of a sudden, you get a phone call. It's your friend and she wants you to go to a kickback with her.")
        print("Will you go to the 'kickback' or 'be studious'?")
        option = input()
        if option == "kickback":
            print("You go to the kickback and just chill with people from your school. However, you have college apps to finish.")
            print("Will you 'leave now' or 'chill'?")
            option = input()
            if option == "leave now":
                print("You are the definition of a scholar! Because of your INCREDIBLE efforts, you go to a prestigous university and become a millionaire! GO YOU!!")
            elif option == "chill":
                print("Interesting...you get the best of both worlds! You have fun, but you also get your apps done! You get into your top choice and become a successful intellectual!")
                gameOn = False
        if option == "be studious":
            print("You are the definition of a scholar! Because of your INCREDIBLE efforts, you go to a prestigous university and become a millionaire! GO YOU!!")
            gameOn = False
    elif option == "party":
        print("You impulsively give into going to your friend's party. About an hour passes and your phone starts to buzz. You notice that your mom has called 9 times...")
        print("do you want to 'go home' or 'stay'?")
        option = input()
        if option == "go home":
            print("You fun times are over now. it's time to go home and hit the books!")
            print("Will you actually 'hit the books' or 'procrasinate' just a bit longer?")
            option = input()
            if option == "hit the books":
                print("You are the true definition of a scholar! Because of your INCDREDIBLE efforts, you go to a prestigous university and become a millionaire! GO YOU!!")
                gameOn = False
            elif option == "procrasinate":
                print("Because your procrasination gets the best of you, you never submit all of your college apps. However, you still attend a decent college and make your parents proud. You have successfully achieved higher education!")
                gameOn = False
        elif option == "stay":
            print("You decide to stay and have the best night of your senior year! You meet a lot of friends from different schools nearby.")
            print("It's getting pretty late and you start to think that it is time to leave, but your crush that you've had throughout high school slowly approaches you.")
            print("Will you 'hang out' with them a little longer or 'leave' and work on your college apps?")
            option = input()
            if option == "hang out":
                print("You stay with your crush and hang out with him in the backyard of the house.")
                print("All of a sudden...you hear a familar voice that sounded like it was yelling your name...")
                print("It's your MOM. She shuts down the party and drags you out of the party. You become a social outcast with no friends.")
                gameOn = False
            elif option == "leave":
                print("You decide that your crush is not worth your time. YOU ARE AN INDEPENDENT INTELLECTUAL! You decide to go home.")
                print("Your decisions got you to where you are! Although you did not get into your top choice, you still have the best time at a college that you did not expect to be at! Your family is proud of you achieving a higher education!")
                gameOn = False
