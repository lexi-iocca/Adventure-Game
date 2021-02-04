"""Adventure Project
Adventure Project.py
Demonstrates functions, if statements,
lists, sound, classes and easygui
Lexi Iocca
11/06/17
"""

import easygui
import character  # links the character code to this one
import pygame

pygame.init()  # allows sound to be added to the game
pygame.mixer.init()
Backpack = character.Character()  # makes backpack where user can store items they find during game

# these are the lines that attach the sound to a variable
backtrack = pygame.mixer.Sound("backtrack.ogg")
wave = pygame.mixer.Sound("waves.ogg")
bear1 = pygame.mixer.Sound("Griz.ogg")
planeSound = pygame.mixer.Sound("plane.ogg")
shiny = pygame.mixer.Sound("shiny.ogg")
rolling = pygame.mixer.Sound("rolling.ogg")
lose = pygame.mixer.Sound("lose.ogg")
champ = pygame.mixer.Sound("champ.ogg")
think1 = pygame.mixer.Sound("think1.ogg")


def setup():
    backtrack.play()  # plays through the whole game
    global name
    name = easygui.enterbox("Please enter your name so we can get started", "Island Escape",
                            image="hello.gif")
    # so their name can be used in messages throughout the game but don't
    # have to enter it if they want to play again
    intro()


def intro():
    easygui.msgbox(name + ", you are the only person who survived a plane crash", "Island Escape",
                   image="planecrash.gif")  # explain what the object of the game is
    easygui.msgbox(
        "You ended up on a deserted island and you have to find a way to survive and escape at the same time!",
        "Island Escape", image="es.gif")
    easygui.msgbox(
        "You have a backpack for anything you find to help you but be aware- you can only use an item more than once "
        "if you collect it more than once",
        "Island Escape", image="back.gif")
    easygui.msgbox("Good Luck and Be Careful out there!", "Island Escape", image="good.gif")
    main()


def main():  # the central area of the game- everything branches off from it
    choice = easygui.buttonbox("Where do you want to go?", "Island Escape",
                               choices=('Stay on Beach', 'Ocean', 'Forest', 'Mountain'), image="island.gif")
    if choice == "Stay on Beach":
        beach()
    elif choice == "Ocean":  # if / elif statements used so the player is brought to where they choose from above
        ocean()
    elif choice == "Forest":
        forest()
    else:
        mountain()


################################################

def beach():
    sheltOrFire = easygui.buttonbox("You have arrived at the beach, what would you like to do?", "Island Escape",
                                    choices=('Build Shelter', 'Build a Fire', 'I want to go somewhere else'))
    if sheltOrFire == "Build Shelter":
        shelter()
    elif sheltOrFire == "I want to go somewhere else":  # in case they want to go back
        main()
    else:  # build a fire
        fire()


def shelter():  # you need sticks to build a shelter
    if Backpack.checkInventory("sticks"):  # if sticks is found in there backpack it allows them to build a shelter
        easygui.msgbox(
            "Good job, " + name + ", now you have a place to take cover but you still need to get off of this island!",
            "Island Escape", image="shelter.gif")
        Backpack.removeFromInventory("sticks")
        main()
    else:  # if they don't have sticks they have to go back
        easygui.msgbox("You can't build a shelter without sticks!", "Island Escape", image="ee.gif")
        beach()


def fire():  # need sticks and either trout or boar to be able to create a fire
    if Backpack.checkInventory("sticks") and Backpack.checkInventory("trout") or Backpack.checkInventory("boar"):
        Backpack.removeFromInventory("sticks" and "trout")
        planeSound.play()
        easygui.msgbox("Just before you take your first bite, a plane sees the smoke signal and you get saved",
                       "Island Escape", image="fire.gif")
        survive()
    elif Backpack.checkInventory("sticks") and Backpack.checkInventory("boar"):
        Backpack.removeFromInventory("sticks" and "boar")
        planeSound.play()
        easygui.msgbox("Just before you take your first bite, a plane sees the smoke signal and you get saved",
                       "Island Escape", image="fire.gif")
        survive()
    else:  # don't have food or sticks - or neither so they have to go back
        easygui.msgbox("Come back when you have sticks and something to cook, you haven't eaten in a while",
                       "Island Escape", image="hun.gif")
        main()


#############################################

def forest():
    huntOrCollect = easygui.buttonbox("Now do you want to do:", "Island Escape",
                                      choices=('hunt', 'collect sticks', 'back to beach'))
    if huntOrCollect == "hunt":
        hunt()
    elif huntOrCollect == "back to beach":
        main()
    else:  # collect sticks
        Backpack.addToInventory("sticks")  # added to inventory since they need it to be able to complete some tasks
        easygui.msgbox("Sticks have been added to your backpack", "Island Escape", image="stick.gif")
        forest()


def hunt():  # need sticks`
    animal = easygui.buttonbox("What would you like to hunt?", "Island Escape", choices=('deer', 'wild boar'),
                               image="what.gif")
    if animal == "deer":
        if Backpack.checkInventory("sticks"):
            easygui.msgbox("Darn deer was too quick " + name + ", and you were just too darn slow", "Island Escape",
                           image="deer.gif")
            Backpack.removeFromInventory(
                "sticks")  # sticks are removed so they have to go collect more before they can use them again
            tryanimal2 = easygui.buttonbox("Now What?", "Island Escape",
                                           choices=('try catching a boar', 'go back to the forest'))
            if tryanimal2 == "try catching a boar":
                boar()
            else:  # go back to forest
                forest()
        else:  # if they don't have sticks they have to go back
            easygui.msgbox("You need sticks to make a hunting tool first", "Island Escape", image="hunt.tool.gif")
            forest()
    else:  # choose boar instead
        boar()
        forest()


def boar():
    if Backpack.checkInventory("sticks"):  # make sure they have sticks or they have to go back
        Backpack.addToInventory("boar")  # add boar to inventory
        easygui.msgbox("A wild boar has been added to you backpack", "Island Escape", image="wild.gif")
        Backpack.removeFromInventory("sticks")  # sticks removed
        forest()
    else:  # if they don't have sticks
        easygui.msgbox(name + ", you need sticks to make a hunting tool first", "Island Escape", image="hunt.tool.gif")
        forest()


#############################################

def ocean():
    wave.play()
    catchOrSwim = easygui.buttonbox("What would you like to do?", "Island Escape",
                                    choices=('catch food', 'try swimming to safety', 'back to beach'))
    if catchOrSwim == "back to beach":
        main()
    elif catchOrSwim == "try swimming to safety":
        easygui.msgbox("Oh no, there was a storm and you drowned!", "Island Escape", image="storm.gif")
        lose.play()
        restart()
    else:
        catch()


def catch():
    fishfood = easygui.buttonbox("What do you want to catch?", "Island Escape", choices=('trout', 'shark'))
    if fishfood == "trout":  # need sticks (if they have sticks- add trout to inventory)
        if Backpack.checkInventory("sticks"):
            Backpack.addToInventory("trout")
            easygui.msgbox("A trout has been added to your backpack", "Island Escape", image="trout.gif")
            Backpack.removeFromInventory("sticks")
            ocean()
        else:
            easygui.msgbox("Come on " + name + ", you need to find something to spear the fish with first",
                           "Island Escape", image="spear.gif")
            main()

    else:  # need sticks (to catch a shark)
        if Backpack.checkInventory("sticks"):
            easygui.msgbox("Unfortunately, that shark was a little more desperate for food than you were :(",
                           "Island Escape", image="bruce.gif")
            Backpack.removeFromInventory("sticks")
            lose.play()
            restart()
        else:
            easygui.msgbox("You need something to kill the shark with before you go hunting " + name, "Island Escape",
                           image="spear.gif")
            main()


############################################

def mountain():
    searchOrTop = easygui.buttonbox("What do you want to do", "Island Escape",
                                    choices=('Search the Rocks', 'Go to the Top', 'back to beach'))
    if searchOrTop == "back to beach":
        main()
    elif searchOrTop == "Search the Rocks":
        search()
    else:  # go to the top
        toTop()


def toTop():
    toRuins = easygui.buttonbox("From the top of the mountain you see ancient ruins, do you want to go?",
                                "Island Escape", choices=('yes', 'no'))
    if toRuins == "no":  # sent back to the mountain
        mountain()
    else:  # go to ancient ruins
        chooseTemple()


def chooseTemple():
    atRuin = easygui.buttonbox("What do you want to do?", "Island Escape", choices=(
        'Look in temple 1', 'Look in temple 2', 'Look in temple 3', 'Go Back to the Mountain'), image="temples.gif")
    if atRuin == "Look in temple 1":
        temple1()
    elif atRuin == "Look in temple 2":
        temple2()
    elif atRuin == "Look in temple 3":
        temple3()
    else:  # back to mountain
        mountain()


def temple1():  # need a key to open the treasure chest
    easygui.msgbox("ooh, you found a treasure chest", "Island Escape", image="chest.gif")
    if Backpack.checkInventory("key"):  # can't open the treasure chest without finding they key first
        easygui.msgbox("Good thing I found the key earlier", "Island Escape", image="key.gif")
        Backpack.addToInventory("jewels")
        shiny.play()  # plays sound effect
        Backpack.removeFromInventory("key")  # once they use the key it is removed from their backpack
        easygui.msgbox("Jewels have been added to your backpack", "Island Escape", image="jewel.gif")
        chooseTemple()
    else:  # if they don't have the key
        easygui.msgbox(
            "Sorry, " + name + " you will need a key before you get your hands on whatever is in the treasure chest",
            "Island Escape", image="key.gif")
        chooseTemple()  # sent back to choose another temple or go back


def temple2():
    easygui.msgbox("You fell in a trap!!!", "Island Escape", image="trap.gif")  # the game ends/they lose
    restart()


def temple3():
    password = "age"
    passOpt = easygui.buttonbox(
        "You have to get the correct answer to this riddle to unlock a secret door that you found. You only have one "
        "try, do you want to go for it?",
        "Island Escape", choices=('yes', 'no'))
    if passOpt == "yes":
        think1.play()
        passInput = easygui.enterbox("What goes up, but doesn't go back down", "Island Escape",
                                     image="think.gif").lower()  # changes answer to lowercase so if they entered the
        # correct answer in uppercase it still works
        if passInput == password:
            easygui.msgbox("Good job " + name + "!!!")
            easygui.msgbox(
                "The door opens up into a secret bunker where you find a radioset. You use it to signal for help and...",
                "Island Escape")
            survive()
        else:
            easygui.msgbox("Oh no, " + name + ", the answer was age :(", "Island Escape")
            easygui.msgbox(
                "The floor opens up beneath you and you fall into a dungeon cell, trapped for hundreds of years, "
                "but don't worry, you won't be alone for long...",
                "Island Escape", image="cell.gif")
            if Backpack.checkInventory("jewels"):
                easygui.msgbox(
                    "But wait, there is a hole in the wall the exact size of one of those jewels you remember finding "
                    "earlier...",
                    "Island Escape")
                easygui.msgbox("You rummage through your backpack to find the jewel and fit it into the wall...",
                               "Island Escape", image="fit.gif")
                easygui.msgbox(
                    "It's a perfect fit! The door of your dungeon cell opens up and you run through the halls of the "
                    "jail where you find a hanger "
                    "with a plane in it waiting for you, you've never flown a plane before but you find a manual and "
                    "there's a first time for everything!",
                    "Island Escape", image="plane.gif")
                easygui.msgbox("You buckle up and fly away into the sunset and back home", "Island Escape",
                               image="sunset.gif")
                survive()
            else:  # They don't have the jewels
                lose.play()
                restart()
    else:
        chooseTemple()


def search():
    caveOrNo = easygui.buttonbox("You found the entrance to a cave, do you want to enter it?", "Island Escape",
                                 choices=('yes', 'no'), image="cave.gif")
    if caveOrNo == "yes":
        cave()
    else:  # don't want to enter the cave
        mountain()


def cave():
    leftRight = easygui.buttonbox("Which way do you want to go?", "Island Escape",
                                  choices=('left', 'right', 'I dont want to enter the cave'), image="leftright1.gif")
    if leftRight == "left":  # add key to inventory
        Backpack.addToInventory("key")
        easygui.msgbox("You found a key, it has been added to your backpack", "Island Escape", image="key.gif")
        cave()
    elif leftRight == "I dont want to enter the cave":
        mountain()
    else:  # right
        right()


def right():
    bear1.play()
    bear = easygui.buttonbox("AHHHHHHH, A BEAR, WHAT DO YOU DO?", "Island Escape", choices=('go back', 'attack it'),
                             image="bearr.gif")
    if bear == "go back":
        mountain()
    else:  # attack it
        attack()


def attack():
    easygui.msgbox("You have to roll a die, if you roll a 1 you live and if you roll a 2, the bear does",
                   "Island Escape", image="die.gif")
    from random import randint
    roll = (randint(1, 2))  # generates either 1 or 2 for the die roll
    rolling.play()
    if roll == 1:  # they live
        easygui.msgbox("you rolled a 1", "Island Escape", image="one.gif")
        easygui.msgbox("You continue through the cave and find a river with a boat in it", "Island Escape")
        easygui.msgbox("You sail away from the island into safety!", "Island Escape", image="speed.gif")
        survive()
    else:  # roll = 2 so they have to restart or exit
        easygui.msgbox("you rolled a 2", "Island Escape", image="two.gif")
        easygui.msgbox("that means you didn't make it :(", "Island Escape")
        lose.play()
        restart()


#############################################

def survive():  # for if they find a way to escape the island/win
    champ.play()
    easygui.msgbox("YOU SURVIVED " + name.upper() + "!", "Island Escape", image="sur.gif")
    restart()


def restart():  # for if they want to play again- the game starts from the beginning
    playagain = easygui.buttonbox("Would you like to play again?", "Island Escape", choices=('yes', 'no'),
                                  image="playa.gif")
    if playagain == "yes":
        Backpack.removeFromInventory("sticks")
        Backpack.removeFromInventory("trout")
        Backpack.removeFromInventory(
            "boar")  # remove all the items so if they play again they start with an empty inventory
        Backpack.removeFromInventory("key")
        Backpack.removeFromInventory("jewels")
        intro()  # game restarts
    if playagain == "no":  # game ends
        exit()


###########################################

setup()  # calls the start of the game which leads to the different functions depending on what the user chooses
