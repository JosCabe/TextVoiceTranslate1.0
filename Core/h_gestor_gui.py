from Core.a_lector_texto import LectorTexto
from Core.b_procesador_texto import ProcesadorTexto
from Core.c_conversor_voz import ConversorVoz
from Core.d_editor_audio import EditorAudio
from Core.e_reproductor_audio import ReproductorAudio
from Core.f_gestor_archivos import GestorArchivos

class GestorGUI:
    """
    Clase adaptadora para usar todas las funcionalidades desde la interfaz gráfica.
    """

    def __init__(self):
        self.texto = ""
        self.lector = LectorTexto()
        self.procesador = ProcesadorTexto()
        self.conversor = ConversorVoz()
        self.editor = EditorAudio()
        self.reproductor = ReproductorAudio()
        self.archivos = GestorArchivos()


    def leer_archivo(self, ruta):
        self.lector.leer_archivo(ruta)
        self.texto = self.lector.get_texto()


    def leer_url(self, url):
        self.lector.leer_url(url)
        self.texto = self.lector.get_texto()


    def resumir_texto(self):
        self.procesador.set_texto(self.texto)
        resultado = self.procesador.resumir_texto()
        self.texto = self.procesador.get_texto()
        return resultado


    def traducir_texto(self, idioma):
        self.procesador.set_texto(self.texto)
        self.procesador.traducir_texto(idioma)
        self.texto = self.procesador.get_texto()


    def reproducir(self):
        ruta_original, idioma = self.conversor.convertir(self.texto, "audio_original")
        ruta_acelerado = self.editor.acelerar_audio(ruta_original, idioma.upper())
        self.reproductor.reproducir(ruta_acelerado)


    def cerrar_aplicacion(self):
        import sys
        sys.exit(0)
