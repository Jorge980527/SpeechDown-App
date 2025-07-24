# SpeechDown: Aplicación Web Responsive para el Apoyo al Desarrollo del Habla 🗣️👶📝

## 📘 Descripción del Proyecto

**SpeechDown** es una aplicación web **MVP (Producto Mínimo Viable)** diseñada para apoyar el desarrollo del habla en niños, especialmente aquellos con **Síndrome de Down**.  
Su objetivo principal es proporcionar una herramienta interactiva que genere ejercicios de habla personalizados mediante la integración de **Inteligencia Artificial generativa**.

---

## ✨ Características Principales (MVP)

- **🎤 Generador de Actividades de Habla**  
  Permite a los usuarios ingresar una palabra clave. Utilizando la API de OpenAI (GPT-3.5 Turbo), la aplicación genera un ejercicio de habla corto, divertido y enfocado en la pronunciación clara.

- **🖥️ Interfaz de Usuario Básica**  
  Un frontend simple, intuitivo y responsive desarrollado con **HTML, CSS y JavaScript**, asegurando una experiencia de usuario fluida en diferentes dispositivos.

- **🔌 Backend RESTful**  
  Implementado en **Python con el framework Flask**, actúa como el puente entre el frontend y la potente API de OpenAI, gestionando eficientemente las solicitudes de generación de texto.

---

## 🛠️ Requisitos del Sistema

Para poner en marcha este proyecto en tu máquina local, necesitarás:

- Python 3.x (se recomienda **Python 3.10 o superior**)
- Acceso a una **clave API válida de OpenAI**

---

## 🚀 Instrucciones de Despliegue y Ejecución

### 1. Clonar el Repositorio

```bash
git clone https://github.com/Jorge980527/SpeechDown-App.git
cd SpeechDown-App
```

(Asegúrate de reemplazar `Jorge980527` con tu nombre de usuario de GitHub si el repositorio está bajo otra cuenta.)

---

### 2. Configuración y Ejecución del Backend (Python/Flask)

#### a. Crear y Activar Entorno Virtual

```bash
cd backend
python -m venv venv
```

**Activar el entorno virtual según el sistema operativo:**

- **macOS / Linux:**

```bash
source venv/bin/activate
```

- **Windows (Símbolo del sistema):**

```cmd
venv\Scripts\activate.bat
```

- **Windows (PowerShell):**

```powershell
.\venv\Scripts\Activate.ps1
```

---

#### b. Instalar Dependencias

```bash
pip install Flask flask-cors openai
```

---

#### c. Configurar la Clave API de OpenAI

Reemplaza `TU_CLAVE_API_OPENAI` con tu clave API real de OpenAI.

- **macOS / Linux:**

```bash
export OPENAI_API_KEY='TU_CLAVE_API_OPENAI'
```

- **Windows (Símbolo del sistema):**

```cmd
set OPENAI_API_KEY="TU_CLAVE_API_OPENAI"
```

- **Windows (PowerShell):**

```powershell
$env:OPENAI_API_KEY="TU_CLAVE_API_OPENAI"
```

---

#### d. Ejecutar el Backend

```bash
python app.py
```

El backend se iniciará y estará accesible en:  
**http://127.0.0.1:5000/**

---

### 3. Ejecutar el Frontend (Interfaz de Usuario)

#### a. Navega a la carpeta frontend

```bash
cd ../frontend
```

#### b. Abre `index.html` en tu navegador web

- Puedes **arrastrar el archivo** `index.html` a una pestaña de tu navegador  
- O **hacer doble clic** sobre el archivo

---

## 🏗️ Diagrama de Arquitectura

https://drive.google.com/file/d/1TFQDw441G6IdQWntz4rSyKqb6N1JCfu7/view?usp=sharing
https://drive.google.com/file/d/1z0Wa0w6QWNMkS-xJpAWqfEwhJTipQjJ_/view?usp=sharing
---

## 💡 Ejemplos de Prompts Usados con la API de IA

```python
prompt = f"Crea un ejercicio de habla muy corto (2-3 oraciones) para un niño con Síndrome de Down usando la palabra '{user_word}'. Enfócate en la pronunciación clara y hazlo divertido."
```

### Explicación del Prompt

- **Personalización:** Usa la palabra clave ingresada por el usuario (`{user_word}`)
- **Audiencia específica:** Enfocado en niños con **Síndrome de Down**
- **Objetivo terapéutico:** Pide ejercicios centrados en la **pronunciación clara**
- **Formato y tono:** Ejercicios **cortos y divertidos** para mantener el interés



