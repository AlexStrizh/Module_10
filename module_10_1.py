import threading
from time import sleep
from datetime import datetime


def write_words(word_count, file_name):
    file = open(file_name, 'a', encoding='utf-8')
    for word in range(word_count):
        file.write(f'Какое-то слово №{word + 1}\n')
        sleep(0.1)
    file.close()
    print(f'Завершилась запись в файл {file_name}')


time_now = datetime.now()

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

time_stop = datetime.now()
time_run = time_stop - time_now

print(f'Время работы функций {time_run}')

time_now_2 = datetime.now()

thread_1 = threading.Thread(target=write_words, args=(10, 'example5.txt'))
thread_2 = threading.Thread(target=write_words, args=(30, 'example6.txt'))
thread_3 = threading.Thread(target=write_words, args=(200, 'example7.txt'))
thread_4 = threading.Thread(target=write_words, args=(100, 'example8.txt'))

thread_1.start()
thread_2.start()
thread_3.start()
thread_4.start()

thread_1.join()
thread_2.join()
thread_3.join()
thread_4.join()

time_stop = datetime.now()
time_run_2 = time_stop - time_now_2

print(f'Время работы потоков {time_run_2}')

print(f'Потоки выполняются на {time_run-time_run_2} секунд быстрее функций')