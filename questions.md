
# Pasos necesarios para entrenar un modelo de detección con categorías no existentes en los modelos preentrenados.

## 1. Pasos a seguir
### Seleccionamos un pre-trained model
Elegimos un modelo pre-entrenado que se ajuste a nuestros requisitos de tarea y arquitectura. 

### Preparamos el dataset de entrenamiento
Recolectamos y preparamos nuestro conjunto de datos. Nos aseguramos de que esté etiquetado y dividido en conjuntos de entrenamiento, validación y prueba.

El tamaño de nuestro conjunto de datos influye en la medida en que podemos ajustar finamente el modelo. Cuanto mayor sea, y más equilibradas estén las categorías, mejor podremos hacer el fine-tunning y evitar overfitting, o desbalance de datos.

### Hacemos el preprocesamiento de datos
En este caso, podemos normalizar los valores de píxeles y redimensionar imágenes.

### Modificamos la Output layer
Reemplazamos la output layer del modelo pre-entrenado con una nueva que se adapte a nuestra tarea específica. 

El número de neuronas en la capa de salida debe coincidir con el número de clases en nuestro conjunto de datos.

### Definimos una loss function
Elegimos una función de pérdida apropiada para nuestra tarea específica. Por ejemplo, para tareas de clasificación, típicamente se usa cross-entropy.

### Ajustamos los parámetros del fine-tuning
Establecemos hiperparámetros como learning rate, batch size y epochs. Pueden necesitar ajustarse según nuestro conjunto de datos y tarea.

### Hacemos el fine-tuning
Entrenamos el modelo con los datos nuevos y la loss function definida. Supervisamos el rendimiento en el conjunto de validación para evitar el overfitting.

### Evaluamos y Ajustamos
Evaluamos el modelo fine-tuneado con el conjunto de test.

Si es necesario, iteramos y ajustamos hiperparámetros o aumentamos el conjunto de datos para obtener un mejor rendimiento.


## Problemas que puedan surgir y medidas para reducir el riesgo

Problemas que podríamos encontrarnos:

### Data inbalance
Las nuevas categorías no tienen suficientes muestras de datos para que el entrenamiento sea efectivo, lo que lleva a un conjunto de datos desbalanceados. Esto puede hacer que las predicciones estén sesgadas hacia las clases mayoritarias y tener un mal rendimiento para las clases minoritarias

### Overfitting
Hacer fine-tuning en un dataset pequeño con nuevas categorías podría llevar a overfitting, de forma que el modelo se especializa en los datos de entrenamiento en lugar de generalizar.

Formas de mitigar esos problemas:

### Aumento de datos
Generando datos sintéticos para disminuir el desbalance de datos y ampliar el conjunto de datos de entrenamiento. Usando técnicas como data synthesis, oversampling, etc.

### Transfer learning
Usando un modelo pre-entrenado cuyos datos de entrenamiento sean lo suficientemente numerosos y diversos puede hacer que el fine-tuning sea más efectivo.

## Estimación de la cantidad de datos necesarios y resultados de métricas esperados.

La cantidad de datos que necesitemos va a variar mucho en función de:
- El tipo de categorias para los que queremos especializarnos. Si son más complejas y requieren más características distintivas, necesitaremos más datos para obtener buenas métricas.
- La calidad de los datos. Cuanto más diversos sean nuestros datos y de mayor calidad, más podrá generalizar el modelo y necesitaremos menos datos para obtener buenas métricas.
- La capacidad del modelo base. Si partimos de un modelo de muchos parámetros, es posible que necesitemos más datos.

En cuanto a métricas, podemos fijarnos en el accuracy, f1-score, etc. para evaluar el rendimiento. 

- Accuracy: proporción de predicciones correctas respecto a las totales. Puede no ser muy representativo para datasets desbalanceados

- f1-score: Media armónica de precisión y recall. Considera falsos positivos y falsos negativos. Calcularíamos el f1-score de cada clase individualmente y tomaríamos la media.

## Técnicas para mejorar el despempeño, métricas en entrenamiento y métricas en inferencia

Para mejorar las métricas en el entrenamiento, a parte de las técnicas ya mencionadas, podemos:

- Optimizar hiperparámetros, con técnicas como grid search, random search, bayesian optimization, etc. con el objetivo de probar distintas conmbinaciones de hiperparámetros y ver con cuáles obtenemos mejores métricas.

- Reducir dimensionalidad, con técnicas como PCA para reducir la dimensionalidad de los datos y eliminar características irrelevantes o redundantes.

- Hacer freeze the las capas Pre-entrenadas. Podemos hacer freeze de algunas de las capas iniciales del modelo pre-entrenado. Esto es especialmente útil cuando nuestro conjunto de datos es pequeño, ya que evita que el modelo olvide lo que aprendió durante el pre-entrenamiento.

Para mejorar el desempeño en la inferencia, podemos:

- Optimización de Modelos: Utilizar técnicas de compresión y optimización de modelos para reducir el tamaño y la complejidad del modelo, lo que puede mejorar la velocidad de inferencia y reducir el uso de recursos computacionales.

- Pruning: Aplicar técnicas de poda (pruning) para eliminar conexiones o neuronas menos importantes del modelo, reduciendo así su tamaño y complejidad sin comprometer significativamente el rendimiento.

- Inferencia por Lotes (Batch Inference): Realizar inferencia en lotes (batch inference) en lugar de hacer predicciones de forma individual, lo que puede aprovechar mejor los recursos computacionales y mejorar la eficiencia de la inferencia.

- Técnicas de Paralelización y Distribución: Implementar técnicas de paralelización y distribución para ejecutar la inferencia en múltiples dispositivos o servidores, lo que puede acelerar significativamente el tiempo de inferencia en aplicaciones de gran escala.
