from PyDictionary import PyDictionary #for dictionary
import pyttsx3
import speech_recognition as sr
import time

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


#dictionay created

def word_dict():
    speaking("Dictionary Activate...!")
    dictionary=PyDictionary()
    speaking("What is the problem sir...")
    p1=command()
    while True:
        if 'meaning' in p1:
            #replace extra speak word
            p1=p1.replace('what is the','')
            p1=p1.replace('of','')
            p1=p1.replace('jarvis','')
            p1=p1.replace('what is','')
            p1=p1.replace('meaning','')
            p1=p1.replace(' ','')
            ans=dictionary.meaning(p1) #get meaning
            speaking("Meaning is..")
            speaking(ans)
            time.sleep(2)
        elif 'synonym' in p1:
            #replace extra speak word
            p1=p1.replace('what is the','')
            p1=p1.replace('of','')
            p1=p1.replace('jarvis','')
            p1=p1.replace('what is','')
            p1=p1.replace(' ','')
            p1=p1.replace('synonym','')
            ans=dictionary.synonym(p1) #get snyonyms
            ans="synonym is.."+ans
            print(ans)
            speaking(ans)
            time.sleep(2)
        elif 'antonym' in p1:
            #replace extra speak word
            p1=p1.replace('what is the','')
            p1=p1.replace('of','')
            p1=p1.replace('jarvis','')
            p1=p1.replace('what is','')
            p1=p1.replace(' ','')
            p1=p1.replace('antonym','')
            ans=dictionary.antonym(p1) #get antonym
            ans="antonym is.."+ans
            print(ans)
            speaking(ans)
            time.sleep(2)
        speaking("What is your next problem sir...")
        take=command()
        li=['close dictionay','please of','leave from dictionay','out of dictionay']
        i=0
        f=0
        while(i<len(li)):
            if li[i] in take:
                f=1
                break
            i=i+1
        if(f==1):
            speaking("Ok sir.. dictionary close")
            break
        else:
            p1=command()


    









