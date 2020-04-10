import datetime
import sys
import json
from pprint import pprint
from contextlib import contextmanager

def runtime(start_time, finish_time):
    script_runtime = finish_time - start_time
    script_runtime = str(script_runtime).split(':')
    print(f'Время запуска кода в менеджере контекста: {start_time}')
    print(f'Время окончания работы кода: {finish_time}')
    print(f'Времени потрачено на выполнение кода: {script_runtime[0]} часов, {script_runtime[1]} минут, {script_runtime[2]} секунд')

def decompose(deser_json):
    decomposed_json = []
    for hit in deser_json:
        temporary_dictionary = {'number': hit['num'], 'strain': hit['description'][0]['title'],
                                'len': hit['hsps'][0]['align_len'],
                                'gaps': hit['hsps'][0]['gaps'], 'sequence': hit['hsps'][0]['hseq']}
        decomposed_json.append(temporary_dictionary)
    return decomposed_json

@contextmanager
def timer(path, encoding='utf-8'):
    try:
        function_initiation = datetime.datetime.now()
        json_file = open(path, encoding = encoding)
        yield json_file
    finally:
        exc_type, exc_val, exc_tb = sys.exc_info()
        if exc_type is not None:
            print(f'Внимание! Ошибка: {exc_val}')
        json_file.close()
        function_finished = datetime.datetime.now()
        runtime(function_initiation, function_finished)


with timer('gene.json') as gene_file:
    alignments = json.load(gene_file)
    pprint(decompose(alignments['BlastOutput2'][0]['report']['results']['search']['hits']))
