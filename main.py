#!/usr/bin/python3

from re import search
from search_engine_parser import GoogleSearch
import sys


def get_search_results(query):
    search_args = (query, 1)
    gsearch = GoogleSearch()
    gresults = gsearch.search(*search_args)
    return gresults['title']


def words_in_sentence(sentence):
    return len(sentence.split(" "))

def main():
    query = sys.argv[1]
    search_results = list()
    raw_search_results = get_search_results(query)
    

    for raw_search_result in raw_search_results:
        raw_search_result_length = words_in_sentence(raw_search_result)

        if raw_search_result_length < 5:
            raw_search_results.remove(raw_search_result)
            
    print(raw_search_results[0])




if __name__=="__main__":
    main()