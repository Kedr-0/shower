import random, os

ruta_limpiar = "E:\\TeraBoxDownload\\" #input("Direccion: ")


cantidad = 0
for raiz, _, archivos in os.walk(ruta_limpiar):
    cantidad += len(archivos)


validadcion = input(f"Estas a punto de eliminar {cantidad} archivos. Deseas continuar (s/n): " )

for raiz, directorios, archivos in os.walk(ruta_limpiar):

    for _archivo in archivos:

        if validadcion.lower() == "s":

            try:
                
                raiz_archivo = os.path.join(raiz,_archivo)
                
                with open(raiz_archivo, "rb+") as file:
            
                    size = os.path.getsize(raiz_archivo)
                    
                    if size == 0:
                        file.write(b'\x00')
                        size = 1

                    file.seek(0)
                    file.write(b'\x00' * size)
                    file.flush()
                    os.fsync(file.fileno())

                    file.seek(0)
                    file.write(b'\xff' * size)
                    file.flush()
                    os.fsync(file.fileno())

                    file.seek(0)
                    trash_aleatorio = os.urandom(size)
                    file.write(trash_aleatorio)
                    file.flush()
                    os.fsync(file.fileno())

            except Exception as e:
                print(f"Cierra el archivo '{_archivo}: {e}'")
                continue

            fecha = random.uniform(1704067200.0, 1735603199.0)
            os.utime(raiz_archivo, (fecha,fecha))
            
            new_name=f"temp.{random.randint(1, 9999)}"
            
            os.rename(raiz_archivo, os.path.join(raiz,new_name))
            os.remove(os.path.join(raiz,new_name))

            print(f"Archivo {_archivo}... Eliminado")
    
        else:
            exit(0)

