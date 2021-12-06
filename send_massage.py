from os import read
import webbrowser
import keyboard
import time
from addcontact import add_Contact #our module
import pyttsx3
import pywhatkit
import speech_recognition as sr
import smtplib #for mail send

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

#sending massage
def sending_massage(query):

    #searching contact existing
    def seraching(data,namePerson):
        i=0
        while(i<len(data)):
            if (namePerson==data[i]):
                return i
            i=i+1
        return -1 #if not found
    
    #for whatsapp
    if 'whatsapp' in query:
        speaking("Sir..tell me name....")
        namePerson=command() #take name
        if 'main study' in namePerson:
            speaking("Tell me the message ...!")#take whatsapp massage
            #take timing for the massage
            msg=command()
            path='https://web.whatsapp.com/accept?code=DxnuLnqj8e62d2x921jzKx'
            webbrowser.open(path)
            time.sleep(20)
            keyboard.write(msg)
            time.sleep(1)
            keyboard.press('enter')
            speaking("ok,sir,sending whatsapp massage")
        elif 'unknown' in namePerson: #for unknown
            speaking("write the number sir..!")
            no=input("Enter number:") #take number
            no="+91"+no #+91 for india
            speaking("Tell me the message ...!")
            msg=command() #take whatsapp massage
            #take timing for the massage
            speaking("write the time")
            speaking("Time in hour")
            hr=int(input("Write : "))
            speaking("Time in minutes")
            mn=int(input("Write : "))
            pywhatkit.sendwhatmsg(no,msg,hr,mn,20) #send whatsapp massage
            speaking("whatsapp message sent")
            keyboard.press('enter')

            
        else :
            #Open file of contact name
            f=open("contactname.text")
            data=f.read() #get all the contact
            data=data.split(',') #convert into list
            f.close()
            idx=seraching(data,namePerson) #calling search

            if(idx!=-1): #contact is found
                #open mobile number file
                f=open("mobileno.text")
                number=f.read()#get all the number
                number=number.split(",") #convert into list
                no=number[idx] #get exactly number
                no="+91"+no
                speaking("Tell me the message ...!")#take whatsapp massage
                #take timing for the massage
                msg=command()
                speaking("write the time")
                speaking("Time in hour")
                hr=int(input("Write : "))
                speaking("Time in minutes")
                mn=int(input("Write : "))
                pywhatkit.sendwhatmsg(no,msg,hr,mn,20) #send the massage
                # keyboard.press('enter')
                speaking("whatsapp message sent")
                keyboard.press('enter')
                

            else: #if name not found
                speaking("Sir name is not found..")
                speaking("Sir..do you want to add the name  in the contact...!")
                choice=command() #if gives for add contact
                if 'no' in choice:
                    speaking("Ok sir fine")
                else:
                    add_Contact() #add new contact

    if 'mail' in query:
        speaking("Sir..tell me name....")
        namePerson=command() #take name

        if 'unknown' in namePerson:
            speaking("sir please write the mail")
            to=input("write the mail :")
            speaking("tell me the message")
            content=command()
            server=smtplib.SMTP('smtp.gmail.com' , 587)
            # server.ehlo()
            server.starttls()
            f=open('password.text',)
            pass_word=f.read()
            server.login('kabirsk58694@gmail.com',pass_word)
            server.sendmail('kabirsk58694@gmail.com',to,content)
            server.quit()
        
        else:
            #Open file of email contact name
            f=open("emailcontact.text")
            data=f.read() #get all the contact
            data=data.split(',') #convert into list
            f.close()
            idx=seraching(data,namePerson) #calling search

            if(idx!=-1): #emailcontact is found
                #open emailname file
                f=open("emailname.text")
                mail=f.read()#get all the email
                mail=mail.split(",") #convert into list
                to=mail[idx] #get exactly email
                
                speaking("Tell me the message ...!")#take whatsapp massage
                #take timing for the massage
                content=command()
                server=smtplib.SMTP('smtp.gmail.com' , 587)
                server.ehlo()
                server.starttls()
                f=open('password.text',)
                pass_word=f.read()
                server.login('kabirsk58694@gmail.com',pass_word)
                server.sendmail('kabirsk58694@gmail.com',to,content)
                server.quit()
                speaking("Mail sent successfully")

            else: #if name not found
                speaking("Sir name is not found in the email conatact..")
                speaking("Sir..can you want to add in the email contact...!")
                choice=command() #if gives for add contact
                if 'no' in choice:
                    speaking("Ok sir fine")
                else:
                    speaking("write the name sir :")
                    name=input('name :')
                    speaking("Write th email sir")
                    mail_name=input("Write email :")
                    f1=open('emailcontact.text',mode='a')
    
                    name=','+name
                    mail_name=','+mail_name
                    f1.write(name)
                    f2=open('emailname.text',mode='a')
                    f2.write(mail_name)
                    f1.close()
                    f2.close()
                    speaking("Contact add sucessfully")




