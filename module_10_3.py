import threading
import random
import time


class Bank:
    def __init__(self):
        threading.Thread.__init__(self)
        self.balance = 0
        self.lock = threading.Lock()


    def deposit(self):
        for i in range(100):
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            money = random.randint(50, 500)
            self.balance += money
            print(f'Пополнение на {money} рублей. Баланс: {self.balance} рублей.')
            time.sleep(1)


    def take(self):
        for i in range(100):
            money = random.randint(50, 500)
            print(f'Запрос на снятие {money} рублей.')
            if self.balance >= money:
                self.balance -= money
                print(f'Снятие {money} рублей. Баланс: {self.balance} рублей.')
            else:
                print(f'Запрос отклонён, недостаточно средств.')
                self.lock.acquire()
            time.sleep(1)

bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')