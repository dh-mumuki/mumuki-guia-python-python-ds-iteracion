Como te contábamos cuando empezaste, prpogramar nos da un gran poder: **nos permite automatizar tareas repetitivas y tediosas.** <br>
¿Y quué quiere decir eso de "repetitivas"? Pensemos, por ejemplo, cómo haríamos si quisieramos repetir 5 veces la misma instrucción e imprimir por pantalla 5 veces la misma variable: <br>

``` python
mejor_lenguaje_de_programacion = "Python"
print (mejor_lenguaje_de_programacion)
print (mejor_lenguaje_de_programacion)
print (mejor_lenguaje_de_programacion)
print (mejor_lenguaje_de_programacion)
print (mejor_lenguaje_de_programacion)

# Esto imprimiría por pantalla 5 veces la variable Python 

```
¿Notás qué es lo que se repite? Sí, estamos haciendo 5 veces lo mismo: imprimir la variable Python. Sin dudas, sería mucho más interesante tener que repetir esta instrucción 5 veces, sino que la computadora hiciera eso por nosotros... :sunglasses:

Entonces ¿Cómo hacemos eso? Te presentamos los bucles 

**Bucle**<br>
Es una estructura de control que repite un bloque de instrucciones. Un bucle `for` es un bucle que repite el bloque de instrucciones un número prederminado de veces. El bloque de instrucciones que se repite se suele llamar cuerpo del bucle y cada repetición se suele llamar iteración.En Python se define de esta manera.<br>

``` python
for variable in elemento iterable (lista, cadena, range, etc.):
    cuerpo bucle

```
<br>
El cuerpo del bucle se ejecuta tantas veces como elementos tenga el elemento recorrible. 
Ahora ya podemos imprimir 5 veces la variable `mejor_lenguaje_de_programacion` sin tener que escribir 5 veces print :wink:


