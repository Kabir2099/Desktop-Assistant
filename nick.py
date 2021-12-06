import pyttsx3
import speech_recognition as sr


assistant=pyttsx3.init("sapi5") #creation object for speak
voices=assistant.getProperty('voices') #check voices

assistant.setProperty('voice', voices[0].id) # 1 for female 0 for male
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

def nick_name():
    f=open("naming.text",mode='w')
    speaking("Sir tell the nickename which you want to give")
    take=command()
    f.write(take)
    f.close
    return take


    










