#se importan las librerias necesarias
import os
import glob
import time
import datetime
import csv
import RPi.GPIO as GPIO
from datetime import datetime

#se inicializan variables
fecha=datetime.utcnow()
string_fecha = fecha.strftime('%Y-%m-%d')
Nombre_archivo = string_fecha+"_TEMPERATURA"+".csv"

#se configura la interfaz one-wire
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
 
base_dir = '/sys/bus/w1/devices/'
device_path = glob.glob(base_dir + '28*')[0]

#funcion para leer la temperatura
def read_temp_raw():
    with open(device_path +'/w1_slave','r') as f:
        valid, temp = f.readlines()
    return valid, temp
 
def read_temp():
    valid, temp = read_temp_raw()

    while 'YES' not in valid:
        time.sleep(0.2)
        valid, temp = read_temp_raw()

    pos = temp.index('t=')
    if pos != -1:
        temp_string = temp[pos+2:]
        temp_c = float(temp_string)/1000.0 
        temp_f = temp_c * (9.0 / 5.0) + 32.0
        return temp_c

#se guarda el tiempo de inicio en la variable inicio
inicio = time.time()

try:
    while 1: #bucle infinito
        c = read_temp()#Se lee la temperatura
        Ahora = datetime.utcnow()#Se lee la fecha y hora
        Ahora_string = Ahora.strftime('%Y-%m-%d %H:%M:%S')#se almacena la fecha y hora como string
        TiempoAhora = time.time()#se guarda el tiempo hasta el momento en la variable TiempoAhora
        if (TiempoAhora >= inicio + 10):#se verifica si ya pasaron 10 segundos
            inicio = time.time()#se reinicia la varaible inicio
            datos = [["Fecha y hora", "Temperatura"], #columnas del archivo .csv
                     [Ahora_string, str(c)]]
            archivo = open(Nombre_archivo, 'a', newline="")#se abre el archivo .csv
            with archivo:
                archivo_N = csv.writer(archivo)        
                archivo_N.writerows(datos)#se escriben los datos leídos por el sensor en el archivo .csv
            archivo.close()
            print("\nFecha y hora: "+Ahora_string+" Temperatura: "+str(c))#Se imprimen por consola los datos
except KeyboardInterrupt:#interrupción por teclado
    pass
GPIO.cleanup()