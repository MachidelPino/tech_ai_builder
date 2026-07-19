# Resumen del curso

El curso profundiza en el diseño de pipelines de **Retrieval-Augmented Generation (RAG)** con LangChain. El recorrido abarca la carga de fuentes heterogéneas, diferentes estrategias de chunking, embeddings, almacenamiento vectorial, modelos locales con Ollama, reescritura de consultas y observabilidad con LangSmith.

El objetivo central es comprender que la calidad de un sistema RAG no depende únicamente del modelo generativo. También está determinada por cómo se preparan los documentos, cómo se representan, qué información recupera el sistema y de qué manera se construye el contexto enviado al modelo.

## Aula 01 — Conceptos sobre RAG

### Arquitectura básica de RAG

Un pipeline RAG combina recuperación de información con generación de texto.

El recorrido general es:

1. cargar una base de conocimiento;
2. dividir los documentos en fragmentos;
3. convertir los fragmentos en embeddings;
4. almacenarlos en una base vectorial;
5. representar la consulta del usuario como un vector;
6. recuperar los fragmentos más similares;
7. incorporarlos al prompt como contexto;
8. generar una respuesta mediante un LLM.

Este enfoque permite obtener respuestas basadas en información específica, en lugar de depender únicamente del conocimiento incorporado durante el entrenamiento del modelo.

### Carga y fragmentación inicial

LangChain ofrece document loaders para convertir archivos en objetos que puedan procesarse dentro del pipeline.

En el ejemplo inicial se utiliza `TextLoader` para cargar documentos de texto. Luego, `RecursiveCharacterTextSplitter` divide el contenido en chunks configurando:

- tamaño máximo del fragmento;
- superposición entre fragmentos;
- separadores utilizados durante la división.

El overlap ayuda a conservar relaciones entre partes del texto que podrían quedar separadas por el límite de un chunk.

### Embeddings y almacenamiento en memoria

Los fragmentos se convierten en embeddings mediante un modelo de Google Generative AI.

El embedding representa semánticamente cada fragmento como un vector numérico. Los documentos pueden almacenarse inicialmente en `InMemoryVectorStore`, una alternativa útil para pruebas rápidas.

A partir del vector store se crea un retriever, encargado de buscar los fragmentos más relacionados con la consulta.

El almacenamiento en memoria es sencillo, pero:

- no conserva los datos al terminar el proceso;
- puede consumir muchos recursos;
- no es apropiado para grandes colecciones;
- obliga a reconstruir el índice en cada ejecución.

### Construcción del prompt

Después de recuperar los fragmentos relevantes, estos se unen para formar el contexto del prompt.

El prompt debe indicar de manera explícita que la respuesta debe construirse utilizando el contexto proporcionado. Una estructura común incluye:

- un mensaje de sistema con las reglas;
- el contexto recuperado;
- la pregunta original;
- instrucciones sobre qué hacer cuando el contexto no es suficiente.

El modelo se configura con una temperatura baja para reducir la variabilidad y favorecer respuestas más concretas.

### Composición de la cadena

LangChain permite componer una cadena con:

1. el prompt;
2. el modelo;
3. un parser de salida.

La consulta y el contexto se pasan como entrada a la cadena. También puede activarse el modo de depuración para inspeccionar los datos que circulan por cada etapa.

### Ambientes virtuales

El ambiente virtual aísla las dependencias del proyecto y evita conflictos con otros proyectos o con la instalación global de Python.

Para este repositorio debe crearse en la raíz de la carpeta del curso:

```text
.venv/
```

La activación depende del sistema y del shell.

#### PowerShell

```powershell
.\.venv\Scripts\Activate.ps1
```

#### CMD

```cmd
.venv\Scripts\activate.bat
```

#### Bash o Zsh

```bash
source .venv/bin/activate
```

Las restricciones de ejecución de PowerShell no deben desactivarse globalmente sin comprender sus implicancias. Es preferible aplicar cambios limitados al usuario o a la sesión cuando sean necesarios.

## Aula 02 — Chunking y vectorización

### Componentes de un pipeline avanzado

Un pipeline RAG puede separarse en cuatro bloques:

1. **Indexación:** carga, segmentación, embeddings y almacenamiento.
2. **Construcción de la consulta:** transformación de la pregunta para mejorar la búsqueda.
3. **Recuperación:** selección de la información relevante.
4. **Generación y evaluación:** creación y análisis de la respuesta.

Separar estas responsabilidades facilita modificar y evaluar cada parte sin reconstruir toda la aplicación.

### Carga de fuentes heterogéneas

LangChain dispone de loaders para distintos formatos.

#### Archivos PDF

`PyPDFLoader` permite cargar documentos PDF y conservar metadatos como el archivo y la página de origen.

#### Páginas web

`WebBaseLoader` recupera contenido web y puede combinarse con Beautiful Soup para seleccionar o limpiar elementos HTML.

#### Directorios

`DirectoryLoader` permite procesar múltiples archivos de una carpeta mediante un loader común.

#### Combinación de fuentes

`MergedDataLoader` permite unificar resultados de distintos cargadores, por ejemplo documentos PDF y archivos de texto.

#### Navegación recursiva

`RecursiveUrlLoader` puede recorrer enlaces relacionados y cargar varias páginas a partir de una URL inicial.

Antes de indexar contenido web se deben revisar permisos, términos de uso, ruido del HTML y posibles duplicados.

### Estrategias de chunking

La segmentación influye directamente sobre la recuperación.

#### División por caracteres

`RecursiveCharacterTextSplitter` intenta respetar separadores naturales mientras mantiene un tamaño aproximado.

Es simple, flexible y suele funcionar como punto de partida.

#### División por tokens

La división por tokens permite alinear mejor los chunks con los límites reales de los modelos.

Resulta especialmente útil cuando el costo, la longitud del contexto o el máximo aceptado por el modelo son restricciones importantes.

#### Tokenizer de Hugging Face

Un tokenizer de Hugging Face puede utilizarse para dividir el contenido de acuerdo con la tokenización de un modelo específico.

Esto permite:

- estimar mejor la longitud de cada fragmento;
- respetar límites del modelo;
- trabajar con modelos multilingües;
- reducir inconsistencias entre chunking y embeddings.

#### Chunking semántico

`SemanticChunker` intenta dividir el contenido según cambios en el significado, en lugar de usar únicamente una cantidad fija de caracteres o tokens.

Puede producir fragmentos más coherentes, pero también requiere:

- generar embeddings durante la segmentación;
- mayor tiempo de procesamiento;
- más consumo de recursos;
- evaluación específica para cada dominio.

### Idioma y modelo de embeddings

El idioma de los documentos debe considerarse al elegir un modelo de embeddings.

Un modelo multilingüe puede representar mejor textos y consultas en diferentes idiomas. Utilizar un modelo poco adecuado puede reducir la similitud entre fragmentos conceptualmente relacionados.

### Tokenización

Los tokens son las unidades que un modelo procesa. Pueden representar palabras, partes de palabras, caracteres o símbolos.

Distintos tokenizers pueden producir resultados diferentes para el mismo texto debido a:

- su vocabulario;
- el idioma;
- el tratamiento de la puntuación;
- la longitud promedio de los tokens;
- las reglas para palabras desconocidas.

La tokenización afecta:

- el tamaño real de los chunks;
- los límites de contexto;
- la generación de embeddings;
- el consumo de recursos;
- el costo de las llamadas a una API.

### Vector store en memoria

`InMemoryVectorStore` permite almacenar embeddings dentro del proceso actual.

Después de cargar los documentos, el retriever puede configurarse con parámetros como:

```python
search_kwargs={"k": 3}
```

El valor `k` determina cuántos fragmentos se recuperan. Un valor alto agrega más contexto, pero también puede incorporar ruido y aumentar el consumo de tokens.

### Persistencia con Pinecone

Pinecone permite almacenar los vectores fuera de la aplicación.

Para crear el índice deben definirse correctamente:

- nombre;
- dimensión de los vectores;
- métrica de distancia;
- modelo de embeddings utilizado.

La dimensión del índice debe coincidir exactamente con la dimensión producida por el modelo de embeddings.

Entre las métricas habituales se encuentra la similitud coseno, útil para comparar la orientación de los vectores.

La búsqueda con puntuación permite inspeccionar la distancia o similitud de cada resultado, pero el significado de la puntuación depende de la métrica y de la implementación utilizada.

### Criterios para la indexación

Una estrategia de indexación debe definir:

- qué fuentes se aceptan;
- cómo se limpian;
- qué metadatos se conservan;
- cómo se dividen;
- qué modelo genera los embeddings;
- dónde se almacenan;
- cómo se actualiza o elimina contenido;
- cómo se evitan duplicados.

La indexación no es una etapa secundaria: determina qué información podrá recuperar el sistema.

## Aula 03 — RAG con Ollama

### Modelos locales

Ollama permite descargar y ejecutar modelos de lenguaje y embeddings localmente.

Sus principales ventajas son:

- mayor control sobre el entorno;
- posibilidad de trabajar sin enviar todas las consultas a una API externa;
- experimentación con distintos modelos;
- reducción de costos variables de API.

También introduce limitaciones:

- uso de memoria y capacidad de cómputo local;
- menor velocidad según el hardware;
- instalación y mantenimiento;
- diferencias de calidad entre modelos;
- necesidad de administrar versiones.

### Preparación del proyecto local

El proyecto se organiza con:

- un ambiente virtual `.venv/`;
- un archivo `requirements.txt`;
- un archivo `.env`;
- un script principal, por ejemplo `rag.py`;
- los documentos que formarán la base de conocimiento.

Las dependencias se instalan con:

```bash
pip install -r requirements.txt
```

Los modelos de Ollama deben descargarse antes de utilizarlos:

```bash
ollama pull nombre-del-modelo
```

El repositorio no debe depender de una versión concreta de Python solo porque haya sido utilizada en el curso. La versión adecuada debe definirse según la compatibilidad real de las dependencias del proyecto.

### Embeddings locales y FAISS

Los documentos se cargan, dividen y convierten en embeddings mediante un modelo disponible en Ollama.

FAISS se utiliza como vector store local. Para instalar su implementación compatible con CPU puede ser necesario:

```bash
pip install faiss-cpu
```

FAISS permite construir un índice local eficiente, aunque su persistencia y actualización deben implementarse explícitamente si la aplicación necesita reutilizarlo entre ejecuciones.

### LangSmith y observabilidad

LangSmith permite inspeccionar el recorrido de las cadenas y modelos.

Puede registrar:

- entradas;
- prompts;
- respuestas;
- documentos recuperados;
- tiempos de ejecución;
- errores;
- secuencia de componentes.

La observabilidad ayuda a detectar si una respuesta genérica se debe a:

- falta de contexto;
- recuperación deficiente;
- prompt ambiguo;
- modelo inadecuado;
- datos mal preparados.

La API key de LangSmith debe almacenarse en `.env` y no publicarse.

### Integración del retriever en la cadena

Crear el vector store no alcanza para construir un RAG. Los documentos recuperados deben incorporarse realmente al prompt.

El flujo correcto es:

1. recibir la pregunta;
2. invocar el retriever;
3. obtener los fragmentos;
4. unirlos o formatearlos como contexto;
5. pasar contexto y pregunta a la cadena;
6. invocar el modelo.

`RunnablePassthrough` puede utilizarse para conservar la pregunta original mientras otra rama del pipeline genera el contexto.

Una cadena que invoque el modelo sin insertar los fragmentos recuperados producirá una respuesta general, aunque exista un vector store correctamente configurado.

### Separación entre tokenizer y embeddings

Los modelos locales no siempre exponen un tokenizer compatible para el chunking.

En esos casos puede utilizarse un tokenizer de Hugging Face. Debe elegirse uno compatible con el modelo o con características semejantes a las usadas durante su entrenamiento.

El desacoplamiento aporta flexibilidad, pero debe documentarse porque tokenizer y modelo de embeddings pasan a ser componentes independientes.

## Aula 04 — Optimización de consultas

### Reescritura de preguntas

Las consultas de los usuarios pueden ser vagas, breves o utilizar términos distintos de los documentos.

Una cadena de reescritura utiliza un LLM para convertir la pregunta original en una formulación más adecuada para la búsqueda vectorial.

Puede construirse con:

- `PromptTemplate`;
- un modelo local mediante Ollama;
- `StrOutputParser`.

El modelo reescritor debe preservar la intención original. Una reescritura que agregue hechos o cambie el problema puede recuperar documentos incorrectos.

### Capacidad del modelo

Los modelos pequeños consumen menos recursos, pero pueden producir reescrituras incompletas o inconsistentes.

Un modelo más grande puede mejorar el resultado, aunque también aumenta:

- uso de memoria;
- latencia;
- consumo energético;
- requisitos de hardware.

La selección debe basarse en pruebas y no únicamente en el tamaño del modelo.

### Estrategia de múltiples consultas

Una única representación vectorial puede no recuperar todos los fragmentos relevantes.

La estrategia multiquery genera varias versiones de la pregunta original. Cada versión se utiliza para consultar la base vectorial, ampliando la cobertura de la recuperación.

El pipeline puede utilizar:

- un prompt que solicite diferentes reformulaciones;
- un modelo de lenguaje;
- `CommaSeparatedListOutputParser`;
- una consulta al retriever por cada reformulación.

Después deben combinarse los resultados y eliminarse duplicados antes de construir el contexto.

Esta técnica puede mejorar el recall, pero aumenta:

- número de consultas;
- latencia;
- consumo de tokens;
- cantidad de fragmentos que deben evaluarse.

### Gestión de tokens

El consumo de tokens aparece en varias etapas:

- división de documentos;
- embeddings;
- reescritura de consultas;
- generación de múltiples preguntas;
- contexto enviado al modelo;
- respuesta final.

Para optimizarlo se puede:

- ajustar el tamaño y overlap de los chunks;
- reducir contenido irrelevante;
- limitar `k`;
- deduplicar resultados;
- redactar prompts más directos;
- restringir la longitud de la respuesta;
- evitar repetir instrucciones innecesarias.

Reducir tokens no debe degradar el contexto hasta hacer que la respuesta pierda precisión.

### Ajuste del pipeline frente a entrenamiento del modelo

El aula utiliza el término “finetuning”, pero las prácticas desarrolladas se concentran en mejorar el comportamiento del sistema mediante:

- reescritura de consultas;
- selección de modelos;
- modificación de prompts;
- múltiples búsquedas;
- gestión del contexto;
- evaluación de resultados.

Estas técnicas optimizan el pipeline RAG, pero no modifican los pesos internos del modelo. Por lo tanto, no equivalen a un proceso de fine-tuning supervisado.

### Evaluación

Una mejora solo puede considerarse útil si se compara con una referencia.

Conviene evaluar:

- relevancia de los documentos recuperados;
- cobertura de la información necesaria;
- fidelidad de la respuesta al contexto;
- presencia de afirmaciones no respaldadas;
- latencia;
- tokens consumidos;
- costo;
- estabilidad entre ejecuciones.

LangSmith puede utilizarse para comparar configuraciones y observar el efecto de los cambios.

## Arquitectura final del pipeline

El sistema desarrollado a lo largo del curso puede representarse mediante las siguientes etapas:

1. cargar documentos desde archivos, directorios o páginas web;
2. limpiar y normalizar el contenido;
3. seleccionar una estrategia de chunking;
4. tokenizar cuando sea necesario;
5. generar embeddings;
6. almacenar los vectores en memoria, FAISS o Pinecone;
7. recibir la consulta;
8. reescribirla o generar múltiples variantes;
9. recuperar los fragmentos relevantes;
10. combinar y deduplicar los resultados;
11. construir el contexto;
12. completar el prompt;
13. invocar el modelo;
14. parsear la respuesta;
15. registrar la ejecución;
16. evaluar calidad, latencia y consumo.

## Buenas prácticas principales

- Separar indexación, recuperación y generación.
- Conservar metadatos de las fuentes.
- Elegir loaders adecuados para cada formato.
- Evaluar el chunking con datos del dominio.
- Considerar idioma y tokenizer al elegir embeddings.
- Verificar que la dimensión del índice coincida con los vectores.
- No asumir que más fragmentos producen una respuesta mejor.
- Confirmar que el contexto recuperado llegue al modelo.
- Deduplicar resultados cuando se utilizan múltiples consultas.
- Pedir al modelo que se limite a la información proporcionada.
- Comparar diferentes configuraciones mediante evaluaciones repetibles.
- Registrar trazas sin exponer datos sensibles.
- Documentar modelos, versiones y dependencias utilizadas.

## Seguridad y publicación

Las credenciales de Gemini, Pinecone, LangSmith u otros servicios deben almacenarse en un archivo `.env`.

No deben publicarse:

```text
.env
.venv/
__pycache__/
.ipynb_checkpoints/
*.db
*.db-shm
*.db-wal
```

Antes de versionar notebooks o scripts se debe revisar que no contengan:

- API keys;
- tokens;
- rutas locales;
- documentos privados;
- URLs con credenciales;
- datos personales;
- outputs innecesarios;
- trazas con contenido sensible.

Los índices vectoriales tampoco deben publicarse automáticamente. Pueden contener representaciones y metadatos derivados de documentos que no estén autorizados para distribución.

## Conclusión

El principal aprendizaje del curso es que RAG debe entenderse como un sistema completo y no como una única llamada a un modelo.

La precisión depende de decisiones tomadas en cada etapa: selección de fuentes, carga, chunking, embeddings, almacenamiento, recuperación, reescritura de consultas, construcción del prompt y evaluación.

Las técnicas avanzadas permiten ampliar la cobertura y mejorar las respuestas, pero también agregan costo y complejidad. Cada mejora debe justificarse mediante pruebas sobre consultas y documentos representativos del problema real.