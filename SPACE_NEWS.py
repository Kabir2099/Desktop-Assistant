import pyttsx3
import speech_recognition as sr
from PIL import Image #for showing image
import os
import requests
from datetime import date
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


def nasa_news(query):
    if 'today' in query:
        new_date= date.today()
        
    else:
        speaking("write which date of nasa news you want to hear")
        new_date=input("write date : ")
        new_date=new_date.replace(":",'-')

    url=f'https://api.nasa.gov/planetary/apod?api_key=DJeRaviF9xpWSHOi4R6X3wRtla37jpEOiKG1NCMC'
    params={'date':str(new_date)}
    r=requests.get(url,params=params)
    data=r.json()
    #get information
    info=data['explanation']
    title=data['title']
    # print(info)
    # print(data)
    #image scrap
    imag_url=data['url']
    image_r=requests.get(imag_url)
    file_name='C:\\Users\\KABIR\\Pictures\\NASA_IMAGE\\'+str(new_date)+'.jpg'
    with open(file_name,'wb') as f:
        f.write(image_r.content)
    
    path1='C:\\Users\\KABIR\\Pictures\\NASA_IMAGE\\'+str(new_date)+'.jpg'
    # path2='C:\\Users\\KABIR\\Desktop\\JARVIS\\'+str(file_name)
    # os.rename(path1,path2)
    try:
        img=Image.open(path1)
        img.show()
    except:
        pass

    

    speaking(f'title is {title}')
    speaking(f"according to nasa{info}")




















