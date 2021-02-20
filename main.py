#!/usr/bin/env python3
'''
Usage: 
    main.py [--m] [--b] [--s]
'''
import os
import time
import sys
from PIL import Image
from docopt import docopt
from multiprocessing import Process, Pool, cpu_count
import generate_mirror
import change_brightness
import random_shadow


# PATH = '../autorace/data/'
PATH = 'test'


def get_path_list(path):
    path_list = []
    for root, dirs, files in os.walk(path, topdown=False):
        for name in dirs:
            print(os.path.join(root, name))
            path_list.append(os.path.join(root, name))
    return path_list


if __name__ == '__main__':
    args = docopt(__doc__)
    start_time = time.time()
    path_list = get_path_list(PATH)
    num_cpu = cpu_count()
    pool = Pool(processes=num_cpu)
    if args['--m']:
        pool.map(generate_mirror.generator, path_list)
    elif args['--b']:
        pool.map(change_brightness.change, path_list)
    elif args['--s']:
        pool.map(random_shadow.generator, path_list)
    pool.close()
    pool.join()
    end_time = time.time()
    print('Time used ' + time.strftime("%H:%M:%S",
                                       time.gmtime(end_time - start_time)))
