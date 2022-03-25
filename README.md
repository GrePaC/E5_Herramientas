# EQUIPO 5 HERRAMIENTAS
### SEMANA TEC Herramientas computacionales

Integrantes
* Demian Marín Martínez A01368643
* Carolina Arratia Camacho A01367552
* Luis Felipe Depardon Jaso A01770043
* Grecia Pacheco Castellanos A01366730

## INTRODUCCIÓN
Durante la semana tec llamada "Herramientas computacionales: el arte de la programación" se exploraron diversas tecnologías como el uso de comandos dentro de linux para el manejo de directorios, la manipulación de archivos multimedia, y el manejo de archivos de python con diversos propósitos.
Como parte del reto de la semana se tenía la manipulación de imágenes con distintos tipos de Kernel, lo cual se puede de visualizar en el presente proyecto. 

### Objetivo
El objetivo de la actividad es tener conocimiento sobre las herramientas de procesamiento de imágenes. Conocer conceptos como convolución y kernel, así como su aplicación. Se busca lograr aplicar diferentes kernel a una imagen para observar el cambio que se presentan en estas; con esto se puede comprender la manera en la que esto nos puede servir como base para el análisis de imágenes. 

## Computer Science Tools: Creación Repo Virtual

Para la integración del proyecto final se realizó un repositorio de GitHub identificado con el nombre del equipo "E5_Herramientas", donde cada uno de los integrantes tenía una branch para realizar los cambios, por lo que cada uno subió sus respectivos kernels a excepción de Grecia que fue el archivo .py tomado como main ya que contenía la implementacción de el kernel del "sombrero mexicano" (Ricker wavelet).

En el archivo principal denominado "convolution_e5_herramientas_main.py" se importaron el resto de los kernels contenidos en "demianKernel.py", "funcion_LF" y "kernel_Caro.py" para poder obtener la imagen de esa manera en una única graficación.

El poder tener las diversas ramas en github y crear las "pull request" nos permitía tener un control acerca de las versiones del proyecto para realizar únicamente las modificaciones deseadas dentro de la versión entregable del mismo.

## CONVOLUCIÓN

Con la actividad se pudo entender como la convolución es un proceso matemático entre 2 funciones que crean una tercera. En procesamiento de imágenes esto sucede al pasar por cada píxel de una imagen para realizar cálculos con el píxel y los píxeles cercanos. 

Así mismo, durante la actividad se usaron kernels que desde el punto de vista del área de visión computacional es una matriz que se utilizará para hacer un tipo de convolución en nuestros datos. El kernel define el tamaño, peso y anchor de nuestra convolución.

Con esto en mente cada uno de los integrantes del equipo realizó una implementación de determinado kernel, dentro de los que encontramos:

* Demian’s kernel
* Sharpen kernel
* Caro's kernel
* Exponencial kernel
* Gauss kernel
* Mexican hat kernel

A continuación se presentará una explicación del funcionamiento de cada uno de ellos.
 
### Demian’s kernel

Esta función genera un kernel de 3x3 con la función f(x)=x*y, dando como resultado:

![kernel1](https://drive.google.com/uc?id=1jQ-IrkqksjKupg9b24Zv19byS8rZddh)


Al hacer la convolución la imagen original se ve de la siguiente manera:

![kernelDemian](https://drive.google.com/uc?id=16HyU7OQKrWdz3fV4P0MjwZ7oxIcvIXOW)


### Sharpen kernel

Consiste en una matriz 3x3 con los valores mostrados en la siguiente imagen :

![kernel2](https://drive.google.com/uc?id=1hUrhFv6vUofRi8YrMwsj071RD7Q3HE0I)


Lo cual nos dió como resultado en la imagen:

![sharpen](https://drive.google.com/uc?id=19zwcurOJHM6ZaGnJjjfse_O8RtEQ85EM)


### Caro's kernel

El kernel se genera con la función sin_func y esta  llena una matriz 3x3 con la función f(x,y)=sin(x)+y: de la siguiente manera:

![kernel3](https://drive.google.com/uc?id=1vEBWWmvI360viUHPycuSQVq3YSpigblZ)

Lo que procesa la imagen como se muestra a continuación:

![sin_func](https://drive.google.com/uc?id=1l8z3YdlL4oeJvy-7K0XwUvATOjeTOVch)

### Exponencial kernel

Se realizó la implementación como se vió  en clase donde la imagen se transforma a borroso como se muestra en la imagen:

![exp](https://drive.google.com/uc?id=1-ZNlXaafzUL08sh7kkfKjOmUwARBqrOe)



### Gauss kernel

Implementación usando la función que modela la campana de Gauss, tal como el exponencial kernel descrito anteriormente

![exp](https://drive.google.com/uc?id=1uhRqKk-OtYDOIgO0QPS8BCkSq37FTDiT)


### Mexican hat kernel

En este kernel se está modelando con la función comúnmente identificada como "sombrero mexicano" o formalmente "ricker wavelet" que ayuda a identificar los bordes más nítidos de la imagen, tal como se muestra a continuación.

![exp](https://drive.google.com/uc?id=1iLfgrGNlCLHWdpDUvkZm9gQlWiBhfnRW)

