import json
import sys
from itertools import zip_longest
from lab_python_fp.print_result import print_result
from lab_python_fp.gen_random import gen_random
from lab_python_fp.unique import Unique
from lab_python_fp.cm_timer import cm_timer_1


@print_result
def f1(data):
    return sorted(Unique([job['job-name'].lower() for job in data], ignore_case=True))


@print_result
def f2(jobs):
    return list(filter(lambda x: x.lower().startswith('программист'), jobs))


@print_result
def f3(jobs):
    return list(map(lambda x: f"{x} с опытом Python", jobs))


@print_result
def f4(jobs):
    salaries = gen_random(len(jobs), 100000, 200000)
    return [f"{job}, зарплата {salary} руб." for job, salary in zip(jobs, salaries)]


if __name__ == '__main__':
    path = sys.argv[1] if len(sys.argv) > 1 else 'data_light.json'
    with open(path) as file:
        data = json.load(file)

    with cm_timer_1():
        f4(f3(f2(f1(data))))
