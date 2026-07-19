# LangChain: técnicas avanzadas de RAG

Curso de la formación **Inteligencia de Datos y RAG Avanzado** de **ONE AI for Tech**, orientado al diseño y optimización de pipelines de **Retrieval-Augmented Generation (RAG)** con LangChain.

El recorrido profundiza en la preparación de documentos, chunking, embeddings, bases vectoriales, modelos locales con Ollama, reescritura de consultas y evaluación de pipelines mediante LangSmith.

## Información general

- **Programa:** ONE AI for Tech
- **Formación:** Inteligencia de Datos y RAG Avanzado
- **Categoría:** Cursos de IA para Datos
- **Plataforma:** Alura
- **Carga horaria:** 10 horas
- **Cantidad de aulas:** 4
- **Estado:** Completado
- **Certificado:** Obtenido

> La plataforma informa una carga total de 10 horas. Las duraciones visibles de las cuatro aulas suman 3 h 04 min y no necesariamente contemplan ejercicios, lecturas y prácticas.

## Objetivo del curso

Comprender y construir pipelines RAG más completos, desde la carga y segmentación de documentos hasta la recuperación, generación y evaluación de respuestas.

El curso busca desarrollar criterios para:

- organizar un ambiente de desarrollo aislado;
- integrar modelos de lenguaje mediante LangChain;
- dividir documentos en fragmentos adecuados;
- generar embeddings y almacenarlos en una base vectorial;
- implementar cadenas RAG;
- trabajar con modelos locales mediante Ollama;
- mejorar consultas y prompts;
- monitorear y evaluar el comportamiento del pipeline.

## ¿Por qué realizar este curso?

Una implementación básica de RAG puede funcionar en una demostración, pero suele necesitar ajustes para responder de manera consistente en escenarios reales.

Este curso permite profundizar en las decisiones que más influyen en la calidad del sistema:

- cómo dividir y preparar los documentos;
- qué información convertir en embeddings;
- cómo recuperar los fragmentos relevantes;
- cómo integrar modelos locales;
- cómo reformular preguntas para mejorar la búsqueda;
- cómo evaluar resultados, costos y consumo de tokens.

También introduce herramientas de observabilidad que permiten analizar el recorrido de cada consulta en lugar de tratar el pipeline como una caja negra.

## Contenido del curso

| Aula | Tema | Duración | Clases | Estado |
|---|---|---:|---:|---|
| 01 | Conceptos sobre RAG | 47 min | 9 | Completado |
| 02 | Chunking y vectorización | 75 min | 8 | Completado |
| 03 | RAG con Ollama | 34 min | 7 | Completado |
| 04 | Finetuning con RAG | 28 min | 7 | Completado |

## Detalle de aulas

### Aula 01 — Conceptos sobre RAG

Introducción a la arquitectura de Retrieval-Augmented Generation y preparación del ambiente necesario para desarrollar el proyecto.

Contenidos principales:

- revisión de los fundamentos de RAG;
- estructura general de un pipeline de recuperación y generación;
- construcción progresiva del pipeline;
- configuración de un entorno virtual con `virtualenv`;
- uso de Jupyter Notebook;
- activación del entorno virtual en diferentes shells;
- organización inicial de las dependencias del proyecto.

### Aula 02 — Chunking y vectorización

Preparación de documentos para su recuperación semántica y almacenamiento en una base vectorial.

Contenidos principales:

- uso de document loaders;
- carga y normalización de documentos;
- estrategias de chunking;
- relación entre fragmentación y calidad de recuperación;
- generación de embeddings;
- tokenización aplicada a embeddings;
- creación y consulta de un vector store;
- optimización de búsquedas semánticas.

### Aula 03 — RAG con Ollama

Integración de modelos ejecutados localmente dentro de un pipeline RAG.

Contenidos principales:

- instalación y uso de Ollama;
- selección de modelos locales;
- configuración de un modelo de embeddings;
- almacenamiento vectorial con FAISS;
- construcción de una RAG chain;
- recuperación de documentos relevantes;
- integración de tokenizers con modelos ejecutados mediante Ollama;
- optimización de consultas documentales.

### Aula 04 — Finetuning con RAG

Ajuste del comportamiento del pipeline mediante técnicas aplicadas al prompt y a las consultas.

Contenidos principales:

- reescritura de consultas;
- ajuste del prompt;
- evaluación de la personalización de respuestas;
- envío de múltiples preguntas;
- análisis de costos y consumo de tokens;
- monitoreo y evaluación del pipeline;
- revisión final de la arquitectura desarrollada.

> En este contexto, “finetuning” se utiliza como nombre del aula. Los contenidos visibles se concentran principalmente en la optimización del pipeline, los prompts y las consultas, no en el entrenamiento de los pesos de un modelo.

## Conceptos principales

### Pipeline RAG

Un pipeline RAG conecta distintas etapas:

1. carga de documentos;
2. preparación y división del contenido;
3. generación de embeddings;
4. almacenamiento vectorial;
5. recuperación de fragmentos;
6. construcción del contexto;
7. generación de la respuesta;
8. evaluación del resultado.

Cada etapa puede afectar la precisión, relevancia, costo y trazabilidad del sistema.

### Document loaders

Los document loaders convierten fuentes externas en una representación que LangChain puede procesar.

Además del contenido, conviene conservar metadatos que permitan identificar:

- archivo de origen;
- página o sección;
- tipo de documento;
- fecha o versión;
- otros datos útiles para citar y filtrar resultados.

### Chunking

El chunking divide documentos extensos en fragmentos más pequeños antes de generar embeddings.

La estrategia elegida debe equilibrar:

- suficiente contexto dentro de cada fragmento;
- precisión durante la recuperación;
- consumo de tokens;
- solapamiento entre fragmentos;
- estructura semántica del documento.

No existe un tamaño universalmente correcto. Debe evaluarse según el dominio y los documentos utilizados.

### Embeddings

Los embeddings representan el significado del texto mediante vectores numéricos.

Permiten comparar una consulta con los fragmentos almacenados y recuperar aquellos que presentan mayor similitud semántica.

La calidad del resultado depende tanto del modelo de embeddings como del contenido utilizado para generarlos.

### Vector stores

Un vector store conserva los embeddings y permite realizar búsquedas por similitud.

El curso incluye el uso de **FAISS**, una biblioteca orientada a la búsqueda eficiente de vectores.

### Ollama

Ollama permite descargar y ejecutar modelos localmente.

Su integración puede aportar:

- mayor control sobre el ambiente;
- experimentación sin depender completamente de APIs externas;
- procesamiento local de determinados datos;
- flexibilidad para cambiar de modelo.

El uso local también exige considerar los recursos disponibles, la instalación y el mantenimiento del entorno.

### RAG chains

Una RAG chain organiza la comunicación entre el retriever, el prompt y el modelo.

Su responsabilidad es recuperar el contexto relevante, incorporarlo a la consulta y producir una respuesta basada en esa información.

### Reescritura de consultas

La forma en que una persona formula una pregunta no siempre coincide con la estructura de los documentos.

La reescritura de consultas puede:

- aclarar la intención;
- eliminar ambigüedades;
- incorporar términos relevantes;
- mejorar la recuperación;
- descomponer preguntas complejas.

La consulta reescrita debe conservar la intención original y no introducir supuestos incorrectos.

### Observabilidad y evaluación

El monitoreo permite inspeccionar qué ocurrió dentro del pipeline:

- entrada recibida;
- consulta procesada;
- fragmentos recuperados;
- prompt final;
- respuesta generada;
- latencia;
- errores;
- consumo de tokens.

Herramientas como **LangSmith** ayudan a analizar ejecuciones y comparar ajustes en el pipeline.

## Resumen del curso

Los apuntes técnicos filtrados y organizados por aula se almacenarán en:

[`resumen.md`](./resumen.md)

## Prácticas y código

El curso incluye prácticas con Python y Jupyter Notebook. El código se almacenará en:

```text
codigo/
```

La organización interna se definirá según los archivos reales del curso, sin imponer subcarpetas por aula cuando no aporten claridad.

El entorno virtual debe crearse en la raíz de la carpeta del curso:

```text
.venv/
```

Las dependencias utilizadas pueden registrarse en:

```text
requirements.txt
```

Una estructura posible es:

```text
langchain-tecnicas-avanzadas-de-rag/
├── README.md
├── resumen.md
├── requirements.txt
├── codigo/
└── certificado/
```

## Seguridad

Las credenciales de proveedores de modelos y herramientas de observabilidad deben almacenarse mediante variables de entorno.

Las claves no deben escribirse directamente en:

- notebooks;
- scripts de Python;
- prompts;
- archivos de configuración versionados;
- capturas de pantalla.

Los archivos que no deben publicarse incluyen:

```gitignore
.env
.venv/
__pycache__/
.ipynb_checkpoints/
*.db
*.db-shm
*.db-wal
```

Antes de versionar notebooks se debe comprobar que no contengan:

- API keys o tokens;
- rutas locales;
- documentos privados;
- datos personales;
- respuestas con información sensible;
- errores que expongan configuraciones;
- outputs innecesariamente extensos.

Si se utilizan datasets o documentos reales, también debe verificarse que puedan compartirse públicamente.

## Herramientas principales

- Python;
- Jupyter Notebook;
- `virtualenv`;
- LangChain;
- Ollama;
- FAISS;
- modelos de embeddings;
- bases de datos vectoriales;
- LangSmith.

## Certificado

El certificado del curso se almacenará en:

```text
certificado/
```

**Estado:** Obtenido.

## Estado actual

- **Curso:** Finalizado
- **Aulas completadas:** 4 de 4
- **Progreso:** 100 %
- **Certificado:** Obtenido