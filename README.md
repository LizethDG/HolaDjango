# 🐍 Proyecto Django: Sistema de Usuarios con MySQL y Docker

Este proyecto es una aplicación web desarrollada con Django que permite el registro y autenticación de usuarios usando correo electrónico, nombre y contraseña. Utiliza MySQL como base de datos y está completamente contenerizada con Docker para facilitar su despliegue y desarrollo.

---

## 🚀 Características

- ✅ Registro de usuarios con nombre, correo electrónico y contraseña  
- 🔐 Inicio de sesión seguro  
- 🖼️ Interfaz moderna y responsiva con imágenes de fondo  
- 📋 Listado de usuarios *(puedes ampliar esta funcionalidad)*  
- 🧠 Gestión de sesiones y cierre de sesión  
- 🐳 Configuración lista para desarrollo con Docker y MySQL  

---

## 📁 Estructura del Proyecto

```plaintext
├── app/                 # Código fuente de la aplicación Django
│   ├── users/           # App de usuarios
│   ├── templates/       # HTMLs personalizados
│   ├── static/          # Archivos estáticos (CSS, imágenes)
│   └── ...
├── docker/
│   ├── web/             # Dockerfile de Django
│   └── db/              # Configuración de MySQL
├── docker-compose.yml   # Orquestación con Docker Compose
└── README.md            # Este archivo
```
---

## 🛠️ Requisitos

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)
- *(Opcional)* Python 3.x si deseas ejecutar comandos de Django fuera de Docker

---

## ⚙️ Instalación y Ejecución

### 1. Clona el repositorio:

```bash
git clone https://github.com/tu_usuario/tu_repositorio.git
cd tu_repositorio
```
## Construye y ejecuta los contenedores:

- Aplica las migraciones y crea un superusuario:
- Abre una terminal en el contenedor web:
- Accede a la aplicación:
- Abre tu navegador en http://localhost:8000

## 🎨 Personalización
- Imágenes de fondo: Puedes cambiar las imágenes en la carpeta static para personalizar el aspecto visual.
- Templates: Modifica los archivos en templates para cambiar la interfaz.
- Funcionalidad: Amplía las vistas y modelos en views.py y models.py para agregar más características.
## 🔒 Seguridad
- Las vistas principales están protegidas: solo usuarios autenticados pueden acceder a la página principal.
- Las sesiones se gestionan de forma segura usando el sistema de autenticación de Django.
## 📄 Licencia
Este proyecto es de uso académico y puedes modificarlo libremente para tus necesidades.
