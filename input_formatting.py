import os
import pandas as pd
import cv2

# Caricare il CSV
df = pd.read_csv('data/_annotations.csv')

# Directory di output
output_dir = 'isolated_cells/'

# Creare le cartelle per le classi
classes = df['class'].unique()
for cls in classes:
    class_dir = os.path.join(output_dir, cls)
    os.makedirs(class_dir, exist_ok=True)

# Funzione per ritagliare e salvare le immagini
def save_cropped_images(df, output_dir):
    for index, row in df.iterrows():
        image_path = f"data/images/{row['filename']}"
        image = cv2.imread(image_path)
        
        # Coordinate di ritaglio
        xmin, ymin, xmax, ymax = row['xmin'], row['ymin'], row['xmax'], row['ymax']
        
        # Ritagliare l'immagine
        cropped_image = image[ymin:ymax, xmin:xmax]
        
        # Creare il percorso di salvataggio
        class_dir = os.path.join(output_dir, row['class'])
        output_path = os.path.join(class_dir, f"{os.path.splitext(row['filename'])[0]}_{index}.jpg")
        
        # Salvare l'immagine ritagliata
        cv2.imwrite(output_path, cropped_image)

save_cropped_images(df, output_dir)
