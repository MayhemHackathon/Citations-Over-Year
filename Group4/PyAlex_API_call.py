# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 04:27:21 2022

@author: xwtar
"""

import pyalex
from pyalex import Works, Authors, Venues, Institutions, Concepts
import json

pyalex.config.email = "xavier.tarr@gmail.com"

pager = Works().search_filter(display_name="Boiling").paginate(per_page=26)
papers = []

for page in pager:
    for paper in page:
        papers.append(paper)
        if len(papers) > 25:
            break
    if len(papers) > 25:
        break

with open('data2.json', 'w') as f:
    json.dump(papers, f)