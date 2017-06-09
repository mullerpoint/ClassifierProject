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

import numpy as np                          # Used For Statistics Functions
import pandas as pd                         # Used to store data
from nltk.tag import pos_tag                # Used to tag words with their part of speech
from nltk.tokenize import word_tokenize     # Used to tokenize text down to words


##########################################################
# Main
##########################################################


def main():
    # open the excel file and parse the first sheet to a dataframe
    xls_file = pd.ExcelFile("./Context_Extraction.xlsx")
    df = xls_file.parse('Final')

    print(df.text_heading)  # DEBUG

    # Tokenize the text and save the list of tokens as a new column
    token_list = []
    for row in df['text_heading']:
        token_list.append(tokenize(row))
    df['tokens'] = token_list

    print(df['tokens'])  # DEBUG

    # Get the number of tokens in each row and save the number as a new column
    len_list = []
    for row in df['tokens']:
        len_list.append(len(row))
    df['text_length'] = len_list

    # Count verbs
    # df['verb_count'] = count_verbs(df['tokens'])

    # do clustering analysis
    # TODO

    print(df['text_length'])  # DEBUG

    # Make determination of Generic/Specific based on clusters and save as a column
    # TODO


##########################################################
# Functions
##########################################################


def tokenize(in_string):
    string_tagged = pos_tag(word_tokenize(in_string))
    return string_tagged


def count_verbs():
    # TODO
    return -1


if __name__ == '__main__':
    main()
