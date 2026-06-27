# Actividad N° 7: Exploración de Aplicaciones Preinstaladas

## 1. Aplicaciones preinstaladas
* **Definición**: Son aplicaciones que Django incluye por defecto para ofrecer funcionalidades base necesarias en aplicaciones web (como autenticación, sesiones y administración)[cite: 13, 14].
* **Ubicación**: Se declaran en la lista 'INSTALLED_APPS' del archivo 'settings.py'[cite: 15, 16].

### Análisis de INSTALLED_APPS[cite: 16]:
* **django.contrib.admin**: Sistema de administración. [cite: 17]
* **django.contrib.auth**: Sistema de autenticación de usuarios. [cite: 18]
* **django.contrib.contenttypes**: Seguimiento de modelos. [cite: 19]
* **django.contrib.sessions**: Gestión de sesiones. [cite: 20]
* **django.contrib.messages**: Sistema de mensajes. [cite: 21]
* **django.contrib.staticfiles**: Gestión de archivos estáticos. [cite: 22]

## 2. Interacción con modelos
Se realizó la creación exitosa del usuario 'estudiante_test' y su asignación al grupo 'Grupo_Exploracion' mediante el shell de Django. Se verificó la tabla de sesiones.

## 3. Acceso desde el Admin
Nota: La exploración se realizó mediante el shell de Django debido a restricciones del entorno de desarrollo. [cite: 33, 34]

## 4. Reflexión final
* **Importancia**: La aplicación 'django.contrib.auth' es vital para la seguridad y control de acceso. [cite: 39]
* **Observación**: El sistema de administración de Django es extremadamente eficiente al generar interfaces automáticamente basándose en los modelos definidos. [cite: 40]
