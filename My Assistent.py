import pyttsx3
import speech_recognition as sr
import pyaudio
import wikipedia
import datetime
import webbrowser  
#import smtplib
import os
import pygame
#import wolframalpha
import pyautogui
import psutil
import pyjokes
import string
import random
import time
import fibonacci
from time import sleep

#from selenium import webdriver
#try:
   #app = wolframalpha.Client('PP9VGA-R9LKJA59QW')
#except Exception:
  #print("Some features are not work. Checke your network connection.")
  # speak("Some features are not work. Checke your network connection.")


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 180) 


def speak(audio):
  engine.say(audio)
  engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12 :
      print("Good Morning!")
      speak("Good Morning!")

    elif hour>=12 and hour<18 :
      print("Good Afternoon!")
      speak("Good Afternoon!")

    else:
      print("Good Evening!")
      speak("Good Evening!")

    print("Rayhan Mahmud sir, I am Ayesha, your virtual assistent. How may I help you sir?")
    speak("Rayhan Mahmud sir, I am Ayesha, your virtual assistent. How may I help you sir?")


#EXTRA STARTING
    # print("Welcome Home sir,")
    # speak("Welcome Home sir,")
    # strTime = datetime.datetime.now().strftime('%m/%d/%Y %I:%M:%S %p')
    # print("Now the time is" +" " + strTime)
    # speak(f"Now the time is {strTime} ")
    # speak("I am at your service sir..")

def takeCommand():
  r = sr.Recognizer()
  with sr.Microphone() as source:
    print("Listening...")
    # speak("Listening...")
    r.pause_threshold = 1
    audio = r.listen(source)

  try:
  
     print("Recognizing..")
     speak("Recognaizing..")
     query = r.recognize_google(audio, language='en-in')
    #  print(f"User said: {query}\n")

  except Exception as e:
    print(e)
    print("Sir, Kindly say that again please")
    speak("Sir, Kindly say that again please")
    return "none"
  return query


def sendEmail(to, content):
  server = smtplib.SMTP('smtp.gmail.com', 587)
  server.ehlo()
  server.starttls()
  server.login('hrosid888@gmail.com', 'rez01789%%')
  server.sendmail('hrosid888@gmail.com', to, content)
  server.close()

def screenshot():
  img = pyautogui.screenshot()
  img.save('C:\\Users\\Rayhan Mahmud\\Pictures\\Screenshots\\ss.png')

def cpu():
  cpuinfo = str(psutil.cpu_percent())
  print("You CPU is at..." + cpuinfo)
  speak("You CPU is at.." + cpuinfo)
  battery = psutil.sensors_battery()
  print("Your battery level is in..")
  speak("Your battery level is in..")
  print(battery.percent)
  speak(battery.percent)
  speak("percent. It's look like all is well. But you can speed up by delete your temporary files. And turn off screen recorder..")


def jokes():
  x = pyjokes.get_joke()
  print(x)
  speak(x)

def jokes2():
  x = pyjokes.get_joke()
  print(x)
  speak(x)

if __name__ == "__main__":
    wishMe()

while True:
    query = takeCommand().lower()



#searching wikipedia

    if 'wikipedia' in query:
      speak("Searching Wikipedia...")
      query = query.replace("wikipedia", "")
      results = wikipedia.summary(query, sentences = 2)
      print("According to Wikipedia..")
      speak("According to Wikipedia..")
      print(results)
      speak(results)








#Ayeshas info

    elif 'about you' in query:
       print("Sure, This is Ayesha. I am a AI and I am your virtual assistent. I was made by Rezwan Mahmud Rayhan on October 27 ,2020. He is nothing but a sinful servant of Almighty Allah. He is from Sylhet, Bangladesh. Nice to meet you sir.")

       speak("Sure, This is Ayesha. I am a AI and I am your virtual assistent. I was made by Rezwan Mahmud Rayhan on October 27 ,2020. He is nothing but a sinful servant of Almighty Allah. He is from Sylhet, Bangladesh. Nice to meet you sir.")

    elif 'thanks' in query:
       print("My pleasure")
       speak("My pleasure!")
    
    elif 'how are you' in query:
      speak("I'm doing well. Sir, there a remainder for you..")
     
  

#Quiting 

    elif 'offline' in query:
      
      print("Sir, I am quiting, have a nice day!")
      speak("Sir, I am quiting, have a nice day!")
      exit()




#Opening Websites
    elif 'open youtube' in query:
        webbrowser.open('www.youtube.com')
        print("Opening Youtube..")
        speak("Opening Youtube..")
    elif 'open google' in query:
        webbrowser.open('www.google.com')
        print("Openinig Google..")
        speak("Openinig Google..")
    elif 'facebook' in query:
        webbrowser.open('www.facebook.com')
        print("Opening Facebook..")
        speak("Opening Facebook..")
        speak("Checking facebook notification..")
        speak("Sir, it's seems you all caught up")

    elif 'stack' in query:
        webbrowser.open('www.stackoverflow.com')
        print("Openinig StackOverflow..")
        speak("Openinig StackOverflow..")
        speak("Don't be scare about bugs. Beacause, Bugs is  one of your friends. who never leave you, if it 6am or 6pm doesn't matter ")




#playing music 
    elif 'play sura' in query:
      music_dir = 'E:\\islami\\Song'
      speak("Playing Sura al-zumur by Shaikh Noreen")
      songs = os.listdir(music_dir)
      print(songs)
      os.startfile(os.path.join(music_dir, songs[0]))




#date and time
    
    elif 'the time' in query:
      strTime = datetime.datetime.now().strftime('%d/%m/%Y %I:%M:%S %p')
      print("Sir, Now the time is" +" " + strTime)
      speak(f"Sir, Now the time is {strTime} ")





#Apps openning
    elif 'whatsapp' in query:
      print("opening WhatsApp")
      speak("opening WhatsApp")
      
      whatPath = "C:\\Users\\Rayhan Mahmud\\AppData\\Local\\WhatsApp\\WhatsApp"
      os.startfile(whatPath)

    elif 'code' in query:
      print("opening Visual Studio Code")
      speak("opening Visual Studio Code")
      
      vsPath = "C:\\Users\\Rayhan Mahmud\\AppData\\Local\\Programs\\Microsoft VS Code\\Code"
      os.startfile(vsPath)


  


# #Calculator option

    elif 'some calculation' in query:
      speak("Enter the first number: ")
      x = int(input("Enter vthe first number:"))
      speak("Enter the second number: ")
      y = int(input("Enter the second number:"))
      print("What kind of calculation should I do?")
      speak("What kind of calculation should I do?")

    elif 'multiplication' in query:
      z = x*y
      result = str(x) +" "+ "multiply by"+" " + str(y) + " " + "=" +" "+ str(z)
      print(result)
      speak(result)

    elif 'division' in query:
      z = x/y
      result = str(x) +" "+ "division by"+" " + str(y) + " " + "=" +" "+ str(z)
      print(result)
      speak(result)
   

    elif 'addition' in query:
      z = x + y
      result = str(x) +" "+ "addition by"+" " + str(y) + " " + "=" +" "+ str(z)
      print(result)
      speak(result)


    elif 'substraction' in query:
      z = x - y
      result = str(x) +" "+ "substract by"+" " + str(y) + " " + "=" +" "+ str(z)
      print(result)
      speak(result)

    elif 'bigger' in query:
      print("Don't think me weak. I am ready to do any kind of calculation...")
      speak("Don't think me weak. I am ready to do any kind of calculation...")


#Currency exchange
    elif 'exchange calculation' in query:
      print("Why not,,let's start..")
      speak("Why not,,let's start..")
    elif "dollar in taka" in query:
      speak("Enter the Dollar amound")
      dtk = int(input("Enter the  Dollar amound:"))
      rate = 85
      in_taka = dtk*rate
      result = str(dtk) + " "+"dollar in Taka:"+" " + str(in_taka) +" "+ "Taka"
      print(result)
      speak(result)
     

    elif "taka in dollar" in query:
      speak("Enter the taka amound")
      dtk = int(input("Enter the  Taka amound:"))
      rate = 0.012
      in_dollar = dtk*rate
      result = str(dtk)+ " "+ "Taka in Dollar:" + " " +  str(in_dollar) +" "+ "Taka"
      print(result)
      speak(result)

    elif "pound in taka" in query:
      speak("Enter the Pound amound")
      dtk = int(input("Enter the  Pound amound:"))
      rate = 110
      in_taka = dtk*rate
      result = str(dtk)+ " "+ "Pound in Taka:" + " " + str(in_taka) +" "+ "Taka"
      print(result)
      speak(result)

    elif "taka in pound" in query:
      speak("Enter the Pound amound")
      dtk = int(input("Enter the  Dollar amound:"))
      rate = 0.0090
      in_pound = dtk*rate
      result = str(dtk)+ " "+ "Taka in Pound:" + " " + str(in_pound) +" "+ "Taka"
      print(result)
      speak(result)


#What Ayeha Can Do??

    elif "can do" in query:
      speak("Hmm, I can do lot of things. hmm , let me think. Oh yes I can speak..")

    
    elif "intelligent" in query:
      print("Yes I am... You have to understand who programmed me!")
      speak("Yes I am. You have to understand who programmed me!")
      speak("Just kidding..I am thinking about how can I surprise you. Do you wanna be surprised???")


#Surprize prank
    elif 'surprise' in query:
      print("Okey! Just wait and see and also listen carefully:)")
      speak("Okey! Just wait and see and also listen carefully:)")
      
      pygame.init()
      window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
      pygame.mixer.init()
      pygame.mixer.music.load("ratsasan.mp3")
      pygame.mixer.music.play()
      sleep(7)
      pygame.mixer.music.load("scary.mp3")
      pygame.mixer.music.play()
      sleep(.5)
      image = pygame.image.load('scr.jpg')
      window.blit(image, (0,0))
      pygame.display.update()
      sleep(4)


    

#Sending Email 

    elif 'send email' in query:
      try:
        print("What should I say?")   
        speak("What should I say?") 
        content = takeCommand().lower()  
        to = "mahmudrayhan029@gmail.com"
        sendEmail(to, content)
        print("Email has been sent successfully!")
        speak("Email has been sent successfully!")

      except Exception as e:
        print(e)
        print("I am really sorry! I can't send the Email.")
        speak("I am really sorry! I can't send the Email.")


#Weather 
     
    # elif 'alpha' in query:
    #   try:
    #     print("Hello! What can I do for you?") 
    #     speak("Hello! What can I do for you?") 
    #     x = input("ask....:")
    #     res = app.query(x)
    #     output = next(res.results).text
    #     print(output)
    #     speak(output)
    
    #   except:
    #     print("Poor Internet Connection...")
    #     speak("Poor Internet Connection...")


#  #SEARCH IN CHROME
# #    elif 'search' in query:
#       print("Sir, What should I search?")
#       speak("Sir, What should I search?")
#       chromepath = 'C:\\Program Files (x86)\\Google\\hrome\\Application\\chrome.exe %s'
#       search = takeCommand().lower()
#       wb.get(chromepath).open_new_tab(search+ '.com')
#       print("Searching Google...")
#       speak("Searching Google...")
#       speak("Showing search result... Mental Hospital wants to know your location..")


#REMEBERING AYESHA...
    elif 'remember' in query:
      print('Yeah sure!  What should I remember?')
      speak('Yeah sure!  What should I remember?')
      data = takeCommand()
     
   
      print('Sir, The remembering process has been successful')
      speak('Sir, The remembering process has been successful')
      rem = open('data.txt', 'w')
      rem.write(data)
      rem.close()

    elif 'told you' in query:
      rem = open('data.txt', 'r')
      print('You told me to remember that... \n'  + rem.read())
      speak('You told me to remember that...' + rem.read())
      



#TAKING SCREENSHOT
    
    elif 'screenshot' in query:
      screenshot()
      print("Your screen had been captured...")
      speak("Your screen had been captured...")


#CPU info

    elif 'system info' in query:
      cpu()
      

#Ayesha's JOKE

    elif 'bored' in query:
      speak("Oh no. Boss, would you like to hear jokes?")

    elif 'joke' in query:
      jokes()
    elif 'another one' in query:
      jokes2()


#ShotDown, LogOut and Restart 
   
    elif 'shutdown' in query:
      os.system("shutdown /s /t 1")
    elif 'logout' in query:
      os.system("shutdown -l")
    elif 'restart' in query:
      os.system("shutdown /r /t 1")






#Reading Books 

    # elif 'read book' in query:

    # elif 'suitable' in query:
    #   speak("Of course not...You guys are stiil not matured. If you go there , your parents will punish you..")
   
    

#Ayesha's Random Password

    elif 'password' in query:
        s1 = string.ascii_lowercase
        s2 = string.ascii_uppercase
        s3 = string.digits
        s4 = string.punctuation
        speak("Yes I can..")
        print("What do you want to keep the length of the password..")
        speak('what do you want to keep the length of the password type here')
        len = int(input("Type here...:")) 
        s=[]
        s.extend(list(s1))
        s.extend(list(s2))
        s.extend(list(s3))
        s.extend(list(s4))
        # print("Your password is:")
        passw = "Sir, Your password is" + " " + "=" + " ".join(random.sample(s,len))
        print(passw)
        speak(passw)
    

#weather brodcast

    elif 'weather' in query:
        speak("Wanna know which city??")
        city = takeCommand().lower()
        speak("It's will be take a momment. Please wait..")
        print("Currently in Sylhet...")
        speak("Currently in Sylhet...")
        print("..................................")
        print("Mostly dry. Warm (max 30°C on Fri afternoon, min 18°C on Sun night). Wind will be generally light.")
        speak("Mostly dry. Warm (max 30°C on Fri afternoon, min 18°C on Sun night). Wind will be generally light.")


#searching
    elif 'search' in query:
        driver = webdriver.Chrome()
        speak("What should I search??")
        keyword = takeCommand().lower()
        driver.get("https://www.google.com/search?q="+keyword+"&oq="+keyword+"&aqs=chrome..69i57j46i39j46i433i457j0j0i433j46i175i199i433j0.10567j0j7&sourceid=chrome&ie=UTF-8")
        print("Searching Google...")
        speak("Searching Google...")
        speak("Showing search result... Mental Hospital wants to know your location..")



#Atesha's Number gussing game

    elif 'gussing game' in query:
      random_num = random.randint(10, 40)
      the_number = random_num
      i = 10

      print("-===Welcome to the Rayhan Mahmud's gussing game===- \n ")
      speak("Welcome to the Rayhan Mahmud's gussing game ")
      print("***INTRODUCTION: \n *//The game is about to guss a number from some clues. You will be get 10 chances to guss the number correctly. If you can guss the number in this 10 chances you will be declare as winner. If you can't then you will be loss..")
      speak("INTRODUCTION: \n The game is about to guss a number from some clues. You will be get 10 chances to guss the number correctly. If you can guss the number in this 10 chances you will be declare as winner. If you can't then you will be loss..")
      print("***RULES: \n 1. You have to guss the number under 10 chances. \n 2. Your input must have to be a number. ")
      speak("RULES: \n  You have to guss the number under 10 chances. \n Your input must have to be a number. ")
      print("***CLUES: \n 1. The number is a posetive number. \n 2. The number is under 60.")
      speak("CLUES: \n  The number is a posetive number. \n  The number is under 60.")

  #functionals
      while True:
        speak("Enter your gussing number")
        user_input = int(input("Enter your gussing number:"))
  
        i = i - 1
        if user_input == the_number:
          print("Congratulations! You correctly guss the number..")
          speak("Congratulations! You correctly guss the number..")
          print("Number of chances you took to finish ","="," ", 10 - i)
          speak("Number of chances you took to finish ")
          speak(10 - i)
          break
        elif i == 0:
          print("game over boss..")
          speak("game over boss..")
          print("Think wisely and follow my clues!")
          speak("Think wisely and follow my clues!")
          print("The right answer is ", the_number)
          speak("The right answer is ")
          speak(the_number)
          break
#clues
  
        elif user_input > the_number + 10 and i < 9:
          print("You are too far from the number...")
          speak("You are too far from the number...")
          print("Try again. Never give up!")
          speak("Try again. Never give up!")
          print("Your gussing opportunity left ","="," ", i)
          speak("Your gussing opportunity left ")
          speak(i)
          print("#Clue: The number is less than 40 and more than 10..")
          speak("Clue: The number is less than 40 and more than 10..")
          continue

        elif (user_input + 5 == the_number and i < 8 ):
          print("Increase little bit more...")
          speak("Increase little bit more...")
          print("Your gussing opportunity left " , "=", " ", i)
          speak("Your gussing opportunity left ")
          speak(i)
        elif (user_input - 5 == the_number  and i < 8 ):
          print("Decrease little bit more...")
          speak("Decrease little bit more...")
          print("Your gussing opportunity left " , "=", " ", i)
          speak("Your gussing opportunity left ")
          speak(i)

        elif user_input < the_number - 10  and i < 8:
          print("You are too far from the number...")
          speak("You are too far from the number...")
          print("Increase the number..")
          speak("Increase the number..")
          print("Your gussing opportunity left ","="," ", i)
          speak("Your gussing opportunity left ")
          speak(i)
          print("#Clue: The number is less than 40 and more than 10..")
          speak("Clue: The number is less than 40 and more than 10..")
          continue

        elif user_input + 2 == the_number or user_input - 2 == the_number and i < 8:
          print("Decrease little bit or incrase little bit..! You are near to the victory.")
          speak("Decrease little bit or increase little bit..! You are near to the victory.")
          print("Never give up!")
          speak("Never give up!")
          print("Your gussing opportunity left ","="," ", i)
          speak("Your gussing opportunity left ")
          speak(i)
          continue


#ending
        elif user_input != the_number and the_number % 2 == 0 and i < 6:
          print("Wrong gussing!")
          speak("Wrong gussing!") 
          print("#Clue: The number is a Even number.")
          speak("Clue: The number is a Even number.")
          print("Your gussing opportunity left ","="," ", i)
          speak("Your gussing opportunity left ")
          speak(i)
          continue
        elif user_input != the_number and the_number % 2 != 0 and i < 6:
          print("Wrong gussing!")
          speak("Wrong gussing!") 
          print("#Clue: The number is a Odd number.")
          speak("Clue: The number is a Odd number.")
          print("Your gussing opportunity left ","="," ", i)
          speak("Your gussing opportunity left ")
          speak(i)
          continue
  
        elif user_input != the_number:
          print("Wrong gussing!")
          speak("Wrong gussing!")
          print("Try again. Never give up!")
          speak("Try again. Never give up!")
          print("Your gussing opportunity left ","="," ", i)
          speak("Your gussing opportunity left ")
          speak(i)
          continue
 
        else:
          print("Input Error! Enter a valid input...")
          speak("Input Error! Enter a valid input...")



#fibonacci
    elif'fibonacci' in query:
      speak("Until how much do you want to find out the Fibonacci numbers")
      user_input = int(input("Until how much do you want to find out the Fibonacci numbers?: "))
      print(fibonacci.fibo(user_input))
      speak(f"You have successfully done to find out the Fibonacci numbers untill {user_input}")




#Ayeshas work project
  
    elif "work" in query:
    
      i = 0

      speak("Yeah sure, I am ready to do..")
      print("Yeah sure, I am ready to do..")
      speak("How much 'delete' button do you wanna press?")
      x = int(input("How much 'delete' button do you wanna press? \n"))

      speak("How much 'backspace' button do you wannna press?")
      y = int(input("How much 'backspace' button do you wannna press? \n"))

      speak("After how many do you want to stop?")
      z = int(input("After how many do you want to stop? \n"))

      time.sleep(4)
 
      while True:

        if i == z:
          print("Hurray! Your work succssfully comleted..")
          speak("Hurray! Your work succssfully comleted..")
          break

        elif i == 3:
          print("Boss, 10 lines comleted..")
          speak("Boss, 10 lines comleted..")
          i = i + 1

        elif i % 2 == 0 and i == z/2:
          print("Hey Boss! I completed half of the work successfully.")
          speak("Hey Boss! I completed half of the work successfully.")
          i = i + 1
        elif i % 2 != 0 and i == (z + 1)/2:
          print("Hey Boss! I completed half of the work successfully.")
          speak("Hey Boss! I completed half of the work successfully.")
          i = i + 1



        else:
          time.sleep(0.25)
          pyautogui.press('home')

          for _ in range(x):
            pyautogui.press('delete')
            pyautogui.press('end')

          for _ in range(y):
            pyautogui.press('backspace')


        pyautogui.press('down')
        i = i + 1
        # time.sleep(1)
        continue



        