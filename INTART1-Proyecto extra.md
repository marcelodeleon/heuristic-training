# Inteligencia Artificial 1

Este es el planteo del proyecto extra individual del curso de [_Inteligencia Artificial 1_](https://webasignatura.ucu.edu.uy/course/view.php?id=7484) del primer semestre de 2018, para las carreras de [Licenciatura](https://carreras.ucu.edu.uy/index.php/carreras/ingenieria-y-tecnologias/informatica-lic) e [Ingeniería en Informática](https://carreras.ucu.edu.uy/index.php/carreras/ingenieria-y-tecnologias/ingenieria-en-informatica) de la [UCU](http://ucu.edu.uy), a cargo de los docentes [Agustín Castillo](mailto:agustin.castillo@ucu.edu.uy) y [Leonardo Val](mailto:lval@ucu.edu.uy).

Este proyecto no es obligatorio. Los estudiantes pueden realizarlo para ganar puntos extra para aprobar el curso. Las entregas que se calificarán serán aquellas hechas por estudiantes cuyo promedio de calificaciones sea insuficiente para aprobar el curso.

## Planteo

En la unidad temática de búsqueda con heurísticas se realizó un trabajo con el algoritmo [MiniMax](https://en.wikipedia.org/wiki/Minimax#Combinatorial_game_theory). Se trató de la implementación de un jugador artificial para un juego inventado por la cátedra, llamado _Cuantetí_. Dado que dicho agente usaba MiniMax, el problema se resume a plantear una buena función de evaluación heurística para los estados de juego. Lo que se pretende en este trabajo es diseñar y construir un programa que permita ajustar automáticamente una función de evaluación heurística similar.

El estudiante debe primero plantear un modelo de función heurística, cuyos parámetros serán ajustados por un algoritmo de optimización. Luego, debe elegirse una de las metaheurísticas vistas en el curso para optimizar el modelo anterior. Éstas son: _[Hill Climbing](https://en.wikipedia.org/wiki/Hill_climbing)_, _[Simulated Annealing](https://en.wikipedia.org/wiki/Simulated_annealing)_ y _[Algoritmos Genéticos](https://en.wikipedia.org/wiki/Genetic_algorithm)_ (otras variantes de computación evolutiva se pueden elegir también). Por último, debe ejecutarse la optimización y verificar que el jugador MiniMax con la heurística obtenida le gana la mayoría de las veces al jugador aleatorio y al jugador MiniMax con heurística aleatoria.

El proyecto debe programarse en [Python 3](https://www.python.org/). Se espera que los estudiantes reutilicen el código visto y realizado durante el curso.

## Cronograma

El jueves 10 de mayo los estudiantes que deseen realizar este proyecto extra deberán comunicarle a los docentes su intención, indicando su elección de método de optimización. La entrega podrá realizarse hasta el domingo 13 de mayo a las 23 horas.

La entrega debe incluir:

+ todo el código fuente programado y necesario para ejecutar los experimentos, 

+ la bibliografía utilizada,

+ un breve reporte (formato PDF) con un resumen de los datos obtenidos y las conclusiones del trabajo,

La entrega *no* debe incluir:

+ código compilado (e.g. archivos `.pyc`),

+ archivos temporales,

+ archivos de manejo de proyecto, de IDEs o del entorno del sistema operativo.

Las entregas cuyas pruebas no puedan reproducirse (por el motivo que sea) serán calificadas con 0 puntos. El respeto a las normas de entrega forma parte de la calificación final.

