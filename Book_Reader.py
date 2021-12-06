
import pyttsx3
import speech_recognition as sr
import PyPDF2
from gtts import gTTS
from googletrans import Translator
from playsound import playsound
import os

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

def reader(query):
    speaking("Tell me name of the book")
    name=input("enter book name :")
    Book_dir='C:\\Users\\KABIR\Desktop\\Book' #get directory
    Books=os.listdir(Book_dir) #list all of the book
    name=name+'.pdf'
    if name in Books:
        path='C:\\Users\\KABIR\Desktop\\Book\\'+name
        os.startfile(path)
        book=open(path,'rb')
        pdfreader=PyPDF2.PdfFileReader(book)
        pages=pdfreader.getNumPages()
        speaking(f"Number of pages in this book are {pages}")
        speaking("Enter from which page i have to start reading")
        numpage=int(input("Enter start page : "))
        page=pdfreader.getPage(numpage)
        text=page.extractText()
        speaking("Tell me which language, i have to read")
        lang=command()

        dict_lang={'marathi':'mr','bihari':'bh','italian':'it','korean':'ko','swedish':'sw','malayalam':'ml','latin':'la','urdu':'ur','armenian':'hy','english':'en','hindi':'hi','bengali':'bn','arabic':'ar','tamli':'ta','spanish':'es','french':'fr','chinese':'zh-cn'}
       
        if lang in dict_lang:
           transl=Translator()
           language=dict_lang[lang]
           textlang=transl.translate(text,dest=language).text
           textm=textlang
           speech=gTTS(text=textm)
           try:
               speech.save("book.mp3")
               playsound("book.mp3")
           except:
               playsound("book.mp3")
        else:
            speaking(text)

    else:
        speaking("No book found in your directory")
















