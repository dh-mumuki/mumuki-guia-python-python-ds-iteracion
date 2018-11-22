#### Iterando una lista de elementos

Para iterar sobre una lista, vamos a hacer un llamado al `for`, la sintaxis para utilizar el `for` es la siguiente:

``` python
mi_lista = [1, 2, 3, 5]

for numero in mi_lista:
  print(numero)
```
 _Salida:_
**>1** 

**>2** 
 
**>3** 

**>5** 

En este `for` iteramos sobre una lista (mi_lista), para cada iteración asignamos uno a uno los valores contenidos en la lista a la variable numero e imprimimos el valor asignado.

Dentro de la iteración también es posible redefinir el valor que toma la varible definida en el `for`, veamos este código:

``` python
mi_lista = [1, 2, 3, 5]

for numero in mi_lista:
  numero = numero + 10
  print(numero)
```
 _Salida:_
**>11** 

**>12** 
 
**>13** 

**>15** 

Acá tomamos cada elemento de la lista y se lo asignamos a la variable numero. Una vez dentro del cuerpo del for, sumamos la variable **numero** con 10, y reasignamos el valor **numero** con el resultado de esta operación.

Vemos las dos primeras iteraciones:
  
  *  iter1: asigno valor 1 a numero -> (numero vale 1)
  *  iter1: reasigno (10 + numero) a numero -> (numero vale 11)
  *  iter1: imprimo numero
  *  iter2: asigno valor 2 a numero -> (numero vale 2)
  *  iter2: reasigno (10 + numero) a numero -> (numero vale 12)
  *  iter2: imprimo numero


**Qué imprime este código?**

``` python
for i in [4, 1, 3]:
  print(i)
```

