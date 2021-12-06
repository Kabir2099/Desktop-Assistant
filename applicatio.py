import webbrowser
import os
import cv2



def openApps(query):
    if 'youtube' in query:
        webbrowser.open("https://www.youtube.com")
    elif 'whatsapp' in query:
        webbrowser.open('whatsapp.com')
    elif 'google map' in query:
        webbrowser.open('https://www.google.com/maps/place/V+I+P+Guest+House/@22.5687639,88.4861334,18.25z/data=!4m8!3m7!1s0x3a020ad7a5dededd:0x1347c2ae8264d8fb!5m2!4m1!1i2!8m2!3d22.5677027!4d88.487095?hl=fr')
    elif 'google' in query:
        webbrowser.open('google.com')
    elif 'chrome' in query:
        code_path="C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
        os.startfile(code_path)
    elif 'visual studio' in query:
        code_path="C:\\Users\\KABIR\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(code_path)
    elif 'dev c' in query:
        os.startfile("C:\\Program Files (x86)\\Dev-Cpp\\devcpp.exe")
    elif 'netflix' in query:
        webbrowser.open('netflix.com')
    elif 'telegram' in query:
        webbrowser.open("https://www.telegram.com")
    elif 'twitter' in query:
        webbrowser.open("https://twitter.com")
    elif 'facebook' in query:
        webbrowser.open("https://www.facebook.com")
    elif 'stackoverflow' in query:
        webbrowser.open("https://stackoverflow.com")
    elif 'gfg' in query:
        webbrowser.open("https://www.geeksforgeeks.org")
    elif 'leetcode' in query:
        webbrowser.open("https://leetcode.com")
    elif 'hackerrank' in query:
        webbrowser.open("https://www.hackerrank.com")
    elif 'codechef' in query:
        webbrowser.open("https://www.codechef.com")
        
    elif 'codeforce' in query:
        webbrowser.open("https://codeforces.com/")
    elif 'quora' in query:
        webbrowser.open("https://www.quora.com/")
    elif 'udemy' in query:
        webbrowser.open("https://www.udemy.com/")
    elif 'coursera' in query:
        webbrowser.open("https://www.coursera.org/in")
    elif 'music' in query:
        os.startfile("C:\\Users\\KABIR\Desktop\\My Song")
    elif 'video' in query:
        os.startfile("C:\\Users\\KABIR\\Desktop\\My Song")
    elif 'camera' in query:
        cap=cv2.VideoCapture(0)
        while True:
            ret,img=cap.read()
            cv2.imshow('webcam',img)
            k=cv2.waitKey(50)
            if k==27:
                break

        cap.release()
        cv2.destroyAllWindows()
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
   
        
       