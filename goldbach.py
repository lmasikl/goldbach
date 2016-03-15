# coding: utf-8

import matplotlib.pyplot
import itertools
import time


def get_prime_numbers(max_value):
    prime_numbers_list = []
    lp = [0 for i in range(0, max_value + 1)]
    for i in range(2, max_value + 1):
        if lp[i] == 0:
            lp[i] = i
            prime_numbers_list.append(i)

        for n, prime_number in enumerate(prime_numbers_list):
            if prime_number <= lp[i] and i * prime_number <= max_value:
                lp[i * prime_number] = prime_number
            else:
                break

    return [1] + prime_numbers_list


def get_even_numbers(max_value):
    return range(4, max_value + 2, 2)


def calc(number, show_graph=True):
    prime_numbers = list(get_prime_numbers(number))
    numbers_list = list(get_even_numbers(number))

    premutations = itertools.combinations(prime_numbers, 2)
    premutations_sums = [x + y for x, y in premutations]
    premutations_sums = list(sorted(premutations_sums))
    grouped_sums = itertools.groupby(premutations_sums)

    sums = [len(list(s)) for n, s in grouped_sums if n in numbers_list]

    if show_graph:
        matplotlib.pyplot.plot(numbers_list, sums, '.')
        matplotlib.pyplot.show()


def work_time():
    numbers = list(range(0, 10100, 100))
    times = []
    for x in numbers:
        begin = time.time()
        calc(x, False)
        times.append(time.time() - begin)

    matplotlib.pyplot.plot(numbers, times, '.')
    matplotlib.pyplot.show()


calc(2 * 10**4)

