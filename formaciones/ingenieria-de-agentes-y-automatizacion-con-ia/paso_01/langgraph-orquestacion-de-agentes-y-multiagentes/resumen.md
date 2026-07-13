# Resumen del curso

> **Nota de implementación:** el curso utiliza `gemini-2.5-flash` en varios ejemplos. En este repositorio se reemplazó por `gemini-3.1-flash-lite` para reducir el consumo de recursos durante las prácticas.

## Aula 01 — Agente ReAct

Esta aula introduce el patrón **ReAct**, que combina razonamiento y acción para construir agentes capaces de decidir qué hacer, ejecutar herramientas, observar resultados y continuar hasta responder una consulta.

### Ciclo ReAct

El agente trabaja mediante un ciclo iterativo:

1. **Pensamiento:** analiza la consulta y decide qué necesita.
2. **Acción:** selecciona y ejecuta una herramienta.
3. **Pausa:** espera el resultado de la acción.
4. **Observación:** incorpora el resultado al contexto.
5. **Respuesta o nueva iteración:** decide si ya puede responder o necesita otra acción.

Este enfoque permite que una LLM no se limite a generar texto, sino que pueda interactuar con funciones y fuentes externas.

### Estado e historial

El agente mantiene información como:

* consulta del usuario;
* historial de mensajes;
* acción pendiente;
* observación obtenida;
* respuesta final.

El historial permite sostener conversaciones más coherentes y reutilizar información de interacciones anteriores.

### Herramientas del agente

Se construyen funciones para consultar información de un inventario, como:

* disponibilidad de productos;
* precios;
* producto más costoso;
* valor total de una lista de artículos.

La capacidad del agente depende directamente de las herramientas disponibles. Si no existe una función adecuada para una tarea, el agente no puede resolverla de forma confiable.

### Ingeniería de prompts

El prompt debe describir claramente:

* el ciclo ReAct;
* las herramientas disponibles;
* el formato esperado de cada acción;
* cuándo debe detenerse;
* cómo presentar la respuesta final.

Una buena definición del prompt reduce errores y ayuda al agente a elegir correctamente las herramientas.

### Máscaras de respuesta

Las máscaras de respuesta permiten transformar datos internos en respuestas claras y consistentes para el usuario.

Sirven para:

* estandarizar el formato;
* mejorar la presentación;
* ocultar detalles técnicos innecesarios;
* evitar exponer información sensible.

## Aula 02 — Añadiendo componentes

Esta aula introduce **LangGraph** como framework para representar flujos de agentes mediante grafos.

### Componentes de LangGraph

Los elementos principales son:

* **Nodos:** funciones o acciones ejecutadas dentro del flujo.
* **Aristas:** conexiones que determinan el orden de ejecución.
* **Aristas condicionales:** rutas seleccionadas según una decisión.
* **Estado:** información compartida entre los nodos.

Esta estructura permite controlar de forma explícita cómo interactúan la LLM, las herramientas y la lógica de aplicación.

### AgentState

Se utiliza una estructura de estado para almacenar el historial de mensajes y los datos generados durante la ejecución.

Cada nodo puede leer el estado, realizar una tarea y devolver una actualización.

### Agente de búsqueda con Tavily

Se integra Tavily como herramienta de búsqueda web para obtener información actualizada.

El agente recibe un prompt que le indica:

* buscar información reciente;
* realizar una o varias consultas;
* comparar resultados cuando sea necesario;
* responder de forma clara y fundamentada.

También se incorpora la fecha actual al prompt para mejorar consultas relacionadas con información temporal.

### Visualización del grafo

LangGraph permite representar visualmente el flujo mediante diagramas Mermaid.

Esto ayuda a comprender:

* qué nodos existen;
* cómo se conectan;
* cuándo se invocan herramientas;
* qué rutas puede tomar el agente.

### Llamadas paralelas

Un agente puede ejecutar varias herramientas o consultas en paralelo cuando las tareas son independientes.

Esto reduce el tiempo total de respuesta, aunque requiere manejar:

* errores parciales;
* resultados incompletos;
* orden de las respuestas;
* consolidación de información.

## Aula 03 — Búsqueda y raspado con agentes

Esta aula combina búsquedas web con técnicas de **web scraping** para recolectar información estructurada desde páginas de internet.

### Búsqueda simple y agéntica

Se exploran herramientas como:

* DDGS para búsquedas simples;
* Tavily para búsquedas asistidas por IA;
* agentes que seleccionan y analizan resultados.

La búsqueda agéntica no solo devuelve enlaces: utiliza una LLM para decidir qué buscar, evaluar los resultados y seleccionar fuentes relevantes.

### Limitaciones del web scraping

Algunas páginas dificultan la extracción automática mediante:

* contenido cargado dinámicamente;
* medidas antibots;
* restricciones de acceso;
* estructuras HTML variables;
* paginación y parámetros en las URLs.

Por eso, una herramienta puede funcionar correctamente en un sitio y fallar en otro.

### Selenium y BeautifulSoup

Se utilizan dos herramientas complementarias:

* **Selenium:** automatiza un navegador y permite cargar contenido dinámico.
* **BeautifulSoup:** procesa el HTML y extrae elementos específicos.

El flujo general consiste en:

1. abrir la página con Selenium;
2. esperar que el contenido se cargue;
3. obtener el HTML;
4. analizarlo con BeautifulSoup;
5. identificar etiquetas y atributos;
6. extraer y organizar los datos.

### Limpieza de URLs

Las URLs pueden incluir parámetros de seguimiento, sesiones, búsquedas o paginación.

Limpiarlas permite:

* evitar fuentes duplicadas;
* estandarizar enlaces;
* mejorar logs e índices;
* trabajar siempre con una dirección base consistente.

En Python se pueden usar herramientas como `urllib.parse` para separar y reconstruir URLs sin parámetros innecesarios.

## Aula 04 — Persistencia y streaming

Esta aula introduce mecanismos para conservar el estado de los agentes y observar su ejecución paso a paso.

### Persistencia

La persistencia permite que el agente recuerde conversaciones y estados anteriores, incluso entre distintas ejecuciones.

Se utiliza SQLite junto con `SqliteSaver` para almacenar checkpoints del grafo.

Esto permite conservar:

* historial de mensajes;
* resultados intermedios;
* contexto de conversación;
* estado de cada hilo.

### Threads

Cada conversación se identifica mediante un `thread_id`.

Para que el agente recuerde una conversación anterior, las nuevas ejecuciones deben utilizar el mismo identificador.

Usar otro `thread_id` crea un contexto independiente.

### Streaming

El streaming permite observar los eventos generados durante la ejecución del agente.

Es útil para:

* mostrar respuestas progresivamente;
* entender qué nodo se está ejecutando;
* revisar llamadas a herramientas;
* detectar errores;
* depurar flujos complejos.

### Agregación de múltiples fuentes

Un agente puede combinar información obtenida desde distintas herramientas o fuentes.

El proceso incluye:

1. recolectar resultados;
2. validar cada fuente;
3. resolver inconsistencias;
4. consolidar la información;
5. generar una respuesta final.

Esto puede mejorar la confiabilidad, aunque también aumenta la complejidad cuando las fuentes se contradicen.

## Aula 05 — Human in the Loop

**Human in the Loop —HITL—** permite incorporar revisión humana dentro del flujo de un agente.

Es especialmente útil cuando una acción puede tener consecuencias importantes, cuando existe riesgo de alucinación o cuando se necesita aprobación explícita.

### Interrupciones

El grafo puede configurarse para detenerse antes de ejecutar una herramienta.

El flujo queda pausado para que una persona pueda:

* revisar la acción propuesta;
* aprobarla;
* rechazarla;
* modificar el estado;
* proporcionar información adicional.

Después de la intervención, el flujo puede continuar desde el punto en que fue interrumpido.

### Aprobación humana

Una estrategia de HITL puede seguir este proceso:

1. el agente recibe la consulta;
2. decide realizar una acción;
3. el flujo se pausa;
4. una persona revisa la decisión;
5. la acción se aprueba o cancela;
6. el agente continúa según la decisión.

Este patrón resulta útil para operaciones como enviar mensajes, modificar datos, realizar pagos o ejecutar acciones irreversibles.

### Inyección manual

También es posible modificar manualmente el estado del agente.

Esto permite:

* corregir una respuesta;
* reemplazar un mensaje;
* agregar contexto;
* forzar una decisión;
* ajustar el resultado antes de continuar.

### Snapshots

Un snapshot representa el estado completo del grafo en un momento determinado.

Puede incluir:

* historial de mensajes;
* variables del estado;
* acciones pendientes;
* identificador del hilo;
* metadatos de ejecución.

Los snapshots sirven para depuración, auditoría, restauración e intervención controlada.

## Aula 06 — Orquestando multiagentes

Esta aula presenta una arquitectura con varios agentes especializados que colaboran para completar una tarea.

El ejemplo principal implementa un flujo iterativo para planificar, investigar, redactar y revisar contenido.

### Estado multiagente

El estado incluye claves específicas para cada etapa:

* `task`;
* `plan`;
* `content`;
* `draft`;
* `critique`;
* `revision_number`;
* `max_revisions`.

Usar claves independientes evita sobrescrituras y facilita seguir la evolución de cada dato.

### Agentes y nodos

El sistema se divide en varios roles:

* **Planificador:** crea un esquema inicial.
* **Investigador:** busca información relevante.
* **Escritor:** genera un borrador.
* **Crítico:** analiza el contenido y propone mejoras.
* **Investigador de revisión:** obtiene información adicional a partir de la crítica.

Cada rol se implementa como un nodo del grafo.

### Flujo iterativo

El grafo sigue una secuencia similar a:

1. planificar;
2. investigar;
3. generar un borrador;
4. revisar el contenido;
5. buscar información adicional;
6. generar una nueva versión;
7. finalizar cuando se alcanza el límite de revisiones.

Las aristas condicionales determinan si el flujo debe continuar revisando o terminar.

### Salidas estructuradas

Pydantic permite definir estructuras para las respuestas de los modelos, por ejemplo una lista de consultas de investigación.

Esto mejora la consistencia y facilita que otros nodos procesen la información.

### Interfaz con Gradio

El sistema multiagente se integra con Gradio para permitir que el usuario:

* ingrese un tema;
* defina la cantidad de revisiones;
* ejecute el grafo;
* observe los resultados progresivamente.

## Aula 07 — Creando un asistente de email

Esta aula aplica LangGraph a un asistente capaz de clasificar correos, responder mensajes y programar reuniones.

### Triaje de emails

El sistema clasifica cada correo en una de tres categorías:

* `ignore`;
* `notify`;
* `respond`.

La decisión se basa en:

* contenido del correo;
* perfil del usuario;
* reglas de prioridad;
* instrucciones definidas en el prompt.

### Router con salida estructurada

Se crea un modelo Pydantic para obligar a la LLM a devolver una categoría válida.

Esto aporta:

* formato predecible;
* validación automática;
* integración sencilla con el grafo;
* menor riesgo de respuestas ambiguas.

### Herramientas del asistente

El agente dispone de herramientas para:

* redactar o enviar correos;
* programar reuniones;
* consultar disponibilidad en el calendario.

En el curso, estas funciones representan la estructura necesaria, aunque algunas se implementan como simulaciones.

### Grafo del asistente

El flujo incluye:

1. recepción del correo;
2. clasificación mediante el router;
3. finalización si debe ignorarse;
4. notificación si corresponde;
5. envío al agente de respuesta cuando necesita una acción.

Separar el router del agente de respuesta mejora la modularidad y permite modificar la lógica de clasificación sin rehacer todo el sistema.

### Routers basados en reglas o modelos

Un router puede implementarse mediante:

* **Reglas:** comportamiento simple, predecible y económico.
* **Modelos de IA:** mayor capacidad para comprender contexto y matices.
* **Enfoque híbrido:** reglas para casos claros y un modelo para situaciones ambiguas.

### Memoria semántica

La memoria semántica permite almacenar información relevante sobre preferencias, interacciones y contexto previo.

En un asistente puede utilizarse para:

* personalizar respuestas;
* recordar decisiones;
* adaptar recomendaciones;
* evitar preguntas repetidas;
* mantener continuidad entre conversaciones.

Su uso requiere considerar privacidad, seguridad y control sobre la información almacenada.

## Cierre del curso

Los principales conceptos trabajados fueron:

* agentes ReAct;
* herramientas y funciones;
* LangGraph;
* nodos y aristas;
* estado compartido;
* Tavily y DDGS;
* llamadas paralelas;
* web scraping con Selenium y BeautifulSoup;
* persistencia con SQLite;
* checkpoints y threads;
* streaming;
* Human in the Loop;
* snapshots;
* grafos multiagente;
* Pydantic;
* routers;
* memoria semántica;
* asistentes de email;
* interfaces con Gradio.

La idea central del curso es que LangGraph permite construir sistemas de agentes controlables y con estado, donde diferentes modelos, herramientas y agentes especializados colaboran dentro de flujos explícitos, observables y adaptables.
