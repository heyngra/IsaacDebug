#This program enables / disables Debug Console for The Binding of Isaac: Repentance.
#Windows and Linux (proton) Only!
import os
import sys
import getpass
if os.name == "nt":
    import msvcrt
    global windowspath
    windowspath = r"%s/Documents/My Games/Binding Of Isaac Repentance/options.ini" % os.environ['USERPROFILE']
else:
    global linuxpath
    linuxpath = r"/home/%s/.steam/steam/steamapps/compatdata/250900/pfx/dosdevices/c:/users/steamuser/Documents/My Games/Binding of Isaac Repentance/options.ini" % getpass.getuser()

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

clear()

def yes_no(answer):
    while True:
        choice = input(answer).lower()
        if "y" in choice and not "n" in choice:
           return True
        elif "n" in choice and not "y" in choice:
           return False

def loadData():
    global linuxpath
    global windowspath
    if os.name == "nt":
        try:
            f = open(windowspath, "r")
            options_read = f.readlines()
            f.close()
            for searchDebug in options_read:
                if "EnableDebugConsole=" in searchDebug:
                    if searchDebug == "EnableDebugConsole=1\n":
                        return True
                    else:
                        return False
        except Exception:
            raise FileNotFoundError("The options.ini file can't be found. If you want to report this issue, use this code: 5")
    else:
        try:
            f = open(linuxpath, "r")
            options_read = f.readlines()
            f.close()
            for searchDebug in options_read:
                if "EnableDebugConsole=" in searchDebug:
                    if searchDebug == "EnableDebugConsole=1\n":
                        return True
                    else:
                        return False
        except Exception:
            if FileNotFoundError():
                print("The options.ini file can't be found.")
                print("Set path: ", linuxpath)
                if yes_no("Do you want to enter your steam compatdata path manually? Y/n\n"):
                    path = input("Enter your steam compatdata path: ")
                    path2 = path + "250900/pfx/dosdevices/c:/users/steamuser/Documents/My Games/Binding of Isaac Repentance/options.ini"
                    linuxpath = r"%s" % path2
                    loadData()
                else:
                    sys.exit(1)


def debugConsole(enabled):
    if os.name == "nt":
        f = open(windowspath, "r")
    else:
        f = open(linuxpath, "r")
    options_read = f.readlines()
    f.close()
    if enabled == True:
        options_read = [temp.replace('EnableDebugConsole=1', 'EnableDebugConsole=0') for temp in options_read]
    if enabled == False:
        options_read = [temp.replace('EnableDebugConsole=0', 'EnableDebugConsole=1') for temp in options_read]
    if os.name == "nt":
        f = open(windowspath, "w")
    else:
        f = open(linuxpath, "w")
    f.writelines(options_read)
    f.close()
    main()

def main():
    x = loadData()
    clear()
    if x == True:
        print("If you want to disable debug console click Enter. Click any other button to close the app.")
    else:
        print("If you want to enable debug console click Enter. Click any other button to close the app.")
    if os.name == "nt":
        kinput = msvcrt.getch()
        if kinput == b'\r':
            debugConsole(x)
        else:
            sys.exit(1)
    else:
        kinput = input()
        if kinput == "":
            debugConsole(x)
        else:
            sys.exit(1)
if __name__ == '__main__':
    main()
