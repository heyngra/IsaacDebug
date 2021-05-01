#This program enables / disables Debug Console for The Binding of Isaac: Repentance.
#Windows Only!
import os
import msvcrt

def loadData():
    try:
        f = open(r"%s/Documents/My Games/Binding Of Isaac Repentance/options.ini" % os.environ['USERPROFILE'], "r")
        options_read = f.readlines()
        f.close()
        for searchDebug in options_read:
            if "EnableDebugConsole=" in searchDebug:
                if searchDebug == "EnableDebugConsole=1\n":
                    return True
                else:
                    return False
    except:
        raise FileNotFoundError("The options.ini file can't be found. Are you using Windows? If you want to report this issue, use this code: 5")
def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
def debugConsole(enabled):
    f = open(r"%s/Documents/My Games/Binding Of Isaac Repentance/options.ini" % os.environ['USERPROFILE'], "r")
    options_read = f.readlines()
    f.close()
    if enabled == True:
        options_read = [temp.replace('EnableDebugConsole=1', 'EnableDebugConsole=0') for temp in options_read]
    if enabled == False:
        options_read = [temp.replace('EnableDebugConsole=0', 'EnableDebugConsole=1') for temp in options_read]
    f = open(r"%s/Documents/My Games/Binding Of Isaac Repentance/options.ini" % os.environ['USERPROFILE'], "w")
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
    y = msvcrt.getch()
    if y == b'\r':
        debugConsole(x)
    else:
        exit()
if __name__ == '__main__':
    main()