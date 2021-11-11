from decoderWiegand import decoder
import lcd_i2c as lcd_i2c
import time
import pigpio
global num_IN
global msg_LCD
num_IN=0

def callback(bits, code):
  global num_IN
  #print("code={}".format(code))
  num_IN=code
                                                                                                                                          
pi = pigpio.pi()


def ReadWiegand():
  global num_IN
  
  w_D = decoder(pi, 23, 24, callback)
  time.sleep(1)
  #w_D.cancel()
  
    
      #pi.stop()
  if num_IN==8:
    return True
  else:
    return False