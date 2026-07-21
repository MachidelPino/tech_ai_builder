# Oracle Cloud Infrastructure

Formación de **ONE AI for Tech** orientada a la construcción, publicación y gestión de aplicaciones en la nube mediante **Oracle Cloud Infrastructure (OCI)**.

El recorrido abarca desde la configuración inicial de servidores y redes hasta el despliegue de aplicaciones, el trabajo con bases de datos, la automatización de infraestructura y la aplicación de prácticas de seguridad, disponibilidad y escalabilidad.

## Información general

- **Programa:** ONE AI for Tech
- **Escuela:** DevOps
- **Tipo:** Formación
- **Plataforma:** Alura
- **Duración estimada:** 16 horas
- **Cursos:** 2
- **Certificado de formación:** Sí
- **Estado:** No iniciada
- **Progreso actual:** 0 de 2 cursos completados

## Objetivo de la formación

Aprender a crear, publicar y administrar aplicaciones en la nube utilizando los principales servicios de Oracle Cloud Infrastructure.

La formación propone desarrollar una visión práctica de infraestructura moderna, incluyendo servidores, redes, bases de datos, despliegue de aplicaciones, automatización y seguridad.

## Objetivos de aprendizaje

Al completar la formación, se espera poder:

- comprender los conceptos fundamentales de cloud computing;
- configurar recursos dentro de Oracle Cloud Infrastructure;
- crear y administrar servidores en la nube;
- estructurar redes virtuales;
- gestionar accesos y permisos;
- desplegar aplicaciones dinámicas;
- implementar operaciones CRUD;
- publicar sitios estáticos;
- trabajar con bases de datos en la nube;
- automatizar infraestructura mediante código;
- aplicar prácticas de seguridad;
- comprender estrategias de balanceo de carga;
- preparar aplicaciones para escenarios de alta disponibilidad;
- analizar criterios básicos de escalabilidad.

## Organización del recorrido

La formación presenta un único paso que reúne dos cursos complementarios sobre despliegue, bases de datos e infraestructura como código.

> Esta organización corresponde al recorrido interno de la formación y no implica un orden obligatorio respecto de las demás formaciones del programa Tech AI Builder.

### Paso 01 — Oracle Cloud Infrastructure

| Tipo | Contenido | Estado |
|---|---|---|
| Curso | Oracle Cloud Infrastructure: implementación de una aplicación en la nube | Pendiente |
| Curso | Oracle Cloud Infrastructure: base de datos e infraestructura como código | Pendiente |

## Cursos incluidos

### 1. Oracle Cloud Infrastructure: implementación de una aplicación en la nube

Curso orientado a la creación y publicación de una aplicación utilizando servicios de OCI.

Los temas generales de la formación indican que este recorrido puede incluir:

- configuración de servidores;
- redes virtuales;
- gestión de accesos;
- despliegue de aplicaciones;
- operaciones CRUD;
- alojamiento de contenido estático;
- seguridad y disponibilidad.

**Estado:** Pendiente

### 2. Oracle Cloud Infrastructure: base de datos e infraestructura como código

Curso enfocado en la integración de bases de datos en la nube y en la automatización de recursos de infraestructura.

Los temas generales de la formación indican que este recorrido puede incluir:

- bases de datos administradas;
- conexión entre aplicaciones y servicios de datos;
- automatización de infraestructura;
- infraestructura como código;
- seguridad;
- escalabilidad;
- balanceo de carga;
- alta disponibilidad.

**Estado:** Pendiente

> Los contenidos específicos de cada curso se documentarán a partir de sus respectivas descripciones y aulas. No se asumen herramientas o servicios concretos que todavía no hayan sido informados.

## Contenidos principales

- cloud computing;
- Oracle Cloud Infrastructure;
- servidores en la nube;
- redes virtuales;
- gestión de identidades y accesos;
- despliegue de aplicaciones;
- operaciones CRUD;
- alojamiento de sitios estáticos;
- bases de datos en la nube;
- automatización de infraestructura;
- infraestructura como código;
- seguridad;
- balanceo de carga;
- alta disponibilidad;
- escalabilidad.

## Herramientas y servicios

La herramienta principal de la formación es:

- Oracle Cloud Infrastructure.

Los servicios concretos de OCI, lenguajes, frameworks y herramientas de automatización se documentarán en los README de cada curso cuando aparezcan en el contenido oficial.

## Estructura de documentación

Cada curso tendrá como base la siguiente organización:

```text
nombre-del-curso/
├── README.md
├── resumen.md
└── certificado/
```

Cuando el contenido lo justifique, también podrán incorporarse:

```text
codigo/
recursos/
images/
```

No se crearán carpetas adicionales por aula salvo que exista una necesidad concreta de organización.

## Criterio de documentación

La documentación de esta formación seguirá estos principios:

- resumir los conceptos técnicos con redacción propia;
- evitar reproducir de forma extensa el contenido de Alura;
- conservar decisiones de arquitectura y buenas prácticas;
- documentar los recursos de OCI utilizados en cada práctica;
- incluir código o archivos de infraestructura solo cuando aporten valor;
- evitar publicar configuraciones temporales o específicas de una cuenta personal;
- priorizar una estructura clara y útil para portfolio;
- documentar los costos, límites o restricciones solo cuando sean relevantes para una práctica.

## Seguridad

Los proyectos de infraestructura requieren una revisión especialmente cuidadosa antes de publicarse.

No deben versionarse:

- contraseñas;
- claves privadas;
- API keys;
- tokens;
- archivos de configuración con credenciales;
- identificadores sensibles de cuentas;
- datos reales almacenados en bases de datos;
- secretos de aplicaciones;
- archivos de estado que expongan información de infraestructura.

También deben revisarse antes de publicar:

- direcciones IP públicas;
- OCIDs;
- nombres de tenancy o compartments;
- URLs activas de servicios;
- reglas de red;
- archivos de configuración de OCI;
- scripts que contengan credenciales;
- capturas del panel con información de la cuenta.

Archivos comunes que deben mantenerse fuera del repositorio:

```gitignore
.env
.venv/
__pycache__/
.ipynb_checkpoints/
*.db
*.db-shm
*.db-wal
*.pem
*.key
```

Si se utilizan herramientas de infraestructura como código, sus archivos de estado tampoco deben publicarse cuando contengan identificadores, recursos o datos sensibles.

## Certificados

Cada certificado se almacenará dentro del directorio del curso correspondiente:

```text
nombre-del-curso/
└── certificado/
```

No se utilizará una carpeta global de certificados.

## Estado de la formación

- **Estado actual:** No iniciada
- **Progreso:** 0 de 2 cursos
- **Certificado de formación:** Pendiente