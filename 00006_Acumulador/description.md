Imaginemos que teemos que sumar los elementos de una lista ¿Cómo hacemos?<br>
Para eso usamos una variable acumuladora a la que le vamos sumando cada elemento de la lista.<br>
Veamos un ejemplo:

``` python
sumatoria = 0

for i in [1, 2, 3, 4]:
    sumatoria += i
    print(sumatoria)
```

**Importantes:**

* Antes del bucle se le asigna cero a lavariable acumuladora.
* En cada iteración se le va sumando a la variable `sumatoria` el valor del elemento.

<br>

> :memo: **Escriba un código que sume los los elementos de una lista de números en una variable llamada `sumatoria`.**