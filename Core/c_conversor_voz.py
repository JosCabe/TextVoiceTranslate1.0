from gtts import gTTS
from langdetect import detect
import os


class ConversorVoz:
    """
    Convierte texto a voz usando gTTS y guarda el archivo mp3 original.
    """

    def __init__(self):
        self.ruta_audio = None
        self.idioma_detectado = "es"

    def convertir(self, texto, nombre_base="audio_original"):
        self.idioma_detectado = detect(texto)
        nombre_archivo = f"{nombre_base}.mp3"
        self.ruta_audio = os.path.join(os.getcwd(), nombre_archivo)

        audio = gTTS(text=texto, lang=self.idioma_detectado)
        audio.save(self.ruta_audio)

        print(f"✅ Audio guardado: {self.ruta_audio}")
        return self.ruta_audio, self.idioma_detectado
