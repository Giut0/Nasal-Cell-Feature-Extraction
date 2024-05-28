import os
import pandas as pd
import cv2

'''
This script is used to isolate cells from the original images by cutting out the individual cells and saving them in the folder of the class they belong to.
'''

df = pd.read_csv('data/_annotations.csv')
output_dir = 'isolated_cells/'

classes = df['class'].unique()

for cls in classes:
    class_dir = os.path.join(output_dir, cls)
    os.makedirs(class_dir, exist_ok=True)

def save_cropped_images(df, output_dir):

    for index, row in df.iterrows():
        image_path = f"data/images/{row['filename']}"
        image = cv2.imread(image_path)
        
        # Clip coordinates
        xmin, ymin, xmax, ymax = row['xmin'], row['ymin'], row['xmax'], row['ymax']
        
        # Crop the image
        cropped_image = image[ymin:ymax, xmin:xmax]
        
        class_dir = os.path.join(output_dir, row['class'])
        output_path = os.path.join(class_dir, f"{os.path.splitext(row['filename'])[0]}_{index}.jpg")
        
        # Saving the cropped image
        cv2.imwrite(output_path, cropped_image)

save_cropped_images(df, output_dir)
