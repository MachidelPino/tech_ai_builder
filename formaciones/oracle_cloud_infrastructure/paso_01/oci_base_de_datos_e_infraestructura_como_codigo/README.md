# Oracle Cloud Infrastructure: base de datos e infraestructura como código

Curso de la formación **Oracle Cloud Infrastructure** de **ONE AI for Tech**, orientado a conectar una aplicación con servicios de datos y almacenamiento de OCI, habilitar acceso mediante HTTPS y automatizar infraestructura con Terraform.

## Información general

- **Programa:** ONE AI for Tech
- **Formación:** Oracle Cloud Infrastructure
- **Categoría:** Cursos de Cloud Computing
- **Plataforma:** Alura
- **Carga horaria:** 8 horas
- **Cantidad de aulas:** 4
- **Estado:** Finalizado
- **Certificado:** Obtenido

> Las duraciones visibles de las aulas suman 2 h 54 min. La carga horaria informada por la plataforma también puede contemplar lecturas, ejercicios y prácticas.

## Objetivo del curso

Aprender a ampliar una aplicación desplegada en OCI mediante una base de datos en la nube, una API desarrollada con Node.js, almacenamiento de objetos, conexión HTTPS e infraestructura como código.

## Contenido del curso

| Aula | Tema | Duración | Estado |
|---|---|---:|---|
| 01 | Bases de datos en OCI | 40 min | Completado |
| 02 | Conectando una API y la base de datos | 48 min | Completado |
| 03 | Almacenamiento | 59 min | Completado |
| 04 | Infraestructura como código | 27 min | Completado |

## Detalle de aulas

### Aula 01 — Bases de datos en OCI

Introducción a las alternativas de bases de datos disponibles en Oracle Cloud Infrastructure.

Contenidos principales:

- bases de datos en la nube;
- criterios para seleccionar una base de datos;
- creación de una base de datos autónoma;
- características de las bases de datos Oracle;
- diferencias generales entre bases relacionales y no relacionales.

### Aula 02 — Conectando una API y la base de datos

Preparación y despliegue de una API en una instancia de OCI.

Contenidos principales:

- configuración del ambiente;
- estructura de una aplicación Node.js;
- despliegue de una API en OCI;
- ejecución del servicio;
- pruebas de una API REST;
- conexión con la base de datos;
- configuración del acceso a la aplicación.

### Aula 03 — Almacenamiento

Uso de servicios de almacenamiento para publicar contenido y proteger el acceso a la aplicación.

Contenidos principales:

- alternativas de almacenamiento en OCI;
- niveles de acceso;
- publicación de contenido mediante Object Storage;
- selección del tipo de almacenamiento adecuado;
- configuración de SSL en el load balancer;
- acceso mediante HTTPS.

### Aula 04 — Infraestructura como código

Introducción a la automatización de recursos de infraestructura.

Contenidos principales:

- fundamentos de Infrastructure as Code;
- administración de recursos mediante OCI Resource Manager;
- definición de infraestructura con Terraform;
- automatización y reproducibilidad;
- ventajas y criterios de uso de IaC.

## Conceptos principales

### Bases de datos en la nube

Los servicios de bases de datos administradas reducen parte del trabajo operativo relacionado con instalación, mantenimiento y disponibilidad.

La elección del servicio debe considerar:

- modelo de datos;
- volumen y patrones de acceso;
- escalabilidad;
- disponibilidad;
- integración con la aplicación;
- seguridad;
- costos.

### Autonomous Database

Servicio administrado de Oracle orientado a automatizar tareas operativas de una base de datos, como aprovisionamiento, mantenimiento y determinadas optimizaciones.

### Aplicación Node.js en OCI

La API se ejecuta sobre una instancia de cómputo y se conecta con la base de datos para exponer operaciones mediante HTTP.

La publicación requiere coordinar:

- dependencias de la aplicación;
- variables de entorno;
- proceso de ejecución;
- permisos de red;
- acceso a la base de datos;
- pruebas de los endpoints.

### API REST

Una API REST organiza el acceso a recursos mediante endpoints y operaciones HTTP.

Las pruebas deben comprobar tanto las respuestas esperadas como los errores de validación, conexión y autorización.

### Object Storage

Servicio destinado a almacenar objetos como archivos, imágenes, respaldos y contenido estático.

Los buckets y objetos pueden configurarse con distintos niveles de acceso. El contenido no debe hacerse público salvo que el caso de uso lo requiera explícitamente.

### SSL y HTTPS

HTTPS protege la comunicación entre el cliente y la aplicación mediante cifrado.

En la arquitectura del curso, el certificado se configura en el load balancer, que recibe las conexiones seguras y distribuye el tráfico hacia los backends.

### Infraestructura como código

Infrastructure as Code permite describir recursos mediante archivos versionables y reproducibles.

Entre sus beneficios se encuentran:

- consistencia entre ambientes;
- revisión de cambios;
- reducción de configuraciones manuales;
- reutilización;
- automatización;
- trazabilidad.

### Terraform

Terraform utiliza archivos declarativos para definir el estado deseado de la infraestructura.

Un flujo habitual incluye:

1. definir proveedores y recursos;
2. inicializar el proyecto;
3. revisar el plan;
4. aplicar los cambios;
5. conservar el estado de forma segura;
6. destruir recursos cuando dejan de ser necesarios.

### OCI Resource Manager

Servicio de OCI que permite ejecutar y administrar configuraciones de Terraform dentro de Oracle Cloud.

## Arquitectura trabajada

El curso amplía la infraestructura del curso anterior con los siguientes componentes:

1. aplicación Node.js desplegada en una instancia;
2. API REST conectada a una base de datos autónoma;
3. contenido estático alojado en Object Storage;
4. load balancer configurado con SSL;
5. acceso público mediante HTTPS;
6. recursos definidos o administrados con Terraform y OCI Resource Manager.

## Resumen del curso

Los apuntes técnicos filtrados y organizados por aula se almacenarán en:

[`resumen.md`](./resumen.md)

## Prácticas y código

Los archivos reutilizables del curso se organizarán según su función:

```text
codigo/
```

Si las prácticas de Terraform justifican una separación clara, puede utilizarse:

```text
codigo/
├── api/
└── terraform/
```

Esta división solo debe aplicarse cuando refleje la estructura real del material desarrollado.

## Seguridad

Antes de publicar la aplicación o los archivos de infraestructura se debe comprobar que no contengan:

- contraseñas o cadenas de conexión;
- credenciales de la base de datos;
- claves privadas;
- tokens;
- OCIDs sensibles;
- datos de la tenancy;
- certificados privados;
- archivos wallet de Oracle Database;
- variables con secretos;
- direcciones o endpoints que no deban exponerse.

No deben versionarse:

```gitignore
.env
.oci/
*.pem
*.key
.terraform/
terraform.tfstate
terraform.tfstate.*
crash.log
```

Los archivos `*.tfvars` deben revisarse antes de publicarse y mantenerse fuera del repositorio cuando incluyan secretos o datos específicos de una cuenta.

El archivo `.terraform.lock.hcl` puede versionarse para mantener consistentes las versiones de los proveedores.

También deben aplicarse estas prácticas:

- limitar el acceso de red a la base de datos;
- utilizar variables de entorno en la API;
- evitar buckets públicos innecesarios;
- proteger el estado de Terraform;
- revisar el plan antes de aplicar cambios;
- eliminar recursos de práctica cuando ya no se utilicen.

## Certificado

El certificado se almacenará en:

```text
certificado/
```

**Estado:** Obtenido

## Estado actual

- **Curso:** Finalizado
- **Aulas completadas:** 4 de 4
- **Certificado:** Obtenido
