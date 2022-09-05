/*Se importan las librerias*/
#include <pigpio.h>
#include <stdio.h>
#include <unistd.h>


int main(void)
{

   if (gpioInitialise()<0) return 1;

   gpioSetMode(18, PI_OUTPUT); /*Se inicializa el GPIO18 como salida */

   while (1) { /*bucle infinito*/
      gpioWrite(18, 1); /*Se sube el GPIO18*/
      gpioWrite(18, 0); /*Se baja el GPIO18*/
    }

   gpioTerminate();
}