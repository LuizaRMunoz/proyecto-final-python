# Sistema de Gestión de Activos e Incidentes de Seguridad

Una aplicación web desarrollada en **Django** orientada a la gestión de infraestructura tecnológica (ITSM) y operaciones de seguridad (SecOps). Este sistema permite administrar el ciclo de vida de los activos de la organización y registrar la evolución de los incidentes de seguridad, con un fuerte enfoque en la **trazabilidad, auditoría y control de cambios**.

## Características principales

### Gestión de activos
* **Inventario centralizado:** Registro detallado de activos (servidores, APIs, equipos, etc.) con sus respectivas IPs, niveles de criticidad y estado.
* **Seguridad de modificación (Step-up Authentication):** Las ediciones de activos sensibles requieren una contraseña de administrador para ser procesadas.
* **Auditoría automática:** Todo cambio genera un registro inmutable en el Historial del Activo, detallando quién hizo el cambio, cuándo, qué campos se modificaron y el motivo.

### Gestión de incidentes
* **Reporte rápido:** Creación de tickets de incidentes vinculados directamente a los activos afectados, con niveles de severidad (Crítico, Alto, Medio, Bajo).
* **Ciclo de vida evolutivo:** Los incidentes **no se eliminan** (cumpliendo con estándares de seguridad). En su lugar, evolucionan de estado (Abierto -> En Investigación -> Resuelto -> Cerrado).
* **Línea de tiempo (Timeline):** Cada ticket cuenta con un registro de evolución donde los operadores deben documentar obligatoriamente las acciones realizadas para cambiar el estado del incidente, requiriendo autorización para impactar los cambios.

## Stack Tecnológico

* **Backend:** Python 3, Django.
* **Base de Datos:** SQLite (por defecto en Django).
* **Frontend:** HTML5, Bootstrap 5 (Modales dinámicos, sistema de grillas, badges y alertas), CSS personalizado.

## Instalación y Uso Local

Sigue estos pasos para levantar el proyecto en tu entorno local:

1. **Clonar el repositorio:**
   ```bash
   git clone [[Proyecto_Final]](https://github.com/LuizaRMunoz/proyecto-final-python.git)
   cd proyecto-final-python

2. **Crear y activar entorno virtual:**
python -m venv venv
**Windows:** venv/Scripts/activate
**MacOS:** source venv/bin/activate

3. **Instalar dependencias:**
pip install django
pip install pillow

4. **Aplicar migraciones:**
python manage.py makemigrations
python manage.py migrate

5. **Crear un superusuario (para acceder al panel de admin):**
python manage.py createsuperuser

6. **Ejecutar el servidor local:**
python manage.py runserver

## Credenciales y Entorno de Pruebas
**Aviso Importante:** Este proyecto está configurado para un entorno de desarrollo/evaluación. 
Para poder probar el ciclo completo de la herramienta (como la edición de activos y la actualización de incidentes), el sistema solicita una clave de autorización (*Step-up Authentication*).

* **Contraseña requerida para probar las modificaciones:** `admin123`
*(En un entorno de producción real, esto estaría conectado a un sistema de gestión de contraseñas o variables de entorno).*

