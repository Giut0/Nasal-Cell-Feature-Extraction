import os
import csv

def genera_csv_per_immagini(directory_base, nome_file_csv):
    # Lista per memorizzare le informazioni delle immagini
    dati_immagini = []

    # Percorri la directory base
    for root, dirs, files in os.walk(directory_base):
        for file in files:
            # Ottieni il percorso completo del file
            percorso_completo = os.path.join(root, file)
            # Ottieni la cartella dove si trova il file
            nome_cartella = os.path.basename(root)
            # Aggiungi le informazioni alla lista
            dati_immagini.append([file, nome_cartella])

    # Scrivi i dati nel file CSV
    with open(nome_file_csv, mode='w', newline='') as file_csv:
        writer = csv.writer(file_csv)
        writer.writerow(['filename', 'class'])
        writer.writerows(dati_immagini)

directory_base = 'isolated_cells/'
nome_file_csv = 'isolated_cells/single_cell_dataset.csv'
genera_csv_per_immagini(directory_base, nome_file_csv)
