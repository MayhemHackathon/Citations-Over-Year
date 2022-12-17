# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 04:27:21 2022

@author: xwtar
"""

import pyalex
from pyalex import Works, Authors, Venues, Institutions, Concepts
import json

#Need to pull cited_by_count and works_count from authorships
# def Pull_Cited_By_Count:
    
#Need the count from referenced_works
# def Count_Referenced_Works:

#Need counts by year cumulative for five years after publication
# def Five_Cumulative_Years

pyalex.config.email = "xavier.tarr@gmail.com"

#pager = Works().search_filter(publication_year=2017,is_retracted=0 ).paginate(per_page=26)
pager_2017 = Works().filter(publication_year=2017, is_retracted=False, is_paratext=False).paginate(per_page=200)
pager_2016 = Works().filter(publication_year=2016, is_retracted=False, is_paratext=False).paginate(per_page=200)
pager_2015 = Works().filter(publication_year=2015, is_retracted=False, is_paratext=False).paginate(per_page=200)
pager_2014 = Works().filter(publication_year=2014, is_retracted=False, is_paratext=False).paginate(per_page=200)
pager_2013 = Works().filter(publication_year=2013, is_retracted=False, is_paratext=False).paginate(per_page=200)

papers = []
paper_formatted = []

for page in pager_2017:
    for paper in page:
        paper_formatted = [paper['id'], paper['doi'],paper['title'],paper['publication_year'],paper['host_venue'],
                      paper['type'],paper['open_access'],paper['authorships'],paper['concepts'],paper['referenced_works'],
                      paper['counts_by_year'],paper['abstract']]
        papers.append(paper_formatted)
        if len(papers) > 25:
            break
    if len(papers) > 25:
        break

# with open('data3.json', 'w') as f:
#     json.dump(papers, f)