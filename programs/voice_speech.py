import win32com.client as win
while True:
    b = input("(y) for enter , (0) for exit : ")
    
    if (b == 'y'):
        
        print("welcome!!!!\n")
        a = str(input("Enter the list values : "))
        a = a.split(",")
        print(a)
        c = input("what to say : ")
        spk = win.Dispatch("SAPI.SpVoice")
        for i in a:
            print(f"{c} "+i)
        for name in a:
            names = name.split()
            spe = f"{c} {names[0]}"
            spk.speak(spe)
    elif (b == '0'):
        break
    print("\ncongo for all the shoutout winners")
