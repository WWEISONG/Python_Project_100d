import time

class Clock(object):
    """数字时钟"""

    def __init__(self, hour=0, minute=0, second=0):
        """初始化方法"""

        self._hour = hour
        self._minute = minute
        self._second = second

    def run(self):
        """走字"""
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0

    def show(self):
        """显示时间"""
        return f'{self._hour:02}:{self._minute:02}:{self._second:02}'

def main():
    clock = Clock(23, 59, 58)
    while True:
        print(clock.show())
        time.sleep(1)
        clock.run()

if __name__ == '__main__':
    main()























































