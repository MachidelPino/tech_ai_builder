# LangChain: Automatizando el análisis de datos con agentes

Curso de la formación **Inteligencia de Datos y RAG Avanzado** de **ONE AI for Tech**, orientado a crear un asistente capaz de analizar archivos CSV, ejecutar herramientas de Python, generar explicaciones y visualizaciones, y ofrecer una interfaz interactiva con Streamlit.

## Información general

- **Programa:** ONE AI for Tech
- **Formación:** Inteligencia de Datos y RAG Avanzado
- **Categoría:** Cursos de IA para Datos
- **Plataforma:** Alura
- **Carga horaria:** 12 horas
- **Cantidad de aulas:** 5
- **Estado:** No iniciado
- **Certificado:** Pendiente

> Las duraciones visibles de las aulas suman 3 h 21 min. La carga horaria informada por la plataforma también puede contemplar ejercicios, lecturas y prácticas.

## Objetivo del curso

Construir una aplicación de análisis de datos que permita realizar preguntas sobre archivos CSV y delegar distintas tareas a un agente de LangChain.

El proyecto integra:

- modelos de lenguaje;
- DataFrames;
- ejecución de código Python;
- herramientas personalizadas;
- memoria conversacional;
- generación de estadísticas y gráficos;
- orquestación de herramientas;
- interfaz web con Streamlit;
- publicación de la aplicación.

## Contenido del curso

| Aula | Tema | Duración | Estado |
|---|---|---:|---|
| 01 | Respondiendo preguntas sobre datos en archivos CSV | 49 min | Pendiente |
| 02 | Obteniendo respuestas explicativas | 31 min | Pendiente |
| 03 | Construyendo herramientas de cero | 49 min | Pendiente |
| 04 | Orquestando agentes con múltiples herramientas | 29 min | Pendiente |
| 05 | Creando una interfaz interactiva | 43 min | Pendiente |

## Detalle de aulas

### Aula 01 — Respondiendo preguntas sobre datos en archivos CSV

Preparación del ambiente y construcción del primer flujo para analizar un DataFrame mediante un modelo de lenguaje.

Contenidos principales:

- configuración del entorno;
- conexión con un LLM mediante Groq;
- generación de código para analizar datos;
- ejecución del código generado con una herramienta de Python;
- conexión entre herramientas y modelos;
- automatización de consultas sobre un DataFrame;
- respuesta a preguntas formuladas en lenguaje natural.

### Aula 02 — Obteniendo respuestas explicativas

Evolución del flujo inicial para producir respuestas más claras y mantener contexto durante la conversación.

Contenidos principales:

- construcción de cadenas de conversación;
- transformación de resultados técnicos en explicaciones;
- memoria conversacional;
- fundamentos de agentes;
- uso de agentes para análisis de datos;
- implementación de un agente con LangChain.

### Aula 03 — Construyendo herramientas de cero

Creación de herramientas personalizadas destinadas a tareas específicas de análisis.

Contenidos principales:

- definición de herramientas y prompts;
- herramienta exploratoria;
- análisis estadístico;
- herramienta de visualización;
- pruebas aisladas;
- criterios para describir entradas, salidas y responsabilidades;
- integración de herramientas personalizadas con LangChain.

### Aula 04 — Orquestando agentes con múltiples herramientas

Construcción de un agente capaz de seleccionar y utilizar distintas herramientas dentro de un mismo flujo.

Contenidos principales:

- generación de un catálogo de herramientas;
- diseño de un prompt estratégico;
- selección de la herramienta adecuada;
- creación y prueba del agente;
- agentes orquestadores;
- integración del asistente completo de análisis de datos.

### Aula 05 — Creando una interfaz interactiva

Conversión del proyecto en una aplicación web accesible desde el navegador.

Contenidos principales:

- preparación del entorno de la aplicación;
- creación de un ambiente virtual;
- organización de herramientas y componentes;
- construcción de la interfaz con Streamlit;
- interacción entre interfaz, agente y datos;
- despliegue en la nube;
- consolidación del proyecto final.

## Conceptos principales

### Análisis de datos con LLMs

El modelo interpreta preguntas en lenguaje natural y propone operaciones sobre los datos.

Este enfoque permite consultar un DataFrame sin escribir manualmente cada instrucción, pero la salida del modelo debe validarse antes de utilizarse.

### DataFrames y archivos CSV

Los datos tabulares se cargan en un DataFrame para facilitar:

- filtrado;
- agrupación;
- cálculos;
- estadísticas;
- transformación;
- visualización.

La estructura, los tipos de datos y los valores faltantes deben inspeccionarse antes del análisis.

### Herramientas de Python

Una herramienta de Python permite ejecutar operaciones que el modelo no debería resolver únicamente mediante texto.

Puede utilizarse para:

- consultar un DataFrame;
- calcular estadísticas;
- transformar datos;
- generar gráficos;
- validar resultados.

### Agentes

Un agente utiliza el modelo para decidir qué acción ejecutar y qué herramienta aplicar.

A diferencia de una cadena fija, el recorrido puede variar según la consulta recibida.

### Herramientas personalizadas

Una herramienta debe tener:

- una responsabilidad concreta;
- un nombre descriptivo;
- una descripción clara;
- entradas definidas;
- una salida previsible;
- manejo de errores.

Las descripciones son relevantes porque el agente las utiliza para seleccionar la herramienta adecuada.

### Memoria conversacional

La memoria conserva información de interacciones anteriores para mantener continuidad.

Debe limitarse a los datos necesarios y evitar el almacenamiento accidental de información sensible.

### Orquestación

La orquestación coordina herramientas exploratorias, estadísticas y gráficas dentro de una única experiencia.

El agente debe elegir la herramienta según la intención de la consulta y combinar los resultados cuando corresponda.

### Streamlit

Streamlit permite crear interfaces web para proyectos de Python con componentes como:

- carga de archivos;
- campos de texto;
- botones;
- tablas;
- mensajes;
- gráficos.

La interfaz debe separar claramente la entrada del usuario, la ejecución del agente y la presentación del resultado.

## Arquitectura del proyecto

El proyecto final sigue una estructura general como esta:

1. el usuario carga un archivo CSV;
2. la aplicación crea un DataFrame;
3. el usuario formula una pregunta;
4. el agente interpreta la intención;
5. selecciona una herramienta;
6. ejecuta el análisis;
7. procesa el resultado;
8. genera una explicación o visualización;
9. muestra la respuesta en Streamlit.

## Resumen del curso

Los apuntes técnicos filtrados y organizados por aula se almacenarán en:

[`resumen.md`](./resumen.md)

## Prácticas y código

El proyecto se almacenará en:

```text
codigo/
```

La estructura interna debe reflejar la implementación real. Una separación posible, cuando resulte útil, es:

```text
codigo/
├── app.py
├── tools/
└── data/
```

No debe aplicarse esta estructura de forma obligatoria si el curso utiliza una organización diferente.

El ambiente virtual debe crearse en la raíz de la carpeta del curso:

```text
.venv/
```

Las dependencias pueden registrarse en:

```text
requirements.txt
```

## Seguridad

Este curso requiere especial cuidado porque el agente puede generar y ejecutar código Python.

No debe permitirse la ejecución irrestricta de código generado por un modelo sobre un sistema con acceso a:

- archivos personales;
- credenciales;
- red interna;
- variables de entorno sensibles;
- bases de datos reales;
- permisos administrativos.

Para una aplicación pública se deben aplicar medidas como:

- ejecución en un entorno aislado;
- validación de operaciones;
- límites de tiempo y recursos;
- restricción de librerías;
- control de archivos accesibles;
- bloqueo de comandos del sistema;
- registro seguro de errores.

Las API keys deben almacenarse en `.env` y mantenerse fuera del repositorio.

No deben versionarse:

```gitignore
.env
.venv/
__pycache__/
.ipynb_checkpoints/
*.db
*.db-shm
*.db-wal
```

Antes de publicar archivos CSV, notebooks o capturas se debe comprobar que no contengan:

- datos personales;
- información confidencial;
- claves o tokens;
- rutas locales;
- outputs extensos;
- errores con información sensible;
- conversaciones reales;
- datos de prueba que identifiquen personas.

## Certificado

El certificado se almacenará en:

```text
certificado/
```

**Estado:** Pendiente.

## Estado actual

- **Curso:** No iniciado
- **Aulas completadas:** 0 de 5
- **Resumen:** Pendiente
- **Prácticas:** Pendientes
- **Certificado:** Pendiente