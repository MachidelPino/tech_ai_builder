# Automatización de Flujos: integrando n8n e IA

Curso perteneciente al programa **Tech AI Builder**, dentro de la formación **Ingeniería de Agentes y Automatización con IA**.

Este curso profundiza en la creación de automatizaciones con **n8n**, integrando servicios de correo electrónico, hojas de cálculo y herramientas de Inteligencia Artificial para construir flujos orientados a atención al cliente, clasificación de información, generación de informes y seguimiento de reclamos.

## Información general

* **Programa:** Tech AI Builder
* **Formación:** Ingeniería de Agentes y Automatización con IA
* **Categoría:** IA para Programación
* **Plataforma:** Alura
* **Estado:** En progreso
* **Certificado:** Completado

## Objetivo del curso

El objetivo del curso es aprender a diseñar workflows más completos con n8n, incorporando modelos de IA para analizar información, tomar decisiones, generar respuestas y automatizar procesos operativos.

A lo largo del curso se trabaja con triggers, condiciones, clasificación de correos, análisis de sentimientos, generación automática de informes, memoria para agentes y procesamiento estructurado de datos.

## ¿Por qué realizar este curso?

Este curso permite:

* configurar y personalizar workflows mediante la interfaz visual de n8n;
* integrar servicios como Gmail, Outlook y Google Sheets;
* utilizar triggers y condiciones para clasificar información;
* generar respuestas automáticas para atención al cliente;
* incorporar ChatGPT y otros modelos dentro de workflows;
* analizar sentimientos en comentarios y feedback;
* generar y enviar informes automáticamente;
* estructurar información extraída de correos electrónicos;
* construir automatizaciones de atención al cliente de extremo a extremo.

## Contenido del curso

| Aula | Tema                                              | Duración estimada | Estado      |
| ---- | ------------------------------------------------- | ----------------: | ----------- |
| 01   | ChatGPT como copiloto de productividad            |            51 min | Completado |
| 02   | Atención al cliente inteligente                   |            57 min | Completado   |
| 03   | Organización de informes automatizados            |            45 min | Completado   |
| 04   | Seguimiento de reclamos y comentarios             |            33 min | Completado   |
| 05   | Automatización completa de la atención al cliente |            44 min | Completado   |

## Detalle de aulas

### Aula 01 — ChatGPT como copiloto de productividad

Contenidos principales:

* Introducción a n8n y automatización de procesos.
* Aplicaciones de n8n para especialistas en Inteligencia Artificial.
* Creación y configuración de una cuenta en n8n.
* Construcción del primer workflow.
* Configuración de prompts y procesamiento de texto.
* Importación de workflows desde GitHub.
* Integración de diferentes servicios de correo electrónico.
* Configuración y uso de APIs desde Google Cloud.
* Automatización de generación de resúmenes.
* Uso de ChatGPT como apoyo para tareas productivas.

### Aula 02 — Atención al cliente inteligente

Contenidos principales:

* Conexión de Outlook con n8n.
* Captura y procesamiento de correos electrónicos.
* Edición y normalización de campos.
* Generación de respuestas automáticas con ChatGPT.
* Uso de preguntas frecuentes como contexto para la IA.
* Integración de modelos multimodales.
* Clasificación de correos y solicitudes.
* Lógica condicional con nodos `IF` y `Switch`.
* Ramificación de workflows según la intención detectada.
* Automatización del seguimiento de reclamos.

### Aula 03 — Organización de informes automatizados

Contenidos principales:

* Conexión de un agente de IA con Google Sheets.
* Configuración del prompt de un agente.
* Uso de ChatGPT como analista de datos.
* Elección del modelo adecuado según la tarea.
* Generación automática de informes.
* Envío de informes por correo electrónico.
* Edición y revisión de archivos JSON.
* Incorporación de memoria en agentes de IA.
* Ingeniería de prompts aplicada a análisis e informes.

### Aula 04 — Seguimiento de reclamos y comentarios

Contenidos principales:

* Recopilación de comentarios mediante formularios.
* Preparación y limpieza de datos de feedback.
* Buenas prácticas para recolectar opiniones de clientes.
* Clasificación de sentimientos mediante IA.
* Creación de prompts con salida estructurada en JSON.
* Identificación de comentarios positivos, negativos y neutrales.
* Generación automática de sugerencias de mejora.
* Estructuración de resultados.
* Envío de notificaciones e informes por correo electrónico.
* Aplicación de análisis de sentimientos en distintos contextos.

### Aula 05 — Automatización completa de la atención al cliente

Contenidos principales:

* Configuración de agentes para recibir y procesar pedidos.
* Extracción de información específica desde correos electrónicos.
* Uso de mensajes de sistema para controlar el comportamiento de la IA.
* Construcción de un agente para gestión de eventos.
* Registro y anotación automática de pedidos.
* Automatización de tareas operativas.
* Personalización de respuestas y recomendaciones.
* Pruebas y depuración de workflows.
* Escalabilidad de automatizaciones con n8n.
* Construcción de una solución completa de atención al cliente.

## Conceptos principales

Durante el curso se trabajan los siguientes conceptos:

* Automatización de procesos.
* Workflows con n8n.
* Triggers.
* Integraciones con Gmail y Outlook.
* Google Sheets.
* APIs de Google Cloud.
* ChatGPT.
* Agentes de IA.
* Prompt engineering.
* System messages.
* Salidas estructuradas.
* JSON.
* Clasificación de intenciones.
* Nodos `IF` y `Switch`.
* Análisis de sentimientos.
* Memoria para agentes.
* Generación automática de informes.
* Procesamiento de correos.
* Pruebas y depuración.
* Escalabilidad de workflows.

## Resumen del curso

Los conceptos principales de cada aula se documentan en:

* [`resumen.md`](./resumen.md)

Este archivo se actualizará a medida que avance en el curso, tomando como base los resúmenes generados por la plataforma y filtrándolos para conservar únicamente la información relevante.

## Prácticas y workflows

Las automatizaciones desarrolladas durante el curso se guardarán en la carpeta:

```text
workflows/
```

Cada práctica podrá incluir:

* el workflow exportado desde n8n en formato `.json`;
* una captura de pantalla del flujo;
* una descripción breve dentro de este README.

Estructura esperada:

```text
workflows/
├── 01-nombre-del-workflow.json
├── 01-nombre-del-workflow.png
├── 02-nombre-del-workflow.json
├── 02-nombre-del-workflow.png
└── ...
```

Los nombres de los archivos deben describir la función de la automatización y no limitarse únicamente al número del aula.

## Seguridad

Antes de publicar cualquier workflow exportado se debe verificar que no contenga:

* API keys;
* tokens de acceso;
* credenciales OAuth;
* direcciones de correo personales;
* IDs privados de documentos o recursos;
* URLs de webhooks activos;
* información real de clientes;
* datos fijados dentro de `pinData`.

Las credenciales deben configurarse directamente en n8n y nunca incluirse en los archivos versionados.

## Certificado

El certificado se agregará al completar el curso:

```text
certificado/
└── certificado.pdf
```

## Estado actual

Curso finalizado.
