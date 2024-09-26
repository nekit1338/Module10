import datetime
import multiprocessing

name_files = [f'./file {number}.txt' for number in range(1, 5)]


def read_info(name):
    all_data = []
    with open(name, 'r') as f:
        line = f.readline()
        while line:
            all_data.append(line.strip())
            line = f.readline()
    return all_data


if __name__ == '__main__':
    """Линейное выполнение"""
    start = datetime.datetime.now()
    for file in name_files:
        result = read_info(file)
    end = datetime.datetime.now()
    print(end - start)
    """Многопроцессное выполнение"""
    start = datetime.datetime.now()
    with multiprocessing.Pool() as pool:
        data = pool.map(read_info, name_files)
    end = datetime.datetime.now()
    print(end - start)
