from threading import Thread

from time import sleep


class Knight(Thread):
    def __init__(self, name, power):
        Thread.__init__(self)
        self.kname: str = name
        self.power: int = power
        super().__init__()

    def run(self):
        print(f'{self.kname}, на нас напали!')
        enemies = 100
        days = 0
        while enemies > 0:
            sleep(1)
            days += 1
            enemies -= self.power
            if enemies < 0:
                enemies = 0
            print(f'{self.kname} сражается {days} дней(дня), осталось {enemies} воинов ')
        print(f'{self.kname} одержал победу спустя {days} дней(дня)')


def main():
    knight1 = Knight('Sir Lancelot', 10)
    knight2 = Knight('Sir Galahad', 20)
    knight1.start()
    knight2.start()
    knight1.join()
    knight2.join()
    print(f'Все битвы окончены')


if __name__ == '__main__':
    main()
