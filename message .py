import pywhatkit as pwt
from datetime import datetime

now = datetime.now()

def sendmessage(total):
    if(total==1):
        pwt.sendwhatmsg("+918017262239", "Patient is in critical condition",now.hour,now.minute+1,15,True,10)
    elif(total==2):
        pwt.sendwhatmsg("+918017262239", "Patient needs help for washroom",now.hour,now.minute+1,15,True,10)
    elif(total==3):
        pwt.sendwhatmsg("+918017262239", "Patient needs water",now.hour,now.minute+1,15,True,10)