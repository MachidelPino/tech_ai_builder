Resumen del curso

El curso introduce los fundamentos de Oracle Cloud Infrastructure (OCI) y desarrolla una infraestructura básica para publicar una aplicación web.

La práctica combina organización de recursos, control de acceso, redes virtuales, instancias de cómputo, configuración de servidores y balanceo de carga. El resultado es una arquitectura con dos servidores detrás de un load balancer público.

Aula 01 — Computación en la nube

Concepto general

La computación en la nube permite utilizar recursos informáticos alojados en centros de datos y accesibles a través de Internet.

Entre estos recursos se incluyen:

servidores;

almacenamiento;

redes;

bases de datos;

plataformas de desarrollo;

aplicaciones completas.

En lugar de adquirir y mantener infraestructura física propia, los recursos pueden aprovisionarse según las necesidades del proyecto.

Ventajas principales

Costo

Reduce la inversión inicial en hardware y permite ajustar el gasto a los recursos utilizados.

Esto no garantiza automáticamente un menor costo: una configuración sobredimensionada o recursos que permanecen activos sin necesidad pueden generar gastos innecesarios.

Velocidad

Los recursos pueden crearse en pocos minutos, acelerando el desarrollo, las pruebas y el despliegue.

Escalabilidad

La capacidad puede adaptarse a la demanda.

Escalabilidad vertical: aumentar los recursos de una instancia.

Escalabilidad horizontal: agregar más instancias.

Productividad

El equipo puede concentrarse en la aplicación mientras el proveedor administra la infraestructura física.

Confiabilidad

La nube ofrece servicios para mejorar disponibilidad, monitoreo, respaldo y recuperación, aunque estos beneficios dependen de una arquitectura correctamente diseñada.

Tipos de nube

Pública: infraestructura ofrecida por un proveedor externo a través de Internet.

Privada: infraestructura destinada a una única organización.

Híbrida: combinación de recursos públicos y privados.

Modelos de servicio

IaaS

El proveedor administra el hardware y la virtualización. El usuario conserva control sobre el sistema operativo, la red, las aplicaciones y los datos.

Las instancias utilizadas en el curso son un ejemplo de IaaS.

PaaS

El proveedor también administra parte de la plataforma de ejecución. El equipo se concentra principalmente en desarrollar y desplegar la aplicación.

SaaS

El proveedor entrega una aplicación completa accesible mediante Internet.

Serverless

Permite ejecutar código sin administrar servidores directamente. La infraestructura subyacente continúa existiendo, pero queda a cargo del proveedor.

Aula 02 — Cuenta Free Tier y consola de OCI

Modalidades gratuitas

El curso diferencia entre:

recursos incluidos en la capa gratuita;

créditos promocionales disponibles durante una prueba temporal.

Los servicios, límites y condiciones pueden cambiar. Antes de crear recursos es necesario revisar la documentación oficial y el panel de facturación.

Creación de la cuenta

El proceso general incluye:

completar los datos solicitados;

verificar el correo electrónico;

elegir una región principal;

verificar un medio de pago;

configurar las credenciales de acceso.

La verificación del medio de pago no implica por sí sola contratar servicios pagos, pero es necesario comprobar qué recursos están cubiertos por la capa gratuita.

Región principal

Una región es una ubicación geográfica que contiene infraestructura de OCI.

La elección influye en:

disponibilidad de servicios;

latencia;

residencia de datos;

costos;

capacidad disponible.

Autenticación multifactor

MFA agrega una segunda comprobación al inicio de sesión y debe habilitarse especialmente en cuentas con acceso a infraestructura, datos o facturación.

Consola de OCI

La consola web permite:

buscar servicios;

seleccionar regiones;

cambiar de compartment;

crear y administrar recursos;

consultar notificaciones;

revisar facturación;

acceder a Cloud Shell.

Cloud Shell

Cloud Shell proporciona una terminal dentro de OCI con herramientas preinstaladas.

Desde allí se pueden ejecutar comandos del sistema y de OCI CLI, por ejemplo:

oci iam user list

Las operaciones disponibles dependen de los permisos del usuario conectado.

Aula 03 — Arquitectura, compartments e IAM

Organización general de OCI

OCI agrupa sus servicios en áreas como:

Compute;

Storage;

Networking;

Database;

Identity and Security;

Observability and Management;

Developer Services;

Billing and Cost Management;

Governance.

Tenancy

La tenancy representa el entorno principal de una organización dentro de OCI.

Contiene usuarios, políticas, compartments y recursos administrados por la cuenta.

Compartments

Los compartments son contenedores lógicos utilizados para organizar recursos.

Pueden representar:

proyectos;

equipos;

departamentos;

ambientes como desarrollo, pruebas y producción.

También pueden anidarse para crear jerarquías.

Cada compartment posee un identificador único denominado OCID.

Los compartments organizan recursos, pero el acceso se controla mediante políticas de IAM.

Separación de ambientes

Una estructura inicial puede ser:

tenancy
├── desarrollo
└── produccion

Esta separación facilita aplicar permisos diferentes y reduce el riesgo de modificar recursos productivos por error.

IAM

Identity and Access Management determina quién puede acceder a los recursos y qué acciones puede realizar.

Sus componentes principales son:

usuarios;

grupos;

políticas;

dominios de identidad.

Un flujo habitual consiste en:

crear un usuario;

agregarlo a un grupo;

definir una política para el grupo;

limitar la política al compartment necesario.

Principio de mínimo privilegio

Las políticas deben conceder únicamente los permisos requeridos. Otorgar acceso administrativo global por comodidad aumenta innecesariamente el riesgo.

Claves SSH

Cloud Shell se utiliza para generar un par de claves:

clave pública;

clave privada.

Ejemplo:

ssh-keygen -t rsa -b 2048 -f ~/.ssh/cloudshellkey

La clave pública puede asociarse a una instancia. La clave privada debe mantenerse protegida y nunca publicarse.

Aula 04 — Redes y VCN

VCN

Una Virtual Cloud Network es una red virtual configurable dentro de OCI.

Contiene componentes como:

subredes;

tablas de rutas;

gateways;

listas de seguridad.

CIDR

CIDR define rangos de direcciones IP.

La VCN y sus subredes reciben bloques que no deben superponerse. Planificar el direccionamiento desde el inicio evita cambios complejos cuando la infraestructura ya está desplegada.

Subred pública

Una subred pública puede permitir que sus instancias reciban direcciones IP públicas y se comuniquen directamente con Internet.

Normalmente utiliza:

Internet Gateway;

tabla de rutas;

reglas de seguridad.

Subred privada

Una subred privada evita el acceso directo desde Internet.

Sus instancias pueden usar un NAT Gateway para iniciar conexiones salientes sin aceptar conexiones entrantes desde Internet.

Gateways

Internet Gateway

Permite comunicación entre la VCN e Internet.

NAT Gateway

Permite que recursos privados inicien conexiones hacia Internet sin exponerlos directamente.

Service Gateway

Permite acceder a determinados servicios de Oracle sin atravesar Internet público.

Tablas de rutas

Indican hacia qué gateway debe enviarse el tráfico según su destino.

Las subredes públicas y privadas suelen necesitar rutas diferentes.

Listas de seguridad

Definen reglas de entrada y salida para las subredes.

Ejemplos utilizados en el curso:

puerto 22 para SSH;

puerto 80 para HTTP.

Las reglas deben limitar el origen tanto como sea posible. Abrir SSH a 0.0.0.0/0 expone el servicio a todo Internet y no es recomendable en un entorno real.

Asistente de creación

El asistente de OCI puede generar automáticamente:

subred pública;

subred privada;

Internet Gateway;

NAT Gateway;

Service Gateway;

tablas de rutas;

reglas iniciales.

Aunque acelera la configuración, es importante comprender los componentes creados.

Aula 05 — Compute y balanceo de carga

Instancias de cómputo

Una instancia es una máquina virtual que ejecuta un sistema operativo dentro de OCI.

Al crearla se define:

nombre;

compartment;

imagen del sistema operativo;

shape;

cantidad de CPU;

memoria;

VCN y subred;

clave SSH;

asignación de IP pública.

Shapes

El shape determina la capacidad de la instancia.

Puede incluir:

cantidad de OCPUs;

memoria;

arquitectura del procesador;

tipo de instancia.

La elección debe equilibrar rendimiento, compatibilidad y costo.

Conexión mediante SSH

Después de crear la instancia se utiliza su IP pública y la clave privada correspondiente:

ssh -i ~/.ssh/cloudshellkey opc@<IP_PUBLICA>

La clave privada debe tener permisos restrictivos y permanecer fuera del repositorio.

Instalación de Apache

El curso instala Apache HTTP Server sobre Oracle Linux:

sudo yum -y install httpd
sudo systemctl start httpd

También se habilita el puerto 80 en el firewall del sistema:

sudo firewall-cmd --permanent --add-port=80/tcp
sudo firewall-cmd --reload

La página de prueba se guarda en:

/var/www/html/index.html

Para que el servicio sea accesible deben coincidir dos niveles de configuración:

firewall del sistema operativo;

reglas de red de OCI.

Abrir el puerto en un solo nivel no es suficiente.

Segunda instancia

Se crea una segunda instancia con una configuración equivalente y un contenido visual diferente.

Esto permite comprobar qué backend responde a cada solicitud.

Load balancer

El balanceador recibe solicitudes y las distribuye entre las instancias configuradas como backends.

Cliente
   |
Load Balancer
   |---------|
Instancia 1  Instancia 2

Su configuración incluye:

dirección pública o privada;

backend set;

instancias backend;

health checks;

listener;

algoritmo de distribución.

Listener

Recibe tráfico en un protocolo y puerto determinados.

En el curso se utiliza HTTP sobre el puerto 80.

Health checks

Permiten verificar si cada backend responde correctamente.

Cuando una instancia falla la comprobación, el balanceador puede dejar de enviarle tráfico.

Algoritmos de balanceo

Round Robin

Distribuye solicitudes de forma secuencial entre los backends.

Least Connections

Envía la solicitud al backend con menos conexiones activas.

IP Hash

Utiliza la IP del cliente para intentar dirigirlo al mismo backend.

Puede ofrecer afinidad básica, pero no reemplaza una estrategia adecuada para gestionar sesiones.

Escalabilidad y disponibilidad

Agregar más instancias permite escalar horizontalmente.

El load balancer reduce la dependencia de un único servidor, pero una arquitectura realmente disponible también debe considerar:

health checks;

distribución entre dominios o zonas;

automatización de despliegues;

persistencia de datos;

estado compartido;

monitoreo;

recuperación ante fallos.

Arquitectura final

La práctica construye la siguiente infraestructura:

tenancy y cuenta de OCI;

compartment para organizar el proyecto;

usuario, grupo y política de IAM;

VCN;

subred pública y privada;

gateways y tablas de rutas;

reglas de seguridad;

dos instancias de cómputo;

Apache instalado en ambas;

load balancer público;

listener HTTP;

backends y health checks.

Buenas prácticas principales

Separar recursos mediante compartments.

Aplicar permisos a grupos y no directamente a cada usuario.

Seguir el principio de mínimo privilegio.

Habilitar autenticación multifactor.

Mantener las claves privadas fuera del repositorio.

Planificar los rangos CIDR antes de crear la red.

Utilizar subredes privadas para recursos que no requieran exposición pública.

Limitar reglas de entrada a los puertos y orígenes necesarios.

Revisar tanto el firewall del sistema como las reglas de OCI.

Configurar health checks para los backends.

Controlar costos y límites antes de aprovisionar recursos.

Eliminar los recursos de práctica que ya no sean necesarios.

Seguridad y publicación

No deben versionarse:

.env
.oci/
*.pem
*.key

Antes de publicar scripts, comandos o capturas se debe verificar que no contengan:

claves privadas;

contraseñas;

tokens;

OCIDs sensibles;

datos de la tenancy;

correos personales;

direcciones IP que no deban exponerse;

información de facturación;

reglas de acceso inseguras.

Los ejemplos del curso pueden utilizar reglas amplias para simplificar las pruebas. En un entorno real deben sustituirse por configuraciones más restrictivas.

Conclusión

El curso presenta una primera implementación completa en OCI: desde la organización de la cuenta hasta la publicación de un servicio web distribuido entre dos instancias.

El aprendizaje principal es que desplegar una aplicación no consiste solamente en crear una máquina virtual. También requiere administrar identidades, redes, claves, firewalls, servidores, reglas de acceso y disponibilidad.