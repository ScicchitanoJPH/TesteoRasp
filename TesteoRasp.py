import colorama
import RPi.GPIO as GPIO
import time
import datetime as dt
import serial  
import os, time
from colorama import Fore , Style
import Receiver
from Sender import SendWiegand
import threading
from random import randrange


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

colorama.init(autoreset=True)

msg=0

StatusSalida="Sin Testear"
StatusEntradas="Sin Testear"
StatusSerial="Sin Testear"
StatusWiegand="Sin Testear"

#Bornera de salida
Pin_Contacto1=5
Pin_Contacto2=6
Pin_Contacto3=26
Pin_Contacto4=16

#Pines
Pin_LED1=13
Pin_LED2=19

#Bornera de entrada
Pin_IN1=21
Pin_IN2=20



#Seteo de pines
GPIO.setup(Pin_Contacto1, GPIO.OUT)
GPIO.setup(Pin_Contacto2, GPIO.OUT)
GPIO.setup(Pin_Contacto3, GPIO.OUT)
GPIO.setup(Pin_Contacto4, GPIO.OUT)
GPIO.setup(Pin_LED1, GPIO.OUT)
GPIO.setup(Pin_LED2, GPIO.OUT)

GPIO.setup(Pin_IN1, GPIO.IN)
GPIO.setup(Pin_IN2, GPIO.IN)



# Activo todas las salidas
def ContactosON():
    GPIO.output(Pin_Contacto1, True)
    GPIO.output(Pin_Contacto2, True)
    GPIO.output(Pin_Contacto3, True)
    GPIO.output(Pin_Contacto4, True)

    GPIO.output(Pin_LED1, True)
    GPIO.output(Pin_LED2, True)

def ContactosOFF():
    GPIO.output(Pin_Contacto1, False)
    GPIO.output(Pin_Contacto2, False)
    GPIO.output(Pin_Contacto3, False)
    GPIO.output(Pin_Contacto4, False)
    
    GPIO.output(Pin_LED1, False)
    GPIO.output(Pin_LED2, False)

def SalidasTest():
    print('Si todos los leds estan encendidos, ingrese 1, si alguno no enciende, presione 0\n')
    aux=5
    while aux!=1 and aux!=0:
        ContactosON()
        aux=int(input())
    ContactosOFF()
    if aux==1:
        print(Fore.GREEN +"*************")
        print(Fore.GREEN +'Salidas OK  *')
        print(Fore.GREEN +"*************")
        return "OK"
    if aux==0:
        print(Fore.RED +'****************')
        print(Fore.RED +'Salidas ERROR  *')
        print(Fore.RED +'****************')
        return "ERROR"

def EntradasTest():
    timeout=10
    print("Presione el boton 1")
    t0=dt.datetime.now()
    t1=dt.datetime.now()
    aux_dif=0
    while GPIO.input(Pin_IN1):
        dif=int((t1-t0).total_seconds())
        if aux_dif!=dif:
            print(dif)
            aux_dif=dif
        if(dif>=timeout):
            print(Fore.RED +'*************************************')
            print(Fore.RED +'Se ha superado el tiempo de espera  *')
            print(Fore.RED +'*************************************')
            return "ERROR"
        t1=dt.datetime.now()
    print("Presione el boton 2")

    t0=dt.datetime.now()
    t1=dt.datetime.now()
    dif=int((t1-t0).total_seconds())
    aux_dif=0
    while GPIO.input(Pin_IN2):
        dif=int((t1-t0).total_seconds())
        if aux_dif!=dif:
            print(dif)
            aux_dif=dif
        if(dif>=timeout):
            print(Fore.RED +'*************************************')
            print(Fore.RED +'Se ha superado el tiempo de espera  *')
            print(Fore.RED +'*************************************')
            return "ERROR"
        t1=dt.datetime.now()
    print(Fore.GREEN +"**************")
    print(Fore.GREEN +'Entradas OK  *')
    print(Fore.GREEN +"**************")
    return "OK"


def SerialTest():
    # Enable Serial Communication
    port = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=1)
    port.flushInput()
    msg='Test'
    port.write(msg)
    rcv = port.readline()
    print(rcv)
    if rcv == "Test":
        print(Fore.GREEN +"******************")
        print(Fore.GREEN +"Puerto Serie OK  *")
        print(Fore.GREEN +"******************")
        return "OK"
    else:
        print(Fore.RED +"*********************")
        print(Fore.RED +"Puerto Serie ERROR  *")
        print(Fore.RED +"*********************")
        return "ERROR"


def WiegandTest():
    timeout=10
    print("Testeando Wiegand...")
    t0=dt.datetime.now()
    t1=dt.datetime.now()
    while True:
        dif=int((t1-t0).total_seconds())
        if(dif>=timeout):
            print(Fore.RED +"****************")
            print(Fore.RED +"Wiegand ERROR  *")
            print(Fore.RED +"****************")
            return "ERROR"
        rdm_msg=randrange(10)
        hilo1 = threading.Thread(target=SendWiegand(rdm_msg))
        hilo2 = threading.Thread(target=Receiver.ReadWiegand())
        hilo1.start()
        hilo2.start()
        if Receiver.num_IN==rdm_msg:
            print(Fore.GREEN +"*************")
            print(Fore.GREEN +"Wiegand OK  *")
            print(Fore.GREEN +"*************")
            return "OK"
        t1=dt.datetime.now()



while 1:

    if StatusSalida=="OK" and StatusEntradas=="OK" and StatusSerial=="OK" and StatusWiegand=="OK":
        print(Style.BRIGHT + Fore.GREEN + "******** Todo funciona OK, Proceso Finalizado ********")
        break

    time.sleep(1)
    print("\n\n")
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    print("Ingrese el numero que desea testear:\n")
    if StatusSalida=="Sin Testear":
        print("1) Salidas \n")
    if StatusSalida=="OK":
        print(Fore.GREEN + "1) Salidas \n")
    if StatusSalida=="ERROR":
        print(Fore.RED + "1) Salidas \n")


    if StatusEntradas=="Sin Testear":
        print("2) Entradas\n")
    if StatusEntradas=="OK":
        print(Fore.GREEN + "2) Entradas\n")
    if StatusEntradas=="ERROR":
        print(Fore.RED + "2) Entradas\n")

    if StatusSerial=="Sin Testear":
        print("3) Serial\n")
    if StatusSerial=="OK":
        print(Fore.GREEN + "3) Serial\n")
    if StatusSerial=="ERROR":
        print(Fore.RED + "3) Serial\n")

    if StatusWiegand=="Sin Testear":
        print("4) Wiegand\n")
    if StatusWiegand=="OK":
        print(Fore.GREEN + "4) Wiegand\n")
    if StatusWiegand=="ERROR":
        print(Fore.RED + "4) Wiegand\n")


    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")

    print("\n\n")

    Test=int(input())
    if Test==1:
        StatusSalida = SalidasTest()
    if Test==2:
        StatusEntradas = EntradasTest()
    if Test==3:
        StatusSerial = SerialTest()
    if Test==4:
        StatusWiegand = WiegandTest()

