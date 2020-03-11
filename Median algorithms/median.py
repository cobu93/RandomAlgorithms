import numpy as np
import argparse
import time 
import math


def r_select(array, position):
    splitter = np.random.randint(0, len(array), size=1)[0]

    positive_part = []
    negative_part = []

    for index, element in enumerate(array):
        if element <= array[splitter] and index != splitter:
            negative_part.append(element)
        elif element > array[splitter]:
            positive_part.append(element)

    if len(negative_part) == position - 1:
        return array[splitter]
    elif len(negative_part) >= position:
        return r_select(negative_part, position)
    else:
        return r_select(positive_part, position - 1 - len(negative_part))

def r_median(array):
    n = len(array)
    r_subset = np.random.choice(array, size=math.ceil(n ** 0.75))
    r_subset = np.sort(r_subset)
    d_pos = math.floor(0.5 * (n ** 0.75) - math.sqrt(n)) - 1
    d_pos = 0 if d_pos < 0 else d_pos
    u_pos = math.ceil(0.5 * (n ** 0.75) + math.sqrt(n)) - 1

    d = r_subset[d_pos]
    u = r_subset[u_pos]

    C = []
    l_d = 0
    l_u = 0

    for element in array:
        if element >= d and element <= u:
            C.append(element)

        if element < d:
            l_d += 1
        elif element > u:
            l_u += 1 

    if l_d > n / 2 or l_u > n / 2:
        return None, 1.0

    if len(C) > 4 * (n ** 0.75):
        return None, 1.0

    return np.sort(C)[math.floor(n / 2) - l_d - 1], n ** -0.25 


parser = argparse.ArgumentParser(description='Get median of random array of integers.')
parser.add_argument('length', type=int, help='Array length.')
parser.add_argument('max', type=int, help='Max value in array.')
parser.add_argument('-r', '--reps', required=False, type=int, default=5, help='Repetitions for r_median algorithm.')

args = parser.parse_args()


random_array = np.random.randint(1, args.max + 1, size=args.length)

rs_start_time = time.time()
r_select_median = r_select(random_array.tolist(), math.ceil(len(random_array) / 2))
rs_end_time = time.time()


rm_start_time = time.time()
r_m_median = None
r_median_prob = 1.0
for i in range(0, args.reps):
    i_r_median, i_r_median_prob = r_median(random_array)
    if i_r_median is not None:
        r_median_prob *= i_r_median_prob
        if r_m_median is None:
            r_m_median = i_r_median
        elif r_m_median != i_r_median:
            raise Exception('Medians were distinct! ({}, {})'.format(r_m_median, i_r_median)) 

rm_end_time = time.time()


lower_median = math.floor((random_array.shape[0] - 1)/ 2)
real_medians = np.sort(random_array)[lower_median]

print('Real median:{}'.format(real_medians))
print('R-Select median:{}    Elapsed time:{} seconds'.format(r_select_median, rs_end_time - rs_start_time))
print('R-Median median:{}    Probability:{}    Elapsed time:{} seconds'.format(r_m_median, 1 - r_median_prob, rm_end_time - rm_start_time))