# Automatización Simple: Chatbot & Agente Virtual

Este proyecto es una herramienta de automatización modular escrita en Python que combina un chatbot de consola con capacidades de web scraping y consulta de APIs. Permite a los usuarios obtener información en tiempo real, como el precio de acciones y el clima, de manera sencilla y extensible.

## 🏗️ Arquitectura del Proyecto

El proyecto sigue un diseño **modular y basado en intenciones**, lo que facilita la adición de nuevas funcionalidades sin afectar el núcleo del sistema.

### Estructura de Carpetas
- `main.py`: Punto de entrada principal para una interacción rápida por consola (Regex-based).
- `agente_selenium.py`: Asistente avanzado que utiliza **Selenium** para tareas que podrían requerir automatización del navegador.
- `funciones_agente/`: Directorio que contiene los "cerebros" del agente. Cada archivo es un módulo independiente para una tarea específica.
  - `obtener_clima.py`: Integración con la API de `wttr.in`.
  - `obtener_precio_accion.py`: Integración con `yfinance`.
- `utils/`: Utilidades comunes para el procesamiento de datos.
  - `sanitizar.py`: Lógica para limpiar el lenguaje natural y extraer entidades clave.

### Flujo de Ejecución
1. **Entrada**: El usuario escribe una consulta (ej: "¿Cuál es el precio de Apple?").
2. **Detección de Intención**: El sistema identifica si se trata de clima, acciones o comandos de salida.
3. **Procesamiento (Sanitización)**: Se extrae la entidad relevante ("Apple") eliminando el ruido del lenguaje.
4. **Ejecución de Función**: Se invoca el módulo correspondiente.
5. **Respuesta**: Se devuelve el resultado al usuario.

---

## 🚀 Cómo hacerlo Escalable

Para transformar este prototipo en un sistema de grado de producción, se recomiendan los siguientes cambios:

1.  **Uso de LLMs (GPT/Claude)**: En lugar de expresiones regulares y `sanitizar.py`, integrar una API de modelo de lenguaje para manejar la extracción de intenciones y entidades de forma mucho más robusta.
2.  **Base de Datos de Conocimiento (RAG)**: Implementar una base de datos vectorial para que el agente pueda consultar documentos locales o manuales.
3.  **Sistema de Plugins**: Crear una clase base abstracta para las funciones del agente, permitiendo que nuevas habilidades se carguen dinámicamente.
4.  **API Rest / Interfaz Web**: Migrar la lógica a un framework como **FastAPI** o **Flask** para ofrecer el servicio a través de una aplicación web o móvil.
5.  **Gestión de Sesiones**: Implementar persistencia para que el agente recuerde el contexto de conversaciones previas.

---

## 🛠️ Próximos Pasos Posibles

1.  **Nuevas Funciones**:
    *   `obtener_noticias`: Resumen de las noticias más importantes del día.
    *   `gestionar_calendario`: Integración con Google Calendar para añadir eventos.
    *   `traduccion_texto`: Traducción rápida entre idiomas.
2.  **Mejoras de Selenium**: Implementar búsquedas visuales en sitios que no tienen API pública.
3.  **Seguridad**: Añadir manejo de variables de entorno (`.env`) para claves de API sensibles.
4.  **Dockerización**: Crear un `Dockerfile` para asegurar que el entorno (incluyendo Chrome y ChromeDriver) sea consistente en cualquier máquina.

---

## 📖 Documentación General

### Requisitos
*   Python 3.8+
*   Google Chrome (para el agente Selenium)
*   Librerías: `selenium`, `webdriver-manager`, `requests`, `yfinance`.

### Instalación
```bash
pip install -r requirements.txt
```

### Ejecución
Para el chatbot básico:
```bash
python main.py
```

Para el asistente con Selenium:
```bash
python agente_selenium.py
```
