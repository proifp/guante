#Calibrar sensor
#print('sensor flexionado')
import spidev
from time import sleep
import os


#Abrimos el bus SPI
spi = spidev.SpiDev()#declaramos el objeto 
spi.open(0,0)#SPIO
spi.max_speed_hz= 1000000#declaramos la velocidad de trasnmision 1Mhz

def leercanal(canal):#recuerda que hablamos del canal del integrado
    adc = spi.xfer2([1, (8+canal)<<4,0]) 
    data = ((adc[1]&3) << 8) + adc[2]
    return data
cont = 0
while True:
    
    sensor_pulgar=leercanal(0)#en el canal 2 de 8 esta el flex para el dedo anular
        

for i in range(10):
    pos_inicial=sensor_pulgar
    
    cont+=sensorpulgar
print(cont/10)    

#def leer_pos_sensor_pulgar(sensor_pulgar):
 #   pos_inicial=sensor_pulgar
    