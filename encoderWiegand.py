import pigpio
import time



""" --------------------------------------------------------------------------------------------


   Codificador Wiegand


-------------------------------------------------------------------------------------------- """
   
class Encoder:

    def __init__(self, pi, gpio_0, gpio_1):

        self.pi = pi
        self.gpio_0 = gpio_0
        self.gpio_1 = gpio_1

        # Inicializo pins de la RPI como salidas wiegand
        self.pi.set_mode(gpio_0, pigpio.OUTPUT)
        self.pi.set_mode(gpio_1, pigpio.OUTPUT)    

        # Asigno un valor logico 1 a los pines de salida wiegand
        self.pi.write(gpio_0, 1)
        self.pi.write(gpio_1, 1)

    @staticmethod
    def encoderWiegand(valor, pi, gpio_0, gpio_1, cantidadBits):
   
        i = 0 
 
        Variable = bin(valor)[2:].zfill(cantidadBits)  
        
        #Variable = "10000000001000010011110011"

        # Envio codigo wiegand    
        
        while i < cantidadBits:
                       
            if int(Variable.format(valor)[i],2)  == 0: 
                pi.write(gpio_0, 0) 
                time.sleep(0.00008) # sleep delay fall (std : 0.00008)
                pi.write(gpio_0, 1) 
                time.sleep(0.00024) # sleep delay rise (std : 0.00024) 
                #print("0")
            else: 
                pi.write(gpio_1, 0) 
                time.sleep(0.00008) # sleep delay fall (std : 0.00008)
                pi.write(gpio_1, 1) 
                time.sleep(0.00024) # sleep delay rise (std : 0.00024)   
                #print("1")
            
            i = i + 1
    
 