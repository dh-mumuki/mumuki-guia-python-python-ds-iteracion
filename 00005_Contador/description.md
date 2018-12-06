En muchos programas se necesitan variables que cuenten cuántas veces ha ocurrido algo, a estas variables se las llama contadores.
<br>
Veamos algunos ejemplos:
<br>
``` python
contador = 0
for i in range(1, 6):
    contador = contador + 1
print("Desde 1 hasta 5 hay " + contador + "números")

ム
> "Desde 1 hasta 5 hay 2 múltiplos de 2**
```
<br>

**Detalles importantes:**

* En cada iteración, el programa comprueba si i es múltiplo de 2.
* El contador se modifica sólo si la variable de control i es múltiplo de 2.
* El contador va aumentando de uno en uno.
* Antes del bucle se debe dar un valor inicial al contador (en este caso, 0)


> Python permite escribir `contador += 1` en lugar de `contador = contador + 1` 

<br>

:memo: **Dada la siguiente lista, escribir un código que cuente todos los elementos de una lista en una variable llamada contador.**<br>
`lista = [2, 5, 4, 8, 9, 3, 5 , 6]`

