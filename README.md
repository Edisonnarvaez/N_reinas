Integrantes: Edison Stiven Navaez y Marino Botina

1. ¿Qué es el problema de las N-Reinas? Explica su formulación y la restricción principal que debe cumplirse en una solución?

Respuesta: El problema de las N-Reinas consiste en colocar N reinas en un tablero de ajedrez NxN de manera que ninguna reina pueda atacar a otra. En ajedrez, una reina puede atacar en horizontal, vertical y diagonal. La formulación típica usa una representación donde cada reina se coloca en una columna diferente, y el objetivo es asignar una fila a cada columna (un vector de tamaño N) tal que no haya conflictos.

La restricción principal es que no debe haber dos reinas en la misma fila, columna o diagonal. En la representación como vector (donde el índice es la columna y el valor es la fila), ya se garantiza que no hay reinas en la misma columna ni fila, por lo que el foco está en evitar conflictos diagonales.

2. ¿Qué características tiene un algoritmo evolutivo? Explica cada uno de sus componentes básicos (población, selección, cruzamiento, mutación, evaluación).

Un algoritmo evolutivo (AE) es un método de optimización inspirado en la evolución biológica. Sus componentes básicos son:

Población: Conjunto de posibles soluciones (individuos) al problema. En este caso, cada individuo será un vector representando una configuración de N reinas.
Selección: Proceso para elegir individuos "aptos" que generarán la próxima generación. Favorece a los mejores según su aptitud.
Cruzamiento (crossover): Combina dos individuos (padres) para crear descendientes, mezclando sus características. Por ejemplo, intercambiar partes de dos vectores.
Mutación: Introduce cambios aleatorios en un individuo para mantener diversidad. Por ejemplo, cambiar la fila de una reina en el vector.
Evaluación: Calcula la aptitud (fitness) de cada individuo para medir qué tan buena es la solución. Aquí, evaluaremos conflictos entre reinas.

3.En un algoritmo evolutivo, ¿por qué es importante la función de aptitud (fitness function) y cómo se podría definir para este problema?

La función de aptitud es crucial porque guía la evolución, indicando qué individuos son mejores. Para las N-Reinas, podemos definirla como el número de pares de reinas en conflicto (ataques mutuos). Una solución óptima tiene fitness = 0 (sin conflictos). Por ejemplo, para cada par de reinas, verificamos si están en la misma diagonal calculando si la diferencia absoluta de sus columnas es igual a la de sus filas: |col1 - col2| = |fila1 - fila2|.

4.¿Qué métodos de selección existen en los algoritmos evolutivos? Explica cómo funciona la selección por torneo y la selección proporcional a la aptitud (ruleta).

Métodos comunes incluyen:
Selección por torneo: Se eligen k individuos al azar, y el mejor (menor fitness en este caso) "gana". Es simple y controla la presión selectiva ajustando k.

Selección proporcional a la aptitud (ruleta): Cada individuo tiene una probabilidad de ser elegido proporcional a su aptitud. Para un problema de minimización como este, se invierte el fitness (ej. 1/(1 + conflictos)) para que los mejores tengan mayor probabilidad.

Otros métodos incluyen selección elitista (conservar los mejores directamente) o selección por rango.

En términos de mutación, ¿qué métodos pueden aplicarse a la representación del problema de las N-Reinas? ¿Earliesto en tu intuitive para encontrar una solución?

Para un vector de N-Reinas:

Mutación por intercambio: Intercambiar las filas de dos posiciones aleatorias en el vector.
Mutación por desplazamiento: Cambiar el valor (fila) de una posición a un número aleatorio entre 0 y N-1.

Mi intuición sugiere que la mutación por desplazamiento es más efectiva, ya que ajusta posiciones individuales para reducir conflictos diagonales, mientras que el intercambio podría ser más disruptivo pero útil para escapar de óptimos locales.

Parte 2: Implementación del Algoritmo Evolutivo

https://github.com/Edisonnarvaez/N_reinas.git

Parte 3: Preguntas de análisis

1. ¿Cuántas generaciones fueron necesarias para N=6, N=8? ¿Cómo varía con el tamaño de la población?

Corre el código con n=6 y n=8, y prueba population_size = 50, 100, 200. Generalmente, más población reduce generaciones porque hay más diversidad, pero aumenta el costo computacional.

2. ¿Cómo influye la tasa de mutación en la convergencia?

Prueba 0.05, 0.1, 0.2.
Corre el código con mutation_rate = 0.05, 0.1, 0.2. Una tasa baja (0.05) puede converger lentamente o estancarse; una alta (0.2) introduce más exploración pero puede desestabilizar buenas soluciones. 0.1 suele ser un balance.

3. ¿Diferencia entre búsqueda aleatoria y enfoque evolutivo?

La búsqueda aleatoria genera soluciones sin aprendizaje (fitness constante alto). 
El enfoque evolutivo mejora progresivamente el fitness gracias a selección y cruzamiento. Compara generaciones y fitness final.
4. ¿Cómo mejorar la eficiencia sin aumentar generaciones?

Usar selección elitista (mantener el mejor individuo).
Optimizar la función de aptitud con cálculos más rápidos.
Ajustar el tamaño del torneo o usar cruzamiento multipunto.
