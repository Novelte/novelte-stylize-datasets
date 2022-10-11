import pathlib
import os
import argparse
from tqdm import tqdm
import shutil
parser = argparse.ArgumentParser()
parser.add_argument("-a", "--annot-path", type=str, help="annotation source path")
parser.add_argument("-p", "--style-path", type=str, help="stylist image source path")
parser.add_argument("-o", "--output-path", type=str, help="annotation output path")

args = parser.parse_args()
style_path = args.style_path
annot_path = args.annot_path
output_path = args.output_path


for filename in tqdm(os.listdir(style_path)):
    if '.jpg' in filename:
        filename_array = filename.split('-')
        stylist_array = filename.split('.')

        image_index = filename_array[0]
        style_index = stylist_array[0]
        if os.path.exists(os.path.join(annot_path, (image_index + '.txt'))):
            image_annot = os.path.join(annot_path, (image_index + '.txt'))
            stylist_annot = os.path.join(output_path, (style_index + '.txt'))
            shutil.copyfile(image_annot, stylist_annot)




