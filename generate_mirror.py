import json
import os
import glob
import sys
from PIL import Image


def generator(folder_name):
    new_folder_name = folder_name+'-m'

    if not os.path.isdir(new_folder_name):
        os.mkdir(new_folder_name)

    for file_name in glob.glob(os.path.join(folder_name, '*.json')):
        with open(file_name, encoding='utf-8', mode='r') as current_file:
            try:
                json_data = json.load(current_file)
                new_json_path = new_folder_name + \
                    '/' + os.path.basename(file_name)
                if os.path.basename(file_name) == 'meta.json':
                    with open(new_json_path, 'w', encoding='utf-8') as f:
                        json.dump(json_data, f, ensure_ascii=False, indent=4)

                # handle image mirror
                img_path = folder_name+'/'+json_data['cam/image_array']
                img_obj = Image.open(img_path)
                rotated_image = img_obj.transpose(Image.FLIP_LEFT_RIGHT)
                new_img_path = new_folder_name + \
                    '/' + json_data['cam/image_array']
                rotated_image.save(new_img_path)

                # handle new angle
                new_user_angle = -json_data['user/angle']
                new_angle = new_user_angle + json_data['user/angle_noise']
                json_data['user/angle'] = new_user_angle
                json_data['angle'] = new_angle
                with open(new_json_path, 'w', encoding='utf-8') as f:
                    json.dump(json_data, f, ensure_ascii=False, indent=4)
                # print("Finished: " + os.path.basename(file_name))
            except:
                if os.path.basename(file_name) == 'meta.json':
                    print('skipping: ' + file_name)
                else:
                    print('error: ' + file_name)
    print(folder_name + ' finished')


if __name__ == '__main__':
    pass
