from Core.a_lector_texto import LectorTexto
from Core.b_procesador_texto import ProcesadorTexto
from Core.c_conversor_voz import ConversorVoz
from Core.d_editor_audio import EditorAudio
from Core.e_reproductor_audio import ReproductorAudio
from Core.f_gestor_archivos import GestorArchivos
from Core.g_gestor_interaccion import GestorInteraccion


def main():
    print("🟢 Iniciando aplicación Texto a Voz...")

    #Leer texto
    lector = LectorTexto()
    lector.leer_input()
    texto_original = lector.get_texto()

    #Procesar texto (resumen si tiene más de 100 palabras)
    procesador = ProcesadorTexto()
    procesador.set_texto(texto_original)

    if procesador.contar_palabras() >= 100:
        procesador.resumir_texto()

    texto_procesado = procesador.get_texto()

    #Convertir a voz
    conversor = ConversorVoz()
    ruta_original, idioma_detectado = conversor.convertir(texto_procesado, nombre_base="audio_original")

    #Acelerar audio
    editor = EditorAudio()
    ruta_acelerado = editor.acelerar_audio(ruta_original, idioma_detectado.upper())

    # Reproducir audio
    reproductor = ReproductorAudio()
    reproductor.reproducir(ruta_acelerado)

    #Preguntar si eliminar archivos
    if GestorInteraccion.preguntar_eliminacion():
        archivos = GestorArchivos()
        archivos.eliminar_archivos([ruta_original, ruta_acelerado])
    else:
        print("🗃️ Archivos conservados por elección del usuario.")

    print("✅ Proceso completado.")

if __name__ == "__main__":
    main()
