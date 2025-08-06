from a_lector_texto import LectorTexto
from b_procesador_texto import ProcesadorTexto
from c_conversor_voz import ConversorVoz
from d_editor_audio import EditorAudio
from e_reproductor_audio import ReproductorAudio
from f_gestor_archivos import GestorArchivos


class AppTextoAVoz:
    """
    Clase principal que orquesta el flujo completo del programa.
    """

    def __init__(self):
        self.lector = LectorTexto()
        self.procesador = ProcesadorTexto()
        self.conversor = ConversorVoz()
        self.editor = EditorAudio()
        self.reproductor = ReproductorAudio()
        self.archivos = GestorArchivos()

    def ejecutar(self):
        #1 Leer texto desde teclado
        self.lector.leer_input()
        texto = self.lector.get_texto()

        #2 Procesar texto
        self.procesador.set_texto(texto)

        if self.procesador.contar_palabras() >= 100:
            self.procesador.resumir_texto()

        #(opcional) traducir
        #self.procesador.traducir_texto("es")

        texto_final = self.procesador.get_texto()

        #3 Convertir a voz
        ruta_original, idioma_detectado = self.conversor.convertir(texto_final, nombre_base="audio_original")

        #4 Acelerar con FFmpeg
        ruta_acelerado = self.editor.acelerar_audio(ruta_original, idioma_detectado.upper())

        #5 Reproducir
        self.reproductor.reproducir(ruta_acelerado)

        #6Eliminar archivos (opcional)
        #self.archivos.eliminar_archivos([ruta_original, ruta_acelerado])
