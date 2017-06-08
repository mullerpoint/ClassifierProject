#!/usr/bin/env python

##########################################################
#
# Summer 2017 Project 1
# Gary Muller
# Dr Rohit Valecha
# University of Texas at San Antonio
# A project to classify text as specific or generic
#
##########################################################

##########################################################
# Imports
##########################################################

import numpy as np                                                  # Used For Statistics Functions
import pandas as pd                                                 # Used to store data
from nltk.tag import pos_tag_sents

##########################################################
# Main
##########################################################
def main():
    # open the excel file and parse the first sheet to a dataframe
    xls_file = pd.ExcelFile("./Context_Extraction.xlsx")
    df = xls_file.parse('Final')

    print(df.text_heading) #DEBUG

    # Create a clean version of the text with all extra symbols stripped out
    df['cleantext'] = clean_text(df['text_heading'])

    # tokenize the clean text
    df['tokens'] = tokenize(df['cleantext'])

    # get length
    df['text_length'] = len(df['cleantext'])

    # Count verbs
    df['verb_count'] = count_verbs(df['tokens'])

    #Do clustering analysis
    #TODO


def clean_text(in_string):
    #TODO
    return -1


def tokenize(in_string):
    string_tagged = pos_tag_sents(in_string)
    return string_tagged


def count_verbs():
    #TODO
    return -1


if __name__ == '__main__':
    main()
