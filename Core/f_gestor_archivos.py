import os


class GestorArchivos:
    """
    Gestiona operaciones básicas sobre archivos, como eliminar.
    """

    def eliminar_archivos(self, rutas):
        for archivo in rutas:
            if archivo and os.path.exists(archivo):
                try:
                    os.remove(archivo)
                    print(f"🗑️ Archivo eliminado: {archivo}")
                except Exception as e:
                    print(f"⚠️ No se pudo eliminar '{archivo}': {e}")
            else:
                print(f"⚠️ Ruta inválida o archivo no existe: {archivo}")
