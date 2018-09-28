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
