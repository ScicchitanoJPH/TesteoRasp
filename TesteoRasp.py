import colorama
import RPi.GPIO as GPIO
import time
import datetime as dt
from colorama import Fore , Style
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

colorama.init(autoreset=True)

msg=0

StatusSalida="Sin Testear"
StatusEntradas="Sin Testear"

#Bornera de salida
Pin_Contacto1=5
Pin_Contacto2=6
Pin_Contacto3=26
Pin_Contacto4=16
#Pin_Contacto5=27
#Pin_Contacto6=17
#Pin_Contacto7=24
#Pin_Contacto8=23

#Pines
Pin_LED1=13
Pin_LED2=19
#Pin_LED3=12

#Bornera de entrada
Pin_IN1=21
Pin_IN2=20



#Seteo de pines
GPIO.setup(Pin_Contacto1, GPIO.OUT)
GPIO.setup(Pin_Contacto2, GPIO.OUT)
GPIO.setup(Pin_Contacto3, GPIO.OUT)
GPIO.setup(Pin_Contacto4, GPIO.OUT)
#GPIO.setup(Pin_Contacto5, GPIO.OUT)
#GPIO.setup(Pin_Contacto6, GPIO.OUT)
#GPIO.setup(Pin_Contacto7, GPIO.OUT)
#GPIO.setup(Pin_Contacto8, GPIO.OUT)

GPIO.setup(Pin_LED1, GPIO.OUT)
GPIO.setup(Pin_LED2, GPIO.OUT)
#GPIO.setup(Pin_LED3, GPIO.OUT)

GPIO.setup(Pin_IN1, GPIO.IN)
GPIO.setup(Pin_IN2, GPIO.IN)



# Activo todas las salidas
def ContactosON():
    GPIO.output(Pin_Contacto1, True)
    GPIO.output(Pin_Contacto2, True)
    GPIO.output(Pin_Contacto3, True)
    GPIO.output(Pin_Contacto4, True)
    #GPIO.output(Pin_Contacto5, True)
    #GPIO.output(Pin_Contacto6, True)
    #GPIO.output(Pin_Contacto7, True)
    #GPIO.output(Pin_Contacto8, True)
    
    GPIO.output(Pin_LED1, True)
    GPIO.output(Pin_LED2, True)
    #GPIO.output(Pin_LED3, True)

def ContactosOFF():
    GPIO.output(Pin_Contacto1, False)
    GPIO.output(Pin_Contacto2, False)
    GPIO.output(Pin_Contacto3, False)
    GPIO.output(Pin_Contacto4, False)
    #GPIO.output(Pin_Contacto5, False)
    #GPIO.output(Pin_Contacto6, False)
    #GPIO.output(Pin_Contacto7, False)
    #GPIO.output(Pin_Contacto8, False)
    
    GPIO.output(Pin_LED1, False)
    GPIO.output(Pin_LED2, False)
    #GPIO.output(Pin_LED3, False)

def SalidasTest():
    print('Verifique que todos los contactores y leds esten encendidos\n')
    print('Si todos estan encendidos, ingrese 1, si alguno no enciende, presione 0\n')
    aux=5
    while aux!=1 and aux!=0:
        ContactosON()
        aux=int(input())
    ContactosOFF()
    if aux==1:
        print(Fore.GREEN +'Las salidas funcionan OK')
        return "OK"
    if aux==0:
        print(Fore.RED +'ERROR en las salidas')
        return "ERROR"

def EntradasTest():
    timeout=10
    print("La entrada 1 esta escuchando, ponga el pin 21 a 3.3V por al menos menos un segundo")
    t0=dt.datetime.now()
    t1=dt.datetime.now()
    aux_dif=0
    while GPIO.input(Pin_IN1):
        dif=int((t1-t0).total_seconds())
        if aux_dif!=dif:
            print(dif)
            aux_dif=dif
        if(dif>=timeout):
            print(Fore.RED +'Se ha superado el tiempo de espera')
            return "ERROR"
        t1=dt.datetime.now()
    print("La entrada 2 esta escuchando, ponga el pin 20 a 3.3V por al menos menos un segundo")

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
            print('Se ha superado el tiempo de espera')
            return "ERROR"
        t1=dt.datetime.now()
    return "OK"

while 1:

    if StatusSalida=="OK" and StatusEntradas=="OK":
        print(Style.BRIGHT + Fore.GREEN + "******** Todo funciona OK, Proceso Finalizado ********")

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

    Test=int(input())
    if Test==1:
        StatusSalida = SalidasTest()
    if Test==2:
        StatusEntradas = EntradasTest()

