Se entiende por acumulador a aquella variable a la que se le va sumando el resultado de una operación.<br>

``` python
sumatoria = 0
for i in [1, 2, 3, 4]:
    sumatoria += i
print("La suma de los números de 1 a 4 es " + sumatoria)
```
<br>

**Detalles importantes:**

* El acumulador se modifica en cada iteración del bucle (en este caso, el valor de i se añade al acumulador suma).
* Antes del bucle se debe dar un valor inicial al acumulador (en este caso, 0)

<br>

:memo:**Escriba un código que sume los los elementos de una lista de números en una variable llamada `sumatoria`.**
