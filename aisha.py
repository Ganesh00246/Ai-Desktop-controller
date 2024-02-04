from unittest import result
import pyttsx3
import speech_recognition as sr
import datetime
import os #opreating system controler
import cv2 # my fev computer vision
from requests import get #ip web link
import wikipedia
import webbrowser #web link
import pywhatkit as kit #message sender
import smtpd
from asyncore import read
from http import server
import smtplib
import sys
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
voices=engine.setProperty('voice',voices[2].id)
engine.setProperty('rate',160)
def speak(audio):
engine.say(audio)
print(audio)
engine.runAndWait()
def TakeCommand():
r=sr.Recognizer()
with sr.Microphone() as source:
print('Listing....')
r.pause_threshold=1
audio=r.listen(source,timeout=10,phrase_time_limit=10)
try:
print("Recognizing....")
query=r.recognize_google(audio,language='en-in')
print(f"user said : {query}")
except Exception as e:
speak(" please Say that again. Gk")
return " none"
return query
def wish():
hour=int(datetime.datetime.now().hour)
if(hour>=0) and hour<=12:
speak("Good morning gk")
elif(hour>12) and hour<18 :
speak("Good afternoon gk")
else:
speak("Good evening gk ")
# speak(" i am your please tell me how can i help you ")
def sendEmail(to,content) :
server=smtplib.SMTP("smtp.gmail.com",587)
server.ehlo()
server.starttls()
server.login('gkendre2468@gmail.com','gkendre123')
server.sendmail('gkendre2468@gmail.com', to ,content)
server.close()
if __name__=="__main__":
wish()
# if 1:
while True:
query=TakeCommand().lower()
#Not Working check
if "open vs code " in query:
npath="C:\\Users\\Public\\Desktop\\chrome.exe"
os.startfile(npath)
#Not working check
elif "open command prompt " in query:
os.system("start cmd")
elif "open camera" in query:
cap=cv2.VideoCapture(0)
while True:
ret ,img=cap.read()
cv2.imshow('webcamp',img)
k=cv2.waitKey(50)
if k==27:
break
cap.release()
cv2.destroyAllWindows()
elif "what is my current ip address" in query:
ip=get('https://api.ipify.org').text
speak(f"Your current ip address is {ip}")
#cm according to wikipedia what is (query)
elif "wikipedia" in query:
speak("searching wikipedia....")
query=query.replace("wikipedia","")
results=wikipedia.summary(query,sentences=2)
speak("according to wikipedia")
speak(results)
#web site link
elif "open youtube" in query:
webbrowser.open("www.youtube.com")
# speak("sir, what , should i search on youtube")
#google search watch this code "taking command from user here "
elif "open google" in query:
speak("what should i search on google ,Gk")
camd=TakeCommand().lower()
res= webbrowser.open(f"{camd}")
# #sending message whatsapp message check and learn :
# elif "send message " in query:
# kit.sendwhatmsg("+91",this is testing protocal "2,25)
elif " email to ganesh " in query:
try:
speak("what should email sir ")
content=TakeCommand().lower()
to ="ganesh3850@gmail.com"
sendEmail=(to,content)
speak("Email has been sent to ganesh ")
except Exception as e:
print(e)
speak("sorry Gk i am not able to send this mail to
ganesh ")
elif "no thanks" in query:
speak("Ok , now i am going to sleep , if you have any other
work just call me i'll be there ")
sys.exit()
elif "hi aisha" in query:
speak("hello handsome")
elif "good morning Ayesha" in query:
speak("so , tell me what task to perform now ")
elif " do nothing "in query:
speak("ok as you say ")
speak(" do we have any other work to do...")