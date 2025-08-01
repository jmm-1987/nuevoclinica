# 🦷 Chatbot Clínica Dental - Interfaz Web

Un asistente virtual moderno para clínica dental con interfaz web elegante y navegación por botones interactivos.

## 🚀 Características

### 🎨 Interfaz Moderna
- **Burbuja de chat elegante** con diseño responsive
- **Navegación por botones** en lugar de números
- **Animaciones suaves** y transiciones fluidas
- **Indicadores de escritura** para simular experiencia real
- **Diseño adaptativo** para móviles y desktop

### 📋 Funcionalidades del Chatbot
- **Información de tratamientos** con detalles completos
- **Agendar citas** con formularios integrados
- **Ubicaciones** de múltiples centros
- **Información de financiación** con opciones de pago
- **Validación de datos** en tiempo real
- **Confirmaciones visuales** para cada acción

## 🛠️ Tecnologías Utilizadas

- **Backend**: Python Flask
- **Base de Datos**: SQLite
- **Frontend**: HTML5, CSS3, JavaScript
- **Frameworks**: Bootstrap 5, Font Awesome
- **Fuentes**: Google Fonts (Poppins)

## 📦 Instalación y Uso

### Requisitos
- Python 3.6 o superior
- Flask
- Gunicorn (para producción)

### Instalación Local
```bash
# Instalar dependencias
pip install -r requirements.txt

# Ejecutar la aplicación
python app_chatbot.py
```

### Acceso Local
La aplicación estará disponible en: `http://localhost:5001`

### Despliegue en Render

1. **Crear cuenta en Render**: Ve a [render.com](https://render.com) y crea una cuenta

2. **Conectar repositorio**: 
   - Conecta tu repositorio de GitHub/GitLab
   - Render detectará automáticamente la configuración

3. **Configuración automática**:
   - Render usará el archivo `render.yaml` para configurar el servicio
   - El comando de inicio será: `gunicorn app_chatbot:app`

4. **Variables de entorno** (opcional):
   - Puedes agregar variables de entorno en el dashboard de Render
   - Por ejemplo: `FLASK_ENV=production`

5. **Despliegue**:
   - Render desplegará automáticamente tu aplicación
   - Obtendrás una URL pública (ej: `https://tu-app.onrender.com`)

### Archivos de Configuración para Render

- `render.yaml`: Configuración del servicio web
- `gunicorn.conf.py`: Configuración del servidor WSGI
- `requirements.txt`: Dependencias de Python
- `.gitignore`: Archivos excluidos del repositorio

## 🎯 Experiencia de Usuario

### Navegación Intuitiva
1. **Menú principal** con 4 opciones principales
2. **Botones interactivos** con iconos y efectos hover
3. **Flujo guiado** paso a paso
4. **Opciones de retorno** en cada nivel
5. **Validación automática** de formularios

### Flujo de Agendar Cita
1. Seleccionar tratamiento
2. Completar datos del paciente
3. Elegir fecha disponible
4. Seleccionar hora
5. Confirmar cita
6. Recibir confirmación

## 📊 Estructura del Proyecto

```
nuevoclinica/
├── app_chatbot.py          # Aplicación Flask principal
├── templates/
│   └── chatbot.html        # Interfaz web del chatbot
├── clinica.db              # Base de datos SQLite
└── README.md               # Documentación
```

## 🎨 Características de Diseño

### Paleta de Colores
- **Primario**: Azul (#2563eb)
- **Secundario**: Azul oscuro (#1e40af)
- **Éxito**: Verde (#10b981)
- **Fondo**: Gradiente azul-morado

### Componentes
- **Burbujas de chat** con sombras suaves
- **Botones interactivos** con efectos hover
- **Formularios** con validación visual
- **Indicadores de escritura** animados
- **Mensajes de éxito** con gradientes

## 🔧 Personalización

### Modificar Tratamientos
Los tratamientos se almacenan en la base de datos SQLite. Para agregar nuevos:

1. Editar la lista `tratamientos_ejemplo` en `app_chatbot.py`
2. Reiniciar la aplicación

### Cambiar Ubicaciones
Editar la lista `ubicaciones_ejemplo` en el método `init_database()`.

### Ajustar Horarios
Modificar la lista `horas_disponibles` en el método `chat()`.

## 📱 Responsive Design

La interfaz se adapta automáticamente a:
- **Desktop**: Contenedor centrado de 500px
- **Móvil**: Pantalla completa sin bordes
- **Tablet**: Tamaño intermedio optimizado

## 🚀 Ventajas del Sistema

1. **Experiencia moderna**: Interfaz tipo chatbot real
2. **Navegación intuitiva**: Botones en lugar de números
3. **Diseño responsive**: Funciona en cualquier dispositivo
4. **Base de datos integrada**: Almacenamiento persistente
5. **Fácil personalización**: Código modular y bien estructurado
6. **Validación robusta**: Verificación de datos en tiempo real

## 🔮 Posibles Mejoras Futuras

- **Integración con WhatsApp**: API de WhatsApp Business
- **Notificaciones push**: Recordatorios de citas
- **Panel de administración**: Gestionar citas y datos
- **Autenticación**: Sistema de login para pacientes
- **Pagos online**: Integración con pasarelas de pago
- **Chat en vivo**: Conexión con agentes humanos

## 📞 Soporte

Para consultas o mejoras del sistema, contactar con el equipo de desarrollo.

---

**Desarrollado con ❤️ para clínicas dentales modernas** 