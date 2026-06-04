conversaciones = []


def user_mensaje(coversaciones, text):
  user = {
      "role": 'user',
      "parts": [{"text": text}]
  }
  coversaciones.append(user)

def assistant_mensaje(coversaciones, text):
    assistant = {
        "role": 'model',
        "parts": [{"text": text}]
    }
    coversaciones.append(assistant)
