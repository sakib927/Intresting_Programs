import face_recognition
import cv2
import numpy as np
import csv
import os
from os import listdir
from datetime import datetime
import qrcode  
import time
import pyttsx3
from random_word import RandomWords
from quote import quote
import pyautogui
import random
from global_var import *
from gformcreation import *

video_capture = cv2.VideoCapture(0)

engine  = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)        #0 for male  #1 for female 

def get_url():
    if Url_for_google_form != "error":
        print("New Url Created")
        return Url_for_google_form
    else :
        print("Using Recovery Url Due To Some Technical Issues")
        return Url_for_google_form_recovery

def speak(audio):
    '''This function will take a string and then read it aloud'''
    engine.say(audio)
    engine.runAndWait()

def wishme():
    '''This function will greet you based on time'''
    hour = int(datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good Morning!")
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        print("Good Afternoon!")
        speak("Good Afternoon!")   

    else:
        print("Good Evening!")
        speak("Good Evening!")  
 
wishme()

import speech_recognition as sr

def takeCommand():
    '''It takes microphone input from the user and returns string output'''
                                                                        
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query

#New data entry  edit in imgtest.py for first release
def take_pic():
    '''Takes a new data by taking  picture.
    Note :- To take a pic press s button'''

    speak("Enter number of data that you want to add :- ")
    no_loop = int(input("Enter number of data that you want to add :- "))
    
    for i in range(no_loop):
        print("Please Follow the following Rules :- \n 1) Do not use blank spaces instead you can use _ \n 2) Use Camel casing \n Example :- 'Sakib_Ali' Or 'SakibAli' ")
        speak("Please Follow the following Rules :- \n 1) Do not use blank spaces instead you can use _ \n 2) Use Camel casing \n Example :- 'Sakib_Ali' Or 'SakibAli' ")
        print("Please type Your Name")
        speak("Please type Your Name")
        #print("You may use the the speak command to speak you name or you can type your name.")
        #speak("You may use the the speak command to speak you name or you can type your name")
        #print("Disclaimer your spelling of name may be incorrect when using the speak function. If this happens please contact the administrator.")
        #speak("Disclaimer your spelling of name may be incorrect when using the speak function. If this happens please contact the administrator")
        #print("If you wish to use speak function press 1 when your opinion is asked else to use keyboard press 2")
        #speak("If you wish to use speak function press 1 when your opinion is asked else to use keyboard press 2")
        #opinion = int(input("Please input your opinion:- "))
        opinion = 2
        if opinion == 1:
            your_name = takeCommand().lower()
        elif opinion == 2:
            speak("Enter your name :- ")
            your_name = input("Enter your name :- ")
        else:
            print("Error")
            print("Due to error we will take the attendance first. Please contact the administrator. ")
            speak("Due to error we will take the attendance first. Please contact the administrator. ")
            break

        if your_name == "none" or your_name == 'None':
            print("error")
            speak("Due to error we will take the attendance first. Please contact the administrator. ")
            print("Due to error we will take the attendance first. Please contact the administrator. ")
            break

        img_name = path_for_photo_storing+'\\' + your_name + ".jpg"
        camera = cv2.VideoCapture(0)
        speak("Enter s to take your photo")
        while True:
            return_value,image = camera.read()
            cv2.imshow('image',image)
            if cv2.waitKey(1)& 0xFF == ord('s'):
                cv2.imwrite(img_name,image)
                break
        camera.release()
        cv2.destroyAllWindows()
    
    if no_loop>0:
        return 1

while True:
    print("Hello do you want to add new data in the database ? Yes/No")
    speak("Hello do you want to add new data in the database ? Yes/No")
    alpha_choice = input("Enter Your Choice ")
    alpha_choice = alpha_choice.lower()
    if alpha_choice == 'yes':
        admin_instruct = take_pic()
        break
    elif alpha_choice =='no':
        print("No new data added to database")
        speak("No new data added to database")
        break
    else :
        print("Please answer in yes or no")
        continue

time.sleep(5)

known_faces_names =  []
folder_dir = path_for_photo_storing
for images in os.listdir(folder_dir):
	if (images.endswith(".jpg")):
         temp_image = os.path.splitext(images)[0]
         known_faces_names.append(temp_image)


print("The following students are in the database :- ")
speak("The following students are in the database :- ")
print(known_faces_names)
#speak(known_faces_names)

known_faces_names_images = []
known_faces_encoding = []
known_faces_path = []

for i in known_faces_names:
    x = i+"_image"
    known_faces_names_images.append(x)
    y = i+"_encoding"
    known_faces_encoding.append(y)
    path = path_for_photo_storing +"\\" + i + ".jpg"
    known_faces_path.append(path)

def generate_Qr():
    '''This function will generate a qr code of the link.'''
    url_for_google_form = get_url()
    for i in range(len(known_faces_names)):
        your_name_qr = known_faces_names[i] 
        Url = url_for_google_form + your_name_qr
        qr_img = qrcode.make(Url)  
        img_name = path_for_qrcodes_storing+'\\' + your_name_qr + ".jpg"
        qr_img.save(img_name)

generate_Qr()

for i in range(len(known_faces_path)):
    known_faces_names_images[i] = face_recognition.load_image_file(known_faces_path[i])
    known_faces_encoding[i] = face_recognition.face_encodings(known_faces_names_images[i])[0]


students  = known_faces_names.copy()

face_loction  = []
face_encoding = []
face_names = []
s = True

now = datetime.now()
current_date = now.strftime("%Y-%m-%d")

print("Todays Date is :- ")
speak("Todays Date is :- ")
print(current_date)
speak(current_date)

current_date_file = now.strftime("%Y-%m-%d")
def create_folder():
    '''This function will create a folder and name it by todays name in the format of yyyy-mm-dd'''
    directory = "Folder_Of_" + current_date_file
    parent_dir = path_for_main_folder
    ultimate_path = os.path.join(parent_dir, directory)
    os.mkdir(ultimate_path)
    print("Directory '% s' created" % directory)
    return ultimate_path

def create_morning_folder():
    '''This function will create a folder and name it by Puching In'''
    directory = "Folder_Of_Punching_In" 
    parent_dir = path_for_main_folder +"//"+"Folder_Of_"+current_date_file
    ultimate_path = os.path.join(parent_dir, directory)
    os.mkdir(ultimate_path)
    print("Directory '% s' created" % directory)
    return ultimate_path

def create_evening_folder():
    '''This function will create a folder and name it by Punching out'''
    directory = "Folder_Of_Punching_Out" 
    parent_dir = path_for_main_folder +"//"+"Folder_Of_"+current_date_file
    ultimate_path = os.path.join(parent_dir, directory)
    os.mkdir(ultimate_path)
    print("Directory '% s' created" % directory)
    return ultimate_path

checking_path = os.path.exists( path_for_main_folder +"//"+"Folder_Of_"+current_date_file)

if checking_path == True:
    print("Folder exists")
else :
    print("Folder doen't exists")
    print("Creating folder")
    ultimate_path = create_folder()

hour = int(datetime.now().hour)

checking_path_folder_evn = os.path.exists(path_for_main_folder+"//"+"Folder_Of_"+ current_date_file +"//" + "Folder_Of_Punching_Out")
checking_path_folder_mor = os.path.exists(path_for_main_folder+"//"+"Folder_Of_"+current_date_file +"//"+ "Folder_Of_Punching_In")

if hour>=0 and hour<12:
    file_name_prefix = "Punching In"
    if checking_path_folder_mor == False:
        ultimate_path_morning = create_morning_folder()
        ultimate_path_for_files = ultimate_path_morning
    else :
        ultimate_path_for_files = path_for_main_folder +"//"+"Folder_Of_"+ current_date_file +"//" + "Folder_Of_Punching_In"
elif hour>=12 and hour<23 :
    file_name_prefix = "Punching Out"
    if checking_path_folder_evn == False:
        ultimate_path_evening = create_evening_folder()
        ultimate_path_for_files = path_for_main_folder +"//"+"Folder_Of_"+ current_date_file +"//" + "Folder_Of_Punching_Out"
    else :
        ultimate_path_for_files = checking_path_folder_evn

folder = ultimate_path_for_files
file_name = file_name_prefix + '.csv'
file_path = os.path.join(folder, file_name)

f = open(file_path ,'w+',newline = '')
lnwriter = csv.writer(f)

while True:
    _,frame = video_capture.read()         ## _ first will be  signal which we dont want from second we will take the input
    small_frame = cv2.resize(frame,(0,0),fx=0.25,fy=0.25)    ##resizeing in small format
    rgb_small_frame = small_frame[:,:,::-1]   ## cv2 allways take the input in bgr format so we are converting the rgb in to bgr by reverse slicing -1 
    if s:
        face_loctions = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame,face_loctions)
        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_faces_encoding,face_encoding)
            name = ""
            face_distace = face_recognition.face_distance(known_faces_encoding,face_encoding)
            best_match_index = np.argmin(face_distace)
            if matches[best_match_index]:
                name = known_faces_names[best_match_index]

            face_names.append(name)
            if name in known_faces_names:
                if name in students:
                    students.remove(name)
                    myScreenshot = pyautogui.screenshot()
                    current_date = now.strftime("%Y-%m-%d-%I-%M-%p")
                    time1 = current_date
                    url = ultimate_path_for_files + "//" + name +"_" +time1 + ".jpg"
                    myScreenshot.save(url)
                    speak("Welcome"+ name)
                    Url = path_for_qrcodes_storing + "\\" + name  + ".jpg"                             ##changes made here
                    speak("Please scan the Qr code which is displayed ")
                    img = cv2.imread(Url,
				                        cv2.IMREAD_COLOR)

                    cv2.imshow(name, img)
                    cv2.waitKey(30000)      #note miliseconds #30s set
                    cv2.destroyWindow(name)                                  ## to prevent multiple attentance of same person
                    print("Remaning Students :-")
                    speak("Remaning Students Are :-")                  
                    print(students)
                    #speak(students)
                    speak("To Exit please press q")
                    current_time = now.strftime("%I-%M %p")
                    lnwriter.writerow([name,current_time,url])

    cv2.imshow("Attendence System ", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


video_capture.release()
cv2.destroyAllWindows()
f.close()

print("Wishing you a great day")
speak("wishing you a great day")
print("Here is you Quote of the day You may read it .")
speak("Here is you Quote of the day You may read it .")

r = RandomWords()           
w = r.get_random_word()
res = quote(w, limit=1)
safewords = ["code of behavior",
"custom",
"diplomatic code",
"etiquette",
"formalities",
"guideline" ]

try:
    for i in range(len(res)):
        print("Keyword Generated: ",w)
        print("\nQuote Generated: ",res[i]['quote'])
except TypeError:
    safewords_g = random.randint(0,len(safewords)-1)
    res = quote(safewords[safewords_g],limit=1)
    for i in range(len(res)):
        print("Keyword Generated: ",safewords[safewords_g])
        print("\nQuote Generated: ",res[i]['quote'])

time.sleep(7)

print("The Following Attendance Marked :- ")
speak("The Following Attendance Marked :- ")
with open(file_path, mode ='r')as file:
  csvFile = csv.reader(file)
  print("Names " + "Time_Stamp" )
  for lines in csvFile:
        print(lines[0],lines[1])
        speak(lines[0])
        speak(lines[1])