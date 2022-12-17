# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 04:27:21 2022

@author: xwtar
"""

import pyalex
from pyalex import Works, Authors, Venues, Institutions, Concepts

pyalex.config.email = "xavier.tarr@gmail.com"

Works()["W2741809807"]["open_access"]


test = Works().search("3D Printing").get()

print(test[0]["relevance_score"])