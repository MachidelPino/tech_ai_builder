# Resumen del curso

El curso amplía una aplicación desplegada en **Oracle Cloud Infrastructure (OCI)** mediante una base de datos autónoma, una API REST desarrollada con Node.js, almacenamiento de objetos, acceso mediante HTTPS e infraestructura como código con Terraform.

El recorrido conecta servicios de datos, cómputo, red y automatización para construir una arquitectura más completa y reproducible.

## Aula 01 — Bases de datos en OCI

### Alternativas de bases de datos

OCI ofrece distintos servicios según el modelo de datos y el tipo de carga de trabajo.

Entre las opciones presentadas se encuentran:

- Oracle Database;
- Autonomous Database;
- MySQL HeatWave;
- PostgreSQL;
- servicios orientados a documentos JSON.

La elección debe considerar:

- estructura de los datos;
- volumen;
- frecuencia de lectura y escritura;
- concurrencia;
- disponibilidad;
- seguridad;
- costos;
- mantenimiento requerido.

### Bases relacionales y no relacionales

Las bases relacionales organizan la información mediante tablas, filas, columnas y relaciones definidas. Son adecuadas cuando se necesita estructura consistente, integridad referencial, transacciones y consultas SQL.

Las bases no relacionales permiten modelos más flexibles, como documentos JSON. Son útiles cuando la estructura puede variar o no todas las entidades poseen los mismos campos.

La elección debe responder a las necesidades reales del sistema y no únicamente a la tecnología utilizada.

### Autonomous Database

Autonomous Database automatiza tareas operativas como:

- aprovisionamiento;
- ajuste y escalado;
- aplicación de parches;
- protección de datos;
- detección de fallos;
- failover y recuperación.

Esto reduce parte del trabajo manual, aunque la aplicación todavía debe gestionar correctamente sus credenciales, conexiones, consultas y permisos.

### Tipos de carga de trabajo

Al crear una base autónoma se puede seleccionar un perfil según el uso previsto:

- **Data Warehouse:** análisis y grandes volúmenes de datos;
- **Transaction Processing:** operaciones transaccionales y alta concurrencia;
- **JSON:** aplicaciones centradas en documentos;
- **APEX:** desarrollo de aplicaciones low-code.

En el proyecto se utiliza una base orientada a documentos JSON.

### Colecciones JSON y SODA

La base permite crear colecciones y almacenar documentos formados por pares clave-valor.

```json
{
  "nombre": "Cliente",
  "email": "cliente@example.com"
}
```

La aplicación accede a estos documentos mediante **SODA** —Simple Oracle Document Access—, una interfaz de Oracle para trabajar con datos documentales sin depender exclusivamente de SQL.

### Compatibilidad con MongoDB

Oracle ofrece una API compatible con herramientas y drivers de MongoDB sobre Autonomous JSON Database.

Esto puede facilitar migraciones o integraciones al conservar interfaces conocidas, aunque la compatibilidad concreta debe comprobarse según las operaciones utilizadas por la aplicación.

## Aula 02 — API y conexión con la base de datos

### Arquitectura de la aplicación

La aplicación del curso es una API REST construida con:

- Node.js;
- Express;
- `oracledb`;
- SODA.

Los archivos principales cumplen funciones diferentes:

- `package.json`: dependencias y metadatos;
- `app.js`: configuración del servidor y rutas;
- `cliente-service.js`: conexión y operaciones de datos;
- `bin/www`: inicio del servidor.

La API expone rutas para crear, consultar, actualizar y eliminar clientes.

### Operaciones CRUD

| Operación | Método HTTP |
|---|---|
| Crear | `POST` |
| Consultar | `GET` |
| Actualizar | `PUT` |
| Eliminar | `DELETE` |

### Preparación de la instancia

Para ejecutar la API se realizan estas tareas:

1. conectarse mediante SSH;
2. actualizar paquetes;
3. instalar Git;
4. instalar Oracle Instant Client;
5. instalar Node.js;
6. clonar el repositorio;
7. instalar dependencias;
8. configurar la conexión;
9. iniciar la aplicación.

La compatibilidad entre el sistema operativo, Node.js, Instant Client y `oracledb` debe verificarse antes de fijar versiones.

### Wallet y variables de entorno

La conexión con Autonomous Database utiliza un wallet con los archivos necesarios para establecer una conexión segura.

El wallet debe transferirse de forma segura, conservar permisos restrictivos y permanecer fuera del repositorio.

Las credenciales se proporcionan mediante variables de entorno, por ejemplo:

```text
DB_USER
DB_PASSWORD
CONNECT_STRING
```

Nunca deben escribirse directamente en el código.

### Exposición del puerto

La API se ejecuta inicialmente en el puerto `3000`.

Para acceder desde fuera de la instancia deben configurarse dos niveles:

1. firewall del sistema operativo;
2. reglas de entrada de la VCN.

Una aplicación puede estar funcionando y seguir siendo inaccesible si alguno de estos niveles bloquea el tráfico.

### Ejecución con systemd

Ejecutar `npm start` desde una terminal no garantiza que la aplicación continúe activa al cerrar la sesión.

Un servicio de `systemd` permite:

- ejecutar la aplicación en segundo plano;
- iniciarla automáticamente;
- consultar su estado;
- reiniciarla;
- centralizar su configuración.

```bash
sudo systemctl daemon-reload
sudo systemctl start doguito.service
sudo systemctl status doguito.service
sudo systemctl enable doguito.service
```

No es recomendable incluir contraseñas directamente en una unidad de `systemd` versionada. Deben utilizarse archivos de entorno protegidos o mecanismos de secretos.

### Pruebas de la API

Los endpoints se prueban mediante un cliente HTTP, verificando:

- respuestas exitosas;
- cuerpos JSON;
- códigos de estado;
- identificadores;
- errores de validación;
- recursos inexistentes;
- fallos de conexión.

## Aula 03 — Almacenamiento y HTTPS

### Tipos de almacenamiento

#### Block Storage

Funciona como un disco persistente asociado a una instancia.

Es apropiado para sistemas de archivos, datos de aplicaciones y ampliación de capacidad.

#### File Storage

Proporciona un sistema de archivos compartido mediante NFS.

Es útil cuando varias instancias necesitan acceder al mismo conjunto de archivos.

#### Object Storage

Guarda archivos como objetos dentro de buckets.

Es adecuado para:

- imágenes;
- videos;
- documentos;
- archivos estáticos;
- copias de seguridad;
- contenido distribuido por Internet.

### Niveles de acceso

- **Standard:** datos consultados con frecuencia;
- **Infrequent Access:** datos menos utilizados;
- **Archive:** conservación prolongada con acceso poco frecuente.

La política de almacenamiento debe equilibrar disponibilidad, tiempo de recuperación y costo.

### Buckets, objetos y prefijos

Los archivos se almacenan dentro de buckets. Los prefijos permiten organizarlos con una estructura lógica semejante a carpetas:

```text
site/
├── index.html
├── css/
├── images/
└── js/
```

Los prefijos no representan necesariamente directorios físicos.

### Publicación del frontend

El frontend está compuesto por HTML, CSS, JavaScript e imágenes.

El código JavaScript debe apuntar al endpoint correcto del backend. Fijar una IP o un puerto directamente dificulta cambiar de ambiente, por lo que en un proyecto real conviene utilizar configuración externa o un proceso de build.

### Acceso público

Un bucket público facilita la publicación de contenido estático, pero también expone todos los objetos alcanzados por esa política.

Antes de habilitarlo se debe verificar que:

- el contenido sea realmente público;
- no existan archivos internos;
- no se incluyan configuraciones;
- no haya credenciales;
- las políticas sean lo más limitadas posible.

### Mixed content

Los navegadores bloquean una página cargada mediante HTTPS cuando intenta consumir una API mediante HTTP.

La arquitectura debe mantener una comunicación segura desde el cliente:

```text
Frontend HTTPS
      |
Load Balancer HTTPS
      |
Backend
```

El load balancer puede finalizar la conexión TLS y reenviar el tráfico hacia la instancia.

### SSL en el load balancer

Para habilitar HTTPS se necesita:

- certificado;
- clave privada;
- listener HTTPS;
- backend set;
- reglas de red apropiadas.

La clave privada del certificado nunca debe publicarse.

### Errores 502

Un error `502 Bad Gateway` puede indicar que el balanceador no consigue comunicarse correctamente con el backend.

Posibles causas:

- puerto incorrecto;
- aplicación detenida;
- health check fallido;
- reglas de red;
- firewall;
- backend equivocado;
- configuración desactualizada.

## Aula 04 — Infraestructura como código

### Limitaciones del aprovisionamiento manual

Crear recursos desde la consola es útil para aprender, pero se vuelve problemático cuando aumentan los recursos, existen varios ambientes o diferentes personas aplican configuraciones.

La configuración manual favorece diferencias entre ambientes y errores difíciles de rastrear.

### Infrastructure as Code

IaC representa la infraestructura mediante archivos declarativos o scripts.

Sus beneficios principales son:

- automatización;
- reproducibilidad;
- control de versiones;
- revisión de cambios;
- consistencia;
- trazabilidad;
- reducción de tareas repetitivas.

### Terraform

Terraform permite definir recursos mediante archivos `.tf`.

Una configuración puede incluir:

- proveedor OCI;
- compartments;
- redes;
- subredes;
- instancias;
- variables;
- salidas;
- scripts de inicialización.

Flujo habitual:

```bash
terraform init
terraform plan
terraform apply
terraform destroy
```

`terraform plan` permite revisar los cambios antes de aplicarlos.

### Cloud-init

Un archivo como `cloudinit.yaml` puede automatizar la configuración inicial de una instancia.

Puede ejecutar tareas como:

- instalar paquetes;
- configurar el firewall;
- iniciar servicios;
- crear archivos;
- desplegar una aplicación.

Esto reduce la necesidad de configurar manualmente cada servidor mediante SSH.

### OCI Resource Manager

Resource Manager ejecuta configuraciones de Terraform dentro de OCI.

El flujo utiliza una **stack** obtenida desde fuentes como:

- archivo ZIP;
- repositorio Git;
- Object Storage;
- plantillas;
- recursos existentes.

Sobre la stack se pueden ejecutar operaciones de planificación, aplicación, actualización y destrucción.

### Estado de Terraform

Terraform utiliza un archivo de estado para relacionar la configuración con los recursos creados.

Puede contener:

- OCIDs;
- direcciones;
- atributos internos;
- datos sensibles.

No debe publicarse en Git. En proyectos colaborativos debe almacenarse en un backend remoto con control de acceso y bloqueo.

### Arquitecturas relacionadas

#### Monolito

Concentra sus módulos en una única unidad desplegable. Puede ser adecuado para sistemas pequeños, aunque un fallo o despliegue afecta al conjunto completo.

#### Microservicios

Divide la aplicación en servicios independientes. Puede mejorar independencia y escalabilidad, pero agrega complejidad de red, observabilidad, despliegue y consistencia de datos.

#### Contenedores

Docker empaqueta aplicaciones y dependencias en imágenes reproducibles. Kubernetes coordina su despliegue, escalado y disponibilidad.

#### API Gateway

Centraliza la entrada a distintas APIs o microservicios y puede aplicar autenticación, límites, rutas y otras políticas.

No es equivalente a un load balancer, aunque ambos participan en la gestión del tráfico.

## Arquitectura final

La solución desarrollada combina:

1. Autonomous JSON Database;
2. colección de documentos;
3. instancia de cómputo;
4. API REST con Node.js;
5. conexión mediante wallet y variables de entorno;
6. servicio administrado por `systemd`;
7. frontend en Object Storage;
8. load balancer;
9. acceso HTTPS;
10. infraestructura automatizada con Terraform;
11. scripts de inicialización con cloud-init;
12. ejecución mediante OCI Resource Manager.

## Buenas prácticas principales

- Elegir la base de datos según el modelo de datos y la carga.
- Mantener wallets y credenciales fuera del repositorio.
- Utilizar variables de entorno.
- Ejecutar aplicaciones mediante un gestor de servicios.
- Probar firewall y reglas de VCN por separado.
- Evitar IPs fijas dentro del frontend.
- Publicar buckets solo cuando sea necesario.
- Usar HTTPS para frontend y API.
- Revisar health checks y puertos del load balancer.
- Definir infraestructura mediante código.
- Ejecutar `terraform plan` antes de aplicar.
- Proteger el estado de Terraform.
- Destruir los recursos de práctica cuando ya no se utilicen.

## Seguridad y publicación

No deben versionarse:

```text
.env
.oci/
*.pem
*.key
Wallet_*/
*.zip
.terraform/
terraform.tfstate
terraform.tfstate.*
crash.log
```

También deben revisarse cuidadosamente:

- archivos `*.tfvars`;
- unidades de `systemd`;
- scripts de cloud-init;
- variables de Terraform;
- certificados;
- claves privadas;
- archivos de conexión;
- capturas de la consola.

El archivo `.terraform.lock.hcl` puede versionarse para conservar versiones consistentes de los proveedores.

## Conclusión

El curso muestra cómo transformar una aplicación básica en una solución desplegada con datos persistentes, frontend público, API, HTTPS y automatización de infraestructura.

El aprendizaje principal es que una aplicación en la nube depende de varios componentes coordinados: base de datos, credenciales, red, proceso de ejecución, almacenamiento, seguridad y aprovisionamiento reproducible.
