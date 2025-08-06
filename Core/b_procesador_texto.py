from langdetect import detect
from googletrans import Translator
from summa.summarizer import summarize
import jieba


class ProcesadorTexto:
    """
    Clase encargada de analizar, traducir y resumir un texto.
    Requiere que se le pase el texto mediante set_texto().
    """

    def __init__(self):
        self.texto = ""


    def set_texto(self, texto):
        self.texto = texto


    def get_texto(self):
        return self.texto


    def contar_palabras(self):
        idioma = detect(self.texto)
        if idioma.startswith("zh"):
            palabras = list(jieba.cut(self.texto))
            return len(palabras)
        else:
            return len(self.texto.split())


    def resumir_texto(self, min_palabras=100, num_oraciones=5):
        idioma_actual = detect(self.texto)

        if idioma_actual.startswith("zh"):
            print("🔍 Segmentando texto en chino con jieba...")
            palabras_chinas = list(jieba.cut(self.texto))
            texto_segmentado = " ".join(palabras_chinas)
        else:
            texto_segmentado = self.texto

        if len(texto_segmentado.split()) < min_palabras:
            print(f"\n⚠️ El texto tiene menos de {min_palabras} palabras. No se puede resumir.")
            return False

        print(f"\n🧠 Generando resumen...")
        resumen = summarize(self.texto, split=True)
        if resumen:
            resumen_texto = " ".join(resumen[:num_oraciones])
            self.texto = resumen_texto
            idioma_actual = detect(self.texto).upper()
            print(f"\n🔽🔽🔽 RESUMEN EN {idioma_actual} 🔽🔽🔽\n" + "-" * 30)
            print(self.texto)
            return idioma_actual


    def traducir_texto(self, idioma_destino="en"):
        idioma_detectado = detect(self.texto)
        print(f"\n🌐 Traduciendo del idioma {idioma_detectado.upper()} a {idioma_destino.upper()}...")

        try:
            traductor = Translator()
            traduccion = traductor.translate(self.texto, src=idioma_detectado, dest=idioma_destino)
            self.texto = traduccion.text
            print("✅ Traducción completada.")
            return idioma_detectado
        except Exception as e:
            print(f"❌ Error al traducir el texto: {e}")
