import  time
import threading

class Knight(threading.Thread):

    def __init__(self, name: str, power: int):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power


    def run(self):
        enemies = 100
        day = 0
        print(f'{self.name} , на нас напали!')
        for enemy in range(enemies):
            if enemies > 0:
                time.sleep(1)
                day += 1
                enemies -= self.power
                print(f'{self.name} сражается {day} дней(дня), осталось {enemies} воинов.')
            else:
                print(f'{self.name} одержал победу спустя {day} дней(дня)!')
                break


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()

print('Все битвы закончились!')