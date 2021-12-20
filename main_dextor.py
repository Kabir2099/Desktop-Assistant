import pyttsx3 #for speak
import speech_recognition as sr #for listening
import datetime #for time
import webbrowser  #for open browser
import pywhatkit # for google searching
import random #for generate random integer
import os #opearting system module
import wikipedia #for wikipidia searching
import pyautogui #for screenshot
import keyboard #for keyboard press
import pyjokes #for jokes
import time #for time
from playsound import playsound #for play anything
from tkinter import Label,Entry,Button,Tk,StringVar #for gui
from pytube import YouTube #for you tube video download
import requests #for request data from webpage
import json #for convert dictionary
import speedtest #for internet speed
from pywikihow import search_wikihow #for anything how to search
import psutil #for battery percentage
import cv2 #for webcam
from bs4 import BeautifulSoup


from SPACE_NEWS import nasa_news
from nick import nick_name #for nickname its my own module
from send_massage import sending_massage #own module for sending massage
from addcontact import add_Contact#own module for add contact
from applicatio import openApps #own module for open application
from automation import chrome_auto, youtube_auto #own module for automation
from myword import word_dict #own module for dictionary
from Book_Reader import reader #own module for audiobook read
from lang_translate import my_trans #own module for translate


assistant=pyttsx3.init("sapi5") #creation object for speak
voices=assistant.getProperty('voices') #check voices
# print(voices)
assistant.setProperty('voice', voices[1].id) # 1 for female 0 for male

rate=assistant.getProperty('rate')
assistant.setProperty('rate',170) #rate of voices

#speak function for speaking
def speak(audio):
    assistant.say(audio) #say() method to speak 
    print("")
    assistant.runAndWait() #to run the speech we use runAndWait() All the say() texts won’t be said unless the interpreter encounters runAndWait().
    print("")

#craete wish function
def wishme():
    hour = int(datetime.datetime.now().hour)
    if(hour>4 and hour<12):
        speak("Good Morning")
    elif(hour>=12 and hour<18):
        speak("Good Afternoon")
    
    elif(hour>=18 and hour<=23):
        speak("Good Evening")
    else:
        speak('hey it is night time...greetings of the day')
    # speak("I am your desktop assistant Jarvis.. How can i help you")
    f=open("naming.text") #read the name
    name=f.read()
    f.close()
    data="I am"+name+"your desktop assistant...How can i help you"
    speak(data)

def takecommand():  #Create command function
 
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

#searching function to serach youtube,goggle
def search(query):
    #youtube search  
    
    if 'youtube' in query:
       speak("Ok sir,this is what i found for your serach")
       query=query.replace('jarvis',"")
       query=query.replace('youtube search',"")
       wb="https://www.youtube.com/results?search_query="+query
       webbrowser.open(wb)
         
    #google search  
    elif 'google' in query:
        speak("Ok sir,this is what i found for your serach")
        query=query.replace('jarvis',"")
        query=query.replace('google search',"")
        que=query
        pywhatkit.search(query)
        try:
            wiki=wikipedia.summary(que,5) #get wikipedia info : 5-> no .of lines
            speak(wiki) #speak
        except:
            pass
    
    #if user tell search then wikipedia
    elif 'wikipedia' in query:
        speak("searching wikipedia.....!")
        query=query.replace("jarvis","") #my extra talking
        query=query.replace("in",'')
        query=query.replace('search','')
        query=query.replace('searching','')
        que=query.replace("wikipedia","") #for searching speaking
        query=que
        query=query.replace(" ","_") #for open wikipedia webpage
        try:
            query="https://en.wikipedia.org/wiki/"+query #open wikipedia
            webbrowser.open(query) #open
            wiki=wikipedia.summary(que,5) #get wikipedia info : 5-> no .of lines
            speak("According to the wikipedia...!")
            speak(wiki) #speak
        except:
            speak("Not match anything in wikipedia... can i searh in google")
            take=takecommand()
            if 'no' in query:
                speak("Ok sir.. you can ask anything")
            else:
                speak("Ok sir,this is what i found for your serach")
                pywhatkit.search(que)

        
    speak("Done sir !")

#for wikipedia seaching
def wikipedia_Search(query):
    speak("searching wikipedia.....!")
    query=query.replace("jarvis","") #my extra talking
    query=query.replace("in",'')
    query=query.replace('search','')
    query=query.replace('searching','')
    que=query.replace("wikipedia","") #for searching speaking

    query=que
    query=query.replace(" ","_") #for open wikipedia webpage
    #try except use for if not found in wikipeia and handle the error
    try:
        query="https://en.wikipedia.org/wiki/"+query #open wikipedia
        webbrowser.open(query) #open
        wiki=wikipedia.summary(que,5) #get wikipedia info : 5-> no .of lines
        speak("According to the wikipedia...!")
        speak(wiki) #speak
    except:
        speak("Not match anything in wikipedia... can i searh in google")
        take=takecommand()
        if 'no' in query:
            speak("Ok sir.. you can ask anything")
        else:
            speak("Ok sir,this is what i found for your serach")
            pywhatkit.search(que)

#websites open    
def web_open(query):
    speak("Ok sir,Launching....")
    query=query.replace("jarvis","")
    query=query.replace("website","")
    web1=query.replace("open","")
    web1=web1.replace(" ","")
    # web1=input("enter : ")
    web2="https://www."+web1+".com"
    webbrowser.open(web2)
    speak("Launched ..!")

#for play msuic
def play_music():
    #giving choice to jarvis
    speak("can you give me choice for play music..!")
    choice=takecommand() #take choice
    if 'yes' in choice: #if give permission 
        speak("Thank you sir for giving me choice")
        music_dir='C:\\Users\\KABIR\Desktop\\My Song' #get directory
        songs=os.listdir(music_dir) #list all of the song with .mp3
        print(songs)
        r=random.randint(0,len(songs)-1) #random integer for playing random song
        os.startfile(os.path.join(music_dir,songs[r])) #play song
    #if i want to tell the song name
    else:
        speak("Ok sir.. tell me name of the song")
        musicname=takecommand()
        #my music location
        music_dir='C:\\Users\\KABIR\Desktop\\My Song'
        songs=os.listdir(music_dir)
        music_mp3=musicname+'.mp3' #for searching in the list

        if music_mp3 in songs: # if song is found in my folder
            file=music_dir+'\\'+music_mp3
            os.startfile(file) #play

        #if not found then start in youtube
        else:
            pywhatkit.playonyt(musicname)     
    
    speak("Song started.. enjoy it sir")

#taking screenshot
def screen_shot():
    #take file name
    speak("Ok sir, what i should give name of the file")
    file_name=takecommand()
    #add file extenson
    file_name=file_name+".png"
    path="C:\\Users\\KABIR\\Pictures\\Screenshots\\"+file_name #save location
    kk=pyautogui.screenshot() #take screenshot
    kk.save(path) #save into directery
    os.startfile(path) #open file
    speak("Here is your screenshot")

#close any application
def close_Application(query):
    speak("Ok sir.. wait a second")
    query=query.replace("close","")
    query=query.replace(" ","")
    #for close: 'TASKKILL /F /im' +name app +'.exe' ans use os.system
    if 'youtube' in query:
        path='TASKKILL /F /im'+' msedge.exe' 
        os.system(path)
    elif 'google maps' in query:
        path='TASKKILL /F /im'+' msedge.exe'
        os.system(path)
    elif 'whatsapp' in query:
        path='TASKKILL /F /im'+' msedge.exe'
        os.system(path)
    elif 'google' in query:
        path='TASKKILL /F /im'+' msedge.exe'
        os.system(path)
    elif 'telegram' in query:
        path='TASKKILL /F /im'+' msedge.exe'
        os.system(path)
    elif 'chrome' in query:
        path='TASKKILL /F /im'+' msedge.exe'
        os.system(path)
    else:
        path='TASKKILL /F /im'+query+'.exe'
        os.system(path)

    speak("Sucessfully close")

#jokes
def joke_speak():
    get=pyjokes.get_joke(language='en',category='all')
    speak(get)
    speak("How was the joke...?")
    li=['worst','ghatia','bekar','not good','bad','not good','average','not upto the standard']
    choice=takecommand()
    i=0
    f=0
    while(i<len(li)):
        if li[i] in choice:
            f=1
        i=i+1
    if(f==1):
        speak("sorry sir can i try a new joke")
        ch=takecommand()
        li_ch=['no','stop','leave','enough','no more','not required']
        i=0
        f=0
        while(i<len(li_ch)):
            if li_ch[i] in ch:
                f=1
            i=i+1
        if(f==1):
            speak('ok sir...Next time i can try to talk a better jokes')
        else:
            speak("Thanks sir for giving me one more choice...here is a new joke for you sir")
            joke_speak()
    else:
        speak("glad that you liked the joke...! do you want to hear more joke")
        ch=takecommand()
        li_ch=['no','stop','leave','enough','no thank you','no more']
        i=0
        f=0
        while(i<len(li_ch)):
            if li_ch[i] in ch:
                f=1
            i=i+1
        if(f==1):
            speak('ok sir.')
        else:
            speak("here is a next joke for you sir")
            joke_speak()

#repaet my word
def repeat_word():
    speak('Ok sir...tell the words')
    while True:
        word=takecommand()
        li_stop=['stop no more','stop please','please no more','no more','end please']
        i=0
        f=0
        while(i<len(li_stop)):
            if li_stop[i] in word:
                f=1
                break
            i=i+1
        if(f==1):
            speak("Ok cool sir...now stop the repeatition mode..")
            break
        speak(word)

#for alarm set to voice .. if we want then we can use it
def set_alarm():
    speak("sir..please tell me the time to set alarm,for example set alarm to 5:30 am")
    tt=takecommand()
    tt=tt.replace("set alarm to ","")
    tt=tt.replace('.','')
    tt.upper()
    altime=str(datetime.datetime.now().strptime(tt,"%I:%M %p"))
    # print(altime)
    altime=altime[11:-3]
    horeal=altime[:2]
    horeal=int(horeal)
    mireal=altime[3:5]
    mireal=int(mireal)
    speak(f"done,alarm is set for {tt}")

    while True:
        if horeal==datetime.datetime.now().hour:
            if mireal==datetime.datetime.now().minute:
                speak("time to wake up sir")
                playsound('audio.mp3')
                speak('alarm closed')
            elif mireal<datetime.datetime.now().hour:
                break  
    # speak("ok sir...enter time..")
    # t=input("Enter time : ")
    # speak("Alarm set successfully...")
    # while True:
    #     now_time=datetime.datetime.now()
    #     ti=now_time.strftime("%H:%M:%S")
    #     if(ti==t):
    #         speak("Sir time to wake up..")
    #         # music_dir='C:\\Users\\KABIR\Desktop\\ringtone'
    #         # songs=os.listdir(music_dir)
    #         # r=random.randint(0,len(songs)-1)
    #         # playsound(songs[r])
    #         playsound('audio.mp3')
    #         speak("Alarm closed")
    #     elif(ti>t):
    #         break

#you tube video download
def yt_download():
    root=Tk()
    root.geometry('500x300')
    root.resizable(0,0)
    root.title("Youtube Video Downloader")
    Label(root,text='Youtube Video Downloader',font='arial 15 bold').pack()
    speak("Sir...Enter the Video link")
    link=StringVar()
    Label(root,text="Paste Link Here",font='arial 15 bold').place(x=160,y=60)
    Entry(root,width=70,textvariable=link).place(x=32,y=90)

    def videoDownloader():
        url=YouTube(str(link.get()))
        video=url.streams.first()
        video.download('C:\\Users\\KABIR\\Desktop\\My Video')
        Label(root,text='Downloaded',font='arial 15 bold').place(x=180,y=210)
    
    Button(root,text='Download',font='arial 15 bold',bg='pale violet red',padx=2,command=videoDownloader).place(x=180,y=150)
    root.mainloop()
    speak("Video Download successfully")
    os.startfile("C:\\Users\\KABIR\\Desktop\\My Video")
    speak("Here is your video")

#Temperature of any city but we dont use
def temp_Search(srch):
    #extra word remove
    srch=srch.replace("jarvis",'')
    srch=srch.replace("temperature","")
    srch=srch.replace('in','')
    srch=srch.replace("of",'')
    srch=srch.replace("tell me","")
    #weather api
    url='http://api.openweathermap.org/data/2.5/weather?q=+'+srch+'&appid=067fda8d35b3c88f50a2be0f2945f1f5'
    data=requests.get(url).text #get all the information as string
    data=json.loads(data) #convert string into dict
    # print(data)
    if(data['cod']==404): #if city name not valid
        speak("invalid city name..Please check your city name sir..")
    else:
        temp_City=data['main']['temp']-273.15 #get temperature in k ...so -273.15
        temp_City=round(temp_City,2) #round figure
        temp=str(temp_City) 
        tell="Temperature of"+srch+"is"+temp+"degree celcius"
        speak(tell) #speak 

#weather information
def weather_news(srch):
    #extra word remove
    srch=srch.replace("jarvis",'')
    srch=srch.replace("weather","")
    srch=srch.replace("of",'')
    srch=srch.replace('news','')
    srch=srch.replace('report','')
    srch=srch.replace("tell me","")
    srch=srch.replace("information",'')
    #weather api
    url='http://api.openweathermap.org/data/2.5/weather?q=+'+srch+'&appid=067fda8d35b3c88f50a2be0f2945f1f5'
    data=requests.get(url).text #get all the information as string
    data=json.loads(data) #convert string into dict
    # print(data)
    if(data['cod']==404): #if city name not valid
        speak("invalid city name..Please check your city name sir..")
    else:
        #get all the information
        temp_City=data['main']['temp']-273.15 #get temperature in k ...so -273.15
        temp_City=round(temp_City,2) #round figure
        temp=str(temp_City)
        weather_des=data["weather"][0]["description"] 
        hmdt=data['main']['humidity']
        speed_air=data["wind"]["speed"]
        #for better broadcast
        weather_tell="Current weather is"+weather_des
        hmdt_tell="Current humidity is"+str(hmdt)+"percentage"
        speed_tell="Current air speed is "+str(speed_air)+"kilometers per hour"
        tell="Current Temperature is"+temp+"degree celcius"
        report="weather report of "+srch+"is broadcast ...listen carefully"
        #speak all the information
        speak(report)
        speak(weather_tell)
        speak(tell)
        speak(hmdt_tell)
        speak(speed_tell)

#speed test
def speed_Test(s):
    speak("checking speed.....please wait a minute sir..")
    speed=speedtest.Speedtest() #just use short name of function
    download=speed.download() #get downloading speed
    coreect_dwld=int(download/800000) #convert into mbps
    Upload=speed.upload() #get uploading speed
    correct_upload=int(Upload/800000) #convert into mbps
    if 'download' in s:
        speak(f"downloading speed is {coreect_dwld} mbp s")
    elif 'uploading' in s:
        speak(f"uploading speed is {correct_upload}  mbp s")
    else:
        speak(f"downloading speed is {coreect_dwld}  mbp s")
        speak(f"uploading speed is {correct_upload}  mbp s")

#how to search
def how_serach(query):
    #replace extra things
    query=query.replace("jarvis","")
    query=query.replace("tell me","")
    query=query.replace("about",'')
    try:
        max_result=1
        how_to=search_wikihow(query,max_result) #get results
        assert len(how_to)==1 #assertion
        # print(type(how_to))
        how_to[0].print() #print result
        speak(how_to[0].summary) #speak
    except:
        speak("sorry sir.. i am not able to find this")

#get temperature
def temp_outside(srch):
    # srch= "temperature in newtown"
    srch=srch.replace("today",'')
    srch=srch.replace("today's",'')
    url = f"https://www.google.com/search?q={srch}"
    r = requests.get(url)
    data = BeautifulSoup(r.text,"html.parser")
    temperature = data.find("div", class_ ="BNeawe").text
    print(temperature)
    speak("temperature is : "+temperature)
#get any movie link
def movie_open(m):
    speak("Ok sir...movie link opening")
    m=m.replace("jarvis",'')
    m=m.replace("open","")
    m=m.replace('movie',"")
    m=m.replace('link',"")
    s=m
    m=m.split(" ")
    if(len(m)>1):
        s='+'.join(m)
    link="https://moviesverse.co/?s="+s #movie verse link open
    webbrowser.open(link)
    speak("link open...now you can download movie from here")

#any thing Show to searching
def howTo_mode():
    speak("How to do mode is activated")
    speak("please tell me what you want to know")
    while True:
        how=takecommand() #get whivh you want to search
        try:
            max_result=1
            how_to=search_wikihow(how,max_result) #get  search ressult
            assert len(how_to)==1 #assertion
            # print(type(how_to))
            how_to[0].print() #print result
            speak(how_to[0].summary) #speak the result
        except: #if not find anything
           speak("sorry sir.. i am not able to find this")
        
        #for next time
        speak('are you want to know more things')
        ch=takecommand()
        if 'yes' in ch:
            speak("tell me what you want to know")
        else:
            speak("How to do mode closed")
            break

#battery_charge
def battery_charge():
    battery=psutil.sensors_battery() #get charge
    percatge=battery.percent #convert into percente
    speak(f"our system have {percatge} percent battery")

    if  percatge>=75:
        speak("We have enough power to continue our work")
    elif percatge>=50:
        speak("We can work..but after some time need charge our battery")
    elif percatge>=40:
        speak("we should connect our system to charging point to charge our battery")
    elif percatge>=20:
        speak("We don't have enough power to work,please connect to charging")
    else:
        speak("we have very low battery...please connect to charging the system will shutdown very soon")


#taskexecution
def task():
    speak("hello sir..i am jarvis ..your desktop assistant")
    speak("How may i help you?")
    al_s="none" #for alarm
    #for one time checking
    battery_choice1=True
    battery_choice2=True

    while True:
        battery=psutil.sensors_battery()
        percentage=battery.percent

        if (percentage<=30 and battery_choice1 and percentage>20):
            speak(f"our system have {percentage} percent battery")
            speak("sir..We don't have enough power to work,please connect to charging")
            battery_choice1=False
        if(percentage<=20 and battery_choice2):
            speak(f"our system have {percentage} percent battery")
            speak("sir...we have very low battery...please connect to charging the system will shutdown very soon")
            battery_choice2=False
        query=takecommand()
        if 'dictionary' in query:
            word_dict()
        elif 'translator' in query:
            my_trans()
        elif 'temperature' in query:
            temp_outside(query)
        elif 'what is the time' in query:
            time=datetime.datetime.now().strftime("%H:%M:%S")
            speak(time)
        elif 'avi time' in query:
            time=datetime.datetime.now().strftime("%H:%M:%S")
            speak(time)
        elif 'jarvis time keya hai' in query:
            time=datetime.datetime.now().strftime("%H:%M:%S")
            speak(time)
        elif 'tell time' in query:
            time=datetime.datetime.now().strftime("%H:%M:%S")
            speak(time)  
        elif 'book read' in query:
            reader(query)
        elif 'how to do mode' in query:
            howTo_mode()
        elif 'movie link' in query:
            movie_open(query)
        elif 'audiobook' in query:
            reader(query)
        elif 'video download' in query:
            yt_download()
        elif 'weather' in query:
            weather_news(query)
        elif 'alarm' in query:
            # set_alarm()
            speak("ok sir...enter time..")
            al_s=input("Enter time : ")
            speak("Alarm set successfully...")
        elif 'volume mute' in query:
            pyautogui.press('volumemute')
        elif 'search' in query:
            search(query)
        elif 'joke' in query:
            speak("Listen carefully the joke...!")
            joke_speak()
        elif 'jokes' in query:
            speak("Listen carefully the joke...!")
            joke_speak()
        elif 'my location' in query:
            speak("ok sir...wait a second")
            webbrowser.open('https://www.google.com/maps/place/V+I+P+Guest+House/@22.5687639,88.4861334,18.25z/data=!4m8!3m7!1s0x3a020ad7a5dededd:0x1347c2ae8264d8fb!5m2!4m1!1i2!8m2!3d22.5677027!4d88.487095?hl=fr')
            speak("It is your location sir..!")
        elif 'open my location' in query:
            speak("ok sir...wait a second")
            webbrowser.open('https://www.google.com/maps/place/V+I+P+Guest+House/@22.5687639,88.4861334,18.25z/data=!4m8!3m7!1s0x3a020ad7a5dededd:0x1347c2ae8264d8fb!5m2!4m1!1i2!8m2!3d22.5677027!4d88.487095?hl=fr')
            speak("It is your location sir..!")
        elif 'location' in query:
            speak("ok sir...wait a second")
            webbrowser.open('https://www.google.com/maps/place/V+I+P+Guest+House/@22.5687639,88.4861334,18.25z/data=!4m8!3m7!1s0x3a020ad7a5dededd:0x1347c2ae8264d8fb!5m2!4m1!1i2!8m2!3d22.5677027!4d88.487095?hl=fr')
            speak("It is your location sir..!")
        elif 'hello' in query:
            speak("Hello Sir..!")
            wishme() #wish function calling
        elif 'how are you' in query:
            speak("I am fine Sir")
            speak("What about you")
        elif 'you need a break' in query:
            speak("Ok sir,You call me anytime")
            speak("just speak jarvis wake up")
            break
        elif 'keya haal hai' in query:
            speak("Main to bohut bodia hu bhai")
        elif 'bye' in query:
            speak("Ok sir,bye")
            break
        elif 'i am also fine' in query:
            speak('Good sir')
        elif 'what are you doing' in query:
            speak('Nothing sir ,, waiting for your command')   
        elif 'search' in query:
            search(query)
        elif 'website' in query:
            web_open(query)
        elif 'music' in query:
            play_music()     
        elif 'wikipedia' in query:
            wikipedia_Search(query)
        elif 'nickname' in query:
            name=nick_name()
        elif 'send' in query:
            sending_massage(query)
        elif 'contact' in query:
            add_Contact()
        elif 'screenshot' in query:
            screen_shot() 
        elif 'youtube automation' in query:
            youtube_auto()
        #short-cut trick of youtube keyboard press
        elif 'play the video' in query:
            keyboard.press('space bar') 
        elif 'puase the video' in query:
            keyboard.press('space bar') 
        elif 'restart video' in query:
            keyboard.press('0')
        elif 'skip' in query:
            keyboard.press('l')
        elif 'back' in query:
            keyboard.press('j')
        elif 'out of full screen' in query:
            keyboard.press('f')
        elif 'full screen' in query:
            keyboard.press('f')
        elif 'out of film mode' in query:
            keyboard.press('t')
        elif 'film mode on' in query:
            keyboard.press('t')
        elif 'unmute' in query:
            keyboard.press('m')
        elif 'mute' in query:
            keyboard.press('m')
        elif 'start the video' in query:
            keyboard.press('k')
        elif 'half screen' in query:
            keyboard.press('f')
        elif 'next video' in query:
            keyboard.press('SHIFT+n')
        elif 'previous video' in query:
            keyboard.press('SHIFT+p')
        elif 'decrease playback rate' in query:
            keyboard.press('SHIFT+,')
        elif 'increase playback rate' in query:
            keyboard.press('SHIFT+.')
        elif 'chrome automation' in query:
            chrome_auto()
        #short-cut trick of youtube keyboard press
        elif 'close this tab' in query:
            keyboard.press_and_release('Ctrl + w')
        elif 'close the tab' in query:
            keyboard.press_and_release('Ctrl + w')
        elif 'close tab' in query:
            keyboard.press_and_release('Ctrl + w')
        elif 'close this window' in query:
            keyboard.press_and_release('Alt + F4')
        elif 'close the window' in query:
            keyboard.press_and_release('Alt + F4')
        elif 'close window' in query:
            keyboard.press_and_release('Alt + F4')
        elif 'new tab' in query:
            keyboard.press_and_release('Ctrl + t')
        elif 'new window' in query:
            keyboard.press_and_release('Ctrl + t')
        elif 'menu' in query:
            keyboard.press_and_release('Alt+F')
        elif 'incognito mode' in query:
            keyboard.press_and_release('Ctrl + Shift + n')
        elif 'next tab' in query:
            keyboard.press_and_release('Ctrl + PgDn')
        elif 'previous tab' in query:
            keyboard.press_and_release('Ctrl + PgUp')
        elif 'tab 1' in query:
            keyboard.press_and_release('Ctrl + 1')
        elif 'tab 2' in query:
            keyboard.press_and_release('Ctrl + 2')
        elif 'tab 3' in query:
            keyboard.press_and_release('Ctrl + 3')
        elif 'tab 4' in query:
            keyboard.press_and_release('Ctrl + 4')
        elif 'tab 5' in query:
            keyboard.press_and_release('Ctrl + 5')
        elif 'tab 6' in query:
            keyboard.press_and_release('Ctrl + 6')
        elif 'tab 7' in query:
            keyboard.press_and_release('Ctrl + 7')          
        elif 'right most tab' in query:
            keyboard.press_and_release('Ctrl + 9')
        elif 'minimize window' in query:
            keyboard.press_and_release('Alt + Space +n')
        elif 'maximize window' in query:
            keyboard.press_and_release('Alt + Space +x')
        elif 'print the page' in query:
            keyboard.press_and_release('Ctrl + p')
        elif 'pdf' in query:
            keyboard.press_and_release('Ctrl + p')
        elif 'reload' in query:
            keyboard.press_and_release('F5')
        elif 'chrome history' in query:
            keyboard.press_and_release('Ctrl + h')
        elif 'top of the page' in query:
            keyboard.press_and_release('Home')
        elif'bottom of the page' in query:
            keyboard.press_and_release('End')
        elif 'show bookmark' in query:
            keyboard.press_and_release('Ctrl + Shift + o')
        elif 'open file' in query:
            keyboard.press_and_release('Ctrl + 0')
        elif 'open' in query:
            speak("Ok sir.wait a second")
            openApps(query)
            speak("Your command sucessfully executed")           
        elif 'repeat my word' in query:
            repeat_word()
        elif 'repeat word' in query:
            repeat_word()
        elif 'close' in query:
            close_Application(query)   
        elif 'remember that' in query:
            remsg=query.replace("remember that",'')
            remsg=remsg.replace('Jarvis',"")
            msg="you tell me remind that "+remsg
            speak(msg)
            f=open("Remember.text",mode='w')
            f.write(remsg)
            f.close()
        elif 'what do you remember' in query:
            f=open("Remember.text",mode='r')
            data=f.read()
            f.close()
            msg="you tell me remember that "+data
            speak(msg)
        elif 'download speed' in query:
            speed_Test(query)
        elif 'upload speed' in query:
            speed_Test(query)
        elif 'internet speed' in query:
            speed_Test(query)
        elif 'how to' in query:
            how_serach(query)
        elif 'battery' in query:
            battery_charge()
        elif 'how much power left' in query:
            battery_charge()
        elif 'how much power we have' in query:
            battery_charge()
        elif 'webcam' in query:
            cap=cv2.VideoCapture(0)
            while True:
               ret,img=cap.read()
               cv2.imshow('webcam',img)
               k=cv2.waitKey(50)
               if k==27:
                  break
            cap.release()
            cv2.destroyAllWindows()   
        elif 'volume up' in query:
            pyautogui.press('volumeup')
        elif 'volume down' in query:
            pyautogui.press('volumedown')
        elif 'nasa news' in query:
            nasa_news(query)
        
        #this is for also set alarm
        if al_s not in 'none':
            now_time=datetime.datetime.now()
            ti=now_time.strftime("%H:%M:%S")
            if(ti>=al_s):
               speak("Sir time to wake up..")
               playsound('audio.mp3')
               speak("Alarm closed")
               al_s='none'

# task() #calling task

#wake-up
while True:
    permsn=takecommand()
    if 'wake up' in permsn:
        task()
   







