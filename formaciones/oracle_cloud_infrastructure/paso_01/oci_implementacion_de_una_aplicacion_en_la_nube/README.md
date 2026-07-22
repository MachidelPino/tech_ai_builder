# Oracle Cloud Infrastructure: implementación de una aplicación en la nube

Curso de la formación **Oracle Cloud Infrastructure** de **ONE AI for Tech**, orientado a comprender la arquitectura básica de OCI y desplegar una aplicación sobre recursos de cómputo, red y balanceo de carga.

## Información general

- **Programa:** ONE AI for Tech
- **Formación:** Oracle Cloud Infrastructure
- **Categoría:** Cursos de Cloud Computing
- **Plataforma:** Alura
- **Carga horaria:** 8 horas
- **Cantidad de aulas:** 5
- **Estado:** No iniciado
- **Certificado:** Pendiente

## Objetivo del curso

Aprender a configurar una infraestructura inicial en Oracle Cloud Infrastructure para publicar una aplicación, incluyendo la creación de una cuenta, la organización de recursos, la configuración de redes virtuales, el aprovisionamiento de instancias y el uso de un balanceador de carga.

## Contenido del curso

| Aula | Tema | Duración | Estado |
|---|---|---:|---|
| 01 | Computación en la nube | 13 min | Pendiente |
| 02 | Cuenta Free Tier OCI | 26 min | Pendiente |
| 03 | Arquitectura OCI | 40 min | Pendiente |
| 04 | Redes | 18 min | Pendiente |
| 05 | Compute | 49 min | Pendiente |

## Detalle de aulas

### Aula 01 — Computación en la nube

Introducción a los conceptos básicos de cloud computing, sus ventajas y los motivos para utilizar infraestructura bajo demanda.

### Aula 02 — Cuenta Free Tier OCI

Creación de una cuenta en Oracle Cloud, revisión del modo gratuito y navegación inicial por la consola de OCI.

### Aula 03 — Arquitectura OCI

Presentación de la estructura general de Oracle Cloud Infrastructure y de los componentes utilizados para organizar y administrar recursos:

- compartments;
- usuarios;
- Identity and Access Management;
- Cloud Shell.

### Aula 04 — Redes

Introducción a las redes en OCI y configuración de una **Virtual Cloud Network (VCN)** para conectar instancias y otros recursos.

### Aula 05 — Compute

Creación y configuración de instancias de cómputo dentro de la VCN, instalación del software necesario, despliegue de una segunda instancia y configuración de un load balancer.

## Conceptos principales

### Cloud computing

Modelo que permite consumir recursos de infraestructura de forma remota y bajo demanda, reduciendo la necesidad de administrar hardware propio.

### Compartments

Contenedores lógicos utilizados para organizar recursos dentro de OCI y aplicar políticas de acceso de forma ordenada.

### IAM

Sistema de gestión de identidades, usuarios, grupos y permisos de Oracle Cloud Infrastructure.

### Cloud Shell

Terminal disponible desde la consola de OCI para ejecutar comandos y administrar recursos sin configurar una terminal local.

### VCN

Red virtual privada dentro de OCI. Permite definir el entorno de conectividad de las instancias y controlar cómo se comunican entre sí y con Internet.

### Compute instances

Máquinas virtuales aprovisionadas en OCI para ejecutar aplicaciones y servicios.

### Load balancer

Servicio que distribuye el tráfico entre varias instancias, evitando depender de un único servidor y mejorando la disponibilidad de la aplicación.

## Arquitectura desarrollada

La práctica principal del curso sigue esta estructura general:

1. crear y organizar los recursos dentro de OCI;
2. configurar usuarios y accesos;
3. crear una VCN;
4. desplegar una primera instancia;
5. instalar y ejecutar la aplicación;
6. crear una segunda instancia;
7. configurar un balanceador de carga;
8. distribuir las solicitudes entre ambos servidores.

## Resumen del curso

Los apuntes técnicos filtrados y organizados por aula se almacenarán en:

[`resumen.md`](./resumen.md)

## Prácticas y recursos

Los scripts, configuraciones o archivos de aplicación que resulten útiles para el repositorio se almacenarán en:

```text
codigo/
```

Las capturas solo se conservarán cuando ayuden a comprender una configuración o arquitectura y deberán revisarse antes de publicarse.

## Seguridad

Antes de subir archivos relacionados con OCI se debe comprobar que no contengan:

- contraseñas o tokens;
- claves privadas SSH;
- archivos `.pem` o `.key`;
- OCIDs sensibles;
- datos de la tenancy;
- direcciones de correo personales;
- direcciones IP públicas que no deban exponerse;
- reglas de acceso innecesariamente abiertas;
- configuraciones con credenciales;
- capturas con información privada de la cuenta.

No deben versionarse:

```gitignore
.env
*.pem
*.key
.oci/
```

Las políticas y reglas de red deben aplicar el principio de mínimo privilegio. Los recursos creados para practicar deben revisarse y eliminarse cuando ya no sean necesarios para evitar exposición o consumo accidental.

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