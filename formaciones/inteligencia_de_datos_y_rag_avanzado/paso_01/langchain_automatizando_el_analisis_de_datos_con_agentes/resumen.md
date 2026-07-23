# Resumen del curso

El curso desarrolla un asistente de análisis de datos capaz de recibir archivos CSV, responder preguntas en lenguaje natural, generar informes exploratorios, calcular estadísticas descriptivas y producir visualizaciones.

La solución combina **Pandas**, **LangChain**, un modelo servido mediante **Groq**, herramientas personalizadas, un agente basado en el patrón **ReAct** y una interfaz web construida con **Streamlit**.

> El identificador de modelo utilizado en las clases pertenece a la configuración del curso. En una implementación actual debe reemplazarse por un modelo disponible y compatible con tool calling.

## Aula 01 — Preguntas sobre datos en archivos CSV

### Preparación de los datos

El proyecto comienza cargando un archivo CSV con Pandas:

```python
import pandas as pd

df = pd.read_csv("datos_entregas.csv")
```

Antes de automatizar el análisis conviene inspeccionar:

- primeras filas;
- nombres de columnas;
- tipos de datos;
- dimensiones;
- valores faltantes;
- duplicados;
- valores categóricos;
- posibles errores de formato.

Esta revisión inicial permite proporcionar al modelo información correcta sobre la estructura del DataFrame.

### Integración con un LLM

LangChain se utiliza para conectar la aplicación con un modelo disponible mediante Groq.

La API key debe obtenerse desde una variable de entorno y nunca escribirse directamente en el código:

```python
from os import getenv
from langchain_groq import ChatGroq

llm = ChatGroq(
    api_key=getenv("GROQ_API_KEY"),
    model="MODELO_COMPATIBLE",
    temperature=0,
)
```

Una temperatura baja resulta adecuada para tareas de análisis y generación de código, donde se busca reducir variaciones innecesarias.

### Generación de código

El modelo recibe una pregunta sobre el DataFrame y genera código Python para resolverla.

Ejemplos de operaciones posibles:

- promedios;
- medianas;
- correlaciones;
- agrupaciones;
- filtrados;
- conteos;
- estadísticas por categoría.

La respuesta del modelo no debe ejecutarse sin revisión. Puede contener columnas inexistentes, errores de sintaxis, supuestos incorrectos, operaciones demasiado costosas o instrucciones inseguras.

### `PythonAstREPLTool`

`PythonAstREPLTool` permite ejecutar expresiones de Python dentro de un contexto que contiene el DataFrame.

La herramienta puede conectarse al modelo mediante tool calling para que el LLM:

1. interprete la consulta;
2. genere una operación;
3. invoque la herramienta;
4. reciba el resultado;
5. produzca una respuesta.

También pueden utilizarse parsers para convertir las solicitudes de herramientas en una estructura más fácil de procesar.

### Riesgo de ejecución de código

La ejecución automática de código generado por un LLM es una operación de alto riesgo.

No debe realizarse en un sistema con acceso irrestricto a archivos personales, credenciales, red interna, comandos del sistema, bases de datos reales o variables de entorno sensibles.

Una versión pública necesita aislamiento, límites de recursos, validación de código y restricciones explícitas.

## Aula 02 — Respuestas explicativas y agentes

### Limitaciones de una cadena fija

Una chain sigue una secuencia previamente definida.

Puede resolver consultas simples, pero resulta limitada cuando la pregunta requiere varios cálculos, decisiones intermedias, selección dinámica de herramientas, corrección de un intento anterior o interpretación de resultados.

### Historial de conversación

`MessagesPlaceholder` permite incorporar mensajes anteriores dentro del prompt.

`ToolMessage` representa la respuesta producida por una herramienta y debe estar relacionada con la llamada correspondiente mediante su identificador.

El historial puede mejorar la continuidad, pero no garantiza por sí solo respuestas correctas o explicativas.

### Agentes

Un agente permite que el modelo decida dinámicamente qué pasos seguir.

Su ciclo general es:

1. analizar la pregunta;
2. elegir una herramienta;
3. ejecutarla;
4. observar el resultado;
5. decidir si necesita otra acción;
6. producir la respuesta final.

### Patrón ReAct

ReAct combina razonamiento y acción:

```text
Pregunta
→ razonamiento
→ acción
→ observación
→ nuevo razonamiento
→ respuesta final
```

Este patrón resulta útil cuando una consulta requiere más de una operación sobre el DataFrame.

### Agente para Pandas

LangChain ofrece agentes capaces de interactuar directamente con DataFrames.

En el curso se utiliza un agente con tool calling y trazas detalladas para observar los pasos ejecutados.

La opción `allow_dangerous_code=True` habilita ejecución de código potencialmente peligroso. Solo debe utilizarse en un ambiente controlado y nunca como configuración predeterminada de una aplicación pública.

### Motivo para crear herramientas propias

Los agentes predefinidos pueden presentar respuestas inconsistentes, idioma incorrecto, formatos difíciles de controlar, operaciones innecesarias o menor previsibilidad.

Las herramientas personalizadas permiten restringir el comportamiento y definir salidas específicas.

## Aula 03 — Herramientas personalizadas

### Creación de herramientas

LangChain permite crear herramientas mediante distintos niveles de abstracción.

#### Decorador `@tool`

Adecuado para funciones simples:

```python
from langchain_core.tools import tool

@tool
def ejemplo(entrada: str) -> str:
    """Descripción clara de la responsabilidad de la herramienta."""
    return entrada
```

#### `StructuredTool`

Permite definir explícitamente nombre, descripción, función, esquema de argumentos y comportamiento de retorno.

#### `BaseTool`

Proporciona mayor control para validaciones avanzadas, ejecución síncrona y asíncrona, integración con sistemas externos, manejo personalizado de errores e instrumentación.

### Importancia de la descripción

El agente utiliza el nombre y la descripción para decidir cuándo invocar una herramienta.

Una buena descripción debe aclarar qué tarea resuelve, cuándo debe utilizarse, qué entrada espera, qué salida genera y qué tareas no debe resolver.

### Herramienta exploratoria

La herramienta de información general resume la estructura del DataFrame mediante datos como:

- dimensiones;
- nombres y tipos de columnas;
- valores nulos;
- cadenas que representan valores faltantes;
- duplicados;
- posibles problemas de calidad.

El resultado técnico se entrega a una cadena que lo transforma en un informe explicativo.

### Herramienta estadística

La herramienta de estadísticas descriptivas utiliza operaciones de Pandas como:

```python
df.describe(include="number").transpose()
```

Luego, el modelo interpreta los resultados para explicar tendencia central, dispersión, mínimos y máximos, posibles valores atípicos, diferencias entre columnas y próximos análisis recomendados.

Los comentarios del modelo deben presentarse como interpretación y no como pruebas estadísticas concluyentes.

### Herramienta de visualización

La herramienta recibe una solicitud y genera código para construir un gráfico.

El prompt incluye información sobre columnas, tipos de datos, una muestra del DataFrame, el tipo de visualización solicitado y el formato esperado.

El código generado se ejecuta para obtener una figura de Matplotlib.

### Riesgos de `exec()`

Ejecutar el script generado mediante `exec()` permite realizar cualquier operación disponible en el entorno.

Antes de considerar una aplicación pública se necesitan medidas como:

- análisis de sintaxis;
- lista blanca de operaciones;
- bloqueo de imports;
- eliminación de acceso a `os`, `sys` y `subprocess`;
- entorno aislado;
- tiempo máximo de ejecución;
- límite de memoria;
- restricción de lectura y escritura;
- revisión de errores sin exponer secretos.

Limitar las variables globales entregadas a `exec()` reduce la superficie de ataque, pero no vuelve segura la ejecución por sí sola.

### Pruebas de visualización

Las herramientas deben probarse con solicitudes variadas, por ejemplo promedios por categoría, boxplots, distribuciones, conteos y comparación entre variables.

Además de comprobar que el gráfico se genera, se debe validar que las columnas existan, el tipo de gráfico sea apropiado, los ejes sean correctos, los datos estén agregados adecuadamente y el resultado no sea engañoso.

## Aula 04 — Orquestación de herramientas

### Catálogo de herramientas

El agente recibe un conjunto de herramientas con responsabilidades diferentes:

- información general del DataFrame;
- estadísticas descriptivas;
- visualizaciones;
- ejecución de análisis específicos.

Cada herramienta debe tener una función claramente diferenciada para reducir ambigüedades durante la selección.

### `return_direct`

Cuando `return_direct=True`, la salida de la herramienta puede devolverse directamente sin que el agente la reformule.

Es útil para resultados ya preparados, aunque debe utilizarse con cuidado cuando se necesita validación o explicación adicional.

### Prompt ReAct

El prompt orienta el comportamiento del agente y define el formato de interacción entre razonamiento, herramientas y observaciones.

La adaptación al análisis de datos incluye instrucciones en español, descripción del DataFrame, catálogo de herramientas, reglas para seleccionar acciones y formato de respuesta final.

El prompt debe evitar pedir que se exponga razonamiento interno detallado al usuario. Lo importante es que el agente entregue resultados, operaciones utilizadas y explicaciones verificables.

### Creación del agente

El agente ReAct se construye a partir de:

- el modelo;
- las herramientas;
- el prompt.

`AgentExecutor` se encarga de coordinar las iteraciones.

Configuraciones relevantes:

- herramientas disponibles;
- límite de iteraciones;
- manejo de errores de parsing;
- tiempo máximo;
- trazas de ejecución;
- estrategia de finalización.

### Evaluación del orquestador

El agente se prueba con tareas distintas: informe general, estadísticas descriptivas, preguntas específicas, comparaciones y generación de gráficos.

La prueba debe verificar no solo la respuesta final, sino también la herramienta elegida, los argumentos utilizados, las operaciones ejecutadas, la cantidad de iteraciones, los errores y la consistencia de los resultados.

## Aula 05 — Interfaz con Streamlit

### Migración desde notebook

El proyecto pasa de Google Colab a una estructura de aplicación local.

La raíz del curso contiene:

```text
.venv/
.env
requirements.txt
codigo/
```

El entorno se crea con:

```bash
python -m venv .venv
```

Las dependencias se instalan con:

```bash
python -m pip install -r requirements.txt
```

### Organización del código

Una separación posible es:

```text
codigo/
├── app.py
└── herramientas.py
```

`herramientas.py` puede contener la configuración del modelo, funciones de análisis, herramientas y creación del catálogo.

`app.py` puede encargarse de la interfaz, carga del CSV, creación del DataFrame, construcción del agente, interacción con el usuario y presentación de resultados.

### DataFrame como dependencia

En una aplicación real el DataFrame debe pasarse explícitamente a las herramientas.

Esto evita depender de variables globales creadas en un notebook y permite reconstruir el conjunto de herramientas cada vez que el usuario carga un archivo.

### Interfaz de Streamlit

La aplicación permite:

- cargar un CSV;
- visualizar una muestra;
- generar un informe general;
- obtener estadísticas descriptivas;
- hacer preguntas;
- solicitar gráficos.

Componentes habituales:

```python
st.file_uploader(...)
st.dataframe(...)
st.text_input(...)
st.button(...)
st.spinner(...)
st.markdown(...)
st.pyplot(...)
```

### Estado de la aplicación

Streamlit vuelve a ejecutar el script ante cada interacción.

Para conservar datos o resultados entre ejecuciones puede utilizarse:

```python
st.session_state
```

También pueden aplicarse mecanismos de caché para evitar cargar o procesar repetidamente el mismo archivo.

### Validación de archivos

Antes de procesar un CSV se debe comprobar:

- extensión;
- tamaño;
- codificación;
- delimitador;
- cantidad de filas y columnas;
- encabezados;
- tipos;
- datos sensibles;
- contenido inesperado.

Un archivo cargado por un usuario debe tratarse como entrada no confiable.

### Despliegue

La aplicación se publica conectando un repositorio de GitHub con Streamlit Community Cloud.

El repositorio debe incluir código, `requirements.txt` y archivos públicos necesarios.

La API key se configura mediante el sistema de secrets de la plataforma, no en un `.env` versionado.

### Limitaciones del despliegue gratuito

La versión gratuita puede imponer límites de memoria, CPU, aplicaciones activas, suspensión por inactividad y visibilidad del repositorio.

Es apropiada para prototipos y portfolio, pero no necesariamente para una aplicación productiva que ejecute código generado dinámicamente.

## Arquitectura final

El flujo general de la aplicación es:

1. el usuario carga un CSV;
2. Pandas crea el DataFrame;
3. la aplicación inspecciona su estructura;
4. se construyen herramientas asociadas al DataFrame;
5. el agente recibe una consulta;
6. selecciona la herramienta;
7. ejecuta el análisis;
8. interpreta el resultado;
9. presenta texto, tablas o gráficos en Streamlit.

## Buenas prácticas principales

- Inspeccionar los datos antes de analizarlos.
- No asumir que los tipos inferidos por Pandas son correctos.
- Mantener la API key fuera del código.
- Utilizar modelos compatibles con tool calling.
- Validar las respuestas estructuradas del modelo.
- Crear herramientas con responsabilidades concretas.
- Probar cada herramienta por separado.
- Limitar las iteraciones del agente.
- Registrar acciones y errores sin exponer información sensible.
- Verificar los resultados numéricos antes de explicarlos.
- Tratar archivos cargados como entradas no confiables.
- Evitar `allow_dangerous_code` y `exec()` fuera de entornos aislados.
- Separar la lógica de análisis de la interfaz.
- Fijar dependencias compatibles en `requirements.txt`.
- Configurar secretos mediante el servicio de despliegue.

## Seguridad y publicación

No deben versionarse:

```text
.env
.venv/
__pycache__/
.ipynb_checkpoints/
*.db
*.db-shm
*.db-wal
```

Antes de publicar el proyecto se debe comprobar que no contenga:

- API keys;
- archivos CSV con datos privados;
- conversaciones reales;
- rutas locales;
- código generado almacenado accidentalmente;
- logs sensibles;
- capturas con secretos;
- outputs excesivos de notebooks.

El principal riesgo técnico del proyecto es la ejecución de código generado por un LLM. Una aplicación demostrativa puede utilizar un dataset controlado, pero no debe presentarse como segura para archivos arbitrarios sin implementar aislamiento y controles adicionales.

## Conclusión

El curso muestra cómo evolucionar desde una consulta simple sobre un DataFrame hasta una aplicación con agentes, herramientas especializadas e interfaz web.

El aprendizaje más importante es que el modelo no reemplaza las operaciones de análisis. Su función es interpretar la solicitud, seleccionar herramientas y explicar resultados obtenidos mediante código verificable.

La flexibilidad de los agentes mejora la experiencia de uso, pero también introduce riesgos y menor previsibilidad. Por eso, el diseño debe combinar herramientas acotadas, validación, observabilidad y aislamiento.