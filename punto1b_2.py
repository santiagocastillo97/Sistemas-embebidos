#Se importa la libreria RPi.GPIO
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.OUT)#Se inicializa el GPIO18 como salida

try:
    while True:#bucle infinito
        GPIO.output(18, True)#se sube el GPIO18
        GPIO.output(18, False)#e baja el GPIO18
except KeyboardInterrupt:#Interrupción por teclado
    pass
GPIO.cleanup()