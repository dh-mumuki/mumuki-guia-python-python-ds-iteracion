Imaginemos que tenemos que sumar los elementos de una lista. ¿Cómo podríamos hacer? 🤔 <br>
Para eso, usamos una variable acumuladora a la que le vamos sumando cada elemento de la lista.<br>
Veamos un ejemplo:

``` python
sumatoria = 0

for i in [1, 2, 3, 4]:
    sumatoria += i
    print(sumatoria)
```

**Para tener en cuenta:**

* Antes del bucle, se le asigna cero a la variable acumuladora.
* En cada iteración, se le va sumando a la variable acumuladora el valor de cada elemento.<br>

> :memo: **Escribí un código que sume los los elementos de la siguiente lista: `[2, 5, 4, 8, 9, 3, 5 , 6]` en una variable llamada `sumatoria`.**
