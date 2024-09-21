import time
import random
import threading


class Bank:
    def __init__(self):
        self.lock = threading.Lock()
        self.balance = 0

    def deposit(self):
        for i in range(100):
            amount = random.randint(50, 500)
            self.balance += amount
            print(f"Пополнение: {amount}. Баланс: {self.balance}")
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            time.sleep(0.001)

    def take(self):
        for i in range(100):
            amount = random.randint(50, 500)
            print(f"Запрос на {amount}")
            if amount <= self.balance:
                self.balance -= amount
                print(f"Снятие: {amount}. Баланс: {self.balance}")
            else:
                print(f"Запрос отклонён, недостаточно средств")
                self.lock.acquire()


if __name__ == "__main__":
    bk = Bank()
    th1 = threading.Thread(target=bk.deposit, args=(bk,))
    th2 = threading.Thread(target=bk.take, args=(bk,))

    th1.start()
    th2.start()
    th1.join()
    th2.join()

    print(f'Итоговый баланс: {bk.balance}')
