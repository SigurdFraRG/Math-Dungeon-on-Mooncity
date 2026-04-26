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
                time.sleep(10)
                awake = [
                    "You wake up, it's dark\n",
                    "You try to look around but to no success\n",
                    "What do you do? [Get up (getup)], [Look around (look)]\n",
                ]
                wakechoice = input("Input:  ").strip().lower()

                if wakechoice == "getup":
                    getup = [
                        "You get up\n",
                        "Looking for anything that might help you find a way out\n",
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
                        "Your eye catches a glimps of something.",
                        "You walk towards it to find a damaged flashlight",
                    ]
                    for line in look:
                        print(line)
                        time.sleep(3)

                    

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

            