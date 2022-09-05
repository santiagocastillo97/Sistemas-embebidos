#!/bin/sh 

cd /sys/class/gpio #se accede al directorio gpio

echo "18" > export #se asigna 18 a export
echo "out" > gpio18/direction #se establece GPIO18 como salida

int_handler() { #función interrupción
    echo "\nInterrumpido." 
    kill $PPID 
    exit 1 
} 
trap 'int_handler' INT

while true # bucle infinito
do
	echo 1 > gpio18/value #se sube el GPIO18
	echo 0 > gpio18/value #se baja el GPIO18
done

exit 0