import pyttsx3

engine = pyttsx3.init() # to initialize the library
name = input("Enter your name : ")
# engine.say("hello world!") 
engine.say(f"hello {name}")
engine.runAndWait() #run and foor the program to finish before my prg quits.get()