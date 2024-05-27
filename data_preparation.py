import os
import csv

'''
This script generates a csv file containing the file name and class for each isolated cell image.
'''

def generate_csv_file(base_directory, csv_file):

    img_data = []

    for root, dirs, files in os.walk(base_directory):
        for file in files:
            # Get file complete path
            complete_path = os.path.join(root, file)
            # Get the folder where the file is located
            directory_name = os.path.basename(root)
            img_data.append([file, directory_name])

    # Write data to csv file
    with open(csv_file, mode='w', newline='') as file_csv:
        writer = csv.writer(file_csv)
        writer.writerow(['filename', 'class'])
        writer.writerows(img_data)

base_directory = 'isolated_cells/'
csv_file = 'isolated_cells/single_cell_dataset.csv'
generate_csv_file(base_directory, csv_file)
