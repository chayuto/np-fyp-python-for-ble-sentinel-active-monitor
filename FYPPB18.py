
import subprocess, time, httplib, urllib

from bbio import *

#***************************************************

class RunCmd(object):
    def cmd_run(self, cmd):
        self.cmd = cmd
        subprocess.call(self.cmd, shell=True)

#**************Starting message and setting up the GPIO***************

bbio.bbio_init()

pinMode(GPIO2_1, OUTPUT)
pinMode(GPIO0_27, INPUT)
#while True: #Run the progam infinitely

#Calling lcdmessage1.js
a = RunCmd()
a.cmd_run('node lcdmessage1.js')

delay(800)
digitalWrite(GPIO2_1, HIGH)
delay(3000)
X=digitalRead(GPIO0_27)
digitalWrite(GPIO2_1, LOW)

#*************Vital Sign mode***********
if X==1:
 #Calling lcdmessagevs,js
 a = RunCmd()
 a.cmd_run('node lcdmessagevs.js')
 a.cmd_run('python directconnect.py')
 a.cmd_run('python getattributevitalsign.py')
 a.cmd_run('python disconnect.py') 
 #a.cmd_run('./python_uploader upload vitaldata.txt')
 a.cmd_run('node lcdmessagevsdone.js')

#***********Fall detection mode*********
else: 
 #Calling lcdmessagefd.js
 a = RunCmd()
 a.cmd_run('node lcdmessagefd.js')
 a.cmd_run('python directconnect.py')
 a.cmd_run('python getattributefall.py')
 a.cmd_run('node lcdmessagefalling.js')
 a.cmd_run('python disconnect.py')

 conn = httplib.HTTPSConnection("api.pushover.net:443")
 conn.request("POST", "/1/messages.json",
  urllib.urlencode({
    "token": "aA2bEjV2CqtwavfNFLTVCCb7cCbofT",
    "user": "ukV5ZvQedvmEAuUKtsSPPoH77gdDVa",
    "message": "fall detected",
   "title": "Sentinel Active Monitor",
  }), { "Content-type": "application/x-www-form-urlencoded" })
 conn.getresponse()


#lcdmessagefall.js
#lcdmessagenofall.js

#*************Ending message***************

a = RunCmd()
a.cmd_run('node lcdmessageend.js')

bbio.bbio_cleanup()

