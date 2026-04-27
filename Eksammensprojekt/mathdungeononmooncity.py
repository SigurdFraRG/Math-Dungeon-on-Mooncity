import sys
import time
import random

def delete_last_line():
    sys.stdout.write("\x1b[1A")
    sys.stdout.write("\x1b[2K")

def delete_title(n=1):
    for i in range(n):
        sys.stdout.write("\x1b[1A")
        sys.stdout.write("\x1b[2K")

boss = {
    "enemy": "goblin",
    "health": 20,
    "max_health": 20,
}
# dictionary for python (husker det som en ordbog)

attacks = {
    "latk": {"damage": 1, "hit_chance": 0.994}, #dict inside dict, with hit chance 99.4%
    "matk": {"damage": 2, "hit_chance": 0.6723}, # 67.23%
    "hatk": {"damage": 3, "hit_chance": 0.3045}, # 30.45%
}

delete_title(3)
thetext = [
    "████████╗██╗  ██╗███████╗",
    "╚══██╔══╝██║  ██║██╔════╝",
    "   ██║   ███████║█████╗ ",
    "   ██║   ██╔══██║██╔══╝ ",
    "   ██║   ██║  ██║███████╗",
    "   ╚═╝   ╚═╝  ╚═╝╚══════╝",
]

for line in thetext:
    print(line)
    time.sleep(0.2)

time.sleep(0.7)
delete_title(6)
time.sleep(0.7)
mathtext = [
    "███╗   ███╗ █████╗ ████████╗██╗  ██╗",
    "████╗ ████║██╔══██╗╚══██╔══╝██║  ██║",
    "██╔████╔██║███████║   ██║   ███████║",
    "██║╚██╔╝██║██╔══██║   ██║   ██╔══██║",
    "██║ ╚═╝ ██║██║  ██║   ██║   ██║  ██║",
    "╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝",
]
for line in mathtext:
    print(line)
    time.sleep(0.2)

time.sleep(0.7)
delete_title(6)
time.sleep(0.7)
dungeontext = [
    "██████╗ ██╗   ██╗███╗   ██╗ ██████╗ ███████╗ ██████╗ ███╗   ██╗",
    "██╔══██╗██║   ██║████╗  ██║██╔════╝ ██╔════╝██╔═══██╗████╗  ██║",
    "██║  ██║██║   ██║██╔██╗ ██║██║  ███╗█████╗  ██║   ██║██╔██╗ ██║",
    "██║  ██║██║   ██║██║╚██╗██║██║   ██║██╔══╝  ██║   ██║██║╚██╗██║",
    "██████╔╝╚██████╔╝██║ ╚████║╚██████╔╝███████╗╚██████╔╝██║ ╚████║",
    "╚═════╝  ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝ ╚══════╝ ╚═════╝ ╚═╝  ╚═══╝",
]
for line in dungeontext:
    print(line)
    time.sleep(0.2)

time.sleep(0.7)
while True:
        delete_title(21)
        themathdung = [
            "████████╗██╗  ██╗███████╗    ███╗   ███╗ █████╗ ████████╗██╗  ██╗    ██████╗ ██╗   ██╗███╗   ██╗ ██████╗ ███████╗ ██████╗ ███╗   ██╗",
            "╚══██╔══╝██║  ██║██╔════╝    ████╗ ████║██╔══██╗╚══██╔══╝██║  ██║    ██╔══██╗██║   ██║████╗  ██║██╔════╝ ██╔════╝██╔═══██╗████╗  ██║",
            "   ██║   ███████║█████╗      ██╔████╔██║███████║   ██║   ███████║    ██║  ██║██║   ██║██╔██╗ ██║██║  ███╗█████╗  ██║   ██║██╔██╗ ██║",
            "   ██║   ██╔══██║██╔══╝      ██║╚██╔╝██║██╔══██║   ██║   ██╔══██║    ██║  ██║██║   ██║██║╚██╗██║██║   ██║██╔══╝  ██║   ██║██║╚██╗██║",
            "   ██║   ██║  ██║███████╗    ██║ ╚═╝ ██║██║  ██║   ██║   ██║  ██║    ██████╔╝╚██████╔╝██║ ╚████║╚██████╔╝███████╗╚██████╔╝██║ ╚████║",
            "   ╚═╝   ╚═╝  ╚═╝╚══════╝    ╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝    ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝ ╚══════╝ ╚═════╝ ╚═╝  ╚═══╝",
        ]
        for line in themathdung:
            print(line)
            time.sleep(0.2)
        time.sleep(1)
        print("\n")
        print("                                                              --[Menu]--\n")
        time.sleep(0.1)
        print("                                                          ---START GAME[1]---\n")
        time.sleep(0.1)
        print("                                                          ---HOW TO PLAY[2]---\n")
        time.sleep(0.1)
        print("                                                            ---ABOUT US[3]---\n")
        time.sleep(0.1)
        print("                                                             ---QUIT[4]---\n")
    
        intro = input("Please enter a valid command: ").strip().lower()

        if intro == "1":
            delete_title(100)
            time.sleep(0.2)
            begintext = [
            "You find yourself walking down a narrow path...",
            "Trees surround you, as if you were trapped by them",
            "You continue walking..."
            ]
            for line in begintext:
                print(line)
                time.sleep(2)
            delete_title(4)
            forestscene = [
                r"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀",
                r"⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⡰⡇⠁⠀⠀⠀⠀⠀⢀⠀⠀⡰⡇⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⡰⡇⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⡰⡇⠁⠀⠀",
                r"⠀⠀⠀⠀⠀⠀⠀⠀⠰⢾⠇⠨⡦⠀⠂⠀⠀⠀⠀⠰⢾⠇⠨⡦⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⢾⠇⠨⡦⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⢾⠇⠨⡦⠀⠂⠀",
                r"⠀⠀⠀⠀⠀⠀⡀⠀⢈⣹⠜⠻⢾⠃⠀⠀⡀⠀⢈⣹⠜⠻⢾⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⢈⣹⠜⠻⢾⠃⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⢈⣹⠜⠻⢾⠃⠀⠀⠀⠀",
                r"⠀⠀⠀⠀⠀⠀⠁⢠⣿⡵⠾⣻⣶⠿⠦⠀⠁⢠⣿⡵⠾⣻⣶⠿⠦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⢠⣿⡵⠾⣻⣶⠿⠦⠀⠀⠀⠀⠀⠀⠁⢠⣿⡵⠾⣻⣶⠿⠦⠀⠀",
                r"⠀⠀⠀⠀⢀⠀⢀⣠⣮⣦⡶⠻⠛⢶⣄⡀⠁⠀⠀⣦⡶⠻⠛⢶⣄⡀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⢀⣠⣮⣦⡶⠻⠛⢶⣄⡀⠁⠀⠀⠀⠀⢀⠀⢀⣠⣮⣦⡶⠻⠛⢶⣄⡀⠁",
                r"⠀⠀⠀⠀⠀⠀⢀⣽⠏⠁⣠⣂⣦⣈⣝⣦⣄⠀⠈⠁⣠⣂⣦⣈⣝⣦⣄⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣽⠏⠁⣠⣂⣦⣈⣝⣦⣄⠀⠀⠀⠀⠀⢀⣽⠏⠁⣠⣂⣦⣈⣝⣦⣄⠀⠈⠁",
                r"⠀⠀⠀⠀⠁⣠⣾⣵⣾⣾⠟⡙⠟⠿⣍⡉⠀⠀⠆⣾⠟⡙⠟⠿⣍⡉⠀⠀⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⣠⣾⣵⣾⣾⠟⡙⠟⠿⣍⡉⠀⠀⠀⠀⠁⣠⣾⣵⣾⣾⠟⡙⠟⠿⣍⡉⠀⠀⠆",
                r"⠀⠰⠀⠀⠄⣠⣶⣾⣭⡶⠟⠻⣶⡰⣜⣳⣦⣄⠀⡀⠀⠻⣶⡰⣜⣳⣦⣄⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⠀⠀⠄⣠⣶⣾⣭⡶⠟⠻⣶⡰⣜⣳⣦⠀⠄⣠⣶⣾⣭⡶⠟⠻⣶⡰⣜⣳⣦⣄⠀⡀",
                r"⠀⠀⠀⢀⣠⣴⣿⣋⡴⣪⠎⣄⡙⠻⠿⣯⣉⠉⠀⠀⠎⣄⡙⠻⠿⣯⣉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣿⣋⡴⣪⠎⣄⡙⠻⠿⣯⣉⠀⢀⣠⣴⣿⣋⡴⣪⠎⣄⡙⠻⠿⣯⣉⠉⠀⠀",
                r"⠀⠂⠀⢀⣉⡭⢿⡛⣛⣵⠎⠀⠙⢾⣶⣦⣭⣷⣦⠐⠀⠀⠙⢾⣶⣦⣭⣷⣦⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⢀⣉⡭⢿⡛⣛⣵⠎⠀⠙⢾⣶⠀⠂⠀⢀⣉⡭⢿⡛⣛⣵⠎⠀⠙⢾⣶⣦⣭⣷⣦⠐",
                r"⠀⠀⢈⣙⣿⡿⠿⠟⣋⢅⡄⡄⡐⣄⢤⣉⠷⢦⣄⣀⠠⠀⡐⣄⢤⣉⠷⢦⣄⣀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⣙⣿⡿⠿⠟⣋⢅⡄⡄⡐⣄⠀⠀⠀⠀⢈⣙⣿⡿⠿⠟⣋⢅⡄⡄⡐⣄⢤⣉⠷⢦⣄⣀⠠",
                r"⠐⠾⠿⢽⣷⡶⠶⡿⣓⣭⣾⣿⢷⣬⣓⢿⠿⠿⣯⣉⣁⠀⢷⣬⣓⢿⠿⠿⣯⣉⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠾⠿⢽⣷⡶⠶⡿⣓⣭⣾⣿⢷⣬⠀⠐⠾⠿⢽⣷⡶⠶⡿⣓⣭⣾⣿⢷⣬⣓⢿⠿⠿⣯⣉⣁",
                r"⠀⠀⠀⠉⠉⠉⠛⠛⠉⢀⣿⢿⡀⠙⠋⠓⠿⠿⠏⠉⠉⠀⠀⠙⠋⠓⠿⠿⠏⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠛⠛⠉⢀⣿⢿⡀⠙⠋⠀⠀⠀⠉⠉⠉⠛⠛⠉⢀⣿⢿⡀⠙⠋⠓⠿⠿⠏⠉⠉",
                r"⠀⠀⠀⠀⠀⠀⠠⠤⠶⠾⢿⡯⠷⠶⠤⠄⠀⠀⠠⠤⠶⠾⢿⡯⠷⠶⠤⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠤⠶⠾⢿⡯⠷⠶⠤⠄⠀⠀⠀⠀⠀⠀⠠⠤⠶⠾⢿⡯⠷⠶⠤⠄",
            ]
            for line in forestscene:
                print(line)
                time.sleep(0.2)
            time.sleep(2)

            delete_title(50)

            thehole = [
                "As you finally reach an opening in the forest.",
                "You find yourself standing infront of a hole.",
                "It seems deep, as if there is no end.",
            ]
        
            for line in thehole:
                print(line)
                time.sleep(2)
            time.sleep(1.5)
            delete_title(3)

            hole = [
                "⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣠⣤⣤⣤⣤⣤⣤⣤⣤⣄⣀⣀",
                "⠀⠀⠀⢀⣤⣴⣾⣿⣿⡿⠿⠿⠿⠟⠛⠛⠻⠿⠿⠿⢿⣿⣿⣷⣦⣤⡀",
                "⠀⢀⣼⣿⡿⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⢿⣿⣧⡀",
                "⠀⢸⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⡇",
                "⠀⠈⢻⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⡟⠁",
                "⠀⠀⠀⠈⠛⠳⢦⣤⣄⣀⣀⡀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣠⣤⡴⠞⠛⠁",
                "⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠙⠛⠛⠛⠛⠛⠛⠛⠛⠋⠉⠉\n",
            ]
            for line in hole:
                print(line)
                time.sleep(0.2)

            print("As you stare into what seems like a bottomless hole, you think.\n")
            time.sleep(0.5)
            print("Should i inspect it? [Inspect], [Leave]\n")

            enter = input("What do you do?: ").strip().lower()

            if enter == "inspect":
                delete_title(50)
                print("You take a step closer, and look down\n")
                time.sleep(1.5)
                delete_title(50)
                print("Suddenly... You feel something push you from behind\n")
                time.sleep(1.5)
                print("You fall into the hole... It feels almost endless.\n")
                time.sleep(1.5)
                print("You pass out\n")
                time.sleep(3)
                delete_title(50)
                titledrop = [
                    "████████╗██╗  ██╗███████╗  ██╗  ██╗ ██████╗ ██╗     ███████╗",
                    "╚══██╔══╝██║  ██║██╔════╝  ██║  ██║██╔═══██╗██║     ██╔════",
                    "   ██║   ███████║█████╗    ███████║██║   ██║██║     █████╗ ",
                    "   ██║   ██╔══██║██╔══╝    ██╔══██║██║   ██║██║     ██╔══╝  ",
                    "   ██║   ██║  ██║███████╗  ██║  ██║╚██████╔╝███████╗███████╗",
                    "   ╚═╝   ╚═╝  ╚═╝╚══════╝  ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚══════╝\n",
                ]
                for line in titledrop:
                    print(line)
                    time.sleep(0.2)
                
                awake = [
                    "You wake up, your body hurts.\n",
                    "You try to look around but to no success, it's dark.\n",
                    "What do you do? [Get up (getup)], [Look around (look)]\n",
                ]
                for line in awake:
                    print(line)
                    time.sleep(3)

                wakechoice = input("Input:  ").strip().lower()

                if wakechoice == "getup":
                    getup = [
                        "You get up\n",
                        "Trying to look for anything that might help you find a way out\n",
                        "In a corner you find a damaged flashlight\n",
                    ]

                    for line in getup:
                        print(line)
                        time.sleep(3)

                elif wakechoice == "look":
                    look = [
                        "You decide to look around again\n",
                        "Still... trying to look around again, it's too dark to see\n",
                        "However despite your futile attempt at looking around\n",
                        "Your eye catches a glimps of something metallic in a corner.\n",
                        "You walk towards it to find a damaged flashlight\n",
                    ]
                    for line in look:
                        print(line)
                        time.sleep(3)
                    time.sleep
                    
                delete_title(50)
                flashlight = [
                    "As you pick up the flashlight, in hopes that it still works.\n",
                    "You try the power button.\n",
                    "To your surprise, the flashlight gives just enough light for you to see your surroundings\n",
                ]
                for line in flashlight:
                    print(line)
                    time.sleep(3)
                
                getlight = [
                    "You return to the place where you woke up\n",
                    "The light illuminates the path infront of you\n",
                    "All you see is a rocky wall\n",
                    "Where do you look [Right], [Left] or [Behind]?\n"
                ]
                for line in getlight:
                    print(line)
                    time.sleep(3)
                while True:
                    direction = input("Input direction: ")
                    
                    if direction == "behind":
                        lookbehind = [
                            "You look behind you, flashing the dim light at whatever may lay before you.\n",
                            "You see the faint trace of a door\n",
                            "You think... Should i open it? [Open], [Keep Looking (Looking)]\n"
                        ]
                        for line in lookbehind:
                            print(line)
                            time.sleep(3)
                        choicedoor = input("What do you do? ")

                        if choicedoor == "Open":
                            print("You move slowly towards the door, being suspicous of your surroundings")
                            delete_title(100)
                            break
                        elif choicedoor == "Looking":
                            print("You decide to keep looking.")
                            delete_title(100)
                        else:
                            print("Input invalid, try again")
                            delete_title(100)
                    elif direction == "right":
                        rightlook = [
                            "You decide to look to your right.",
                            "With the little light from your flashlight, you make out a torch hanging from the wall"
                            "Nothing much to see..."
                        ]
                        for line in rightlook:
                            print(line)
                            time.sleep(3)
                        delete_title(100)
                    elif direction == "left":
                        leftlook = [
                            "You look to your left..."
                            "It's just a wall..."
                        ]
                        for line in leftlook:
                            print(line)
                            time.sleep(3)
                        delete_title(100)
                    else:
                        print("Input invalid, try again")
                        delete_title(100)
                print("As you get closer to the door, you see...")
                time.sleep(3)
                delete_title(100)
                thedoor = [
                    "████████╗██╗  ██╗███████╗    ██████╗  ██████╗  ██████╗ ██████╗ ",
                    "╚══██╔══╝██║  ██║██╔════╝    ██╔══██╗██╔═══██╗██╔═══██╗██╔══██╗",
                    "   ██║   ███████║█████╗      ██║  ██║██║   ██║██║   ██║██████╔╝",
                    "   ██║   ██╔══██║██╔══╝      ██║  ██║██║   ██║██║   ██║██╔══██╗",
                    "   ██║   ██║  ██║███████╗    ██████╔╝╚██████╔╝╚██████╔╝██║  ██║",
                    "   ╚═╝   ╚═╝  ╚═╝╚══════╝    ╚═════╝  ╚═════╝  ╚═════╝ ╚═╝  ╚═╝",
                ]
                for line in thedoor:
                    print(line)
                    time.sleep(0.2)
                

                #While true here

            if enter == "leave":
                print("You decide to leave, not giving it another thought.")
                time.sleep(0.5)
                print("The End. (This is ending 1/2)\n")
                print("[Return]")

                ending1 = input("Input: ").strip().lower()

                if ending1 == "return":
                    print("returning...")
                    time.sleep(3)
                    delete_title(100)
                
                else:
                    delete_title(100)

        elif intro == "2":
            while True:
                    delete_title(30)
                    howplaytxt = [
                    "The game is simple, you are given choices and must respond with valid answers or commands.\n",
                    "Commands and prompts are often shown with the following\n",
                    "[1] [2] [3]... and so on         or          [Run] [Walk] [Look behind]... and so on\n",
                    "To return to the menu screen type [Return]\n",
                    ]
                    for line in howplaytxt:
                        print(line)
                        time.sleep(0.1)

                    retcom = input("").strip().lower()
                    if retcom == "return":
                        delete_title(8)
                        break
                    else:
                        print("Invalid command please try again.")
                        time.sleep(0.5)
                        delete_title(8)

        elif intro == "3":
            while True:
                delete_title(30)
                time.sleep(0.2)
                abttxt = [
                "We are two HTX students who like to explore and learn about systems, therefore we've created this game as our first text based video game\n",
                "Credits:\n",
                "Mitnavnstorm = Coder\n",
                "Culn = Coder and story director\n",
                "To return to the menu screen type [Return]\n",
                ]
                for line in abttxt:
                    print(line)
                    time.sleep(0.1)
                retcom2 = input("").strip().lower()
                if retcom2 == "return":
                    break
                else:
                    print("Invalid command please try again.")
                    delete_title(6)

        elif intro == "4":
            delete_title(30)
            print("Are you sure you want to quit? [Yes/No]")
            quitpromp = input("").strip().lower()
            if quitpromp == "yes":
                delete_title(14)
                break
            elif quitpromp == "no":
                 delete_title(14)
            else:
                print("Invalid input please try again")
                time.sleep(0.7)
                delete_title(14)
        else:
            print("Invalid Input please try again")
            time.sleep(2)
            delete_title(33)    