# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 04:27:21 2022

@author: xwtar
"""

import pyalex
from pyalex import Works, Authors, Venues, Institutions, Concepts
import json

#Need the count from referenced_works
# def Count_Referenced_Works:
# 
# Input: List of string IDs
# Output num length of List 
def Count_Referenced_Works(referenced_Works):
    return len(referenced_Works)


#Need counts by year cumulative for five years after publication
# def Five_Cumulative_Years
#input -> countsByYear (list of dictionaries, key of year and countsByYear ordered by renency
#output <- list of countsByYear nums, ordered from pubYear to five years out
def Five_Cumulative_Years(countsByYear, pubYear):
    cumulativeYears = []
    CURRENT_YEAR = 2022
    totalCounts = 0
    if len(countsByYear) < CURRENT_YEAR - pubYear:
        yearTracker = pubYear
        for set in countsByYear[len(countsByYear):0:-1]:
            if set.get('year') == yearTracker:
                totalCounts += set.get('cited_by_count')
            cumulativeYears.append(totalCounts)
            yearTracker = yearTracker+1
    else:
        for set in countsByYear[len(countsByYear):0:-1]:
            totalCounts += set.get('cited_by_count')
            cumulativeYears.append(totalCounts)
    return cumulativeYears[0:5]

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
        if paper['counts_by_year'][-1]['year'] >= paper['publication_year']:
            count_references = Count_Referenced_Works(paper['referenced_works'])
            count_cumulative_by_year = Five_Cumulative_Years(paper['counts_by_year'], paper['publication_year'])
            paper_formatted = [paper['id'], paper['doi'],paper['title'],paper['publication_year'],paper['host_venue'],
                      paper['type'],paper['open_access'],paper['concepts'],count_references,
                      count_cumulative_by_year,paper['abstract']]
            papers.append(paper_formatted)
        if len(papers) > 10000:
            break
    if len(papers) > 10000:
        break

for page in pager_2016:
    for paper in page:
        if paper['counts_by_year'][-1]['year'] >= paper['publication_year']:
            count_references = Count_Referenced_Works(paper['referenced_works'])
            count_cumulative_by_year = Five_Cumulative_Years(paper['counts_by_year'], paper['publication_year'])
            paper_formatted = [paper['id'], paper['doi'],paper['title'],paper['publication_year'],paper['host_venue'],
                      paper['type'],paper['open_access'],paper['concepts'],count_references,
                      count_cumulative_by_year,paper['abstract']]
            papers.append(paper_formatted)
        if len(papers) > 20000:
            break
    if len(papers) > 20000:
        break

for page in pager_2015:
    for paper in page:
        if paper['counts_by_year'][-1]['year'] >= paper['publication_year']:
            count_references = Count_Referenced_Works(paper['referenced_works'])
            count_cumulative_by_year = Five_Cumulative_Years(paper['counts_by_year'], paper['publication_year'])
            paper_formatted = [paper['id'], paper['doi'],paper['title'],paper['publication_year'],paper['host_venue'],
                      paper['type'],paper['open_access'],paper['concepts'],count_references,
                      count_cumulative_by_year,paper['abstract']]
            papers.append(paper_formatted)
        if len(papers) > 30000:
            break
    if len(papers) > 30000:
        break
    
for page in pager_2014:
    for paper in page:
        if paper['counts_by_year'][-1]['year'] >= paper['publication_year']:
            count_references = Count_Referenced_Works(paper['referenced_works'])
            count_cumulative_by_year = Five_Cumulative_Years(paper['counts_by_year'], paper['publication_year'])
            paper_formatted = [paper['id'], paper['doi'],paper['title'],paper['publication_year'],paper['host_venue'],
                      paper['type'],paper['open_access'],paper['concepts'],count_references,
                      count_cumulative_by_year,paper['abstract']]
            papers.append(paper_formatted)
        if len(papers) > 40000:
            break
    if len(papers) > 40000:
        break
    
for page in pager_2013:
    for paper in page:
        if paper['counts_by_year'][-1]['year'] >= paper['publication_year']:
            count_references = Count_Referenced_Works(paper['referenced_works'])
            count_cumulative_by_year = Five_Cumulative_Years(paper['counts_by_year'], paper['publication_year'])
            paper_formatted = [paper['id'], paper['doi'],paper['title'],paper['publication_year'],paper['host_venue'],
                      paper['type'],paper['open_access'],paper['concepts'],count_references,
                      count_cumulative_by_year,paper['abstract']]
            papers.append(paper_formatted)
        if len(papers) > 50000:
            break
    if len(papers) > 50000:
        break

# with open('AI_data_bigger.json', 'w') as f:
#     json.dump(papers, f)
    
with open("sample.json", "w") as outfile:
    new_data = []
    for element in papers:
        dct= {}
        dct['ID'], dct['DOI'], dct['Title'], dct['publication_year'], dct['HostVenue'], dct['Type'], dct['OpenAccess'], dct['Concepts'], dct['ReferencedWork'], dct['CitedByYear'] , dct['Abstract'] = element[0], element[1], element[2], element[3], element[4], element[5], element[6], element[7], element[8], element[9], element[10]
        new_data.append(dct)
    json.dump(new_data, outfile)