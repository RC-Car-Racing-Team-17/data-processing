import os
import shutil

PATH = '../autorace/data/'

if __name__ == '__main__':
    for root, dirs, files in os.walk(PATH, topdown=False):
        for name in dirs:
            last_char = name[len(name) - 1]
            if last_char == 'm' or last_char == 'l' or last_char == 'd' or last_char == 's':
                try:
                    shutil.rmtree(os.path.join(root, name))
                    print('Removed ' + os.path.join(root, name))
                except:
                    print('Fail in removing ' + os.path.join(root, name))
    print("All done")
