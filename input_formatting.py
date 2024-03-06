import pandas as pd

def convert_coordinates(filename, width, height, class_name, xmin, ymin, xmax, ymax):
    # Calcola le nuove coordinate
    x = (xmin + xmax) / 2 / width
    y = (ymin + ymax) / 2 / height
    new_width = (xmax - xmin) / width
    new_height = (ymax - ymin) / height

    # Mappa le classi in valori numerici
    class_mapping = {
        "epithelial": 0,
        "neutrophil": 1,
        "eosinophil": 2,
        "muciparous": 3,
        "artefatto": 4,
        "lymphocyte": 5,
        "epithelial ciliated": 6,
        "batteri": 7,
        "metaplastic": 8,
        "mast cell": 9
    }
    class_id = class_mapping.get(class_name, -1)

    return class_id, x, y, new_width, new_height


def write_output(filename, data):
    with open(filename, 'a') as f:
        for item in data:
            f.write(' '.join(map(str, item)) + '\n')

data = pd.read_csv("_annotations.csv", delimiter=",")

for index, row in data.iterrows():
    filename = row["filename"]
    width = row["width"]
    height = row["height"]
    class_name = row["class"]
    xmin = row["xmin"]
    ymin = row["ymin"]
    xmax = row["xmax"]
    ymax = row["ymax"]
    class_id, x, y, new_width, new_height = convert_coordinates(filename, width, height, class_name, xmin, ymin, xmax, ymax)
    output_filename = "labels/" + filename.replace(".jpg", ".txt")
    output_data = [(class_id, x, y, new_width, new_height)]
    write_output(output_filename, output_data)

