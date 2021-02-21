import sys
import os
import glob
import json

path = "test/tub1"

if __name__ == '__main__':
    json_list = glob.glob(os.path.join(path, '*.json'))
    for file_name in json_list:
        if os.path.basename(file_name) == 'meta.json':
            continue
        img_path = ""
        with open(file_name, encoding='utf-8', mode='r') as current_file:
            try:
                
                json_data = json.load(current_file)
                img_path = os.path.join(
                    path, json_data['cam/image_array'])
            except:
                print("error: " + file_name)

        if not os.path.exists(img_path):
            print("Remove: " + file_name)
            os.remove(file_name)
    print("All finished")
