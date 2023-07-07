import os
import random
import datetime
import tkinter as tk
from configparser import ConfigParser


class Conf(ConfigParser):
    def take(self):
        i = 0
        while i <= 1:
            if os.path.isfile('conf.ini'):
                try:
                    self.read('conf.ini')
                    break
                except:
                    i += 1
                    self.create()
            else:
                i += 1
                self.create()

    def create(self):
        self.init = {
            'last': {
                'date': '2020-01-01',
                'CD': 0,
            },
            'counter': {
                f'{i + 1:0>3}': 0 for i in range(100)
            }
        }
        self.read_dict(self.init)
        with open('conf.ini', 'w') as f:
            self.write(f, space_around_delimiters=True)

class Generate():
    def __init__(self):
        self.today = datetime.date.today().strftime('%Y-%m-%d')
        self.cd = random.randint(1, 100)

    def is_lately(self, lastday):
        return True if self.today == lastday else False
    
    def show(self, text):
        pass

    def go(self, config: Conf):
        if self.islately(config['last']['date'] == self.today):
            pass
        else:
            pass

if __name__ == '__main__':
    config = Conf()
    config.take()
    generate = Generate()
    generate.go(config)



    
    