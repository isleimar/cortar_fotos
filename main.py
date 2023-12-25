import os
import csv
import gdown
from cut_photo import Cut_photos
import random
import time

data_file = "data/cracha.csv"
input_photos = "input_photos/"
output_photos = "output_photos/"
width = 1772
height = 2362

def pausa():
    m1, m2 = (10, 30)
    # Define os parâmetros para a distribuição normal
    media = m1 + ((m2 - m1)/2)  # Média do intervalo (média entre 5 e 10)
    desvio_padrao = 1.5  # Desvio padrão para controlar a dispersão
    # Gera um número aleatório usando uma distribuição normal
    intervalo_aleatorio = random.gauss(media, desvio_padrao)
    # Ajusta o número para garantir que esteja dentro do intervalo desejado (5 a 10 segundos)
    intervalo_aleatorio = max(m1, min(m2, intervalo_aleatorio))
    # Pausa por um intervalo aleatório
    time.sleep(intervalo_aleatorio)
    # O código abaixo será executado após a pausa aleatória
    print(f"Pausa concluída ({intervalo_aleatorio:.2f} segundos), continuando a execução.")


def download_file_from_google_drive(file_id, dest_path):    
    url = f'https://drive.google.com/uc?id={file_id}'
    gdown.download(url, dest_path, quiet=False)

def ler_csv(arquivo):
    with open(arquivo, 'r') as arquivo_csv:    
        leitor_csv = csv.DictReader(arquivo_csv)        
        lista_dicionarios = []
        for linha in leitor_csv:        
            lista_dicionarios.append(linha)
        return lista_dicionarios

def main():
    cut = Cut_photos()
    cut.width = width
    cut.height = height
    registros = ler_csv(data_file)
    for registro in registros:
        id = registro['id']        
        photo_in = "{}{}".format(input_photos,id)
        photo_out = "{}{}.jpg".format(output_photos,id)
        # pausa()
        if not os.path.exists(photo_in):
            download_file_from_google_drive(id,photo_in)
        if not os.path.exists(photo_in):
            raise "Fala! Arquivo não existe!"
        cut.cut(photo_in,photo_out)
        print(id)
    # cut = Cut_photos()
    # cut.width = width
    # cut.height = height
    # cut.cut(input_photo, output_photo)
    pass

if __name__ == "__main__":
    main()