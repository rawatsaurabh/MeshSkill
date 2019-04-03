from flask import Flask
from flask_ask import Ask,statement,convert_errors
import logging
import serial
print "Mesh Skill"
ser=serial.Serial("/dev/ttyS0",baudrate=115200,timeout=5.0)
if ser.isOpen():
               print(ser.name + 'is open..')             
app = Flask(__name__)
ask = Ask(app,'/')
logging.getLogger("flask_ask").setLevel(logging.DEBUG)
@ask.intent('LocationControlIntent',mapping={'status':'status','location':'location'})
def location_control(status,location):
               locationDict={
                               'lights':21
                              }           
               //Custom Protocol to send data over Serial UART to ST's BlueNRG Mesh Node.This will change in the future Release.
               value = bytearray([116,101,115,116,32,83,69,84,45,48,51,113])
               ser.write(value)
 port = 5000
app.run(host='0.0.0.0',port=port)
