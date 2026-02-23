# GRUPO 2 — MASTER EN CIBERSEGURIDAD 
# Integrantes:
- Héctor Ramos Vera  
- David León Guaman  
- Polk Brando Vernaza

#  API  – Platos Típicos por País

##  Descripción del Proyecto

Este proyecto consiste en el desarrollo de una **API  en Python utilizando Flask** que permite gestionar platos típicos asociados a un país.

La aplicación implementa operaciones CRUD (Crear, Leer, Actualizar y Eliminar) y almacena los registros en un archivo JSON.

Antes de registrar un nuevo plato, el sistema valida la existencia del país mediante el consumo de una API externa, garantizando la integridad de los datos.

---

#  Evidencias del Desarrollo del Proyecto

## 1️ Inicio del Proyecto en GitHub

Se realizó la creación y configuración inicial del repositorio en GitHub, estableciendo la estructura base del proyecto y organizando el trabajo colaborativo del equipo.

![Inicio del proyecto](/capturas_pantalla/pyinitil.png)

# 👥 Distribución de Responsabilidades del Equipo

## 2️ David León Guaman  
**Responsable de la fase inicial del proyecto y desarrollo de funciones auxiliares**

### 1. Configuración Inicial  
Creación de la estructura base del proyecto, organización del entorno de trabajo y configuración inicial del repositorio.

![Configuración inicial](/capturas_pantalla/Dav1.jpeg)

### 2. Desarrollo de Funciones Auxiliares  
Implementación de funciones de apoyo para optimizar la lógica interna y facilitar la gestión de datos dentro de la aplicación.

![Funciones auxiliares](/capturas_pantalla/Dav2.jpeg)

### 3. Implementación del Menú Principal  
Diseño del endpoint principal que permite visualizar las rutas disponibles dentro de la API.

![Menú principal](/capturas_pantalla/Dav3.jpeg)

### 4. Test de Validación  
Ejecución de pruebas para verificar el correcto funcionamiento de las funcionalidades desarrolladas en esta fase.

![Test validación David](/capturas_pantalla/Dav4.jpeg)

---

## 3️ Héctor Ramos Vera  
**Responsable de la creación de funciones principales de consulta y validación con API externa**

### 1. Desarrollo de Funciones CRUD (Crear y Consultar)  
Implementación de la función para crear registros validando previamente la existencia del país mediante una API externa, así como la consulta general y consulta por ID.

![Código Héctor](/capturas_pantalla/hect2.jpeg)

### 2. Test de Validación  
Pruebas funcionales para comprobar la correcta integración con la API externa y el funcionamiento de los endpoints desarrollados.

![Test validación Héctor](/capturas_pantalla/hect1.jpeg)

---

## 4️ Polk Brando Vernaza  
**Responsable de funciones avanzadas y configuración de entorno Docker**

### 1. Desarrollo de Funciones (Editar y Eliminar)  
Implementación de las funcionalidades para actualizar y eliminar registros almacenados en el archivo JSON.

![Código Polk](/capturas_pantalla/pol1.png)

### 2. Test de Validación  
Pruebas para verificar la correcta modificación y eliminación de registros en la API.

![Test validación Polk](/capturas_pantalla/pol2.png)

### 3. Configuración de Dockerfile y requirements.txt  
Creación y configuración de:
- `Dockerfile`
- `requirements.txt`
- Contenerización del proyecto para su despliegue

![Archivos Docker y configuración](/capturas_pantalla/pol2.png)

---

## 5 Corrección de Errores y Validación de Funciones

Se llevó a cabo la depuración del código, optimización de la lógica y validación progresiva de cada endpoint para garantizar su correcto funcionamiento.

![Corrección y validación](/capturas_pantalla/pyfinal.png)

---

## 6 Ejecución de Tests Automatizados

Se implementaron pruebas automatizadas para verificar de manera sistemática el funcionamiento correcto de todos los endpoints y operaciones CRUD.

![Tests automatizados](/capturas_pantalla/tespy_1.png)

---

#  Cumplimiento de los Puntos Solicitados

## 1️ API Funcionando Localmente

Ejecución correcta de la aplicación en entorno local verificando el acceso a los endpoints.

![API local](/capturas_pantalla/lcpy1.png)

---

## 2️ Construcción de la Imagen Docker

Creación exitosa de la imagen Docker a partir del Dockerfile configurado para el proyecto.

![Construcción Docker](/capturas_pantalla/dock_1.png)

---

## 3️ Contenedor en Ejecución

Ejecución del contenedor Docker con la API funcionando correctamente dentro del entorno aislado.

### 3.1 Contenedor Activo
![Contenedor activo](/capturas_pantalla/dock_2.png)

### 3.2 Aplicación Ejecutándose en el Contenedor
![Aplicación en Docker](/capturas_pantalla/dokerrunpy.png)

![Validación en contenedor](/capturas_pantalla/pyi_1validando.png)

---

## 4️ Pruebas con cURL Exitosas

Validación manual de cada endpoint utilizando comandos cURL.

### 4.1 Mostrar el Menú Principal
![Menú principal](/capturas_pantalla/tespy_1.png)

### 4.2 Crear un Registro (Validando País Existente)
![Crear registro](/capturas_pantalla/tespy_2.png)

### 4.3 Validación de País No Existente
![País no existente](/capturas_pantalla/tespy_3.png)

### 4.4 Ver Todos los Platos Registrados
![Ver todos](/capturas_pantalla/tespy_4.png)

### 4.5 Obtener un Plato por ID
![Get por ID](/capturas_pantalla/tespy_5.png)

### 4.6 Editar un Registro
![Editar registro](/capturas_pantalla/tespy_6.png)

### 4.7 Eliminar un Registro
![Eliminar registro](/capturas_pantalla/tespy_7.png)

---

## 5️ API Desplegada en la Nube (Google Cloud)

El proyecto fue integrado y desplegado exitosamente en un entorno cloud, permitiendo el acceso público a la API desde internet.


### 5.1 Merge Realizado Correctamente sin Conflictos

Se realizó la integración final de las ramas hacia `main` sin presentar conflictos, asegurando estabilidad del código antes del despliegue en producción.

![Merge exitoso](/capturas_pantalla/merge_exi.png)


### 5.2 Proceso de Publicación en Google Cloud Exitoso

Se llevó a cabo el despliegue de la aplicación utilizando Google Cloud Run, construyendo la imagen del contenedor y publicándola en un entorno productivo.

Este proceso incluyó:
- Construcción automática de la imagen Docker
- Publicación en Artifact Registry
- Despliegue del servicio en Cloud Run
- Configuración de acceso público

![Despliegue en Google Cloud](/capturas_pantalla/googlecloud.png)


##  6️ Endpoint Accesible Públicamente

Una vez desplegada, la API quedó disponible a través de una URL pública, permitiendo su acceso desde navegador o herramientas como `curl`.


### 6.1 Acceso al Menú Principal desde el Navegador

Visualización del endpoint raíz (`/`) directamente desde el navegador, confirmando que el servicio se encuentra activo en la nube.

![Endpoint navegador](/capturas_pantalla/endpoidaccebli.png)

### 6.2 Acceso al Endpoint usando cURL

Prueba del endpoint público utilizando `curl`, validando la correcta respuesta del servicio desde línea de comandos.

![Endpoint curl](/capturas_pantalla/epcur1.png)

### 6.3 Creación y Consulta de Registros en el Entorno Cloud

Se realizó la creación de un nuevo registro validando la existencia del país mediante la API externa y posteriormente se consultaron todos los registros almacenados.

Con esta prueba se confirma:

- Correcto funcionamiento del endpoint público
- Integración exitosa con la API externa
- Persistencia de datos en el entorno desplegado
- Funcionamiento completo del CRUD en producción

![Validación en Google Cloud](/capturas_pantalla/googlecloud3.png)

#  Tecnologías Utilizadas

- Python 3
- Flask
- Requests
- JSON
- Docker
- cURL
- GitHub

---

#  Funcionalidades Principales

✔ Validación de país mediante API externa  
✔ Registro de platos típicos  
✔ Consulta general y por ID  
✔ Edición de registros  
✔ Eliminación de registros  
✔ Persistencia de datos en archivo JSON  
✔ Contenerización con Docker  
✔ Pruebas automatizadas  

---