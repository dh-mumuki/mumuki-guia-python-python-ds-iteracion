En muchos programas se necesitan variables que cuenten cuántas veces ha ocurrido algo. A estas variables se las llama **contadores**.<br>
¿Cómo hacemos para contar los elementos de una lista?

``` python
contador = 0

for i in [1, 2, 3, 4, 5, 6]:
    contador = contador + 1

print(contador)
> 6
```

**Para tener en cuenta:**

* Antes del bucle, se debe dar un valor inicial cero al contador.
* En cada iteración, el contador va aumentando de uno en uno, hasta que se termine de recorrer toda la lista.

> ¡Te dejamos un truquito! :wink: <br>
Python permite escribir `contador += 1` en lugar de `contador = contador + 1` 

Veamos si se entendió:

> :memo: **Escribí un código que cuente todos los elementos de la siguiente lista:**
`lista = [2, 5, 4, 8, 9, 3, 5, 6]`
