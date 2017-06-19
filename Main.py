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

import pandas as pd             # Used to store data
import spacy                    # Used to do named entity recognition


##########################################################
# Main
##########################################################

def main():
    # open the excel file and parse the first sheet to a dataframe
    xls_file = pd.ExcelFile("./Context_Extraction.xlsx")
    df = xls_file.parse('Final')

    # Load the spaCy python language processor using the english library/model
    nlp = spacy.load('en_core_web_md')  # Big processing model
    # nlp = spacy.load('en')            # Default processing model

    # used to store the list of location bool results
    location_list = []

    temp_int = 0  # DEBUG

    # used to detect if a location has already been found in the sentence
    # and prevent multiple successes from being appended to the location_list
    location_found = False

    for row in df['text_heading']:

        # perform NER on the row using the model specified above
        tagged_str = nlp(row)

        # For each of the tagged entities in the sentence iterate through them
        # for the complete list of entity types see
        # https://spacy.io/docs/usage/entity-recognition#entity-types
        for ent in tagged_str.ents:

            # If the entity is tagged with GPE (countries, cities, states)
            # append a '1' to the list and set the location found to true
            if ent.label_ == 'GPE':
                if not location_found:
                    location_list.append(1)
                    location_found = True
                    print('1')  # DEBUG
                # if
            # if

            # If the entity is tagged with LOC (non-GPE locations, mountain ranges, bodies of water)
            # append a '1' to the list and set the location found to true
            elif ent.label_ == 'LOC':
                if not location_found:
                    location_list.append(1)
                    location_found = True
                    print('1')  # DEBUG
                # if
            # if

        # In case no location was found after iterating through all entities in the sentence append a '0' to the list
        if not location_found:
            location_list.append(0)
            print('0')  # DEBUG
        # if

        # reset location bool to false before starting the next row
        location_found = False

        # DEBUG counter for progress monitoring
        temp_int = temp_int + 1  # DEBUG
        print(temp_int)  # DEBUG
    # for

    # create a column in the data frame to contain the location_list
    df['location_bool'] = location_list

    # output the results
    print(df[['location_bool', 'text_heading']])


##########################################################
# Functions
##########################################################

# call main() when starting this file
if __name__ == '__main__':
    main()
