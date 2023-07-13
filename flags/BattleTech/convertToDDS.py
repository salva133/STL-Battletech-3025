import os
from PIL import Image
import pyDDS

# Funktion zum Umwandeln von Bildern in DDS
def convert_to_dds(input_filename, output_filename):
    img = Image.open(input_filename)
    raw_image = img.tobytes()
    dds_image = pyDDS.ddsFormat(raw_image, img.size[0], img.size[1])
    with open(output_filename, 'wb') as f:
        f.write(dds_image)

# Hole eine Liste aller Dateien im aktuellen Verzeichnis
files = os.listdir('.')

# Filtere auf JPG- und PNG-Dateien
image_files = [f for f in files if f.lower().endswith(('.png', '.jpg'))]

# Konvertiere jede Bild-Datei in DDS
for image_file in image_files:
    base_name = os.path.splitext(image_file)[0]
    convert_to_dds(image_file, f'{base_name}.dds')
