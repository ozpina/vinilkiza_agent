import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

# Inicializa el cliente moderno
client = genai.Client()

try:
    print("Enviando petición a Gemini 2.5 Flash...")
    
    # Usamos estrictamente uno de los modelos activos de tu lista
    response = client.models.generate_content(
        model='gemini-2.5-flash', 
        contents='Hola, responde únicamente con la palabra: Ok.'
    )
    
    print("\n¡Éxito total! El agente respondió:")
    print(response.text)

except Exception as e:
    print("\nOcurrió un error:")
    print(e)