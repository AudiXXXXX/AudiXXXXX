
# condition-----> I
import pyttsx3
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
 
import random
speak("Hay, how are you . Are you ready to play game")
speak("choose odd or even")
b=(input("choose odd or even"))

if(b=="odd"):
    a="even"
else:
    a="odd"
speak("you have choose")
speak(b)
speak("I has choose")
speak(a)
print("you have choose", b)
print("computer has choose",a)
speak(",,,enter a number between 1-6")
c=int(input("enter a number between 1-6"))
d=random.randint(1,6)
speak("you choose")
speak(c)
speak("computer choose")
speak(d)
print("you choose", c)
print("computer choose", d)

e=c+d
speak(e)
print(e)

if(b=="even"):
        e=c+d
        if(e % 2==0):
            g="you win"
        else:
           g="you loose"
else:
        e=c+d
        if(e % 2== 1):
           g="you win"
        else:
            g="you loose"
speak(g)
print(g)

#condition ---------> II
if g=="you win":
    speak("Choose balling or batting")
    h=input("Choose balling or batting")
else:
    i=random.randint(1,2)
    if i== 1:
        i= "balling"
        h="batting"
    else:
        i="batting"
        h="balling"
if h=="batting":
    i="balling"
elif h== "balling":
    i="batting"
speak("you ")
speak(h)
speak("i")
speak(i)
print("you --->", h)
print("comp --->", i)

# condition ----------> III

if h=="balling":
    j=0
    
    while j<200 :
        speak("Enter your ball")
        k= int(input("Enter you ball"))
        z= random.randint(1,6)
        speak(z)
        print("computer-",z)
        print("you-",k)
        
        if k==z:
            break
        else:
            pass
        
        j=j +z

        
        
        print("whole computer score-",j)
        print("-----------------------------------")
        speak ("next turn")
        
    speak("target is ")
    speak(j)
    print("target is ",j)
    speak("your tern to batting")
    print("your tern to batting")
    m=0
    while m<j:
        n=random.randint(1,6)
        o=int(input("Enter your run"))
        speak(n)
        print("computer-",n)
        print("you-",o)
        if o==n:
            break
        m=m+o
        
        print("whole-",m)
        print("-----------------------------------")
        speak("Next turn")
    if m>j :
        speak("you win")
        print("you win")
    else:
         speak ("you losse")
         print("you losse")
        

# condition -------> IV

else:
    j=0
    while j<200:
        k=random.randint(1,6)
        speak("Enter your run")
        z=int(input("enter your run"))
        speak(k)
        print("you-",z)
        print("computer-",k)
        j=j+z
        
        
        print("whole score-",j)
        print("----------------------------------")
        speak("Next turn")
        if k==z:
            break
        
    speak("you have score")
    speak(j)
    speak("run")
    speak("its term of your balling")  
    print("you have score",j,"run")
    print("its term of your balling")
    q=0
    while q<j:
        r=random.randint(1,6)
        s=int(input("enter your ball"))
        speak(r)
        print("you-",s)
        print("computer-",r)
        if s==r:
            break
        q=q+r
        
        print("computer whole score-",q)

        print("----------------------------------")
        speak("Next term")
        
        
    if q>j:
         speak("YOU losse")
         print("you losse")
    elif(q==j):
        speak ("draw")
        print("draw")
    else:
        speak("you win")
        print("you win")








    



