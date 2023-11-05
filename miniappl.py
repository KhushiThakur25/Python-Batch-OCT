import random
from datetime import datetime as dt
greetingIntent = ["hello","hi","hey","hi there","hello there","hlo"]
dateIntent = ["date","tell me date","what's the date","today's date","what's the date.?"]
timeIntent = ["time","tell me time","what's the time","current time"]
chat = True
while chat:
    msg = input("Enter the msg..")
    msg = msg.lower()
    #if msg == "hello" or msg == "hi" or msg == "hey":
    # in - membership operator
    if msg in greetingIntent:
        print(random.choice(greetingIntent),"user")
    elif msg in dateIntent:
        date = dt.now().date()
        print("Date is :",date.strftime("%d %b,%Y,%A"))
    elif msg in timeIntent:
        time = dt.now().time()
        print("Time is :",time.strftime("%H:%M:%S,%p"))
    elif msg == "bye":
        print("bye user..")
        chat = False
    else:
        print("i don't understand..")
