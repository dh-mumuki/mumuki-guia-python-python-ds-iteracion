En muchos programas se necesitan variables que cuenten cuántas veces ha ocurrido algo (contadores) o que acumulen valores (acumuladores). Las situaciones pueden ser muy diversas, por lo que simplemente hay aquí un par de ejemplos para mostrar la idea.<br>

**Contador**<br>
Se entiende por contador una variable que lleva la cuenta del número de veces que se ha cumplido una condición. El ejemplo siguiente es un ejemplo de programa con contador (en este caso, la variable que hace de contador es la variable `contador`)::<br>

``` python
contador = 0
for i in range(1, 6):
    contador = contador + 1
print(f"Desde 1 hasta 5 hay {cuenta} múltiplos de 2")
```

 _Salida:_
**La suma de los números de 1 a 4 es 10**
<br>

**Detalles importantes:**

* En cada iteración, el programa comprueba si i es múltiplo de 2.
* El contador se modifica sólo si la variable de control i es múltiplo de 2.
* El contador va aumentando de uno en uno.
* Antes del bucle se debe dar un valor inicial al contador (en este caso, 0)


> Python permite escribir `contador += 1` en lugar de `contador = contador + 1` 

<br>

**Dada la siguiente lista, escribir un código que sume todos los elementos de una lista y luego imprima el resutlado**<br>
`lista = [2, 5, 4, 8, 9, 3, 5 , 6]`

