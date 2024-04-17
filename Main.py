import os
import time

saveDataExists = os.path.exists(os.getcwd() + "\\savedata.txt")
if saveDataExists != True:
    print(f"saveDataExists: {str(saveDataExists)} : Creating New save data.")
    
    print("Make sure the Directory has a backslash at the end or the app won't detect it!.")
    dir = input("Enter the Ready or Not Directory Folder! >: ")
    if dir.find("\\steamapps\\common\\Ready Or Not\\") == -1 or os.path.exists(dir) != True:
        print("WARNING DIRECTORY DOESN'T EXISTS, EXITING.")
        time.sleep(2)
        quit()
    else:
        print("Directory exists saving...")
        with open('savedata.txt', 'a') as file:
            truename = "ReadyorNot_Dir: "+dir+"\n"
            file.write(truename)
        file.close()
    print("SaveData Has been created Continuing..")
    time.sleep(2)
else:
    #Continue / skip
    pass
#MAIN--
data =[]
print("Welcome to Ready or Not Mod Disabler")
while True:
    with open("savedata.txt", "r") as savedata:
        for i in savedata:
            data.append(i)
    
    SteamRoT = data[0].replace("ReadyorNot_Dir: ", "")
    #print("Directory to the game: " + SteamRoT)

    RoTmods = SteamRoT + "\\ReadyOrNot\\Content\\Paks\\mod.io\\3791\\mods"
    if not os.path.exists(RoTmods):
        print("cannot detect mod folder exiting.")
        time.sleep(2)
        break
    else:
        pass
    
    yes = ["y", "yes", "sure", "why not", "fine"]

    Enabled = True
    if len(os.listdir(RoTmods)) > 0:
        Enabled = True
        print("Mods Are Enabled\nWould you like to disable them? Y\\N")
        
    else:
        Enabled = False
        print("Mods Are Disabled\nWould you like to enable them? Y\\N")

    user = input("\nEnter a Command <: ")
    user = user.lower()
    print("You entered: "+user)
    
    #easter eggs
    if user == "fuck you":
        print("fuck me? ur the bitch who needs a script to disable mods you lazy bitch")
        time.sleep(2)
        os.system("cls")
    elif user == "why not":
        print("I'm gonna take that as a yes, next time you're gonna say yes or no, you lazy fuck. ")
        time.sleep(2)
        os.system("cls")
    else:
        pass

    if user == yes:
        if Enabled:
            print("You have disabled you mods.")
            Enabled = False
            time.sleep(2)
        else:
            print("You have Enabled you mods.")
            Enabled = True
            time.sleep(2)
    else:
        print("Canceled. Nothing has changed")
        time.sleep(2)

    os.system("cls")
