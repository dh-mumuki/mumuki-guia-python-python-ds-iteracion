En los ejemplos anteriores usamos una lista para facilitar la comprensión del funcionamineto de los bucles, pero también podemos utilizar el método `range()`. Esta función devuelve una secuencia de números enteros que inicia en 0 (por defecto) y termina en el valor que indiquemos en el argumento (sin incluir).<br>

Veamos un ejemplo:<br>

``` python
for i in range(6):
  print(i)

ム
> 0
> 1
> 2
> 3
> 4
> 5
```
También podemos utilizar esta función para repetir una instrucción una determinada cantidad de veces, como observamos a continuación:<br>

``` python
for i in range(6):
  print("Hola, Mundo!")

ム
> "Hola, Mundo!"
> "Hola, Mundo!"
> "Hola, Mundo!"
> "Hola, Mundo!"
> "Hola, Mundo!"
> "Hola, Mundo!"
```
<br>
> :memo: **Usá la función `range()` para imprimir por pantalla 4 veces "Python" :snake:**