En muchos programas se necesitan variables que cuenten cuántas veces ha ocurrido algo, a estas variables se las llama contadores.
<br>
¿Cómo haríamos para contar los elementos de una lista?

``` python
contador = 0

for i in range(6):
    contador = contador + 1
    print(contador)

ム
> 1
> 2
> 3
> 4
> 5
> 6
```

**Importantes:**
* Antes del bucle se debe dar un valor inicial cero al contador.
* En cada iteración, el contador va aumentando de uno en uno, hasta que se termine de recorrer toda la lista
* De esta forma habremos contado cuántos elementos tiene la lista



> Python permite escribir `contador += 1` en lugar de `contador = contador + 1` 

<br>

:memo: **Dada la siguiente lista, escribir un código que cuente todos los elementos de una lista en una variable llamada contador.**<br>
`lista = [2, 5, 4, 8, 9, 3, 5 , 6]`

