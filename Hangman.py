import turtle
import time

def firsterror():
    penguin = turtle.Turtle()  # Remember the capital T
    # A speed of 0 makes him go as fast as possible

    arm_length = 100  # Change these if you want
    leg_length = 120

    def reset():  # reset sends him back to the center
        penguin.pu()  # pu is short for penup. Either work, you can use them interchangeably
        penguin.setpos(0, 50)
        penguin.pd()  # pd is short for pendown

    def base():
        penguin.pu()
        penguin.setpos(-100, -150)
        penguin.pd()

    def stick():
        penguin.pu()
        penguin.setpos(-150, -150)
        penguin.pd()

    # draw a stickman
    base()
    penguin.speed(0)
    penguin.seth(270)
    penguin.rt(90)
    penguin.fd(50)
    penguin.seth(180)
    penguin.fd(50)
    stick()
    # stick
    penguin.speed(0)
    penguin.seth(90)
    penguin.fd(350)
    penguin.rt(90)
    penguin.fd(150)
    penguin.rt(90)
    penguin.fd(50)

    reset()

    # head
    penguin.speed(1)
    penguin.seth(90)  # seth is short for set_heading, and it changes the direction jim is facing.

    penguin.rt(90)
    penguin.circle(50)

    turtle.clear()


def seconderror():
    penguin = turtle.Turtle()  # Remember the capital T
    # A speed of 0 makes him go as fast as possible

    arm_length = 100  # Change these if you want
    leg_length = 120

    def reset():  # reset sends him back to the center
        penguin.pu()  # pu is short for penup. Either work, you can use them interchangeably
        penguin.setpos(0, 50)
        penguin.pd()  # pd is short for pendown

    def base():
        penguin.pu()
        penguin.setpos(-100, -150)
        penguin.pd()

    def stick():
        penguin.pu()
        penguin.setpos(-150, -150)
        penguin.pd()

    # draw a stickman
    base()
    penguin.speed(0)
    penguin.seth(270)
    penguin.rt(90)
    penguin.fd(50)
    penguin.seth(180)
    penguin.fd(50)
    stick()
    # stick
    penguin.speed(0)
    penguin.seth(90)
    penguin.fd(350)
    penguin.rt(90)
    penguin.fd(150)
    penguin.rt(90)
    penguin.fd(50)

    reset()

    # head
    penguin.speed(0)
    penguin.seth(90)  # seth is short for set_heading, and it changes the direction jim is facing.

    penguin.rt(90)
    penguin.circle(50)

    # arm
    reset()

    # arm 1
    penguin.speed(1)
    penguin.seth(230)
    penguin.fd(arm_length)

    turtle.clear()


def thirderror():
    penguin = turtle.Turtle()  # Remember the capital T
    # A speed of 0 makes him go as fast as possible

    arm_length = 100  # Change these if you want
    leg_length = 120

    def reset():  # reset sends him back to the center
        penguin.pu()  # pu is short for penup. Either work, you can use them interchangeably
        penguin.setpos(0, 50)
        penguin.pd()  # pd is short for pendown

    def base():
        penguin.pu()
        penguin.setpos(-100, -150)
        penguin.pd()

    def stick():
        penguin.pu()
        penguin.setpos(-150, -150)
        penguin.pd()

    # draw a stickman
    base()
    penguin.speed(0)
    penguin.seth(270)
    penguin.rt(90)
    penguin.fd(50)
    penguin.seth(180)
    penguin.fd(50)
    stick()
    # stick
    penguin.speed(0)
    penguin.seth(90)
    penguin.fd(350)
    penguin.rt(90)
    penguin.fd(150)
    penguin.rt(90)
    penguin.fd(50)

    reset()

    # head
    penguin.speed(0)
    penguin.seth(90)  # seth is short for set_heading, and it changes the direction jim is facing.

    penguin.rt(90)
    penguin.circle(50)

    # arm
    reset()

    # arm 1
    penguin.speed(0)
    penguin.seth(230)
    penguin.fd(arm_length)

    reset()

    # arm 2
    penguin.speed(1)
    penguin.seth(310)
    penguin.fd(arm_length)

    turtle.clear()


def fourtherror():
    penguin = turtle.Turtle()  # Remember the capital Ta
    # A speed of 0 makes him go as fast as possible

    arm_length = 100  # Change these if you want
    leg_length = 120

    def reset():  # reset sends him back to the center
        penguin.pu()  # pu is short for penup. Either work, you can use them interchangeably
        penguin.setpos(0, 50)
        penguin.pd()  # pd is short for pendown

    def base():
        penguin.pu()
        penguin.setpos(-100, -150)
        penguin.pd()

    def stick():
        penguin.pu()
        penguin.setpos(-150, -150)
        penguin.pd()

    # draw a stickman
    base()
    penguin.speed(0)
    penguin.seth(270)
    penguin.rt(90)
    penguin.fd(50)
    penguin.seth(180)
    penguin.fd(50)
    stick()
    # stick
    penguin.speed(0)
    penguin.seth(90)
    penguin.fd(350)
    penguin.rt(90)
    penguin.fd(150)
    penguin.rt(90)
    penguin.fd(50)

    reset()

    # head
    penguin.speed(0)
    penguin.seth(90)  # seth is short for set_heading, and it changes the direction jim is facing.

    penguin.rt(90)
    penguin.circle(50)

    # arm
    reset()

    # arm 1
    penguin.speed(0)
    penguin.seth(230)
    penguin.fd(arm_length)

    reset()

    # arm 2
    penguin.speed(0)
    penguin.seth(310)
    penguin.fd(arm_length)

    reset()

    # body
    penguin.speed(1)
    penguin.seth(270)
    penguin.fd(150)

    turtle.clear()


def fiftherror():
    penguin = turtle.Turtle()  # Remember the capital T
    # A speed of 0 makes him go as fast as possible

    arm_length = 100  # Change these if you want
    leg_length = 120

    def reset():  # reset sends him back to the center
        penguin.pu()  # pu is short for penup. Either work, you can use them interchangeably
        penguin.setpos(0, 50)
        penguin.pd()  # pd is short for pendown

    def base():
        penguin.pu()
        penguin.setpos(-100, -150)
        penguin.pd()

    def stick():
        penguin.pu()
        penguin.setpos(-150, -150)
        penguin.pd()

    # draw a stickman
    base()
    penguin.speed(0)
    penguin.seth(270)
    penguin.rt(90)
    penguin.fd(50)
    penguin.seth(180)
    penguin.fd(50)
    stick()
    # stick
    penguin.speed(0)
    penguin.seth(90)
    penguin.fd(350)
    penguin.rt(90)
    penguin.fd(150)
    penguin.rt(90)
    penguin.fd(50)

    reset()

    # head
    penguin.speed(0)
    penguin.seth(90)  # seth is short for set_heading, and it changes the direction jim is facing.

    penguin.rt(90)
    penguin.circle(40)

    # arm
    reset()

    # arm 1
    penguin.speed(0)
    penguin.seth(230)
    penguin.fd(arm_length)

    reset()

    # arm 2
    penguin.speed(0)
    penguin.seth(310)
    penguin.fd(arm_length)

    reset()

    # body
    penguin.speed(0)
    penguin.seth(270)
    penguin.fd(150)

    # leg 1
    penguin.speed(1)
    penguin.seth(230)
    penguin.fd(leg_length / 2)

    turtle.clear()


def sixtherror():
    penguin = turtle.Turtle()  # Remember the capital T
    # A speed of 0 makes him go as fast as possible

    arm_length = 100  # Change these if you want
    leg_length = 120

    def reset():  # reset sends him back to the center
        penguin.pu()  # pu is short for penup. Either work, you can use them interchangeably
        penguin.setpos(0, 70)
        penguin.pd()  # pd is short for pendown

    def base():
        penguin.pu()
        penguin.setpos(-100, -150)
        penguin.pd()

    def stick():
        penguin.pu()
        penguin.setpos(-150, -150)
        penguin.pd()

    # draw a stickman
    base()
    penguin.speed(0)
    penguin.seth(270)
    penguin.rt(90)
    penguin.fd(50)
    penguin.seth(180)
    penguin.fd(50)
    stick()
    # stick
    penguin.speed(0)
    penguin.seth(90)
    penguin.fd(350)
    penguin.rt(90)
    penguin.fd(150)
    penguin.rt(90)
    penguin.fd(50)

    reset()

    # head
    penguin.speed(0)
    penguin.seth(90)  # seth is short for set_heading, and it changes the direction jim is facing.

    penguin.rt(90)
    penguin.circle(40)

    # arm
    reset()

    # arm 1
    penguin.speed(0)
    penguin.seth(230)
    penguin.fd(arm_length)

    reset()

    # arm 2
    penguin.speed(0)
    penguin.seth(310)
    penguin.fd(arm_length)

    reset()

    # body
    penguin.speed(0)
    penguin.seth(270)
    penguin.fd(150)

    # leg 1

    penguin.speed(0)
    penguin.seth(230)
    penguin.fd(leg_length / 2)

    # leg 2
    penguin.speed(0)
    penguin.seth(50)
    penguin.fd(leg_length / 2)

    penguin.speed(1)
    penguin.seth(310)
    penguin.fd(leg_length / 2)

    turtle.clear()


def lost():
    penguin = turtle.Turtle()
    arm_length = 100
    leg_length = 120

    def reset():
        penguin.pu()
        penguin.setpos(0, 70)
        penguin.pd()

    def base():
        penguin.pu()
        penguin.setpos(-100, -150)
        penguin.pd()

    def stick():
        penguin.pu()
        penguin.setpos(-150, -150)
        penguin.pd()

    # draw a stickman
    base()
    penguin.speed(0)
    penguin.seth(270)
    penguin.rt(90)
    penguin.fd(50)
    penguin.seth(180)
    penguin.fd(50)
    stick()
    # stick
    penguin.speed(0)
    penguin.seth(90)
    penguin.fd(350)
    penguin.rt(90)
    penguin.fd(150)
    penguin.rt(90)
    penguin.fd(50)

    reset()

    # head
    penguin.speed(0)
    penguin.seth(90)  # seth is short for set_heading, and it changes the direction jim is facing.

    penguin.rt(90)
    penguin.circle(40)

    # arm
    reset()

    # arm 1
    penguin.speed(0)
    penguin.seth(230)
    penguin.fd(arm_length)

    reset()

    # arm 2
    penguin.speed(0)
    penguin.seth(310)
    penguin.fd(arm_length)

    reset()

    # body
    penguin.speed(0)
    penguin.seth(270)
    penguin.fd(150)

    # leg 1

    penguin.speed(0)
    penguin.seth(230)
    penguin.fd(leg_length / 2)

    # leg 2
    penguin.speed(0)
    penguin.seth(50)
    penguin.fd(leg_length / 2)

    penguin.speed(0)
    penguin.seth(310)
    penguin.fd(leg_length / 2)
    reset()

    # left eye
    penguin.speed(50)
    penguin.pu()
    penguin.setpos(-20, 120)
    penguin.pd()
    penguin.seth(45)
    penguin.fd(10)
    penguin.seth(225)
    penguin.fd(20)
    penguin.pu()
    penguin.setpos(-20, 120)
    penguin.pd()
    penguin.seth(135)
    penguin.fd(10)
    penguin.seth(315)
    penguin.fd(20)

    # right eye
    penguin.speed(10)
    penguin.pu()
    penguin.setpos(20, 120)
    penguin.pd()
    penguin.seth(45)
    penguin.fd(10)
    penguin.seth(225)
    penguin.fd(20)
    penguin.pu()
    penguin.setpos(20, 120)
    penguin.pd()
    penguin.seth(135)
    penguin.fd(10)
    penguin.seth(315)
    penguin.fd(20)

    penguin.pu()
    penguin.setpos(-100, -150)
    penguin.pd()
    penguin.speed(1)
    penguin.seth(0)
    penguin.fd(200)

    turtle.clear()


def dance():
    penguin = turtle.Turtle()
    arm1 = turtle.Turtle()
    arm2 = turtle.Turtle()
    penguin.hideturtle()
    arm2.hideturtle()
    arm1.hideturtle()

    arm_length = 100
    leg_length = 120

    def reset():
        penguin.pu()
        penguin.setpos(0, 46)
        penguin.pd()
        arm1.pu()
        arm1.setpos(0, 46)
        arm1.pd()
        arm2.pu()
        arm2.setpos(0, 46)
        arm2.pd()

    def base():
        penguin.pu()
        penguin.setpos(-100, -150)
        penguin.pd()

    def stick():
        penguin.pu()
        penguin.setpos(-150, -150)
        penguin.pd()

    # draw a stickman
    base()
    penguin.speed(0)
    penguin.seth(270)
    penguin.rt(90)
    penguin.fd(50)
    penguin.seth(180)
    penguin.fd(50)
    stick()
    # stick
    penguin.speed(0)
    penguin.seth(90)
    penguin.fd(350)
    penguin.rt(90)
    penguin.fd(150)
    penguin.rt(90)
    penguin.fd(50)

    reset()

    # head
    penguin.speed(0)
    penguin.seth(90)

    penguin.rt(90)
    penguin.circle(40)

    # arm
    reset()

    # arm 1
    arm1.speed(0)
    arm1.seth(230)
    arm1.fd(arm_length)

    reset()

    # arm 2
    arm2.speed(0)
    arm2.seth(310)
    arm2.fd(arm_length)

    reset()

    # body
    penguin.speed(0)
    penguin.seth(270)
    penguin.fd(150)

    # leg 1

    penguin.speed(0)
    penguin.seth(230)
    penguin.fd(leg_length / 2)

    # leg 2
    penguin.speed(0)
    penguin.seth(50)
    penguin.fd(leg_length / 2)

    penguin.speed(0)
    penguin.seth(310)
    penguin.fd(leg_length / 2)
    reset()
    for i in range(3):
        # PAUSE
        time.sleep(0.5)

        arm1.clear()
        arm1.speed(0)
        arm1.seth(170)
        arm1.fd(arm_length)

        # PAUSE
        time.sleep(0.5)

        reset()
        arm2.clear()
        arm2.speed(0)
        arm2.seth(10)
        arm2.fd(arm_length)

        # PAUSE
        time.sleep(0.5)
        reset()
        arm1.clear()
        arm1.speed(0)
        arm1.seth(5)
        arm1.fd(arm_length)

        # PAUSE
        time.sleep(0.5)

        reset()
        arm2.clear()
        arm2.speed(0)
        arm2.seth(310)
        arm2.fd(arm_length)

        # PAUSE
        time.sleep(0.5)
        reset()
        arm1.clear()
        arm1.speed(0)
        arm1.seth(165)
        arm1.fd(arm_length)

        time.sleep(0.5)
        reset()
        arm2.clear()
        arm2.speed(0)
        arm2.seth(230)
        arm2.fd(arm_length)

    turtle.clear()


"""
functions = {1: firsterror(), 2: seconderror(), 3: thirderror(),
             4: fourtherror(),
             5: fiftherror(), 6: sixtherror, 7: lost(), 8: dance()}
"""


def function_call(wr_attempts):
    if wr_attempts == 1:
        firsterror()
        turtle.clearscreen()
    elif wr_attempts == 2:
        seconderror()
        turtle.clearscreen()
    elif wr_attempts == 3:
        thirderror()
        turtle.clearscreen()
    elif wr_attempts == 4:
        fourtherror()
        turtle.clearscreen()
    elif wr_attempts == 5:
        fiftherror()
        turtle.clearscreen()
    elif wr_attempts == 6:
        lost()
        turtle.clearscreen()
    elif ("_ " not in guess):
        dance()


class Player:
    def __init__(self, name, score=0):
        self.name = name
        self.score = score

    def score_incr(self):
        self.score += 1 * ("_ " not in guess)

    def get_score(self):
        return self.score


print("Rules :-")
print("1.This is a 2 -player game lets call them player 1 and player.")
print("2.At first Player 1 will enter a secret word for player 2.")
print("3.Then Player 1 will enter a meaningful hint for player 2 to help with guessing the word.")
print("4.Then Player 1 can enter a guess letter and if it exists in the word it will be shown in the program.")
print("5.Player will get exactly 6 wrong attempt after which their hangman will die.")
print("6.Player 2 will go next and they can go in turns for as many terms as previously decided")
print("7.At last player with the best score will win")

print("Please put the turtle graphic console opened in the background in a split screen with the IDE as it is a major part of the game")

enter = input("Press Enter to start.......")

for i in range(5):
    print("")
print("--------Let's do the entries for the game--------")
print("")
player1 = Player(input("Enter the name of first player here :"))
player2 = Player(input("Enter the name of second player here :"))
turns = int(input("Please enter the number of turns for this game here :"))

for i in range(turns):
    print("-----Round", i + 1, "-----")
    for i in range(3):
        print("")
    print("------Its player 1's turn to give the word------")
    word1 = input("Please enter the  word here :").upper()
    hint = input("Give a hint for your word")
    word = list(word1)
    guess = ["_ "] * len(word)
    wr_attempts = 0
    for i in range(100):
        print("")
    print(*guess)
    print("------Please pass the device to player 2------")
    print("Your Hint is : ", hint, "'", sep="")
    while wr_attempts < 6 and "_ " in guess:
        let = input("Enter your guess letter here :").upper()
        present = False
        wr_attempts += (let in guess)
        for j in range(len(word)):
            if word[j] == let:
                guess[j] = let
                present = True
        if not present:
            wr_attempts += 1
        print(*guess)
        if wr_attempts == 6:
            print("You have had your 6  attempts. Alas, now your Hangman is dead!!")
        function_call(wr_attempts)
    player2.score_incr()

    for i in range(10):
        print("")

    print("------Its player 2's turn to give the word------")
    word1 = input("Please enter the  word here :").upper()  # player 2's turn
    hint = input("Give a hint for your word")
    word = list(word1)
    guess = ["_ "] * len(word)
    wr_attempts = 0
    for i in range(100):
        print("")
    print(*guess)
    print("------Please pass the device to player 1------")
    print("Your Hint is : ", hint, "'", sep="")
    while wr_attempts < 6 and "_ " in guess:
        let = input("Enter your guess letter here :").upper()
        present = False
        wr_attempts += (let in guess)
        for j in range(len(word)):
            if word[j] == let:
                guess[j] = let
                present = True
        if not present:
            wr_attempts += 1
        print(*guess)
        if wr_attempts == 6:
            print("You have had your 6  attempts. Alas, now your Hangman is dead!!")
        function_call(wr_attempts)
    player1.score_incr()

    for i in range(10):
        print("")

for i in range(3):
    print("")

print(sorted([player1, player2], key=Player.get_score)[0].name * (not player1.score == player2.score),
      "Both played good, its a Draw!!." * (player1.score == player2.score),
      "is the winner." * (not player1.score == player2.score))
