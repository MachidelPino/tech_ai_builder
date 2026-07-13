# Resumen del curso

## Aula 01 — Comenzando con n8n

Esta aula introduce **n8n** como una plataforma de automatización de workflows que permite conectar aplicaciones, servicios, APIs y herramientas de Inteligencia Artificial mediante una interfaz visual basada en nodos.

Puede utilizarse para automatizar tareas en áreas como operaciones, seguridad, desarrollo, ventas y gestión de información, integrando servicios como Gmail, Google Sheets, Google Drive, Slack, Telegram, Gemini y otras plataformas.

### Workflows, nodos y triggers

Un workflow representa un proceso automatizado compuesto por nodos conectados.

Los elementos principales son:

* **Trigger:** evento que inicia la automatización.
* **Nodo:** acción o transformación ejecutada dentro del flujo.
* **Conexión:** define cómo pasan los datos entre nodos.
* **Credencial:** autorización utilizada para acceder a un servicio externo.
* **Ejecución:** instancia concreta en la que se procesa el workflow.

Los triggers pueden activarse:

* manualmente;
* en horarios determinados;
* cuando ocurre un evento en una aplicación;
* mediante webhooks;
* al recibir nuevos datos.

### Primer flujo: Gmail y Google Sheets

Se construye un workflow que detecta correos nuevos en Gmail y registra su información en Google Sheets.

El flujo sigue estos pasos:

1. Gmail detecta un mensaje nuevo.
2. n8n obtiene los datos del correo.
3. Se extraen campos como remitente, destinatario y contenido.
4. Google Sheets agrega una nueva fila con esa información.
5. El workflow se activa para ejecutarse automáticamente.

Este ejemplo muestra cómo mapear datos producidos por un nodo hacia los campos requeridos por el siguiente.

### Variables en n8n

Las variables permiten almacenar y reutilizar valores dentro de los workflows.

Pueden utilizarse para:

* URLs;
* configuraciones;
* valores temporales;
* resultados intermedios;
* parámetros compartidos;
* referencias utilizadas por varios nodos.

Las variables reducen duplicación y facilitan el mantenimiento. Los datos sensibles deben gestionarse mediante credenciales o variables de entorno, no escribirse directamente en los nodos.

## Aula 02 — Conexión con LLMs

Esta aula integra búsquedas web y modelos de lenguaje dentro de un workflow.

El flujo principal busca información reciente, procesa los resultados con Gemini y genera contenido listo para publicar.

### Chat Trigger

Se utiliza un `Chat Trigger` para iniciar el workflow a partir de un mensaje del usuario.

El texto recibido puede utilizarse dinámicamente como término de búsqueda o entrada para otros nodos.

### Búsqueda web con Tavily

Tavily se integra mediante una API key y permite configurar aspectos como:

* consulta;
* período temporal;
* cantidad máxima de resultados;
* inclusión del contenido completo de las páginas.

La salida contiene una colección de resultados con datos como título, URL y contenido.

### Procesamiento de colecciones

Los resultados obtenidos pueden necesitar transformaciones antes de enviarse al modelo.

Se utilizan nodos como:

* **Split Out:** separa una colección en elementos individuales.
* **Aggregate:** vuelve a reunir varios elementos en una única estructura.

Un flujo típico puede:

1. obtener varias páginas;
2. separar cada resultado;
3. resumirlos individualmente;
4. agrupar los resúmenes;
5. generar un contenido final.

### Integración con Gemini

Gemini se conecta mediante una credencial obtenida desde Google AI Studio.

En el ejemplo, el modelo se utiliza para:

* resumir cada noticia;
* seleccionar información importante;
* combinar varios resúmenes;
* generar una publicación para LinkedIn;
* adaptar tono, estructura y hashtags.

La calidad de la salida depende en gran medida de las instrucciones incluidas en el prompt.

### Ejemplo de automatización completa

Un flujo de generación de contenido puede seguir esta secuencia:

1. recibir un tema mediante chat;
2. buscar información reciente con Tavily;
3. separar los resultados;
4. resumir cada fuente con Gemini;
5. agrupar los resúmenes;
6. crear una publicación final;
7. enviar o publicar el contenido mediante otra integración.

El mismo patrón puede utilizarse para enriquecimiento de leads, generación de correos personalizados o procesamiento de información externa.

### Seguridad con OAuth 2

OAuth 2 permite autorizar aplicaciones sin compartir directamente la contraseña de una cuenta.

Las notificaciones de seguridad ayudan a:

* detectar accesos no reconocidos;
* revisar qué aplicaciones tienen permisos;
* auditar nuevas conexiones;
* revocar autorizaciones sospechosas.

Las cuentas utilizadas en automatizaciones deben revisarse periódicamente y recibir alertas de seguridad.

## Aula 03 — Funciones útiles en n8n

Esta aula trabaja con condiciones, generación automática de respuestas y prompts dinámicos.

### Nodo IF

El nodo `IF` divide un workflow según una condición.

Cada elemento puede seguir una de dos rutas:

* `true`, si cumple la condición;
* `false`, si no la cumple.

Las condiciones pueden evaluar:

* texto;
* números;
* fechas;
* booleanos;
* existencia de campos;
* contenido de direcciones de correo.

### Clasificación de correos

Se crea un flujo que detecta nuevos mensajes de Gmail y los separa según el dominio del remitente.

Ejemplo:

1. Gmail recibe un correo.
2. El nodo `IF` verifica el campo `From`.
3. Si el remitente pertenece a un dominio específico, continúa hacia Gemini.
4. Gemini genera una respuesta.
5. Gmail responde dentro del hilo original.

Para mantener la conversación correcta, el nodo de respuesta debe utilizar el identificador del mensaje o del hilo recibido por el trigger.

### Prompts dentro de workflows

Un prompt eficaz debe indicar:

* tarea;
* contexto;
* tono;
* restricciones;
* formato de salida;
* datos dinámicos que debe utilizar.

En una automatización de correo, también conviene indicar que el modelo devuelva únicamente el cuerpo del mensaje, sin explicaciones adicionales ni comentarios técnicos.

Los prompts pueden incorporar expresiones de n8n para insertar datos provenientes de nodos anteriores.

## Aula 04 — Low Code y generación de JSON

Esta aula introduce el uso de JSON y código personalizado dentro de n8n.

### JSON

JSON es un formato utilizado para representar e intercambiar datos.

Sus estructuras principales son:

* **Objeto:** conjunto de pares clave-valor entre llaves `{}`.
* **Array:** lista ordenada de valores entre corchetes `[]`.

Los valores pueden ser:

* texto;
* números;
* booleanos;
* listas;
* objetos anidados;
* valores nulos.

Ejemplo:

```json
{
  "nombre": "María",
  "edad": 28,
  "activo": true
}
```

JSON resulta especialmente importante en n8n porque los nodos intercambian información mediante estructuras similares.

### Código personalizado

El nodo de código permite ejecutar JavaScript o Python para realizar transformaciones que no pueden resolverse fácilmente mediante nodos visuales.

Puede utilizarse para:

* generar listas;
* crear objetos JSON;
* recorrer elementos;
* calcular valores;
* cambiar estructuras;
* normalizar datos;
* preparar entradas para nodos posteriores.

En el ejemplo se genera una lista de usuarios con campos como nombre, edad y estado de actividad. Luego, el nodo `IF` filtra los usuarios activos.

### Low code

n8n combina una interfaz visual con la posibilidad de escribir código.

Los nodos visuales son adecuados para operaciones comunes, mientras que el código permite resolver transformaciones más específicas.

La idea no es reemplazar todos los nodos con código, sino utilizarlo cuando simplifica el workflow o permite implementar lógica que no está disponible directamente.

### Condiciones con datos estructurados

Los valores booleanos pueden emplearse para controlar el flujo.

Por ejemplo:

```json
{
  "nombre": "María",
  "activo": true
}
```

El nodo `IF` puede comprobar `activo` y ejecutar una acción solamente cuando su valor sea verdadero.

## Aula 05 — Conexión con herramientas de Google

Esta aula construye un workflow activado por archivos agregados a Google Drive.

El objetivo es detectar archivos nuevos, descargarlos, procesarlos con IA y generar contenido a partir de ellos.

### Google Cloud y OAuth

Conectar Google Drive con n8n requiere configurar credenciales en Google Cloud.

El proceso general incluye:

1. crear un proyecto;
2. habilitar Google Drive API;
3. configurar la pantalla de consentimiento OAuth;
4. crear un cliente OAuth para aplicación web;
5. registrar la URI de redirección de n8n;
6. obtener `Client ID` y `Client Secret`;
7. agregar usuarios de prueba si la aplicación no está verificada;
8. completar la autorización desde n8n.

El `Client Secret` y otras credenciales no deben incluirse en exportaciones públicas del workflow.

### Trigger de Google Drive

El trigger detecta la creación de archivos dentro de una carpeta determinada.

A partir de ese evento, el workflow puede:

* consultar metadatos;
* descargar el archivo;
* identificar su tipo;
* enviarlo a otro servicio;
* moverlo después de procesarlo.

### Procesamiento de audio con IA

El ejemplo trabaja con archivos de audio:

1. se agrega un archivo a Google Drive;
2. el trigger inicia el workflow;
3. el archivo se descarga;
4. Gemini genera una transcripción;
5. la transcripción se utiliza para crear contenido;
6. opcionalmente, se genera una imagen relacionada;
7. el resultado queda preparado para una publicación.

Este patrón puede adaptarse a documentos, imágenes, archivos CSV o PDFs.

### Tipos de datos y coerción

n8n trabaja con distintos tipos de datos:

* strings;
* números;
* booleanos;
* fechas;
* objetos;
* arrays;
* archivos binarios.

La coerción ocurre cuando un valor se convierte automáticamente de un tipo a otro. Puede provocar errores, por ejemplo al comparar un número almacenado como texto.

Es preferible realizar conversiones explícitas para asegurar que:

* las condiciones funcionen correctamente;
* las operaciones matemáticas usen números;
* los booleanos no sean interpretados como texto;
* los nodos reciban el formato esperado.

## Cierre del curso

Los principales conceptos trabajados fueron:

* workflows;
* nodos y conexiones;
* triggers;
* credenciales;
* Gmail;
* Google Sheets;
* Google Drive;
* Google Cloud;
* Tavily;
* Gemini;
* OAuth 2;
* prompts dinámicos;
* Split Out y Aggregate;
* condiciones con `IF`;
* JSON;
* ejecución de código;
* tipos de datos;
* procesamiento automático de archivos.

La idea central del curso es que n8n permite automatizar procesos conectando aplicaciones, datos e Inteligencia Artificial en workflows visuales. Los nodos resuelven operaciones comunes, mientras que las expresiones y el código permiten adaptar los flujos a necesidades más específicas.
