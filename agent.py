import os
from google import genai
from dotenv import load_dotenv
from memory import user_mensaje, assistant_mensaje

load_dotenv()

# Inicializa el cliente moderno
client = genai.Client()
generation_config = genai.types.GenerateContentConfig(max_output_tokens=1000)
coversaciones = []



def chat(text_usuario):

    print("Enviando petición a Gemini 2.5 Flash...")
    user_mensaje(coversaciones, text_usuario)
    # Usamos estrictamente uno de los modelos activos de tu lista
    response = client.models.generate_content(
        model='gemini-2.5-flash', 
        contents=coversaciones,
        config = generation_config
        
    )

    assistant_mensaje(coversaciones,response.text)
    return response.text
    



if __name__ == "__main__":
    print("--- INICIANDO PRUEBA DE AGENTE EN MEMORIA ---")
    
    # Turno 1: Le damos un dato clave
    print("\n--- Turno 1 ---")
    msg1 = "Hola me llamo miguel"
    print(f"Usuario: {msg1}")
    r1 = chat(msg1)
    print(f"Bot: {r1}")
    
    # Turno 2: Comprobamos si recuerda el Turno 1 sin volverle a decir el nombre
    print("\n--- Turno 2 (Comprobando memoria) ---")
    msg2 = "¿Recuerdas cuál es mi nombre?"
    print(f"Usuario: {msg2}")
    r2 = chat(msg2)
    print(f"Bot: {r2}")
    
   # assistant_mensaje(coversaciones, answer)
  #  user_mensaje(coversaciones,'Sabes cuale es mi nombre?')