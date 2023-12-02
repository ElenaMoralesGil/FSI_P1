# practicas-FSI
*Elena Morales Gil*

*Nelson Cabrera Cano*

# PRACTICA  1 

## Explicación del código  


### Run.py 



Contiene el código principal, encargado de coordinar y ejecutar todas las pruebas. La hemos hecho configurable, conteniendo al inicio unas constantes modificables, los algoritmos y problemas a comprobar. Pudiendo cambiar cualquiera de estas constantes a nuestro gusto; para el caso de los algoritmos y problemas bastaría con comentar aquello que no queramos que se ejecute. 

Las constantes **SHOW_TERMINAL** y **SHOW_PLOT** administran que haya salida por consola y que se muestre el gráfico de las comparaciones de tiempo, respectivamente. 

La contante **TEST_REPEAT** determina el número de veces que se ejecutará cada algoritmo con cada problema (luego se hará media) para así tener una estimación más acertada de la medida de tiempo. 

La función **test_problem** es la encargada de testear cada problema con cada uno de los algoritmos, haciendo un sumatorio de los tiempos de ejecución de cada uno de los algoritmos. 

La función **test_search** es la encargada de, con un algoritmo y un problema dados, ejecutar el número de veces configurado, sacar la media mostrar los resultados por pantalla. 

El flujo principal de la aplicación es el siguiente: 

* Por cada problema, testeamos cada uno de los algoritmos. 
* Calculamos la media de los tiempos. 
* Si esta activado, se muestra una gráfica con las medias de los tiempos para cada uno de los algoritmos. 
* Se ha optado por usar picosegundos, ya que los resultados son de ese orden, y así tenemos más claridad. 

### Plot.py 

Módulo que provee una función para facilitar la creación de la gráfica. 


### Search.py 

 

Modificamos el metodo **graph_search** para que cuente el número de nodos visitados, generados y expandidos. Además de darle la opción de que se impriman los resultados todos los tests de run mediante la variable show. 

También añadimos 2 funciones, **branch_and_bound_graph_search** y **heuristic_graph_search**, las cuales se encargan de llamar a la función de búsqueda con los parámetros correspondientes. 

Se ha modificado ligeramente el método encargado de la búsqueda para permitir controlar la salida por consola. 

 

### Utils.py 

 

Creamos 2 clases, las cuales servirán para representar cómo funciona las funciones de append y extend de Branch and Bound y Heuristic Branch and Bound.  

En ambas heredamos de FIFOQueue ya que ambas funcionan como una cola, pero con la característica de que esta ordenada. 

En la clase  **Branch_and_bound** ordenamos la lista por coste acumulado utilizando la función sorted. Tanto para el append como el extend, aunque sabemos que en el append no es necesario, pero creemos que no es dañino. 

Y en **HeuristiMethod** hacemos lo mismo, pero ordenándolo por la suma del coste acumulado y la heurística para los mismos métodos que el Branch and Bound. 

 

## Dificultades 

No hemos encontrado ninguna dificultad con esta práctica.  
