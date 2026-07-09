# Resumen del curso

## Aula 01 — Configurando el LLM

Esta aula introduce el uso de **LangGraph** y **LangChain** para construir agentes de Inteligencia Artificial capaces de trabajar con modelos de lenguaje y ejecutar tareas de forma más autónoma.

El objetivo inicial es configurar el entorno, conectar un modelo de lenguaje y crear una primera interacción controlada con Gemini.

### Preparación del ambiente

Se trabaja en Google Colab y se instalan las bibliotecas necesarias para usar LangChain, LangGraph y Gemini.

Entre las librerías utilizadas se encuentran:

* `langchain`
* `langgraph`
* `google-generativeai`
* `langchain-google-genai`

También se configura una API key desde Google AI Studio y se guarda de forma segura usando los secretos de Google Colab.

### Conexión con Gemini

Se utiliza `ChatGoogleGenerativeAI` para crear una instancia del modelo Gemini.

A partir de esta configuración, se puede enviar una consulta al modelo y recibir una respuesta generada por la LLM.

### Prompt template inicial

Se define un `PromptTemplate` para guiar el comportamiento del modelo.

El template permite indicar el rol que debe asumir la IA, el tema sobre el que debe responder y el tipo de respuesta esperada.

Esto permite obtener respuestas más consistentes que si se enviaran preguntas sueltas sin estructura.

## Aula 02 — Haciendo las primeras búsquedas

Esta aula muestra cómo conectar una LLM con herramientas externas para que pueda acceder a información actualizada y resolver tareas que exceden su conocimiento interno.

### Uso de herramientas externas

Se integra **Tavily** como herramienta de búsqueda web.

La herramienta permite que el agente realice búsquedas en internet y utilice los resultados para responder consultas con información más actualizada.

El flujo general incluye:

* crear una cuenta en Tavily;
* obtener una API key;
* guardar la clave de forma segura;
* crear una función de búsqueda;
* decorar la función con `@tool`;
* vincular la herramienta al modelo.

### Limitación de una LLM con herramientas sin agente

Aunque una LLM pueda reconocer una herramienta disponible, eso no significa necesariamente que sepa usarla correctamente dentro de un flujo completo.

En la práctica, puede identificar que necesita buscar información, pero no ejecutar la herramienta y construir una respuesta final de forma adecuada.

Esto introduce la necesidad de usar agentes.

### Agente ReAct con LangGraph

Se utiliza `create_react_agent` para crear un agente capaz de razonar y actuar.

El enfoque ReAct combina:

* **Reasoning:** el agente analiza qué necesita hacer.
* **Acting:** el agente decide qué herramienta usar y ejecuta una acción.

Con este enfoque, el agente puede recibir una pregunta, decidir si necesita buscar información, ejecutar la búsqueda y generar una respuesta basada en los resultados.

### System prompt

Se define un `System Prompt` para guiar el comportamiento del agente.

El prompt indica que el agente debe actuar como asistente de investigación, usar la herramienta de búsqueda web cuando sea necesario, analizar los resultados y responder de forma clara incluyendo fuentes.

### Prompt templates

Los prompt templates ayudan a estructurar las instrucciones enviadas a una LLM.

Sus ventajas principales son:

* reutilizar prompts;
* facilitar mantenimiento;
* separar instrucciones del resto del código;
* permitir personalización dinámica;
* mejorar la claridad de las respuestas;
* reducir errores al trabajar con múltiples entradas.

## Aula 03 — Perfeccionando búsquedas con múltiples agentes

Esta aula introduce la orquestación de múltiples agentes mediante grafos. El objetivo es combinar agentes especializados y coordinar sus respuestas dentro de un flujo común.

### Agente de búsqueda científica

Se crea un segundo agente especializado en literatura científica usando `ArxivQueryRun`.

Este agente permite consultar información académica o científica desde arXiv, complementando al agente de búsqueda web.

También se encapsulan los agentes en funciones reutilizables para poder integrarlos más fácilmente dentro de un grafo.

### Estado compartido

Se introduce una estructura de estado común mediante `TypeDict`.

El estado funciona como un repositorio compartido que transporta la información entre nodos del grafo.

Puede contener datos como:

* consulta original del usuario;
* resultado de búsqueda web;
* resultado de búsqueda científica;
* respuesta final;
* decisión del router.

El estado es clave para que los nodos puedan trabajar de forma coordinada.

### StateGraph

LangGraph permite definir flujos de trabajo como grafos usando `StateGraph`.

Un grafo está compuesto por:

* nodos;
* aristas;
* estado compartido;
* punto de inicio;
* punto de finalización.

Cada nodo ejecuta una tarea específica y puede leer o modificar el estado.

### Grafo básico

Se construye un primer grafo con un agente de búsqueda web.

El flujo básico es:

1. inicio del grafo;
2. ejecución del agente;
3. finalización del flujo.

Este primer ejemplo permite entender cómo compilar, ejecutar y visualizar un grafo de LangGraph.

### Nodo supervisor

Se implementa un nodo supervisor encargado de combinar respuestas generadas por distintos agentes.

El supervisor recibe el estado, revisa los resultados disponibles y construye una respuesta final más clara y organizada.

Su función es consolidar información de varias fuentes, por ejemplo:

* resultados de búsqueda web;
* artículos científicos;
* mensajes de error si alguna búsqueda no obtuvo resultados.

### Router agent

Se implementa un agente enrutador encargado de decidir qué agente debe ejecutarse según la consulta del usuario.

El router analiza la pregunta y decide entre opciones como:

* `web_search`;
* `scientific_search`.

Luego, mediante aristas condicionales en el grafo, la ejecución se dirige al nodo correspondiente.

Esto permite construir flujos más dinámicos, donde no siempre se ejecutan los mismos pasos.

### Orquestación de agentes

La orquestación consiste en coordinar varios agentes especializados dentro de un flujo común.

En este curso, el grafo puede combinar:

* un agente de búsqueda web;
* un agente de búsqueda científica;
* un router que decide el camino;
* un supervisor que consolida la respuesta final.

Este enfoque permite crear sistemas más flexibles que una única llamada directa a una LLM.

### Importancia del estado

El estado permite que los datos circulen entre los nodos del grafo de forma controlada.

Sus principales ventajas son:

* modularidad;
* reutilización de nodos;
* escalabilidad;
* trazabilidad;
* facilidad de depuración;
* coordinación entre agentes.

En flujos multiagente, el estado es fundamental para saber qué información produjo cada nodo y cómo debe usarse en los pasos siguientes.

## Aula 04 — Construyendo una visualización

Esta aula muestra cómo crear una interfaz simple para interactuar con el agente construido.

### Gradio

Se utiliza **Gradio** para construir una interfaz web en Python.

La interfaz permite enviar una consulta al agente y visualizar la respuesta final generada por el grafo.

### Función de ejecución

Se define una función principal que recibe la pregunta del usuario, invoca el grafo de LangGraph y devuelve la respuesta final.

El flujo es:

1. el usuario escribe una pregunta;
2. la función ejecuta el grafo;
3. el grafo procesa la consulta mediante sus agentes;
4. se obtiene la respuesta final;
5. Gradio muestra la respuesta en pantalla.

### Interfaz web

Con `gr.Interface` se define una aplicación simple con:

* una caja de texto para ingresar preguntas;
* una salida en formato Markdown;
* título;
* descripción;
* función asociada al grafo.

Esto permite transformar el agente en una aplicación interactiva más fácil de probar y presentar.

## Cierre del curso

El curso presenta una introducción práctica a la creación de agentes con LangGraph.

Los conceptos principales trabajados son:

* configuración de LLMs con Gemini;
* uso de LangChain;
* uso de herramientas externas;
* integración con Tavily;
* creación de agentes ReAct;
* prompt templates;
* agentes especializados;
* búsqueda web;
* búsqueda científica con arXiv;
* grafos de ejecución con LangGraph;
* estado compartido;
* nodos supervisores;
* routing condicional;
* orquestación multiagente;
* visualización con Gradio.

La idea central es que LangGraph permite modelar flujos de IA como grafos, donde distintos agentes y herramientas colaboran para resolver tareas de forma más estructurada, flexible y escalable.
