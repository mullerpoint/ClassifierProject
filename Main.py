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

import numpy as np          # Used For Statistics Functions
import pandas as pd         # Used to store data
import spacy                # Used to do named entity recognition



##########################################################
# Main
##########################################################


def main():
    # open the excel file and parse the first sheet to a dataframe
    xls_file = pd.ExcelFile("./Context_Extraction.xlsx")
    df = xls_file.parse('Final')

    print(df['text_heading'][0])  # DEBUG

    nlp = spacy.load('en')
    # doc = nlp('this is a test sentence typed in San Antonio by Gary')


    ner_list = []
    temp_int = 0  # DEBUG
    for row in df['text_heading']:
        tagged_str = nlp(row)
        ner_list.append(tagged_str)
        temp_int = temp_int + 1  # DEBUG
        print(temp_int)  # DEBUG

    df['ner_tags'] = ner_list






##########################################################
# Functions
##########################################################


if __name__ == '__main__':
    main()
