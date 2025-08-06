import trafilatura

class LectorTexto:
    """
    Clase encargada de obtener texto desde distintas fuentes:
    - Entrada manual
    - Archivo local
    - URL de artículo web
    """

    def __init__(self):
        self.texto = ""


    def leer_input(self):
        self.texto = input("De Texto a Voz, introduce el texto: ")


    def leer_archivo(self, ruta):
        try:
            with open(ruta, "r", encoding="utf-8") as archivo:
                self.texto = archivo.read()
        except FileNotFoundError:
            print("Archivo no encontrado.")


    def leer_url(self, url):
        try:
            downloaded = trafilatura.fetch_url(url)
            if downloaded:
                self.texto = trafilatura.extract(downloaded, include_comments=False)
                return "Texto extraído correctamente de la URL."
            else:
                self.texto = ""
                return "No se pudo descargar el contenido de la URL."
        except Exception as e:
            print(f"Error al procesar la URL: {e}")


    def get_texto(self):
        return self.texto
