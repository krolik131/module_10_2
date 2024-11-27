import time
import threading
class  Knight(threading.Thread):
    enemies = 100
    def __init__(self, name,power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        day= 0
        print(f' {self.name} на нас напали!')
        while self.enemies > 0:
            self.enemies = self.enemies - self.power
            day += 1
            time.sleep(1)
            print(f' {self.name} сражается {day} день(дня) осталось {self.enemies} войнов')
        print(f'{self.name} одержал победу спустя {day} дней(дня)!')

# Создание класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

thread1 = Knight(first_knight.name, first_knight.power)
thread1.start()
thread2 = Knight(second_knight.name, second_knight.power)
thread2.start()

