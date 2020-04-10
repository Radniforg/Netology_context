import datetime
import sys
from contextlib import contextmanager

def runtime(start_time, finish_time):
    script_runtime = finish_time - start_time
    script_runtime = str(script_runtime).split(':')
    print(f'Время запуска кода в менеджере контекста: {start_time}')
    print(f'Время окончания работы кода: {finish_time}')
    print(f'Времени потрачено на выполнение кода: {script_runtime[0]} часов, {script_runtime[1]} минут, {script_runtime[2]} секунд')

@contextmanager
def decompose(path, encoding='utf-8'):
    try:
        function_initiation = datetime.datetime.now()
        xml = open(path, encoding = encoding)
        yield xml
    finally:
        exc_type, exc_val, exc_tb = sys.exc_info()
        if exc_type is not None:
            print(f'Внимание! Ошибка: {exc_val}')
        xml.close()
        function_finished = datetime.datetime.now()
        runtime(function_initiation, function_finished)

with decompose('gene.json') as gene_file:
    pass
