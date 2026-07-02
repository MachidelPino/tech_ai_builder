# Resumen del curso

## Aula 01 — Generación de Código

Esta aula introduce el uso de herramientas de Inteligencia Artificial como apoyo en el desarrollo de software. La idea central es entender a la IA como un **copiloto** que puede acelerar tareas, generar ideas y ayudar a resolver problemas, pero sin reemplazar el criterio técnico de la persona desarrolladora.

El curso plantea el desarrollo de una funcionalidad concreta: un formulario frontend de satisfacción que se irá mejorando progresivamente con distintas herramientas de IA.

### Generación inicial de código

Se trabaja con ChatGPT y Gemini para generar código a partir de instrucciones simples. Un ejemplo inicial consiste en pedir un contador regresivo y observar que, si el prompt no especifica el entorno o lenguaje deseado, la IA puede devolver una solución que no coincide con lo esperado.

Esto muestra la importancia de indicar con claridad:

* qué se quiere construir;
* en qué lenguaje debe estar escrito;
* dónde se va a ejecutar;
* qué comportamiento debe tener;
* si debe incluir estructura, estilos e interactividad.

Para visualizar código HTML, CSS y JavaScript se utiliza CodePen, un entorno online que permite probar resultados rápidamente sin instalar herramientas locales.

### HTML, CSS y JavaScript

El curso repasa la función básica de cada tecnología en una página web:

* **HTML:** define la estructura y los elementos.
* **CSS:** controla la apariencia visual.
* **JavaScript:** agrega comportamiento e interactividad.

Esta separación ayuda a entender mejor el código generado por IA y a pedir modificaciones más precisas.

### Canvas en ChatGPT y Gemini

Se exploran herramientas tipo Canvas para trabajar de forma más interactiva con código generado por IA.

A diferencia del flujo tradicional de copiar y pegar respuestas, Canvas permite generar, editar, previsualizar y ajustar código en un mismo entorno. Esto reduce el cambio constante de contexto entre el chat y el editor, y hace más simple validar el resultado.

También se remarca la importancia de iniciar nuevos chats cuando cambia el objetivo, para evitar que el contexto anterior afecte las respuestas.

### Prompts efectivos

Un prompt funciona como una instrucción para la IA. Cuanto más claro, específico y consistente sea, mejor será la respuesta.

Un buen prompt debería evitar ambigüedades y especificar el resultado esperado. En desarrollo, esto puede incluir lenguaje, entorno, restricciones, funcionalidades, estructura visual, criterios de aceptación y formato de salida.

La calidad del prompt influye directamente en la calidad del código generado.

### De asistente a copiloto

La IA puede usarse de forma básica como asistente que responde preguntas o genera fragmentos de código. Sin embargo, el enfoque más productivo es integrarla como copiloto dentro del flujo de trabajo.

Esto implica usarla para generar, revisar, ajustar, explicar y mejorar código, manteniendo siempre la supervisión humana sobre el resultado.

## Aula 02 — De la demanda al prototipo

Esta aula muestra cómo transformar una necesidad inicial en un prototipo funcional usando IA. El foco está en pasar de una demanda informal a requisitos más claros, criterios de aceptación y código ejecutable.

### De idea a requisitos

Se plantea el caso de un formulario de satisfacción para recolectar feedback de clientes. Antes de pedir código, se definen requisitos funcionales concretos, como niveles de satisfacción, campo de comentarios, botón de envío, mensaje de agradecimiento y validaciones.

Este paso es importante porque la IA responde mejor cuando recibe una especificación clara del problema y del comportamiento esperado.

### Prompt para prototipado

A partir de los requisitos, se crea un prompt detallado para generar el prototipo en HTML, CSS y JavaScript.

El resultado inicial puede funcionar parcialmente, pero suele requerir revisión. Por eso, generar código con IA no elimina la necesidad de probar, interpretar errores y ajustar la solución.

### Comparación entre ChatGPT y Gemini

Se utilizan ChatGPT Canvas y Gemini Canvas para generar y modificar el formulario. Ambas herramientas permiten crear prototipos, probar cambios y ajustar el código de forma interactiva.

Gemini permite trabajar con historial de versiones y vista previa, lo que facilita comparar estados del código y corregir detalles visuales o funcionales.

### Refactorización con IA

El código generado inicialmente por una IA puede necesitar mejoras. La refactorización permite reorganizar, simplificar o mejorar partes del código sin cambiar necesariamente su comportamiento principal.

La IA puede ayudar a:

* mejorar estilos visuales;
* reorganizar funciones;
* hacer el código más legible;
* corregir mensajes o comportamientos;
* adaptar la interfaz a nuevos requisitos.

Aun así, es importante probar cada cambio y conservar versiones anteriores cuando sea posible.

### Riesgos de editar sin precisión

Pedirle a una IA que reescriba un código completo sin instrucciones claras puede provocar pérdida de reglas de negocio o cambios no deseados.

Una mejor práctica es pedir modificaciones específicas, explicar qué debe mantenerse y validar que el resultado conserve la funcionalidad original.

## Aula 03 — Ejecución de Código

Esta aula se enfoca en la diferencia entre generar código y lograr que ese código funcione en un entorno real.

La IA puede producir una solución aparentemente correcta, pero la persona desarrolladora debe verificar si el código puede ejecutarse correctamente, si tiene acceso a los recursos necesarios y si cumple con el objetivo práctico.

### Frontend y backend

Se repasan diferencias básicas entre frontend y backend:

* **Frontend:** parte visible e interactiva con la que trabaja el usuario.
* **Backend:** lógica, procesamiento, acceso a datos, archivos, APIs o servicios externos.

Esta distinción es importante porque algunas soluciones pueden funcionar como prototipo visual, pero necesitar backend para ser útiles en un sistema real.

### Filtro de palabras prohibidas

Se trabaja con un ejemplo de moderación de comentarios usando Python. El objetivo es reemplazar palabras prohibidas por asteriscos.

Primero, la lista de palabras puede estar escrita directamente en el código, pero esa solución es poco flexible. Una mejora consiste en cargar las palabras prohibidas desde un archivo externo, como `palabras-prohibidas.txt`.

Esto permite modificar la lista sin cambiar el código fuente.

### Archivos externos y entorno de ejecución

Cuando el código depende de archivos externos, el entorno de ejecución importa. La IA puede escribir código para leer un archivo, pero si ese archivo no existe en el entorno donde se ejecuta el programa, aparece un error.

Este problema muestra una limitación común: la IA puede generar código teórico, pero no siempre tiene acceso real a archivos, APIs, credenciales o infraestructura.

### Google Colab

Google Colab se utiliza como entorno para ejecutar código Python y cargar archivos externos.

Esto permite probar soluciones que no funcionan dentro del entorno aislado de una IA, especialmente cuando el código necesita interactuar con archivos.

### Rol del desarrollador

El rol de la persona desarrolladora es conectar el código generado por IA con el entorno real.

La IA puede generar la lógica, pero el desarrollador debe:

* preparar los archivos necesarios;
* elegir el entorno correcto;
* ejecutar y probar el código;
* interpretar errores;
* adaptar la solución al contexto real;
* validar que el resultado cumpla con el objetivo.

## Aula 04 — Conociendo a Claude y Grok

Esta aula compara distintas herramientas de IA para desarrollo y muestra que no todas son igual de útiles para las mismas tareas.

La idea principal es no depender de una sola IA, sino elegir la herramienta adecuada según el tipo de problema.

### Exploración de herramientas

Se presentan Claude y Grok como alternativas a ChatGPT y Gemini para tareas de generación, edición y adaptación de código.

Grok se destaca por su velocidad y por generar prototipos rápidamente. Claude se presenta como una herramienta útil para trabajar con interfaces, edición de código y resultados visuales.

La comparación muestra que cada herramienta tiene fortalezas y limitaciones.

### Migración y adaptación de código

Se trabaja con la idea de pasar código entre herramientas y lenguajes. Por ejemplo, continuar en Claude un código generado con ChatGPT, o convertir una lógica escrita en Python a JavaScript para integrarla en un formulario web.

Este flujo requiere supervisión, porque cada IA puede interpretar las instrucciones de forma distinta y no siempre respetar la estructura original.

### Diferencias entre herramientas

El curso muestra que algunas herramientas permiten editar fragmentos específicos de código, mientras que otras requieren instrucciones más completas o tienen flujos menos directos.

Esto refuerza la importancia de conocer cómo trabaja cada plataforma y adaptar el prompt a sus características.

### Elección de herramienta según la tarea

La comparación del curso propone usar distintas IAs según el objetivo:

* herramientas rápidas para consultas simples o prototipos inmediatos;
* herramientas con buena vista previa para frontend e interfaces;
* modelos con mejor razonamiento para lógica compleja o backend;
* modelos con contexto amplio para documentación extensa o análisis de archivos.

La conclusión principal es que la versatilidad está en saber combinar herramientas y elegir la más adecuada para cada parte del trabajo.

## Aula 05 — Corrección del código y buenas prácticas

Esta aula cierra el curso con foco en verificación, documentación, buenas prácticas y el rol de la IA dentro del flujo de desarrollo.

### Verificación del código

Después de generar o traducir código con IA, es necesario probar que funcione correctamente.

En el caso del filtro de palabras, se verifica que la lógica funcione con distintas entradas, incluyendo variaciones con mayúsculas. También se prueba el código en diferentes entornos para comprobar que el resultado no dependa únicamente de la herramienta que lo generó.

### Organización del código

Se trabaja sobre mejoras de organización, como separar CSS del HTML y mantener una estructura más clara.

Aunque un prototipo puede tener todo el código junto, un proyecto más mantenible requiere separar responsabilidades y ordenar mejor los archivos.

### Lógica de negocio

El curso menciona que algunas funcionalidades pueden implementarse en el frontend para demostración, pero en sistemas reales la lógica de negocio suele pertenecer al backend.

Esto es importante para validaciones, seguridad, análisis de datos y control del comportamiento del sistema.

### Documentación

La documentación permite entender, mantener y extender un proyecto en el futuro. También facilita la colaboración con otras personas.

La IA puede ayudar a generar una primera versión de la documentación técnica, incluyendo:

* descripción general del proyecto;
* tecnologías utilizadas;
* estructura del código;
* funcionamiento de la lógica;
* guía de mantenimiento;
* posibles extensiones futuras.

Sin embargo, esa documentación debe revisarse para asegurar que sea correcta, clara y útil.

### Agentes locales y seguridad

Se menciona el caso de asistentes locales capaces de actuar directamente sobre el sistema del usuario, acceder a archivos o ejecutar tareas.

Este tipo de herramientas puede ser potente para automatizar procesos, pero también implica riesgos. Dar acceso a archivos, terminal o permisos del sistema a una IA requiere especial cuidado, configuración segura y evitar privilegios innecesarios.

### Flujo de desarrollo con IA

El curso resume el trabajo con IA en varias etapas:

1. generar una primera versión del código;
2. verificar si cumple la función básica;
3. refinar el resultado con una o varias herramientas;
4. probarlo en un entorno real;
5. detectar casos límite y errores;
6. documentar el proyecto;
7. preparar el código para futuras mejoras.

La idea final es adoptar una mentalidad de copiloto: la IA acelera el trabajo, pero el criterio humano sigue siendo fundamental para dirigir, validar, corregir y llevar una solución del prototipo a un uso real.
