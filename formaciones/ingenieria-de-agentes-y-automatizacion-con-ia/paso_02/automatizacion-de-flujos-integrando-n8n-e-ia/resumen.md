# Resumen del curso

## Aula 01 — ChatGPT como copiloto de productividad

Esta aula introduce **n8n** como una plataforma low-code para automatizar procesos mediante workflows visuales. Su objetivo es conectar aplicaciones, APIs y modelos de Inteligencia Artificial para ejecutar tareas repetitivas con mínima intervención humana.

### Fundamentos de n8n

Un workflow se construye conectando nodos, cada uno encargado de una acción específica.

Los componentes principales son:

* **Trigger:** evento que inicia la automatización.
* **Nodo de acción:** ejecuta una operación sobre los datos.
* **Conexión:** define cómo circula la información entre nodos.
* **Credencial:** permite acceder de forma autenticada a servicios externos.
* **Expresión:** incorpora datos dinámicos producidos por otros nodos.

n8n permite integrar servicios como Gmail, Outlook, Google Sheets, Google Drive, OpenAI y otras aplicaciones mediante nodos que abstraen el uso de sus APIs.

### Beneficios de la automatización

Automatizar procesos permite:

* reducir tareas manuales y repetitivas;
* disminuir errores humanos;
* mantener resultados consistentes;
* procesar mayores volúmenes de información;
* integrar sistemas que normalmente funcionan por separado;
* liberar tiempo para tareas de mayor valor.

Al incorporar IA, los workflows pueden además interpretar texto, resumir información, clasificar datos, generar respuestas y tomar decisiones simples.

### Primer workflow con correo e IA

Se construye una automatización para resumir correos electrónicos:

1. Gmail detecta un nuevo correo.
2. n8n obtiene el contenido completo del mensaje.
3. Un nodo de OpenAI procesa el texto.
4. El modelo genera un resumen.
5. Gmail envía el resultado por correo.

El prompt del sistema define que el modelo debe resumir el mensaje en español, extraer los puntos principales y producir una frase ejecutiva sin agregar información externa.

Un detalle importante fue desactivar la opción `Simplify` del trigger de Gmail, ya que podía recortar el contenido del correo e impedir que el modelo analizara el texto completo.

### APIs y credenciales

Las APIs permiten que n8n se comunique con servicios externos.

Para utilizar servicios de Google puede ser necesario:

* crear un proyecto en Google Cloud;
* habilitar la API correspondiente;
* configurar credenciales;
* utilizar OAuth o una cuenta de servicio;
* otorgar permisos sobre los recursos necesarios.

Las API keys, tokens, claves privadas y archivos de credenciales no deben escribirse directamente en los workflows públicos ni subirse al repositorio.

### Integración de servicios de correo

n8n puede automatizar tareas tanto con Gmail como con Outlook.

Aunque ambos servicios permiten enviar y recibir mensajes, pueden diferir en:

* configuración de OAuth;
* límites de envío;
* estructura de los datos;
* operaciones disponibles;
* integración con sus respectivos ecosistemas.

## Aula 02 — Atención al cliente inteligente

Esta aula desarrolla un workflow de atención al cliente que captura correos, organiza sus datos, genera respuestas con IA y decide cuándo debe intervenir una persona.

### Captura y preparación de correos

El flujo comienza con un trigger de Outlook que se activa al recibir un nuevo mensaje.

Luego se utiliza `Edit Fields` —anteriormente denominado `Set`— para conservar únicamente los datos relevantes, por ejemplo:

* remitente;
* asunto;
* cuerpo del mensaje;
* identificador del correo;
* información necesaria para responder.

Este paso ayuda a normalizar la información y evita enviar datos innecesarios a los nodos siguientes.

### Respuestas automáticas basadas en FAQs

Se conecta un modelo de OpenAI para responder consultas frecuentes.

El system prompt incluye:

* rol del asistente;
* información oficial de la empresa;
* preguntas frecuentes;
* tono esperado;
* límites de actuación;
* instrucciones para no inventar respuestas.

Si una consulta está cubierta por las FAQs, el modelo puede generar una respuesta automática que luego se envía desde Outlook.

El workflow puede publicarse para ejecutarse periódicamente y funcionar sin intervención manual.

### Clasificación de consultas

No todos los correos deben recibir una respuesta automática. Para manejar esta diferencia se incorpora un primer modelo que clasifica cada consulta como:

* **SIMPLE:** puede resolverse utilizando la información disponible.
* **COMPLEJA:** incluye reclamos, facturación, situaciones sensibles o información no cubierta.

Después, un nodo `IF` divide el flujo:

* las consultas simples se responden automáticamente;
* las consultas complejas se escalan a una persona.

Para los casos complejos, la IA puede generar un resumen y una respuesta sugerida, pero la decisión final queda en manos del equipo humano.

### IF y Switch

Los nodos condicionales permiten que el workflow tome distintas rutas.

`IF` es apropiado cuando se evalúa una condición verdadera o falsa, mientras que `Switch` resulta más claro cuando un valor puede pertenecer a varias categorías.

Las condiciones pueden operar sobre distintos tipos de datos:

* texto;
* números;
* fechas;
* booleanos;
* arrays;
* objetos.

### Buenas prácticas para prompts

Un prompt efectivo debería incluir:

* contexto;
* tarea;
* instrucciones;
* restricciones;
* tono;
* formato de salida.

También puede utilizar ejemplos para mostrar el comportamiento esperado.

En automatizaciones, conviene solicitar respuestas limpias y predecibles, evitando explicaciones adicionales que puedan romper el procesamiento del nodo siguiente.

## Aula 03 — Organización de informes automatizados

Esta aula utiliza un agente de IA conectado a Google Sheets para analizar datos, generar informes ejecutivos y enviarlos automáticamente por correo.

### Conexión con Google Sheets

Se configura Google Cloud para permitir que n8n acceda a una hoja de cálculo.

El proceso incluye:

1. habilitar Google Sheets API;
2. crear una cuenta de servicio;
3. descargar una credencial JSON;
4. utilizar `client_email` y `private_key` en n8n;
5. compartir la hoja con la cuenta de servicio.

La clave privada debe almacenarse exclusivamente como credencial segura y nunca publicarse.

### Agente de IA con herramientas

Se utiliza un nodo `AI Agent` conectado a una herramienta de Google Sheets.

El agente recibe un prompt que define:

* su rol como analista de datos;
* la fuente de información disponible;
* qué herramienta puede utilizar;
* qué tipo de análisis debe generar;
* cómo debe presentar sus resultados.

En lugar de recibir todos los datos directamente, el agente puede decidir cuándo consultar la hoja mediante la herramienta configurada.

### Análisis de datos en lenguaje natural

El agente transforma datos numéricos en respuestas comprensibles, por ejemplo:

* cantidad total de clientes;
* promedios diarios;
* tendencias;
* comparaciones;
* resúmenes ejecutivos.

Las respuestas deben validarse comparándolas con cálculos realizados directamente en la hoja de cálculo.

La IA ayuda a interpretar y comunicar los resultados, pero no reemplaza la verificación de datos.

### Automatización de informes

El workflow puede seguir esta secuencia:

1. recibir una consulta por correo;
2. extraer y normalizar los campos;
3. enviar la consulta al agente;
4. consultar Google Sheets;
5. generar un informe;
6. estructurar el mensaje;
7. enviarlo automáticamente por Outlook.

Los datos se mapean mediante expresiones que referencian campos producidos por nodos anteriores.

### Elección del modelo

No todos los modelos ofrecen el mismo equilibrio entre:

* razonamiento;
* velocidad;
* costo;
* contexto disponible;
* calidad de escritura;
* precisión numérica.

La elección debe basarse en la tarea real. Para informes numéricos, es importante evaluar el modelo con ejemplos y verificar que los cálculos sean correctos.

### Memoria del agente

Sin memoria, cada mensaje se procesa como una interacción independiente. Esto provoca problemas en preguntas de seguimiento que dependen de información previa.

Agregar memoria permite mantener contexto, por ejemplo:

1. “¿Cuántos clientes tenemos?”
2. “¿Y cuántos compraron el último mes?”

La memoria debe asociarse correctamente a una sesión o conversación para evitar mezclar información de usuarios distintos.

### Ingeniería de prompts

Una estructura útil para prompts incluye:

* **Contexto:** situación y datos disponibles.
* **Tarea:** resultado que debe producirse.
* **Instrucciones:** reglas y límites.
* **Tono y formato:** forma de presentar la respuesta.

También se pueden aplicar técnicas como role prompting, separadores, ejemplos y few-shot prompting.

## Aula 04 — Seguimiento de reclamos y comentarios

Esta aula construye una automatización para leer feedback desde Google Sheets, analizar su sentimiento y notificar los casos negativos.

### Recolección de feedback

Los comentarios pueden obtenerse mediante:

* formularios;
* encuestas;
* correos;
* redes sociales;
* entrevistas;
* sistemas de soporte.

n8n permite centralizar esta información y enviarla automáticamente a un proceso de análisis.

En el workflow del curso, Google Sheets funciona como fuente de los comentarios.

### Análisis de sentimientos

El análisis de sentimientos clasifica textos como:

* positivos;
* negativos;
* neutrales.

El flujo general comprende:

1. recolección;
2. limpieza;
3. análisis;
4. clasificación;
5. interpretación;
6. acción posterior.

Los modelos de lenguaje pueden analizar comentarios difíciles de interpretar, aunque la calidad depende del contexto proporcionado y del prompt.

### Salida estructurada en JSON

El modelo recibe un system prompt que exige responder únicamente con JSON.

La estructura incluye datos como:

* cliente;
* sentimiento;
* resumen;
* sugerencia de mejora cuando corresponda.

Solicitar una salida estructurada facilita que los nodos posteriores procesen el resultado sin depender de texto libre.

Las APIs transportan datos en JSON, por lo que mantener estructuras válidas y predecibles es fundamental para que la información circule correctamente entre nodos.

### Detección de comentarios negativos

Después del análisis se utiliza un nodo `IF` para detectar los casos clasificados como negativos.

Solo esos elementos continúan hacia la rama de notificación, reduciendo mensajes innecesarios y permitiendo priorizar situaciones que requieren atención.

### Organización y envío de resultados

Un segundo modelo transforma la información técnica en un mensaje HTML legible para una persona no técnica.

El correo puede incluir:

* nombre del cliente;
* comentario original;
* sentimiento;
* resumen;
* sugerencia de mejora;
* formato visual con títulos y negritas.

Luego, Gmail envía la alerta al equipo responsable.

### Condiciones, bucles y procesamiento por lotes

Los workflows más complejos pueden combinar:

* condiciones mediante `IF`;
* múltiples rutas mediante `Switch`;
* procesamiento repetido mediante `Split in Batches`;
* integración con varias APIs.

Esto permite analizar grandes cantidades de comentarios y procesarlos uno por uno sin construir manualmente una operación para cada entrada.

## Aula 05 — Automatización completa de la atención al cliente

Esta aula reúne los conceptos anteriores en un agente capaz de recibir pedidos por correo, extraer información, registrarla y responder automáticamente.

### Recepción y registro de pedidos

El flujo comienza con Outlook como trigger.

Cuando llega un correo:

1. se obtienen los datos del mensaje;
2. el agente interpreta el pedido;
3. Google Sheets agrega una fila;
4. se genera una respuesta;
5. Outlook envía el mensaje al cliente.

La hoja de pedidos contiene campos como:

* fecha;
* canal;
* cliente;
* asunto;
* mensaje.

### Datos deterministas e inferidos

No todos los datos deberían ser calculados por la IA.

La información que ya existe en el sistema debe obtenerse directamente:

* fecha actual;
* remitente;
* asunto;
* cuerpo del correo.

Esto mejora la precisión y reduce el uso innecesario del modelo.

La IA debería reservarse para tareas que requieren interpretación, por ejemplo:

* determinar la intención;
* identificar el canal cuando no es explícito;
* resumir el pedido;
* generar una respuesta;
* clasificar la solicitud.

### System messages

El system message define el comportamiento general del agente.

Puede especificar:

* identidad;
* objetivo;
* herramientas disponibles;
* datos que debe registrar;
* restricciones;
* tono;
* formato de respuesta;
* situaciones que deben escalarse.

Cuanto más claras sean estas instrucciones, más consistente será el comportamiento del sistema.

### Agente de ventas

El agente construido en el curso recibe un pedido, registra los datos en Google Sheets y responde al cliente.

El flujo puede publicarse para operar automáticamente y revisar nuevos correos cada cierto intervalo.

Aunque el ejemplo utiliza un agente autónomo, las operaciones sensibles deberían incorporar validaciones o intervención humana antes de ejecutarse.

### Pruebas y depuración

Un workflow debería probarse en distintos niveles:

* **Prueba de nodo:** verifica cada componente por separado.
* **Prueba de integración:** comprueba que varios nodos intercambien correctamente los datos.
* **Prueba de extremo a extremo:** ejecuta el flujo completo desde el trigger hasta la acción final.

Para depurar se deben revisar:

* ejecuciones;
* datos de entrada y salida;
* mensajes de error;
* credenciales;
* expresiones;
* formatos;
* ramas condicionales.

### Escalabilidad

La evolución de una automatización puede dividirse en tres niveles:

1. **Agente individual:** ejecuta una tarea lineal.
2. **Sistema multiagente:** un orquestador delega tareas a agentes especializados.
3. **Sistema con memoria persistente:** conserva información de largo plazo y recupera contexto mediante búsqueda semántica.

En sistemas empresariales también son importantes:

* modularidad;
* observabilidad;
* manejo de errores;
* control de costos;
* memoria de corto y largo plazo;
* Human in the Loop;
* gobernanza de datos.

## Cierre del curso

Los principales conceptos trabajados fueron:

* automatización de procesos;
* nodos y triggers;
* Gmail y Outlook;
* Google Sheets;
* APIs y credenciales;
* ChatGPT y agentes de IA;
* system prompts;
* Edit Fields;
* nodos `IF` y `Switch`;
* clasificación de consultas;
* escalado a atención humana;
* análisis de datos;
* informes automatizados;
* memoria de agentes;
* análisis de sentimientos;
* salidas estructuradas en JSON;
* procesamiento por lotes;
* pruebas y depuración;
* automatización de pedidos;
* escalabilidad y sistemas multiagente.

La idea central del curso es que n8n permite combinar servicios, datos e Inteligencia Artificial para crear procesos completos. La IA aporta interpretación y generación de contenido, mientras que n8n controla el flujo, las condiciones, las herramientas y las acciones ejecutadas.
