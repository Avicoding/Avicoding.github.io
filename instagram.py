#import pywhatkit
#pywhatkit.sendwhatmsg("+916306844234","hi",16,44)
import time
from keyboard import press
import subprocess
    
msg = "hi"

subprocess.Popen(["cmd", "/C", "start whatsapp://send?phone=+919580485600 & text="+str(msg)], shell=True)
        
time.sleep(1)
press('enter')



