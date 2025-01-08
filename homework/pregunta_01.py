# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""


def pregunta_01():
    import zipfile
    import os
    import pandas as pd
    ruta_zip="files/input.zip"
    ruta_ext="files"
    ruta_out="files/output"
    ruta_datos="files/input"
    def extractor():
        try:
            if os.path.exists(ruta_ext) and os.listdir(ruta_ext):
                print(f"El archivo ya está extraído en: {ruta_ext}")
            else:
                with zipfile.ZipFile(ruta_zip, 'r') as zip_ref:
                    zip_ref.extractall(ruta_ext)
                    print(f"Archivos extraídos en: {ruta_ext}")
            
        except FileNotFoundError:
            print("archivo no encontrado")
        except FileExistsError:
            print("archivo invalido")

    def create_output():
        os.makedirs(ruta_out, exist_ok=True)
        print(f"carpeta de salida creado o ya existente en {ruta_out}")
    
    def directory(directorio):
        datos = []
        for sentimiento in ['positive', 'negative', 'neutral']:
            sentimiento_dir = os.path.join(directorio, sentimiento)
            if os.path.exists(sentimiento_dir):
                for archivo in os.listdir(sentimiento_dir):
                    ruta_archivo = os.path.join(sentimiento_dir, archivo)
                    if os.path.isfile(ruta_archivo):
                        with open(ruta_archivo, 'r', encoding='utf-8') as f:
                            frase = f.read().strip()
                            datos.append({'phrase': frase, 'target': sentimiento})
        return datos
        
    def action():
        train_data = directory(os.path.join(ruta_datos, 'train'))
        test_data = directory(os.path.join(ruta_datos, 'test'))

        pd.DataFrame(train_data).to_csv(os.path.join(ruta_out, 'train_dataset.csv'), index=False)
        pd.DataFrame(test_data).to_csv(os.path.join(ruta_out, 'test_dataset.csv'), index=False)
    

    def work():
        extractor()
        create_output()
        action()
        print("datos manipulados")
    work()

pregunta_01()
    
    # """
    # La información requerida para este laboratio esta almacenada en el
    # archivo "files/input.zip" ubicado en la carpeta raíz.
    # Descomprima este archivo.

    # Como resultado se creara la carpeta "input" en la raiz del
    # repositorio, la cual contiene la siguiente estructura de archivos:


    # ```
    # train/
    #     negative/
    #         0000.txt
    #         0001.txt
    #         ...
    #     positive/
    #         0000.txt
    #         0001.txt
    #         ...
    #     neutral/
    #         0000.txt
    #         0001.txt
    #         ...
    # test/
    #     negative/
    #         0000.txt
    #         0001.txt
    #         ...
    #     positive/
    #         0000.txt
    #         0001.txt
    #         ...
    #     neutral/
    #         0000.txt
    #         0001.txt
    #         ...
    # ```

    # A partir de esta informacion escriba el código que permita generar
    # dos archivos llamados "train_dataset.csv" y "test_dataset.csv". Estos
    # archivos deben estar ubicados en la carpeta "output" ubicada en la raiz
    # del repositorio.

    # Estos archivos deben tener la siguiente estructura:

    # * phrase: Texto de la frase. hay una frase por cada archivo de texto.
    # * sentiment: Sentimiento de la frase. Puede ser "positive", "negative"
    #   o "neutral". Este corresponde al nombre del directorio donde se
    #   encuentra ubicado el archivo.

    # Cada archivo tendria una estructura similar a la siguiente:

    # ```
    # |    | phrase                                                                                                                                                                 | target   |
    # |---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
    # |  0 | Cardona slowed her vehicle , turned around and returned to the intersection , where she called 911                                                                     | neutral  |
    # |  1 | Market data and analytics are derived from primary and secondary research                                                                                              | neutral  |
    # |  2 | Exel is headquartered in Mantyharju in Finland                                                                                                                         | neutral  |
    # |  3 | Both operating profit and net sales for the three-month period increased , respectively from EUR16 .0 m and EUR139m , as compared to the corresponding quarter in 2006 | positive |
    # |  4 | Tampere Science Parks is a Finnish company that owns , leases and builds office properties and it specialises in facilities for technology-oriented businesses         | neutral  |
    # ```


    # """
