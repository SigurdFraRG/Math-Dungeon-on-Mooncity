import sys
import time

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
        print("                                                              --[Menu]--")
        time.sleep(0.1)
        print("                                                          ---START GAME[1]---")
        time.sleep(0.1)
        print("                                                          ---HOW TO PLAY[2]---")
        time.sleep(0.1)
        print("                                                            ---ABOUT US[3]---")
        time.sleep(0.1)
        print("                                                             ---QUIT[4]---")
    
        intro = input("Please enter a valid command: ").strip().lower()

        if intro == "1":
            print("")

        if intro == "2":
            while True:
                    delete_title(14)
                    print("The game is simple, you are given choices and must respond with valid answers or commands.")
                    time.sleep(0.1)
                    print("")
                    time.sleep(0.1)
                    print("Commands and prompts are often shown with the following")
                    print("")
                    time.sleep(0.1)
                    print("[1] [2] [3]... and so on         or          [Run] [Walk] [Look behind]... and so on")
                    print("")
                    time.sleep(0.1)
                    print("To return to the menu screen type [Return]")
                    time.sleep(0.1)
                    retcom = input("").strip().lower()
                    if retcom == "return":
                        delete_title(8)
                        break
                    else:
                        print("Invalid command please try again.")
                        time.sleep(0.5)
                        delete_title(8)

        if intro == "3":
            while True:
                delete_title(14)
                time.sleep(0.2)
                print("We are two HTX students who like to explore and learn about systems, therefore we've created this game as our first text based video game")
                print("")
                time.sleep(0.2)
                print("Credits:")
                print("")
                time.sleep(0.2)
                print("Mitnavnstorm = Coder")
                print("")
                time.sleep(0.2)
                print("Culn = Coder and story director")
                print("")
                time.sleep(0.2)
                print("To return to the menu screen type [Return]")
                retcom2 = input("").strip().lower()
                if retcom2 == "return":
                    break
                else:
                    print("Invalid command please try again.")
                    delete_title(6)

        if intro == "4":
            delete_title(14)
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

            