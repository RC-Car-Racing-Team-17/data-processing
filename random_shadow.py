import sys
import os
import glob
import json
import cv2
from PIL import Image
sys.path.append('Automold/')
import Automold as am


def generator(folder_name):
    new_folder_name = folder_name + '-s'

    if not os.path.isdir(new_folder_name):
        os.mkdir(new_folder_name)

    for file_name in glob.glob(os.path.join(folder_name, '*.json')):
        with open(file_name, encoding='utf-8', mode='r') as current_file:
            try:
                json_data = json.load(current_file)
                # copy json files
                new_json_path = os.path.join(
                    new_folder_name, os.path.basename(file_name))
                if os.path.basename(file_name) == 'meta.json':
                    with open(new_json_path, 'w', encoding='utf-8') as f:
                        json.dump(json_data, f, ensure_ascii=False, indent=4)
                    continue

                # generate random shadow in new image
                img_path = os.path.join(
                    folder_name, json_data['cam/image_array'])
                img_obj = cv2.imread(img_path)
                img_shadow = am.add_shadow(img_obj)
                new_img_path = os.path.join(
                    new_folder_name, json_data['cam/image_array'])
                cv2.imwrite(new_img_path, img_shadow)
                with open(new_json_path, 'w', encoding='utf-8') as f:
                    json.dump(json_data, f, ensure_ascii=False, indent=4)
            except:
                if os.path.basename(file_name) == 'meta.json':
                    print('skipping: ' + file_name)
                else:
                    print('error: ' + file_name)
    print(folder_name + ' finished')


if __name__ == '__main__':
    pass
