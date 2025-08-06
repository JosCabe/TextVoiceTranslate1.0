import os
import subprocess
import platform


class ReproductorAudio:
    """
    Reproduce un archivo de audio según el sistema operativo.
    """

    def reproducir(self, ruta_audio):
        if not ruta_audio or not os.path.exists(ruta_audio):
            print("❌ Archivo de audio no válido o no encontrado.")
            return

        print("🎯 Intentando reproducir el audio...")
        sistema = platform.system()
        print(f"🖥️ Sistema operativo detectado: {sistema}")

        try:
            if sistema == "Windows":
                try:
                    os.startfile(ruta_audio)
                except Exception:
                    subprocess.Popen(['wmplayer.exe', ruta_audio], shell=True)
                    print("✅ Audio reproducido con wmplayer.exe")
            elif sistema == "Darwin":  # macOS
                subprocess.call(["afplay", ruta_audio])
            elif sistema == "Linux":
                subprocess.call(["xdg-open", ruta_audio])
            else:
                print("❌ Reproducción automática no soportada en este sistema.")
        except Exception as e:
            print(f"❌ Error al reproducir el audio: {e}")
