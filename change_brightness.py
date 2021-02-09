import os
import glob
import json
from PIL import Image, ImageEnhance

LIGHT_FACTOR = 1.5
DARK_FACTOR = 0.5


def change(folder_name):
    light_folder_name = folder_name + '-l'
    dark_folder_name = folder_name + '-d'
    if not os.path.isdir(light_folder_name):
        os.mkdir(light_folder_name)
    if not os.path.isdir(dark_folder_name):
        os.mkdir(dark_folder_name)
    for file_name in glob.glob(os.path.join(folder_name, '*.json')):
        with open(file_name, encoding='utf-8', mode='r') as current_file:
            try:
                json_data = json.load(current_file)
                # copy json files
                light_json_path = light_folder_name + \
                    '/' + os.path.basename(file_name)
                dark_json_path = dark_folder_name + \
                    '/' + os.path.basename(file_name)
                with open(light_json_path, 'w', encoding='utf-8') as f:
                    json.dump(json_data, f, ensure_ascii=False, indent=4)
                with open(dark_json_path, 'w', encoding='utf-8') as f:
                    json.dump(json_data, f, ensure_ascii=False, indent=4)
                if os.path.basename(file_name) == 'meta.json':
                    continue

                img_path = folder_name+'/'+json_data['cam/image_array']
                img_obj = Image.open(img_path)
                enhancer = ImageEnhance.Brightness(img_obj)
                # create light image
                img_light = enhancer.enhance(LIGHT_FACTOR)
                new_img_path = light_folder_name + \
                    '/' + json_data['cam/image_array']
                img_light.save(new_img_path)

                # create dark image
                img_dark = enhancer.enhance(DARK_FACTOR)
                new_img_path = dark_folder_name + \
                    '/' + json_data['cam/image_array']
                img_dark.save(new_img_path)
                # print("Finished: " + os.path.basename(file_name))
            except:
                print('error: ' + file_name)
    print(folder_name + ' finished')
