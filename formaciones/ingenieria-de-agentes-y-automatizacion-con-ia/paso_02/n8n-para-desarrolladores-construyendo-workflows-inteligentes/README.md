# n8n para desarrolladores: Construyendo workflows inteligentes

Curso perteneciente al programa **Tech AI Builder**, dentro de la formación **Ingeniería de Agentes y Automatización con IA**.

Este curso está orientado a la construcción de workflows más robustos con **n8n**, aplicados a procesos de desarrollo de software. El eje práctico consiste en automatizar la revisión de Pull Requests, integrar GitHub y Slack, incorporar intervención humana, registrar ejecuciones, manejar errores y utilizar Inteligencia Artificial para analizar cambios de código.

## Información general

- **Programa:** Tech AI Builder
- **Formación:** Ingeniería de Agentes y Automatización con IA
- **Categoría:** IA para Programación
- **Plataforma:** Alura
- **Estado:** Completado
- **Certificado:** Completado

## Objetivo del curso

El objetivo del curso es aprender a diseñar workflows orientados a escenarios de desarrollo, utilizando n8n para conectar servicios, controlar rutas de ejecución, registrar información y automatizar tareas relacionadas con Pull Requests.

A lo largo del curso se trabaja con GitHub, Slack, Trello, nodos de código, Data Tables, manejo de errores, Human in the Loop y modelos de IA como Gemini.

## ¿Por qué realizar este curso?

Este curso permite:

- desarrollar un pipeline completo para la revisión de Pull Requests;
- automatizar tareas repetitivas dentro del flujo de desarrollo;
- modelar rutas de ejecución con tratamiento de datos y salidas;
- omitir o redirigir etapas cuando faltan datos o se producen errores;
- utilizar nodos de GitHub, Code y otras herramientas de n8n;
- organizar ramificaciones mediante nodos condicionales;
- integrar notificaciones por correo electrónico y Slack;
- incorporar Gemini para revisar cambios de código;
- registrar ejecuciones y auditorías mediante Data Tables;
- monitorear y depurar el historial de ejecuciones del sistema.

## Contenido del curso

| Aula | Tema | Duración estimada | Estado |
|---|---|---:|---|
| 01 | Primera automatización | 22 min | Completado |
| 02 | Setup y Human in the Loop | 36 min | Completado |
| 03 | Observabilidad del flujo | 20 min | Completado |
| 04 | Tratamiento de errores y nodos personalizados | 21 min | Completado |
| 05 | Asistente de IA en el flujo | 40 min | Completado |

## Detalle de aulas

### Aula 01 — Primera automatización

Contenidos principales:

- Presentación del curso.
- Configuración inicial de n8n.
- Creación de la primera automatización.
- Automatización de notificaciones.
- Tipos de hosting disponibles para n8n.
- Gestión de proyectos mediante workflows.
- Construcción inicial de un flujo para Pull Requests.
- Integración básica con GitHub.

### Aula 02 — Setup y Human in the Loop

Contenidos principales:

- Configuración de Slack.
- Incorporación de Human in the Loop.
- Filtrado de eventos.
- Control del flujo de ejecución.
- Manejo de errores en solicitudes.
- Fijación de datos para pruebas en n8n.
- Integración entre Slack y GitHub.
- Aprobaciones y validaciones humanas dentro de una automatización.

### Aula 03 — Observabilidad del flujo

Contenidos principales:

- Introducción a Data Tables.
- Registro de datos de ejecución.
- Filtros para auditoría.
- Monitoreo de ejecuciones programadas.
- Documentación interna con Sticky Notes.
- Creación de un registro de Pull Requests.
- Trazabilidad y seguimiento del workflow.

### Aula 04 — Tratamiento de errores y nodos personalizados

Contenidos principales:

- Ejecución de código dentro de n8n.
- Automatización de movimientos en Trello.
- Tratamiento de errores.
- Manejo de fallos dentro de un flujo de publicación.
- Estructura de retorno de datos en n8n.
- Integración entre Pull Requests y Trello.
- Creación de nodos y transformaciones personalizadas.

### Aula 05 — Asistente de IA en el flujo

Contenidos principales:

- Relación entre estrategia y automatización.
- Incorporación de Gemini para revisar Pull Requests.
- Optimización de notificaciones.
- Elección del nodo adecuado según la tarea.
- Uso de outputs estructurados.
- Integración de IA dentro de un pipeline de desarrollo.
- Construcción de la versión final de la automatización de Pull Requests.

## Conceptos principales

Durante el curso se trabajan los siguientes conceptos:

- Automatización de procesos de desarrollo.
- Pull Requests.
- GitHub.
- Slack.
- Trello.
- Human in the Loop.
- Nodos condicionales.
- Manejo de errores.
- Nodos de código.
- Data Tables.
- Auditoría.
- Observabilidad.
- Monitoreo de ejecuciones.
- Sticky Notes.
- Outputs estructurados.
- Gemini.
- Integración de servicios.
- Pipelines automatizados.

## Resumen del curso

Los conceptos principales de cada aula se documentarán en:

- [`resumen.md`](./resumen.md)

Este archivo se actualizará a medida que avance en el curso, tomando como base los resúmenes generados por la plataforma y filtrándolos para conservar únicamente la información relevante.

## Prácticas y workflows

Los workflows desarrollados durante el curso se guardarán en la carpeta:

```text
workflows/
```

Cada práctica podrá incluir:

- el workflow exportado desde n8n en formato `.json`;
- una captura de pantalla en formato `.png`;
- una descripción breve dentro de este README.

Estructura sugerida:

```text
workflows/
├── 01-nombre-del-workflow.json
├── 01-nombre-del-workflow.png
├── 02-nombre-del-workflow.json
├── 02-nombre-del-workflow.png
└── ...
```

Los nombres deben describir la función de cada automatización y no limitarse únicamente al número del aula.

## Seguridad

Antes de publicar cualquier workflow exportado se debe verificar que no contenga:

- API keys;
- tokens de acceso;
- credenciales OAuth;
- URLs de webhooks activos;
- nombres o identificadores privados de repositorios;
- direcciones de correo personales;
- datos reales de Pull Requests;
- IDs internos de Slack, GitHub o Trello;
- datos fijados dentro de `pinData`.

Las credenciales deben configurarse directamente en n8n y nunca incluirse en los archivos versionados.

## Certificado

El certificado se agregará al completar el curso:

```text
certificado/
└── certificado.pdf
```

## Estado actual

Curso finalizado.