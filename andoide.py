
import time
from keyboard import press
import subprocess
    
msg ="hi"

subprocess.Popen(["cmd", "/C", "start whatsapp://send?phone=+916306844234^&text="+str(msg)], shell=True)
        
time.sleep(5)
press('enter')


