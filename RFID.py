import RPi.GPIO as g
import MFRC522
import signal
import time
import pyrebase
g.setwarnings(False)
MIFAREReader = MFRC522.MFRC522()
config = {
  "apiKey": "AIzaSyAqvZfsPEItIeflTuVP_Xy7hoxWlu-Lsxg",
  "authDomain": "myfirebase3-9ac1b.firebaseapp.com",
  "databaseURL": "https://myfirebase3-9ac1b.firebaseio.com/",
  "storageBucket": "myfirebase3-9ac1b.appspot.com",
    }
g.setmode(g.BOARD)
red=37
g.setup(red,g.OUT)
firebase=pyrebase.initialize_app(config)
db=firebase.database()
c=1
list=[]
while True:
    (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
    (status,uid) = MIFAREReader.MFRC522_Anticoll()
    if status == MIFAREReader.MI_OK:
        if uid not in list:
            u=str(uid)
            p="product"+str(c)
            print ("Card detected")
            g.output(red,true)
            time.sleep(0.5)
            g.output(red,False)
            list.append(uid)
            t=u+" claimed"
            db.child("/").update({p:t})
            c=c+1
time.sleep(1)
g.cleanup()
