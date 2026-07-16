# Resumen del curso

El curso desarrolla un workflow completo para automatizar parte del ciclo de revisión de pull requests. A lo largo del proyecto se integran GitHub, Gmail, Slack, Trello, las Data Tables de n8n y Gemini, combinando nodos visuales con lógica personalizada en JavaScript.

El flujo resultante permite detectar nuevas pull requests, registrar información para auditoría, solicitar una decisión humana, actualizar herramientas externas y complementar la revisión con un análisis generado por inteligencia artificial.

## Aula 01 — Introducción y primera automatización

### Arquitectura general del workflow

El proyecto parte de un evento ocurrido en GitHub: la creación o modificación de una pull request. A partir de ese evento, n8n recibe los datos y coordina acciones en otras aplicaciones.

La arquitectura inicial sigue una secuencia sencilla:

1. GitHub genera un evento.
2. El trigger de n8n recibe la información.
3. Los datos de la pull request se reutilizan mediante expresiones.
4. Gmail y otras integraciones envían notificaciones automáticas.

Este modelo introduce una idea central de n8n: los datos producidos por un nodo quedan disponibles para los siguientes, lo que permite construir mensajes, condiciones y acciones dinámicas.

### Triggers y datos dinámicos

Los triggers son los nodos que inician una ejecución. En este caso, el trigger de GitHub escucha eventos relacionados con pull requests dentro de un repositorio determinado.

La información recibida puede incluir:

* tipo de acción ejecutada;
* autor de la pull request;
* título;
* URL;
* repositorio;
* ramas involucradas;
* otros datos enviados por GitHub.

Estos valores pueden referenciarse desde nodos posteriores sin escribirlos manualmente, evitando configuraciones rígidas y permitiendo que el mismo workflow procese distintos eventos.

### Opciones de implementación de n8n

n8n puede utilizarse mediante diferentes modalidades.

#### n8n Cloud

Es la versión administrada por la plataforma. Reduce las tareas de instalación y mantenimiento, pero está sujeta a los límites y costos del plan contratado.

#### Instalación local

La versión self-hosted puede instalarse mediante Docker o npm. Es adecuada para aprendizaje, desarrollo y pruebas, ya que permite ejecutar workflows localmente sin depender de una suscripción.

Su principal limitación es que la instancia solo permanece disponible mientras la computadora y el proceso de n8n estén funcionando.

#### Servidor externo o VPS

Una instancia self-hosted también puede desplegarse en un servidor externo. Esto permite mantener los workflows disponibles permanentemente y conservar un mayor control sobre la infraestructura.

La elección entre cloud, instalación local y VPS depende de factores como:

* disponibilidad requerida;
* presupuesto;
* volumen de ejecuciones;
* mantenimiento;
* seguridad;
* cantidad de usuarios;
* necesidad de control sobre los datos.

### Organización mediante proyectos

Los proyectos de n8n permiten agrupar workflows, credenciales y miembros relacionados con un equipo o una finalidad específica.

Separar las automatizaciones por proyecto mejora:

* la asignación de responsabilidades;
* la colaboración;
* la gobernanza;
* el control de acceso;
* la organización de credenciales;
* la auditoría de ejecuciones;
* el mantenimiento de los workflows.

Los nombres de los proyectos deben describir claramente el proceso, producto o equipo al que pertenecen.

---

## Aula 02 — Control de flujo y decisiones humanas

### Integración con Slack

Slack se utiliza como canal de notificación y como interfaz para que una persona pueda intervenir en el workflow.

La integración puede realizarse utilizando:

* una conexión asociada a un usuario;
* una aplicación o bot de Slack.

El uso de un bot requiere crear una aplicación, asignar los permisos necesarios e instalarla dentro del workspace. Los scopes deben limitarse a las operaciones que realmente necesite el workflow, como leer canales o enviar mensajes.

Además, el bot debe formar parte del canal en el que intentará publicar. De lo contrario, la operación puede fallar aunque las credenciales sean válidas.

### Filtrado de eventos

Un trigger de GitHub puede activarse ante diferentes acciones relacionadas con una pull request. Por ejemplo, puede ejecutarse cuando se abre, actualiza o etiqueta.

Por este motivo, no alcanza con configurar el trigger: también es necesario validar el tipo de evento recibido.

El nodo **Filter** permite continuar únicamente cuando se cumple una condición. En este proyecto se utiliza para dejar pasar solo las acciones correspondientes a la apertura de una nueva pull request.

Este filtrado evita:

* notificaciones duplicadas;
* registros innecesarios;
* ejecuciones provocadas por eventos irrelevantes;
* decisiones tomadas sobre un contexto incorrecto.

### Diferencia entre Filter e If

Aunque ambos nodos evalúan condiciones, cumplen funciones distintas.

#### Filter

Permite continuar únicamente con los datos que cumplen una condición. Los elementos que no la cumplen dejan de avanzar por esa rama.

Es apropiado cuando los eventos inválidos o irrelevantes deben descartarse.

#### If

Divide el workflow en dos caminos:

* `true`, cuando la condición se cumple;
* `false`, cuando no se cumple.

Es apropiado cuando ambos resultados necesitan un tratamiento diferente.

En el workflow del curso, el nodo `If` se utiliza para separar las respuestas de aprobación y rechazo.

### Human in the Loop

El enfoque **Human in the Loop** incorpora una decisión humana dentro de un proceso automatizado.

En lugar de aprobar una pull request automáticamente, n8n envía la información a Slack y espera que una persona seleccione una opción. Mientras no exista una respuesta, la ejecución queda en espera.

Este patrón resulta especialmente útil cuando la automatización participa en decisiones:

* sensibles;
* difíciles de revertir;
* ambiguas;
* relacionadas con seguridad;
* que requieren responsabilidad humana.

La automatización prepara la información y ejecuta las acciones posteriores, pero conserva a una persona como responsable de la decisión final.

### Interacción con GitHub

Después de recibir la decisión desde Slack, el workflow puede crear una revisión, comentario u otra acción sobre la pull request.

Los valores necesarios deben obtenerse dinámicamente desde el evento original de GitHub, como el repositorio, el número de pull request y el autor.

Durante las pruebas también deben considerarse las restricciones de la plataforma. Por ejemplo, GitHub no permite que una persona apruebe su propia pull request. Cuando una acción real no puede probarse con una única cuenta, puede sustituirse temporalmente por un comentario o una operación equivalente que permita validar el flujo.

### Datos fijados para pruebas

La función de fijación de datos, o **pin data**, permite conservar la salida de un nodo y reutilizarla durante el desarrollo.

Esto facilita:

* probar nodos posteriores sin repetir llamadas externas;
* trabajar con datos consistentes;
* reducir ejecuciones innecesarias;
* depurar partes específicas del workflow.

Sin embargo, los datos fijados pueden quedar desactualizados o contener información sensible. Antes de exportar y publicar un workflow deben eliminarse o revisarse cuidadosamente.

---

## Aula 03 — Persistencia, auditoría y documentación

### Persistencia con Data Tables

Las Data Tables de n8n permiten almacenar información estructurada dentro de la plataforma.

En el proyecto se utilizan para mantener un registro de las pull requests procesadas. Cada fila puede contener datos como:

* propietario o autor;
* enlace de la pull request;
* estado de aprobación;
* estado de finalización;
* identificadores de seguimiento.

El nodo `Insert Row` agrega un registro cuando una nueva pull request supera las validaciones iniciales.

Posteriormente, `Update Rows` permite modificar ese mismo registro según la decisión recibida desde Slack o el resultado final del proceso.

Esta persistencia funciona como un sistema básico de:

* auditoría;
* trazabilidad;
* seguimiento;
* consulta histórica;
* depuración.

### Momento de persistencia

Los datos no deberían registrarse inmediatamente después del trigger si todavía no se comprobó que el evento sea válido.

Una secuencia más segura es:

1. recibir el evento;
2. validar el tipo de acción;
3. normalizar los datos necesarios;
4. insertar el registro;
5. continuar con las integraciones.

Esto evita guardar eventos que el workflow no debía procesar.

### Identificación de ejecuciones

Cada ejecución de n8n posee un identificador único accesible mediante:

```text
{{ $execution.id }}
```

Guardar este valor junto con los datos de negocio facilita relacionar un registro persistido con una ejecución concreta.

También puede utilizarse información destacada de ejecución para hacer que ciertos valores sean buscables desde la vista de ejecuciones.

La identificación explícita mejora la observabilidad porque permite:

* encontrar una ejecución específica;
* revisar qué datos recibió;
* localizar el nodo que falló;
* reconstruir el recorrido de un evento;
* relacionar logs internos con sistemas externos.

### Documentación dentro del workflow

Las Sticky Notes permiten incluir documentación directamente en el canvas de n8n.

Pueden utilizarse para explicar:

* el objetivo de una sección;
* requisitos previos;
* reglas de negocio;
* decisiones técnicas;
* credenciales necesarias;
* posibles errores;
* comportamiento de cada rama.

Las notas deben complementar la estructura visual, no reemplazar nombres descriptivos ni documentación externa cuando el proceso sea complejo.

### Nombres descriptivos

Renombrar nodos y credenciales mejora notablemente la legibilidad.

Un nombre como `Validar evento de PR` comunica mejor su propósito que `Filter1`. De la misma manera, una credencial debería identificar el servicio y el ambiente sin revelar información sensible.

La nomenclatura consistente simplifica la colaboración, la depuración y el mantenimiento.

---

## Aula 04 — Trello, JavaScript y manejo de errores

### Integración con Trello

Trello se incorpora para mantener sincronizado el estado de una tarea con el resultado de la pull request.

El workflow obtiene el identificador de una tarjeta desde el título de la pull request y utiliza ese dato para actualizarla.

Este enfoque requiere establecer una convención de nombres. Por ejemplo, el título de la pull request puede incluir el ID de la tarjeta al final.

Una convención solo es confiable cuando:

* está documentada;
* es validada antes de utilizarse;
* mantiene un formato estable;
* contempla el caso en que el dato no aparezca.

### Nodo Code y transformación de datos

El nodo `Code` permite ejecutar JavaScript para procesar información que no puede resolverse cómodamente mediante nodos visuales.

En el proyecto se utiliza para:

1. leer el título de la pull request;
2. dividir el texto mediante `split`;
3. extraer el identificador de Trello;
4. devolverlo como un campo estructurado.

Los nodos de código deben devolver los datos en el formato esperado por n8n. Incluso cuando se produce un único resultado, se retorna un array de objetos:

```javascript
return [
  {
    json: {
      idCard,
    },
  },
];
```

Mantener una salida estructurada permite que otros nodos puedan mapear, filtrar y reutilizar los valores correctamente.

### Obtención y filtrado de listas

Para mover una tarjeta es necesario conocer el ID de la lista de destino.

El workflow consulta las listas disponibles en el tablero y luego utiliza un filtro para conservar únicamente la que tenga el nombre esperado, por ejemplo `Hecho`.

Filtrar antes de actualizar la tarjeta evita que el nodo siguiente se ejecute una vez por cada lista devuelta.

### Validación de precondiciones

El código debe comprobar que el título incluya el identificador esperado antes de intentar utilizarlo.

Cuando el dato no existe, se puede lanzar un error explícito:

```javascript
throw new Error("ID de Trello no encontrado");
```

Un error descriptivo facilita la depuración y evita que el workflow continúe utilizando un valor incorrecto o inexistente.

### Rutas alternativas ante errores

Los errores no siempre deben detener toda la automatización.

n8n permite configurar el comportamiento de cada nodo para:

* detener la ejecución;
* continuar;
* reintentar;
* enviar el error por una salida alternativa.

La salida de error puede conectarse a una rama secundaria que:

* registre el problema;
* notifique a una persona;
* actualice el estado en una Data Table;
* omita una integración no esencial;
* ejecute un mecanismo alternativo.

Por ejemplo, si no existe un ID de Trello, el workflow puede completar el proceso de GitHub y Slack, pero registrar que la tarjeta no pudo actualizarse.

La estrategia adecuada depende de si la operación fallida es crítica para el objetivo principal del flujo.

---

## Aula 05 — Inteligencia artificial aplicada al workflow

### Analizar el proceso antes de automatizar

Antes de construir una automatización es necesario entender el proceso manual.

El análisis previo debe identificar:

* problema que se quiere resolver;
* evento que inicia el proceso;
* entradas necesarias;
* responsables;
* cuellos de botella;
* decisiones;
* excepciones;
* resultado esperado;
* métricas relevantes.

Automatizar un proceso mal definido puede trasladar sus problemas al workflow o incluso amplificarlos.

### Integración con Gemini

Gemini se incorpora como una capa adicional de análisis para revisar el contenido de una pull request.

Durante el curso se utiliza el diff de la pull request como contexto para que el modelo evalúe buenas prácticas y genere una recomendación.

El resultado se incluye en el mensaje enviado a Slack, proporcionando información adicional a la persona responsable de aprobar o rechazar los cambios.

La inteligencia artificial complementa la revisión humana, pero no reemplaza automáticamente la decisión final.

### Diseño del prompt

El prompt se divide en instrucciones con responsabilidades diferentes.

#### Rol o contexto

Define el perfil que debe adoptar el modelo y el tipo de análisis esperado.

#### Solicitud del usuario

Describe la tarea concreta, los datos disponibles y el objetivo del análisis.

#### Instrucciones del sistema

Establece reglas, criterios técnicos, restricciones y el formato de salida.

Separar estas funciones mejora la claridad y facilita ajustar cada parte sin reescribir toda la configuración.

### Respuestas estructuradas

Solicitar una salida JSON permite integrar la respuesta de la IA con la lógica del workflow.

Una estructura posible contiene:

```json
{
  "aprobado": true,
  "recomendacion": "Descripción breve",
  "comentario": "Observaciones técnicas"
}
```

La estructura debe definirse con campos claros y tipos previsibles. Esto reduce la ambigüedad y permite utilizar los valores en nodos posteriores.

### Parseo y validación

La respuesta generada puede procesarse mediante un nodo `Code` para convertir el texto JSON en datos utilizables por n8n.

Después del parseo, un nodo `If` puede evaluar el campo booleano de aprobación y dirigir el workflow hacia ramas diferentes.

Las respuestas de un modelo generativo no deben asumirse como válidas sin comprobación. Conviene validar:

* que la respuesta exista;
* que sea JSON válido;
* que incluya todos los campos requeridos;
* que los campos tengan el tipo esperado;
* que exista una ruta alternativa ante errores.

### Pruebas con Edit Fields

El nodo `Edit Fields` permite modificar o forzar valores durante el desarrollo.

Esto facilita probar distintos escenarios sin volver a ejecutar todas las integraciones:

* resultado aprobado;
* resultado rechazado;
* respuesta incompleta;
* valores inesperados;
* ausencia de datos.

Las pruebas controladas permiten validar las ramas condicionales y el formato de los mensajes antes de conectar nuevamente los servicios reales.

---

## Arquitectura final del workflow

El workflow completo combina las siguientes etapas:

1. GitHub informa un evento relacionado con una pull request.
2. Un filtro comprueba que la acción sea relevante.
3. La pull request se registra en una Data Table.
4. Se guarda información para auditoría y trazabilidad.
5. Gemini analiza el diff y devuelve una respuesta estructurada.
6. Slack muestra los datos de la pull request y el análisis de la IA.
7. Una persona aprueba o rechaza la operación.
8. Un nodo `If` separa ambos resultados.
9. GitHub recibe una revisión, comentario o acción equivalente.
10. Trello actualiza la tarjeta relacionada cuando existe un identificador válido.
11. La Data Table registra el resultado final.
12. Las ramas de error documentan o notifican los problemas encontrados.

## Buenas prácticas principales

* Filtrar los eventos inmediatamente después del trigger.
* Utilizar nombres descriptivos para nodos, credenciales y campos.
* Mantener las decisiones sensibles bajo supervisión humana.
* Persistir identificadores que permitan rastrear cada ejecución.
* Validar los datos antes de enviarlos a servicios externos.
* Definir rutas específicas para errores esperables.
* Devolver información estructurada desde los nodos de código.
* Solicitar respuestas estructuradas a los modelos de IA.
* Validar y parsear las respuestas generadas antes de usarlas.
* Utilizar datos fijados y campos editables solo como herramientas de prueba.
* Documentar reglas de negocio y convenciones directamente en el workflow.
* Limitar los permisos de las integraciones al mínimo necesario.

## Seguridad

Las credenciales de GitHub, Google, Slack, Trello y Gemini deben administrarse mediante el sistema de credenciales de n8n y nunca escribirse directamente dentro de nodos de código, prompts o campos exportables.

Antes de publicar el workflow deben revisarse especialmente:

* tokens;
* API keys;
* secretos de aplicaciones;
* URLs de webhooks;
* IDs privados;
* direcciones de correo;
* nombres de canales o workspaces;
* datos de pull requests reales;
* valores almacenados mediante `pinData`;
* información persistida en Data Tables.

El archivo exportado debe contener únicamente la estructura reutilizable de la automatización.

## Conclusión

El proyecto muestra cómo n8n puede utilizarse para coordinar un proceso de desarrollo que involucra eventos, notificaciones, persistencia, decisiones humanas, herramientas de gestión e inteligencia artificial.

El principal aprendizaje no consiste únicamente en conectar servicios, sino en diseñar workflows observables, mantenibles y resistentes a errores. La automatización debe validar sus entradas, registrar lo ocurrido, manejar excepciones y mantener intervención humana en las decisiones que no conviene delegar completamente.
