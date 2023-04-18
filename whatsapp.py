import pywhatkit
import pyttsx3 as p
import speech_recognition as sr
import time

#class what():
#def phone_number():

def whatsapp_chat():
    r = sr.Recognizer()
    engine = p.init()
    engine.setProperty("rate", 140)
    engine.say("to which number would you like to send the message sir?")
    engine.runAndWait()
    print("please say the number to send the message")
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        try:
            phone = r.recognize_google(audio)
            print(phone)
        except sr.UnknownValueError:
            print("")
        except sr.RequestError as e:
            print("")

    #def message_format():
    r2 = sr.Recognizer()
    engine = p.init()
    engine.setProperty("rate", 140)
    engine.say("what message would you like to send?")
    engine.runAndWait()
    print("please say the message")
    with sr.Microphone() as source1:
        r2.adjust_for_ambient_noise(source1)
        audio1 = r2.listen(source1)
        try:
            message = r2.recognize_google(audio1)
            print(message)
        except sr.UnknownValueError:
            print("")
        except sr.RequestError as e:
            print("")

    r3 = sr.Recognizer()
    engine = p.init()
    engine.setProperty("rate", 140)
    engine.say("at which hour would you like to send the message?")
    engine.say("please say the hour in 24 hour format")
    engine.runAndWait()
    print("please say the hour in 24 hour format")
    with sr.Microphone() as source2:
        r3.adjust_for_ambient_noise(source2)
        audio2 = r3.listen(source2)
        try:
            hour = r3.recognize_google(audio2)
            print(hour)
        except sr.UnknownValueError:
            print("")
        except sr.RequestError as e:
            print("")

    r4 = sr.Recognizer()
    engine = p.init()
    engine.setProperty("rate", 140)
    engine.say("at which minute would you like to send the message?")
    engine.runAndWait()
    print("please say the minute")
    with sr.Microphone() as source3:
        r4.adjust_for_ambient_noise(source3)
        audio3 = r4.listen(source3)
        try:
            minute = r4.recognize_google(audio3)
            print(minute)
        except sr.UnknownValueError:
            print("")
        except sr.RequestError as e:
            print("")

    #summary
    engine.setProperty("rate", 140)
    engine.say("the final summary of the message is, phone number is " + phone + " ,message is"  + message + " ,time to send in hour is " + hour + " ,in minute is " + minute + " ,sir")
    print("the final summary of the message is, phone number is " + phone + " ,message is " + message + " ,time to send in hour is " + hour + " ,in minute is " + minute + " ,sir")
    time.sleep(3)

    r5 = sr.Recognizer()
    engine = p.init()
    engine.setProperty("rate", 140)
    engine.say("should i sent the message right now sir?")
    engine.runAndWait()
    print("answer it by saying 'yes' or 'no'.")
    with sr.Microphone() as source4:
        r5.adjust_for_ambient_noise(source4)
        audio4 = r5.listen(source4)
        try:
            result = r5.recognize_google(audio4)
            print(result)
        except sr.UnknownValueError:
            print("")
        except sr.RequestError as e:
            print("")

    hour = int(hour)
    minute = int(minute)

    if "yes" in result:
        print("+91"+phone, message, hour, minute)
        pywhatkit.sendwhatmsg("+91"+phone, message, hour, minute)
        time.sleep(60)
        from repetition import first
        first() 
    elif "no" in result:
        from repetition import first
        first()
#phone_number
#message_format
#you = phone_number
#we = message_format


