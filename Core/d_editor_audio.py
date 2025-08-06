import os
import subprocess
import sys


class EditorAudio:
    """
    Usa FFmpeg para editar un archivo de audio (por ejemplo, acelerarlo).
    """

    def __init__(self):
        # Detectar si ejecutamos desde .exe (PyInstaller)
        if getattr(sys, 'frozen', False):
            base_path = sys._MEIPASS
            ffmpeg_local = os.path.join(base_path, "ffmpeg", "bin", "ffmpeg.exe")
        else:
            ffmpeg_local = os.path.join("ffmpeg", "bin", "ffmpeg.exe")

        # Ruta de respaldo
        respaldo = "D:\\ffmpeg-7.1.1-essentials_build\\bin\\ffmpeg.exe"

        # Usar la disponible
        self.ruta_ffmpeg = ffmpeg_local if os.path.exists(ffmpeg_local) else respaldo


    def acelerar_audio(self, ruta_entrada, idioma_tag, nombre_salida="audio_acelerado.mp3"):
        ruta_salida = os.path.join(os.getcwd(), nombre_salida)

        try:
            subprocess.run([
                self.ruta_ffmpeg,
                "-y",
                "-i", ruta_entrada,
                "-filter:a", "atempo=1.25",
                "-id3v2_version", "3",
                "-metadata", f"title=Idioma detectado: {idioma_tag}",
                "-metadata", "artist=Texto a Voz Inteligente",
                "-metadata", "album=Conversión Rápida",
                "-metadata", "genre=Voz Sintética",
                "-metadata", "track=1",
                ruta_salida
            ], check=True)

            if os.path.exists(ruta_salida):
                print(f"⚡ Audio acelerado correctamente: {ruta_salida}")
                return ruta_salida
            else:
                raise FileNotFoundError(f"No se encontró el archivo generado: {ruta_salida}")

        except Exception as e:
            print(f"❌ Error al acelerar audio con FFmpeg: {e}")
            return None
