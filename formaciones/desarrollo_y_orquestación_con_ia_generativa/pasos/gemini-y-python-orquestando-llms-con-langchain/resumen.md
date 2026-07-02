# Resumen del curso

## Aula 01 — Primeros pasos con LangChain

Esta aula introduce el uso de **LangChain** como framework para construir aplicaciones con modelos de lenguaje en Python.

La idea principal es que LangChain permite trabajar con distintas LLMs de forma más flexible, facilitando el cambio entre modelos según el caso de uso. Esto es útil para crear aplicaciones más robustas, escalables y adaptables.

### Ambiente virtual en Python

Se trabaja con la creación de un ambiente virtual para aislar las dependencias del proyecto.

El ambiente virtual permite que cada proyecto tenga sus propias librerías y versiones, evitando conflictos con otros proyectos de Python.

Flujo general:

* crear un ambiente virtual;
* activarlo;
* seleccionar el intérprete correcto en VS Code;
* instalar dependencias desde `requirements.txt`;
* configurar variables de entorno en un archivo `.env`.

Las API keys, como las de Gemini o Cohere, deben guardarse en `.env` y no subirse al repositorio.

### Primer uso de Gemini con LangChain

Se realiza una primera implementación usando Gemini desde LangChain.

El flujo consiste en:

* importar los módulos necesarios;
* configurar el modelo;
* codificar una imagen en base64;
* construir un mensaje con texto e imagen;
* enviar el mensaje al modelo;
* recibir una descripción generada por la LLM.

Esto introduce el uso de modelos multimodales, capaces de procesar texto e imágenes.

### Comparación entre Gemini y Cohere

Se compara el uso de Gemini y Cohere para una misma consulta.

La conclusión principal es que no todos los modelos son igual de adecuados para todas las tareas. Gemini resulta más apropiado para análisis multimodal, mientras que Cohere puede ser útil para tareas textuales y contextos lingüísticos específicos.

Elegir el modelo correcto depende de factores como:

* tipo de entrada;
* calidad esperada de la respuesta;
* idioma;
* especialización del modelo;
* costo de uso;
* facilidad de integración.

LangChain ayuda a cambiar de modelo con menor fricción dentro de una misma aplicación.

## Aula 02 — Prompt templates y Output Parsing

Esta aula se enfoca en estandarizar las interacciones con LLMs usando plantillas de prompts y parsers de salida.

### Prompt templates

Los `PromptTemplate` y `ChatPromptTemplate` permiten definir estructuras reutilizables para enviar instrucciones a una LLM.

Esto evita escribir prompts manualmente en cada llamada y facilita mantener un formato consistente.

Usar plantillas ayuda a:

* reutilizar instrucciones;
* reducir errores;
* separar lógica de aplicación y texto del prompt;
* cambiar variables dinámicamente;
* trabajar con distintos modelos de forma más ordenada.

### Análisis de imágenes con templates

Se adapta el análisis de imágenes para usar una plantilla que combine texto e imagen codificada en base64.

El mensaje enviado al modelo puede incluir distintos tipos de contenido, por ejemplo:

* una instrucción textual;
* una imagen codificada;
* variables que se completan dinámicamente.

Esto permite construir flujos más flexibles y reutilizables.

### Output parsers

Los parsers de salida permiten controlar mejor el formato de la respuesta del modelo.

En esta etapa se usa `StrOutputParser` para convertir la respuesta de la LLM en una cadena de texto simple.

Esto ayuda a que las salidas sean más predecibles y fáciles de usar dentro de una cadena de procesamiento.

### LCEL

LCEL —LangChain Expression Language— permite encadenar componentes de LangChain de forma clara.

Con LCEL se pueden conectar pasos como:

* prompt;
* modelo;
* parser;
* procesamiento posterior.

El operador `|` permite construir cadenas de ejecución legibles, por ejemplo conectando un template con una LLM y luego con un parser.

### Encadenamiento de flujos

Se trabaja con la idea de usar la salida de un modelo como entrada para otro.

Por ejemplo:

1. Gemini analiza una imagen.
2. La salida de Gemini se usa como entrada para Cohere.
3. Cohere genera un resumen textual.

Este enfoque permite combinar fortalezas de distintos modelos dentro de un mismo flujo.

## Aula 03 — Estructurando salidas: diferentes formatos de salida

Esta aula profundiza en la generación de respuestas estructuradas, especialmente en formato JSON.

El objetivo es que las respuestas de las LLMs puedan ser utilizadas por otras partes de una aplicación, como APIs, bases de datos, dashboards o sistemas automatizados.

### Salidas en JSON

Cuando una aplicación necesita procesar automáticamente la respuesta de una LLM, no alcanza con recibir texto libre.

El formato JSON permite obtener datos organizados en campos definidos, lo que facilita su integración con otros sistemas.

Ejemplo de campos para describir una imagen:

* título;
* descripción;
* etiquetas.

### Pydantic y BaseModel

Se utiliza Pydantic para definir modelos de datos en Python.

Un modelo con `BaseModel` permite especificar qué campos debe tener la salida y qué tipo de dato corresponde a cada uno.

Esto aporta:

* estructura;
* validación;
* documentación implícita;
* menor riesgo de respuestas inconsistentes.

### JsonOutputParser

`JsonOutputParser` permite pedirle al modelo que responda siguiendo una estructura JSON específica.

Combinado con Pydantic, permite indicar instrucciones de formato más claras y obtener respuestas más fáciles de procesar.

El parser puede generar instrucciones de formato que luego se insertan dentro del prompt mediante variables parciales.

### Adaptación del parser

Si se usa `StrOutputParser`, la salida JSON puede terminar convertida en texto plano. Para conservar una salida estructurada, es necesario usar un parser adecuado, como `JsonOutputParser`.

La elección del parser depende del formato que necesita la aplicación.

## Aula 04 — Agentes orquestadores

Esta aula introduce la creación de agentes capaces de decidir qué herramienta utilizar según la solicitud del usuario.

La idea principal es pasar de cadenas fijas a un sistema más flexible, donde un agente pueda razonar, elegir una acción y ejecutar una herramienta.

### Agentes ReAct

ReAct combina dos capacidades:

* **razonar** sobre el problema;
* **actuar** usando herramientas disponibles.

Un agente ReAct puede analizar una entrada, decidir si necesita usar una herramienta, ejecutar esa herramienta, observar el resultado y continuar hasta producir una respuesta final.

Esto permite construir aplicaciones más dinámicas que una cadena lineal simple.

### Orquestador en Python

Se crea una estructura de orquestador con LangChain.

El orquestador incluye:

* un modelo de lenguaje base;
* un prompt de agente;
* una lista de herramientas disponibles;
* un mecanismo de ejecución del agente.

El agente no hace todo por sí mismo: necesita herramientas bien definidas para resolver tareas específicas.

### Herramienta de análisis de imagen

Se estructura una herramienta personalizada heredando de `BaseTool`.

Una herramienta debe tener:

* nombre;
* descripción clara;
* parámetros de entrada;
* lógica de ejecución;
* comportamiento de retorno.

La descripción es importante porque ayuda al agente a decidir cuándo debe usar esa herramienta.

Luego, la herramienta de análisis de imagen se integra al orquestador para que el agente pueda procesar imágenes cuando la solicitud lo requiera.

### Ejecución del agente

Se crea un archivo principal para instanciar el agente, configurar el ejecutor y enviar una pregunta.

El flujo general es:

1. el usuario realiza una solicitud;
2. el agente interpreta la intención;
3. el agente decide si necesita una herramienta;
4. se ejecuta la herramienta correspondiente;
5. el agente usa el resultado para construir la respuesta final.

## Aula 05 — Creando herramientas con diferentes LLMs

Esta aula amplía el orquestador agregando nuevas herramientas y combinando distintos modelos dentro del mismo sistema.

### Herramienta de explicación

Se implementa una herramienta orientada a explicar conceptos de forma didáctica.

La herramienta usa:

* `BaseTool`;
* Cohere como LLM;
* `PromptTemplate`;
* `StrOutputParser`.

El prompt define el rol del modelo y el estilo de respuesta esperado, por ejemplo explicar un tema de forma simple, con ejemplos y adaptado a un público específico.

### Integración de herramientas en el orquestador

La herramienta de explicación se agrega al agente orquestador.

De esta manera, el agente puede decidir entre distintas herramientas según la tarea:

* analizar imágenes;
* explicar conceptos;
* responder usando el modelo más adecuado.

Esto muestra cómo LangChain permite construir agentes modulares donde cada herramienta cumple una función específica.

### Uso comercial de LangChain

LangChain puede usarse para integrar LLMs en soluciones empresariales, especialmente cuando se necesita conectar modelos con herramientas, APIs, flujos de datos o procesos internos.

También se menciona LangSmith como herramienta complementaria para observar, probar, depurar e iterar aplicaciones basadas en LLMs.

En contextos comerciales, es importante considerar:

* costos de uso;
* complejidad técnica;
* privacidad;
* seguridad;
* cumplimiento normativo;
* escalabilidad;
* monitoreo de respuestas.

### Combinación de diferentes LLMs

Uno de los puntos centrales del curso es que una solución puede usar más de un modelo.

Por ejemplo:

* Gemini para análisis multimodal;
* Cohere para explicaciones textuales;
* otros modelos para tareas específicas.

La ventaja de LangChain es que permite orquestar distintos modelos y herramientas dentro de un mismo flujo, reduciendo la dependencia de un único proveedor.

### Cierre del curso

El curso presenta una base práctica para crear aplicaciones con Python, Gemini, Cohere y LangChain.

Los conceptos principales trabajados son:

* uso de LLMs desde Python;
* ambientes virtuales y variables de entorno;
* modelos multimodales;
* prompt templates;
* parsers de salida;
* LCEL;
* salidas estructuradas con JSON;
* Pydantic;
* agentes ReAct;
* herramientas personalizadas;
* orquestación de múltiples LLMs.

La idea final es que LangChain permite construir aplicaciones más flexibles y escalables, donde el desarrollador define flujos, herramientas y criterios de uso, mientras los modelos de lenguaje se integran como componentes dentro de una arquitectura mayor.
