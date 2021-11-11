from random import randrange
from encoderWiegand import Encoder
import time
import pigpio
from random import randrange

#print("Incia Sender")
pi = pigpio.pi()

def SendWiegand(dato):                                                                                                                                     
  w_E = Encoder(pi, 17, 27)  
  w_E.encoderWiegand(dato,pi,17,27,4)
  time.sleep(2)