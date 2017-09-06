import itertools
import numpy as np

import timeit


def gen_ms(sd):
    ms_array = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    ms_array[0] = sd[0]
    ms_array[1] = sd[1]
    ms_array[2] = sd[2]
    ms_array[3] = 34 - sd[0] - sd[1] - sd[2]

    ms_array[4] = sd[3]
    ms_array[5] = sd[4]
    ms_array[6] = sd[5]
    ms_array[7] = - sd[3] - sd[4] - sd[5] + 34

    ms_array[8] = sd[6]
    ms_array[9] = 2 * sd[0] + sd[1] + sd[2] + sd[3] - sd[5] + sd[6] - 34
    ms_array[10] = - 2 * sd[0] - sd[1] - sd[2] - sd[3] - sd[4] - sd[6] + 68
    ms_array[11] = sd[4] + sd[5] - sd[6]

    ms_array[12] = - sd[0] - sd[3] - sd[6] + 34
    ms_array[13] = - 2 * sd[0] - 2 * sd[1] - sd[2] - sd[3] - sd[4] + sd[5] - sd[6] + 68
    ms_array[14] = 2 * sd[0] + sd[1] + sd[3] + sd[4] - sd[5] + sd[6] - 34
    ms_array[15] = sd[0] + sd[1] + sd[2] + sd[3] + sd[6] - 34

    return ms_array


def gen_ms_mat(sd):
    xx = np.append(np.array(sd), [1])
    yy = np.array([[1, 0, 0, -1, 0, 0, 0, 0, 0, 2, -2, 0, -1, -2, 2, 1],
                   [0, 1, 0, -1, 0, 0, 0, 0, 0, 1, -1, 0, 0, -2, 1, 1],
                   [0, 0, 1, -1, 0, 0, 0, 0, 0, 1, -1, 0, 0, -1, 0, 1],
                   [0, 0, 0, 0, 1, 0, 0, -1, 0, 1, -1, 0, -1, -1, 1, 1],
                   [0, 0, 0, 0, 0, 1, 0, -1, 0, 0, -1, 1, 0, -1, 1, 0],
                   [0, 0, 0, 0, 0, 0, 1, -1, 0, -1, 0, 1, 0, 1, -1, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, -1, -1, -1, -1, 1, 1],
                   [0, 0, 0, 34, 0, 0, 0, 34, 0, -34, 68, 0, 34, 68, -34, -34]])
    ms_array = np.matmul(xx, yy)
    return ms_array


def isms(ms_array):
    if len(set(ms_array)) != 16:
        return
    for k in ms_array:
        if k > 16 or k < 1:
            return
    return 1


def test():
    PERM = itertools.permutations(range(1, 17), 7)
    for i in PERM:
        magic_squre = gen_ms(i)
        if isms(magic_squre):
            print(i, magic_squre)


if __name__ == '__main__':
    t1 = timeit.Timer('test()', 'from __main__ import test')
    print(t1.timeit(1))

