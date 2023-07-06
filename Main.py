import os
import random
import datetime
import tkinter as tk
from configparser import ConfigParser


class conf():
    def __init__(self):
        self.init = {
            'last': {
                'date': '2020-01-01',
                'CD': 0,
            },
            'counter': {
                f'{i + 1:0>3}': 0 for i in range(100)
            }
        }

    def create(self):
        print(1)
        config = ConfigParser()
        config.read_dict(self.init)
        with open('conf.ini', 'w') as f:
            config.write(f, space_around_delimiters=True)


if __name__ == '__main__':
    config = ConfigParser()
    conf().create()  
    i = 0
    while i <= 1:
        if os.path.isfile('conf.ini'):
            try:
                config.read('conf.ini')
                print(2)
                break
            except:
                i += 1
                conf.create()
        else:
            i += 1
            conf().create()            
    