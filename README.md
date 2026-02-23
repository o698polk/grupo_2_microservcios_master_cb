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

---

## 2️ Corrección de Errores y Validación de Funciones

Se llevó a cabo la depuración del código, optimización de la lógica y validación progresiva de cada endpoint para garantizar su correcto funcionamiento.

![Corrección y validación](/capturas_pantalla/pyfinal.png)

---

## 3️ Ejecución de Tests Automatizados

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