#!/usr/bin/python
# -*- coding: utf-8 -*-
import itertools

"""
define a magic-squre: 4*4 array[][]
    | a[0][0] | a[0][1] | a[0][2] | a[0][3] |
    | a[1][0] | a[1][1] | a[1][2] | a[1][3] |
    | a[2][0] | a[2][1] | a[2][2] | a[2][3] |
    | a[3][0] | a[3][1] | a[3][2] | a[3][3] |

pick 7 number in range(1,17) as a magic-squre seed list: seed[0]~seed[6].
so:
    a[0][0] = seed[0]
    a[0][1] = seed[1]
    a[0][2] = seed[2]
    a[0][3] = 34-seed[0]-seed[1]-seed[2]

    a[1][0] = seed[3]
    a[1][1] = seed[4]
    a[1][2] = seed[5]
    a[1][3] = 34-seed[3]-seed[4]-seed[5]

    a[2][0] = seed[6]
    a[2][1] = 2*seed[0]+seed[1]+seed[2]+seed[3]-seed[5]+seed[6]-34
    a[2][2] = 68-seed[1]-seed[2]-seed[3]-seed[4]-seed[6]-2*seed[0]
    a[2][3] = seed[4]+seed[5]-seed[6]

    a[3][0] = 34-seed[3]-seed[6]-seed[0]
    a[3][1] = seed[5]-2*seed[1]-seed[2]-seed[3]-seed[4]-2*seed[0]-seed[6]+68
    a[3][2] = 2*seed[0]+seed[1]+seed[3]+seed[4]-seed[5]+seed[6]-34
    a[3][3] = seed[0]+seed[1]+seed[2]+seed[3]+seed[6]-34

see if a[][] is a magic-squre.
"""
def getms(seed):
    """get a magic squre.
    para:
        seed -- a list of 7 int number.
    return:
        ms_list -- magic squre list.
    """
    ms_list = []
    # a00 ~ a03
    ms_list.append(seed[0])
    ms_list.append(seed[1])
    ms_list.append(seed[2])
    ms_list.append(34 - seed[0] - seed[1] - seed[2])
    # a10 ~ a13
    ms_list.append(seed[3])
    ms_list.append(seed[4])
    ms_list.append(seed[5])
    ms_list.append(34 - seed[3] - seed[4] - seed[5])
    # a20 ~ a23
    ms_list.append(seed[6])
    ms_list.append(2 * seed[0] + seed[1] + seed[2] + seed[3] - seed[5] + seed[6] - 34)
    ms_list.append(68 - seed[1] - seed[2] - seed[3] - seed[4] - seed[6] - 2 * seed[0])
    ms_list.append(seed[4] + seed[5] - seed[6])
    # a30 ~ a33
    ms_list.append(34 - seed[3] - seed[6] - seed[0])
    ms_list.append(seed[5] - 2 * seed[1] - seed[2] - seed[3] - seed[4] - 2 * seed[0] - seed[6] + 68)
    ms_list.append(2 * seed[0] + seed[1] + seed[3] + seed[4] - seed[5] + seed[6] - 34)
    ms_list.append(seed[0] + seed[1] + seed[2] + seed[3] + seed[6] - 34)
    return ms_list


def isms(ms_list):
    """if array is a magic squre, return 1"""
    if len(set(ms_list)) != 16:
        return
    for k in ms_list:
        if k > 16 or k < 1:
            return
    return 1

# itertools.permutations(iterable[, r])
# return successive r length permutations of elements in the iterable.
PERM = itertools.permutations(xrange(1, 17), 7)

for i in range(0, 60000000):
    seed_list = PERM.next()
    magic_squre_list = getms(seed_list)
    if isms(magic_squre_list):
        print i, magic_squre_list
