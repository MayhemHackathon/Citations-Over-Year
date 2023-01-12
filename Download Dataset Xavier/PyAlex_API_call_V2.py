# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 04:27:21 2022

@author: xwtar
"""

import pyalex
from pyalex import Works, Authors, Venues, Institutions, Concepts
import json

# Need to pull cited_by_count and works_count from authorships
# Can pull data with Authors().search_filter(display_name="einstein").get()
# def Pull_Cited_By_Count:

# Need the count from referenced_works
# def Count_Referenced_Works:

# Need counts by year cumulative for five years after publication
# def Five_Cumulative_Years

pyalex.config.email = "xavier.tarr@gmail.com"

# pager = Works().search_filter(publication_year=2017,is_retracted=0 ).paginate(per_page=26)
# pager_2017 = Works().filter(publication_year=2017, is_retracted=False,
#                             is_paratext=False).paginate(per_page=200)
# pager_2016 = Works().filter(publication_year=2016, is_retracted=False,
#                             is_paratext=False).paginate(per_page=200)
# pager_2015 = Works().filter(publication_year=2015, is_retracted=False,
#                             is_paratext=False).paginate(per_page=200)
# pager_2014 = Works().filter(publication_year=2014, is_retracted=False,
#                             is_paratext=False).paginate(per_page=200)
# pager_2013 = Works().filter(publication_year=2013, is_retracted=False,
#                             is_paratext=False).paginate(per_page=200)

papers = []
paper_formatted = []

# for page in pager_2017:
#     for paper in page:
#         paper_formatted = [paper['id'], paper['doi'], paper['title'], paper['publication_year'], paper['host_venue'],
#                            paper['type'], paper['open_access'], paper['authorships'], paper['concepts'], paper['referenced_works'],
#                            paper['counts_by_year'], paper['abstract']]
#         papers.append(paper_formatted)
#         if len(papers) > 25:
#             break
#     if len(papers) > 25:
#         break


PAPERS_PER_YEAR = 10
properties_to_keep = ['id', 'doi', 'title', 'publication_year', 'host_venue',
                      'type', 'open_access', 'concepts', 'referenced_works',
                      'counts_by_year', 'abstract']


def get_data(year_start, year_end, primary_filter):
    papers_by_year = {}
    for year in range(year_start, year_end, 1):
        papers_by_year[year] = []
        journal = Works() \
            .filter(publication_year=year) \
            .filter(is_retracted=False, is_paratext=False) \
            .paginate(per_page=200)

        flag = False
        for page in journal:
            for paper in page:

                if len(papers_by_year[year]) > PAPERS_PER_YEAR:
                    flag = True
                if flag:
                    break

                new_paper = {}
                for property in properties_to_keep:
                    new_paper[property] = paper[property]

                # ------- transform some properties ------- 
                new_paper["referenced_works"] = len(
                    new_paper["referenced_works"])

                new_paper["counts_by_year"] = sorted(
                    new_paper["counts_by_year"], key=lambda x: x['year'])
                for index in range(1, len(new_paper["counts_by_year"])):
                    new_paper["counts_by_year"][index]["cited_by_count"] += new_paper["counts_by_year"][index-1]["cited_by_count"]

                # ------- transformation completed ------- 

                papers_by_year[year].append(new_paper)

            if flag:
                break
    return papers_by_year


papers_by_year = get_data(
    2010, 2015, {"is_retracted": False, "is_paratext": False})
# print(papers_by_year)

with open("sample.json", "w") as outfile:
    outfile.write(json.dumps(papers_by_year))
