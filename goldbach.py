# coding: utf-8
import itertools

import matplotlib.pyplot


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


def get_number_of_decisions(prime_numbers, number):
    prime_numbers_less_than_number = filter(lambda n: n < number, prime_numbers)
    premutations = itertools.permutations(prime_numbers_less_than_number, 2)
    premutations_sums = [x + y for x, y in premutations]
    equal_to_number_sums = list(filter(lambda s: s == number, premutations_sums))
    return len(equal_to_number_sums) / 2


if __name__ == '__main__':
    number = 1000

    prime_numbers = list(get_prime_numbers(number))
    numbers_list = get_even_numbers(number)

    numbers_of_decisions = [get_number_of_decisions(prime_numbers, n) for n in numbers_list]

    matplotlib.pyplot.plot(numbers_list, numbers_of_decisions, 'ro')
    matplotlib.pyplot.show()

