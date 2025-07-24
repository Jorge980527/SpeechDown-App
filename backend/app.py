from flask import Flask, request, jsonify # 
from flask_cors import CORS # 
import os # 

# Importa la librería de OpenAI o Google Gemini, según la que vayas a usar
from openai import OpenAI # 
# from google.generativeai import configure, GenerativeModel # Si usas Google Gemini

app = Flask(__name__) # 
CORS(app) # Habilita CORS para todas las rutas, necesario para que el frontend pueda conectar 

# --- Configuración de la API de IA ---
# Asegúrate de que tu clave API esté configurada como variable de entorno
# Por ejemplo, si usas OpenAI, la variable de entorno debe llamarse OPENAI_API_KEY
# Si usas Google Gemini, debe ser GOOGLE_API_KEY

# Para OpenAI:
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY")) # 

# Para Google Gemini (descomenta y reemplaza si lo usas):
# configure(api_key=os.getenv("GOOGLE_API_KEY"))
# model = GenerativeModel('gemini-pro') # O el modelo que prefieras


@app.route('/') # 
def home(): # 
    return "Backend is running!" # 

@app.route('/generate_activity', methods=['POST']) # 
def generate_activity(): # 
    data = request.json # Obtiene los datos JSON enviados desde el frontend 
    user_word = data.get('word') # Esperamos una clave 'word' 

    if not user_word: # 
        return jsonify({"error": "Por favor, proporciona una palabra para generar la actividad."}), 400 # 

    try:
        # --- Lógica de generación con IA ---
        # Este prompt es una versión simplificada y directa para el prototipo.
        # Puedes mejorarlo con más detalles sobre sílabas, edad, etc., si tienes tiempo. 
        prompt = f"Crea un ejercicio de habla muy corto (2-3 oraciones) para un niño con Síndrome de Down usando la palabra '{user_word}'. Enfócate en la pronunciación clara y hazlo divertido."

        # Usando OpenAI:
        completion = client.chat.com.completions.create( # 
            model="gpt-3.5-turbo", # Puedes probar con "gpt-4o-mini" si está disponible y es rápido 
            messages=[ # 
                {"role": "system", "content": "Eres un asistente de terapia del habla amigable y creativo para niños con Síndrome de Down."}, # 
                {"role": "user", "content": prompt} # 
            ],
            max_tokens=100 # Limita la longitud para respuestas rápidas 
        )
        generated_text = completion.choices[0].message.content # 

        # Usando Google Gemini (descomenta y reemplaza si lo usas):
        # response = model.generate_content(prompt)
        # generated_text = response.text

        return jsonify({"activity": generated_text}) # Devuelve la actividad generada 

    except Exception as e: # 
        print(f"Error al llamar a la API de IA: {e}") # 
        return jsonify({"error": f"No se pudo generar la actividad: {str(e)}"}), 500 # 

if __name__ == '__main__': # 
    app.run(debug=True, port=5000) # Ejecuta la aplicación en el puerto 5000
