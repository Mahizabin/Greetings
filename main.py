#Quick Quiz2

name=input("Enter your name ")
import time
timestamp = time.strftime('%H:%M:%S')
print("The time is",timestamp)
hour= int(time.strftime('%H'))
if(hour>0 and hour<12):
    print("Good Morning",name)
elif(hour>=12 and hour<17):
    print("Good Afternoon",name)
else:
    print("Good Night",name)
 


