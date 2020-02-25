# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 09:30:13 2019

@author: 18537
"""


def biggest(aDict):

    counter = 0

    result = None

    if aDict == {}:

        return result

    else:

        for i in aDict.keys():

            if len(aDict[i]) > counter:

                result = i

    return result
print(biggest({'b': [1, 7, 5, 4, 3, 18, 10, 0], 'a': []}))