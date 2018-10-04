#### Introducción.

El proceso de recorrer una estructura de datos se conoce como iteración, en términos generales se suele utilizar la iteración para comprobar propiedades sobre los elementos que pertenecen a alguna estructura de datos, ya sea para obtener alguna conclusión general (un estadístico, una propiedad de un sistema, etc), o para seleccionar un subgrupo de estos elementos (filtrar un conjunto de números primos en una lista u obtener el mejor predictor de un conjunto de modelos de machine learning).

#### Uso del `for`.

Para recorrer una estructura de datos, es necesario que tenga la propiedad de ser iterable, tipos iterables podrian ser: una lista, un diccionario, un string, etc.

El llamado al `for` se realiza de la siguiente manera:

``` pyhton
for elemento in algun_iterable:
   cuerpo_del_for
```

Inspeccionemos por separado este enunciado:

  * `for`: es el comienzo de la declaracion del ciclo for.
  * `elemento`: es el nombre de la variable que va a tomar cada valor dentro del `cuerpo_del_for`.
  * `in`: indica la estructura sobre la que queremos iterar.
  * `cuerpo_del_for`: es el código que se ejecuta en cada iteracion.

Para cada ejecución del `cuerpo_del_for` el valor de la variable `elemento` se va modificando.
  

#### Iterando una lista de elementos.

Para iterar sobre una lista, vamos a hacer un llamado al `for`, la sintaxis para utilizar el `for` es la siguiente:

``` pyhton
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

``` pyhton
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

