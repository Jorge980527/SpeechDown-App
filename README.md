SpeechDown: Aplicación Web Responsive para el Apoyo al Desarrollo del Habla 🗣️👶
📝 Descripción del Proyecto
Este proyecto es una aplicación web MVP (Producto Mínimo Viable) diseñada para apoyar el desarrollo del habla en niños, especialmente aquellos con Síndrome de Down. Su objetivo principal es proporcionar una herramienta interactiva que genere ejercicios de habla personalizados mediante la integración de Inteligencia Artificial generativa.

✨ Características Principales (MVP)
Generador de Actividades de Habla: Permite a los usuarios ingresar una palabra clave. Utilizando la API de OpenAI (GPT-3.5 Turbo), la aplicación genera un ejercicio de habla corto, divertido y enfocado en la pronunciación clara.

Interfaz de Usuario Básica: Un frontend simple, intuitivo y responsive desarrollado con HTML, CSS y JavaScript, asegurando una experiencia de usuario fluida en diferentes dispositivos.

Backend RESTful: Implementado en Python con el framework Flask, actúa como el puente entre el frontend y la potente API de OpenAI, gestionando eficientemente las solicitudes de generación de texto.

🛠️ Requisitos del Sistema
Para poner en marcha este proyecto en tu máquina local, necesitarás:

Python 3.x (se recomienda Python 3.10 o superior).

Acceso a una clave API válida de OpenAI.

🚀 Instrucciones de Despliegue y Ejecución
Sigue estos pasos detallados para configurar y ejecutar la aplicación en tu entorno local:

1. Clonar el Repositorio

Primero, obtén una copia del código fuente clonando el repositorio de Git:

git clone https://github.com/Jorge980527/SpeechDown-App.git
cd SpeechDown-App

(Asegúrate de reemplazar Jorge980527 con tu nombre de usuario de GitHub si el repositorio está bajo otra cuenta.)

2. Configuración y Ejecución del Backend (Python/Flask)

a. Crear y Activar Entorno Virtual:

Navega a la carpeta backend y crea un entorno virtual para gestionar las dependencias del proyecto de forma aislada y evitar conflictos:

cd backend
python -m venv venv

Luego, activa el entorno virtual según tu sistema operativo:

macOS / Linux:

source venv/bin/activate

Windows (Símbolo del sistema):

venv\Scripts\activate.bat

Windows (PowerShell):

.\venv\Scripts\Activate.ps1

b. Instalar Dependencias:

Con el entorno virtual activado, instala las librerías de Python necesarias para el backend:

pip install Flask flask-cors openai

c. Configurar la Clave API de OpenAI:

La aplicación requiere una clave de API de OpenAI para comunicarse con el modelo de IA. Es fundamental que esta clave se configure como una variable de entorno por razones de seguridad y para evitar exponerla en el código.

Reemplaza TU_CLAVE_API_OPENAI con tu clave API real de OpenAI.

macOS / Linux (en tu terminal, antes de ejecutar el backend):

export OPENAI_API_KEY='TU_CLAVE_API_OPENAI'

Windows (Símbolo del sistema, en tu terminal, antes de ejecutar el backend):

set OPENAI_API_KEY="TU_CLAVE_API_OPENAI"

(Consejo: Para una persistencia más cómoda en tu entorno de desarrollo, puedes añadir esta línea a tu archivo de configuración de shell (ej. .bashrc o .zshrc en Linux/macOS) o a las variables de entorno del sistema en Windows.)

d. Ejecutar el Backend:

Desde la carpeta backend y con el entorno virtual activado, inicia el servidor Flask:

python app.py

El backend se iniciará y estará accesible en http://127.0.0.1:5000/. Deja esta terminal abierta y el servidor funcionando mientras uses la aplicación.

3. Ejecutar el Frontend (Interfaz de Usuario)

El frontend es una aplicación web estática construida con HTML, CSS y JavaScript.

a. Navega a la carpeta frontend:

Abre una nueva terminal (o una pestaña en tu terminal actual) y navega a la carpeta del frontend:

cd ../frontend

b. Abre index.html en tu navegador web:

Simplemente arrastra el archivo index.html a una pestaña de tu navegador web preferido (Chrome, Firefox, Safari, Edge) o haz doble clic en él.

Una vez que tanto el backend como el frontend estén corriendo, podrás interactuar con la aplicación, ingresar palabras y generar actividades de habla personalizadas.

🏗️ Diagrama de Arquitectura
A continuación, se presenta un diagrama de bloques simplificado que ilustra la arquitectura de la aplicación SpeechDown:

(Importante: Debes crear esta imagen (architecture.png) y colocarla dentro de una carpeta llamada docs en la raíz de tu repositorio para que el enlace en el README funcione correctamente.)

💡 Ejemplos de Prompts Usados con la API de IA
El backend (app.py) utiliza el siguiente prompt principal para comunicarse con la API de OpenAI (modelo gpt-3.5-turbo) y generar las actividades de habla:

prompt = f"Crea un ejercicio de habla muy corto (2-3 oraciones) para un niño con Síndrome de Down usando la palabra '{user_word}'. Enfócate en la pronunciación clara y hazlo divertido."

Explicación del Propósito del Prompt:

Este prompt ha sido cuidadosamente diseñado para ser conciso y directo, optimizado para la generación rápida de ejercicios de habla relevantes y efectivos. Sus puntos clave son:

Personalización: Incorpora dinámicamente la palabra clave ({user_word}) proporcionada por el usuario, haciendo cada ejercicio único.

Audiencia Específica: Dirige la generación hacia "un niño con Síndrome de Down", lo que ayuda a la IA a adaptar el lenguaje, la complejidad y el vocabulario de manera apropiada.

Objetivo Terapéutico: Solicita explícitamente que el ejercicio se enfoque en la "pronunciación clara", alineándose con el objetivo principal de la aplicación.

Formato y Tono: Pide un formato "muy corto (2-3 oraciones)" y un tono "divertido" para mantener el interés y la motivación del niño durante la actividad.

Este enfoque permite obtener respuestas pertinentes y utilizables para el propósito de la aplicación, incluso en un formato de Producto Mínimo Viable (MVP).

🤝 Contribuciones
¡Las contribuciones son bienvenidas! Si deseas mejorar este proyecto, por favor, crea un "issue" para reportar un problema o sugerir una mejora, o envía un "pull request" con tus cambios.

📄 Licencia
Este proyecto está bajo la licencia MIT. Puedes ver los detalles completos en el archivo LICENSE (si lo incluyes en tu repositorio).
