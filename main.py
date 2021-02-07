import json
import os
import glob
import sys
from PIL import Image

PATH = '../autorace/data/'
FOLDER_NAME = 'tub_7_21-02-07'

if len(sys.argv) > 1:
    FOLDER_NAME = sys.argv[1]

NEW_FOLDER_NAME = FOLDER_NAME+'-mirror'

if not os.path.isdir(PATH+NEW_FOLDER_NAME):
    os.mkdir(PATH+NEW_FOLDER_NAME)

for file_name in glob.glob(os.path.join(PATH+FOLDER_NAME, '*.json')):
    with open(file_name, encoding='utf-8', mode='r') as current_file:
        try:
            json_data = json.load(current_file)
            new_json_path = PATH+NEW_FOLDER_NAME + \
                '/' + os.path.basename(file_name)
            if os.path.basename(file_name) == 'meta.json':
                with open(new_json_path, 'w', encoding='utf-8') as f:
                    json.dump(json_data, f, ensure_ascii=False, indent=4)

            # handle image mirror
            img_path = PATH+FOLDER_NAME+'/'+json_data['cam/image_array']
            img_obj = Image.open(img_path)
            rotated_image = img_obj.transpose(Image.FLIP_LEFT_RIGHT)
            new_img_path = PATH+NEW_FOLDER_NAME + \
                '/' + json_data['cam/image_array']
            rotated_image.save(new_img_path)

            # handle new angle
            new_user_angle = -json_data['user/angle']
            new_angle = new_user_angle + json_data['user/angle_noise']
            json_data['user/angle'] = new_user_angle
            json_data['angle'] = new_angle
            with open(new_json_path, 'w', encoding='utf-8') as f:
                json.dump(json_data, f, ensure_ascii=False, indent=4)
            print("Finished: " + os.path.basename(file_name))
        except:
            print('error: ' + file_name)

print("Finished All")