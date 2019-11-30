#!/user/bin/python
import spidev
from time import sleep
import os
from gpiozero import Servo
from gpiozero import LED
from time import sleep

#motor = LED(19)
#motor1 = LED(26)
servo = Servo(19)
#Abrimos el bus SPI
spi = spidev.SpiDev()#declaramos el objeto 
spi.open(0,0)#SPIO
spi.max_speed_hz= 1000000#declaramos la velocidad de trasnmision 1Mhz

        
def leercanal(canal):#recuerda que hablamos del canal del integrado
    adc = spi.xfer2([1, (8+canal)<<4,0]) 
    data = ((adc[1]&3) << 8) + adc[2]
    return data

def conversionvolts(data, digitos):
    volts = (data * 3.3) / float(1023)#calculo de las muestras
    volts = round(volts,digitos)#aplicamos el método para redondear
    return volts

#def movimiento(sensor_indice, sensor_medio, sensor_anular):
def sensor_pull(sensor_pulgar):
    if(sensor_pulgar < 710 or sensor_pulgar > 770):
        print('-Flexionado sensor pulgar')
    
def sensor_ind(sensor_indice):
    if(sensor_indice < 851 or sensor_indice > 900):
        print('-Flexionado sensor indice')
        servo.max()
        sleep(1)
    elif(sensor_indice < 801 or sensor_indice > 850):
        servo.mid()
        sleep(1)
    elif(sensor_indice < 750 or sensor_indice > 800):
        servo.min()
        sleep(1)

def sensor_mid(sensor_medio):
    if(sensor_medio < 700 or sensor_medio > 800):
        
        print('-Flexionado sensor medio')
    
def sensor_anu(sensor_anular):
    if(sensor_anular < 700 or sensor_anular > 800):
        print('  -Flexionado sensor anular')
        
def sensor_men(sensor_menique):
    if(sensor_menique < 700 or sensor_menique > 800):
        print('-Flexionado sensor meñique')
      


while True:
    
    sensor_pulgar=leercanal(0)#en el canal 2 de 8 esta el flex para el dedo anular
        
    sensor_indice=leercanal(1)#en el canal 0 de 8 esta el flex para el dedo anular

    sensor_medio=leercanal(2)#en el canal 1 de 8 esta el flex para el dedo anular
     
    sensor_anular=leercanal(3)#en el canal 2 de 8 esta el flex para el dedo anular
    
    sensor_menique=leercanal(4)#en el canal 2 de 8 esta el flex para el dedo anular
    
    #movimiento(sensor_indice, sensor_medio, sensor_anular)#indica cual se está moviendo.
    sensor_anu(sensor_anular)
    sensor_mid(sensor_medio)
    sensor_ind(sensor_indice)

    print('_____________________________________________________________________________________________________________________')
    print("sensor pulgar {} bits | Sensor indice {} bits | Sensor medio {} bits | Sensor anular {} bits |sensor meñique {} bits |".format (sensor_pulgar, sensor_indice, sensor_medio, sensor_anular,sensor_menique))
    #print("sensor medio volt's {} V {} bits".format (sensor_medio_v,sensor_medio )) print("sensor anular volt's {} V {} bits".format (sensor_anular_v,sensor_anular ))#adc=convertidor analogico digital
    sleep(0.25)