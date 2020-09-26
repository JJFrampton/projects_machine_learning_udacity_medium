import pandas as pd

def expand_multi_choice_category(dataframe, column, separator, concat=True):

    """---
    
    Expand Multiple Choice Categorical Variables
    
    Usage:
        Used to expand a categorical column that may contain multiple answers
        ie
        |favorite juice|   convert    |apple |orange |pear |
        |apple,orange  |     ===>     |1     |1      |0    |
        |pear,apple    |              |1     |0      |1    |
    
    Args:
        dataframe: pandas.DataFrame
            - the target dataframe
        column: string
            - the column to expand
        separator: string
            - the char(s) to split the string on
            ie ',' or ';'
        concat: bool
            - if true returns the concatinated frame
            - if false returns the series
            
    See:
        pd.concat([df[[0]], df[1].str.split(', ', expand=True)], axis=1)
        https://stackoverflow.com/questions/37600711/pandas-split-column-into-multiple-columns-by-comma

        pd.concat([df.drop('Issues', 1), df['Issues'].str.get_dummies(sep=",")], 1)
        https://stackoverflow.com/questions/57469676/python-one-hot-encoding-for-comma-separated-values
    """
    dummies = dataframe[column].str.get_dummies(sep=";")
    print("Expanded %s to %s boolean features" %(column, dummies.shape[1]))
    print(dummies.columns)
    print(dummies.head())
    if concat == False:
        return dummies
    else:
        return pd.concat([dataframe.drop(column, axis=1), dummies], axis=1)

def check_null_percent(dataframe, cutoff):
    """---
    
    Check null values in columns
    
    Returns a set of column names which have null values of $cutoff % or higher
    ie check_nulls(dataframe, 50)
        returns a set of columns where the percentage of nulls is 50% or higher
    
    Args:
        dataframe: Pandas.DataFrame
            The dataframe to work on
        cutoff: integer ( 0 - 100 )
            Percentage of null values
    """
    cutoff = cutoff / 100
    return set(dataframe.columns[dataframe.isnull().mean() > cutoff])
