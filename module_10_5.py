from multiprocessing import Pool
from datetime import datetime

all_data = []

def read_info(name):
    open_file = open(name, 'r')
    while True:
        data = open_file.readline()
        if data == '':
            break
        all_data.append(data)

if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]

    time_now = datetime.now()
    for file in filenames:
        read_info(file)
    print(datetime.now() - time_now, '(линейный)')

    # time_now = datetime.now()
    # with Pool(processes=4) as pool:
    #     pool.map(read_info, filenames)
    # print(datetime.now() - time_now, '(многопроцессорный)')