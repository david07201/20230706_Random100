import os
import random
import datetime
from configparser import ConfigParser

import Window


class Conf(ConfigParser):
    def take(self) -> None:
        i = 0
        while i <= 1:
            if os.path.isfile('conf.ini'):
                try:
                    self.read('conf.ini')
                    break
                except:
                    i += 1
                    self.create()
                    self.set_ini()
            else:
                i += 1
                self.create()
                self.set_ini()

    def create(self) -> None:
        self.init = {
            'last': {
                'date': '2020-01-01',
                'CD': '000',
            },
            'counter': {
                f'{i + 1:0>3}': 0 for i in range(100)
            }
        }
        self.read_dict(self.init)

    def set_ini(self) -> None:
        with open('conf.ini', 'w') as f:
            self.write(f, space_around_delimiters=True)

class Generate():
    def __init__(self, mainwin:Window.Window):
        self.today: str = datetime.date.today().strftime('%Y-%m-%d')
        self.cd: str = f'{random.randint(1, 100):0>3}'
        self.mainwin = mainwin

    def is_lately(self, lastday: str) -> bool:
        return True if self.today == lastday else False
    
    def show(self, cd: str, count: int, text: str='') -> None:
        self.mainwin.label1['text'] = '日期：' + self.today
        self.mainwin.label2['text'] = text + '今天的 CD 號碼為：'
        self.mainwin.label3['text'] = cd
        self.mainwin.label4['text'] = f'累計 {count} 次。'

    def go(self, config: Conf) -> None:
        if self.is_lately(config['last']['date']):
            self.show(
                text='今天已經選過囉！', 
                cd=config['last']['CD'], 
                count=config['counter'].getint(config['last']['CD'])
            )
        else:
            config.set('last', 'date', self.today)
            config.set('last', 'CD', self.cd)
            config.set(
                'counter', self.cd, str(config['counter'].getint(self.cd) + 1))
            config.set_ini()
            self.show(
                cd=self.cd, 
                count=config['counter'].getint(self.cd)
            )


if __name__ == '__main__':
    mainwin = Window.Window()

    config = Conf()
    config.take()
    generate = Generate(mainwin)
    generate.go(config)

    mainwin.mainloop()