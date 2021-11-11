import Receiver
from Sender import SendWiegand
import threading
from random import randrange




while True:
  rdm_msg=randrange(10)
  print("Random Message",rdm_msg)
  hilo1 = threading.Thread(target=SendWiegand(rdm_msg))
  hilo2 = threading.Thread(target=Receiver.ReadWiegand())
  hilo1.start()
  hilo2.start()
  print("Test=",Receiver.num_IN)
  
  if Receiver.num_IN==rdm_msg:
    break;