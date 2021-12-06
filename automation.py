import pyttsx3
import speech_recognition as sr
import keyboard #for keyboard access

assistant=pyttsx3.init("sapi5") #creation object for speak
voices=assistant.getProperty('voices') #check voices

assistant.setProperty('voice', voices[1].id) # 1 for female 0 for male
assistant.setProperty('rate',170)
def speaking(audio):
    assistant.say(audio) #say() method to speak 
    print("")
    assistant.runAndWait() #to run the speech we use runAndWait() All the say() texts won’t be said unless the interpreter encounters runAndWait().
    print("")

def command():  #Create command function
 
    #recognizer
    command=sr.Recognizer()

    #recognize from micrphone
    with sr.Microphone() as source:
        print("Listening.....!")
        command.pause_threshold=1 #Represents the minimum length of silence (in seconds) that will register as the end of a phrase. Can be changed
        audio=command.listen(source) 

        try:
            print("Recognizing....!")
            ## recognize speech using goggle
            query=command.recognize_google(audio,language='en-in')
            # print("You said =",query,type(query))

        except Exception as Error:
            return "None"

        return query.lower()

#short-cut trick of youtube keyboard press

def youtube_auto():
    speaking("What is your command sir...")
    while True:
        cm=command()
        if 'play' in cm:
            keyboard.press('space bar') 
        if 'puase' in cm:
            keyboard.press('space bar') 
        elif 'restart' in cm:
            keyboard.press('0')
        elif 'skip' in cm:
            keyboard.press('l')
        elif 'back' in cm:
            keyboard.press('j')
        elif 'out of full screen' in cm:
            keyboard.press('f')
        elif 'full screen' in cm:
            keyboard.press('f')
        elif 'out of film mode' in cm:
            keyboard.press('t')
        elif 'film mode' in cm:
            keyboard.press('t')
        elif 'unmute' in cm:
            keyboard.press('m')
        elif 'mute' in cm:
            keyboard.press('m')
        elif 'start the video' in cm:
            keyboard.press('k')
        elif 'half screen' in cm:
            keyboard.press('f')
        elif 'next video' in cm:
            keyboard.press('SHIFT+n')
        elif 'previous video' in cm:
            keyboard.press('SHIFT+p')
        elif 'decrease playback rate' in cm:
            keyboard.press('SHIFT+,')
        elif 'increase playback rate' in cm:
            keyboard.press('SHIFT+.')

        
        # speaking("What is your next command sir....")
        # cm=command()
        i=0
        f=0
        list=['off automation','stop automation','close automation','nothing','leave']
        while(i<len(list)):
            if list[i] in cm:
                speaking("Ok sir stop youtube automation")
                f=1
            i=i+1
               
        if(f):
            break

def chrome_auto():
    speaking("Chrome automation started....give me command sir!")
    while True:
        com=command()
        if 'close this tab' in com:
            keyboard.press_and_release('Ctrl + w')
        elif 'close the tab' in com:
            keyboard.press_and_release('Ctrl + w')
        elif 'close tab' in com:
            keyboard.press_and_release('Ctrl + w')
        elif 'close this window' in com:
            keyboard.press_and_release('Alt + F4')
        elif 'close the window' in com:
            keyboard.press_and_release('Alt + F4')
        elif 'close window' in com:
            keyboard.press_and_release('Alt + F4')
        elif 'new tab' in com:
            keyboard.press_and_release('Ctrl + t')
        elif 'new window' in com:
            keyboard.press_and_release('Ctrl + t')
        elif 'menu' in com:
            keyboard.press_and_release('Alt+F')
        elif 'incognito mode' in com:
            keyboard.press_and_release('Ctrl + Shift + n')
        elif 'next tab' in com:
            keyboard.press_and_release('Ctrl + PgDn')
        elif 'previous tab' in com:
            keyboard.press_and_release('Ctrl + PgUp')
        elif 'go to tab 1' in com:
            keyboard.press_and_release('Ctrl + 1')           
        elif 'rightmost tab' in com:
            keyboard.press_and_release('Ctrl + 9')
        elif 'minimize window' in com:
            keyboard.press_and_release('Alt + Space +n')
        elif 'maximize window' in com:
            keyboard.press_and_release('Alt + Space +x')
        elif 'print the page' in com:
            keyboard.press_and_release('Ctrl + p')
        elif 'reload the current page' in com:
            keyboard.press_and_release('F5')
        elif 'chrome history' in com:
            keyboard.press_and_release('Ctrl + h')
        elif 'top of the page' in com:
            keyboard.press_and_release('Home')
        elif'bottom of the page' in com:
            keyboard.press_and_release('End')
        elif 'show bookmark' in com:
            keyboard.press_and_release('Ctrl + Shift + o')
        elif 'open file' in com:
            keyboard.press_and_release('Ctrl + 0')
        elif 'pdf' in com:
            keyboard.press_and_release('Ctrl + p')
        
        i=0
        f=0
        list=['off automation','stop automation','close automation','nothing','leave']
        while(i<len(list)):
            if list[i] in com:
                speaking("Ok sir stop chrome automation")
                f=1
            i=i+1
               
        if(f):
            break
        

        
        
                
        

    
        
        



























