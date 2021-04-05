def replace_regex(dataframe, list_regex, list_to_change, new_column, old_column):
    '''this function takes as input:
        dataframe = the name of the dataframe we are working on
        list_regex = a list of regex patterns we want to replace
        list_to_change = a list of strings we want to replace certain regex patterns with
        new_column = the name of the new column we want to create in the dataframe
        old_column = the old column that we will work on '''
    dataframe[new_column] = dataframe[old_column].str.lower().replace(list_regex, list_to_change, regex=True)
    return dataframe

def extract_regex(dataframe, new_column, old_column, regex_pattern):
    '''only extracts values that match the desired regex pattern, inputs into new column.
        Variables:
        dataframe = what is the dataframe you want to use
        new_colum = what is the name of the new column you want to create
        old_column = to what column will you be a pplying your function
        regex_pattern = What is the regex pattern that identifies all the values
        you want to encapsulate?
        '''
    dataframe[new_column] = dataframe[old_column].str.extract(regex_pattern, expand = False).fillna('')
    return dataframe

def sumnull(dataframe):
    ''' tells us the sum of all NaN type in a given dataframe'''
    return dataframe.isnull().sum()

def createindex(dataframe, column, top_number):
    '''Creates an index of the top number of values in a given column of a dataframe '''
    return dataframe[column].value_counts().head(top_number).index

