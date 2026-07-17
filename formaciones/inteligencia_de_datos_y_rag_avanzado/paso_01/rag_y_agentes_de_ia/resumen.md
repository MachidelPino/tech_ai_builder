# Resumen del curso

El curso desarrolla un sistema de atención basado en inteligencia artificial que combina **LangChain**, **Gemini**, **Retrieval-Augmented Generation (RAG)** y **LangGraph**.

El proyecto parte de una consulta, realiza un triaje inicial y decide entre tres alternativas:

- intentar resolverla mediante información recuperada de documentos;
- solicitar datos adicionales;
- abrir un ticket para intervención humana.

## Aula 01 — LangChain y LLMs

### Preparación del entorno

El desarrollo se realiza inicialmente en Google Colab, instalando las bibliotecas necesarias para trabajar con Gemini y LangChain, entre ellas:

- `langchain`;
- `langchain-google-genai`;
- `google-generativeai`.

Colab permite ejecutar notebooks sin configurar un entorno local, aunque las dependencias deben instalarse nuevamente cuando se reinicia la sesión.

### Gestión de la API key

La API key de Gemini funciona como una credencial de acceso al servicio y no debe escribirse directamente en código que pueda hacerse público.

En Google Colab puede almacenarse mediante su sistema de secretos y recuperarse durante la ejecución. Las prácticas principales para proteger una clave incluyen:

- almacenarla fuera del código;
- limitar sus permisos y ámbito de uso cuando el servicio lo permita;
- monitorear consumos o accesos sospechosos;
- revocarla y reemplazarla si se expone.

Las credenciales nunca deben incluirse en notebooks, repositorios, capturas ni archivos exportados.

### Integración de Gemini con LangChain

La conexión con Gemini se realiza mediante `ChatGoogleGenerativeAI`, indicando el modelo, la API key y parámetros de generación como la temperatura.

Una temperatura baja, por ejemplo `0`, busca reducir la variabilidad de las respuestas cuando se necesita un comportamiento más predecible.

El método `invoke()` permite enviar un prompt al modelo y obtener su respuesta.

### Función de LangChain

LangChain ofrece componentes para integrar modelos de lenguaje dentro de una aplicación sin tener que implementar manualmente toda la comunicación con el proveedor.

Su utilidad principal en el proyecto es organizar:

- la conexión con Gemini;
- los prompts;
- las respuestas estructuradas;
- la recuperación de documentos;
- las cadenas de procesamiento.

### Triaje y salida estructurada

El primer componente inteligente del agente es una función de triaje. Su responsabilidad es interpretar la consulta y clasificarla para determinar el siguiente paso.

El triaje puede decidir entre:

- intentar una resolución automática;
- pedir más información;
- abrir un ticket.

La respuesta del modelo debe tener una estructura previsible para que el programa pueda acceder a cada decisión y utilizarla dentro del flujo. Esto evita depender de texto libre difícil de validar o procesar.

---

## Aula 02 — Generación Aumentada por Recuperación

### Objetivo de RAG

RAG permite que un modelo responda utilizando información recuperada desde documentos externos, en lugar de depender únicamente de los datos incluidos en su entrenamiento.

El proceso combina dos etapas:

1. **Recuperación:** localizar fragmentos relacionados con la consulta.
2. **Generación:** entregar esos fragmentos al modelo como contexto para producir una respuesta.

Este enfoque mejora la trazabilidad y permite trabajar con conocimiento privado, específico o actualizado.

### Carga de documentos

El proyecto utiliza documentos PDF con políticas internas como fuente de conocimiento.

Los archivos se cargan mediante `PyMuPDFLoader`, disponible a través de las integraciones de LangChain. Cada documento se transforma en objetos que conservan tanto el contenido como metadatos útiles para identificar su origen.

Entre las dependencias utilizadas se encuentran:

- `langchain-community`;
- `langchain-text-splitters`;
- `pymupdf`.

### División en fragmentos

Los documentos no se envían completos al modelo. Primero se dividen en fragmentos o **chunks** más pequeños mediante `RecursiveCharacterTextSplitter`.

En el ejemplo del curso se utilizan:

- `chunk_size = 300`;
- `chunk_overlap = 30`.

El solapamiento conserva parte del contexto entre fragmentos consecutivos y reduce la posibilidad de separar información estrechamente relacionada.

La configuración del tamaño debe adaptarse al tipo de documento, al modelo de embeddings y al nivel de detalle requerido.

### Embeddings

Los embeddings convierten texto en vectores numéricos que representan relaciones semánticas.

El curso utiliza `GoogleGenerativeAIEmbeddings` con un modelo de embeddings de Gemini. Tanto los fragmentos como la consulta del usuario se representan como vectores para poder comparar su similitud.

### Vector store con FAISS

Los vectores se almacenan en una base vectorial construida con FAISS.

La creación del vector store combina:

- los fragmentos de los documentos;
- el modelo de embeddings;
- los metadatos de cada fragmento.

A partir de este almacenamiento se crea un **retriever**, encargado de recuperar los fragmentos más relacionados con una consulta.

### Configuración del retriever

El retriever se configura para realizar búsquedas por similitud. Entre los parámetros relevantes se encuentran:

- `k`: cantidad máxima de fragmentos recuperados;
- `score_threshold`: similitud mínima requerida para considerar un fragmento relevante.

Un umbral demasiado bajo puede introducir información poco relacionada. Uno demasiado alto puede descartar contenido útil.

### Prompt del sistema RAG

El prompt define el rol del modelo, la consulta del usuario y el contexto recuperado.

En el proyecto, el modelo adopta un rol relacionado con recursos humanos y debe responder utilizando los documentos proporcionados.

La cadena se construye con:

- `ChatPromptTemplate`;
- `create_stuff_documents_chain`;
- el modelo de lenguaje;
- los documentos recuperados.

El modelo debe reconocer cuándo el contexto no alcanza para contestar, en lugar de inventar información.

### Función de búsqueda y respuesta

La función principal del RAG recibe una pregunta y devuelve una estructura con:

- la respuesta;
- las citas o documentos relacionados;
- un indicador de si se encontró información suficiente.

El flujo general es:

1. buscar fragmentos mediante el retriever;
2. verificar si se encontraron documentos relevantes;
3. enviar la pregunta y el contexto a la cadena;
4. comprobar si el modelo pudo responder;
5. devolver la respuesta y sus fuentes.

Cuando no hay documentos pertinentes o el modelo no puede responder con el contexto disponible, la función devuelve una respuesta equivalente a `No lo sé`, sin citas y con el indicador de éxito en `False`.

Este comportamiento es preferible a producir una respuesta no fundamentada.

### Pruebas del RAG

El sistema se prueba con múltiples consultas para observar:

- la respuesta generada;
- los documentos encontrados;
- las citas utilizadas;
- la ruta y el contenido de cada fragmento;
- los casos en los que no existe información suficiente.

Evaluar un sistema RAG requiere comprobar tanto la calidad de la respuesta como la correspondencia entre esa respuesta y las fuentes recuperadas.

---

## Aula 03 — Agentes autónomos con LangGraph

### Grafo de estado

LangGraph permite modelar un agente como un grafo formado por:

- un estado compartido;
- nodos que ejecutan tareas;
- aristas que conectan los nodos;
- condiciones que determinan el siguiente paso;
- puntos de inicio y finalización.

El agente del curso recibe una pregunta y decide si puede resolverla con RAG, necesita solicitar más información o debe abrir un ticket.

### Estado del agente

El estado se define mediante `TypedDict` y reúne la información que debe conservarse durante la ejecución.

Entre sus campos se incluyen:

- pregunta;
- resultado del triaje;
- respuesta;
- citas;
- indicador de documentos encontrados;
- resultado del RAG;
- acción final.

El estado es compartido por los nodos y se actualiza a medida que el agente avanza.

### `TypedDict` y `Optional`

`TypedDict` permite describir la estructura esperada de un diccionario, indicando qué tipo de dato corresponde a cada campo.

`Optional` expresa que un valor puede contener un tipo determinado o ser `None`.

Estas herramientas no realizan por sí solas todas las validaciones en tiempo de ejecución, pero mejoran:

- la documentación del código;
- el autocompletado;
- el análisis estático;
- la detección temprana de inconsistencias;
- la comunicación entre los nodos.

### Nodos principales

El workflow contiene cuatro nodos principales.

#### `triaje`

Analiza la consulta y determina:

- la acción recomendada;
- la urgencia;
- la información faltante.

#### `auto_resolver`

Ejecuta la función RAG.

Cuando encuentra información suficiente, actualiza la respuesta, las citas y la acción final. Cuando falla, deja el estado preparado para decidir entre pedir información o abrir un ticket.

#### `pedir_info`

Genera una respuesta indicando qué datos adicionales necesita el sistema y establece la acción final correspondiente.

#### `abrir_ticket`

Prepara la apertura de un ticket con la consulta original y el nivel de urgencia determinado durante el triaje.

### Aristas directas y condicionales

Una arista directa conecta un nodo con otro sin evaluar condiciones.

Las aristas condicionales seleccionan el siguiente nodo a partir del estado actual.

Después del triaje, el agente puede dirigirse a:

- `auto_resolver`;
- `pedir_info`;
- `abrir_ticket`.

Después de intentar la resolución mediante RAG:

- el flujo termina si la respuesta fue exitosa;
- abre un ticket si el caso requiere intervención;
- solicita información adicional en los demás casos de fallo.

### Funciones de decisión

Las funciones asociadas a las aristas condicionales no ejecutan la tarea principal. Su responsabilidad es leer el estado y devolver el nombre lógico de la siguiente ruta.

Separar los nodos de las decisiones mantiene el grafo más claro:

- los nodos transforman el estado;
- las funciones de decisión seleccionan el camino.

### Compilación y visualización

Después de registrar los nodos y las aristas, el workflow se compila para obtener un grafo ejecutable.

La visualización mediante Mermaid permite revisar la estructura antes de ejecutar el agente y detectar:

- nodos desconectados;
- rutas inexistentes;
- ciclos involuntarios;
- condiciones mal asignadas;
- finales inaccesibles.

---

## Aula 04 — Ejecución y robustez

### Ejecución del agente

El grafo compilado se ejecuta mediante `invoke()`, pasando el estado inicial con la pregunta del usuario.

Durante la ejecución, LangGraph:

1. inicia el flujo;
2. ejecuta el triaje;
3. evalúa la primera arista condicional;
4. recorre los nodos correspondientes;
5. actualiza el estado;
6. termina con una acción final.

### Evaluación de escenarios

El agente se prueba con consultas de distintos tipos para verificar:

- decisiones del triaje;
- clasificación de urgencia;
- funcionamiento del RAG;
- respuestas generadas;
- citas recuperadas;
- solicitud de información;
- apertura de tickets;
- comportamiento ante preguntas fuera del dominio.

Probar múltiples caminos es indispensable para validar un agente, ya que una ejecución exitosa no demuestra que todas las ramas funcionen correctamente.

### Manejo de errores

Los flujos automatizados deben considerar fallos internos y externos.

#### Validación de entradas

Comprobar que los datos requeridos estén presentes y tengan el formato correcto antes de ejecutar operaciones costosas o irreversibles.

#### Manejo de excepciones

Utilizar `try` y `except` alrededor de operaciones que pueden fallar, como llamadas al modelo, lectura de documentos o consultas al vector store.

Las excepciones deben tratarse de forma específica siempre que sea posible, evitando ocultar errores inesperados.

#### Registros

Guardar información relevante sobre cada fallo permite reconstruir qué ocurrió y facilita el mantenimiento.

Los logs pueden incluir:

- etapa del flujo;
- tipo de error;
- consulta procesada;
- identificador de ejecución;
- cantidad de reintentos;
- acción alternativa tomada.

No deben registrar credenciales ni datos sensibles innecesarios.

#### Reintentos

Los reintentos son útiles frente a errores temporales, como límites de servicio o problemas de conexión.

Deben incluir un límite y, cuando sea posible, una espera progresiva para evitar repetir indefinidamente una operación que seguirá fallando.

---

## Arquitectura final

El agente construido durante el curso sigue este recorrido general:

1. recibe una consulta;
2. ejecuta el triaje;
3. determina si debe intentar una resolución automática;
4. consulta el sistema RAG cuando corresponde;
5. recupera fragmentos desde FAISS;
6. genera una respuesta fundamentada con Gemini;
7. conserva las citas utilizadas;
8. finaliza si la respuesta es suficiente;
9. solicita información adicional cuando faltan datos;
10. abre un ticket cuando el caso requiere intervención humana.

## Buenas prácticas principales

- Mantener las API keys fuera del código y del repositorio.
- Definir salidas estructuradas para las decisiones del LLM.
- Dividir los documentos antes de generar embeddings.
- Conservar metadatos para identificar las fuentes.
- Ajustar `k` y el umbral de similitud mediante pruebas.
- Responder que no se dispone de información cuando el contexto es insuficiente.
- Devolver las citas utilizadas junto con la respuesta.
- Representar explícitamente el estado del agente.
- Separar la lógica de los nodos de la selección de rutas.
- Visualizar el grafo antes de ejecutarlo.
- Probar todos los caminos principales y alternativos.
- Validar entradas y registrar errores relevantes.
- Limitar los reintentos ante fallos temporales.

## Seguridad y publicación

Antes de publicar el proyecto se debe revisar que no incluya:

- API keys o tokens;
- secretos almacenados en notebooks;
- documentos internos o privados;
- consultas con datos personales;
- rutas locales;
- outputs innecesarios;
- logs con información sensible;
- bases vectoriales construidas con contenido que no pueda compartirse.

Los archivos `.env`, entornos virtuales, caches y bases de datos locales deben permanecer fuera del repositorio.

## Posibles extensiones

A partir del proyecto del curso, el agente puede ampliarse mediante:

- conversión del notebook a una aplicación Python;
- interfaz con Streamlit o Gradio;
- persistencia del historial;
- observabilidad de ejecuciones;
- búsqueda web mediante herramientas como Tavily;
- integración con herramientas externas;
- uso de MCP para conectar nuevas fuentes y capacidades.