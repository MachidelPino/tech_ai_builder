# RAG y Agentes de IA

Curso de la formación **Inteligencia de Datos y RAG Avanzado** de **ONE AI for Tech**, orientado a la construcción de aplicaciones que combinan modelos de lenguaje, recuperación de información y agentes autónomos.

A lo largo del curso se trabaja con LangChain para integrar modelos de lenguaje y construir sistemas RAG, y con LangGraph para estructurar agentes mediante grafos de estado.

## Información general

- **Programa:** ONE AI for Tech
- **Formación:** Inteligencia de Datos y RAG Avanzado
- **Categoría:** Cursos de IA para Programación
- **Plataforma:** Alura
- **Duración estimada:** 4 h
- **Cantidad de aulas:** 4
- **Estado:** Fianlizado
- **Certificado:** Obtenido

## Objetivo del curso

Aprender a desarrollar una aplicación basada en inteligencia artificial que combine:

- modelos de lenguaje integrados mediante LangChain;
- prompts con salidas estructuradas;
- embeddings y almacenamiento vectorial;
- recuperación de información mediante RAG;
- agentes autónomos construidos con LangGraph;
- validación, ejecución y manejo de errores.

## ¿Por qué realizar este curso?

El curso permite recorrer los componentes principales de una aplicación moderna basada en modelos de lenguaje, desde la configuración del modelo y el diseño del prompt hasta la recuperación de información y la construcción de agentes.

Su enfoque resulta útil para comprender cómo:

- controlar la salida de un LLM;
- conectar el modelo con conocimiento externo;
- organizar el estado y las decisiones de un agente;
- separar una aplicación en nodos y transiciones;
- probar distintos escenarios de ejecución;
- manejar errores dentro de flujos automatizados.

## Contenido del curso

| Aula | Tema | Duración | Estado |
|---|---|---:|---|
| 01 | LangChain y LLMs | 48 min | Completado |
| 02 | RAG — Generación Aumentada por Recuperación | 66 min | Completado |
| 03 | Construcción de agentes autónomos con grafos de estado | 45 min | Completado |
| 04 | Ejecución del agente | 20 min | Completado |

## Detalle de aulas

### Aula 01 — LangChain y LLMs

Introducción a la integración de modelos de lenguaje mediante LangChain.

Los contenidos principales incluyen:

- creación y protección de una API key de Gemini;
- configuración y uso de Gemini desde LangChain;
- integración de modelos de lenguaje en una aplicación;
- diseño de un prompt de triaje;
- definición de salidas estructuradas;
- construcción de la lógica principal del agente;
- exploración de la función de triaje.

### Aula 02 — RAG: Generación Aumentada por Recuperación

Construcción de un sistema RAG capaz de utilizar documentos como fuente de conocimiento.

Los contenidos principales incluyen:

- preparación del ambiente de desarrollo;
- carga de documentos;
- generación de embeddings;
- configuración de un vector store;
- fundamentos de Retrieval-Augmented Generation;
- diseño del prompt utilizado por el RAG;
- implementación de la función de recuperación y respuesta;
- decisiones relevantes al utilizar RAG;
- ejecución y prueba del sistema.

### Aula 03 — Construcción de agentes autónomos con grafos de estado

Estructuración de un agente mediante LangGraph y representación explícita de su flujo de ejecución.

Los contenidos principales incluyen:

- definición de la estructura del agente;
- programación del grafo;
- uso de `TypedDict` y `Optional` en Python;
- implementación de nodos;
- definición de aristas y transiciones;
- evaluación del recorrido seguido por el agente;
- análisis de los registros generados durante la ejecución.

### Aula 04 — Ejecutando tu agente

Integración y ejecución del agente desarrollado durante el curso.

Los contenidos principales incluyen:

- ejecución del flujo completo;
- prueba del agente en diferentes escenarios;
- manejo de errores en workflows automatizados;
- consolidación del proyecto final;
- revisión de los conceptos principales del curso.

## Conceptos principales

### Modelos de lenguaje con LangChain

LangChain permite integrar modelos de lenguaje dentro de una aplicación y organizar elementos como prompts, respuestas estructuradas y funciones de procesamiento.

El curso utiliza Gemini como modelo y trabaja sobre la necesidad de mantener las credenciales separadas del código.

### Structured output

Las salidas estructuradas permiten definir un formato esperado para la respuesta del modelo.

Esto facilita:

- validar los resultados;
- acceder a campos específicos;
- conectar la salida del LLM con otras funciones;
- reducir ambigüedades;
- utilizar la respuesta para controlar el flujo de una aplicación.

### Embeddings y bases vectoriales

Los embeddings representan fragmentos de información mediante vectores numéricos.

Una base o almacén vectorial permite comparar esos vectores y recuperar los fragmentos más relacionados con una consulta.

### Retrieval-Augmented Generation

RAG combina dos etapas principales:

1. recuperar información relevante desde una fuente externa;
2. proporcionar esa información al modelo para generar una respuesta contextualizada.

Este enfoque permite construir aplicaciones que respondan utilizando documentos o datos concretos en lugar de depender únicamente del conocimiento previo del modelo.

### Agentes y grafos de estado

LangGraph permite representar un agente como un grafo compuesto por:

- un estado compartido;
- nodos que ejecutan operaciones;
- aristas que conectan las etapas;
- condiciones que determinan el siguiente paso.

Esta estructura ayuda a construir flujos explícitos, controlables y más fáciles de analizar.

### Tipado del estado

El uso de herramientas como `TypedDict` y `Optional` permite definir qué información forma parte del estado del agente y qué campos pueden no estar presentes.

Esto mejora la claridad del código y reduce errores durante la comunicación entre nodos.

### Manejo de errores

Los agentes y sistemas RAG dependen de múltiples componentes externos, por lo que deben contemplar posibles fallos en:

- llamadas al modelo;
- acceso a documentos;
- generación de embeddings;
- recuperación de información;
- validación de respuestas;
- transiciones del grafo.

El tratamiento explícito de estos errores evita que el flujo falle sin contexto y facilita su depuración.

## Resumen del curso

Los apuntes técnicos filtrados y organizados por aula se encuentran en:

[`resumen.md`](./resumen.md)

## Prácticas y código

El curso incluye prácticas con Python, LangChain, LangGraph y Gemini. El código desarrollado se almacenará en:

```text
codigo/
```

La estructura interna de esta carpeta se definirá según la organización real de los archivos del curso, sin crear subcarpetas por aula de manera automática.

Cuando corresponda, las dependencias se registrarán en:

```text
requirements.txt
```

El entorno virtual deberá crearse en la raíz de la carpeta del curso:

```text
.venv/
```

## Seguridad

La API key de Gemini debe almacenarse en un archivo `.env` y cargarse desde el código mediante variables de entorno.

No deben incluirse credenciales directamente en:

- archivos de Python;
- notebooks;
- prompts;
- ejemplos;
- capturas de pantalla;
- archivos de configuración versionados.

Antes de publicar el código se debe revisar que no contenga:

- API keys;
- tokens;
- rutas locales;
- documentos privados;
- información personal;
- outputs con datos sensibles;
- archivos generados por bases de datos o sistemas de persistencia.

Los siguientes archivos y directorios no deben versionarse:

```gitignore
.env
.venv/
__pycache__/
.ipynb_checkpoints/
*.db
*.db-shm
*.db-wal
```

## Certificado

El certificado del curso se almacenará en:

```text
certificado/
```

**Estado:** Obtenido.

## Estado actual

- **Curso:** Completado
- **Aulas completadas:** 4 de 4
- **Progreso:** 100 %
- **Resumen:** Completado
- **Certificado:** Obtenido